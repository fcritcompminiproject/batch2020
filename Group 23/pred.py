import pickle
import os
import pandas as pd
def classi(rofilename):
    print("World")
    if(rofilename=="C:/Users/vborh/Desktop/ids/random forest/tdos.csv"):
        file = open("Dosmodel.pkl",'rb')
    elif(rofilename=="C:/Users/vborh/Desktop/ids/random forest/testP.csv"):
       file = open("Probemodel.pkl",'rb')
    file = open("Dosmodel.pkl",'rb')
    df= pd.read_csv(rofilename)
    clf_DoS = pickle.load(file)
    y_predict = clf_DoS.predict(df)
    clf_DoS.predict_proba(df)[0:10]
    Y_DoS_pred=clf_DoS.predict(df)
    return Y_DoS_pred
"""df= pd.read_csv("tdos.csv")
result=classi(df)
df1=pd.read_csv("")
print("Getting Result")
for i in result:
    print(i)"""
