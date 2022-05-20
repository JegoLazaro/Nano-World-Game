# Nano-World-Game

# RANDOM LEVEL
In this level all the conditions are functional. However, the alien is programmed to move randomly on the map where detecting nano or the pit will not prevent the alien to fail the main task which is to reach the gold.
# SMART LEVEL
In this level the alien should be able to scan all the obstacles specifically nano and the pit and will be able to determine the shortest and efficient path from its initial location to the pot of gold.


# DESCRIBE THE PROBLEM
There are four (4) main variables in the program (Alien, Nano, Pit and Gold). The alien will enter the Nano world in the coordinates (0, 0), as it enters the Nano world, the Alien should be able to successfully secure the gold at coordinates (x, y) without being caught by nano or falling into the pit located at different random coordinates (x, y).
 
# WHAT IS THE ENVIRONMENT
Obstacles
Obstacles (Pit) is set randomly inside the map in which the alien should be able to scan and detect.
Entrance
Once the user runs the program the main variable (Alien) is placed at the entrance of the map at coordinates (0,0).
Map
There are four (4) variables present in the map specifically alien, nano, pit and gold. All these variables have their own functionality.
# DIFFERENT ALERTS 
Breeze
A breeze will be triggered once the alien is near the pit. The pit will be set randomly in the map thus making it harder for the alien to detect the obstacle. It’s breeze will be scanned by the alien when it lands one box before the pit.
Glitter Sound
A glitter sound will be activated once the alien detects the gold pot which will be triggered at the coordinates (x +- 1, y+-1) where (x, y) is coordinate of the gold pot.
 Scream
 A scream will be heard once the alien has successfully shot/killed the nano at its back. However, in order for this function to be viable the condition made should be able to detect nano considering its movement. This alert is most likely to be heard since the nano has 3 faces and only 1 back. Everytime the alien takes a step, the nano rotates in its place making it hard for the alien to shoot/kill the nano at the back.


# WHAT IS THE TASK/GOAL OF ALIEN
The main task of the alien is to successfully acquire the pot of gold located randomly inside the map without getting detected by nano and falling into a pit and be able to successfully exit in the same place that it entered the Nano world.
# DETERMINE PROBLEM AND TASK
There are obstacles inside the map that will try to prevent the alien from reaching the pot of gold specifically nano and the pit.
The task is to formulate effective conditions and algorithms which will help the alien detect/scan these obstacles and successfully obtain the gold and return back to where it entered.


# SPECIFY HOW GOAL CAN BE DETERMINED AND DETECTED BY ALIEN
The goal can be determined and be detected by the alien if and only if the coordinates of the alien is equal to the coordinates of the pot of gold. Moreover, the alien will only win if and only if it successfully acquired the pot of gold and returns to its initial position (0,0). 
# STATE AND EXPLAIN ALGORITHM USED AND HOW IT WORKS
For the algorithm used in the smart level, we used the a* algorithm that uses the manhattan distance in calculating the distances between the start and the end goal. A* picks the “neighbor” according to a value-‘f’ which is a parameter equal to the sum of two other parameters – ‘g’ and ‘h’. Variable ‘g’ the movement cost to move from the starting point to a given square on the grid and ‘h’ the estimated movement cost to move from that given square on the grid to the final destination.
