L=[ ]
for i in range(3):
    L2=[ ]
    for j in range(3):
        L2.append(int(input()))
    L.append(L2)
for i in range(3) :
       for j in range(3):
           if(i+j>=2):
             print(L[i] [j] ,end=" ")
           else:
             	print(" ",end=' ')
           	
       print()
	
