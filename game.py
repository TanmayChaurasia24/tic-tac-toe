import os

def printboard(board):
    for row in board:
        print(" | ".join(row))
        print("-"*9)

def check_winner(board , player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3) or all(board[j][i] == player for j in range(3))):
            return True;

    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
        
    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)


def main():
    board = [[" "for i in range(3)] for i in range(3)]
    current_player = "X"

    while True:
        print("\n")
        os.system('cls')
        printboard(board)

        row = int(input(f"player {current_player}, enter the row in 0,1,2: "))
        col = int(input(f"player {current_player}, enter the coloumn in 0,1,2: "))

        if(0 <= row < 3 and 0 <= col < 3 and board[row][col] == " "):
            board[row][col] = current_player
            if check_winner(board , current_player):
                printboard(board)
                print(f"player{current_player}wins")
                break

        elif(is_full(board)):
            printboard(board)
            print("its a tie")
            break

        current_player = "O" if current_player == "X" else "X"

    else:
        print("invalid move")


if __name__ == '__main__':
    main()
