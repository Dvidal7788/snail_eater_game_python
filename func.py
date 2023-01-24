from numpy import random
from time import sleep
from datetime import datetime
import csv

# Globals
HEIGHT = 9
WIDTH = 9

board = []
ghost_coordinates = []

PLAYER = 'x'
GHOST = 'G'
SNAIL = '@'
BLOCK = '#'
EMPTY = '-'
GHOST_START_NUM = 1
SNAIL_START_NUM = GHOST_START_NUM
snails_left = SNAIL_START_NUM
# Why can't I have snails_left as global and update global in function?

# Define Coordinates class and create p1 global
class Coordinates():
    def __init__(self, x, y):
        self.x = x
        self.y = y

p1 = Coordinates(0,0)

# Function definitions
def resetBoard():
    board.clear()
    for i in range(HEIGHT):
        board.append([])
        for j in range(WIDTH):
            board[i].append(EMPTY)


def printBoard(level):
    print("\n" + (" " * 15) + "~~~ SNAIL EATER ~~~")
    print("\n" + (" " * 19) + f"- Level {level} -\n\n")

    for row in board:
        print("\t\t", end='')
        for space in row:
            print(f"{space} ", end='')
        print()
    print()

def spawnPlayer():
    x = random.randint(WIDTH)
    y = random.randint(HEIGHT)
    board[x][y] = PLAYER
    p1.x = x
    p1.y = y

def spawnBlocks(level):

    for i in range(level):

        while True:
            # Using WIDTH-1 and HEIGHT-1 not for indexing, but because I want sets 2 blocks
            x = random.randint(WIDTH-1)
            y = random.randint(HEIGHT-1)

            # Every other set of blocks is turned other way (horizontal vs vertical)
            if i % 2 == 0:
                if board[x][y] == EMPTY and board[x][y+1] == EMPTY:
                    board[x][y] = BLOCK
                    board[x][y+1] = BLOCK
                    break
            else:
                if board[x][y] == EMPTY and board[x+1][y] == EMPTY:
                    board[x][y] = BLOCK
                    board[x][y+1] = BLOCK
                    break


def spawnGhosts(ghost_num):
    for i in range(ghost_num):
        while True:
            x = random.randint(HEIGHT)
            y = random.randint(WIDTH)
            if board[x][y] == EMPTY:
                board[x][y] = GHOST
                ghost_coordinates[i].x = x
                ghost_coordinates[i].y = y
                break

def spawnSnails(snail_num):
    for i in range(snail_num):
        while True:
            x = random.randint(HEIGHT)
            y = random.randint(WIDTH)
            if board[x][y] == EMPTY:
                board[x][y] = SNAIL
                break


