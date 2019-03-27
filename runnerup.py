list1=map(int,raw_input().split())
max1=0
for i in list1:
	if max1<int(i) or max1==0:
		max1=int(i)
max2=0
for i in list1 :
	if max2<int(i) and i!=max1 :
		max2=(i)
print(max2)
