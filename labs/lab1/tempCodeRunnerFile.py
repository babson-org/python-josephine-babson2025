def caesar_cipher():
    """
    Ask the user for text and a shift value.
    Provide options to encrypt or decrypt the text using a Caesar cipher.
    """

    print("you have some work todo!, caesar_cypher")

    # TODO: Get user input text
    text = input("Please enter text: ")

    # TODO: Get shift value
    while True:
        try: 
            shift = int(input("Enter shift value (1-25): "))
            if 1 <= shift <= 25:
                break
            else: print("shift must be between 1 and 25")
        except ValueError:
            print('Please enter an integer 1-25')

## ONLY ALLOW 1-25

    # TODO: Ask user whether to encrypt or decrypt
    choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()
    if choice == 'd':
        shift = -shift

    # TODO: Implement encryption and decryption logic

    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    length = len(alphabet)
    result = ""
    
    for char in text:
        if char in alphabet:
            idx = alphabet.index(char)             
            new_idx = (idx + shift) % length       
            result += alphabet[new_idx]            
        else:
            result += char 

    # TODO: Print the final result
    print("Result:", result)

# Uncomment to test Part 3
caesar_cipher()

