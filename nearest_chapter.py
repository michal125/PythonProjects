import math

new_dict = {}
page = 0

def nearest_chapter(new_dict,page):
   new_val = ""
   new_val = new_dict.values()
   new_arr = []
   arr_keys = []
   pos = 0
   bMin = 0
   bCnt = 0
   
   for x in new_val:
       new_arr.append(x-page)

   new_arr.sort()
   for y in new_arr:
       if y < 0:
          pos += 1
          new_arr.remove(y)
          bMin = 1
       cnt = new_arr.count(y)
       if cnt >= 2:
            index = new_arr.list(y)
            bCnt = 1
            break
   
   if bCnt == 0:           
        min_val = min(new_arr)
        index = new_arr.index(min_val)
   if bMin:
        index = index+pos
   arr_keys = list(new_dict.keys())
   print(arr_keys[index])
   
       
       
   
     
#nearest_chapter({
#  "Chapter 1" : 1,
#  "Chapter 2" : 15,
#  "Chapter 3" : 37
#}, 10)


#nearest_chapter({
#  "New Beginnings" : 1,
#  "Strange Developments" : 62,
#  "The End?" : 194,
#  "The True Ending" : 460
#}, 200)

nearest_chapter({
  "Chapter 1a" : 1,
  "Chapter 1b" : 5
}, 3)
        
        