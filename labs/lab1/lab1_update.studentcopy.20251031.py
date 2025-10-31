# ==============================
# Main Program
# ==============================
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
# Part 1: Draw a Diamond FIX TO BE JUST THE OUTLINE
# ==============================

# Steps to solve:
# 1. Ask the user for an odd number between 3 and 15 for the height of the diamond.
# 2. Make sure the number is valid (odd, in range).
# 3. Use a loop to print the top half of the diamond:
#    - Start with 1 star and go up by 2 each row until reaching the height.
#    - Decrease spaces each row so stars are centered.
# 4. Use another loop to print the bottom half of the diamond:
#    - Start with height-2 stars and go down by 2 until 1.
#    - Increase spaces each row so the diamond stays centered.

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
            height = int(input(txt))
            if height % 2 == 0:       # check if it's odd
                print("It must be odd, try again: ")
                continue
            break  # valid odd number, exit loop
        except ValueError:
            txt = "Please enter an odd integer"


    # TODO: Draw the top half of the diamond

    for i in range(1, height + 1, 2):
            spaces = (height - i) // 2
            if i == 1: 
             print(" " * spaces + "*")
            else:  
                print(" " * spaces + "*" + " " * (i - 2) + "*")

    # TODO: Draw the bottom half of the diamond

    for i in range(height - 2, 0, -2):
            spaces = (height - i) // 2
            if i == 1:  
                print(" " * spaces + "*")
            else:  
                print(" " * spaces + "*" + " " * (i - 2) + "*")

# Uncomment to test Part 1
draw_diamond()


# ==============================
# Part 2: Count Letters, Words, and Sentences
# ==============================

# Steps to solve:
# 1. Ask the user to enter a block of text.
# 2. Count the number of letters:
#    - Using a for loop
#    - Go through each character.
#    - If it's a letter (a–z or A–Z), add 1 to the count.
# 3. Count the number of words:
#    - Split the text by spaces using .split().
#    - Count how many words are in the list.
# 4. Count the number of sentences:
#    - Look at each character in the text.
#    - If it’s a '.', '!', or '?', add 1 to the sentence count.
# 5. Print the counts for letters, words, and sentences.

def text_analysis():
    """
    Ask the user for a block of text.
    Count and display:
        - Number of letters (only count a-zA-Z)
        - Number of words   (use split())
        - Number of sentences (., ?, !) 
    """

    print("you have some work todo!, text_analysis")

    # TODO: Get user input
    text = input("Enter some text: ")

    '''initialize counters
    letters= 0
    words= 1
    sentences = 0 
    '''

    # TODO: Count letters
    letters = 0
    for char in text:
        if char.isalpha():
            letters += 1

    # TODO: Count words
    words = len(text.split())


    # TODO: Count sentences
    
    sentences = 0
    for char in text:
        if char in ".?!":
            sentences += 1

    # TODO: Print the results
    print(f"Letters: {letters}")
    print(f"Words: {words}")        
    print(f"Sentences: {sentences}")    

# Uncomment to test Part 2
text_analysis()


# ==============================
# Part 3: Caesar Cipher – Encrypt and Decrypt
# ==============================

# Steps to solve:
# 1. Ask the user to enter a message (text).
# 2. Ask the user to enter a shift value between 1 and 25.
#    - Keep asking until they give a valid number.
# 3. Ask if they want to encrypt (shift forward) or decrypt (shift backward).
#    - If decrypt, flip the shift to negative.
# 4. Make an alphabet list (a–z).
# 5. For each character in the text:
#    - If it’s a letter, find its position in the alphabet.
#    - Shift it by the shift value (using shifted alphabet).
#    - Add the new letter to the result string.
#    - If it’s not a letter (like a space or punctuation), just add it as-is.
# 6. Print out the final result (encrypted or decrypted text).


def caesar_cipher():
    """
    Ask the user for text and a shift value.
    Provide options to encrypt or decrypt the text using a Caesar cipher.
    """

    # 1. Get user text
text = input("Please enter text: ")

    # 2. Get valid shift value (1–25 only)
while True:
        try: 
            shift = int(input("Enter shift value (1-25): "))
            if 1 <= shift <= 25:
                break
            else:
                print("Shift must be between 1 and 25")
        except ValueError:
            print("Please enter an integer 1-25")

    # 3. Ask user to encrypt or decrypt
choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()
if choice == 'd':
        shift = -shift   # go backwards if decrypting

    # 4. Caesar cipher logic
alphabet = list("abcdefghijklmnopqrstuvwxyz")
length = len(alphabet)
result = ""


shifted_alphabet = alphabet[shift:] + alphabet[:shift] #make shifted alphabet

result = ""

for char in text:
    if char in alphabet:
        idx = alphabet.index(char)     # where the letter is
        result += shifted_alphabet[idx] # grab shifted letter directly
    else:
        result += char

    # TODO: Print the final result
    print("Result:", result)

# Uncomment to test Part 3
caesar_cipher()




if __name__ == "__main__":
    main()