txt = "Please enter an odd number for the diamond height: "
while True:
    try:
        height = int(input("Enter an odd number for the diamond height: "))
        break
    except ValueError:
        txt = "A number for my kingdom, please"
    if height % 2 == 0:       # check if it's odd
            print("It must be odd, try again: ")
            continue
    break
