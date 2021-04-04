list=Its a collaction which ordered and changeable.allows duplicate member

list1=[10,15.5,'python','A',"abc"]
list2=['XYZ','ABC','xyz']

print('list1=',list1)
print('list2=',list2)

print('type of list1 is:',type(list1))
print('lenth of list1=',len(list1))

print('slicing slicing')
#first element=list[0]
print('list[0]=',list1[0])
print('list[1]=',list1[1])
print('list1[2]=',list1[2])

print('list1=',list1[2])

#list[start index: end index(excluding):interval]
print('list1[2:5]=',list1[2:5])
print('list1[0:2]=',list1[0:2])
print('list1[::2]=',list1[::2])

#list reverse without using function
print('list reverse list1[::-1]=',list1[::-1])

#print('list built_in methods')
print('max(list2)=',max(list2))
print('min(list2)=',min(list2))

list3=list1+list2
print('list1+list2=',list3)

len(list3)

'python'in list1
#_in keyward
print('python in list1=','python'in list1)
print('python in list2=','python' not in list2)
print('python in list2=','python'  in list2)

#declare list in different in way
lista,listb=[15,15.5,'python','A',"abc"],['xyz','abc','XYZ']
print('lista=',lista)
print('listb=',listb)

#method to add element to the list
#list.append(element)
list2.append('python')

#list.extend(seq)
list2.extend('rv')

#list.append(seq)
list1.append(list2)
print(list1)
print('len(list1)=',len(list1))

#insert(index,element)
list2.insert(3,'epro')
print('list2=',list2)

#to check the index position of an element 
#list.index(element)
print('list2,index("xyz")=',list2.index("xyz"))

#to count the number of occurances of element
#list2.count(element)
print('list2.count("xyz")=',list2.count('xyz'))
print('list2.count(10)=',list2.count(10))
print('list2.count("xyz")=',list2.count("xyz"))

