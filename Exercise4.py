#Sets
Exercise Level 1
>>> it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
>>> A = {19, 22, 24, 20, 25, 26}
>>> B = {19, 22, 20, 25, 26, 24, 28, 27}
>>> age = [22, 19, 24, 25, 26, 24, 25, 24]
>>> len(it_companies)
7
>>> it_companies.add('twitter')
>>> print(it_companies)
{'Amazon', 'Microsoft', 'twitter', 'Facebook', 'IBM', 'Apple', 'Oracle', 'Google'}
>>> new_set = {'AB','kateo','dontknow'}
>>> print(new_set)
{'dontknow', 'kateo', 'AB'}
>>> it_companies.update(new_set)
>>> print(it_companies)
{'Oracle', 'dontknow', 'twitter', 'Amazon', 'Microsoft', 'Facebook', 'IBM', 'Apple', 'kateo', 'Google', 'AB'}
>>> it_companies.remove('AB')
>>> print(it_companies)
{'Oracle', 'dontknow', 'twitter', 'Amazon', 'Microsoft', 'Facebook', 'IBM', 'Apple', 'kateo', 'Google'}
'''
>>>
In sets we have remove and discard that have basically same functionality 
but there is a minor difference i.e when we want to remove an item from a set which is not present ,
it will throw an error . But on the other hand if we do the same with discard it will not throw any 
exception or error and will execute the following set.
'''
"""
Questions:- 
# LEVEL 1
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
Exercises: Level 1
1.Find the length of the set it_companies
2.Add 'Twitter' to it_companies
3.Insert multiple IT companies at once to the set it_companies
4.Remove one of the companies from the set it_companies
5.What is the difference between remove and discard

"""
Exercise Level 2
>>> A = {19, 22, 24, 20, 25, 26}
>>> B = {19, 22, 20, 25, 26, 24, 28, 27}
>>> A.update(B)
>>> print(A)
{19, 20, 22, 24, 25, 26, 27, 28}
>>> A.intersection(B)
{19, 20, 22, 24, 25, 26, 27, 28}
>>> print(A.issubset(B))
True
>>> print(A.disjoint(B))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'set' object has no attribute 'disjoint'. Did you mean: 'isdisjoint'?
>>> print(A.isdisjoint(B))
False
>>> A.update(B)
>>> B.update(A)
>>> print(A , B)
{19, 20, 22, 24, 25, 26, 27, 28} {19, 20, 22, 24, 25, 26, 27, 28}
>>> A.symmetric_difference(B)
set()
>>> print(A.symmetric_difference(B))
set()
>>> del set
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'set' is not defined
>>> del A
>>> del B
>>> print (A,B)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'A' is not defined

"""
Questions:-
1.Join A and B
2.Find A intersection B
3 Is A subset of B
4.Are A and B disjoint sets
5.Join A with B and B with A
6.What is the symmetric difference between A and B
7.Delete the sets completely
"""

Exercise Level 3

>>> age = [22, 19, 24, 25, 26, 24, 25, 24]
>>> ages = set(age)
>>> print(ages)
{19, 22, 24, 25, 26}
>>> if len(age) == len(ages):
...     print("Both have same values")
... elif len(age) > len(ages):
...     print("age is bigger than ages")
... else:
...     print("ages is bigger than age")
...
age is bigger than ages

>>> a='I am a teacher and I love to inspire and teach people.'
>>> a.split()
['I', 'am', 'a', 'teacher', 'and', 'I', 'love', 'to', 'inspire', 'and', 'teach', 'people.']
>>> s = a.split()
>>> print(s)
['I', 'am', 'a', 'teacher', 'and', 'I', 'love', 'to', 'inspire', 'and', 'teach', 'people.']
>>> b= set(s)
>>> print(b)
{'teacher', 'teach', 'and', 'people.', 'inspire', 'love', 'I', 'am', 'a', 'to'}


"""
Convert the ages to a set and compare the length of the list and the set, which one is bigger?
I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
"""

#Dictionary 
>> dog = {}
>>> dog['name']= 'kuuta'
>>> dog['color']= 'Black'
>>> dog['breed']= 'german shepherd'
>>> dog['legs']= 4
>>> dog['age']=5
>>> print(dog)
{'name': 'kuuta', 'color': 'Black', 'breed': 'german shepherd', 'legs': 4, 'age': 5}

>>> student['first_name']='baji'
>>> student['last_name']='champiro'
>>> student['gender']='male'
>>> student['age']=69
>>> student['maritalstatus']='single'
>>> student['skills']='rizzer'
>>> student['country']='Indo'
>>> student['city']='Mumba'
>>> student['address']='zy colony 6 jroad'
>>> print(student)
{'first_name': 'baji', 'last_name': 'champiro', 'gender': 'male', 'age': 69, 'maritalstatus': 'single', 'skills': 'rizzer', 'country': 'Indo', 'city': 'Mumba', 'address': 'zy colony 6 jroad'}
>>> print(len(student))
9
>>> print('skills'in student)
True
>>> student['skills']='HTML'
>>> print(student)
{'first_name': 'baji', 'last_name': 'champiro', 'gender': 'male', 'age': 69, 'maritalstatus': 'single', 'skills': 'HTML', 'country': 'Indo', 'city': 'Mumba', 'address': 'zy colony 6 jroad'}
>>> del student
>>> print(student)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'student' is not defined

"""
Questions:-
1.Create an empty dictionary called dog
2.Add name, color, breed, legs, age to the dog dictionary
3.Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
4.Get the length of the student dictionary
5.Modify the skills values by adding one or two skills
6.delete the dictionary
"""
