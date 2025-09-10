# print("hello world")

# # VARIABLE
# name="Qazi Ubaid"
# print(name)

# NAME="Umair"
# print(NAME)

# num=3.14 

# names1=['qazi','ubaid','ahsan']#mutable
# names2=('osama','kashif','zia')#immutable
# names1[0]='qazi ubaid'
# print(names1)
# names2[0]="osama khan"

# print(names2)


num_list=[1,2,3,4,5,1,2,3,4,5]
num_set={1,2,3,4,5,1,2,3,4,5}#unique unorder
print(num_list)
print(num_set)


name='ubaid'
fullname=f'my name is{name}'
print(fullname)

#Conditional statement 
#Indentation
age=40
if age>18 and age<30:  
    print('young')
elif age>30 and age<50:
    print("old")
else:
    print('kid')     

#function
# def greet(name):
#     print(f"hello {name}") #ye function ke sath he due to indentation
#     return 'return from function'
# print("hello greet ") #ye nh he ye bhar he
# result=greet('ubaid') 
# print(result)   


#Loop 2 types in python for,while

name=['ubaid','umair','osama']
for value in name:
  print(value)

one_to_ten=list(range(1,11))
print(one_to_ten)

number=list(range(1,11))
for i in number:
    print("count",i) 



#while

i=0
while i<10:
    print("while",i)
    i+=1