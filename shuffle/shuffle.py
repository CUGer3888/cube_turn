move = ["U", "D", "F", "B", "L", "R", "U'", "D'", "F'", "B'", "L'", "R'"]
import random
from rotate import rotate
def shuffle(matrix,time):
    for i in range(time):
        move1 = random.choice(move)
        if move.index(move1)>=6:
            matrix = rotate(matrix,move1,90,-1)
        else:
            matrix = rotate(matrix,move1,90,1)
    return matrix