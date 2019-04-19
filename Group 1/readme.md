# Malware Family Classification
This application is designed to classify malware into its various families. It uses Machine Learning on python to classify malware families in "malimg" dataset and dataset provided by Microsoft in "Microsoft Malware Classification Challenge"

## Importance
In the recent years, there has been a rapid rise in the number of files submitted to anti-virus companies for analysis, so it has become very difficult to analyse functionality of each file manually. By converting the file into an image representation the malware analysis process independent of any tool also the process becomes less time consuming. Malware  analysis  aims  at  figuring  out  the  actions  performed  by  the  malicious  software and then developing methods to neutralise those actions and prevent further infections. The family classifer held the malware analyst to classify the malware that may exhibit similar behaviour.

## Implementation
The malware family classifier uses algorithms like K-Nearest Neighbours (KNN) and Convolutional Neural Networks (CNN). The classifier module is built using 2 independent datasets. 
For the malimg dataset, it extracts GIST features and then uses KNN along with K-fold Cross Validation on the feature vector previously extracted.
For the Microsoft dataset, it uses CNN using VGG16 with default weights to classify the dataset.

## Datasets
The application uses "malimg" dataset and dataset provided by Microsoft in "Microsoft Malware Classification Challenge".

## GUI
The application uses Tkinter to interface with the user. The user can submit malware in the GUI and the family output is displayed back in the GUI

### Modules required
1.  [BUILT-IN]sklearn
2.  [BUILT-IN]tkinter
3.  [BUILT-IN]glob
4.  [BUILT-IN]matplotlib
5.  [BUILT-IN]os
6.  [BUILT-IN]PIL
7.  [BUILT-IN]pickle
8.  [DOWNLOAD]pandas
9.  [DOWNLOAD]numpy
10. [DOWNLOAD]leargist
11. [DOWNLOAD]keras
12. [DOWNLOAD]cv2

## Steps to run
1.  Execute the python code on the following file "Malimg_train_test.ipynb" with the malimg dataset.
2.  Run the "Malware_Classifier_GUI.py" to generate the GUI.
3.  Submit the Malware file in the GUI.
