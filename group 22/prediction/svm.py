from sklearn import svm
clf = svm.SVC()
clf.fit(X_train, y_train)  
y_pred = clf.predict(Test_data)
printScores(y_test, y_pred, "svm")
