test_str = input().lower()
dicx = {} 
for i in test_str: 
   if i in dicx: 
    dicx[i] += 1
   else: 
     dicx[i] = 1
print(dicx)