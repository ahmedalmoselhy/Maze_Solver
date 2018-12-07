import serial
from time import sleep

class Queue:
    L = []
    def __init__(self):
        print(self.L)
    def enqueue(self,element):
        self.L.append(element)
    def dequeue(self):
        if(self.isEmpty() == False):
            return self.L.pop(0)
        else:
            return None
    def count(self):
        return len(self.L)
    def isEmpty(self):
        return self.count() == 0
################
class Stack:
    L = []
    def __init__(self):
        print(self.L)
    def push(self,element):
        self.L.append(element)
    def pop(self):
        if(self.isEmpty() == False):
            return self.L.pop()
        else:
            return None
    def count(self):
        return len(self.L)
    def isEmpty(self):
        return self.count() == 0
################
class MazeNode:
    # _x = 0
    # _y = 0
    # _isLeft = False
    # _isRight = False
    # _isTop = False
    # _isBottom = False
    def __init__(self, y, x, isLeft, isRight, isTop, isBottom):
        self._x = x
        self._y = y
        self._isLeft = isLeft
        self._isRight = isRight
        self._isTop = isTop
        self._isBottom = isBottom
################
class Maze:
    def __init__(self, xSquare, ySquare):
        self._xSquare = xSquare
        self._ySquare = ySquare
        self._maze = []
        self._startNode = None
        self._goalNode = None
        self.initializeMaze()

    def initializeMaze(self):
        for i in range(self._ySquare):
            row = []
            for j in range(self._xSquare):
                row.append(None)
            self._maze.append(row)

    def setStartNode(self, x, y):
        self._startNode = (x, y)

    def setGoalNode(self, x, y):
        self._goalNode = (x, y)

    def addMazeSquare(self, x, y, isLeft, isRight, isTop, isBottom):
        newMazeSquare = MazeNode(y, x, isLeft, isRight, isTop, isBottom)
        self._maze[y][x] = newMazeSquare

    def getMazeNodeByXY(self, x, y):
        return self._maze[y][x]

    def getMazeNodeByCoords(self, coords):
        return self._maze[coords[1]][coords[0]]

    def getMazeNodeChildren(self, x, y):
        children = []
        if (x > 0 and not self._maze[y][x]._isLeft):
            children.append((self._maze[y][x - 1]._x, self._maze[y][x - 1]._y))
        if (x < (self._xSquare - 1) and not self._maze[y][x]._isRight):
            children.append((self._maze[y][x + 1]._x, self._maze[y][x + 1]._y))
        if (y > 0 and not self._maze[y][x]._isTop):
            children.append((self._maze[y - 1][x]._x, self._maze[y - 1][x]._y))
        if (y < (self._ySquare - 1) and not self._maze[y][x]._isBottom):
            children.append((self._maze[y + 1][x]._x, self._maze[y + 1][x]._y))
        return children

    def depthFirstTraverse(self):
        if (self._startNode is None or self._goalNode is None):
            return None

        stack = Stack()
        stack.push([self._startNode])
        paths = []

        while (not stack.isEmpty()):
            currentPath = stack.pop()
            # print("Current Path", currentPath)
            currentXY = currentPath[-1]
            # print("Current XY", currentXY)
            if (self._goalNode == currentXY):
                paths.append(currentPath)
                break
                # print(paths)
            currentNode = self.getMazeNodeByCoords(currentXY)
            currentChildren = self.getMazeNodeChildren(currentXY[0], currentXY[1])[::-1]
            # print(currentChildren)
            for child in currentChildren:
                # print(child)
                if (child in currentPath):
                    continue
                stack.push(currentPath + [child])
        return paths

    def breadthFirstTraverse(self):
        if (self._startNode is None or self._goalNode is None):
            return None

        queue = Queue()
        queue.enqueue([self._startNode])
        paths = []

        while (not queue.isEmpty()):
            currentPath = queue.dequeue()
            # print("Current Path", currentPath)
            currentXY = currentPath[-1]
            if (self._goalNode == currentXY):
                paths.append(currentPath)
                break
            currentNode = self.getMazeNodeByCoords(currentXY)
            currentChildren = self.getMazeNodeChildren(currentXY[0], currentXY[1])[::-1]
            for child in currentChildren:
                if (child in currentPath):
                    continue
                queue.enqueue(currentPath + [child])
        return paths


# =================================================================================
# =================================================================================
# =================================================================================
# Serial Communication With Arduino Via Bluetooth

