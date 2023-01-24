# snail_eater_game_python
ASCII-based, Pacman style game. Originaly written in C, rewritten in Python with additional features.

<h4>PLAYER: 'x'</h4>
<h4>SNAILS: '@' </h4>
<h4>GHOSTS: 'G' </h4>
<h4>BLOCKS: '##' </h4>

Player is 'x'. <br>
Use w,s,a,d to move up, down, left, right respectively.
Eat all of the snails (represented as '@') to proceed to next level.

The ghosts (represented as 'G') will randomly decide to move towards player after each turn (or if in impossible mode, will always move toward player after each turn).
If you run into a ghost or if a ghost runs into you, you lose! (i.e. you must repeat the level).
The player and ghosts can not go through blocks (represented as '#')
The player CAN though border edge of the board to wrap around to the other side (hint: very useful in avoiding ghost who can NOT wrap around the border)
For each new level, 1 more ghost, 1 more snail and 1 more block will appear, making each level slightly harder than the previous level.

Type 'quit' anytime to quit! Otherwise, keep playing as long as you like; there are no lives lost for dying, you just simply repeat the level!
When you quit, the game will prompt you to record your score in a csv file, keeping track of all the scores (divided into separate csv files for each difficulty level).

Difficulty levels: Easy, Hard, Impossible!
