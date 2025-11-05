# Merges and Sorts the two lists into one new one --> combine = [1, 3, 6, 7, 15, 36, 39] (final level code)

left = [1, 7, 27, 36]
right = [3, 6, 15, 39]

def combine(left, right):
    array = []
    l_cur = 0
    r_cur = 0

    while l_cur < len(left) and r_cur < len(right): 
        if left[l_cur] < right[r_cur]:
            array.append(left[l_cur])
            l_cur += 1
        else:
            array.append(right[r_cur])
            r_cur += 1