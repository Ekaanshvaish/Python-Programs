x=4
y=8
count=0
sol=x^y
for i in range (32):
	if(sol>>i)&1==1:
		count=count+1
print(count)
	