def get_surface(matrix_3d):
    lis = []
    # 第一层所有
    for i in range(5):
        for j in range(5):
            lis.append(matrix_3d[0][i][j])
    # 第二层边缘
    for i in range(5):
        for j in range(5):
            if i == 0 or i == 4 or j == 0 or j == 4:
                lis.append(matrix_3d[1][i][j])
    # 第三层边缘
    for i in range(5):
        for j in range(5):
            if i == 0 or i == 4 or j == 0 or j == 4:
                lis.append(matrix_3d[2][i][j])
    # 第四层边缘
    for i in range(5):
        for j in range(5):
            if i == 0 or i == 4 or j == 0 or j == 4:
                lis.append(matrix_3d[3][i][j])
    # 第五层所有
    for i in range(5):
        for j in range(5):
            lis.append(matrix_3d[4][i][j])
    return lis