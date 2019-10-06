#to count the number of digits and letters in agiven sentence taken as an input from the user
sen=input()
dic={'Letter':0,'digit':0}
for c in sen:
	if c.isalpha():
		dic['Letter']+=1
	elif c.isdigit():
		dic['digit']+=1
print(dic)	
