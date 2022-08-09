from random import choice
import matplotlib.pyplot as plt

class RandomWalk:
    def __init__(self, num_points=10000):
        self.num_points = num_points

        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        #Decidewhich direction to go and how far to go in that direction.
        direction = choice([1,-1])
        distance = choice([0,1,2,3,4])
        return direction * distance

    def walk(self):
        '''Calculate all the steps.'''
        #Keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:
            
            x_step = self.get_step()
            y_step = self.get_step()
            
            if x_step == 0 and y_step == 0:
                continue

            #Calculate the new position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

#Keep making new walks, as long as program is running.
while True:
    rw = RandomWalk(50_000)
    rw.walk()

    plt.style.use('classic')
    fig,ax = plt.subplots(figsize=(15,9))
    point_numbers=range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.plasma, edgecolor='none', s=2)

    # Emphasize the first and last points.
    ax.scatter(0,0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Another one? (y,n): ")
    if keep_running == "n":
        break
