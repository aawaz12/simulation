import numpy as np
import math


class Cell:
    def __init__(self, position, radius, growth_rate):
        self.position = np.array(position)
        self.velocity = np.array([0.0, 0.0])
        self.radius = radius
        self.growth_rate = growth_rate
        self.color='blue'


    def grow(self, dt):
        # Grow the cell based on the provided formula
        self.radius += (2 * math.pi * dt * self.growth_rate) / self.radius
