def print_board(board):
    print("---------")
    for row in board:
        print(f"| {' '.join(row)} |")
    print("---------")


def check_win(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    
    return False


def check_draw(board):
    return all(cell != ' ' for row in board for cell in row)


def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)
        
        try:
            row = int(input(f"Player {current_player}, enter the row (0, 1, 2): "))
            col = int(input(f"Player {current_player}, enter the column (0, 1, 2): "))
            
            if row not in range(3) or col not in range(3):
                print("Invalid input. Please enter row and column values between 0 and 2.")
                continue

            if board[row][col] != ' ':
                print("Cell already taken. Choose another cell.")
                continue
            
            board[row][col] = current_player
            
            if check_win(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            
            if check_draw(board):
                print_board(board)
                print("It's a draw!")
                break
            
            current_player = 'O' if current_player == 'X' else 'X'
        
        except ValueError:
            print("Invalid input. Please enter numeric values for row and column.")

if __name__ == "__main__":
    play_game()