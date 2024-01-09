import numpy as np
from  cellClass import  Cell
import config

class Biofilm:
    
    def __init__(self):
        self.cells = []

    def add_cell(self, cell):
        self.cells.append(cell)

    def remove_cell(self, cell):
        self.cells.remove(cell)

    def update(self, to_divide, grid,cell_radius,max_num_cells,growth_rate,num_cells):
        # Divide cells
        for cell in to_divide:
            cell.radius = cell_radius  # Reset radius to a standard size for a new cell
            if (len(self.cells) < max_num_cells):  # Check max cell limit
                # Create a new cell near the parent cell
                offset= np.random.normal(size=2) *cell_radius
               
                new_position = cell.position +offset
                #print ("AA")
                #print (new_position)
                #print (cell.position)
               # asd
                
                daughter = Cell(new_position, cell_radius,growth_rate)
                self.add_cell(daughter)# Add new cell to biofilm
                #grid.add_cell(daughter)  
                config.num_cells=config.num_cells+1
                print ("Biofil class "+str(config.num_cells))
                

        # Remove cells
        '''
        for cell in to_kill:
            self.remove_cell(cell)
            grid.remove_cell(cell)  # Remove cell from grid
        '''

