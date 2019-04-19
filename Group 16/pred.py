import numpy as np 
from keras.models import model_from_json
import operator
import cv2
import sys,os
import time
from pynput.keyboard import Key, Controller
class Pred:
	def pred():
		c=0
		# Loading the model
		json_file = open("model-bw.json", "r")
		model_json = json_file.read()
		json_file.close()
		loaded_model = model_from_json(model_json)
		# load weights into new model
		loaded_model.load_weights("model-bw.h5")
		print("Loaded model from disk")

		cap=cv2.VideoCapture(0)

		categories={
			0:'A',
			1:'B',
			2:'C',
			3:'D',
			4:'E',
			5:'F',
			6:'G',
			7:'H',
			8:'I',
			9:'J',
			10:'K',
			11:'L',
			12:'M',
			13:'N',
			14:'O',
			15:'P',
			16:'Q',
			17:'R',
			18:'S',
			19:'T',
			20:'U',
			21:'V',
			22:'W',
			23:'X',
			24:'Y',
			25:'SPACE',
			26:'DEL',
			27:'BLANK',
			}
		count=0
		while True:

			_, frame = cap.read()

			frame = cv2.flip(frame,1)
			# Coordinates of the ROI
			x1 = int(0.5*frame.shape[1])
			y1 = 80
			x2 = x1+256
			y2 = y1+256

			
			# The increment/decrement by 1 is to compensate for the bounding box
			cv2.rectangle(frame, (x1-1, y1-1), (x2+1, y2+1), (255,0,0) ,1)
			# Extracting the ROI
			roi1 = frame[y1:y2, x1:x2]
			cv2.imshow("Frame", frame)
			#roi = cv2.resize(roi, (64, 64))

			lower_skin = np.array([0,30,70], dtype=np.uint8)
			upper_skin = np.array([20,255,255], dtype=np.uint8)
			kernel = np.ones((5,5),np.uint8)
			
			#capturing the image!
			#_, roi = cv2.threshold(roi, 150, 255, cv2.THRESH_BINARY)
			#cv2.imshow("ROI", roi)
			roi2 = cv2.cvtColor(roi1, cv2.COLOR_BGR2HSV)
				
			#extract skin colur imagw  
			roi2 = cv2.inRange(roi2, lower_skin, upper_skin)
			cv2.imshow("ROI", roi2)

			roi =cv2.bitwise_and(roi1,roi1,mask=roi2)
			roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
			cv2.imshow("Col", roi)   
			roi=cv2.resize(roi,(128,128))
			
			
			#roi2 = cv2.morphologyEx(roi, cv2.MORPH_CLOSE, kernel)
			#cv2.imshow("Close", roi)
			
			#roi2 =cv2.bitwise_and(roi1,roi1,mask=roi2)
			#roi2 = cv2.cvtColor(roi2, cv2.COLOR_BGR2GRAY)
			#cv2.imshow("ColN", roi2)

			result = loaded_model.predict(roi.reshape(1, 128, 128, 1))
			prediction = {'A': result[0][0], 
						  'B': result[0][1], 
						  'C': result[0][2],
						  'D': result[0][3],
						  'E': result[0][4],
						  'F': result[0][5],
						  'G': result[0][6],
						  'H': result[0][7],
						  'I': result[0][8],
						  'J': result[0][9],
						  'K': result[0][10],
						  'L': result[0][11],
						  'M': result[0][12],
						  'N': result[0][13],
						  'O': result[0][14],
						  'P': result[0][15],
						  'Q': result[0][16],
						  'R': result[0][17],
						  'S': result[0][18],
						  'T': result[0][19],
						  'U': result[0][20],
						  'V': result[0][21],
						  'W': result[0][22],
						  'X': result[0][23],
						  'Y': result[0][24],
						  'SPACE': result[0][25],
						  'DEL': result[0][26],
						  'BLANK': result[0][27]
						  }
			# Sorting based on top prediction
			prediction = sorted(prediction.items(), key=operator.itemgetter(1), reverse=True)
			
			# Displaying the predictions
			cv2.putText(frame, prediction[0][0], (10, 120), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)    
			cv2.imshow("Frame", frame)
			
			if count == 0:
				temp=prediction[0][0]
			if prediction[0][0]==temp:
				count+=1
			else:	
				temp=prediction[0][0]
				count=0

			if count==50 and temp=='SPACE':
				keyboard.press(Key.space)
				keyboard.release(Key.space)
				count=0
			elif count==50 and temp=='DEL':
				keyboard.press(Key.backspace)
				keyboard.release(Key.backspace)
				count=0
			elif count==50 and temp!='BLANK':
				keyboard.press(temp)
				keyboard.release(temp)
				count=0

			interrupt = cv2.waitKey(20)
			if interrupt & 0xFF == 27: # esc key
				break;
				
			if c==0:
				keyboard = Controller()
				open('op.txt','a').close()
				os.startfile('op.txt')
				time.sleep(2)
				c=1
		cap.release()
		cv2.destroyAllWindows()