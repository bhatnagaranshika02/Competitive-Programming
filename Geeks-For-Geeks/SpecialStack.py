def pop(arr):
    a=arr.pop()
    return a

# function should return 1/0 or True/False
def isFull(n, arr):
    if len(arr) == n:
        return 1
    return 0

# function should return 1/0 or True/False
def isEmpty(arr):
    if len(arr) == 0:
        return 1
    return 0

# function should return minimum element from the stack
def getMin(n, arr):
    return min(arr)
