dict1={}

print('dict1 ',dict1)

print('type(dict1)=',type(dict1))
print('len(dict1)=',len(dict1))

dict2={ 
          'name'   :'python',
          'version' :'3.6.3',
          'method' :'dict',
          }

print('dict2=',dict2)
print('type(dict2)=',type(dict2))
print('len(dict2)=',len(dict2))

#Accessing the values from the keys
dict2['name']
print('dict2["name"]=',dict2['name'])
print('dict2["version"]=',dict2['version'])
print('dict2["method"]=',dict2['method'])

#get all keys
print('dict2.keys()=',dict2.keys())

#get all values
print('dict2.values()=',dict2.values())


#to convert list into dict
list1=[10,20,30,40,50]
list2=['A','B','C','D','E']

#dict1.fromkeys(list1)
newDict=dict.fromkeys(list1)
print(dict1.fromkeys(list1,'python'))
print(dict1.fromkeys(list1,list2))

#dict.update
print(newDict)
newDict.update({10:'A',20:'B',30:'C',40:'D',50:'E'})
print(newDict)

#copy
newDict1=newDict.copy()
print(newDict1)

#dict.get(key)
print("dict2.get('name')=",dict2.get('name'))

#dict.pop(key)
print('newDict before pop(10)',newDict)
newDict.pop(10)
print('newDict after pop(10)',newDict)

#dict.clear()
newDict.clear()
print('newDict.clear()',newDict)
     