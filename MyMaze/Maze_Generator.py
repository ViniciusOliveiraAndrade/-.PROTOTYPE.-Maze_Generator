class Maze_Generator(object):
    def __init__(self, screen_width, screen_height, rows_size, cols_size):
        self.rows = int(screen_height / rows_size)
        self.cols = int(screen_width / cols_size)
        self.rows_size = rows_size
        self.cols_size = cols_size
        self.grid = []
        self.generateGrid()
    
    def generateGrid(self):
        for i in range(self.rows):
            self.grid.append([])
            for j in range(self.cols):
                cell = Cell(i, j, self.cols_size, self.rows_size )
                self.grid[i].append(cell)
    
    def generateMaze(self, i , j):
        self.current_cell = self.grid[i][j] 
        self.current_cell.visited = True
        next_cell = self.checkNeighbors(self.current_cell)
        if next_cell is not None:
            next_cell.visited = True
            current_cell = next_cell
            
            
                                            
    def checkNeighbors(self, current_cell):
        neighbors = []
        
        if current_cell.i > 0 and not self.grid[current_cell.i - 1][current_cell.j].visited: #Verify top
            neighbors.append(self.grid[current_cell.i - 1][current_cell.j])
        
        if current_cell.j < self.cols -1 and not self.grid[current_cell.i][current_cell.j + 1].visited:  #Verify right
            neighbors.append(self.grid[current_cell.i][current_cell.j + 1])
        
        if current_cell.i < self.rows - 1 and not self.grid[current_cell.i + 1][current_cell.j].visited: #Verify botton
            neighbors.append(self.grid[current_cell.i + 1][current_cell.j])
        
        if current_cell.j > 0 and not self.grid[current_cell.i][current_cell.j -1].visited:              #Verify left
            neighbors.append(self.grid[current_cell.i][current_cell.j -1])
        
        if len(neighbors) > 0:
            return neighbors[int(random(len(neighbors)))]
        return None
                
                    
    def display(self):
        for rows in self.grid:
            for cell in rows:
                cell.display()
        
    
class Cell(object):
    def __init__(self, i, j, w_size, h_size):
        self.i = i
        self.j = j
        self.w_size = w_size
        self.h_size = h_size
        self.walls = [True, True, True, True]
        self.visited = False
    
    def display(self):
        x = self.j * self.w_size
        y = self.i * self.h_size
        stroke(255)
        fill(255,255,255)
        text("i={} j={}".format(self.i, self.j), x +2, y+15)
        if self.walls[0]:
            line(x, y, x + self.w_size, y )
        if self.walls[1]:
            line(x + self.w_size, y, x + self.w_size, y + self.h_size )
        if self.walls[2]:
            line(x + self.w_size, y + self.h_size, x, y + self.h_size )
        if self.walls[3]:
            line(x, y + self.h_size, x, y)
        if self.visited:
            fill(255,0,255,100)
            rect(x, y, self.w_size, self.h_size)
