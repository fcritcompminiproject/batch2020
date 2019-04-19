from sklearn import svm
clf = svm.SVC()
clf.fit(X_train2, y_train)  
y_pred = clf.predict(X_test)
printScores(y_test, y_pred, "svm")
