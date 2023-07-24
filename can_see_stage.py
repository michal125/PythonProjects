
arr = []
new_arr = []
def can_see_stage(arr):
    for x in arr:
        for y in x:
            new_arr.append(y)

    bTrue = 0
    bLevel = 0
    for i in range(len(new_arr)-1):
        if new_arr[i] < new_arr[i+1]:
            bTrue = 1
        else:
            if new_arr[i] == new_arr[i+1]:
                bTrue = 1
            else:
                bTrue = 0
                break


    if bTrue:
        print("True")
    else:
        print("False")

#can_see_stage([
#  [1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]
#])

#can_see_stage([
#  [0, 0, 0],
#  [1, 1, 1],
#  [2, 2, 2]
#])

can_see_stage([
  [0, 0, 1],
  [1, 1, 2],
  [3, 3, 4]
])