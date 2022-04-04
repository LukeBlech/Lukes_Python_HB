def rps(p1, p2):
            if p1 == 'scissors':
                p1 = 1
            if p1 == 'paper':
                p1 = 2
            if p1 == 'rock':
                p1 == 3
            if p2 == 'scissors':
                p2 = 1
            if p2 == 'paper':
                p2 = 2
            if p2 == 'rock':
                p2 == 3
        # 1<2<3>1
            if p1 - p2 < 0:
                return "Player 1 won!"
            if p1 - p2 == [0]:
                return "Draw!"
            else:
                return "Player 2 won!"
            