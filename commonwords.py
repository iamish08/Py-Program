#to count the 10 most common word in a given text file
#create a text file before execution
import string
fname=input('Enter filename:')
fhand=open(fname)
counts=dict()
for line in fhand:
	line=line.translate(str.maketrans(","," ",string.punctuation))
	line=line.lower()
	words=line.split()
for word in words:
	if word in words:
		counts[word]=1
	else:
		counts[word]+=1
lst=list()
for key,val in list(counts.items()):
	lst.append((val,key))
lst.sort(reverse=True)
for key,val in lst[:10]:
	print(key,val)

#random changes
