import random

def show_board(board):
    print()
    for i in range(3):
        print(" ".join(board[i]))
    print()

def bomb_game_3x3():
    print("🎮 3x3 Bombani top o‘yini")
    print("Kataklar 1 dan 9 gacha raqamlangan\n")

    board = [["⬜" for _ in range(3)] for _ in range(3)]

    bomba = random.randint(1, 9)

    mapping = {
        1:(0,0), 2:(0,1), 3:(0,2),
        4:(1,0), 5:(1,1), 6:(1,2),
        7:(2,0), 8:(2,1), 9:(2,2)
    }

    show_board(board)

    tanlov = int(input("1-9 oralig‘ida katak tanlang: "))

    row, col = mapping[tanlov]

    if tanlov == bomba:
        board[row][col] = "💣"
        show_board(board)
        print("💥 Boom! Yutqazdingiz!")
    else:
        board[row][col] = "✅"
        show_board(board)
        print("🎉 Tabriklaymiz! Siz tirik qoldingiz!")
        print("Bomba boshqa joyda edi.")

bomb_game_3x3()
