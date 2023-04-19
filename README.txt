Please make sure that the version you are running is Python 3.10 or higher because this program makes use of match statements which is not present in earlier versions of python 

Terminal / Command Line Arguments: 

Small Map: 

Breadth First: 
Python3 Pathfinding.py "Map.txt" "0" "0" "14" "19" "-b"

Dijkstra's Algorithm:
Python3 Pathfinding.py "Map.txt" "0" "0" "14" "19" "-l"

Iterative Deepening: 
Python3 Pathfinding.py "Map.txt" "0" "0" "14" "19" "-i" 
(This algorithm avoids repeated states. The one that didn't avoid repeating states did not work)

Unweighted Manhatten Distance: 
Python3 Pathfinding.py "Map.txt" "0" "0" "14" "19" "-a1" 

Weighted Manhatten Distance (Default weight = 3): 
Python3 Pathfinding.py "Map.txt" "0" "0" "14" "19" "-a2" 

Beam Search: 
Python3 Pathfinding.py "Map.txt" "0" "0" "14" "19" "-a3" 



Larger Map: 
 
Breadth First: 
Python3 Pathfinding.py "Map.txt" "0" "0" "119" "159" "-b"

Dijkstra's Algorithm:
Python3 Pathfinding.py "Map.txt" "0" "0" "119" "159" "-l"

Iterative Deepening: 
Python3 Pathfinding.py "Map.txt" "0" "0" "119" "159" "-i" 
(This algorithm avoids repeated states. The one that didn't avoid repeating states did not work)

Unweighted Manhatten Distance: 
Python3 Pathfinding.py "Map.txt" "0" "0" "119" "159" "-a1" 

Weighted Manhatten Distance (Default weight = 3): 
Python3 Pathfinding.py "Map.txt" "0" "0" "119" "159" "-a2" 

Beam Search (Default weight = 3): 
Python3 Pathfinding.py "Map.txt" "0" "0" "119" "159" "-a3" 



Big Map: (iterative deepening and beam search do not work on this map)

Breadth First: 
Python3 Pathfinding.py "MapBig.txt" "0" "0" "4095" "4092" "-b"

Dijkstra's Algorithm:
Python3 Pathfinding.py "MapBig.txt" "0" "0" "4095" "4092" "-l"

Unweighted Manhatten Distance: 
Python3 Pathfinding.py "MapBig.txt" "0" "0" "4095" "4092" "-a1" 

Weighted Manhatten Distance (Default weight = 3): 
Python3 Pathfinding.py "MapBig.txt" "0" "0" "4095" "4092" "-a2" 

