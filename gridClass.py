
class Site:
    def __init__(self):
        self.contains = []

    def add_cell(self, cell):
        self.contains.append(cell)

    def remove_cell(self, cell):
        self.contains.remove(cell)

    def clear_cells(self):
        self.contains = []

class Grid:

    def __init__(self, grid_width,grid_height, cell_size,global_size):
        self.grid_width = grid_width

        self.grid_height = grid_height
        self.cell_size = cell_size
        self.sites = [[Site() for _ in range(int (global_size/grid_width))] for _ in range(int(global_size/grid_height))]

    def add_cell(self, cell):
        x, y = int(cell.position[0] / self.cell_size), int(cell.position[1] / self.cell_size)
        self.sites[x][y].add_cell(cell)

    def remove_cell(self, cell):
        x, y = int(cell.position[0] / self.cell_size), int(cell.position[1] / self.cell_size)
        self.sites[x][y].remove_cell(cell)

    def get_neighbors(self, cell):
        x, y = int(cell.position[0] / self.cell_size), int(cell.position[1] / self.cell_size)
        neighbors = []
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.grid_width and 0 <= ny < self.grid_height:
                    neighbors.extend(self.sites[nx][ny].contains)
        return neighbors

    def reset(self, bacteria):
        # Clear all sites
        for row in self.sites:
            for site in row:
                site.clear_cells()

        # Add bacteria back to the grid, without periodic boundary conditions
        for b in bacteria:
            
            i = int(b.position[0] / self.grid_width)
            j = int(b.position[1] / self.grid_height)

            # Check if the indices are within the grid bounds
            if 0 <= i < len(self.sites) and 0 <= j < len(self.sites[0]):
                self.sites[i][j].add_cell(b)


