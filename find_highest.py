arr = []
def find_highest(arr):
    max_value = arr[0]
    arr.sort()
    for i  in range(len(arr)):
        if arr[0] < arr[i]:
            max_value = arr[i]
        
    print(max_value)

find_highest([0, 12, 4, 87])