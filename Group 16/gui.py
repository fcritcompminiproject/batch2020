#from pygame import mixer
import time
from tkinter import *
import tkinter.messagebox
from coll import Coll
from pred import Pred
from train import Train
root=Tk()
root.geometry('500x600')
win = Frame(root, relief=RIDGE, borderwidth=2)
win.pack(fill=BOTH,expand=1)
root.title('Sign Language')
win.config(background='light blue')
label = Label(win, text="Sign Language Predictor",bg='light blue',font=('Times 35 bold'))
label.pack(side=TOP)


def hel():
   help(cv2)

def Contri():
   tkinter.messagebox.showinfo("Contributors","\n1.Terrell\n2. Kaustubh \n3. Jonathan \n")


def anotherWin():
   tkinter.messagebox.showinfo("About",'Sign Language Predictor v1.0\n Made Using\n-OpenCV\n-Numpy\n-Tkinter\n-Tensorflow\n-Keras\n In Python 3')

menu = Menu(root)
root.config(menu=menu)

subm1 = Menu(menu)
menu.add_cascade(label="Tools",menu=subm1)
subm1.add_command(label="Open CV Docs",command=hel)

subm2 = Menu(menu)
menu.add_cascade(label="About",menu=subm2)
subm2.add_command(label="Driver Cam",command=anotherWin)
subm2.add_command(label="Contributors",command=Contri)



def exitt():
   exit()

def trainn():
	Coll.coll("train")
	
def test():
	Coll.coll("test")

def webdetRec():
	print("webdetrec")

def webdetrRec():
	print("webdetrec")

   
but1=Button(win,padx=5,pady=5,width=39,bg='white',fg='black',relief=GROOVE,command=trainn,text='Add to Training Data',font=('helvetica 15 bold'))
but1.place(x=5,y=104)

but2=Button(win,padx=5,pady=5,width=39,bg='white',fg='black',relief=GROOVE,command=test,text='Add to Testing Data',font=('helvetica 15 bold'))
but2.place(x=5,y=176)

but3=Button(win,padx=5,pady=5,width=39,bg='white',fg='black',relief=GROOVE,command=Train.train,text='TRAIN',font=('helvetica 15 bold'))
but3.place(x=5,y=250)

but4=Button(win,padx=5,pady=5,width=39,bg='white',fg='black',relief=GROOVE,command=Pred.pred,text='Predict',font=('helvetica 15 bold'))
but4.place(x=5,y=322)

but5=Button(win,padx=5,pady=5,width=39,bg='white',fg='black',relief=GROOVE,command=Coll.show,text='Show Sign Language',font=('helvetica 15 bold'))
but5.place(x=5,y=400)

but5=Button(win,padx=5,pady=5,width=5,bg='white',fg='black',relief=GROOVE,text='EXIT',command=exitt,font=('helvetica 15 bold'))
but5.place(x=210,y=478)

#Label(win, text="Prediction",font=('helvetica 15 bold'),bg='light blue').place(x=110,y=550)
#Entry(win).place(x=215,y=556)

root.mainloop()