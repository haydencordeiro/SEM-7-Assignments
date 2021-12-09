h=list(map(int,input().split()))
x=list(map(int,input().split()))
n=len(h)+len(x)-1
def getVal(a,idx):
    return a[idx] if 0<=idx<len(a) else 0
ol=[]
for i in range(n):
    temp=0
    for k in range(len(h)):
        temp+=getVal(x,k)*getVal(h,i-k)
    ol.append(temp)
print(ol)
