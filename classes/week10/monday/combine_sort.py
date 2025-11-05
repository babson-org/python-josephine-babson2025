
# List [5,4,3,2,1] sort but using combine logic
from combine import combine as cx
def combine_sort(unsorted):

    size = len(unsorted)

    left = unsorted[0:1]
    for idx in range(1, size):
        right = unsorted[idx : + 1]
        left = cx(left, right)

    return left

print(combine_sort([5,4,3,2,1]))