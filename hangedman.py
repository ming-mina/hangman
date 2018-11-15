import random

def hangman(word):
    wrong = 0
    stages =["",
             "_________       ",
             "|               ",
             "|        |      ",
             "|        o      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome hangman")


    while wrong < len(stages) - 1:
        print("\n")
        msg = "Expect 1 character:"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("You win")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("You lose. Word is {}".format(word))


word_list = ["cat","dog","flowers","knight","girls","pillows","fight","git"]
idx = random.randint(0,len(word_list)-1)

hangman( word_list[idx] )
