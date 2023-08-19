import matplotlib.pyplot as plt
from random_walk import Random_walk

# Thats when we do the random walk
rw = Random_walk()
rw.fill_walk()

# Plotting the point for the walk
plt.style.use('classic')
fig, ax = plt.subplots()

ax.scatter(rw.x_values, rw.y_values, s=12)
plt.show()
