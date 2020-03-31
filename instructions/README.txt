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

< -al < algorithm > > : if you chose ai on < mode > you may want to specify which algorithm will solve it (bfs, dfs, idfs, greedy, astar).


Examples:

python3 game.py human 1
python3 game.py human 2
python3 game.py ai 1 -al greedy
python3 game.py ai 2 -al idfs