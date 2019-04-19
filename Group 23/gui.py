import numpy as np
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time
#from pygame import mixer
#import time
#import cv2
from tkinter import *

#import tkinter
#import tkinter.filedialog
#importfiledialog
#import Tkinter.messagebox
import tkinter,tkinter.constants, tkinter.filedialog
import pred
import im
print("Hello")
time=20
root=Tk()
root.geometry('500x570')
frame = Frame(root, relief=RIDGE, borderwidth=4)
frame.pack(fill=BOTH,expand=1)
root.title('Intrusion Detection System')
frame.config(background='sky blue')
label = Label(frame, text="Intrusion Detection System using Machine Learning",bg='sky blue',font=('Times 36 bold'))
label.pack(side=TOP)
#filename = PhotoImage(file="demo1.png")
#background_label = Label(frame,image=filename)
#background_label.pack(side=TOP)
"""import execnet
def call_python_version(Version, Module, Function, ArgumentList):
    gw      = execnet.makegateway("popen//python=python%s" % Version)
    channel = gw.remote_exec(
        from %s import %s as the_function
        channel.send(the_function(*channel.receive()))
     % (Module, Function))
    channel.send(ArgumentList)
    return channel.receive()
"""
from PIL import ImageTk, Image
def img ():
    pass
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.utils.multiclass import unique_labels
def plot_confusion_matrix(y_true, y_pred, classes,
                          normalize=False,
                          title=None,
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if not title:
        if normalize:
            title = 'Normalized confusion matrix'
        else:
            title = 'Confusion matrix, without normalization'

    # Compute confusion matrix
    cm = confusion_matrix(y_true, y_pred)
    # Only use the labels that appear in the data
    classes = classes[unique_labels(y_true, y_pred)]
    #newlabeldf=classes.replace({0:'Normal',1:'DoS',2:'Probe',3:'R2L',4:'U2R'})
    #classes=newlabeldf
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)
    

    fig, ax = plt.subplots()
    im = ax.imshow(cm, interpolation='nearest', cmap=cmap)
    ax.figure.colorbar(im, ax=ax)
    # We want to show all ticks...
    ax.set(xticks=np.arange(cm.shape[1]),
           yticks=np.arange(cm.shape[0]),
           # ... and label them with the respective list entries
           xticklabels=classes, yticklabels=classes,
           title=title,
           ylabel='True label',
           xlabel='Predicted label')

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, format(cm[i, j], fmt),
                    ha="center", va="center",
                    color="white" if cm[i, j] > thresh else "black")
    fig.tight_layout()
    fig.savefig('image.png')
    return ax
 

def web():
   #dlg = filedialog.Open(self)
   
   rofilename = tkinter.filedialog.askopenfilename(initialdir = "C:/Users/vborh/Desktop/ids/random forest",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
   #print("file Name is:",end="")
   print (rofilename)
   #result = call_python_version("2.7", "pred.py", "classi",[root.filename])
   result=pred.classi(rofilename)
   print(len(result))
   if(rofilename=="C:/Users/vborh/Desktop/ids/random forest/tdos.csv"):
       dtest=pd.read_csv("DoStest.csv",header=None)
   elif(rofilename=="C:/Users/vborh/Desktop/ids/random forest/testP.csv"):
       dtest=pd.read_csv("Probetest.csv",header=None)
   print(len(dtest))
   class_names=np.array([0,1,2,3,4])
   print(type(result))
   plot_confusion_matrix(dtest,result, classes=class_names,title='Confusion matrix')
    k=result[0]
   #print (result)
   res.config(text=" %s" %k)
   
but1=Button(frame,padx=5,pady=5,width=39,bg='white',fg='black',relief=GROOVE,command=web,text='Upload Test Data file',font=('helvetica 15 bold'))
#but1.pack(side=TOP)
but1.place(x=500,y=104)
res=Label(frame)
res.place(x=500,y=204)
#but2=Button(frame,padx=5,pady=5,width=39,bg='white',fg='black',relief=GROOVE,command=im.showimage,text='show image',font=('helvetica 15 bold'))
#but2.place(x=500,y=304)
root.mainloop()
