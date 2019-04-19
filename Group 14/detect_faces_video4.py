# USAGE
# python detect_faces_video.py --prototxt deploy.prototxt.txt --model res10_300x300_ssd_iter_140000.caffemodel

# import the necessary packages
from imutils.video import VideoStream
import numpy as np
import argparse
import imutils
import time
import cv2
from PIL import Image
import os

import mysql.connector
import datetime

import face_recognition
import pickle
import operator

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="test",
  autocommit=True
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM mini")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)





ap = argparse.ArgumentParser()
ap.add_argument("-p", "--prototxt", required=False, default='deploy.prototxt.txt',
	help="path to Caffe 'deploy' prototxt file")
ap.add_argument("-m", "--model", required=False, default='res10_300x300_ssd_iter_140000.caffemodel',
	help="path to Caffe pre-trained model")
ap.add_argument("-c", "--confidence", type=float, default=0.5,
	help="minimum probability to filter weak detections")
args = vars(ap.parse_args())

vs = VideoStream(src=1).start()





from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(os.getcwd()+'\\images2') if isfile(join(os.getcwd()+'\\images2', f))]

data = pickle.loads(open(os.getcwd()+'\\data.pickle', "rb").read())
X = data['X']
y = data['y']


print(X)
print(y)


cv2.destroyAllWindows()


while True:

	frame = vs.read()

	rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	boxes = face_recognition.face_locations(rgb,
		model="hog")
	encodings = face_recognition.face_encodings(rgb, boxes)
		
	for encoding in encodings:
		matches = face_recognition.compare_faces(X,
			encoding, tolerance=0.41)
		matchCount = {}
		for inx, m in enumerate(matches):
			if(m):
				if(y[inx] not in matchCount):
					matchCount[y[inx]] = 1
				else:
					matchCount[y[inx]] += 1
		print(matchCount)
		if(not bool(matchCount)):
			continue
		predictedName = max(matchCount.items(), key=operator.itemgetter(1))[0]
		mycursor = mydb.cursor()
		mycursor.execute("SELECT type FROM mini WHERE name='" +predictedName+ "' ORDER BY id DESC LIMIT 1")
		myresult = mycursor.fetchall()
		allowSave = True
		for x in myresult:
			print(x[0])
			if(x[0] == "Out"):
				allowSave = False
				print("REJECTED " + predictedName)
		if(allowSave):
			sql = "INSERT INTO mini(name, type, time) VALUES (%s, %s, %s)"
			curentTime = str(datetime.datetime.now())
			predictedName2 = str(predictedName)
			val = (predictedName2, "Out", str(curentTime))
			mycursor.execute(sql, val)
			print("SAVED " + predictedName)
			mydb.commit();


	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
 
	if key == ord("q"):
		break

cv2.destroyAllWindows()
vs.stop()