#Function

LEVEL 1

def add_two_numbers():
    a=5
    b=10
    sum=a+b
    print('The sum of a & b :',sum)
add_two_numbers()
>>>The sum of a & b : 15

def area_of_circle():
    PI=3.14
    r=int(input("Enter radius :"))
    area = PI*r**2
    print("area:",area)
area_of_circle()
>>>Enter radius :5
area: 78.5

def add_all_nums(*args):
    for item in args:
        if not isinstance(item, (int, float)):
            return f"Error: '{item}' is not a number. Please provide only numeric values."

    # If all are numbers, sum them
    total = sum(args)
    return total
    
print(add_all_nums(1, 2, 3, 4))        # Output: 10
print(add_all_nums(1, 2, "3", 4))      # Output: Error message
>>> ERROR!
10
Error: '3' is not a number. Please provide only numeric values.


def convert_cto_f():
    c=int(input("celsius: "))
    f=(c*9/5)+32
    print("fahrenheit: ",f)
convert_cto_f()
>>> celsius: 10
fahrenheit:  50.0

def check_season(month):
    month=str(month).strip().lower()
    
    if month in ['december','january','february','12','1','2']:
        return 'winter'
    elif month in ['march','april','may','3','4','5']:
        return 'spring'
    elif month in ['june','july','august','6','7','8']:
        return 'summer'
    elif month in ['september','october','november','9','10','11']:
        return 'autumn'
    else:
        print("Invalid_input!")
print(check_season('MAY'))
>>> spring


