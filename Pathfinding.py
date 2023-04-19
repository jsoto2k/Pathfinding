import queue
import sys
import heapq 
import time 

sys.setrecursionlimit(10000)
#check for command line arguments


match len(sys.argv) : 
    case 1: 
        print ('Please provide the a filename, StartX, StartY, GoalX, GoalY, and Search Flag')
    case 2: 
        print ('Please provide a StartX, StartY, GoalX, GoalY, and Search Flag')
    case 3: 
        print ('Please provide a Start Y, GoalX, GoalY, and Search Flag')
    case 4: 
        print ('Please provide a GoalX, GoalY, and Search Flag')
    case 5: 
        print ('Please provide a GoalY and Search Flag')
    case 6: 
        print ('Please provide a Search Flag')
    case 7: 
        print (f'Running with the following command line arguments: {sys.argv[1:]}')   
    case other: 
        print ('Please check your command line arguments and try again')
        

#initializing global variables
mapqueue = queue.Queue(maxsize=0)
priorityMapQueue = queue.PriorityQueue(maxsize=0)
mapstack = []
pathlist = []

mapfile = (sys.argv[1])
StartX = int(sys.argv[2])
StartY = int(sys.argv[3])
GoalX = int(sys.argv[4])
GoalY = int(sys.argv[5])
SearchFlag = (sys.argv[6])

height = ""
width = ""
charactercount = 0
linecount = 0 
xposition = 0
yposition = 0
mapcharacter = ""
char = '' 
visitedcount = 0
depth_limit = 20  
    

class Node:
    def __init__(self, x_y, parent, path_cost, depth):
        self.state = x_y
        self.parent = parent
        self.path_cost = path_cost
        self.depth = depth
        

    def __str__(self):
        return "X,Y:{}   pathCost:{}   Depth:{}".format(self.state,self.path_cost,self.depth)
    
    def __lt__(self, other):
        
        if SearchFlag == "-l":
            self.path_cost < other.path_cost
            return self.path_cost < other.path_cost
            
        elif SearchFlag == "-b":
            self.depth < other.depth
            return self.depth < other.depth
        
        elif SearchFlag == "-a1" : 
            gn1 = self.path_cost
            gn2 = other.path_cost
            
            hn1 = ((width - self.state[0]) + (height - self.state[1]))
            hn2 = ((width - other.state[0]) + (height - other.state[1]))
            return gn1 + hn1 < gn2 + hn2
        
        elif SearchFlag == "-a2": 
            gn1 = self.path_cost
            gn2 = other.path_cost
            weight = 3
            
            hn1 = ((width - self.state[0]) + (height - self.state[1]))
            hn2 = ((width - other.state[0]) + (height - other.state[1]))
            return gn1 + hn1*weight < gn2 + hn2*weight
            
        elif SearchFlag == "-a3":
            self.depth < other.depth
            return self.depth < other.depth
        
class beamSearchQueue:
    def __init__(self,max_size=10):
        self.max_size = max_size
        self.Q = []
        heapq.heapify(self.Q)

    def put(self, element):
        if len(self.Q) < self.max_size:
            heapq.heappush(self.Q, element)
        else:
            heapq.heappush(self.Q, element)
            self.Q = heapq.nsmallest(self.max_size,self.Q)


    def get(self):
        return heapq.heappop(self.Q)

    def empty(self):
        return len(self.Q) == 0

beamqueue = beamSearchQueue(10)

#open mapfile and read in the map one character a time
def createmap():
    temp = ''
    with open(mapfile, 'r') as f:
        temp = f.readline()
        contents = f.read()
    # Create an empty 2D array
        two_d_array = [[]]
        current_row = 0
        current_column = 0
        for char in contents:
            if char != '\n':
                two_d_array[current_row].append((char, False))
                current_column += 1
            else:
                current_row += 1
                current_column = 0
                two_d_array.append([])
    two_d_array.pop() # remove the last empty row
    return two_d_array

