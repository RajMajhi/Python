# Day2: 30 days of python programming
 first_name=('Raj')
>>> last_name=('Majhi')
>>> full_name=('RajMajhi')
>>> country='India'
>>> city="pune"
>>> age=21
>>> year=2026
>>> is_married=('single')
>>> is_true=('Really i am single')
>>> is_light_on="yes"
>>> x, y, z, a = 'x','y','z','a'
>>> print(first_name,last_name,full_name,country,city,age,year,is_married,is_true,is_light_on,xy,z,a)
Raj Majhi RajMajhi India pune 21 2026 single Really i am single yes x y z a

>>> type(first_name)
<class 'str'>
>>> type(last_name)
<class 'str'>
>>> type(full_name)
<class 'str'>
>>> type(country)
<class 'str'>
>>> type(city)
<class 'str'>
>>> type(age)
<class 'int'>
>>> type(year)
<class 'int'>
>>> type(is_married)
<class 'str'>
>>> type(is_true)
<class 'str'>
>>> type(is_light_on)
<class 'str'>
>>> type(x),type(y)
(<class 'str'>, <class 'str'>)
>>> type(z),(a)
(<class 'str'>, 'a')

>>> len(first_name)
3
>>> len(first_name),len(last_name)
(3, 5)
>>> num_one=5
>>> num_two=4
>>> num_three= (num_one+num_two)
>>> print(num_three)
9
>>> diff=(num_two-num_one)
>>> print(diff)
-1
>>> product=(num_two*num_one)
>>> print(product)
20
>>> division=(num_one/num_two)
>>> remainder=(num_two % num_one)
>>> print("division:", division,"remainder:", remainder)
division: 1.25 remainder: 4
>>> exp=(num_one**num_two)
>>> print(exp)
625
>>> floor_division=(num_one//num_two)
>>> print(floor_division)
1

>>> radius=30
>>> area_of_circle= 3.14 * (radius ** 2)
>>> print(area_of_circle)
2826.0
>>> circum_of_circle= 2 * 3.14 * radius
>>> print(area_of_circle)
2826.0
>>> print(circum_of_circle)
188.4
>>> r = int(input("Enter a number:"))
Enter a number:5
>>> a_o_c= 3.14 * (r**2)
>>> print(a_o_c)
78.5

>>> first_name=(input("what is your name?\n:"))
what is your name?
:Raj
>>> last_name=(input("what is your surname?\n:"))
what is your surname?
:Majhi
>>> country=(input("Enter the country!"))
Enter the country!India
>>> age=(input("age:"))
age:21
>>> print(first_name, last_name, country, age)
Raj Majhi India 21
>>> help('keywords')

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not



"""
Questions:- 

1.Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
2.Write a python comment saying 'Day 2: 30 Days of python programming'
3.Declare a first name variable and assign a value to it
4.Declare a last name variable and assign a value to it
5.Declare a full name variable and assign a value to it
6.Declare a country variable and assign a value to it
7.Declare a city variable and assign a value to it
8.Declare an age variable and assign a value to it
9.Declare a year variable and assign a value to it
10.Declare a variable is_married and assign a value to it
11.Declare a variable is_true and assign a value to it
12.Declare a variable is_light_on and assign a value to it
13.Declare multiple variable on one line

Exercises: Level 2
1.Check the data type of all your variables using type() built-in function
2.Using the len() built-in function, find the length of your first name
3.Compare the length of your first name and your last name
4.Declare 5 as num_one and 4 as num_two
5.Add num_one and num_two and assign the value to a variable total
6.Subtract num_two from num_one and assign the value to a variable diff
7.Multiply num_two and num_one and assign the value to a variable product
8.Divide num_one by num_two and assign the value to a variable division
9.Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
10.Calculate num_one to the power of num_two and assign the value to a variable exp
11.Find floor division of num_one by num_two and assign the value to a variable floor_division
12.The radius of a circle is 30 meters.
13.Calculate the area of a circle and assign the value to a variable name of area_of_circle
14.Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
15.Take radius as user input and calculate the area.
16.Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
17.Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
"""
