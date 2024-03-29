# -*- coding: utf-8 -*-
"""Image classification using Random Forest classifier

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lvli9phmz8Ag3KEvaHe-jfR27iZnhwSR
"""

# Commented out IPython magic to ensure Python compatibility.
#Load other modules
import matplotlib.pyplot as plt  #Graphics
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier  #Random Forest algorithm
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import RandomizedSearchCV, GridSearchCV
from sklearn.model_selection import cross_val_score
#To show graphs within the notebook
# %matplotlib inline

#using pandas to read the database stored in the same folder
train=pd.read_csv('train.csv')
test=pd.read_csv('test.csv')

train.head()

#Seperate the target and independant variables
df_x=train.iloc[:,1:]
df_y=train.iloc[:,0]

def print_image(row, df):
    temp=df.iloc[row,:].values
    temp = temp.reshape(28,28).astype('uint8')
    plt.imshow(temp)

print_image(5, df_x)

#Check the frequency of each number
df_y.value_counts().sort_index()

sns.countplot(df_y)

plt.figure(figsize=(12,10))
for i in range(40):
    plt.subplot(4, 10, i+1)
    print_image(i, test)

#Split the dataset
X_train, X_test, y_train, y_test = train_test_split(df_x, df_y, test_size=0.2, random_state=0)
print(X_train.shape)
print(X_test.shape)

#training random Forest
rf=RandomForestClassifier(n_estimators=100)
rf.fit(X_train,y_train)

pred=rf.predict(X_test)
print ("Classification Report")
print(classification_report(y_test, pred))
print ("Confusion Report")
print(confusion_matrix(y_test, pred))

#Cross validation
rf=RandomForestClassifier(n_estimators=100)
rf.fit(df_x, df_y)
score = cross_val_score(rf, df_x, df_y)
print (np.mean(score))

#Predicting on test data
pred=rf.predict(test)

pred = pd.Series(pred,name="Label")
submission = pd.concat([pd.Series(range(1,28001),name = "ImageId"),pred],axis = 1)
submission.to_csv("mnist_rf.csv",index=False)

