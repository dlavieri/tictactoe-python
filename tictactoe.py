board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',]
player = None

def print_board():
    layout = f"[{board[0]}][{board[1]}][{board[2]}]\n[{board[3]}][{board[4]}][{board[5]}]\n[{board[6]}][{board[7]}][{board[8]}]\n"
    print(layout)

def game_over():
    global board
    replay = input('Would you like to play again? Y/N')
    if replay.lower == "y":
        start_game()
    else:
        print("OK Bye then!")

def check_for_winner():
    if board[0] != ' ' and board[0] == board[1] == board[2]:
        print(f'{board[0]} is the winner!')
    elif board[3] != ' ' and board[3] == board[4] == board[5]:
        print(f'{board[0]} is the winner!')
    elif board[6] != ' ' and board[6] == board[7] == board[8]:
        print(f'{board[0]} is the winner!')
    elif board[0] != ' ' and board[0] == board[3] == board[6]:
        print(f'{board[0]} is the winner!')
    elif board[1] != ' ' and board[1] == board[4] == board[7]:
        print(f'{board[0]} is the winner!')
    elif board[2] != ' ' and board[2] == board[5] == board[8]:
        print(f'{board[0]} is the winner!')
    elif board[0] != ' ' and board[0] == board[4] == board[8]:
        print(f'{board[0]} is the winner!')
    elif board[2] != ' ' and board[2] == board[4] == board[6]:
        print(f'{board[2]} is the winner!')
    else:
        play_move()


def play_move():
    global player
    move = int(input(f'Player {player}: which square will you choose?'))
    
    if move not in range(0,9):
        print(f'Thats not a valid square, please choose a number square 0 - 8. Row one is 0-1-2, row two is 3-4-5, and row three is 6-7-8')
        return play_move()
    elif board[move] != ' ':
        print('Sorry! that square is taken! Try another square')
        return play_move()
    else:
        board[move] = player.upper()
        if player.lower() == "x":
            player = "O"
            print_board()
            return check_for_winner()
        else:
            player = "X"
            print_board()
            return check_for_winner()



def start_game():
    global player
    global board
    board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',]
    player = input('Will you be player X or player O? Please type just uppercase "X" or "O"');
    
    if player.lower() != "x" and player.lower() != "o":
        player = str(input("That's not valid! please write just X or O"))
    elif player.lower() == "x":
        print("Player X will go first, choose a square")
        play_move()
    else: 
        print("Player O will go first, choose a square")
        play_move()

start_game()