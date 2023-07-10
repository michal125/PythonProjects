
txt = ""
def frequency_sort(txt):
    isUpper = 0
    new_arr = []
    for x in txt:
        if x.islower():
            isUpper = 0
        else:
            isUpper = 1
            pos = txt.index(x)
            break
    
    for y in txt:
        new_arr.append(y)    
    if isUpper == 0:
       new_arr.reverse()
       result = ''.join(new_arr)
    else:
       replace_char = new_arr[pos]
       new_arr.insert(pos+2, replace_char)
       new_arr.pop(pos)
       new_arr.reverse()
       result = ''.join(new_arr)
         
    print(result)
    
            
#frequency_sort("tree")
#frequency_sort("cccaaa")

frequency_sort("Aabb")