pathlist = createmap()

def get_dimensions():
    with open (mapfile, 'r') as f: 
        line = f.readline()
        width, height = map(int, line.split())
    return width, height

width, height = get_dimensions()

def cost_func(x,y=None):
    
    letter = pathlist[y][x][0]

    if letter == 'R':
        return 1
    if letter == 'f':
        return 2
    if letter == 'F':
        return 4
    if letter == 'h':
        return 5
    if letter == 'r':
        return 7
    if letter == 'M':
        return 10
    if letter == 'W':
        return -1

start_time = time.time() 
def expand(parent_node:Node):
    global visitedcount
    # newNodes_xy = []
    # visitedNodes = []
    visitedcount += 1
    current_cell = parent_node.state
  
    
    # newNodes_xy.append(parent_node)

    directions = ["up", "right", "down", "left"]
    for direction in directions: 
        
        if direction == "up": 
            childcell = current_cell[0]-1, current_cell[1]
        elif direction == "right": 
            childcell = current_cell[0], current_cell[1]+1
        elif direction == "down": 
            childcell = current_cell[0]+1, current_cell[1]       
        elif direction == "left": 
            childcell = current_cell[0], current_cell[1]-1


            
        if childcell[0] < 0 or childcell[0] >= height or childcell[1] < 0 or childcell[1] >= width:
            continue
        if pathlist[childcell[0]][childcell[1]][0] == 'W':
            continue
        if pathlist[childcell[0]][childcell[1]][1] == True:
            continue
        
        childcell = Node(childcell, parent_node, parent_node.path_cost + cost_func(childcell[1],childcell[0]), parent_node.depth + 1)
        
        if (SearchFlag == '-b') :    
            pathlist[childcell.state[0]][childcell.state[1]] = (pathlist[childcell.state[0]][childcell.state[1]][0], True)
            mapqueue.put(childcell)   
            
        elif (SearchFlag == '-l'):
            pathlist[childcell.state[0]][childcell.state[1]] = (pathlist[childcell.state[0]][childcell.state[1]][0], True)
            priorityMapQueue.put(childcell)
            
        elif (SearchFlag == '-i') : 
             pathlist[childcell.state[0]][childcell.state[1]] = (pathlist[childcell.state[0]][childcell.state[1]][0], True)
             mapstack.append(childcell)   
       
        elif (SearchFlag == '-a1'):
            pathlist[childcell.state[0]][childcell.state[1]] = (pathlist[childcell.state[0]][childcell.state[1]][0], True)
            priorityMapQueue.put(childcell)
            
        elif (SearchFlag == '-a2'):
            pathlist[childcell.state[0]][childcell.state[1]] = (pathlist[childcell.state[0]][childcell.state[1]][0], True)
            priorityMapQueue.put(childcell)
            
        elif (SearchFlag == '-a3'): 
            pathlist[childcell.state[0]][childcell.state[1]] = (pathlist[childcell.state[0]][childcell.state[1]][0], True)
            beamqueue.put(childcell)
            
                      
def breadth_first_search() : 
    #begin adding to queue and visited list    
    
    current_cell = (StartY, StartX)
    startingNode = Node(current_cell,None, 0, 0)
    
    mapqueue.put(startingNode)
    
    while mapqueue.empty() == False:
        poppedNode = mapqueue.get()
        if poppedNode.state == (GoalY, GoalX):
            print (f"\nNumber of visited states = {(visitedcount)}")
            print (f"Path Cost = {poppedNode.path_cost}\n")
            print_path(poppedNode)
            break
        
        expand(poppedNode)
   
