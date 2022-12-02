import csv

def score_1(them, me):
    # lose
    if me == ((them + 1) % 3) + 1:
        return me + 0
    # draw
    if me == them:
        return me + 3
    # win
    if me == (them % 3) + 1:
        return me + 6 
        
def score_2(them, me):
    # lose
    if me == 1:
        return 0 + ((them - 2) % 3) + 1
    # draw
    if me == 2:
        return 3 + them 
    # win
    if me == 3:
        return 6 + ((them) % 3) + 1

print(sum([score_1(x, y) for x, y in [list(map(int, x[0].replace("A", "1").replace("B", "2").replace("C", "3").replace("X", "1").replace("Y", "2").replace("Z", "3").split(" "))) for x in list(csv.reader(open("game.txt", "r")))]]))
print(sum([score_2(x, y) for x, y in [list(map(int, x[0].replace("A", "1").replace("B", "2").replace("C", "3").replace("X", "1").replace("Y", "2").replace("Z", "3").split(" "))) for x in list(csv.reader(open("game.txt", "r")))]]))
