import matplotlib.pyplot as plt
plt.style.available

# Pages 444

input_values = range(1, 1001)
squares = [x**2 for x in input_values]

plt.style.use('bmh')
fig, ax = plt.subplots()
# ax.plot(input_values, squares, linewidth=2)
# This is to customize a specific point in the graph(x=2, y=4:    ax.scatter(2, 4, s=80)
# This is to add a pointer to every value provided for x and y:   ax.scatter(input_values, squares, s=80)
# c=squares,cmap=plt.cm.cividis (appoint a colormap to Y axis), colormap  website: https://matplotlib.org/stable/gallery/color/colormap_reference.html
ax.scatter(input_values, squares, c=squares, cmap=plt.cm.cividis, s=10)


ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14, color='blue')
ax.tick_params(axis='both', labelsize=12)

ax.axis([0, 1100, 0, 1100000])  # Specify the range.(#1, #2) = X, (#3, #4) = Y

plt.show()
