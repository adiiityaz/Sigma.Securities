import numpy as np
import panda as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score



df=pd.read_csv('mail_data.csv')
print(df)
df=df.where((pd.notnull(df)),'')
data.head()
data.info()
data.shape
data.loc[data['category']=='spam','category']=0
data.loc[data['category']=='ham','category']=1

X=data['message']
Y=data['category']
print[X]
print[Y]

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=3)
print(X.shape)
print(X_train.shape)
print(X_test.shape)

print(Y.shape)
print(Y_train.shape)
print(Y_test.shape)

feature_extraction=TfidfTransformer(min_df=1,Stop_words='english',Covercase='True')
X_train_features=feature_extraction.fit_transform(X_train)
X_test_features=feature_extraction.fit_transform(X_test)
Y_train=Y_train.astype('int')
Y_test=Y_test.astype('int')
print(X_train)
print(X_train_features)

model=LogisticRegression()
model.fit(X_train_features,Y_train)
prediction_on_training_data=model.predict(X_train_features)
accuracy_on_training_data=accuracy_score(Y_train,prediction_on_training_data)
print('acc on training_ data:',accuracy_on_training_data)
prediction_on_test_data=model.predict(X_test_features)
accuracy_on_test_data=accuracy_score(Y_test,prediction_on_test_data)
print('acc on tyest data:',accuracy_on_test_data)

input_your_mail=[""]
input_data_features=feature_extraction.transform(input_your_mail)
prediction=mode.predict(input_data_features)
if(prediction[0]==1):
    print('it is a ham mail , it is secured')
else:
    print('it is scam mail, and this security issue is called phising')
