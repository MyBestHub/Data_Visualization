import numpy as np
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
import matplotlib.pyplot as plt
plt.style.available

# Pages 444

input_values = range(1, 401)
squares = [x**2 for x in input_values]

plt.style.use('bmh')
fig, ax = plt.subplots()
# ax.plot(input_values, squares, linewidth=2)
# This is to customize a specific point in the graph(x=2, y=4:    ax.scatter(2, 4, s=80)
# This is to add a pointer to every value provided for x and y:   ax.scatter(input_values, squares, s=80)
# c=squares,cmap=plt.cm.cividis (appoint a colormap to Y axis), colormap  website: https://matplotlib.org/stable/gallery/color/colormap_reference.html
scatter = ax.scatter(input_values, squares, c=squares,
                     cmap=plt.cm.cividis, s=10)


ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14, color='black')
ax.tick_params(axis='both', labelsize=12, labelcolor='tab:blue',  # labelcolor for the color name given to each axis, color is just for the tick color
               color='tab:green', size=4, width=2, which="major", direction="out")

# We can add small ticks in between the big ones
ax.tick_params(which='minor', length=4, color='r', direction="out")

# Adding any value = fig.patch  (so I can add a facecolor)
color_test = fig.patch
color_test.set_facecolor('#FFD39B')

ax.axis([0, 1100, 0, 1100000])  # Specify the range.(#1, #2) = X, (#3, #4) = Y

ax.xaxis.set_minor_locator(MultipleLocator(50))


# Adding a color bar and adjust the "shrink" parameter (for the bar size)
cbar = plt.colorbar(scatter, ax=ax, aspect=10, shrink=0.7)
cbar.set_label('Square Value', fontsize=12)

# ax.legend([scatter], ['Square Data'], loc='upper left', fontsize=12)      To Add a Legend

#  plt.tight_layout()                   Ensures all elements fit within the figure area
plt.show()
