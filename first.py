#Commenting in python
# single line comment
''' multiline '''
""" this one too"""

print("hello world")
#print(5+8)

name = "Raj" # This is a string variable
age = 21 # This is an integer variable
print("My name is", name, "and I am", age, "years old.")

is_adult = True # This is a boolean variable

name = "Tony Stark"
age = 51
print (f"My name is {name} {age} years old. and i am a genius") #formatted string literals (f-strings)

name = input("Enter your name: ")
age = input("Enter your age: ")
print(f"My name is " + name + "and I am " + age + "years old.") # '+' concatenation
name = input("Enter your favourite superhero name: ")
print ("oh! Tony I like " + name + " too")


# Data Types and Type Conversion

old_age = input("Enter your age: ") # input() function always returns a string
new_age = int(old_age) + 1 # This will cause an error as we cannot add string and integer directly
print(new_age)

Error:
    new_age = old_age + 1
              ~~~~~~~~^~~
TypeError: can only concatenate str (not "int") to str

possible ways to fix the error:

old_age = 20 # directly assign an integer value
new_age = old_age + 1
print(new_age)


or 

old_age = input("Enter your age: ")
new_age = int(old_age) + 1 # convert string to integer using int() function
print(new_age)

# We can also convert to float (), str(),  bool() etc.

one more example:

first = input("Enter first number: ")
second = input("Enter second number: ")

sum = float(first) + float(second) # converting string to float
print(sum)

# string methods

name = "hello everyone"
print(name.upper()) # it make an entire new string in uppercase
HELLO EVERYONE
print(name.lower()) # same as above but lowercase
hello everyone
print (name.find("e")) # it returns the index of first occurrence of the substring
1
print(name.replace("everyone", "Guys")) # it replaces the substring with new substring
hello Guys
print(name.capitalize()) # it capitalizes the first character of the string
Hello everyone
print(name.title()) # it capitalizes the first character of each word in the string
Hello Everyone

#Keywords in python

name = "Alice"
print ('A' in name) # it checks whether the character is present in the string or not
True
print ('z' in name) # it checks whether the character is present in the string or not
False
print ('z' not in name) # it checks whether the character is absent in the string
True
print ('Alice' in name) # it checks whether the substring is present in the string or not
True
print ('bob'in name) # it checks whether the substring is present in the string or not
False
print ('bob' not in name) # it checks whether the substring is absent in the string
True

# Basic Arithmetic Operations
print(5+2)
7
print(5-2)
3
print(5*2)
10
print(5/2) # float division
2.5
print(5//2) # integer division (floor division)
2
print(5%2) # modulus operator
1
print(5**2) # exponentiation operator
25
print(5+2*3) # operator precedence
11
print((5+2)*3) # using parentheses to change precedence
21


#augmented assignment operators (Shorthand operators)
x = 5
x += 2 # x = x + 2
print(x)
7
x -= 2 # x = x - 2
print(x)
5
x *= 2 # x = x * 2
print(x)
10
x /= 2 # x = x / 2
print(x)
5.0
x //= 2 # x = x // 2
print(x)
2.0
x %= 2 # x = x % 2
print(x)  
0.0
x **= 2 # x = x ** 2
print(x)
0.0

# Comparison and Logical Operators
print(3>2) # greater than
True
print(3<2) # less than
False
print(3>=2) # greater than or equal to
True
print(3<=2) # less than or equal to
False
print(3==2) # equal to
False
print(3!=2) # not equal to
True
print(3==3) # equal to
True
print(3!=3) # not equal to
False
print((3>2) and (2<3)) # logical and
True
print((3>2) or (2>3)) # logical or
True
print(not(3>2)) # logical not
False
print(not(3<2)) # logical not
True
# operator precedence
print(3+2*2>7 and 5-3<4)
False
print(3+2*2>(7 and 5)-3<4)
True
print(3+2*2>7 and (5-3<4))
False

or operator  1 0  = 1 only when both are 0 it gives 0
and operator 1 0 = 0 only when both are 1 it gives 1
not operator 1 =0 and 0 =1


# Escape Sequences in Strings
print("Hello\nWorld") # \n is used for new line
Hello
World
print("Hello\tWorld") # \t is used for tab space
Hello   World
print("He said, \"Hello World\"") # \" is used to include double quote in string
He said, "Hello World"
print('It\'s a beautiful day') # \' is used to include single quote in string
It's a beautiful day
print("C:\\Users\\Username") # \\ is used to include backslash in string
C:\Users\Username
print("Hello\rWorld") # \r is used for carriage return
World
print("Hello\bWorld") # \b is used for backspace
HellWorld
print("Hello\fWorld") # \f is used for form feed
HelloWorld
print("Hello\vWorld") # \v is used for vertical tab
Hello
      World
# Raw Strings
print(r"C:\Users\Username") # r before the string makes it a raw string
C:\Users\Username
print(R"C:\Users\Username") # R before the string also makes it a raw string
C:\Users\Username

# String Slicing
name = "Christopher"
print(name[0]) # first character
C
print(name[3]) # fourth character
s
print(name[-1]) # last character
r
print(name[-3]) # third last character
t
print(name[0:5]) # substring from index 0 to 4
Chris
print(name[3:8]) # substring from index 3 to 7 


# Conditional Statements
#if
a=4
if a>0:
 print("a is greater and is a positive number.")
 
a is greater and is a positive number

#if else
age = int(input("Enter your age: ")) # This is an integer variable

age = 21 # This is an integer variable

if age >= 18:
    print("You are an adult.")
    print("You can vote.")
else:
    print("You are a minor.")
    print("You cannot vote.")

#if elif else
a=0
if a>0:
 print("a is a positive number.")
elif a<0:
 print("a is a negative number.")
else:
 print("a is equal to zero.")

a is equal to zero.

#list 
# Print the lists and its length
print('Fruits:', fruits)
print('Number of fruits:', len(fruits))
print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))
print('Animal products:',animal_products)
print('Number of animal products:', len(animal_products))
print('Web technologies:', web_techs)
print('Number of web technologies:', len(web_techs))
print('Countries:', countries)
print('Number of countries:', len(countries))
 
Fruits: ['banana', 'orange', 'mango', 'lemon']
Number of fruits: 4
Vegetables: ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
Number of vegetables: 5
Animal products: ['milk', 'meat', 'butter', 'yoghurt']
Number of animal products: 4
Web technologies: ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'MongDB']
Number of web technologies: 7
Countries: ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']
Number of countries: 5




