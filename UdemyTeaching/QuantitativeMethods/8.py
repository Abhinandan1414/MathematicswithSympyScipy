'''
Is numpy random randint is really random?
Let us visualize
'''
#from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
print(__doc__)
# Creating dataset
z = np.random.randint(80, size =(500))
x = np.random.randint(80, size =(500))
y = np.random.randint(80, size =(500))
# Creating figure
fig = plt.figure(figsize = (10, 7))
ax = plt.axes(projection ="3d")


# Creating plot
ax.scatter3D(x, y, z, color = "green")
plt.title("simple 3D scatter plot")
# show plot
plt.show()