# playerMove with blocks
def playerMove():

    global snails_left
    validMove = False

    # Loop until valid move is given
    while not validMove:
        validMove = True

        # User input
        move = input("GO!: ")


        # Player Move
        if move.lower() == 'w':
            # --- UP ---

            # Check if at border
            if p1.x == 0:
                # Check if space player can move to
                if (board[HEIGHT-1][p1.y] == SNAIL) or (board[HEIGHT-1][p1.y] == EMPTY):

                    # Decrement snails_left if snail eaten
                    if board[HEIGHT-1][p1.y] == SNAIL:
                        snails_left -= 1

                    board[p1.x][p1.y] = EMPTY
                    board[HEIGHT-1][p1.y] = PLAYER
                    p1.x = HEIGHT-1

                elif board[HEIGHT-1][p1.y] == BLOCK:
                    return 'b'
                elif board[HEIGHT-1][p1.y] == GHOST:
                    board[p1.x][p1.y] = EMPTY
                    return 'g'

            else:
                # Check if space player can move to
                if (board[p1.x-1][p1.y] == SNAIL) or (board[p1.x-1][p1.y] == EMPTY):

                    # Decrement snails_left if snail eaten
                    if board[p1.x-1][p1.y] == SNAIL:
                        snails_left -= 1

                    board[p1.x][p1.y] = EMPTY
                    board[p1.x-1][p1.y] = PLAYER
                    p1.x -= 1

                if board[p1.x-1][p1.y] == BLOCK:
                    return 'b'
                elif board[p1.x-1][p1.y] == GHOST:
                    board[p1.x][p1.y] = EMPTY
                    return 'g'

        elif move.lower() == 's':
            # --- DOWN ---

            # Check if at border
            if p1.x == HEIGHT-1:

                # Check if space player can move to
                if (board[0][p1.y] == SNAIL) or (board[0][p1.y] == EMPTY):

                    # Decrement snails_left if snail eaten
                    if board[0][p1.y] == SNAIL:
                        snails_left -= 1

                    board[p1.x][p1.y] = EMPTY
                    board[0][p1.y] = PLAYER
                    p1.x = 0

                elif board[0][p1.y] == BLOCK:
                    return 'b'
                elif board[0][p1.y] == GHOST:
                    board[p1.x][p1.y] = EMPTY
                    return 'g'

            else:

                # Check if space player can move to
                if (board[p1.x+1][p1.y] == SNAIL) or (board[p1.x+1][p1.y] == EMPTY):

                    # Decrement snails_left if snail eaten
                    if board[p1.x+1][p1.y] == SNAIL:
                        snails_left -= 1

                    board[p1.x][p1.y] = EMPTY
                    board[p1.x+1][p1.y] = PLAYER
                    p1.x += 1

                elif board[p1.x+1][p1.y] == BLOCK:
                    return 'b'
                elif board[p1.x+1][p1.y] == GHOST:
                    board[p1.x][p1.y] = EMPTY
                    return 'g'


        elif move.lower() == 'a':
            # --- LEFT ---

            # Check if at border
            if p1.y == 0:

                # Check if space player can move to
                if (board[p1.x][WIDTH-1] == SNAIL) or (board[p1.x][WIDTH-1] == EMPTY):

                    # Decrement snails_left if snail eaten
                    if board[p1.x][WIDTH-1] == SNAIL:
                        snails_left -= 1

                    board[p1.x][p1.y] = EMPTY
                    board[p1.x][WIDTH-1] = PLAYER
                    p1.y = WIDTH-1

                elif board[p1.x][WIDTH-1] == BLOCK:
                    return 'b'
                elif board[p1.x][WIDTH-1] == GHOST:
                    board[p1.x][p1.y] = EMPTY
                    return 'g'

            else:
                # Check if space player can move to
                if (board[p1.x][p1.y-1] == SNAIL) or (board[p1.x][p1.y-1] == EMPTY):

                    # Decrement snails_left if snail eaten
                    if board[p1.x][p1.y-1] == SNAIL:
                        snails_left -= 1

                    board[p1.x][p1.y] = EMPTY
                    board[p1.x][p1.y-1] = PLAYER
                    p1.y -= 1

                elif board[p1.x][p1.y-1] == BLOCK:
                    return 'b'
                elif board[p1.x][p1.y-1] == GHOST:
                    board[p1.x][p1.y] = EMPTY
                    return 'g'



        elif move.lower() == 'd':
            # --- RIGHT ---

            # Check if at border
            if p1.y == WIDTH-1:

                # Check if space player can move to
                if (board[p1.x][0] == SNAIL) or (board[p1.x][0] == EMPTY):

                    # Decrement snails_left if snail eaten
                    if board[p1.x][0] == SNAIL:
                        snails_left -= 1

                    board[p1.x][p1.y] = EMPTY
                    board[p1.x][0] = PLAYER
                    p1.y = 0

                elif board[p1.x][0] == BLOCK:
                    return 'b'
                elif board[p1.x][0] == GHOST:
                    board[p1.x][p1.y] = EMPTY
                    return 'g'
            else:

                # Check if space player can move to
                if (board[p1.x][p1.y+1] == SNAIL) or (board[p1.x][p1.y+1] == EMPTY):

                    # Decrement snails_left if snail eaten
                    if board[p1.x][p1.y+1] == SNAIL:
                        snails_left -= 1

                    board[p1.x][p1.y] = EMPTY
                    board[p1.x][p1.y+1] = PLAYER
                    p1.y += 1

                elif board[p1.x][p1.y+1] == BLOCK:
                    return 'b'
                elif board[p1.x][p1.y+1] == GHOST:
                    board[p1.x][p1.y] = EMPTY
                    return 'g'

        elif move.lower() == 'quit':
            return 'q'
        else:
            print("Please type 'a', 'w', 's', 'd' only.")
            validMove = False

    return 'p'

