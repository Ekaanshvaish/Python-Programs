L1=list(map(eval,input().split()))
L2=list(map(eval,input().split()))
L3=list(map(eval,input().split()))
l=len(L1)
for i in range(l):
	L4=[]
	L4.append(L1[i])
	L4.append(L2[i])
	L3.append(L4)
print(L3)