def caesar_cipher():
    """
    Ask the user for text and a shift value.
    Provide options to encrypt or decrypt the text using a Caesar cipher.
    """

    print("you have some work todo!, caesar_cypher")

    # TODO: Get user input text
    text = input("Enter text: ")

    # TODO: Get shift value
    shift = int(input("Enter shift value (integer): "))

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
            idx = alphabet.index(char)             # find current letter’s spot
            new_idx = (idx + shift) % length       # move forward or backward
            result += alphabet[new_idx]            # add new shifted letter
        else:
            result += char 

    # TODO: Print the final result
    print("Result:", result)

# Uncomment to test Part 3
caesar_cipher()