# -*- coding: utf-8 -*-
"""netflix.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kb2sPZTu4Lww32xSqDy3mnR1q05QVxNk
"""

import numpy as np
from numpy import linalg as LA
from scipy.sparse import linalg
from scipy.linalg import eig as LAeig
import matplotlib
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg

import csv

userID={0:{0:0}}
movies=set()

with open('train.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
      if len(row)==4:
        movie=row[0]
        user=row[1]
        rate=row[2]
        movies.add(movie)
        if user in userID:
          dic=userID[user]
          dic[movie]=rate 
        else:
          dic={movie: rate}
          userID[user]=dic

print(len(userID))
userLen=len(userID)

#print(userID['6'])
movieLen=len(movies)
print(movieLen)

S=np.zeros((userLen,userLen)) #similarity matrix
keylist=[]
for i in userID.keys():
    keylist.append(i)

for i in range(userLen):
    S[i,i]=1

for i in range(userLen):
    for j in range(i+1,userLen):
      Sum=0
      user1=keylist[i]
      user2=keylist[j]
      dic1=userID[user1]
      dic2=userID[user2]
      rated=dic1.keys()
      count=0
      for k in rated:
        if k in dic2:
          count+=1
          Sum+=np.square(int(dic1[k])-int(dic2[k]))
      if count!=0:
        S[i,j]=np.exp(-np.sqrt(Sum/count)/2)
      else:
        S[i,j]=0
      S[j,i]=S[i,j]
print(S)

A=np.copy(S)

# Construct the Laplacian
D=np.diag(np.sum(A, axis=0))
vol=np.sum(np.diag(D))
tmpD=np.copy(D)
for i in range(userLen):
    tmpD[i,i]=tmpD[i,i]**(-1/2)

# Which Laplacian is this
L=np.eye(userLen)-(tmpD.dot(A)).dot(tmpD)

[val_o, vec_o]=LA.eig(L)

from sklearn.cluster import KMeans
from sklearn import metrics
ks=np.array(keylist)

sp_kmeans10 = KMeans(n_clusters=10).fit(vec_o)
len(sp_kmeans10.labels_)

clusters={0:[]}
for i in range(0,userLen-1):
  us=keylist[i]
  lable=sp_kmeans10.labels_[i]
  if lable in clusters:
    lt=clusters[lable]
    lt.append(us)
  else:
    lt=[us]
    clusters[lable]=lt

predict={1:{}}
for i in range(2,10):
  predict[i]={}

for i in range(1,10):
  for movie in movies:
    subsum=0
    ct=0
    for user in clusters[i]:
      if movie in userID[user]:
        dic=userID[user]
        subsum+=int(dic[movie])
        ct+=1
    doc=predict[i]
    if subsum!=0:
      doc[int(movie)]=subsum/ct
    else:
      doc[int(movie)]=3

doc=predict[1]
8102 in movies

testlist=[]
with open('test.csv') as fx:
    fx_csv = csv.reader(fx)
    for row in fx_csv:
      testlist.append([row[0],row[1],row[3]])
len(testlist)

for ps in testlist:
  movie=int(ps[0])
  user=ps[1]
  for group in range(1,10):
    if user in clusters[group]:
      diction=predict[group]
      ps.append(round(diction.get(movie,3), 2))
      break

fileHeader = ["movie-id", "customer-id", "date", "rating"]

csvFile = open("result.csv", "w")
writer = csv.writer(csvFile)

writer.writerow(fileHeader)
for ps in testlist:
  writer.writerow(ps)


csvFile.close()
