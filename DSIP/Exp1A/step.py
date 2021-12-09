import matplotlib.pyplot as plt
x=[i for i in range(-10,20)]
y=[0 if i<0 else 1 for i in x]
plt.stem(x, y)
plt.show()