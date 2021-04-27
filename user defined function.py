# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 12:11:38 2021

@author: Lenovo
"""

print, input, copy, count - inbuilt-function

print() ---> namdev()- user defined-function



def namdev(name,last):
    return name,last

res =namdev ('namdev','achane')      #calling functon
print("output of namdev function is:",res)

res =namdev('ganesh','takur')
print("output of namdev function is:",res)

#function without arugement
def concatinate():
    name='namdev'
    last='achane'
    return(name,last)

res=concatinate()
print(res)

#2Number. multiplication

def multi(num1,num2):
    result= num1 * num2
    return result

res1 = multi(2,2)

print(res1)