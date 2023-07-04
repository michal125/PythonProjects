
txt = ""
n = 0 
def collect(txt,n):
    arr = []
    i = 0
    j = 0
    new_txt = ""
    if n>0:
        for x in txt:
            i += 1
            j += 1
            bValue = 0
            if i <= n:
                new_txt += x
            else:
                arr.append(new_txt)
                i = 1
                new_txt = ""
                new_txt += x
                bValue = 1
            if len(txt) == j and n < 5:
                arr.append(new_txt)
       
        arr.sort()
        print(arr)
    else:
        print(arr)
        
collect("intercontinentalisationalism", 6)
#collect("strengths", 3)