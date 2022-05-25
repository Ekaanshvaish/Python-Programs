x=int(input("enter a no"))
q=int(x)
count=0
while(q!=0):
          q=q//10
          count=count+1
result=0
cnt=count
q=x
mul=1
while(q!=0):
        rem=q%10
        while(cnt!=0):
                mul=mul*rem
                cnt=cnt-1
        result=result+mul
        cnt=count
        q=q//10
        mul=1
if(result==x):
   print("arm")
else:
   print("not arm")
