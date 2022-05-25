
f=open("python.txt","r")
nooflines=0
noofwords=0
noofcharacters=0
for line in f:
	line=line.strip("\n")
	words=line.split()
	nooflines+=1
	noofwords+=len(words)
	noofcharacters+=len(line)
f.close()
print("lines:",nooflines,"words:",noofwords,"characters",noofcharacters)
