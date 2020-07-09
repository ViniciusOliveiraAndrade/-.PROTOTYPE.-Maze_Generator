from Maze_Generator import Maze_Generator

def setup():
    global maze
    size(400, 400)
    maze = Maze_Generator(width, height, 40, 40) 
    # maze.generateMaze(4,4)
    
    
def draw():
    background(51)
    
    maze.generateMaze(4,4) #Genarete with delay 
    maze.display()