class SerialTransfer(object):
    def __init__(self, port, baudRate = 9600):
        self._port = port
        self._baudRate = baudRate
        # Establish the connection on a specific port with a specific baud rate
        self._serial = serial.Serial(self._port, self._baudRate, timeout=5)
        self._serial.flushInput()
        self._serial.flushOutput()
        print("== SERIAL CONNECTION IS ESTABLISHED SUCCESSFULLY! ==")

    def __del__(self):
        self.close()

    def close(self):
        self._serial.close()

    def send(self, statement):
        if(self._serial.isOpen()):
            print("\n== SERIAL PORT IS OPENED == SENDING ==")
            statement += '\r\n'
            encoded = statement.strip().encode()
            print("Serial is sending", encoded)
            self._serial.write(encoded)
            self._serial.flush()
            sleep(1)
        else:
            print("\n== SERIAL PORT IS NOT OPENED! ==")


    def recieve(self):
        if (self._serial.isOpen()):
            print("\nSerial Port Is Opened ! == recieve()")
            recievedData = self._serial.readline()
            stmt = recievedData.decode().strip()
            return str(stmt)
        else:
            print("Serial Port Is Not Opened ! ")
            return None






# Main App


# =================================================================================
# =================================================================================
# =================================================================================


t = True # There is a wall on this side
f = False # There is no wall on this side

# From here you add your own maze, making it so the app can find the shortest path found
contest = Maze(8, 8) # The Maze we have in the project, WILL be included in the project files!!

# Define each square of the maze as following
# contest.addMazeSquare(y, x, LeftWall, RightWall, TopWall, BottomWall)

# First Row
contest.addMazeSquare(0, 0, t, t, t, f)
contest.addMazeSquare(0, 1, t, f, f, f)
contest.addMazeSquare(0, 2, f, f, t, t)
contest.addMazeSquare(0, 3, f, t, t, f)
contest.addMazeSquare(0, 4, t, f, t, f)
contest.addMazeSquare(0, 5, f, f, t, t)
contest.addMazeSquare(0, 6, f, t, t, f)
contest.addMazeSquare(0, 7, t, t, t, f)

# Second Row
contest.addMazeSquare(1, 0, t, t, f, f)
contest.addMazeSquare(1, 1, t, t, f, f)
contest.addMazeSquare(1, 2, t, t, t, f)
contest.addMazeSquare(1, 3, t, f, f, t)
contest.addMazeSquare(1, 4, f, f, f, t)
contest.addMazeSquare(1, 5, f, t, t, f)
contest.addMazeSquare(1, 6, t, t, f, f)
contest.addMazeSquare(1, 7, t, t, f, f)

# Third Row
contest.addMazeSquare(2, 0, t, t, f, f)
contest.addMazeSquare(2, 1, t, f, f, f)
contest.addMazeSquare(2, 2, f, f, f, t)
contest.addMazeSquare(2, 3, f, f, t, f)
contest.addMazeSquare(2, 4, f, t, t, f)
contest.addMazeSquare(2, 5, t, t, f, t)
contest.addMazeSquare(2, 6, t, t, f, f)
contest.addMazeSquare(2, 7, t, t, f, f)

# Forth Row
contest.addMazeSquare(3, 0, t, t, f, f)
contest.addMazeSquare(3, 1, t, f, f, t)
contest.addMazeSquare(3, 2, f, t, t, t)
contest.addMazeSquare(3, 3, f, t, t, f)
contest.addMazeSquare(3, 4, t, t, f, f)
contest.addMazeSquare(3, 5, t, f, f, f)
contest.addMazeSquare(3, 6, f, f, f, f)
contest.addMazeSquare(3, 7, f, t, f, t)

# Fifth Row
contest.addMazeSquare(4, 0, t, f, f, f)
contest.addMazeSquare(4, 1, f, f, t, t)
contest.addMazeSquare(4, 2, f, f, t, f)
contest.addMazeSquare(4, 3, f, f, f, f)
contest.addMazeSquare(4, 4, t, t, f, f)
contest.addMazeSquare(4, 5, t, f, t, f)
contest.addMazeSquare(4, 6, f, t, f, f)
contest.addMazeSquare(4, 7, t, t, t, f)

# Sixth Row

# Seventh Row

# Eighth Row



# From here you have to modify the port so it can send data to the arduino via blutooth

paths = []
paths.extend(our_maze.depthFirstTraverse())
paths.extend(our_maze.breadthFirstTraverse())

if(len(paths) > 0 ) :
    minPath = paths[0]
    for path in paths :
        if(len(path) < len(minPath)) :
            minPath = path
    minPathStr = ""
    for coord in minPath :
        minPathStr += "(" + str(coord[0]) + "_" + str(coord[1]) + ")"
    print("Min. Length Path:" , minPathStr)

# ------------------------------------------------------------------
print("=============================================")
print("=============================================")

# You must change the port from COM5 to the bluetooth port in your device

t = SerialTransfer('COM5') # YOU MUST Change this port
try:
    t.send(minPathStr)
    t.close()
except Exception as es :
    t.close()
    print("Exception : " , ex)
