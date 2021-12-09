x1=[0,1,-2,3,-4]
x2=[0.5,1,2,1,0.5]
sx=0
sy=2


x2=[0 for i in range(len(x1)-1)]+x2+[0 for i in range(len(x1)-1)]
c=-(len(x1)-1)
ol=[]
while len(x2)>=len(x1):
    temp=x2[-len(x1):]
    y=0
    for i,j in zip(temp,x1):
        y+=(i*j)
    c+=1
    ol.append(y)
    x2.pop()
    


print(ol)
print("zeroth positon is at index "+str(sx+sy))


