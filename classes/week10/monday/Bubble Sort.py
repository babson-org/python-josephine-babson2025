

''' 
CHAT VERSION
numbers = [1, 3, 5, 4, 2]

# Bubble Sort Algorithm
for i in range(len(numbers) - 1):            # Outer loop for each pass
    for j in range(len(numbers) - 1 - i):    # Inner loop for comparisons
        if numbers[j] > numbers[j + 1]:      # Swap if out of order
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("Bubble Sort:", numbers)

'''

# Class Version

def bubble_sort(values):
    sorted = values.copy() # make copy so you don't have to change raw data in case needed for something else later
    size = len(sorted)

    for pass_num in range(size - 1):
        swaps = False
        for idx in range(size - 1 - pass_num):
            if sorted[idx] > sorted[idx + 1]:
                sorted[idx], sorted[idx + 1] = sorted[idx + 1], sorted[idx]
                swaps = True
        if not swaps: break

    return sorted

# Merges and Sorts the two lists into one new one --> combine = [1, 3, 6, 7, 15, 36, 39]

left = [1, 7, 27, 36]
right = [3, 6, 15, 39]

def combine(left, right):
    array = []
    l_cur = 0
    r_cur = 0

    cnt = 0 # sets up so its not a infinite loop, debugging trick

    while cnt < 50: #not infinite, stops after 50 times through
        cnt += 1