import pandas as pd
import numpy as np
from datetime import datetime
data = pd.read_csv('Cleaned_insurance_data.csv')
# # data = pd.read_csv("insurance_data.csv")
# data['Claim Amount']=pd.to_numeric(data['Claim Amount'],errors='coerce')
# data['Premium Amount']=pd.to_numeric(data['Premium Amount'],errors='coerce')
# data['Customer Age']=pd.to_numeric(data['Customer Age'],errors='coerce')
data['Policy Start Date']=pd.to_datetime(data['Policy Start Date'],errors='coerce')
# data['Claim Date']=pd.to_datetime(data['Claim Date'],errors='coerce')
# data=data.dropna()
# data=data[~data['Region'].str.endswith('xx',na=False)]
# # data.to_csv('Cleaned_insurance_data.csv',index=False)

import matplotlib.pyplot as plt
import seaborn as sns
Regions=data.groupby('Region').size().reset_index(name="Totals")
Claims_per_Region= data.groupby(['Region','Policy Type'])['Claim Amount'].sum()
customers_per_region=data.groupby(['Region'])['Customer ID'].nunique()
now = pd.Timestamp.now()
data['Period']= (now.year - data['Policy Start Date'].dt.year)*12 + (now.month - data['Policy Start Date'].dt.month)
# print((data.Period/12).sort_values(ascending=False))
correlation = data.corr(numeric_only=True)
covariance = data.cov(numeric_only=True)
# print(correlation, '\n' , covariance)

plt.figure(figsize=(8,6))
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()
