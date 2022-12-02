import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
df= pd.read_csv('Book1.csv') #read the dataset
#Explore the dataset
df.head()
df.describe() #To know more about the dataset
#Check for null entries
print("Number of null values in the data set are - ",df.isnull().values.any().sum())
#Replace yes and no entries in target to 1 and 0 repsectively
df=df.replace({'admittted':{'Yes':1, 'No':0}})
def interQuartile(x):
  percentile25= x.quantile(0.25)
  percentile75=x.quantile(0.75)
  iqr=percentile75-percentile25
  upperLimit= percentile75+1.5*iqr
  lowerLimit= percentile25-1.5*iqr
  return upperLimit, lowerLimit

upper,lower= interQuartile(df['CET_score'])
print("Lower and upper limit calculated are -", upper, lower)
#Define the independent and dependent variables
y= df['1'] #dependent variable is Decision
x= df.drop(['1'], axis=1)
# splitting the data
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size= 0.2)
#Implementing Logistic Regression using sklearn
modelLogistic = LogisticRegression()
modelLogistic.fit(x_train,y_train)
#print the regression coefficients

print("The intercept b0= ", modelLogistic.intercept_)

print("The coefficient b1= ", modelLogistic.coef_)
#Creating confusion matrix

#Accuracy from confusion matrix
TP= ConfusionMatrix[1,1] #True positive
TN= ConfusionMatrix[0,0] #True negative
Total=len(y_test)
print("Accuracy from confusion matrix is ", (TN+TP)/Total)
