
arr = []

def same_vowel_group(arr):
    vawel_arr = ['a','e','i','o','u','y']
    j = 0
    new_arr = []
    vawel_arr_exp = []
    first_word = arr[0]
    for x in first_word:
        if x in vawel_arr:
            vawel_arr_exp.append(x)
    cnt_vawel = len(vawel_arr_exp)

    for word in arr:
       for char in word:
           if char in vawel_arr_exp:
               j += 1
           if j == cnt_vawel:
               new_arr.append(word)
               j = 0
               
    print(new_arr)
    
#same_vowel_group(["toe", "ocelot", "maniac"])

same_vowel_group(["hoops", "chuff", "bot", "bottom"])
        
        
            