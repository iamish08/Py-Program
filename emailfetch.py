import re
fname=input()
fhand=open(fname)
for line in fhand:
	line=line.rstrip()
	x=re.findall('[a-zA-Z0-9]\S+@\S+[a-zA-Z]',line)
	if(len(x)>0):
		print(x)
