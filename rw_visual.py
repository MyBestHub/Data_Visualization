import matplotlib.pyplot as plt
from random_walk import Random_walk

# Thats when we do the random walk

while True:

    rw = Random_walk()
    rw.fill_walk()

    # Plotting the point for the walk
    plt.style.use('classic')
    fig, ax = plt.subplots()
    # range to generate a list of # equal to # of point in the walk
    point_number = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_number,
               cmap=plt.cm.Blues, edgecolors='none', s=12)  # edgecolors to get ride of the black outline around the points
    plt.show()

    walk_again = input("Do you want to keep walking? (y/n): ")
    if walk_again == 'n':
        break
