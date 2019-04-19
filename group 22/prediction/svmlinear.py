from sklearn import svm
clf = svm.SVC(kernel = "linear")
clf.fit(X_train, y_train)  
y_pred = clf.predict(test_data)
printScores(y_test, y_pred, "linear svm")
