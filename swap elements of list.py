L=[]
n=int(input("enter size"))
for i in range(n):
    x=int(input("enter no"))
    L.append(x)
print("element",L)
for i in range(0,n,2):
	L[i],L[i+1]=L[i+1],L[i]
print("list after swp",L)
