from rotate import rotate
import numpy as np
import random
import time
from projection import get_projection
from get_surface import get_surface
# 创建一个三维数组
matrix_3d = np.array([[[0, 0, 0, 0, 0],
                       [0, 5, 5, 5, 0],
                       [0, 5, 5, 5, 0],
                       [0, 5, 5, 5, 0],
                       [0, 0, 0, 0, 0]],
                      [[0, 3, 3, 3, 0],
                       [4, 1, 2, 3, 2],
                       [4, 4, 5, 6, 2],
                       [4, 7, 8, 9, 2],
                       [0, 1, 1, 1, 0]],
                      [[0, 3, 3, 3, 0],
                       [4, 10, 20, 30, 2],
                       [4, 40, 50, 60, 2],
                       [4, 70, 80, 90, 2],
                       [0, 1, 1, 1, 0]],
                      [[0, 3, 3, 3, 0],
                       [4, 100, 200, 300, 2],
                       [4, 400, 500, 600, 2],
                       [4, 700, 800, 900, 2],
                       [0, 1, 1, 1, 0]],
                      [[0, 0, 0, 0, 0],
                       [0, 6, 6, 6, 0],
                       [0, 6, 6, 6, 0],
                       [0, 6, 6, 6, 0],
                       [0, 0, 0, 0, 0]]
                      ])
file = open("1.txt", "w")
time_1 = time.time()
#7层
nn = 0
for i in range(12):
    for j in range(12):
        for k in range(12):
            for l in range(12):
                for m in range(12):
                    for n in range(12):
                            nn+=1
                            matrix_3d = rotate(matrix_3d, move[i], 90, len(move[i]))
                            matrix_3d = rotate(matrix_3d, move[j], 90, len(move[j]))
                            matrix_3d = rotate(matrix_3d, move[k], 90, len(move[k]))
                            matrix_3d = rotate(matrix_3d, move[l], 90, len(move[l]))
                            matrix_3d = rotate(matrix_3d, move[m], 90, len(move[m]))
                            matrix_3d = rotate(matrix_3d, move[n], 90, len(move[n]))
                            move_str = move[i] + move[j] + move[k] + move[l]+ move[m] + move[n]
                            file.write("".join((map(str, get_surface(matrix_3d)))) + "->" + move_str +"\n")

file.close()
time = time.time() - time_1
print("运行时间:", time)
print(nn)