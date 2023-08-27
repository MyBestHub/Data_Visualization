from random import choice


class Random_walk():

    def __init__(self, num_points=1600):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):

        while len(self.x_values) < self.num_points:

            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3])
            y_step = y_direction * y_distance

            if x_step == 0 and y_step == 0:  # Skip the steps that go nowhere
                continue

            # Calculate new position, we add value in x_step to the last value stored in x_values by adding [-1], same with Y
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
