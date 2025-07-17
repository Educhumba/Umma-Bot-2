import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
data = pd.read_csv('Cleaned_insurance_data.csv')
Regions=data.groupby('Region').size().reset_index(name="Totals")
# print(data.head(14))
# print(data.iloc[10,5])
# x=[1,2,3,4,5,6,7,8]
# y= [22,21,27,23,23,26,29,24]
# plt.plot(x,y, label='Line Graph', linestyle='solid',color='black')
# plt.title("A graph of temperature against time")
# plt.xlabel('Time')
# plt.ylabel("Temperature")
# plt.legend()
# plt.grid(True)
# plt.show()

# reg=Regions.Region
# tot=Regions.Totals
# plt.bar(reg,tot,color='orange',label='bar graph')
# plt.title("Policy holders per region")
# plt.ylabel('holders')
# plt.xlabel('Region')
# plt.show()

# plt.pie(tot,labels=reg,autopct='%1.1f%%',startangle=90)
# plt.title('Policy distribution per region')
# plt.axis('equal')
# plt.show()

# sns.barplot(x="Policy Type", y="Claim Amount", data=data)
# plt.title("Avg Claim Amount per Policy Type")
# plt.xticks(rotation=45)
# plt.grid(True)
# plt.tight_layout()
# plt.show()

# sns.countplot(x='Region', data=data)
# plt.xticks(rotation=45)
# plt.title("Client Count per Region")
# plt.legend()
# plt.show()


# sns.boxplot(x="Policy Type", y="Claim Amount", data=data)
# plt.title("Claim Amount Spread by Policy")
# plt.show()


# sns.histplot(data['Premium Amount'], kde=True, bins=20)
# plt.title("Premium Distribution")
# plt.show()


