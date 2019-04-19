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

net = cv2.dnn.readNetFromCaffe(args["prototxt"], args["model"])
vs = VideoStream(src=0).start()


more = 'y'

X = []
y = []

newAdded = False

while(more == 'y'):

	more = input("Do you want to add more people(y/n)?: ")
	print('\n\n\n')
	if(more != 'y'):
		break;

	newAdded = True
	print('Adding new person')
	print('---------------------')
	name = input("Enter name of this person:")

	sql = "INSERT INTO employees(name) VALUES ('" + name + "')"
	val = (name)
	mycursor.execute(sql)
	mydb.commit();

	count = 0
	while(count != 5):
		frame = vs.read()
		frame = imutils.resize(frame)

		(h, w) = frame.shape[:2]
		blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0,
			(300, 300), (104.0, 177.0, 123.0))
		net.setInput(blob)
		detections = net.forward()

		for i in range(0, detections.shape[2]):
			confidence = detections[0, 0, i, 2]
			if confidence < args["confidence"]:
				continue

			rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
			saveImg = Image.fromarray(rgb)
			saveImg.save(os.getcwd()+'\\images2\\'+name+'-'+str(count)+'.jpeg')
			count += 1
			print("Done %s/5" %count)

			cv2.imshow("Frame", frame)
			key = cv2.waitKey(1) & 0xFF



from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(os.getcwd()+'\\images2') if isfile(join(os.getcwd()+'\\images2', f))]

if(not newAdded):
	data = pickle.loads(open(os.getcwd()+'\\data.pickle', "rb").read())
	X = data['X']
	y = data['y']	

else:
	for file in onlyfiles:
		pos = file.find('-')
		name = file[:pos]
		print(name)

		imgg2 = cv2.imread(os.getcwd()+'\\images2\\'+file)
		imgg = cv2.cvtColor(imgg2, cv2.COLOR_BGR2RGB)
		boxes = face_recognition.face_locations(imgg,
			model="hog")
		encodings = face_recognition.face_encodings(imgg, boxes)
		for encoding in encodings:
			X.append(encoding)
			y.append(name)
	
data = {"X": X, "y": y}
f = open(os.getcwd()+'\\data.pickle', "wb")
f.write(pickle.dumps(data))
f.close()	

print(X)
print(y)


cv2.destroyAllWindows()

c = 0
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
		mycursor.execute("SELECT * FROM mini WHERE name='" +predictedName+ "' ORDER BY id DESC LIMIT 1")
		myresult = mycursor.fetchall()
		allowSave = True
		for x in myresult:
			print(x[2])
			if(x[2] == "In"):
				allowSave = False
				print("REJECTED " + predictedName)
				print(c)
				c += 1
		if(allowSave):
			sql = "INSERT INTO mini(name, type, time) VALUES (%s, %s, %s)"
			curentTime = str(datetime.datetime.now())
			predictedName2 = str(predictedName)
			val = (predictedName2, "In", str(curentTime))
			mycursor.execute(sql, val)
			print("SAVED " + predictedName)
			mydb.commit();

	
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
 
	if key == ord("q"):
		break

cv2.destroyAllWindows()
vs.stop()