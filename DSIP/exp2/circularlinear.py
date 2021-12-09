x1=[2,1,-2]
x2=[1,2,-1]
print("Enter Inputs")
# x1=list(map(int,input().split(",")))
# x2=list(map(int,input().split(",")))
n=len(x1)+len(x2)-1
x1.extend([0 for i in range(n-len(x1))])
x2.extend([0 for i in range(n-len(x2))])
id1=[i for i in range(len(x1))]
id2=[i for i in range(len(x1))]
# initial
id2.reverse()
print("len of output seq",n)
print()
for ik in range(n): 
  temp=id2[-1]
  id2.pop()
  id2.insert(0,temp)
  temp=0
  print("y{}=".format(ik),end=" ")
  for i,j in zip(id1,id2):
    print("{}*{}".format(x1[i],x2[j]),end=" + ")
    temp+=x1[i]*x2[j]
  print(" = {}".format(temp))



