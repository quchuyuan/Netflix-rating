# Netflix-rating
Requirements:
---
To run this project, you'll need Python 3.x and the following python packages:  
  * Numpy  
  - Scipy  
  * csv  
  - Pandas   


Dataset:
---
The training data set consists of 1 million transactions/records (user-movie pairs) of features/attributes:
[Trianing Set](https://drive.google.com/file/d/1BPaRosQv2QdIIx0jkdWe_R7B2vDf4RiV/view?usp=sharing)
<movie id, customer id, rating, date recommended> as your training set as well as

another data set of <movie id, date released movie name>.  
 

Observations and Conclusion:
---
Since the rating is 1-5 and can only take integers if we just use newly generated prediction for further functions like recommendation and normalization of a movie rating, the outcomes of the two methods are quite similar.  

However, since the training set we have is very sparse, the spectral clustering method performed relatively worse. There is a situation that in a certain cluster c, no one has rated movie j, therefore the predicted value is just 3(by default). This is very unreasonable therefore we have to decrease the value of k to relieve it. But there are also side effects to using small k value i.e. there are not enough clusters to separate differently behaved users. Finally, many users may have similar predicted values. I think this is an unsolvable tradeoff and the primary cause is that we do not have sufficient training data.

The Matrix Completion Methods may perform better when training data is relatively insufficient. Since it is like a two-dimension clustering, it can combine more information than 1-D clustering. There is a team in Nvidia has developed a movie recommendation program based on matrix completion, and it also uses a small data set.  Although I have not received my scores for there two methods, I believe the Matrix Completion will score high.
