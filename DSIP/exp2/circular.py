x1=[0,0,3,-1,0]
x2=[1,1,1,0,0]
print("Enter Inputs")
# x1=list(map(int,input().split(",")))
# x2=list(map(int,input().split(",")))
x1.extend([0 for i in range(len(x2)-len(x1))])
x2.extend([0 for i in range(len(x1)-len(x2))])
id1=[i for i in range(len(x1))]
id2=[i for i in range(len(x1))]
# initial
id2.reverse()

print("len of output seq",len(x1))
print() 
for ik in range(len(id1)):
  temp=id2[-1]
  id2.pop()
  id2.insert(0,temp)
  temp=0
  print("y{}=".format(ik),end=" ")
  for i,j in zip(id1,id2):
    print("{}*{}".format(x1[i],x2[j]),end=" + ")
    temp+=x1[i]*x2[j]
  print(" = {}".format(temp))