def ghostMoveEasy():

    player_eaten = False
    for ghost in ghost_coordinates:

        # Randomly decide whether ghost will move horizontally or vertically towards player, or not move at all
        random_return = random.randint(3)

        if random_return == 0:

            # Up/Down
            if ghost.x < p1.x and (not ghost.x == 0):

                if (board[ghost.x+1][ghost.y] == EMPTY) or (board[ghost.x+1][ghost.y] == PLAYER):
                    if board[ghost.x+1][ghost.y] == PLAYER:
                        player_eaten = True

                    board[ghost.x][ghost.y] = EMPTY
                    ghost.x += 1
                    board[ghost.x][ghost.y] = GHOST

            elif ghost.x > p1.x and (not ghost.x == HEIGHT-1):

                if (board[ghost.x-1][ghost.y] == EMPTY) or (board[ghost.x-1][ghost.y] == PLAYER):
                    if board[ghost.x-1][ghost.y] == PLAYER:
                        player_eaten = True

                    board[ghost.x][ghost.y] = EMPTY
                    ghost.x -= 1
                    board[ghost.x][ghost.y] = GHOST

        elif random_return == 1:

            # Left/Right
            if ghost.y < p1.y and (not ghost.y == 0):

                if (board[ghost.x][ghost.y+1] == EMPTY) or (board[ghost.x][ghost.y+1] == PLAYER):
                    if board[ghost.x][ghost.y+1] == PLAYER:
                        player_eaten = True

                    board[ghost.x][ghost.y] = EMPTY
                    ghost.y += 1
                    board[ghost.x][ghost.y] = GHOST
            elif ghost.y > p1.y and (not ghost.y == WIDTH-1):

                if (board[ghost.x][ghost.y-1] == EMPTY) or (board[ghost.x][ghost.y-1] == PLAYER):
                    if board[ghost.x][ghost.y-1] == PLAYER:
                        player_eaten = True

                    board[ghost.x][ghost.y] = EMPTY
                    ghost.y -= 1
                    board[ghost.x][ghost.y] = GHOST

    return player_eaten

def ghostMoveMedium():
    # GHOST CAN MOVE DIAGNALLY

    player_eaten = False
    for ghost in ghost_coordinates:

        # 50/50 randomly decide if ghost will move at all
        if random.randint(2) == 0:

            # Up/Down
            if ghost.x < p1.x and (not ghost.x == 0):

                if (board[ghost.x+1][ghost.y] == EMPTY) or (board[ghost.x+1][ghost.y] == PLAYER):
                    if board[ghost.x+1][ghost.y] == PLAYER:
                        player_eaten = True

                    board[ghost.x][ghost.y] = EMPTY
                    ghost.x += 1
                    board[ghost.x][ghost.y] = GHOST

            elif ghost.x > p1.x and (not ghost.x == HEIGHT-1):

                if (board[ghost.x-1][ghost.y] == EMPTY) or (board[ghost.x-1][ghost.y] == PLAYER):
                    if board[ghost.x-1][ghost.y] == PLAYER:
                        player_eaten = True

                    board[ghost.x][ghost.y] = EMPTY
                    ghost.x -= 1
                    board[ghost.x][ghost.y] = GHOST

        # 50/50 randomly decide whether ghost will move horizontal or vertical towards player, but not both
        if random.randint(2) == 0:

            # Left/Right
            if ghost.y < p1.y and (not ghost.y == 0):

                if (board[ghost.x][ghost.y+1] == EMPTY) or (board[ghost.x][ghost.y+1] == PLAYER):
                    if board[ghost.x][ghost.y+1] == PLAYER:
                        player_eaten = True

                    board[ghost.x][ghost.y] = EMPTY
                    ghost.y += 1
                    board[ghost.x][ghost.y] = GHOST
            elif ghost.y > p1.y and (not ghost.y == WIDTH-1):

                if (board[ghost.x][ghost.y-1] == EMPTY) or (board[ghost.x][ghost.y-1] == PLAYER):
                    if board[ghost.x][ghost.y-1] == PLAYER:
                        player_eaten = True

                    board[ghost.x][ghost.y] = EMPTY
                    ghost.y -= 1
                    board[ghost.x][ghost.y] = GHOST

    return player_eaten

