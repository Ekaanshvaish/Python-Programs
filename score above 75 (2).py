result={}
n=int(input("enter no of students"))
for i in range(n):
	print("enter details of student no",i+1)
	rno=int( input("roll no"))
	name=input("name")
	marks=int(input("marks"))
	result=[name,marks]
print(result)
for student in result :
	if result>75:
	 print(result)
	 