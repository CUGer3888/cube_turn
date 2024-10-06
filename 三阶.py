# cube = [
#     [[0, 0, 0],
#      [0, 0, 0],
#      [0, 0, 0]],
#     [[0, 0, 0],
#      [0, 0, 0],
#      [0, 0, 0]],
#     [[0, 0, 0],
#      [0, 0, 0],
#      [0, 0, 0]],
# ]
# # [z][y][x]相反
# """
# 1 1 1 ,
# 1 1 1 ,
# 1 1 1 ,
#
#
# 1 1 1 ,
# 2 0 1 ,
# 1 1 1 ,
#
#
# 1 1 1 ,
# 1 1 1 ,
# 1 1 1 ,
# """
# # for i in range(3):
# #     for j in range(3):
# #         for k in range(3):
# #             print(cube[i][j][k],end = " ")
# #         print(",")
# #     print("\n")
# center_point = (1, 1, 1)
#
#
# # class Cube():
# #     def __init__(self,):
# #         self.cube =
# qian =  [[1, 1, 1],
#          [1, 1, 1],
#          [1, 1, 1]]
# hou =   [[3, 3, 3],
#          [3, 3, 3],
#          [3, 3, 3]]
# shang = [[6, 6, 6],
#          [6, 6, 6],
#          [6, 6, 6]]
# xia =   [[5, 5, 5],
#          [5, 5, 5],
#          [5, 5, 5]]
# zuo =   [[4, 4, 4],
#          [4, 4, 4],
#          [4, 4, 4]]
# you =   [[2, 2, 2],
#          [2, 2, 2],
#          [2, 2, 2]]
# # for i in range(3):
# #     for j in range(3):
# #         for k in range(3):
# #             if distance(i, j, k) == 3:
# #                 cube[j][k][z] =
# #             if distance(i, j, k) == 2:
# #                 pass
# #             if distance(i, j, k) == 1:
# #                 pass
# #first floor
# cube[0][0][0]=[3,4,5]
# cube[0][1][0]=[0,4,5]
# cube[0][2][0]=[1,4,5]
#
# cube[0][0][1]=[3,0,5]
# cube[0][1][1]=[0,0,4]
# cube[0][1][2]=[1,0,5]
#
# cube[0][0][2]=[1,2,5]
# cube[0][1][2]=[0,2,5]
# cube[0][2][2]=[1,2,5]
#
#
# #secend floor
# cube[1][0][0]=[3,4,0]
# cube[1][1][0]=[0,4,0]
# cube[1][2][0]=[1,4,0]
#
# cube[1][0][1]=[3,0,0]
# cube[1][1][1]=[0,0,0]
# cube[1][2][1]=[1,0,0]
#
# cube[1][0][2]=[3,2,0]
# cube[1][1][2]=[0,2,0]
# cube[1][2][2]=[1,2,0]
#
# #third floor
# cube[2][0][0]=[3,4,6]
# cube[2][1][0]=[0,4,6]
# cube[2][2][0]=[1,4,6]
#
# cube[2][0][1]=[3,0,6]
# cube[2][1][1]=[0,0,6]
# cube[2][2][1]=[1,0,6]
#
# cube[2][0][2]=[3,2,6]
# cube[2][1][2]=[0,2,6]
# cube[2][2][2]=[1,2,6]
#
# """
# R：右
# L：左
# U：上
# D：下
# F：前
# B：后
#
# direction == -1 : 逆时针
# direction ==  1 : 顺时针
# """
# def rotate(position,direction,angle):
#     if position == "F":
#         if angle==90:
#             if direction==-1:
#                 temp_1 = cube[2][2][0]
#                 temp_2 = cube[1][2][0]
#                 temp_3 = cube[0][2][0]
#
#                 cube[0][2][0]=temp_1
#                 cube[1][2][0]=cube[2][2][1]
#                 cube[2][2][0]=cube[2][2][2]
#
#                 cube[2][2][1]=cube[1][2][2]
#                 cube[2][2][2]=cube[0][2][2]
#
#                 cube[0][2][2]=temp_3
#                 cube[1][2][2]=cube[0][2][1]
#                 cube[0][2][1]=temp_2
#
#             if direction ==1:
#                 temp_1 = cube[2][2][0]
#                 temp_2 = cube[1][2][0]
#                 temp_3 = cube[0][2][0]
#
#                 cube[2][2][0]=temp_3
#                 cube[1][2][0]=cube[0][2][1]
#                 cube[0][2][0]=cube[0][2][2]
#
#                 cube[0][2][1]=cube[1][2][2]
#                 cube[0][2][2]=cube[2][2][2]
#
#                 cube[2][2][2]=temp_1
#                 cube[1][2][2]=cube[2][2][1]
#                 cube[2][2][1]=temp_2
#         if angle==180:
#             temp_1 = cube[2][2][0]
#             temp_2 = cube[1][2][0]
#             temp_3 = cube[0][2][0]
#             temp_4 = cube[2][2][1]
#             cube[2][2][0]=cube[0][2][2]
#             cube[1][2][0]=cube[1][2][2]
#             cube[0][2][0]=cube[2][2][2]
#             cube[2][2][1]=cube[0][2][1]
#             cube[2][2][2]=temp_3
#             cube[1][2][2]=temp_2
#             cube[0][2][2]=temp_1
#             cube[0][2][1]=temp_4
#     # if position == "B":
#     #     if angle==90:
#     #         if direction==-1:
#     #         if direction==1:
#     #     if angle==180:
#     #
#     # if position == "L":
#     #     if angle==90:
#     #         if direction==-1:
#     #         if direction==1:
#     #     if angle==180:
#     # if position == "R":
#     #     if angle==90:
#     #         if direction==-1:
#     #         if direction==1:
#     #     if angle==180:
#     # if position == "U":
#     #     if angle==90:
#     #         if direction==-1:
#     #         if direction==1:
#     #     if angle==180:
#     # if position == "D":
#     #     if angle==90:
#     #         if direction==-1:
#     #         if direction==1:
#     #     if angle==180:

# cube = [[[0, 0, 0, 0, 0],
#          [0, 5, 5, 5, 0],
#          [0, 5, 5, 5, 0],
#          [0, 5, 5, 5, 0],
#          [0, 0, 0, 0, 0]],
#
#         [[0, 3, 3, 3, 0],
#          [4, 0, 0, 0, 2],
#          [4, 0, 0, 0, 2],
#          [4, 0, 0, 0, 2],
#          [0, 1, 1, 1, 0]],
#         [[0, 3, 3, 3, 0],
#          [4, 0, 0, 0, 2],
#          [4, 0, 0, 0, 2],
#          [4, 0, 0, 0, 2],
#          [0, 1, 1, 1, 0]],
#         [[0, 3, 3, 3, 0],
#          [4, 0, 0, 0, 2],
#          [4, 0, 0, 0, 2],
#          [4, 0, 0, 0, 2],
#          [0, 1, 1, 1, 0]],
#
#         [[0, 0, 0, 0, 0],
#          [0, 6, 6, 6, 0],
#          [0, 6, 6, 6, 0],
#          [0, 6, 6, 6, 0],
#          [0, 0, 0, 0, 0]]
#         ]
# for i in range(3):
#     cube[i][3][0]=cube[0][3][4-i]
# def rotate(position, direction, angle):
#     if position == "F":
#         if angle == 90:
#             if direction == -1:
#                 cube[1][3][0]=
#             if direction == 1:
#         if angle == 180:
#
#     if position == "B":
#         if angle == 90:
#             if direction == -1:
#                 if direction == 1:
#         if angle == 180:
#
#     if position == "L":
#         if angle == 90:
#             if direction == -1:
#                 if direction == 1:
#         if angle == 180:
#     if position == "R":
#         if angle == 90:
#             if direction == -1:
#                 if direction == 1:
#         if angle == 180:
#     if position == "U":
#         if angle == 90:
#             if direction == -1:
#                 if direction == 1:
#         if angle == 180:
#     if position == "D":
#         if angle == 90:
#             if direction == -1:
#                 if direction == 1:
#         if angle == 180:

"""
matrix_3d = np.array([[[0, 0, 0, 0, 0],
                       [0, 5, 5, 5, 0],
                       [0, 5, 5, 5, 0],
                       [0, 5, 5, 5, 0],
                       [0, 0, 0, 0, 0]],

                      [[0, 3 ,  3, 3 , 0],
                       [4, 10, 11, 12, 2],
                       [4, 13, 14, 15, 2],
                       [4, 16, 17, 18, 2],
                       [0, 1 ,  1, 1 , 0]],
                      [[0, 3 ,  3, 3 , 0],
                       [4, 20, 21, 22, 2],
                       [4, 23, 24, 25, 2],
                       [4, 26, 27, 28, 2],
                       [0, 1 ,  1, 1 , 0]],
                      [[0, 3 ,  3, 3 , 0],
                       [4, 30, 31, 32, 2],
                       [4, 33, 34, 35, 2],
                       [4, 36, 37, 38, 2],
                       [0, 1 ,  1, 1 , 0]],

                      [[0, 0, 0, 0, 0],
                       [0, 6, 6, 6, 0],
                       [0, 6, 6, 6, 0],
                       [0, 6, 6, 6, 0],
                       [0, 0, 0, 0, 0]]
                      ])# 寻找某个方块坐标
def find_block(matrix_3d, num):
    # color_3 为可变参数
    for i in range(1, 4):
        for j in range(1, 4):
            for k in range(1, 4):
                if matrix_3d[i][j][k] == num:
                    return j, k, i

#检查内点在该位置上是否方向正确
def check_block(matrix_3d, num):
    coodinate = find_block(matrix_3d, num_dir["F_U"])
    x,y,z = coodinate[0],coodinate[1],coodinate[2]
    color_x,color_y,color_z = num_reverse_dir[num].split("_")
    toward_x,toward_y,toward_z = coodinate[0]-2,coodinate[1]-2,coodinate[2]-2
    k=0
    if toward_x!=0:
        if matrix_3d[z][x+toward_x][y] == num_to_color[color_x]:
            k+=1
    else:
        k+=1
    if toward_y!=0:
        if matrix_3d[z][x][y+toward_y] == num_to_color[color_y]:
            k+=1
    else:
        k += 1
    if toward_z!=0:
        if matrix_3d[z+toward_z][x][y] == num_to_color[color_z]:
            k+=1
    else:
        k+=1
    if k==3:
        return True
    else:
        return False
num_to_color={"F":1,"R":2,"B":3,"L":4,"U":6,"D":5,"0":0}
num_dir = {"F_U": 37,"R_U":35,"B_U":31,"L_U":33,
           }
num_reverse_dir = {37:"F_0_U",35: "0_R_U",31: "B_0_U",33: "0_L_U",}
# 顶层：
# 编写函数，确定中点
def find_center(matrix_3d):
    F_center = matrix_3d[0][1][1]
    B_center = matrix_3d[1][1][1]
    L_center = matrix_3d[0][1][0]
    R_center = matrix_3d[0][1][2]
    U_center = matrix_3d[0][0][1]
    D_center = matrix_3d[0][2][1]
    return F_center, B_center, L_center, R_center, U_center, D_center
# print(find_block(matrix_3d, num_dir["F_U"]))
# print(check_block(matrix_3d, num_dir["F_U"]))
# 编写函数，复原十字,顺序：F_U,R_U,B_U,L_U
def cross(matrix_3d):
    #F_U
    if matrix_3d[3][3][2] != 37:
        #寻找点坐标
        coodinate = find_block(matrix_3d, num_dir["F_U"])
        x,y,z = coodinate[0],coodinate[1],coodinate[2]
        #判断方向是否正确
        if check_block(matrix_3d, num_dir["F_U"]):
            pass"""

import numpy as np
import random
# 创建一个三维数组
matrix_3d = np.array([[[0, 0, 0, 0, 0],
                       [0, 5, 5, 5, 0],
                       [0, 5, 5, 5, 0],
                       [0, 5, 5, 5, 0],
                       [0, 0, 0, 0, 0]],

                      [[0, 3, 3, 3, 0],
                       [4, 0, 0, 0, 2],
                       [4, 0, 0, 0, 2],
                       [4, 0, 0, 0, 2],
                       [0, 1, 1, 1, 0]],
                      [[0, 3, 3, 3, 0],
                       [4, 0, 0, 0, 2],
                       [4, 0, 0, 0, 2],
                       [4, 0, 0, 0, 2],
                       [0, 1, 1, 1, 0]],
                      [[0, 3, 3, 3, 0],
                       [4, 0, 0, 0, 2],
                       [4, 0, 0, 0, 2],
                       [4, 0, 0, 0, 2],
                       [0, 1, 1, 1, 0]],

                      [[0, 0, 0, 0, 0],
                       [0, 6, 6, 6, 0],
                       [0, 6, 6, 6, 0],
                       [0, 6, 6, 6, 0],
                       [0, 0, 0, 0, 0]]
                      ])