def ghostMoveImpossible():
    # GHOST CAN MOVE DIAGNALLY AND ALWAYS DO

    player_eaten = False
    for ghost in ghost_coordinates:

        # Up/Down
        if ghost.x < p1.x and (not ghost.x == 0):

            if (board[ghost.x+1][ghost.y] == EMPTY) or (board[ghost.x+1][ghost.y] == PLAYER):
                if board[ghost.x+1][ghost.y] == PLAYER:
                    player_eaten = True

                board[ghost.x][ghost.y] = EMPTY
                ghost.x += 1
                board[ghost.x][ghost.y] = GHOST

        elif ghost.x > p1.x and (not ghost.x == HEIGHT-1):

            if (board[ghost.x-1][ghost.y] == EMPTY) or (board[ghost.x-1][ghost.y] == PLAYER):
                if board[ghost.x-1][ghost.y] == PLAYER:
                    player_eaten = True

                board[ghost.x][ghost.y] = EMPTY
                ghost.x -= 1
                board[ghost.x][ghost.y] = GHOST

        # Left/Right
        if ghost.y < p1.y and (not ghost.y == 0):

            if (board[ghost.x][ghost.y+1] == EMPTY) or (board[ghost.x][ghost.y+1] == PLAYER):
                if board[ghost.x][ghost.y+1] == PLAYER:
                    player_eaten = True

                board[ghost.x][ghost.y] = EMPTY
                ghost.y += 1
                board[ghost.x][ghost.y] = GHOST
        elif ghost.y > p1.y and (not ghost.y == WIDTH-1):

            if (board[ghost.x][ghost.y-1] == EMPTY) or (board[ghost.x][ghost.y-1] == PLAYER):
                if board[ghost.x][ghost.y-1] == PLAYER:
                    player_eaten = True

                board[ghost.x][ghost.y] = EMPTY
                ghost.y -= 1
                board[ghost.x][ghost.y] = GHOST

    return player_eaten

def startScreen():

    s = "\n\t   ~~~ EAT THE SNAILS!! (@) ~~~\n\n"
    for i in range(len(s)):
         print(f"{s[i]}", end='', flush=True)
         sleep(.026)

    sleep(0.5)
    printASCIIArt('s')
    sleep(0.5)


    s2 = "    *** DON'T LET THE GHOSTS EAT YOU!! (G) ***\n\n"
    for i in range(len(s2)):
        print(f"{s2[i]}", end='', flush=True)
        sleep(.026)

    sleep(0.5)
    printASCIIArt('g')
    sleep(0.5)

    s3 = "  *** Type 'a', 's', 'w', 'd' to move!! ***\n\n"
    for i in range(len(s3)):
        print(f"{s3[i]}", end='', flush=True)
        sleep(.026)

    sleep(0.5)
    s4 = " *** Or type 'quit' at any time to exit game! ***\n"
    for i in range(len(s4)):
        print(f"{s4[i]}", end='', flush=True)
        sleep(.025)

    sleep(0.5)

#      ---- PRINT_ASCII_ART() -----
def printASCIIArt(choice):

    if choice == 's':
        s = "\t         .----.   @   @\n"
        for i in range(len(s)):
            print(f"{s[i]}", end='', flush=True)
            sleep(.008)
        s2 = "\t        / .-\"-.`.  \\v/\n"
        for i in range(len(s2)):
            print(f"{s2[i]}", end='', flush=True)
            sleep(.008)

        s3 = "\t        | | '\\ \\ \\_/ )\n"
        for i in range(len(s3)):
            print(f"{s3[i]}", end='', flush=True)
            sleep(.008)


        s4 = "\t      ,-\\ `-.' /.'  /\n"
        for i in range(len(s4)):
            print(f"{s4[i]}", end='', flush=True)
            sleep(.008)

        s5 = "\t     '---`----'----'\n\n";
        for i in range(len(s5)):
            print(f"{s5[i]}", end='', flush=True)
            sleep(.008)

    elif choice == 'g':
        g = "\t           .-.\n"
        for i in range(len(g)):
            print(f"{g[i]}", end='', flush=True)
            sleep(.008)

        g2 = "\t          (o o)\n"
        for i in range(len(g2)):
            print(f"{g2[i]}", end='', flush=True)
            sleep(.008)




        g3 = "\t          | O \\\n"
        for i in range(len(g3)):
            print(f"{g3[i]}", end='', flush=True)
            sleep(.008)


        g4 = "\t           \\   \\\n"
        for i in range(len(g4)):
            print(f"{g4[i]}", end='', flush=True)
            sleep(.008)


        g5 = "\t           `~~~'\n\n";
        for i in range(len(g5)):
            print(f"{g5[i]}", end='', flush=True)
            sleep(.008)
    return

