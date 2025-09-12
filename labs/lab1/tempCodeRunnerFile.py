def main():
    while True:
        print("Lab 1 - Python Basics")
        print("1. Draw Diamond")
        print("2. Text Analysis")
        print("3. Caesar Cipher")
        choice = input("Select part to run (1-3): ")
        
        if choice == "1":
            draw_diamond()
        elif choice == "2":
            text_analysis()
        elif choice == "3":
            caesar_cipher()
        else:
            exit()



"""
Lab 1 - Python Basics
Author: <Josephine Ashton>
Instructions: Complete each part below. Save your work and commit + sync in Codespaces.
"""

# ==============================
# Part 1: Draw a Diamond
# ==============================
def draw_diamond():
    """
    Ask the user for an odd number for the diamond height
    and print a symmetric diamond of that height.
    """
print("you have some work todo!, draw_diamond")


    # TODO: Prompt user for an odd number

txt = "Please enter an odd number for the diamond height: "
while True:
    try:
        height = int(input("Enter an odd number for the diamond height: "))
        if height % 2 == 0:       # check if it's odd
            print("It must be odd, try again: ")
            continue
        break  # valid odd number, exit loop
    except ValueError:
        txt = "A number for my kingdom, please"


    # TODO: Draw the top half of the diamond

for i in range(1, height + 1, 2):
        spaces = (height - i) // 2
        print(" " * spaces + "*" * i)

    # TODO: Draw the bottom half of the diamond
    
for i in range(height - 2, 0, -2):
        spaces = (height - i) // 2
        print(" " * spaces + "*" * i)

# Uncomment to test Part 1
draw_diamond()
