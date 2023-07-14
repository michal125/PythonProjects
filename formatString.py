#Ariston

s =""
def formatString(s):
    cnt = 0
    process_cnt = 0
    arr = []
    result = ""
    for x in s:
        process_cnt += 1
        if x != '-' and x != ' ':
            cnt += 1
            arr.append(x)
            if len(arr) == 3:
                result += ''.join(arr)+' '
                arr = []
                cnt = 0
        if x == '-' and x == ' ':
            cnt -= 1
            continue
        
        
    if len(result)%3 == 0 and len(arr) == 1:
        change_result = result[-4:-1]
        change_result = change_result + s[-1]
        arr_new = []
        change_result_cnt = 0
        result2 = ""
        result3 = ""
        for j in change_result:
            change_result_cnt += 1
            result2 += j
            if change_result_cnt == 2:
                arr_new.append(result2)
                change_result_cnt = 0
                result2 = ""
                result3 += "".join(arr_new)+" "
                arr_new = []
        result = result.replace(result[-4:-1],result3)
        
    print(result)
 
#formatString('ABC123DEF')
formatString("00-- 123-234 21")