import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
data = pd.read_csv("Cleaned_insurance_data.csv")
features=['Premium Amount','Policy Type','Region','Customer Age','Incident Type','Gender']
# y= data['Claim Amount']
# X=data[features]
# X=pd.get_dummies(X,drop_first=True)
# train_X, val_X, train_y, val_y= train_test_split(X,y,random_state=1)
# our_model=DecisionTreeRegressor(random_state=1)
# our_model.fit(train_X,train_y)
# pred= our_model.predict(val_X)
# mae=mean_absolute_error(val_y, pred)
# print(mae)

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
y=data['Status']
X=data[features]
X=pd.get_dummies(X,drop_first=True)
train_X, val_X, train_y, val_y = train_test_split(X,y,random_state=1)
model1= DecisionTreeClassifier(random_state=1)
model1.fit(train_X, train_y)
preds=model1.predict(val_X)
evaluation =classification_report(val_y,preds)
print(evaluation)