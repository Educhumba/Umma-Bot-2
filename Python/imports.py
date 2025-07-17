# import math
# import string
# import random
# import datetime
# # ra=input("Enter radius of the circle :")
# # area = (math.pi)*int(ra)
# # print("Area of the circle is {:.3f} units square".format(area))

# # chars= string.ascii_letters + string.digits + string.punctuation
# # passs = random.choices(chars,k=4)
# # print(''.join(passs))

# today = datetime.date.today()
# day = today.strftime("%A")
# print('Today is {} which is {}'.format(today,day))

# import pyjokes

# for j in range(1,4):
#     joke = pyjokes.get_joke()
#     print(joke)

# import requests
# import time
# for j in range(1,4):      
#     joke = requests.get("https://official-joke-api.appspot.com/random_joke")
#     if joke.status_code==200:   
#         print('setup:',joke.json()['setup'])
#         print('punchline :',joke.json()['punchline'])
#         time.sleep(1)
#     else:
#         print("Could not print joke man")
#         break

import csv
import os
if not os.path.exists("mastude.csv"):
    with open("mastude.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['name', 'age', 'course'])
while True:
    print("\n\n1.Enroll student")
    print("2. See enrolled students")
    print("3. Total students and average age :\n")
    choice=input("Choose action :")
    if choice=='1':
        name=input("Enter student's name ")
        age=input("Enter student's age ")
        course=input("Enter student's course ")
        with open("mastude.csv",'a',newline='') as create:
            add = csv.writer(create)
            add.writerow([name,age,course])
    elif choice=='2':
        with open('mastude.csv','r') as info:
            data = csv.DictReader(info)
            for item in data:
                print(item['name'],'-',item['course'])
    elif choice=='3':
        with open("mastude.csv",'r') as info:
            data= csv.DictReader(info)
            ages=[]
            for items in data:
                ages.append(int(items['age']))
                sum_ages=sum(ages)
            if ages:
                print("Total number of students is :{}".format(len(ages)))
                print("The average age is :{}".format(sum_ages/len(ages)))
            else:
                print('No student records found!')
            break
    else:
        break

