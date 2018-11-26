# Genetic Algorithm Pathfinder


class Maze:
    # create the two-dimensional array

    def _createArray(self):

        # build an array

        for i in range(self.height):
            self.maze.append(['*' for i in range(self.width)])

    def getCell(self, x, y):

        # return the value of a certain cell at a specified location

        return self.maze[x][y]

    def printMaze(self):
        """Print the formatted maze to the user."""

        print(*[i for i in self.maze])





    def __init__(self, height, width):
        self.width = width
        self.height = height
        self.maze = []
        # create the array
        self._createArray()


    

maze = Maze(20, 20)
maze.printMaze()

