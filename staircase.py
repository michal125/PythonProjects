
def staircase(n):
    hash_start = "#"
    under_start = "_"
    under_arr = []
    if n > 0:
        for i in range(n):
            under_arr.append(under_start)
    
        for j in range(n):
            under_arr[n-1-j] = hash_start
            result = ''.join(under_arr)
            print(result)
    
    else:
        n = -n
        for i in range(n):
             under_arr.append(hash_start)
        

        for j in range(n):
            result = ''.join(under_arr)
            print(result)
            under_arr[j] = under_start

#staircase(7)
staircase(-8)