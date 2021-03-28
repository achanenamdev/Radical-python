# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 11:51:19 2021

@author: Lenovo
"""

a=10.0
b=20
c="string"
d=True
#check the type of variable
print('type of a is',type(a))

#print the statement with +concat operator
print('value of a+c is',str(a)+c)

print('value of a=',a)

#print the statement with % operator
print('value of a=%f'%a)

#print the statement with .format
print('value of a={}'.format(a))

#variable is not passed in format argv
print('my name is {} and my age is {}'.format("radical",10))

#variable are passed in format argv
name='radical' 
age=10
print('my name is {name} and my age is {age}'.format(name='radical',age=10))

#interchange place of parameter

print('my name is {name} and my age is {age}'.format(age=10,name='radical'))