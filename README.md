# snail_eater_game_python
ASCII-based, Pacman style game. Originaly written in C, rewritten in Python with additional features.

PLAYER: 'x' <br>
SNAILS: '@' <br>
GHOSTS: 'G' <br>
BLOCKS: '##' <br>

<ul>
<li>Player is 'x'. <br> </li>
<li>Use w,s,a,d to move up, down, left, right respectively. <br></li>
<li>Eat all of the snails (represented as '@') to proceed to next level. <br></li>

<li>The ghosts (represented as 'G') will randomly decide to move towards player after each turn (or if in impossible mode, will always move toward player after each turn).</li>
<li>If you run into a ghost or if a ghost runs into you, you lose! (i.e. you must repeat the level).</li>
<li>The player and ghosts can not go through blocks (represented as '#')</li>
<li>The player CAN though border edge of the board to wrap around to the other side (hint: very useful in avoiding ghost who can NOT wrap around the border)</li>
<li>For each new level, 1 more ghost, 1 more snail and 1 more block will appear, making each level slightly harder than the previous level.</li>

<li>Type 'quit' anytime to quit! Otherwise, keep playing as long as you like; there are no lives lost for dying, you just simply repeat the level!</li>
<li>When you quit, the game will prompt you to record your score in a csv file, keeping track of all the scores (divided into separate csv files for each difficulty level).</li>

<li>Difficulty levels: Easy, Hard, Impossible!</li>
</ul>