def countdown(countdown_type):

    # Countdown for start screen
    if countdown_type == 'start':
        s = "\n \t\t~~~ SNAIL EATER ~~~\nBegins in...\n"
        for i in range(len(s)):
            print(f"{s[i]}", end='', flush=True)
            sleep(.028)

    sleep(.8)
    print("\t\t", end='')
    for i in range(3, 0, -1):
        s1 = "     ~~ "
        s2 = " ~~\n"


        for j in range(len(s1)):
            print(f"{s1[j]}", end='', flush=True)
            sleep(.03)

        print(f"{i}", end='')
        sleep(.025)

        for j in range(len(s2)):
            print(f"{s2[j]}", end='', flush=True)
            sleep(.025)
        if i > 1:
            print("\t\t", end='')
        sleep(.8)

    print("\n\t\t    ~~ GO! ~~\n")
    sleep(1.1)

    return

def chooseDifficulty():
    prompt = "\nChoose difficulty level (easy, hard or impossible!): "
    while True:
        choice = input(prompt).strip().lower()
        if choice == 'easy' or choice == 'hard' or choice == 'impossible':
            return choice
        else:
            print("Please type 'easy', 'hard' or 'impossible'.")

def highestScore(high_scores):

    highest_scores = []
    print(sorted(high_scores, key=lambda high_scores: high_scores['LEVELS WON']))



def checkHighScores(difficulty):

    # Read current high scores into list of dicts
    high_scores = []
    path = f"./resources/high_scores_{difficulty}.csv"

    # Iterate through csv
    with open(path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            high_scores.append(row)

    # Determine highest score(s)
    high_scores_sorted = []

    for entry in sorted(high_scores, key=lambda high_scores: high_scores['LEVELS WON'], reverse=True):
        high_scores_sorted.append(entry)

    # rewriteHighScoresInOrder(difficulty, high_scores)

    return high_scores_sorted


# def rewriteHighScoresInOrder(difficulty, high_scores_sorted):

#     path = f"./resources/high_scores_{difficulty}.csv"

#     columns = ['NAME','LEVELS WON','TIMESTAMP']

#     # Rewrite scores to csv
#     with open(path, 'w') as file:
#         writer = csv.DictWriter(file, fieldnames=columns)

#         # ReWrite header
#         for column in columns:
#             if not column == columns[len(columns)-1]:
#                 file.write(f"{column},")
#             else:
#                 file.write(column)
#         file.write('\n')

#         # Re-write entries in order
#         for entry in high_scores_sorted:
#             writer.writerow({'NAME': entry['NAME'], 'LEVELS WON': entry['LEVELS WON'], 'TIMESTAMP': entry['TIMESTAMP']})

def recordScore(name, score, difficulty, high_scores_sorted):

    # APPENDS SCORE TO CSV

    if score == 0:
        return

    timestamp = datetime.now()
    new_entry = {'NAME': name, 'LEVELS WON': score, 'TIMESTAMP': timestamp}

    # Append new entry and resort
    high_scores_sorted.append(new_entry)
    high_scores_sorted.sort(key=lambda high_scores_sorted: int(high_scores_sorted['LEVELS WON']), reverse=True)


    path = f"./resources/high_scores_{difficulty}.csv"
    columns = ['NAME','LEVELS WON','TIMESTAMP']

    # Open file (Write mode) Rerecord scores in order with new entry
    with open(path, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=columns)

        # ReWrite header
        for column in columns:
            if not column == columns[len(columns)-1]:
                file.write(f"{column},")
            else:
                file.write(column)
        file.write('\n')

        # Iterate through scores, writing to csv
        for entry in high_scores_sorted:
            writer.writerow({'NAME': entry['NAME'], 'LEVELS WON': entry['LEVELS WON'], 'TIMESTAMP': entry['TIMESTAMP']})







