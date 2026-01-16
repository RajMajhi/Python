#STRING

>>> r='Thirty'+'Days'+'Of'+'Python'
>>> print(r)
ThirtyDaysOfPython
>>> r='Thirty '+'Days '+'Of'+' Python'
>>> print(r)
Thirty Days Of Python
>>> t='Coding '+'For '+'All'
>>> print(t)
Coding For All
>>> company='Coding For All'
>>> print(company)
Coding For All
>>> print(len('company'))
7
>>> company.upper()
'CODING FOR ALL'
>>> company.lower()
'coding for all'
>>> company.capitalize()
'Coding for all'
>>> company[1:14]
'oding For All'
>>> company.title()
'Coding For All'
>>> company.swapcase()
'cODING fOR aLL'
>>> company[0:1]
'C'
>>> company[:1]
'C'
>>> company[:0]
''
>>> company[-13]
'o'
>>> company[1:14]
'oding For All'
>>> print(company.find('Coding'))
0
>>> print(company.replace('Coding For All','Python'))
Python
>>> a=['Django','Flask','Bottle','Pyramid','Falcon']
>>> r= '#' . join(a)
>>> print(r)
Django#Flask#Bottle#Pyramid#Falcon

>>> print('I am enjoying this challenge.\nI just wonder what is next.')
I am enjoying this challenge.
I just wonder what is next.

>>> print("""Name\t Age\t country\t City\n Raj\t 101\t India\t abrakadabra """)
Name     Age     country         City
 Raj     101     India   abrakadabra

>>> print('radius = 10 \narea = 3.14 * radius ** 2 \nThe area of a circle with radius 10 is 314 meters square')
radius = 10
area = 3.14 * radius ** 2
The area of a circle with radius 10 is 314 meters square
>>> a=8
>>> b=6
>>> print('{}+{}={}'.format(a, b,a+b))
8+6=14
>>> print('{} + {} = {}'.format(a, b,a+b))
8 + 6 = 14
>>> print('8 + 6 = 14\n8 - 6\n8 * 6 = 48\n8 / 6 = 1.33\n8 % 6 = 2\n8 // 6 = 1\n8 ** 6 = 262144')
8 + 6 = 14
8 - 6
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144
'''
Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
Declare a variable named company and assign it to an initial value "Coding For All".
Print the variable company using print().
Print the length of the company string using len() method and print().
Change all the characters to uppercase letters using upper() method.
Change all the characters to lowercase letters using lower() method.
Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
Cut(slice) out the first word of Coding For All string.
Check if Coding For All string contains a word Coding using the method index, find or other methods.
Replace the word coding in the string 'Coding For All' to Python.
The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
Use the new line escape sequence to separate the following sentences.
I am enjoying this challenge.
I just wonder what is next.
Use a tab escape sequence to write the following lines.
Name      Age     Country   City
Asabeneh  250     Finland   Helsinki
Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
The area of a circle with radius 10 is 314 meters square.
Make the following using string formatting methods:
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144
'''
#>>>Data type datatype.
'''
There are four collection data types in Python :

List: is a collection which is ordered and changeable(modifiable). Allows duplicate members.
Tuple: is a collection which is ordered and unchangeable or unmodifiable(immutable). Allows duplicate members.
Set: is a collection which is unordered, un-indexed and unmodifiable, but we can add new items to the set. Duplicate members are not allowed.
Dictionary: is a collection which is unordered, changeable(modifiable) and indexed. No duplicate members.
'''
# LIST

>>> lst= list()
>>> print(len(lst))
0
>>> l=['a','s','f','d','w','k']
>>> print(len(l))
6
>>> l=['a','s','f','d','w','k']
>>> a=l[0]
>>> print(a)
a
>>> a=l[2]
>>> print(a)
f
>>> a=l[5]
>>> print(a)
k
>>> mixed_data_types=['Raj',21,'1000','single','xy colony hsad64']
>>> print(mixed_data_types)
['Raj', 21, '1000', 'single', 'xy colony hsad64']

