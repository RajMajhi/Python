#Conditionals
'''
If Condition
If Else
If Elif Else
Short Hand
Nested Conditions
If Condition and Logical Operators
If and Or Logical Operators
'''
Level 1
>>> age=int(input('Enter your age:'))
Enter your age:30
>>> print("You are old enough to drive") if age>18else print('You need',18-age,'more years to learn to drive')
You are old enough to drive
>>> print(age)
30
>>> age=int(input('Enter your age:'))
Enter your age:15
>>> print("You are old enough to drive") if age>18else print('You need',18-age,'more years to learn to drive')
You need 3 more years to learn to drive

>>> age=int(input('Enter your age:'))
Enter your age:21
 print("You are younger than me.") if age<30 else print('You are',30-age,'years older than me.')
You are younger than me.
>>> age=int(input('Enter your age:'))
Enter your age:36
>>> print("You are younger than me.") if age<30 else print('You are',age-30,'years older than me.')
You are 6 years older than me.

>>> a=int(input('enter a number:'))
enter a number:10
>>> b=int(input('Enter a number:'))
Enter a number:20
>>> if a > b:
...     print('a is greater')
... elif b > a:
...     print('a is smaller')
... else:
...     print('both are equal')
...
a is smaller

"""
Questions:- 
1.Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:

Enter your age: 30
You are old enough to learn to drive.
Output:
2.Enter your age: 15
You need 3 more years to learn to drive.
3.Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:

4.Enter your age: 30
You are 5 years older than me.
5.Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:

Enter number one: 4
Enter number two: 3
4 is greater than 3
"""
Level 2

m=int(input("Enter your marks:"))
if m>=90 and m<100:
    print("A")
elif m>=80 and m<=89:
    print("B")
elif m>=70 and m<=79:
    print("C")
elif m>=60 and m<=69:
    print("D")
else:
    print("F")

Enter your marks:92
A
Enter your marks:86
B
Enter your marks:77
C
Enter your marks:60
D
Enter your marks:59
F

m=input("Enter the month:")
a=['September','October','November']
w=['January','December','February']
S=['March','April','May']
s=['June','July','August']
if m in a:
    print("The season is Autumn")
elif m in w:
    print("The season is Winter")
elif m in S:
    print("The season is Spring")
elif m in s:
    print("The season is Summer")
else:
    print("Entered season is wrong or please type first letter in CAP then all small!")
    
Enter the month:january
Entered season is wrong or please type first letter in CAP then all small!

Enter the month:July
The season is Summer

Enter the month:February
The season is Winter

fruits=['banana','orange','mango','lemon']
f=input("Enter a fruits:")

if f in fruits:
    print("that fruit already exist in the list.")
else:
    fruits.append(f)
print(fruits)
    
Enter a fruits:banana
that fruit already exist in the list.

Enter a fruits:apple
['banana', 'orange', 'mango', 'lemon', 'apple']
"""
Questions:- 
1.Write a code which gives grade to students according to theirs scores:
```sh
90-100, A
80-89, B
70-79, C
60-69, D
0-59, F
```
2.Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
3.The following list contains some fruits:
```sh
fruits = ['banana', 'orange', 'mango', 'lemon']
```

4.If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')

"""
# loops
for i in range(11):
    print(i)
0
1
2
3
4
5
6
7
8
9
10

i=0
while i<11:
    print(i)
    i=i+1
0
1
2
3
4
5
6
7
8
9
10

i=10
while i<=10 and i>=0:
    print(i)
    i=i-1
10
9
8
7
6
5
4
3
2
1
0

for i in range(10,-1,-1):
    print(i)
10
9
8
7
6
5
4
3
2
1
0

for i in range(1,8):
    print('#'*i)
#
##
###
####
#####
######
#######

for i in range(0,11,+1):
    a=i*i
    print(i,'x',i,'=',a)
  
0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100
