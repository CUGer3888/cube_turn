def get_projection(matrix_3d):
    sum_1 = matrix_3d[1][1][1] + matrix_3d[1][2][1] + matrix_3d[1][3][1]
    sum_2 = matrix_3d[1][1][2] + matrix_3d[1][2][2] + matrix_3d[1][3][2]
    sum_3 = matrix_3d[1][1][3] + matrix_3d[1][2][3] + matrix_3d[1][3][3]
    sum_4 = matrix_3d[2][1][1] + matrix_3d[2][2][1] + matrix_3d[2][3][1]
    sum_5 = matrix_3d[2][1][2] + matrix_3d[2][2][2] + matrix_3d[2][3][2]
    sum_6 = matrix_3d[2][1][3] + matrix_3d[2][2][3] + matrix_3d[2][3][3]
    sum_7 = matrix_3d[3][1][1] + matrix_3d[3][2][1] + matrix_3d[3][3][1]
    sum_8 = matrix_3d[3][1][2] + matrix_3d[3][2][2] + matrix_3d[3][3][2]
    sum_9 = matrix_3d[3][1][3] + matrix_3d[3][2][3] + matrix_3d[3][3][3]
    sum_str = str(sum_1) + str(sum_2) + str(sum_3) + str(sum_4) + str(sum_5) + str(sum_6) + str(sum_7) + str(sum_8) + str(sum_9)
    return sum_str