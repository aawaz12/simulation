import numpy as np
from concurrent.futures import ThreadPoolExecutor
import numpy as np


def hertzian_potential(cell1, cell2):
    # Implement the Hertzian potential calculation
    pass

def cell_surface_interaction(cell):
    # Implement cell-surface interaction force
    pass

def gravity_force(cell):
    # Implement gravity force
    pass




def movement(bug, neighbours, cut_off, k, gravity, friction_coefficient, surface_level):
    f = np.array([0.0, 0.0])  # Initialize force vector
    bug.enemy_count = 0

    for b in neighbours:
        disp = b.position - bug.position  # Displacement vector
        dist = np.linalg.norm(disp)  # Distance between bug and b

        if ((dist < bug.radius + b.radius) and dist != 0):
            # Calculate repulsive force
            force_direction = disp / dist
            overlap = (bug.radius + b.radius) - dist
            repulsion_force = force_direction * k * overlap*-1
            f += repulsion_force

 

    # Add gravity force
    f += gravity

    # Add friction force if the cell is on the surface
    # Assuming y-axis is vertical, and surface_level is the y-value of the surface
    if (not (bug.position[1]- bug.radius) >= surface_level) :
        #print ("A")
        # Friction opposes the direction of motion (or potential motion)
        friction_force = -np.sign(bug.velocity) * friction_coefficient
        f += friction_force
        bug.color='red'
        

    return f


def update_position(cell, neighbors, cut_off, k, gravity, friction_coefficient, surface_level, eta, dt):
    # Calculate the total force on the cell
    #print ("cell position")
    #print(cell.position)
    total_force = movement(cell, neighbors, cut_off, k, gravity, friction_coefficient, surface_level)
    #print ("total Forces")
    #print (total_force)

    # Calculate displacement
    displacement = total_force * eta * dt
    velocity=total_force*eta
        #print ("Displacement")
    #print (displacement)
   

    # Update the cell's position
    cell.position =cell.position+ displacement
    cell.velocity=cell.velocity+velocity
    ##dont let it go belw the surfce
    if (cell.position[1]<surface_level):   ##Dont let the position fo bellow the surface
        cell.position[1]=0
    #print (cell.position)


  



