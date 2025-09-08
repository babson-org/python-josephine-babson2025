
'''
# 1

Write down the steps a program would need to make a cup of tea. Then implement a Python 
function make_tea() that prints each step.
'''
# enter your code here

def make_tea():
    print("Step 1: Boil water")
    print("Step 2: Place a teabag in the cup")
    print("Step 3: Pour hot water into the cup")
    print("Step 4: Let the tea steep for a few minutes")
    print("Step 5: Remove the teabag")
    print("Step 6: Add sugar or milk if desired")
    print("Step 7: Stir and enjoy your tea!")

make_tea()



pause=input('pause')
clear_screen()
'''
#2

Given a list [2, 4, 6, 8, 10], write a program that prints the next three numbers in the list.  
(the ones after 10)
'''
# enter your code here

numbers = [2, 4, 6, 8, 10]

last_number = numbers[-1]  # get the last element (10)
step = numbers[1] - numbers[0]  # difference between consecutive numbers (2)

for i in range(1, 4):
    print(last_number + i * step)


pause=input('pause')
clear_screen()
'''
#3

Write a program that asks the user for their first and last name, then prints a greeting:
"Hello, <first name> <last name>!"
'''
# enter your code here
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

print(f"Hello, {first_name} {last_name}!")


pause=input('pause')
clear_screen()
'''
#4

Write a program that prints your Python version and platform using the sys and platform modules.
'''
# enter your code here



pause=input('pause')
clear_screen()
'''
#5

Ask the user to input two numbers. Calculate and print their sum, difference, product, 
and division (both / and //).
'''
# enter your code here

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Division (/):", num1 / num2)
print("Floor Division (//):", num1 // num2)


pause=input('pause')
clear_screen()
'''
#6

Ask the user to input a sentence. Print it in uppercase, lowercase, with the first letter 
capitalized, and split it into words.
'''

# enter your code here

sentence = input("Enter a sentence: ")

print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())
print("Capitalized:", sentence.capitalize())
print("Split into words:", sentence.split())


pause=input('pause')
clear_screen()
'''
#7

Calculate the result of the following without parentheses and then with parentheses:
10 + 2 * 5 / 2 - 3 ** 2
'''
# enter your code here

result1 = 10 + 2 * 5 / 2 - 3 ** 2
print("Without parentheses:", result1)

# With parentheses (example: group addition first)
result2 = (10 + 2) * 5 / (2 - 3) ** 2
print("With parentheses:", result2)

pause=input('pause')
clear_screen()
'''
#8

Create a list of your three favorite foods. Replace the second item with a new one, 
then print the list.
'''
# enter your code here

foods = ["Pizza", "Sushi", "Tacos"]
foods[1] = "Burgers"  # replace 2nd item

print("Updated list:", foods)


pause=input('pause')
clear_screen()
'''
#9

Create a tuple with four numbers. Try to change the first number (observe the error) 
and then print the tuple.
'''
# enter your code here
numbers = (1, 2, 3, 4)

try:
    numbers[0] = 10
except TypeError as Error:
    print("Error:", Error)

print("Tuple:", numbers)


pause=input('pause')
clear_screen()
'''
#10

Create a dictionary representing a student (name, age). Update the age. Create a list of 
favorite numbers and add a new number.
'''
# enter your code here

student = {"name": "Alice", "age": 20}

# update age
student["age"] = 21

# add favorite numbers
favorite_numbers = [3, 7, 12]
favorite_numbers.append(42)

print("Student:", student)
print("Favorite numbers:", favorite_numbers)



pause=input('pause')
clear_screen()
'''
#11

Ask the user to input their favorite quote. Save it to a file quotes.txt 
and read it back to print it.
'''
# enter your code here

quote = input("Enter your favorite quote: ")

with open("quotes.txt", "w") as file:
    file.write(quote)

with open("quotes.txt", "r") as file:
    print("Your saved quote:", file.read())


pause=input('pause')
clear_screen()
'''
#12
Ask the user to input 5 numbers (one at a time), store them in a list, and print the sum and average.
'''
# enter your code here

numbers = []

for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

total = sum(numbers)
average = total / len(numbers)

print("Sum:", total)
print("Average:", average)


pause=input('pause')
clear_screen()