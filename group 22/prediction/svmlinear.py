from sklearn import svm
clf = svm.SVC(kernel = "linear")
clf.fit(X_train2, y_train)  
y_pred = clf.predict(X_test2)
printScores(y_test, y_pred, "linear svm")
