import turtle as t
from copy import deepcopy
from random import choice
from time import sleep

# Import functions from the local package
from mptpkg import voice_to_text, print_say


def conn():
    t.setup(700, 600, 10, 70)
    t.hideturtle()
    t.tracer(False)
    t.bgcolor("lightgreen")
    t.title("Connect Four in Turtle Graphics")
    # Draw six thick vertical lines
    t.pensize(5)
    for i in range(-250, 350, 100):
        t.up()
        t.goto(i, -350)
        t.down()
        t.goto(i, 350)
        t.up()
    # Draw five thin gray horizontal lines to form grid    
    t.pensize(1)
    t.pencolor("grey")
    for i in range(-200, 300, 100):
        t.up()
        t.goto(-350, i)
        t.down()
        t.goto(350, i)
        t.up()
    # Write column numbers on the board
    colnum = 1
    for x in range(-300, 350, 100):
        t.goto(x, 270)
        t.write(colnum, font=('Arial', 20, 'normal'))
        colnum += 1
    # The red player moves first
    turn = "red"
    # The x-coordinates of the center of the 7 columns
    xs = [-300, -200, -100, 0, 100, 200, 300]
    # The y-coordinates of the center of the 6 rows
    ys = [-250, -150, -50, 50, 150, 250]
    # Keep track of the occupied cells
    occupied = [list(), list(), list(), list(), list(), list(), list()]
    # Create a second turtle to show disc falling
    fall = t.Turtle()
    fall.up()
    fall.hideturtle()
    # Create a list of valid moves
    validinputs = [1, 2, 3, 4, 5, 6, 7]

    # Define a horizontal4() function to check connecting 4 horizontally
    def horizontal4(x, y, color, board):
        win = False
        for dif in (-3, -2, -1, 0):
            try:
                if board[x + dif][y] == color and board[x + dif + 1][y] == color and board[x + dif + 2][y] == color and \
                        board[x + dif + 3][y] == color and x + dif >= 0:
                    win = True
            except IndexError:
                pass
        return win
        # Define a vertical4() function to check connecting 4 vertically

    def vertical4(x, y, color, board):
        win = False
        try:
            if board[x][y] == color and board[x][y - 1] == color and board[x][y - 2] == color and board[x][
                y - 3] == color and y - 3 >= 0:
                win = True
        except IndexError:
            pass
        return win
        # Define a forward4() function to check connecting 4 diagonally in / shape

    def forward4(x, y, color, board):
        win = False
        for dif in (-3, -2, -1, 0):
            try:
                if board[x + dif][y + dif] == color and board[x + dif + 1][y + dif + 1] == color and board[x + dif + 2][
                    y + dif + 2] == color and board[x + dif + 3][
                    y + dif + 3] == color and x + dif >= 0 and y + dif >= 0:
                    win = True
            except IndexError:
                pass
        return win
        # Define a back4() function to check connecting 4 diagonally in \ shape

    def back4(x, y, color, board):
        win = False
        for dif in (-3, -2, -1, 0):
            try:
                if board[x + dif][y - dif] == color and board[x + dif + 1][y - dif - 1] == color and board[x + dif + 2][
                    y - dif - 2] == color and board[x + dif + 3][
                    y - dif - 3] == color and x + dif >= 0 and y - dif - 3 >= 0:
                    win = True
            except IndexError:
                pass
        return win
        # Define a win_game() function to check if someone wins the game

    def win_game(num, color, board):
        win = False
        # Convert column and row numbers to indexes in the list of lists board
        x = num - 1
        y = len(board[x]) - 1
        # Check all winning possibilities
        if vertical4(x, y, color, board) == True:
            win = True
        if horizontal4(x, y, color, board) == True:
            win = True
        if forward4(x, y, color, board) == True:
            win = True
        if back4(x, y, color, board) == True:
            win = True
        # Return the value stored in win
        return win  # Count the number of rounds

    rounds = 1

    # Define the validmoves() function to ensure three future moves
    # will not cause any column to have more than six discs in it 
    def validmoves(m1, m2, m3, occupied):
        validmove = False
        if m1 == m2 == m3 and len(occupied[m1 - 1]) <= 3:
            validmove = True
        if m1 == m2 and m2 != m3 and len(occupied[m1 - 1]) <= 4:
            validmove = True
        if m1 == m3 and m2 != m3 and len(occupied[m1 - 1]) <= 4:
            validmove = True
        if m3 == m2 and m2 != m1 and len(occupied[m3 - 1]) <= 4:
            validmove = True
        return validmove
        # Define the smart_computer() function

    def smart_computer():
        if turn == "red":
            nonturn = "yellow"
        else:
            nonturn = "red"
        # Take column 4 in the first move
        if len(occupied[3]) == 0:
            return 4
        # If only one column has free slots, take it
        if len(validinputs) == 1:
            return validinputs[0]
        # Otherwise, see what will happen the next move hypothetically 
        winner = []
        # Go through all possible moves, and see if there is a winning move
        for move in validinputs:
            tooccupy = deepcopy(occupied)
            tooccupy[move - 1].append(turn)
            if win_game(move, turn, tooccupy) == True:
                winner.append(move)
                # If there is a winning move, take it
        if len(winner) > 0:
            return winner[0]
            # If no winning move, look two steps ahead
        if len(winner) == 0 and len(validinputs) >= 2:
            loser = []
            # Check if your opponent has a winning move        
            for m1 in validinputs:
                for m2 in validinputs:
                    if m2 != m1:
                        tooccupy = deepcopy(occupied)
                        tooccupy[m1 - 1].append(turn)
                        tooccupy[m2 - 1].append(nonturn)
                        if win_game(m2, nonturn, tooccupy) == True:
                            winner.append(m2)
                    if m2 == m1 and len(occupied[m1 - 1]) <= 4:
                        tooccupy2 = deepcopy(occupied)
                        tooccupy2[m1 - 1].append(turn)
                        tooccupy2[m2 - 1].append(nonturn)
                        if win_game(m2, nonturn, tooccupy2) == True:
                            loser.append(m2)
                            # If your opponent has a winnng move, block it
            if len(winner) > 0:
                return winner[0]
            # If you can make a move to help your opponent to win, avoid it
            if len(loser) > 0:
                myvalids = deepcopy(validinputs)
                for i in range(len(loser)):
                    myvalids.remove(loser[i])
                if len(myvalids) > 0:
                    return choice(myvalids)
                    # Otherwise, look 3 moves ahead
            if len(winner) == 0 and len(loser) == 0:
                # Look at all possible combinations of 3 moves ahead
                for m1 in validinputs:
                    for m2 in validinputs:
                        for m3 in validinputs:
                            if validmoves(m1, m2, m3, occupied) == True:
                                tooccupy3 = deepcopy(occupied)
                                tooccupy3[m1 - 1].append(turn)
                                tooccupy3[m2 - 1].append(nonturn)
                                tooccupy3[m3 - 1].append(turn)
                                if win_game(m3, turn, tooccupy3) == True:
                                    winner.append(m1)
                                    # See if there is a move now that can lead to winning in 3 moves
                if len(winner) > 0:
                    cnt = {winner.count(x): x for x in winner}
                    maxcnt = sorted(cnt.keys())[-1]
                    return cnt[maxcnt]

                    # Obtain move from a human player

    def person():
        print_say(f"Player {turn}, what's your move?")
        return voice_to_text().lower()

    # Obtain a move from a simple computer
    def simple_computer():
        return choice(validinputs)

    # Ask you for your choice of opponent
    while True:
        print_say("Do you want your opponent to be a person, a simple computer, or a smart computer?")
        which_player = voice_to_text().lower()
        print_say(f"You said {which_player}.")
        if 'person' in which_player:
            player = person
            break
        elif 'simple' in which_player:
            player = simple_computer
            break
        elif 'smart' in which_player:
            player = smart_computer
            break
    # Ask if you want to play first or second
    while True:
        print_say("Do you want to play first or second?")
        preference = voice_to_text().lower()
        print_say(f"You said {preference}.")
        if 'first' in preference:
            preference = 1
            break
        elif 'second' in preference:
            preference = 2
            break
    # Add a dictionary of words to replace
    to_replace = {'number ': '', 'cell ': '', 'column ': '',
                  'one': '1', 'two': '2', 'three': '3',
                  'four': '4', 'for': '4', 'five': '5',
                  'six': '6', 'seven': '7'}
    # Start game loop
    while True:
        # See whose turn to play
        if (preference + rounds) % 2 == 0:
            print_say(f"Player {turn}, what's your move?")
            inp = voice_to_text().lower()
        else:
            inp = player()
            if inp == None:
                inp = choice(validinputs)
        print_say(f"Player {turn} chooses {inp}.")
        try:
            for x in list(to_replace.keys()):
                inp = inp.replace(x, to_replace[x])
        except:
            pass
        # See if input is valid
        try:
            if int(inp) in validinputs:
                col = int(inp)
                # Calculate the lowest available row number in that column
                row = len(occupied[col - 1]) + 1
                # Show the disc fall from the top
                if row < 6:
                    for i in range(6, row, -1):
                        fall.goto(xs[col - 1], ys[i - 1])
                        fall.dot(80, turn)
                        t.update()
                        sleep(0.05)
                        fall.clear()
                # Go to the cell and place a dot of the player's color
                t.up()
                t.goto(xs[col - 1], ys[row - 1])
                t.dot(80, turn)
                t.update()
                # Add the move to the occupied list to keep track
                occupied[col - 1].append(turn)
                # Check if the player has won
                if win_game(col, turn, occupied) == True:
                    # If a player wins, invalid all moves, end the game
                    validinputs = []
                    print_say(f"Congrats player {turn}, you won!")
                    break
                # If all cellls are occupied and no winner, it's a tie
                elif rounds == 42:
                    print_say("Game over, it's a tie!")
                    break
                # Counting rounds
                rounds += 1
                # Update the list of valid moves
                if len(occupied[col - 1]) == 6:
                    validinputs.remove(str(col))
                    # Give the turn to the other player
                if turn == "red":
                    turn = "yellow"
                else:
                    turn = "red"
                    # If inp is not a valid move, try again
        except:
            print_say("Sorry, that's an invalid move!")
    try:
        t.bye()
    except t.Terminator:
        print('exit turtle')
