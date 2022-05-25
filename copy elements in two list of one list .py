L=[]
n=int(input("enter size"))
for i in range(n):
    x=int(input("enter no"))
    L.append(x)
print("element",L)
B=[]
C=[]
for i in range(n):
	if L[i]>0:
		B.append(L[i])
	else:
		C.append(L[i])
print("elements in  second list",B)
print(" elements in third list",C)
