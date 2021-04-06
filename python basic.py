Python is an interpreted programming language.
Python source code is compiled to bytecode as a .pyc file.

a=10.0
b=20
c="string"
d=True

#check the type of variable
print('type of a is ',type(a))

#print the statement with +concat operator
print('value of a+c is ',str(a)+c)
print('value of a=',a)

#print the statement  with % operator
print('value of a=%f'%a)

#print the statement with .format
print('value of a={}'.format(a))

#variable is not passed in format argv
print('my name is {} and my age is {}'.format("radical",10))

#variable is passed in format argv
name='radical'
age=10
print('my name is {name} and my age is {age}'.format(name='radical',age=10))

#interchange place of parameter
print('my name is {name} and my age is {age}'.format(age=10,name='radical'))

#declare variable 
a=1
b=2

#sum of 2nos
result=a+b
print("sum of a add b nos is",result)

#list
a=[1,2,3,4]

#a=[5]
a[3]=5

#append list
#var.append

a.append(6)
a.append(7)

#remove
#var[index]=[]

a[5]=""
a.remove(1)

#pop
# var .pop(n)

a.pop(2)

