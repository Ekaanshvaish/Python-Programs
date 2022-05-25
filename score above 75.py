result={}
n=int(input("enter no of students"))
for i in range(n):
	print("enter details of student no",i+1)
	rno=int( input("roll no"))
	name=input("name")
	marks=int(input("marks"))
	result[rno]=[name,marks]
print(result)
for student in result :
	if result[student]>75:
	 print(result[student])
	 