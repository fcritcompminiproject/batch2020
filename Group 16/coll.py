import cv2
import numpy as np
import os
class Coll:
	def show():
		while True:
			img = cv2.imread('sign.jpg')
			cv2.imshow('sign',img)
			interrupt = cv2.waitKey(10)
			if interrupt & 0xFF == 27:
				break
		cv2.destroyAllWindows()
	def coll(mode):
		# Create the directory structure
		if not os.path.exists("data"):
			os.makedirs("data")
			os.makedirs("data/train")
			os.makedirs("data/test")
			os.makedirs("data/train/A")
			os.makedirs("data/train/B")
			os.makedirs("data/train/C")
			os.makedirs("data/train/D")
			os.makedirs("data/train/E")
			os.makedirs("data/train/F")
			os.makedirs("data/test/A")
			os.makedirs("data/test/B")
			os.makedirs("data/test/C")
			os.makedirs("data/test/D")
			os.makedirs("data/test/E")
			os.makedirs("data/test/F")
			

		# Train or test 
		directory = 'data/'+mode

		cap = cv2.VideoCapture(0)

		# define range of skin color in HSV
		lower_skin = np.array([0,30,70], dtype=np.uint8)
		upper_skin = np.array([20,255,255], dtype=np.uint8)
		kernel = np.ones((5,5),np.uint8)

		while True:
			_, frame = cap.read()
			
			frame = cv2.flip(frame, 1)
			
			# Getting count of existing images
			count = {'a': len(os.listdir(directory+"/A")),
					 'b': len(os.listdir(directory+"/B")),
					 'c': len(os.listdir(directory+"/C")),
					 'd': len(os.listdir(directory+"/D")),
					 'e': len(os.listdir(directory+"/E")),
					 'f': len(os.listdir(directory+"/F")),
					 'g':len(os.listdir(directory+"/G")),
					 'h':len(os.listdir(directory+"/H")),
					 'i':len(os.listdir(directory+"/I")),
					 'j':len(os.listdir(directory+"/J")),
					 'k':len(os.listdir(directory+"/K")),
					 'l':len(os.listdir(directory+"/L")),
					 'm':len(os.listdir(directory+"/M")),
					 'n':len(os.listdir(directory+"/N")),
					 'o':len(os.listdir(directory+"/O")),
					 'p':len(os.listdir(directory+"/P")),
					 'q':len(os.listdir(directory+"/Q")),
					 'r':len(os.listdir(directory+"/R")),
					 's':len(os.listdir(directory+"/S")),
					 't':len(os.listdir(directory+"/T")),
					 'u':len(os.listdir(directory+"/U")),
					 'v':len(os.listdir(directory+"/V")),
					 'w':len(os.listdir(directory+"/W")),
					 'x':len(os.listdir(directory+"/X")),
					 'y':len(os.listdir(directory+"/Y")),
					 'space':len(os.listdir(directory+"/SPACE")),
					 'del':len(os.listdir(directory+"/DEL")),
					 'blank':len(os.listdir(directory+"/BLANK"))
					 }
			
			# Printing the count in each set to the screen
			cv2.putText(frame, "MODE : "+mode, (10, 50), cv2.FONT_HERSHEY_PLAIN, 0.75, (0,255,255), 1)
			cv2.putText(frame, "IMAGE COUNT", (10, 100), cv2.FONT_HERSHEY_PLAIN, 0.75, (0,255,255), 1)
			cv2.putText(frame, "A : "+str(count['a']), (10, 120), cv2.FONT_HERSHEY_PLAIN, 0.75, (0,255,255), 1)
			cv2.putText(frame, "B : "+str(count['b']), (10, 130), cv2.FONT_HERSHEY_PLAIN, 0.75, (0,255,255), 1)
			cv2.putText(frame, "C : "+str(count['c']), (10, 140), cv2.FONT_HERSHEY_PLAIN, 0.75, (0,255,255), 1)
			cv2.putText(frame, "D : "+str(count['d']), (10, 150), cv2.FONT_HERSHEY_PLAIN, 0.75, (0,255,255), 1)
			cv2.putText(frame, "E : "+str(count['e']), (10, 160), cv2.FONT_HERSHEY_PLAIN, 0.75, (0,255,255), 1)
			cv2.putText(frame, "F : "+str(count['f']), (10, 170), cv2.FONT_HERSHEY_PLAIN, 0.75, (0,255,255), 1)
			cv2.putText(frame, "G : "+str(count['g']), (10, 180), cv2.FONT_HERSHEY_PLAIN, 0.75, (0,255,255), 1)
			cv2.putText(frame, "H : "+str(count['h']), (10, 190), cv2.FONT_HERSHEY_PLAIN, 0.75, (0,255,255), 1)
			cv2.putText(frame, "I : "+str(count['i']), (10, 200), cv2.FONT_HERSHEY_PLAIN, 0.75, (0,255,255), 1)
			cv2.putText(frame, "J : "+str(count['j']), (10, 210), cv2.FONT_HERSHEY_PLAIN, 0.75, (0,255,255), 1)
			cv2.putText(frame, "K : "+str(count['k']), (10, 220), cv2.FONT_HERSHEY_PLAIN, 0.75, (0,255,255), 1)
			cv2.putText(frame, "L : "+str(count['l']), (10, 230), cv2.FONT_HERSHEY_PLAIN, 0.75, (0,255,255), 1)
			cv2.putText(frame, "M : "+str(count['m']), (10, 240), cv2.FONT_HERSHEY_PLAIN, 0.75, (0,255,255), 1)
			cv2.putText(frame, "N : "+str(count['n']), (10, 250), cv2.FONT_HERSHEY_PLAIN, 0.75, (0,255,255), 1)
			cv2.putText(frame, "O : "+str(count['o']), (10, 260), cv2.FONT_HERSHEY_PLAIN, 0.75, (0,255,255), 1)
			cv2.putText(frame, "P : "+str(count['p']), (10, 270), cv2.FONT_HERSHEY_PLAIN, 0.75, (0,255,255), 1)
			cv2.putText(frame, "Q : "+str(count['q']), (10, 280), cv2.FONT_HERSHEY_PLAIN, 0.75, (0,255,255), 1)
			cv2.putText(frame, "R : "+str(count['r']), (10, 290), cv2.FONT_HERSHEY_PLAIN, 0.75, (0,255,255), 1)
			cv2.putText(frame, "S : "+str(count['s']), (10, 300), cv2.FONT_HERSHEY_PLAIN, 0.75, (0,255,255), 1)
			cv2.putText(frame, "T : "+str(count['t']), (10, 310), cv2.FONT_HERSHEY_PLAIN, 0.75, (0,255,255), 1)
			cv2.putText(frame, "U : "+str(count['u']), (10, 320), cv2.FONT_HERSHEY_PLAIN, 0.75, (0,255,255), 1)
			cv2.putText(frame, "V : "+str(count['v']), (10, 330), cv2.FONT_HERSHEY_PLAIN, 0.75, (0,255,255), 1)
			cv2.putText(frame, "W : "+str(count['w']), (10, 350), cv2.FONT_HERSHEY_PLAIN, 0.75, (0,255,255), 1)
			cv2.putText(frame, "X : "+str(count['x']), (10, 360), cv2.FONT_HERSHEY_PLAIN, 0.75, (0,255,255), 1)
			cv2.putText(frame, "Y : "+str(count['y']), (10, 370), cv2.FONT_HERSHEY_PLAIN, 0.75, (0,255,255), 1)
			cv2.putText(frame, "SPACE  : "+str(count['space']), (10, 390), cv2.FONT_HERSHEY_PLAIN, 0.75, (0,255,255), 1)
			cv2.putText(frame, "DEL  : "+str(count['del']), (10, 400), cv2.FONT_HERSHEY_PLAIN, 0.75, (0,255,255), 1)
			cv2.putText(frame, "BLANK  : "+str(count['blank']), (10, 410), cv2.FONT_HERSHEY_PLAIN, 0.75, (0,255,255), 1)
			
			# Coordinates of the ROI
			x1 = int(0.5*frame.shape[1])
			y1 = 80
			x2 = x1+256
			y2 = y1+256

			
			cv2.rectangle(frame, (x1-1, y1-1), (x2+1, y2+1), (255,0,0) ,1)
			# Extracting the ROI
			roi1 = frame[y1:y2, x1:x2]
			cv2.imshow("Frame", frame)
			#roi = cv2.resize(roi, (64, 64))
			
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
			
			interrupt = cv2.waitKey(10)
			if interrupt & 0xFF == 27:
				break
			if interrupt & 0xFF == ord('A'):
				cv2.imwrite(directory+'/A/'+str(count['a'])+'.jpg', roi)
			if interrupt & 0xFF == ord('B'):
				cv2.imwrite(directory+'/B/'+str(count['b'])+'.jpg', roi)
			if interrupt & 0xFF == ord('C'):
				cv2.imwrite(directory+'/C/'+str(count['c'])+'.jpg', roi)
			if interrupt & 0xFF == ord('D'):
				cv2.imwrite(directory+'/D/'+str(count['d'])+'.jpg', roi)
			if interrupt & 0xFF == ord('E'):
				cv2.imwrite(directory+'/E/'+str(count['e'])+'.jpg', roi)
			if interrupt & 0xFF == ord('F'):
				cv2.imwrite(directory+'/F/'+str(count['f'])+'.jpg', roi)
			if interrupt & 0xFF == ord('G'):
				cv2.imwrite(directory+'/G/'+str(count['g'])+'.jpg', roi)
			if interrupt & 0xFF == ord('H'):
				cv2.imwrite(directory+'/H/'+str(count['h'])+'.jpg', roi)
			if interrupt & 0xFF == ord('I'):
				cv2.imwrite(directory+'/I/'+str(count['i'])+'.jpg', roi)
			if interrupt & 0xFF == ord('J'):
				cv2.imwrite(directory+'/J/'+str(count['j'])+'.jpg', roi)
			if interrupt & 0xFF == ord('K'):
				cv2.imwrite(directory+'/K/'+str(count['k'])+'.jpg', roi)
			if interrupt & 0xFF == ord('L'):
				cv2.imwrite(directory+'/L/'+str(count['l'])+'.jpg', roi)
			if interrupt & 0xFF == ord('M'):
				cv2.imwrite(directory+'/M/'+str(count['m'])+'.jpg', roi)
			if interrupt & 0xFF == ord('N'):
				cv2.imwrite(directory+'/N/'+str(count['n'])+'.jpg', roi)
			if interrupt & 0xFF == ord('O'):
				cv2.imwrite(directory+'/O/'+str(count['o'])+'.jpg', roi)
			if interrupt & 0xFF == ord('P'):
				cv2.imwrite(directory+'/P/'+str(count['p'])+'.jpg', roi)
			if interrupt & 0xFF == ord('Q'):
				cv2.imwrite(directory+'/Q/'+str(count['q'])+'.jpg', roi)
			if interrupt & 0xFF == ord('R'):
				cv2.imwrite(directory+'/R/'+str(count['r'])+'.jpg', roi)
			if interrupt & 0xFF == ord('S'):
				cv2.imwrite(directory+'/S/'+str(count['s'])+'.jpg', roi)
			if interrupt & 0xFF == ord('T'):
				cv2.imwrite(directory+'/T/'+str(count['t'])+'.jpg', roi)
			if interrupt & 0xFF == ord('U'):
				cv2.imwrite(directory+'/U/'+str(count['u'])+'.jpg', roi)
			if interrupt & 0xFF == ord('V'):
				cv2.imwrite(directory+'/V/'+str(count['v'])+'.jpg', roi)
			if interrupt & 0xFF == ord('W'):
				cv2.imwrite(directory+'/W/'+str(count['w'])+'.jpg', roi)
			if interrupt & 0xFF == ord('X'):
				cv2.imwrite(directory+'/X/'+str(count['x'])+'.jpg', roi)
			if interrupt & 0xFF == ord('Y'):
				cv2.imwrite(directory+'/Y/'+str(count['y'])+'.jpg', roi)
			if interrupt & 0xFF == 8:
				cv2.imwrite(directory+'/DEL/'+str(count['del'])+'.jpg', roi)
			if interrupt & 0xFF == 32:
				cv2.imwrite(directory+'/SPACE/'+str(count['space'])+'.jpg', roi)
			if interrupt & 0xFF == 9 :
				cv2.imwrite(directory+'/BLANK/'+str(count['blank'])+'.jpg', roi)

			
		cap.release()

		cv2.destroyAllWindows()