# rot90 绕y轴顺时针旋转90度
def y_rotate(matrix_3d, k):
    result_3d = np.rot90(matrix_3d, k=k)
    return result_3d

# axes=(2,0),绕x轴逆时针旋转90度
def x_rotate(matrix_3d, k):
    result_3d = np.rot90(matrix_3d, k=k, axes=(2, 0))
    return result_3d

def down_rotate(plane, k):
    # 旋转底面
    plane = np.rot90(plane, k=k, axes=(0, 1))
    return plane

# t = x_rotate(matrix_3d,1)
# print(t)
# exit()
def rotate(matrix_3d, position, angle, direction):
    if position == "F":
        if angle == 90:
            if direction == -1:
                matrix_3d = y_rotate(matrix_3d, 1)
                matrix_3d[0] = down_rotate(matrix_3d[0], -1)
                matrix_3d[1] = down_rotate(matrix_3d[1], -1)
                # 翻回去
                matrix_3d = y_rotate(matrix_3d, -1)

            if direction == 1:
                matrix_3d = y_rotate(matrix_3d, 1)
                matrix_3d[0] = down_rotate(matrix_3d[0], 1)
                matrix_3d[1] = down_rotate(matrix_3d[1], 1)
                # 翻回去
                matrix_3d = y_rotate(matrix_3d, -1)
        if angle == 180:
            matrix_3d = y_rotate(matrix_3d, 1)
            matrix_3d[0] = down_rotate(matrix_3d[0], -1)
            matrix_3d[0] = down_rotate(matrix_3d[0], -1)
            matrix_3d[1] = down_rotate(matrix_3d[1], -1)
            matrix_3d[1] = down_rotate(matrix_3d[1], -1)
            # 翻回去
            matrix_3d = y_rotate(matrix_3d, -1)
    if position == "R":
        if angle == 90:
            if direction == -1:
                matrix_3d = x_rotate(matrix_3d, -1)
                matrix_3d[0] = down_rotate(matrix_3d[0], -1)
                matrix_3d[1] = down_rotate(matrix_3d[1], -1)
                # 翻回去
                matrix_3d = x_rotate(matrix_3d, 1)
            if direction == 1:
                matrix_3d = x_rotate(matrix_3d, -1)
                matrix_3d[0] = down_rotate(matrix_3d[0], 1)
                matrix_3d[1] = down_rotate(matrix_3d[1], 1)
                # 翻回去
                matrix_3d = x_rotate(matrix_3d, 1)
        if angle == 180:
            matrix_3d = x_rotate(matrix_3d, -1)
            matrix_3d[0] = down_rotate(matrix_3d[0], 1)
            matrix_3d[0] = down_rotate(matrix_3d[0], 1)
            matrix_3d[1] = down_rotate(matrix_3d[1], 1)
            matrix_3d[1] = down_rotate(matrix_3d[1], 1)
            matrix_3d = x_rotate(matrix_3d, 1)
    if position == "B":
        if angle == 90:
            if direction == -1:
                matrix_3d = y_rotate(matrix_3d, -1)
                matrix_3d[0] = down_rotate(matrix_3d[0], -1)
                matrix_3d[1] = down_rotate(matrix_3d[1], -1)
                # 翻回去
                matrix_3d = y_rotate(matrix_3d, 1)

            if direction == 1:
                matrix_3d = y_rotate(matrix_3d, -1)
                matrix_3d[0] = down_rotate(matrix_3d[0], 1)
                matrix_3d[1] = down_rotate(matrix_3d[1], 1)
                # 翻回去
                matrix_3d = y_rotate(matrix_3d, 1)
        if angle == 180:
            matrix_3d = y_rotate(matrix_3d, -1)
            matrix_3d[0] = down_rotate(matrix_3d[0], 1)
            matrix_3d[0] = down_rotate(matrix_3d[0], 1)
            matrix_3d[1] = down_rotate(matrix_3d[1], 1)
            matrix_3d[1] = down_rotate(matrix_3d[1], 1)
            # 翻回去
            matrix_3d = y_rotate(matrix_3d, 1)
    if position == "L":
        if angle == 90:
            if direction == -1:
                matrix_3d = x_rotate(matrix_3d, 1)
                matrix_3d[0] = down_rotate(matrix_3d[0], -1)
                matrix_3d[1] = down_rotate(matrix_3d[1], -1)
                # 翻回去
                matrix_3d = x_rotate(matrix_3d, -1)

            if direction == 1:
                matrix_3d = x_rotate(matrix_3d, 1)
                matrix_3d[0] = down_rotate(matrix_3d[0], 1)
                matrix_3d[1] = down_rotate(matrix_3d[1], 1)
                # 翻回去
                matrix_3d = x_rotate(matrix_3d, -1)
        if angle == 180:
            matrix_3d = x_rotate(matrix_3d, 1)
            matrix_3d[0] = down_rotate(matrix_3d[0], 1)
            matrix_3d[0] = down_rotate(matrix_3d[0], 1)
            matrix_3d[1] = down_rotate(matrix_3d[1], 1)
            matrix_3d[1] = down_rotate(matrix_3d[1], 1)
            # 翻回去
            matrix_3d = x_rotate(matrix_3d, -1)
    if position == "U":
        if angle == 90:
            if direction == -1:
                matrix_3d = y_rotate(matrix_3d, 1)
                matrix_3d = y_rotate(matrix_3d, 1)
                matrix_3d[0] = down_rotate(matrix_3d[0], -1)
                matrix_3d[1] = down_rotate(matrix_3d[1], -1)
                # 翻回去
                matrix_3d = y_rotate(matrix_3d, -1)
                matrix_3d = y_rotate(matrix_3d, -1)
            if direction == 1:
                matrix_3d = y_rotate(matrix_3d, 1)
                matrix_3d = y_rotate(matrix_3d, 1)
                matrix_3d[0] = down_rotate(matrix_3d[0], 1)
                matrix_3d[1] = down_rotate(matrix_3d[1], 1)
                # 翻回去
                matrix_3d = y_rotate(matrix_3d, -1)
                matrix_3d = y_rotate(matrix_3d, -1)
        if angle == 180:
            matrix_3d = y_rotate(matrix_3d, 1)
            matrix_3d = y_rotate(matrix_3d, 1)
            matrix_3d[0] = down_rotate(matrix_3d[0], 1)
            matrix_3d[1] = down_rotate(matrix_3d[1], 1)
            matrix_3d[0] = down_rotate(matrix_3d[0], 1)
            matrix_3d[1] = down_rotate(matrix_3d[1], 1)
            # 翻回去
            matrix_3d = y_rotate(matrix_3d, -1)
            matrix_3d = y_rotate(matrix_3d, -1)
    if position == "D":
        if angle == 90:
            if direction == -1:
                matrix_3d[0] = down_rotate(matrix_3d[0], 1)
                matrix_3d[1] = down_rotate(matrix_3d[1], 1)
            if direction == 1:
                matrix_3d[0] = down_rotate(matrix_3d[0], -1)
                matrix_3d[1] = down_rotate(matrix_3d[1], -1)
        if angle == 180:
            matrix_3d[0] = down_rotate(matrix_3d[0], -1)
            matrix_3d[1] = down_rotate(matrix_3d[1], -1)
            matrix_3d[0] = down_rotate(matrix_3d[0], -1)
            matrix_3d[1] = down_rotate(matrix_3d[1], -1)

    return matrix_3d
# rotate(matrix_3d, "R", 90, 1)
# print(matrix_3d)
move = ["U", "D", "F", "B", "L", "R", "U'", "D'", "F'", "B'", "L'", "R'", "U'2", "D'2", "F'2", "B'2", "L'2", "R'2"]
a = input("请输入旋转次数：")
lis = []
for i in range(int(a)):
    lis.append(move[random.randint(0, len(move)-1)])
    print(lis[i],end = " ")

print("\n")
for i in lis:
    if len(i) == 1:
        rotate(matrix_3d, i, 90, 1)
    elif len(i) == 2:
        rotate(matrix_3d, i[0], 90, -1)
    elif len(i) == 3:
        rotate(matrix_3d, i[0], 180, 1)
print("魔方:", matrix_3d)
re_lis = []
for i in lis:
    if len(i) == 1:
        re_lis.append(i+"'")
    elif len(i) == 2:
        re_lis.append(i[0])
    elif len(i) == 3:
        re_lis.append(i)

print("还原:")
for i in re_lis[::-1]:
    print(i, end=" ")