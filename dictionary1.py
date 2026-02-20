Num=set([10,20,30,40,50]) 
Num.add(60) 
print(Num) 

#!/usr/bin/Python
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])

dict = {'Name': 'hitesh', 'Age': 7, 'Class': 'First'}
dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School"; # Add new entry
print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])

dict = {'Name': 'hitesh', 'Age': 7, 'Class': 'First'}
del dict['Name']; # remove entry with key 'Name'
dict.clear(); # remove all entries in dict
del dict ; # delete entire dictionary

dict = {'Name': 'hitesh', 'Age': 7, 'Class': 'First'}
for key, value in dict.items():
    print(key, ' - ', value)
    
    