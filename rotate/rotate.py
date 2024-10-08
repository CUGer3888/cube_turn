import numpy as np
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
move = ["U", "D", "F", "B", "L", "R", "U'", "D'", "F'", "B'", "L'", "R'"]
def rotate(matrix_3d, position, angle, direction):
    if position == "F":
        if angle == 90:
            if direction == 2:
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
            if direction == 2:
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
            if direction == 2:
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
            if direction == 2:
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
            if direction == 2:
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
            if direction == 2:
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