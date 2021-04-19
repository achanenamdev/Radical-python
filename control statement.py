# control statement

# if statement 
temp = 40 
if temp >= 40:
    print ("room is hot")
    
    
age = 17
    
print ('voting system') 
if age > 17:
    print('congrats !!! you are eligible for voting')
else:
    print('oh sorry!!! you are not eligible for voting process')
        
    
age = 35
if age < 22:
    print("study hard !!! ")
elif age >21 and age <26:
    print("your salary shoud be in the range of 10k - 50k")
elif age >25 and age <36:
    print("your salary shoud be in the range of 50k - 2l") 
elif age >35 and age<50:
    print("your salary shoud be in the range of 2ll - 5l")
else:
    print("no need to work ...enjoy the life ....!!!!")
    
 
# python program to check whether the given number is even or odd.
number =input("enter a number")

X = int(number)%2

if  X == 0:
    print("the number is even")
else:
    print("the number is odd")
    
    
    
a=['cat','mouse','rat']

for counter in  'variable':
    for x in a:
        print(a)
        len (a)
        
# control statement 
#for loop

num1,num2=10,20
#range will generate sequence of no. syntax- range (start,end,step)
#syntax i for counter in variable:
    
for i in range(0,11,2):
    print(i)


list1=['soun',"moun","pinky","guddu","duggu"]
print(list1)

#iterate the list with condition
for i in list1:
    if i == "pinky":
        print(i)
        
for i in list1:
    if i == "pinky":
        break
    print(i)
    
#iterate the list with condition
for i in list1:
    if i== "pinky":
        continue
    print(i)
    
dict1={ "name" : "newton",
      "qual" : "me",
      "city" : "pune"}
print(dict1)

#iterate the dict
for i in dict1:
    print(i)
    
for i in dict1:
    print(dict1[i])


for i in dict1.items():
    print(i)
    
    
for i in dict1:
    print('key is ',i, "and value is",dict1[i])
    
for key, value in dict1.items():
    print('key is',key,"and value is",value)
    
#drew pattern    
for i in range(6,1,-1):
    for i in range(6,1,-1):
        if i==1:
            print(' * ')

#range can have negative no. as well            
for i in range (-6,1):
    print('range(-6,1)',i)
                

#write the python program to find out the average of a set of integers        
num1=10 
num2=20
num3=30

avg=(num1+num2+num3)/3
#avg=sum of all item/no of items

count=int(input("enter the count of numbers:"))
i=0
sum=0
for i in range (count):
    x=int(input("enter an integer:"))
    sum =sum+x
avg=sum/count
print("the average is:",avg)
    
    
    
