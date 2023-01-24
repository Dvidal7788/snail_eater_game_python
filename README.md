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
</ul> 

<ul>
<li>The ghosts (represented as 'G') will randomly decide to move towards player after each turn (or if in impossible mode, will always move toward player after each turn).</li>
<li>If you run into a ghost or if a ghost runs into you, you lose! (i.e. you must repeat the level).</li>
<li>The player and ghosts can not go through blocks (represented as '#')</li>
<li>The player CAN though border edge of the board to wrap around to the other side (hint: very useful in avoiding ghost who can NOT wrap around the border)</li>
<li>For each new level, 1 more ghost, 1 more snail and 1 more block will appear, making each level slightly harder than the previous level.</li>
</ul>

<ul>
<li>Type 'quit' anytime to quit! Otherwise, keep playing indefinitely; there are no lives lost for dying, you simply repeat the level!</li>
<li>On exit, you will be prompted to record your score, recorded in csv files (1 csv file per difficulty level).</li>
</ul>

<ul>
<li>Difficulty levels: Easy, Hard, Impossible!</li>
</ul>

<h3>           GAMEBOARD:</h3>
                             ~~~ SNAIL EATER ~~~

                   - Level 1 -


                - - - - - # # - - 
                - - - - - - - - - 
                - - - - x - - - - 
                # # - - - - - - - 
                - - - - - - - - - 
                - - # # - - - - - 
                - - - - - - @ - - 
                - - - - - - - - - 
                - - - - - - G - - 

GO!: 
