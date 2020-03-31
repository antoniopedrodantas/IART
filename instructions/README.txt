Our project consists in replicating the famous Box Word 2 game, as well as developing an AI that can easily beat it.
The game consists in a series of puzzles, where the player (Red Square) has to reach the exit (Dark Blue Square) of
the stage in order to advance to the next level.
Various obstacles are placed around, making the goal harder than it seems at first sight. 
At some stages, there are holes, which can be filled with the boxes placed around. 
There are several types of boxes - the yellow are normal ones, which can be pushed around.
The light blue boxes, called Ice Boxes, when pushed will slide away if there is no wall, hole or another box to stop them.
If the player gets stuck, he can retry the level.
The player can move up, down left and right using the arrow keys.

What do you need?

To successfully run our game you will need Python v.3 or above, as well as the pygame library.
You can easily install these two components here:
https://www.python.org/
https://realpython.com/pygame-a-primer/#background-and-setup


How to run it?

On your shell or command prompt access the folder where these files are. Then, input the following command:

python3 game.py < mode > < level > <-al < algorithm > >

< mode > : here you choose between playing yourself or letting the AI complete the level (can be human or ai).

< level > : is the game level you want to play.

< -al < algorithm > > : if you chose ai on < mode > you need to specify which algorithm will solve it (bfs, dfs, idfs, greedy, astar).

< -v < bool > > : this flag is optional. If you enable it you must follow it by a boolean (true, false, 0, 1, True, False). If true, this will show the nodes the algorithm is processing in real time while searching for the solution. Note: this comes at expense of performance thus, it is only recommended in the first levels


Examples:

game.py human 1

game.py human 2

game.py ai 1 -al greedy -v false

game.py ai 2 -al idfs

game.py ai 3 -al astar -v true

game.py ai 4 -al dfs -v 1


NOTE: 
    - When playing in human mode, press the "R" key to reset the level
    - When playing in human mode, press the "H" for the solution to be printed in the terminal from the starting point after a level reset
      this is only recommneded in the first 3 levels 