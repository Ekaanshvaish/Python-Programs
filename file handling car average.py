f=open("python.txt",'r')
lines=f.readlines()
for line in lines:
    x=lines.split()
    avg=(int)(x[2])
    if avg>=15:
     print(line)
f.close()