>>> it_companies=['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
>>> print(it_companies)
['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
>>> print("No.of companies:",len(it_companies))
No.of companies: 7

>>> it_companies=['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
>>> print(it_companies)
['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
>>> a=it_companies[0]
>>> print(a)
Facebook
>>> a=it_companies[3]
>>> print(a)
Apple
>>> a=it_companies[6]
>>> print(a)
Amazon
>>> it_companies.append('Itcom')
>>> print(it_companies)
['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon', 'Itcom']

>>> del it_companies
>>> print(it_companies)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'it_companies' is not defined

>>> front_end=['HTML','CSS','JS','React','Redux']
>>> back_end=['Node','Express','MongoDB']
>>> print(front_end+back_end)
['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']

'''
Declare an empty list

Declare a list with more than 5 items

Find the length of your list

Get the first item, the middle item and the last item of the list

Declare a list called mixed_data_types, put your(name, age, height, marital status, address)

Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.

Print the list using print()

Print the number of companies in the list

Print the first, middle and last company

Print the list after modifying one of the companies

Add an IT company to it_companies

Destroy the IT companies list

Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

'''
#TUPLE
"""
A tuple is a collection of different data types which is ordered and unchangeable (immutable). Tuples are written with round brackets, (). Once a tuple is created, we cannot change its values. We cannot use add, insert, remove methods in a tuple because it is not modifiable (mutable). Unlike list, tuple has few methods. Methods related to tuples:

tuple(): to create an empty tuple
count(): to count the number of a specified item in a tuple
index(): to find the index of a specified item in a tuple
+ operator: to join two or more tuples and to create a new tuple
"""
>>> tlp=()
>>> print(len(tlp))
0
>>> tlp=('xy','yx','ab','ba')
>>> del tlp
>>> print(tlp)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'tlp' is not defined

>>> sisters=('xy','yx')
>>> brothers=('ab','yb')
>>> siblings=(sisters+brothers)
>>> print(siblings)
('xy', 'yx', 'ab', 'yb')
>>> print("How many siblings do you have?\nSiblings:",len(siblings))
How many siblings do you have?
Siblings: 4
>>> siblings=('mother','father')
>>> family_members=siblings
>>> print(family_members)
('mother', 'father')
>>> siblings=family_members
>>> print(siblings)
('mother', 'father')
>>> fruits =('banana','apple','orange')
>>> vegetables =('tomato','potato','ladyfinger')
>>> animalproducts=('aaa','ggg','sss')
>>> food_stuff_tp=(fruits+vegetables+animalproducts)
>>> print(food_stuff_tp)
('banana', 'apple', 'orange', 'tomato', 'potato', 'ladyfinger', 'aaa', 'ggg', 'sss')
>>> lst=list(food_stuff_tp)
>>> print(lst)
['banana', 'apple', 'orange', 'tomato', 'potato', 'ladyfinger', 'aaa', 'ggg', 'sss']
>>> print(food_stuff_tp)
('banana', 'apple', 'orange', 'tomato', 'potato', 'ladyfinger', 'aaa', 'ggg', 'sss')

>>> print(lst)
['banana', 'apple', 'orange', 'tomato', 'potato', 'ladyfinger', 'aaa', 'ggg', 'sss']
>>> print(food_stuff_tp)
('banana', 'apple', 'orange', 'tomato', 'potato', 'ladyfinger', 'aaa', 'ggg', 'sss')
>>> l=len(food_stuff_tp)
>>> print(l)
9
>>> m_l= l//2
>>> print(m_l)
4
>>> r=food_stuff_tp[:m_l]+food_stuff_tp[m_l+1:]
>>> print(r)
('banana', 'apple', 'orange', 'tomato', 'ladyfinger', 'aaa', 'ggg', 'sss')

>>> del food_stuff_tp
>>> print (food_stuff_tp)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'food_stuff_tp' is not defined
>>>
