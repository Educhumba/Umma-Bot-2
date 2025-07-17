# import pandas as pd
# import numpy as np
# students = {
#     "Name": ["Chumba", "Mercy", "John", "Alice","Mercy","Kerubo","Kylie","Powell"],
#     "Age": [23, 21, 22, 24,33,19,28,31,],
#     "Course": ["CS", "Data Science", "AI", "CS","Maths","Geo","AI","Agric"],
#     "Score": [69, 91, 76, 84,34,76,59,75]
# }
# data = pd.DataFrame(students)
# # statu=data['status']='active'
# # data['Pass']= np.where(data['Score']>=70,'Yes','No')
# # data['Score']=data['Score']+5
# # def ass_grade(score):
# #     if score>=90:
# #         return "A"
# #     elif score>=80:
# #         return "B"
# #     else:
# #         return "c"
# # data['Grade']=data['Score'].apply(ass_grade)
# # print(data.sort_values("Score",ascending=False))
# # print(data.sort_values("Age"))
# # print(data.sort_values(by=['Course','Score'],ascending=[True,False]))

# print(data.groupby('Course')['Score'].mean())
# print(data.groupby('Course').size())
# print(data.groupby('Course')['Age'].max(),'\n\n')
# def category(score):
#     if score >= 85:
#         return "Distinction"
#     elif score > 70:
#         return "Credit"
#     elif score > 50:
#         return "Pass"
#     else:
#         return "Fail"

# data['Result']=data['Score'].apply(category)
# print(data.groupby('Result').size())
# print(data.groupby(['Course','Result']).size())
# print(data.groupby('Course')['Result'].size())









import pandas as pd
def grading(score):
    if score>400:
        return 'A'
    elif score>300:
        return 'B'
    elif score>200:
        return "C"
    elif score>100:
        return 'D'
    else:
        return 'F'
students= pd.read_csv('class_students_results.csv')
subjects=['Math','English','Kiswahili','Science','SST']
students[subjects]=students[subjects].apply(pd.to_numeric, errors='coerce')
students['Total']=students[subjects].sum(axis=1)
students['Grade']=students['Total'].apply(grading)
students['O_Rank']=students['Total'].rank(method='min',ascending=False).astype(int)
Overall_ranking= students.sort_values(by='Total',ascending=False).reset_index(drop=True)
Class_ranking=students.sort_values(by=['Stream','Total'],ascending=[True,False]).reset_index(drop=True)
Class_ranking['C_Rank']=Class_ranking.groupby('Stream')['Total'].rank(method='min',ascending=False).astype(int)
East_List=Class_ranking[Class_ranking['Stream']=='East']
North_List=Class_ranking[Class_ranking['Stream']=='North']
South_List=Class_ranking[Class_ranking['Stream']=='South']
West_List=Class_ranking[Class_ranking['Stream']=='West']
overall_mean= students['Total'].mean()
stream_mean= students.groupby('Stream')['Total'].mean().round(2).sort_values(ascending=False)
subject_mean=students[subjects].mean().round(2)
best_per_subject = {}

# math_champ=students['Math']
# print(Overall_ranking.head(20))
# with pd.ExcelWriter('ranking_report.xlsx') as writer:
#     Overall_ranking.to_excel(writer, sheet_name='Overall', index=False)
#     East_List.to_excel(writer, sheet_name='East', index=False)
#     West_List.to_excel(writer, sheet_name='West', index=False)
#     North_List.to_excel(writer, sheet_name='North', index=False)
#     South_List.to_excel(writer, sheet_name='South', index=False)
print()
