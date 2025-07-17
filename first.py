# name = input("Please enter your name :")
# print("Hello {} welcome to python coding".format(name))

# item =[50,120,230]
# s=sum(item)
# print("Total cost is :{}".format(s))

# const = 23.67891
# print("a 1 dp is {:.1f}".format(const))
# print("a 2 dp is {:.2f}".format(const))
# print("as integer is {}".format(int(const)))

# print("{:<10} | {:>3}".format("Name", "Age"))
# print("{:<10} | {:>3}".format("Alice", 23))
# print("{:<10} | {:>3}".format("Benjamin", 30))
# print("{:<10} | {:>3}".format("Chumba", 21))

# student= "Chumba"
# subject = "Math"
# score= 84.5678
# print("{2} scored {0:.2f} in {1} test".format(score,subject,student))

# hide="steganograpHy is a mEthod of hiding a message in text, image or video so that nobody unauthorized has acces to it, it's such a LoveLy thing to dO"
# hide2="How i Nearly ended lying low yesterday"
# k=hide2.split()
# h=""
# for w in k:
#     h= h + w[0]
# print(h)

# message= input("Enter message to be encoded here :")
# coded = ""
# for hh in message:
#     asci = str(ord(hh))
#     coded = coded + asci + " "
# print(coded)

# cipher = input("Enter ciphered code here :")
# s=cipher.split()
# for c in s :
#     decoded = chr(int(c))
#     print(decoded, end='')

# planets ={'one': ["mercury", 'again','oops'], 'two': "venus", 'three': "earth"}
# planets ['four']= "mars"
# for p in planets:
#     print(" {:<7} = {}".format(p,planets[p]))
# print(planets.items())

# my_details = {'Name': "Chumba", 'age': 22, 'Course': "Bsc Computer Science"}
# my_details['year']=3
# my_details['age']=23
# for d in my_details:
#     print("{} = {}".format(d,my_details[d]))
# l= 'email' in my_details
# if l == False:
#     print("email not found in list")
# print(my_details.items())
# print(my_details.keys())
# print(my_details.values())

# grades = {
#     "Math": [80, 90, 85],
#     "Python": [78, 82, 89],
#     "AI": [92, 94, 90]
# }
# grades["Math"].append(88)
# print(grades["Math"])
# for gradess in grades.values():
#     for g in gradess:
#         print(g,end=' ')
    
# students = {
#     "Chumba": {"age": 22, "course": "CS"},
#     "Mercy": {"age": 21, "course": "Data Science"}
# }
# students["Chumba"]['age']=25
# print(students["Mercy"]['course'])
# print(students["Chumba"])

# code =12345
# if len(str(code))==5 and str(code).isdigit():
#     print("It is valid")
# else:
#     print("False")

# gut=['hey there now','welcome home there','this is fun', 'i am almost there now']
# keywords=['now','fun']
# dic = {}
# for keys in keywords:
#     dic[keys]=[]
#     for ind,words in enumerate(gut):
#         lowered = words.lower().strip(',.')
#         if keys.lower() in lowered.split():
#             dic[keys].append(ind)
# print(dic)

# doc_list=['The Learn Python Challenge Casino', 'They bought a car.', 'Casinoville?', "He bought a casino."," A casino! That's crazy."]

# dic={}
# keywords = ['casino','car']
# for key in keywords:
#     dic[key]=[]
#     for ind,words in enumerate(doc_list):
#         lowered = words.split()
#         nom= [k.strip('. , !').lower() for k in lowered]
#         if key.lower() in nom:
#             dic[key].append(ind)
# print(dic)
