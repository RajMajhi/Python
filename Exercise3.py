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
Questions:- 
1.Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
2.Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
3.Declare a variable named company and assign it to an initial value "Coding For All".
4.Print the variable company using print().
5.Print the length of the company string using len() method and print().
6.Change all the characters to uppercase letters using upper() method.
7.Change all the characters to lowercase letters using lower() method.
8.Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
9.Cut(slice) out the first word of Coding For All string.
10.Check if Coding For All string contains a word Coding using the method index, find or other methods.
11.Replace the word coding in the string 'Coding For All' to Python.
12.The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
13.Use the new line escape sequence to separate the following sentences.
I am enjoying this challenge.
I just wonder what is next.
14.Use a tab escape sequence to write the following lines.
Name      Age     Country   City
Asabeneh  250     Finland   Helsinki
15.Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
16.The area of a circle with radius 10 is 314 meters square.
17.Make the following using string formatting methods:
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
Info:- 
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
Questions:-
1.Declare an empty list

2.Declare a list with more than 5 items

3.Find the length of your list

4.Get the first item, the middle item and the last item of the list

5.Declare a list called mixed_data_types, put your(name, age, height, marital status, address)

6.Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.

7.Print the list using print()

8.Print the number of companies in the list

9.Print the first, middle and last company

10.Print the list after modifying one of the companies

11.Add an IT company to it_companies

12.Destroy the IT companies list

13.Join the following lists:

14.front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

'''
#TUPLE
"""
Info:-
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

>>> a=food_stuff_tp[3:5]
>>> print(a)
['tomato', 'potato']
>>> a=food_stuff_tp[3:6]
>>> print(a)
['tomato', 'potato', 'ladyfinger']

>>> nordic_countries=('Denmark','Estonia','Iceland','Norway','Sweden')
>>> 'Estonia'in nordic_countries
True
>>> 'Iceland' in nordic_countries
True

"""
Questions:-
Exercises: Level 1
1.Create an empty tuple
2.Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
3.Join brothers and sisters tuples and assign it to siblings
4.How many siblings do you have?
5.Modify the siblings tuple and add the name of your father and mother and assign it to family_members
Exercises: Level 2
1.Unpack siblings and parents from family_members
2.Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
3.Change the about food_stuff_tp tuple to a food_stuff_lt list
4.Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
5.Slice out the first three items and the last three items from food_stuff_lt list
6.Delete the food_stuff_tp tuple completely
7.Check if an item exists in tuple:
Check if 'Estonia' is a nordic country

Check if 'Iceland' is a nordic country

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
"""
