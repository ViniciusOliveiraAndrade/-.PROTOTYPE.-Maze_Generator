from Maze_Generator import Maze_Generator

def setup():
    global maze
    size(600, 600)
    maze = Maze_Generator(width, height, 30, 30) 
    maze.generateMaze(4,4)
    
    
def draw():
    background(51)
    
    # maze.generateMaze(4,4) #Genarete with delay 
    maze.display()
