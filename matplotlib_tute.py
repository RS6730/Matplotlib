import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
y = x ** 2


# Functional Method 
plt.plot(x, y, 'r-')
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Work')


# Subplots 
plt.subplot(1, 2, 1)
plt.plot(x, y, 'r')

plt.subplot(1, 2, 2)
plt.plot(x, y, 'r')

# Object Oriented Method
fig = plt.figure()
# axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
# axes.plot(x, y)
# axes.set_xlabel('X Label')
# axes.set_ylabel('Y Label')
# axes.set_title('Title')

axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])

axes1.plot(x, y)
axes2.plot(y, x)


## Part 2
fig,axes = plt.subplots(nrows = 1, ncols = 2)

# DPI
fig = plt.figure(figsize = (3, 2), dpi = 100)
ax = fig.add_axes([0, 0, 1, 1])
ax.plot(x, y)






plt.show() 