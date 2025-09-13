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

    # TODO: Count letters
letters = 0
for c in text:
    if c.isalpha():
        letters += 1

    # TODO: Count words
words = len(text.split())


    # TODO: Count sentences
sentences = 0
for c in text:
    if c in ".?!":
        sentences += 1

    # TODO: Print the results
print(f"Letters: {letters}")
print(f"Words: {words}")        # replace 0
print(f"Sentences: {sentences}")    # replace 0

# Uncomment to test Part 2
text_analysis()