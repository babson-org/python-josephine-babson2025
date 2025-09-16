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
        if i == 1:  # top tip (single star)
            print(" " * spaces + "*")
        else:  # outline: star + spaces + star
            print(" " * spaces + "*" + " " * (i - 2) + "*")

    # TODO: Draw the bottom half of the diamond
    
for i in range(height - 2, 0, -2):
        spaces = (height - i) // 2
        if i == 1:  # bottom tip (single star)
            print(" " * spaces + "*")
        else:  # outline
            print(" " * spaces + "*" + " " * (i - 2) + "*")

# Uncomment to test Part 1
draw_diamond()
