"""
 Napisz skrypt, który będzie grą w kółko i krzyżyk
"""
import random


def print_board(board):
    print("  1 2 3")
    for i in range(3):
        print(str(i + 1) + " " + board[i][0] + " " + board[i][1] + " " + board[i][2])


def check_win(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return True
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return True
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    return False


def check_draw(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return False
    return True


def check_move(board, x, y):
    if x < 0 or x > 2 or y < 0 or y > 2:
        return False
    if board[x][y] != " ":
        return False
    return True


def player_move(board):
    x = int(input("Podaj współrzędną x: "))
    y = int(input("Podaj współrzędną y: "))
    if check_move(board, x - 1, y - 1):
        board[x - 1][y - 1] = "X"
        return True
    else:
        print("Błędny ruch")
        return False


def computer_move(board):
    x = random.randint(1, 3)
    y = random.randint(1, 3)
    if check_move(board, x, y):
        board[x][y] = "O"
        return True
    else:
        return False


def game():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    print_board(board)
    while True:
        if player_move(board):
            print_board(board)
            if check_win(board):
                print("Wygrałeś!")
                break
            if check_draw(board):
                print("Remis!")
                break
            if computer_move(board):
                print_board(board)
                if check_win(board):
                    print("Przegrałeś!")
                    break
                if check_draw(board):
                    print("Remis!")
                    break
            else:
                print("Błędny ruch komputera")
        else:
            print("Błędny ruch")


game()
