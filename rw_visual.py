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

    # Show 1st and last point, help the user to follow better
    ax.scatter(0, 0, c='purple', edgecolors='red',
               s=60)                                      # beginning point (0,0)
    ax.scatter(rw.x_values[-1], rw.y_values[-1],          # Last point (since it start with 0, we do -1 to get the last number(example if it end at 5000, its actually 5001 so we do -1))
               c='orange', edgecolors='red', s=60)

    # ax.get_xaxis().set_visible(False)                    (Remove X axis)
    # ax.get_yaxis().set_visible(False)                    (Remove Y axis)

    plt.show()

    walk_again = input("Do you want to keep walking? (y/n): ")
    if walk_again == 'n':
        break
