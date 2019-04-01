import re
fname=input()
fhand=open(fname)
for line in fhand:
	line=line.rstrip()
	x=re.findall('^from.*([0-9][0-9]):',line)
	print(x)
