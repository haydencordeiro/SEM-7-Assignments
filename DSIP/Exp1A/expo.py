import matplotlib.pyplot as plt
x=[i for i in range(-10,20)]
y=[0 if i<0 else pow(2,i) for i in x]
plt.stem(x, y)
plt.show()