st=input()
ans=" "
for i in range(len(st)):
    ch=st[i]
    if(ch>='a' and ch<='z'):
    	ans+=chr(ord('A')+ord(ch)-ord('a'))
    else:
    	ans+=chr(ord('a')+ord(ch)-ord('A'))
print(ans)
   