def lowest_cost() : 
    #begin adding to queue and visited list   
    
    current_cell = (StartY, StartX)
    startingNode = Node(current_cell,None, 0, 0)
    
    # add the start cell to the queue with a cost of 0
    priorityMapQueue.put(startingNode)
    
    while priorityMapQueue.empty() == False:
        poppedNode = priorityMapQueue.get()
        if poppedNode.state == (GoalY, GoalX):
            print (f"\nNumber of visited states = {(visitedcount)}")
            print (f"Path Cost = {poppedNode.path_cost}")
            print_path(poppedNode)
            break
        
        expand(poppedNode)
        
def depth_limited_search(node, depth_limit):
    if node.depth == depth_limit:
        return None
    if node.state == (GoalY, GoalX):
        return node
    expand(node)
    while mapstack:
        child_node = mapstack.pop()
        result = depth_limited_search(child_node, depth_limit + 20)
        if result is not None:
            return result
    return None

def iterative_deepening():
    global visitedcount
    visitedcount = 0
    for depth_limit in range(0, 1000):
        mapstack.clear()
        current_cell = (StartY, StartX)
        starting_node = Node(current_cell, None, 0, 0)
        result = depth_limited_search(starting_node, depth_limit)
        if result is not None:
            print (f"\nNumber of visited states = {(visitedcount)}")
            print (f"Path Cost = {result.path_cost}")
            print_path(result)

            return result
    print("Failed to find a solution.")      

def a_star_one() : 
    #begin adding to queue and visited list   
    
    current_cell = (StartY, StartX)
    startingNode = Node(current_cell,None, 0, 0)
    
    # add the start cell to the queue with a cost of 0
    priorityMapQueue.put(startingNode)
    
    while priorityMapQueue.empty() == False:
        poppedNode = priorityMapQueue.get()
        if poppedNode.state == (GoalY, GoalX):
            print (f"\nNumber of visited states = {(visitedcount)}")
            print (f"Path Cost = {poppedNode.path_cost}")
            print_path(poppedNode)
            break
        
        expand(poppedNode)

def a_star_two() :
    #begin adding to queue and visited list    
    current_cell = (StartY, StartX)
    startingNode = Node(current_cell,None, 0, 0)
    
    beamqueue.put(startingNode)
    
    while beamqueue.empty() == False:
        poppedNode = beamqueue.get()
        if poppedNode.state == (GoalY, GoalX):
            print (f"\nNumber of visited states = {(visitedcount)}")
            print (f"Path Cost = {poppedNode.path_cost}")
            print_path(poppedNode)
            break
        
        expand(poppedNode)

def checksearchflag() : 
    if (SearchFlag == "-b") : 
        breadth_first_search() 

    elif (SearchFlag == "-l") : 
        lowest_cost()
        
    elif (SearchFlag == "-i") : 
        iterative_deepening() 
   
    elif (SearchFlag == "-ia"): 
        iterative_deepening()
        
    elif (SearchFlag == "-a1") :
        a_star_one() 
    
    elif (SearchFlag == "-a2") : 
        a_star_one()  
    
    elif (SearchFlag == "-a3") : 
        a_star_one()  
         
    else : 
        print ("\nPlease enter a valid search flag") 
        
def print_path(GoalNode:Node):
    # Print the path
    print (time.time()-start_time)
    temp = GoalNode
    for j in range(width):
        for i in range(height):
            if pathlist[i][j][1] == True:
                new_tuple = pathlist[i][j][0] + "▒"
            else:
                new_tuple = pathlist[i][j][0]
            pathlist[i][j] = new_tuple
    

    while temp:
        # print(temp)
        y, x = temp.state
        pathlist[y][x] = '*'
        # print(temp.parent)
        temp = temp.parent
        
    pathlist[StartY][StartX] = 'S'
    pathlist[GoalY][GoalX] = 'G'
    
    # for j in range(width):
    #     print(pathlist[j])

    print("\nPath:")
    for row in pathlist:
        for c in row:
            if len(c) == 1:
                print(c + '  ', end='')
            elif len(c) == 2:  
                print(c + ' ', end='')
        print('\n', end='')

checksearchflag() 
        
