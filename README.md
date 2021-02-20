# Box World 2

Our project consists in replicating the famous Box Word 2 game, as well as developing an AI that can easily beat it. The game consists in a series of puzzles, where the player has to reach the exit of the stage in order to advance to the next level. Various obstacles are placed around, making the goal harder than it seems at first sight. At some stages, there are holes, which can be filled with the boxes placed around. There are several types of boxes - the orange and green are normal ones, which can be pushed around. The grey boxes, called Ice Boxes, when pushed will slide away if there is no wall, hole or another box to stop them. If the player gets stuck, he can retry the level.

![box world printscreen](https://i.imgur.com/5lfnGf7.png)

## What do you need?

To successfully run our game you will need Python v.3 or above, as well as the pygame library.
You can easily install these two components here:
* [Python](https://www.python.org/)
* [pygame](https://realpython.com/pygame-a-primer/#background-and-setup)

## How to run it?

On your shell or command prompt access the folder where these files are. Then input the following command

__python3 game.py < mode > < level > <-al < algorithm > > <-v < bool > >__
* __< mode >__ here you choose between playing yourself or letting the AI complete the level (can be human or ai).

* __< level >__ is the game level you want to play.

* __< -al < algorithm > >__ if you chose ai on < mode > you need to specify which algorithm will solve it (bfs, dfs, idfs, greedy, astar).

*  __< -v < bool > >__  this flag is optional. If you enable it you must follow it by a boolean (true, false, 0, 1, True, False). If true, this will show the nodes the algorithm is processing in real time while searching for the solution. Note: this comes at expense of performance thus, it is only recommended in the first levels

Examples:

* game.py human 1

* game.py human 2

* game.py ai 1 -al greedy -v false

* game.py ai 2 -al idfs

* game.py ai 3 -al astar -v true

* game.py ai 4 -al dfs -v 1
