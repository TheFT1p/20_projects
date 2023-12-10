def print_board(board):
    for row in board:
        print(' | '.join(board))
        print('-'*10)


def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0] #row win
        if board[0][i] == board[1][i] == board[2][i]:
            return  board[0][i] # column win

    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0] #diagonal win
    if board[2][0] == board[1][1] == board[0][2] != ' ':
        return board[2][0] #diagonal win

    return None

def is_board_full(board):
    return all(all(cell != ' ' for cell in row) for row in board)


def play_tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    while True:
        print_board(board)
        row = int(input("insert row number: "))
        col = int(input("insert column number: "))

        if board[row][col] == ' ':
            board[row][col] = current_player
            winner = check_winner(board)
            if winner:
                print_board(board)
                print(f"player {winner} wins!")
                break
            elif is_board_full(board):
                print("it's a tie!")
                break
            else:current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("cell already occupied!")


if __name__ == "__main__":
    play_tic_tac_toe()



print("hello world")



