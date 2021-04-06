
list1=[10,15.5,'python','A','abc']
list2=['xyz','ABC','xyz']

print('list1=',list1)
print('list2=',list2)

print('type of list1 is:',type(list1))

print('lenth of list1=',len(list1))

print('string slicing')
#first element=list[0]
print('list[0])=',list1[0])
print('list[1]=',list1[1])
print('list1[2]=',list1[2])

print('list1 =', list1[2])

#LIST [STARTINDEX:ENDINDEX(EXCLUDING):INTERVAL]

print('list1[2:5]=',list1[2:5])

print('list1[0:2]=',list1[0:2])

print('list1[::2]=',list1[::2])
print('list1[::3]=',list1[::3])
print(list1[1::2])
     

#list reverse without using function
print('list reverse list1[::-1]',list1[::-1])

print('list built -in methods')
print('max(list2)=',max(list2))
print('min(list2)=',min(list2))

list3=list1+list2
print('list1+list2=',list3)


len(list3)

'python' in list1
#_in keyward
#data in variable
print('pythonin list2=','python'not in list1)

print('python in list1 =','python'in list1)

print('python in list2=','python' not in list2)

#declare list in diff way
lista,listb=[15,15.5,'python','a',"abc"],['xyz1','abc','xyz']
print('lista=',lista)
print('listb=',listb)

#method to add element to the list

#list.append(element)
list2.append('python')

#list.extend(seq)
list2. extend('rv')

#list.append(seq)
list1.append(list2)
print(list1)
print('len(list1)',len(list1))

#insert(index,element)
list2.insert(3,'epro')
print('list2=',list2)

#to check the index position of an element
#list.index(element)
print('list2,index("xyz")=',list2.index('xyz'))

#to count the number of occurances of element
#list2.count(element)

print('list2.count("xyz")=',list2.count('xyz'))
print('list2.count(10)=',list2.count(10))
print('list2.count("xyz")=',list2.count("xyz"))

#to remove the elements from the list
#pop (index)
#remove (element)

#list.remove (element)
print('list2',list2)
print('list2.count("xyz")*=',list2.count("xyz"))
list2.remove('xyz')

print('list2',list2)
print('list2.count("xyz")=',list2.count('xyz'))
