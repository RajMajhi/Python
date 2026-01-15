>>>age=int(21)
>>>print(age)
21
>>> height=float(1)
>>> print(height)
1.0
>>> a= 1+3j
>>> print(a)
(1+3j)
>>> b=int(input("Enter base: "))
Enter base: 20
>>> h=int(input("Enter height: "))
Enter height: 10
>>> area = 0.5*b*h
>>> print("The area of the triangle is ",area)
The area of the triangle is  100.0

>>> a = int (input("Enter side a:"))
Enter side a:5
>>> b = int (input("Enter side b:"))
Enter side b:4
>>> c = int (input("Enter side c:"))
Enter side c:3
>>> perimeter = a+b+c
>>> print("The perimeter of the traingle is",perimeter)
The perimeter of the traingle is 12

>>> length=int(input())
10
>>> width=int(input())
20
>>> area=length * width
>>> perimeter= 2*(length * width)
>>> print ("area: ",area, "perimeter: ",perimeter)
area:  200 perimeter:  400

>>> r=7
>>> pi=3.14
>>> a=pi*(r**2)
>>> c=2*pi*r
>>> print('area: ',r , 'circumference:',c)
area:  7 circumference: 43.96
>>> a=3.14*(7**2)
>>> print(a)
153.86

 # Calculate the slope, x-intercept and y-intercept of y=2x-2
>>> slope=2
>>> y=-2
>>> x= -y/slope
>>> print(f'slope:',slope)
slope: 2
>>> print(f'y_intercept:',y)
y_intercept: -2
>>> print(f'x-intercept:',x)
x-intercept: 1.0

#Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)

>>> x1,y1,x2,y2 = 2,2,6,10
>>> m= (y2-y1)/(x2-x1)
>>> d= ((x2-x1)**2 + (y2-y1)**2)**0.5
>>> print('slope:',m)
slope: 2.0
>>> print('Euclidea distance:',d)
Euclidea distance: 8.94427190999916
# compared both the slopes
>>> if slope==m:
...     print("Both the slopes are equal")
... else:
...     print("The slopes are different")
...
Both the slopes are equal

#Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.

>>> x=-3
>>> y=x**2 +6*x+9
>>> print(y)
0

>>> len('python')
6
>>> len('dragon')
6
>>> n= len('python')
>>> p= len('dragon')
>>> print(n,p)
6 6

>>> if n==p:
...     print("false")
... else:
...     print("true")
...
false

>>> r=("on"in "python" and "dragon")
>>> print(r)
dragon
>>> r=('on'in'python')and('on'in'dragon')
>>> print(r)
True
>>> q="I hope this course in not full of jargoan"
>>> q=("jargoan"in"I hope this course in not full of jargoan")
>>> print(q)
True

>>> if "on"in"python" and "on"in"dragon":
...     print("there is no 'on' in both dragon and python")
... else:
...     print("")
...
there is no 'on' in both dragon and python

>>> a=len('python')
>>> b=float(a)
>>> c=str(b)
>>> print(a)
6
>>> print(b)
6.0
>>> print(c)
6.0

>>> num=int(input("Enter a number:"))
Enter a number:10
>>> if num % 2 == 0:
...     print("even")
... else:
...     print("not even")
...
even

>>> n=2.7
>>> a=int(n)
>>> b=7//3
>>> print(a)
2
>>> print(b)
2
>>> if a==b:
...     print("same")
... else:
...     print("not same")
...
same

>>> if type('10') == type(10):
...     print("equal")
... else:
...     print("not equal")
...
not equal

>>> if int('9.8')==10:
...     print()
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '9.8'

a=int(input("Enter hours"))
Enter hours 40
>>> b=int(input("Enter rate per hour:"))
Enter rate per hour:28
>>> c=a*b
>>> print("your weekly earning is"c)
your weekly earning is 1120

>>> a=int(input("Enter number of years you have lived: "))
Enter number of years you have lived: 100
>>>
>>> sec=60
>>> min=60
>>> hours=24
>>> daysin_y=365
>>> c=a*sec*min*hours*daysin_y
>>> print('you have lived for',c,'seconds')
you have lived for 3153600000 seconds




"""
Declare your age as integer variable
Declare your height as a float variable
Declare a variable that store a complex number
Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
    Enter base: 20
    Enter height: 10
    The area of the triangle is 100
Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
Enter side a: 5
Enter side b: 4
Enter side c: 3
The perimeter of the triangle is 12
Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
Calculate the slope, x-intercept and y-intercept of y = 2x -2
Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
Compare the slopes in tasks 8 and 9.
Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
Find the length of 'python' and 'dragon' and make a falsy comparison statement.
Use and operator to check if 'on' is found in both 'python' and 'dragon'
I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
There is no 'on' in both dragon and python
Find the length of the text python and convert the value to float and convert it to string
Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
Check if type of '10' is equal to type of 10
Check if int('9.8') is equal to 10
Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
Enter hours: 40
Enter rate per hour: 28
Your weekly earning is 1120
Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
Enter number of years you have lived: 100
You have lived for 3153600000 seconds.
Write a Python script that displays the following table
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
"""
