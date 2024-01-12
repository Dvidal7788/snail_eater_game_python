import func
from time import sleep
import argparse

def main():
    parser = argparse.ArgumentParser(description='Snail Eater Game')
    args = parser.parse_args()

    game_logic()

def game_logic():

    func.startScreen()
    difficulty = func.chooseDifficulty()
    func.countdown('start')


    level = 1

    while True:

        ghost_num = func.GHOST_START_NUM + (level-1)


        # Create list of ghost coordinates long enough for current amount of ghosts
        for i in range(ghost_num):
            new_coordinate = func.Coordinates(0,0)
            func.ghost_coordinates.append(new_coordinate)

        # Setup
        func.resetBoard()
        func.spawnPlayer()
        func.spawnBlocks(level+2)
        func.spawnGhosts(ghost_num)
        func.spawnSnails(func.SNAIL_START_NUM + (level-1))

        func.snails_left = func.SNAIL_START_NUM + (level-1)

        # Loop for each move until level is won or lost
        while True:
            func.printBoard(level)

            # Player Move
            won_lost = func.playerMove()

            # Check if player won, lost or quit game
            if won_lost == 'g' or func.snails_left == 0 or won_lost == 'q':
                break

            # Ghost Move
            if difficulty == 'easy':
                player_eaten = func.ghostMoveEasy()
            elif difficulty == 'medium':
                player_eaten = func.ghostMoveHard()
            else:
                player_eaten = func.ghostMoveImpossible()
            if player_eaten:
                break



        # End of level
        func.printBoard(level)

        if won_lost == 'q':
            break

        if func.snails_left == 0:
            print(f"Good job!\nYou Passed Level {level}!")
            level += 1
            print(f"\nStarting Level {level} in...\n")
        elif won_lost == 'g':
            print("You LOST!!! (You ran into a ghost!)")
            print(f"\nRedo Level {level} in...\n")
        elif player_eaten:
            print("You LOST!!! (A ghost ate you!)")
            print(f"\nRedo Level {level} in...\n")

        #  Countdown
        func.countdown('next_level')



    # --- End Game ---
    func.printASCIIArt('s')
    func.printASCIIArt('g')

    # Retreive high scores sorted
    high_scores_sorted = func.checkHighScores(difficulty)

    # Print highest scores only (i.e. 1st place or people who tied for 1st place)
    print("CURRENT HIGHEST SCORE(S):")
    for i in range(len(high_scores_sorted)):

        # Make sure not to compare index 0 to -1, resulting in buffer underrun
        if i > 0:
            if high_scores_sorted[i]['LEVELS WON'] < high_scores_sorted[i-1]['LEVELS WON']:
                break

        print(high_scores_sorted[i])


    # Show player their score
    score = level-1
    if score > 0:

        if score == 1:
            print(f"YOU BEAT {score} LEVEL!")
        else:
            print(f"YOU BEAT {score} LEVELS!")


        # Make sure not to index into empty list
        if len(high_scores_sorted) > 0:

            # If player tied or beat the highest scores
            if score > int(high_scores_sorted[0]['LEVELS WON']):
                print(f"COGRATULATIONS!\nTHAT'S A NEW HIGH SCORE!!")

            elif score == int(high_scores_sorted[0]['LEVELS WON']):
                print(f"COGRATULATIONS!\nYOU TIED THE HIGHEST SCORE!!")

        elif len(high_scores_sorted) == 0:
            # If no scores have been recorded yet
            print(f"COGRATULATIONS!\nTHAT'S A NEW HIGH SCORE!!")

        # Record new score
        name = input("TYPE YOUR NAME TO RECORD YOUR SCORE: ")
        func.recordScore(name, score, difficulty, high_scores_sorted)


    print("\nThanks for playing SNAIL EATER!!\n")
    print("\n~~ GOODBYE!! ~~\n")


if __name__ == "__main__":
    main()
