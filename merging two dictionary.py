d={1:2,3:4,5:6}
d1={7:8,9:10,11:12}
d3={}
for i in (d,d1):
  d3.update(i)
print(d3)