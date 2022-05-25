d={}
x=int(input())
for i in range(x):
	k=int(input())
	v=int(input())
	d.update({k:v})
print(d)
print(d.values())
print(d.keys())
print(d.items())
print(sum(d.values()))