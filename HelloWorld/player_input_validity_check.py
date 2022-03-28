winning_cond = {"1": [[0,1,2],[0,3,6],[0,4,8]],
"2": [[0,1,2],[1,4,7]],
"3": [[0,1,2],[2,5,8],[2,4,6]],
"4": [[3,4,5],[0,3,6]],
"5": [[3,4,5],[1,4,7],[0,4,8],[2,4,6]],
"6": [[2,5,8],[3,4,5]],
"7": [[6,7,8],[0,3,6],[2,4,6]],
"8": [[6,7,8], [1,4,7]],
"9": [[6,7,8],[0,4,8],[2,5,8]]}

#def print_board: (Aljosha)
#def check_winners (board):
    #return Bool

#def player_changer():
    #return Player ():

#def validate_input(number):
    #return Bool
number = "6"

numbers = ["1", "2", "3", "4", "5", "x", "o", "8"]

remainingV = []
for i in numbers:
    if i not in ("o", "x"):
        remainingV.append(i)
if number not in numbers:
    print("Invalid input! Please choose between the following numbers: " + str(remainingV))
else:
    print("Pass")