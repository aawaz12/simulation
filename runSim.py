import numpy as np
import matplotlib.pyplot as plt
from biofilmClass import Biofilm
from gridClass import Grid
from cellClass import  Cell
from forces import update_position
import config



# Assuming your Biofilm, Cell, and Grid classes are already defined
# Define your global variables and initialize objects
dt = 0.071
cell_radius = 5
max_num_cells = int((700/(2*cell_radius))*(700/(2*cell_radius))*100)
max_num_cells=1000

eta = 0.03 #Viscosity of medium
k = 1.9  #Spring constant ##1.9
growth_rate = 2
grid_width=cell_radius
grid_height=cell_radius
global_size = 700
cell_size=cell_radius
grid = Grid(grid_width,grid_height, cell_size,global_size)
#num_cells=1
bugs= Biofilm()
growing = True
gravity=np.array([0,-10])
friction_coeff=20
surface_level=0



# Assuming the Cell, Biofilm, Grid, and other related classes and functions are already defined

def draw_biofilm(biofilm, ax):
    ax.clear()  # Clear existing drawings
    ax.set_xlim(-100, 100)  # Adjust these limits to fit your simulation space
    ax.set_ylim(-100, 100)
    for cell in biofilm.cells:
        circle = plt.Circle(cell.position, cell.radius, fc=cell.color, ec='black')
        ax.add_patch(circle)
        



def init():
    
    
    bugs.cells.clear()
    init_position=[1,1]
    
    cell = Cell(init_position,cell_radius,growth_rate) 
    cell = Cell(init_position,cell_radius,growth_rate) 
    # Add initial bacteria...
    bugs.add_cell(cell)
    config.num_cells=config.num_cells+1

def simulate():
    
    print (bugs.cells)
    fig, ax = plt.subplots()
    numSteps=200
    for _ in range(numSteps):  # Define your simulation steps
        # Reset grid with current bacteria
        
        grid.reset(bugs.cells)



        # Biofilm update logic (growth, movement, division, death)
        ##go through each bacteria and  move and divide
        to_divide=[]
        for cell in bugs.cells:
            print (cell.radius)
            
            if(config.num_cells<max_num_cells and growing==1):
                cell.grow(dt)
                print ("GROWING"+str(config.num_cells))
                if (cell.radius > (cell_radius * 1.1)):
                    if (np.random.rand() > 0.8):  # Random check (80% chance not to divide)
                        to_divide.append(cell)
                  
            neighbors = grid.get_neighbors(cell)  # or however you determine neighbors
            #print (neighbors)
            #asd
            update_position(cell, neighbors, 1.2 * cell_radius, k, gravity, friction_coeff, surface_level, eta, dt)
        #if (numSteps%1==0):
        draw_biofilm(bugs, ax)
    
        bugs.update(to_divide,grid,cell_radius,max_num_cells,growth_rate,config.num_cells)
        print("NUMCELL")
        print (config.num_cells)
        #asd
        
        plt.pause(0.1)  # Pause for a brief period to create a visual effect of animation

        
    asd
        # Rendering or data logging
        # Implement your rendering or data logging here

        # Simulation control logic
        # Implement control logic, like stopping condition or user input handling

    

# Start the simulation
init()
simulate()

