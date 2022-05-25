st=input("enter a string")
char=input("entr the char to find freq\n")
count=0
i=0
while(i<len(st)):
          if(st[i]==char):
             count=count+1
          i=i+1
print("freq",char,"is",count)          
         
          