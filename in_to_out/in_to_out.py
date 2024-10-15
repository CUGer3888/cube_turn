"""
Created on 2024/10/9 22:00
@author: yuanzhangjun
gaol: input surface ,return internal
"""


def in_to_out(matrix_3d):
    # 通过魔方的表面反演出内部
    # 八个角
    # (1,1,1) (3,1,1) (1,3,1) (3,3,1)
    # (1,1,3) (3,1,3) (1,3,3) (3,3,3)
    # 十二个棱
    # (2,1,1) (3,2,1) (2,3,1) (1,2,1)
    # (1,1,2) (1,3,2) (3,1,2) (3,3,2)
    # (1,2,3) (2,1,3) (3,2,3) (2,3,3)
    # 六个面心
    # (2,2,0) (2,2,4) (2,1,2)
    # (2,3,2) (3,2,2) (0,2,2)
    centre_point = (2, 2, 2)
    all_lis = [(1, 1, 1), (3, 1, 1), (1, 3, 1), (3, 3, 1),
               (1, 1, 3), (3, 1, 3), (1, 3, 3), (3, 3, 3),

               (2, 1, 1), (3, 2, 1), (2, 3, 1), (1, 2, 1),
               (1, 1, 2), (1, 3, 2), (3, 1, 2), (3, 3, 2),
               (1, 2, 3), (2, 1, 3), (3, 2, 3), (2, 3, 3),

               (2, 1, 2), (3, 2, 2), (2, 3, 2), (1, 2, 2), (2, 2, 1), (2, 2, 3)]
    dir_lis = [{3, 4, 5}, {4, 5}, {1, 4, 5}, {1, 5}, {1, 2, 5}, {2, 5}, {2, 3, 5}, {3, 5},
               {3, 4}, {4}, {1, 4}, {1}, {1, 2}, {2}, {2, 3}, {3},
               {6, 3, 4}, {6, 4}, {6, 1, 4}, {6, 1}, {6, 1, 2}, {6, 2}, {6, 2, 3}, {6, 3},
               {5}, {6}]
    dirctary = {
        0: 1,
        1: 4,
        2: 7,
        3: 8,
        4: 9,
        5: 6,
        6: 3,
        7: 2,
        8: 10,
        9: 40,
        10: 70,
        11: 80,
        12: 90,
        13: 60,
        14: 30,
        15: 20,
        16: 100,
        17: 400,
        18: 700,
        19: 800,
        20: 900,
        21: 600,
        22: 300,
        23: 200,
        24: 5,
        25: 500}
    for i in all_lis:
        x = i[0]
        y = i[1]
        z = i[2]
        # print((x,y,z))
        temp_set = set()
        if x - centre_point[0] != 0:
            temp_set.add(matrix_3d[z][x + x - centre_point[0]][y])
        if y - centre_point[1] != 0:
            temp_set.add(matrix_3d[z][x][y + y - centre_point[1]])
        if z - centre_point[2] != 0:
            temp_set.add(matrix_3d[z + z - centre_point[2]][x][y])
        matrix_3d[z][x][y] = dirctary[dir_lis.index(temp_set)]
    return matrix_3d


def get(matrix_3d, num):
    maxlen = len(matrix_3d)
    for i in range(maxlen):
        for j in range(maxlen):
            for k in range(maxlen):
                if matrix_3d[i][j][k] == num:
                    return (i, j, k)  # 返回的是(z,x,y)
    return None
