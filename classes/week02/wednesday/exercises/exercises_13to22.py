
from classes.week00.second_class.utils import clear_screen
'''
#13 - Conditional Logic
Ask the user for a number and print whether it is positive, negative, or zero.
'''
# enter code here

num = float(input('Enter a number: '))
if num > 0:
    print('Positive')
elif num < 0:
    print('Negative')
else:
    print("Zero")


pause=input('pause')
clear_screen()

'''
#14 - Even/Odd Check
Ask the user for a number and print if it is even or odd.
'''
# enter code here

num = float(input("Enter a number:"))

if num % 2 == 0:
    print('Even')
else:
    print('Odd')

pause=input('pause')
clear_screen()

'''
#15 - Boolean Operators
Ask the user for two numbers and check if both are positive, either is positive, or none is positive.
'''
# enter code here
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

if x > 0 and y > 0:                # both positive
    print("Both are positive")
elif x > 0 or y > 0:               # at least one positive
    print("At least one is positive")
else:
    print("None are positive")


pause=input('pause')
clear_screen()

'''
#16 - For Loop
Print all numbers from 1 to 20, skipping multiples of 3.
'''
# enter code here

for i in range(1, 21):     # numbers 1 through 20
    if i % 3 == 0:         # skip multiples of 3
        continue
    print(i)


pause=input('pause')
clear_screen()

'''
#17 - While Loop
Ask the user to guess a secret number (hardcoded) until they get it right.
'''
# enter code here ***************

secret = 7
guess = 0

while guess != secret:                 # keep looping until guess is correct
    guess = int(input("Guess the secret number: "))

print("You got it!")


pause=input('pause')
clear_screen()

'''
#18 - Break / Continue
Print numbers 1-10 but stop printing when you reach 7 and skip 3.
'''
# enter code here

for i in range(1, 11):
    if i == 3:        # skip 3
        continue
    if i == 7:        # stop at 7
        break
    print(i)


pause=input('pause')
clear_screen()

'''
#19 - Function Definition
Write a function square(x) that returns the square of a number and test it.
'''
# enter code here

def square(x):
    return x * x     # return gives the result back to the caller

print(square(4))     # test → prints 16
print(square(9))


pause=input('pause')
clear_screen()

'''
#20 - Function with Mutable Argument
Write a function add_item(lst, item) that appends item to lst and observe the effect on the original list.
'''
# enter code here

def add_item(lst, item):
    lst.append(item)     # append changes the original list

my_list = [1, 2, 3]
add_item(my_list, 4)
print(my_list)     



pause=input('pause')
clear_screen()

'''
#21 - Comments / Documentation
Write a function greet(name) with single-line and multi-line comments explaining each step.
'''
# enter code here

def greet(name):
    # This function greets the user by name (single-line comment)

    """
    Multi-line comment:
    1. Takes a name
    2. Prints a greeting with it
    """
    print("Hello,", name)

greet("Alice")



pause=input('pause')
clear_screen()

'''
#22 - Combining Tools
Ask the user to enter 5 names. Store them in a list, capitalize each name, sort the list, and print it.
'''
# enter code here

names = []                              # empty list

for i in range(5):                      # repeat 5 times
    name = input("Enter a name: ")
    names.append(name.capitalize())     # .capitalize() makes first letter uppercase

names.sort()                            # sort alphabetically
print(names)



pause=input('pause')
clear_screen()

