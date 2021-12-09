x1=[1,2,3,4]
x2=[5,6,7,8]


x2=[0 for i in range(len(x1)-1)]+x2+[0 for i in range(len(x1)-1)]
c=-(len(x1)-1)
ol=[]
while len(x2)>=len(x1):
    temp=x2[-len(x1):]
    y=0
    for i,j in zip(temp,x1):
        y+=(i*j)
        print(f"{i}*{j}",end=" + ")
    print(f" = {y}")
    c+=1
    ol.append(y)
    x2.pop()
    


print(ol)


