import matplotlib.pyplot as plt
from random_walk import Random_walk
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)

# Thats when we do the random walk

while True:

    rw = Random_walk()
    rw.fill_walk()

    # Plotting the point for the walk
    plt.style.use('classic')

    # To fit the data more nicely, we can add inside plot.sublots() this => figsize=(15, 10)
    fig, ax = plt.subplots(figsize=(11, 8))

    # range to generate a list of # equal to # of point in the walk
    point_number = range(rw.num_points)
    scatter = ax.scatter(rw.x_values, rw.y_values, c=point_number,
                         cmap=plt.cm.Blues, edgecolors='none', s=5)  # edgecolors to get ride of the black outline around the points

    # Show 1st and last point, help the user to follow better
    ax.scatter(0, 0, c='purple', edgecolors='red',
               s=60)                                      # beginning point (0,0)
    ax.scatter(rw.x_values[-1], rw.y_values[-1],          # Last point (since it start with 0, we do -1 to get the last number(example if it end at 5000, its actually 5001 so we do -1))
               c='orange', edgecolors='red', s=60)

    ax.set_xlabel("Horizontal Walk (x axis)", fontsize=14)
    ax.set_ylabel("Vertical Walk (y axis)", fontsize=14)

    ax.tick_params(axis='both', labelsize=14, labelcolor='tab:blue',
                   color='tab:blue', size=7, width=2, direction="out")

    ax.xaxis.set_minor_locator(MultipleLocator(5))
    ax.tick_params(which='minor', length=4, color='r',
                   width=1, direction="out")

    # ax.get_xaxis().set_visible(False)                    (Remove X axis)
    # ax.get_yaxis().set_visible(False)                    (Remove Y axis)

    color_face = fig.patch  # Adding a color around the graph
    color_face.set_facecolor('#E8E8E8')

    cbar = plt.colorbar(scatter, ax=ax, aspect=10, shrink=0.8)
    cbar.set_label('Walk Number', fontsize=12)

    plt.show()

    walk_again = input("Do you want to keep walking? (y/n): ")
    if walk_again == 'n':
        break
