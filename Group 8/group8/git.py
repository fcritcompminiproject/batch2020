import cv2


cap = cv2.VideoCapture(0)

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

while(True):
	# Capture frame-by-frame
    ret, frame = cap.read()

	# Our operations on the frame come here
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30, 30))

    print("Found {0} faces!".format(len(faces)))
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (54, 87, 999), 2)
    #print(faces)
    if len(faces)==2:
        x1,y1,w1,h1=faces[0]
        x2,y2,w2,h2=faces[1]
        cropped_1=frame[y1:y1+h1,x1:x1+w1]
        cropped_1=cv2.resize(cropped_1,(180,180))
        #print(cropped_1)
        cropped_2=frame[y2:y2+h2,x2:x2+w2]
        cropped_2=cv2.resize(cropped_2,(180,180))
        #print(cropped_2.shape)
        frame[y2:y2+180,x2:x2+180] = cropped_1
        frame[y1:y1+180,x1:x1+180] = cropped_2


       
    
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()