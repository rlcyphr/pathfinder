# Genetic Algorithm Pathfinder

import random

class AlreadyExists(BaseException): pass
class outOfBounds(BaseException): pass

# this is for randomising the position of walls inside the maze 

class Maze:
    # create the two-dimensional array


    def _createArray(self):

        # build an array

        for _ in range(self.height):
            self.maze.append(['*' for i in range(self.width)])
        self._genWalls()


    def _addWall(self, *pos):

        """takes an arbitary number of arguments for the position. """

        if list(pos) not in self.walls: self.walls.append(list(pos))
        else: raise AlreadyExists


    def _genWalls(self):

        # generate the walls - about a quarter of the maze has walls.
        ran_x = random.randint(0, 19)
        ran_y = random.randint(0, 19)

        while len(self.walls) < (self.height*self.width) // 4:

            # while less than 25% of the maze is full of stuff

            try:
                self._addWall(ran_x, ran_y)
            except AlreadyExists:
                pass

            ran_x = random.randint(0, 19)
            ran_y = random.randint(0, 19)

        
        for i in self.walls:
            self.maze[i[0]][i[1]] = "W"

        self.maze[0][0] = '*' # the top left position is always the starting point for the maze.




    def getCell(self, x, y):

        # return the value of a certain cell at a specified location

        return self.maze[x][y]

    def printMaze(self):
        """Print the formatted maze to the user."""

        for i in self.maze:
            print(*i)


    def __init__(self, height, width):
        self.width = width
        self.height = height
        self.maze = []
        self.walls = []
        # create the array
        self._createArray()


class Route:


    def __init__(self):

        self.pos = [0, 0]

    # a route is a series of up/down/left/right movements to try to get to the end of the maze
    # it starts at a particular point in the maze and tries to get to the end

    def getPos(self):

        print(self.pos)
        print(self.pos[0], self.pos[1])

    def makeMove(self):

        """Allows the object to make a move to a square that is horizontally or vertically bordering it."""

        # the move can be in one of four directions - north, south, east and west
        # this is chosen randomly

        randir = random.randint(1,4)
        print(self.pos[0])

        def north(self): 

            print("Running the north function.")

            if self[0] < 1:
                raise outOfBounds
            self[0] -= 1

        def south(self): 

            print("Running the south function.")

            if self[0] > 18:
                raise outOfBounds
            self[0] += 1

        def west(self): 

            print("Running the west function.")

            if self[1] < 1:
                raise outOfBounds
            self[1] -= 1

        def east(self): 

            print("Running the east function.")

            if self[1] > 18:
                raise outOfBounds
            self[1] += 1

        directions = {1: north, 2: south, 3: east, 4: west}

        


        try:
            directions[randir](self.pos)
            self.getPos()
        except outOfBounds:
            pass

        # 'pos' refers to the current position of the object that is trying to find a path.
        # if the north function is chosen, it checks if the target position is outside the
        # limits of the grid, or if it would run into a wall.

        # the value of 'pos' is stored as an array of format [x, y] 
        # where x is the horizontal axis and y is the vertical axis.

    







maze = Maze(20, 20)
maze.printMaze()

loc = Route() # create the route 

loc.getPos()

loc.makeMove()

loc.getPos()