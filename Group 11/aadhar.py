#!C:\Users\Aditya\AppData\Local\Programs\Python\Python36-32
import cv2
import re
import sqlite3
import pytesseract
import glob
import os

def function():
	list_of_files = glob.glob('images/*') # * means all formats.Specific format: *.csv
	latest_file = max(list_of_files, key=os.path.getctime)
	img = cv2.imread(latest_file)
	# print(pytesseract.image_to_string(img))
	str1=pytesseract.image_to_string(img)

#Gender
	i=0
	a1=[]
	for text in str1.split():
		a1.append(text)
		if text=="MALE" or text=="Male":
			gender="Male"
		if text=="FEMALE" or text=="Female":
			gender="Female"	
	l=0
	array=[]
	for text in str1.split("\n"):
		array.append(text)
		l=l+1
	print(array)
	print(a1)
#Name
	i=0
	l=0
	loc=0
	p = re.compile('DOB')
	for text in array:
		if p.search(text):
			loc=l
			print(loc)
			break
		l=l+1	
	name=array[loc-1]
	for text in array:
		i=i+1
		if name=="":
			name=array[loc-i]
#DOB
	dob=""
	l=0
	i=0
	for text in a1:
		if p.match(text):
			loc=l
		l=l+1
	print(a1[loc])
	for text in a1:
		if text=="DOB:" or text==";" :
			dob=a1[i+1]
		i=i+1
	if dob=="":
		dob=a1[loc+2]

#UID	
	p = re.compile('[0-9]{4,12}')
	for text in array:
		if p.match(text):
			ano=text
	
	print(ano,name,gender,dob)
	dataitem=[ano,name,dob,gender]


	conn = sqlite3.connect('example.db')
	c = conn.cursor()
	# c.execute('''create table data
	#              (no integer primary key autoincrement,ano text, name text, dob text, gender text)''')

	c.execute("insert into data(ano,name,dob,gender) VALUES (?,?,?,?)",dataitem)
	conn.commit()
	conn.close()
