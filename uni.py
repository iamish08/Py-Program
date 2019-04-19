class quickfind:
    lst=list()
    def _init_(self, n):
        for i in range(0, n):
            self.lst.append(i)
            print(self.lst[i])
    def union(self,p, q):
        p =self.lst[p]
        q = self.lst[q]
        c=0
        for i in self.lst:
            if (i==p):
               self.lst[c]=q
            c+=1
        return self.lst
    def connect(self, p, q):
        return self.lst[p] == self.lst[q]

n = (int(input("enter the number of elements:")))
qf = quickfind(n)
while(True):
    ch=int(input("enter your choice.1-connect\t2-check connection\t3-exit"))
    if ch==1:
        p,q=input("enter two numbers to connect:").split()
        result=qf.union(int(p), int(q))
        print(result)
    elif ch==2:
        p, q = input("enter two numbers to check connectivity:").split()
        result = qf.connect(int(p),int(q))
        print(result)
    elif ch==3:
        break
