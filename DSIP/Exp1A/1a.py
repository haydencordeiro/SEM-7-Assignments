import matplotlib.pyplot as plt

figure, axis = plt.subplots(2, 2)
figure.set_size_inches(18.5, 10.5)
# impulse
x1=[i for i in range(-10,20)]
y1=[0 if i!=0 else 1 for i in x1]


# step

x2=[i for i in range(-10,20)]
y2=[0 if i<0 else 1 for i in x2]



# expo
x3=[i for i in range(-10,20)]
y3=[0 if i<0 else pow(2,i) for i in x3]

# ramp
x4=[i for i in range(-10,20)]
y4=[0 if i<0 else i for i in x4]


axis[0, 0].stem(x1, y1)
axis[0, 0].set_title("Unit Function")
  

axis[0, 1].stem(x2, y2)
axis[0, 1].set_title("Step Function")

axis[1, 0].stem(x3, y3)
axis[1, 0].set_title("Expo Function")

axis[1, 1].stem(x4, y4)
axis[1, 1].set_title("Ramp Function")
  
plt.show()