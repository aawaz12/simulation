import numpy as np
from concurrent.futures import ThreadPoolExecutor
import time
import math
import cell
import forces



def simulate_step(cells, dt):
    for cell in cells:
        # Calculate forces
        for other_cell in cells:
            if cell != other_cell:
                force = hertzian_potential(cell, other_cell)
                cell.apply_force(force)

        # Cell-surface interaction
        surface_force = cell_surface_interaction(cell)
        cell.apply_force(surface_force)

        # Gravity
        gravity = gravity_force(cell)
        cell.apply_force(gravity)

        # Move cell
        cell.move()

        # Grow cell
        cell.grow(dt)

def divide_cells(cells, division_time, current_time):
    if current_time % division_time == 0:
        new_cells = [Cell(cell.position, cell.radius) for cell in cells]
        cells.extend(new_cells)

def run_simulation(division_time, total_time, dt):
    cells = [Cell([0, 0])]  # Start with a single cell
    current_time = 0

    with ThreadPoolExecutor() as executor:
        while current_time < total_time:
            # Simulate step
            executor.submit(simulate_step, cells, dt)

            # Divide cells
            divide_cells(cells, division_time, current_time)

            current_time += dt
            time.sleep(dt)  # Adjust time step as needed

if __name__ == "__main__":
    run_simulation(division_time=10, total_time=100, dt=1)
