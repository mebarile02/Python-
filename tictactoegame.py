"""
tictactoegame.py

This is a complete tictactoegame.  It needs to be edited/consolidated for efficiency.
"""



import sys

def display_board(my_list):
    print(7*' ' + '|' + 7*' ' + '|')
    print(3*' ' + my_list[6] + 3*' ' + '|' +
          3*' ' + my_list[7] + 3*' ' + '|' +
          3* ' ' + my_list[8])
    print(7*' ' + '|' + 7*' ' + '|')
    print(12*'- ')
    print(7*' ' + '|' + 7*' ' + '|')
    print(3*' ' + my_list[3] + 3*' ' + '|' +
          3*' ' + my_list[4] + 3*' ' + '|' +
          3* ' ' + my_list[5])
    print(7*' ' + '|' + 7*' ' + '|')
    print(12*'- ')
    print(7*' ' + '|' + 7*' ' + '|')
    print(3*' ' + my_list[0] + 3*' ' + '|' +
          3*' ' + my_list[1] + 3*' ' + '|' +
          3* ' ' + my_list[2])
    print(7*' ' + '|' + 7*' ' + '|')
    


# function to add 1 to global variable
def plus_one(arg):
    return arg + 1

# assign even turn to player 1, odd turn to player 2

def play_again():
    choice = input('Would you like to play again? Enter Y or N: ' ).lower()
    if choice == 'y':
        return True
    else:
        return False
    

# initial empty board
board_list = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

# Greeting 
print('Welcome to Tic Tac Toe.')

# Player 1 initial input
choose_sides = input('Player 1, do you want to be x or o? ').lower()

# makes sure x or o is entered, assigns even count to x side, odd count to
# o side

while choose_sides != 'x' and choose_sides != 'o':
    choose_sides = input('Player 1, do you want to be x or o? ').lower()
else:
    if choose_sides == 'x':
        count = 0
    else:
        count = 1
    
# assign even turn to player 1, odd count to player 2
turn = 0
dec = True

while dec:
    while board_list[:3] != ['x','x','x'] and board_list[:3] != ['o','o','o'] and \
        board_list[3:6] != ['x','x','x'] and board_list[3:6] != ['o','o','o'] and \
        board_list[6:] != ['x','x','x'] and board_list[6:] != ['o','o','o'] and \
        [board_list[0],board_list[3],board_list[6]] != ['x','x','x'] and \
        [board_list[0],board_list[3],board_list[6]] != ['o','o','o'] and \
        [board_list[1],board_list[4],board_list[7]] != ['x','x','x'] and \
        [board_list[1],board_list[4],board_list[7]] != ['o','o','o'] and \
        [board_list[2],board_list[5],board_list[8]] != ['x','x','x'] and \
        [board_list[2],board_list[5],board_list[8]] != ['o','o','o'] and \
        [board_list[0],board_list[4],board_list[8]] != ['x','x','x'] and \
        [board_list[0],board_list[4],board_list[8]] != ['o','o','o'] and \
        [board_list[2],board_list[4],board_list[6]] != ['x','x','x'] and \
        [board_list[2],board_list[4],board_list[6]] != ['o','o','o']:
            if turn%2 == 0:
                if count%2 == 0:
                    try:
                        position = int(input('Player 1, choose a position: '))
                    except:
                        ValueError
                        break
                    while position < 1 or position > 9:
                        position = int(input('Player 1, choose a valid position: '))
                    else:
                        pass
                    while board_list[position - 1] != ' ':
                        position = int(input('Player 1, that position is filled.\n\
Pick an empty position: '))
                    else:
                        board_list[position - 1] = 'x'
                        turn += 1
                        count += 1          
                else:
                    try:
                        position = int(input('Player 1, choose a position: '))
                    except:
                        ValueError
                        break
                    while position < 1 or position > 9:
                        position = int(input('Player 1, choose a valid position: '))
                    else:
                        pass
                    while board_list[position - 1] != ' ':
                        position = int(input('Player 1, that position is filled. \n\
Pick an empty position: '))
                    else:
                        board_list[position - 1] = 'o'
                        turn += 1
                        count += 1 
            else:
                if count%2 == 0:
                    try:
                        position = int(input('Player 2, choose a position: '))
                    except:
                        ValueError
                        break
                    while position < 1 or position > 9:
                        position = int(input('Player 2, choose a valid position: '))
                    else:
                        pass
                    while board_list[position - 1] != ' ':
                        position = int(input('Player 2, that position is filled.\n\
Pick an empty position: '))
                    else:
                        board_list[position - 1] = 'x'
                        turn += 1
                        count += 1          
                else:
                    try:
                        position = int(input('Player 2, choose a position: '))
                    except:
                        ValueError
                        break
                    while position < 1 or position > 9:
                        position = int(input('Player 2, choose a valid position: '))
                    else:
                        pass
                    while board_list[position - 1] != ' ':
                        position = int(input('Player 2, that position is filled.\n\
Pick an empty position: '))
                    else:
                        board_list[position - 1] = 'o'
                        turn += 1
                        count += 1 
            print('\n'*100)
            display_board(board_list)
            print('\n'*5)
    else:
        if (turn-1)%2 == 0:
            print('Player 1 wins!!!')
            dec = play_again()
            if dec:
                board_list = [' ',' ',' ',' ',' ',' ',' ',' ',' ']   
                choose_sides = input('Player 1, do you want to be x or o? ').lower()
                while choose_sides != 'x' and choose_sides != 'o':
                    choose_sides = input('Player 1, do you want to be x or o? ').lower()
                else:
                    if choose_sides == 'x':
                        count = 0
                    else:
                        count = 1
                turn = 0
        else:
            print('Player 2 wins!!!')
            dec = play_again()
            if dec:
                board_list = [' ',' ',' ',' ',' ',' ',' ',' ',' ']   
                choose_sides = input('Player 1, do you want to be x or o? ').lower()
                while choose_sides != 'x' and choose_sides != 'o':
                    choose_sides = input('Player 1, do you want to be x or o? ').lower()
                else:
                    if choose_sides == 'x':
                        count = 0
                    else:
                        count = 1
                turn = 0            
else:
    print('Goodbye!')

sys.exit(0)
