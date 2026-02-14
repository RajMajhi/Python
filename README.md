# Python Programming Language
Python basics to advance 
<br>
Exercise1= Variables, Builtin Functions.
<br>
Exercise2= Operators
<br>
Exercise3= Strings, Lists, Tuples
<br>
Exercise4= Sets, Dictionary
<br>
Exercise5= Conditionals, Loops
<br>
Exercise6= Functions,

Python is a high-level, interpreted programming language known for its simplicity and readability.  
It is widely used in web development, data science, artificial intelligence, automation, and scientific computing.

---

## 📦 Installation

### 1️⃣ Download Python

Download from the official website:

https://www.python.org/downloads/

During installation (Windows), make sure to check:

```
☑ Add Python to PATH
```

---

### 2️⃣ Verify Installation

Open terminal or command prompt:

```bash
python --version
```

or

```bash
python3 --version
```

---

## ⚙️ Using Python with Virtual Environment (Recommended)

Create a virtual environment:

```bash
python -m venv myenv
```

Activate:

**Windows**
```bash
myenv\Scripts\activate
```

**Mac/Linux**
```bash
source myenv/bin/activate
```

Deactivate:

```bash
deactivate
```

---

## 📓 Using Python with Jupyter Notebook

Install Jupyter:

```bash
pip install notebook
```

Start Jupyter:

```bash
jupyter notebook
```

Create a new Python notebook and start coding.

---

## 🚀 Basic Python Syntax

### 1️⃣ Print Statement

```python
print("Hello, World!")
```

---

### 2️⃣ Variables

```python
name = "Raj"
age = 21
height = 5.8
```

---

### 3️⃣ Data Types

```python
# Integer
x = 10

# Float
y = 3.14

# String
text = "Python"

# Boolean
flag = True

# List
numbers = [1, 2, 3]

# Dictionary
person = {"name": "Raj", "age": 21}
```

---

### 4️⃣ Conditional Statements

```python
age = 18

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

---

### 5️⃣ Loops

#### For Loop

```python
for i in range(5):
    print(i)
```

#### While Loop

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

---

### 6️⃣ Functions

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Raj"))
```

---

### 7️⃣ Classes (OOP Basics)

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."

s1 = Student("Raj", 21)
print(s1.introduce())
```

---

## 📦 Installing Packages

Install packages using pip:

```bash
pip install numpy
```

List installed packages:

```bash
pip list
```

---

## 📁 Running a Python Script

Save file as `main.py` and run:

```bash
python main.py
```

---

## 📚 Useful Libraries

- NumPy (Scientific computing)
- Pandas (Data analysis)
- Matplotlib (Visualization)
- Flask / Django (Web development)
- Scikit-learn (Machine learning)

---

## 🧠 Why Learn Python?

- Beginner-friendly
- Large community support
- Massive ecosystem of libraries
- Used in AI, ML, Quantum Computing, Web, Automation

---

Happy Coding 🚀


