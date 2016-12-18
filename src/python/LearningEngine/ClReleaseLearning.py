# learning from EIA Wednesday release etf price
# open position at prev wednesday close, close at current week Tuesday close


import pandas as pd
import numpy as np

from sklearn import svm

#import excel data

import os
cwd = os.getcwd()
print(cwd)

test_idx=[0,50]

rawDf = pd.read_csv("../../../resource/data/UsoCleanData.csv")

#rawDf=pd.read_excel("../../../resource/data/UsoCleanData.xlsx",sheetname="Sheet2",skiprows=2)

df =rawDf[["Prev Close","Open","High","Low","Close","Volume","Mtm","y"]]


y=df[['y']]
y=y.values.flatten()


x=pd.DataFrame.as_matrix(df[["Prev Close","Open","High","Low","Close","Volume","Mtm"]])


train_x=x[50:]
train_y=y[50:]

test_x=x[:50]
test_y=y[:50]

#clf = svm.SVC()
#clf.fit(train_x,train_y)
#result =clf.predict(test1)
#print(result)

C = 1.0  # SVM regularization parameter
#svc = svm.SVC(kernel='linear', C=C).fit(train_x, train_y)
rbf_svc = svm.SVC(kernel='rbf', gamma=0.7, C=C).fit(train_x, train_y)
poly_svc = svm.SVC(kernel='poly', degree=3, C=C).fit(train_x, train_y)
lin_svc = svm.LinearSVC(C=C).fit(train_x, train_y)




test1=test_x[29].reshape(1,-1)




#print("regular svc: "+svc.score(test_x,test_y))
print(rbf_svc.score(test_x,test_y))
print(poly_svc.score(test_x,test_y))
print(lin_svc.score(test_x,test_y))

