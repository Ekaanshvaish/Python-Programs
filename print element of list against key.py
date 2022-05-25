d={'m':[{'S1':"java","marks":98},{'S2':"java","marks":84}],'n':[{'S1':"java","marks":98},{'S2':"java","marks":84}]}
for key,values in d.items():
    for i in values:
    	print(key,":",i)