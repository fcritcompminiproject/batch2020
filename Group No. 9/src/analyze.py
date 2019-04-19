from __future__ import division
from __future__ import print_function

import sys
import math
import pickle
import copy
import numpy as np
import cv2
import matplotlib.pyplot as plt
from DataLoader import Batch
from Model import Model, DecoderType
from SamplePreprocessor import preprocess


class Constants:
	"filenames and paths to data"
	fnCharList = '../model/charList.txt'
	fnAnalyze = '../data/analyze.png'
	fnPixelRelevance = '../data/pixelRelevance.npy'
	fnTranslationInvariance = '../data/translationInvariance.npy'
	fnTranslationInvarianceTexts = '../data/translationInvarianceTexts.pickle'
	gtText = 'are'
	distribution = 'histogram' 


def odds(val):
	return val / (1 - val)


def weightOfEvidence(origProb, margProb):
	return math.log2(odds(origProb)) - math.log2(odds(margProb))
	
	
def analyzePixelRelevance():
	"simplified implementation of paper: Zintgraf et al - Visualizing Deep Neural Network Decisions: Prediction Difference Analysis"
	
	
	model = Model(open(Constants.fnCharList).read(), DecoderType.BestPath, mustRestore=True)
	
	
	img = cv2.imread(Constants.fnAnalyze, cv2.IMREAD_GRAYSCALE)
	(w, h) = img.shape
	assert Model.imgSize[1] == w
	

	batch = Batch([Constants.gtText], [preprocess(img, Model.imgSize)])
	(_, probs) = model.inferBatch(batch, calcProbability=True, probabilityOfGT=True)
	origProb = probs[0]
	
	grayValues = [0, 63, 127, 191, 255]
	if Constants.distribution == 'histogram':
		bins = [0, 31, 95, 159, 223, 255]
		(hist, _) = np.histogram(img, bins=bins)
		pixelProb = hist / sum(hist)
	elif Constants.distribution == 'uniform':
		pixelProb = [1.0 / len(grayValues) for _ in grayValues]
	else:
		raise Exception('unknown value for Constants.distribution')
	

	pixelRelevance = np.zeros(img.shape, np.float32)
	for x in range(w):
		for y in range(h):
			
			imgsMarginalized = []
			for g in grayValues:
				imgChanged = copy.deepcopy(img)
				imgChanged[x, y] = g
				imgsMarginalized.append(preprocess(imgChanged, Model.imgSize))

			batch = Batch([Constants.gtText]*len(imgsMarginalized), imgsMarginalized)
			
			(_, probs) = model.inferBatch(batch, calcProbability=True, probabilityOfGT=True)
			
			margProb = sum([probs[i] * pixelProb[i] for i in range(len(grayValues))])
			
			pixelRelevance[x, y] = weightOfEvidence(origProb, margProb)
			
			print(x, y, pixelRelevance[x, y], origProb, margProb)
			
	np.save(Constants.fnPixelRelevance, pixelRelevance)


def analyzeTranslationInvariance():
	model = Model(open(Constants.fnCharList).read(), DecoderType.BestPath, mustRestore=True)
	
	img = cv2.imread(Constants.fnAnalyze, cv2.IMREAD_GRAYSCALE)
	(w, h) = img.shape
	assert Model.imgSize[1] == w
	
	imgList = []
	for dy in range(Model.imgSize[0]-h+1):
		targetImg = np.ones((Model.imgSize[1], Model.imgSize[0])) * 255
		targetImg[:,dy:h+dy] = img
		imgList.append(preprocess(targetImg, Model.imgSize))
	
	batch = Batch([Constants.gtText]*len(imgList), imgList)
	
	(texts, probs) = model.inferBatch(batch, calcProbability=True, probabilityOfGT=True)
	
	f = open(Constants.fnTranslationInvarianceTexts, 'wb')
	pickle.dump(texts, f)
	f.close()
	np.save(Constants.fnTranslationInvariance, probs)


def showResults():
	pixelRelevance = np.load(Constants.fnPixelRelevance)
	plt.figure('Pixel relevance')
	
	plt.imshow(pixelRelevance, cmap=plt.cm.jet, vmin=-0.25, vmax=0.25)
	plt.colorbar()
	
	img = cv2.imread(Constants.fnAnalyze, cv2.IMREAD_GRAYSCALE)
	plt.imshow(img, cmap=plt.cm.gray, alpha=.4)
	

	probs = np.load(Constants.fnTranslationInvariance)
	f = open(Constants.fnTranslationInvarianceTexts, 'rb')
	texts = pickle.load(f)
	texts = ['%d:'%i + texts[i] for i in range(len(texts))]
	f.close()
	
	plt.figure('Translation invariance')
	
	plt.plot(probs, 'o-')
	plt.xticks(np.arange(len(texts)), texts, rotation='vertical')
	plt.xlabel('horizontal translation and best path')
	plt.ylabel('text probability of "%s"'%Constants.gtText)
	
	plt.show()


if __name__ == '__main__':
	if len(sys.argv)>1:
		if sys.argv[1]=='--relevance':
			print('Analyze pixel relevance')
			analyzePixelRelevance()
		elif sys.argv[1]=='--invariance':
			print('Analyze translation invariance')
			analyzeTranslationInvariance()
	else:
		print('Show results')
		showResults()

