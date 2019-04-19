import pickle
from PIL import Image
import leargist 
import os
def classi(img_file):
	print (img_file)
	file = open("clf_dump",'rb')
	clf = pickle.load(file)
	Image.Image.tostring = Image.Image.tobytes
	im = Image.open(img_file)
	im1 = im.resize((64,64),Image.ANTIALIAS);
	des = leargist.color_gist(im1)
	X = des[0:320]
	y_predict = clf.predict(X)
	list_fams = os.listdir("/media/term/MISC/Malware/Malimg/malimg_dataset_imgs/")
	return list_fams[int(y_predict[0])]
