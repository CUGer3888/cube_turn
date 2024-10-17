"""
goal : 实现底部4个角的还原
"""
start = [3, 3, 2]  # x,y,z zhongdian
end = [1, 2, 1]  # x,y,z qidian[1,-2,1]


# " "
def suoshu_mian(point):
    centre_point = [2, 2, 2]
    xiang_liang = [p1 - p2 for p1, p2 in zip(point, centre_point)]
    if xiang_liang == [1, 1, 1]:
        return ["F", "R", "U"]
    if xiang_liang == [-1, 1, 1]:
        return ['R', 'B', 'U']
    if xiang_liang == [-1, -1, 1]:
        return ['B', 'L', 'U']
    if xiang_liang == [1, -1, 1]:
        return ['L', 'F', 'U']
    if xiang_liang == [1, 1, -1]:
        return ['F', 'R', 'D']
    if xiang_liang == [-1, 1, -1]:
        return ['R', 'B', 'D']
    if xiang_liang == [-1, -1, -1]:
        return ['B', 'L', 'D']
    if xiang_liang == [1, -1, -1]:
        return ['L', 'F', 'D']


def gongsi_4(point):
    mian_1, mian_2, mian_3 = suoshu_mian(point)
    lis = []
    lis.append([mian_2, 90, -1])
    lis.append([mian_3, 90, -1])
    lis.append([mian_2, 90, 1])
    lis.append([mian_3, 90, 1])
    return lis


def move_D_2(points):
    biaozun = [0,1,2,3]
    # eg = [1,3,0,3]

    start = matirx[3][3][3]
    first = points[0]
    gongsi_4([3,3,1])
    if first ==0:
        pass
    if first ==1:
        print(["D",90,1])
        if chaoxiang and point_is_ok:
            pass
        else:
            gongsi_4([3,3,1])
    if first ==2:
        print(["D",180,2])
        if chaoxiang and point_is_ok:
            pass
        else:
            gongsi_4([3,3,1])
    if first ==4:
        print(["D",90,-1])
        if chaoxiang and point_is_ok:
            pass
        else:
            gongsi_4([3,3,1])
    #backword

    point = matrix[3][3][3]
    if point ==0:
        if chaoxiang and point_is_ok:
            pass
        else:
            gongsi_4([3, 3, 1])
    if point == 1:
        print(["D", 90, 1])
        if chaoxiang and point_is_ok:
            pass
        else:
            gongsi_4([3, 3, 1])
    if point == 2:
        print(["D", 180, 2])
        if chaoxiang and point_is_ok:
            pass
        else:
            gongsi_4([3, 3, 1])
    if point == 3:
        print(["D", 90, -1])
        if chaoxiang and point_is_ok:
            pass
        else:
            gongsi_4([3, 3, 1])
    # backword



    start = matrix[3][1][3]
    if point == start:
        first = points[1]
        gongsi_4([1,3,1])
        if first == 0:
            pass
        if first == 1:
            print(["D", 90, 1])
            if chaoxiang and point_is_ok:
                pass
            else:
                gongsi_4([1,3,1])
        if first == 2:
            print(["D", 180, 2])
            if chaoxiang and point_is_ok:
                pass
            else:
                gongsi_4([1,3,1])
        if first == 4:
            print(["D", 90, -1])
            if chaoxiang and point_is_ok:
                pass
            else:
                gongsi_4([1,3,1])
        # backword

        point = matrix[3][3][3]
        if point == 0:
            if chaoxiang and point_is_ok:
                pass
            else:
                gongsi_4([1,3,1])
        if point == 1:
            print(["D", 90, 1])
            if chaoxiang and point_is_ok:
                pass
            else:
                gongsi_4([1,3,1])
        if point == 2:
            print(["D", 180, 2])
            if chaoxiang and point_is_ok:
                pass
            else:
                gongsi_4([1,3,1])
        if point == 3:
            print(["D", 90, -1])
            if chaoxiang and point_is_ok:
                pass
            else:
                gongsi_4([1,3,1])
        # backword

        if point == start:
            print(["D", 90, -1])
            if chaoxiang and point_is_ok:
                pass
            else:
                gongsi_4([1,3,1])




    start = matrix[3][1][1]
    if point == start:
        first = points[1]
        gongsi_4([1,1,1])
        if first == 0:
            pass
        if first == 1:
            print(["D", 90, 1])
            if chaoxiang and point_is_ok:
                pass
            else:
                gongsi_4([1,1,1])
        if first == 2:
            print(["D", 180, 2])
            if chaoxiang and point_is_ok:
                pass
            else:
                gongsi_4([1,1,1])
        if first == 4:
            print(["D", 90, -1])
            if chaoxiang and point_is_ok:
                pass
            else:
                gongsi_4([1,1,1])
        # backword

        point = matrix[3][3][3]
        if point == 0:
            if chaoxiang and point_is_ok:
                pass
            else:
                gongsi_4([1,1,1])
        if point == 1:
            print(["D", 90, 1])
            if chaoxiang and point_is_ok:
                pass
            else:
                gongsi_4([1,1,1])
        if point == 2:
            print(["D", 180, 2])
            if chaoxiang and point_is_ok:
                pass
            else:
                gongsi_4([1,1,1])
        if point == 3:
            print(["D", 90, -1])
            if chaoxiang and point_is_ok:
                pass
            else:
                gongsi_4([1,1,1])
        # backword

        if point == start:
            print(["D", 90, -1])
            if chaoxiang and point_is_ok:
                pass
            else:
                gongsi_4([1,1,1])




    start = matrix[3][3][1]
    if point == start:
        first = points[1]
        gongsi_4([3,1,1])
        if first == 0:
            pass
        if first == 1:
            print(["D", 90, 1])
            if chaoxiang and point_is_ok:
                pass
            else:
                gongsi_4([3,1,1])
        if first == 2:
            print(["D", 180, 2])
            if chaoxiang and point_is_ok:
                pass
            else:
                gongsi_4([3,1,1])
        if first == 4:
            print(["D", 90, -1])
            if chaoxiang and point_is_ok:
                pass
            else:
                gongsi_4([3,1,1])
        # backword

        point = matrix[3][3][3]
        if point == 0:
            if chaoxiang and point_is_ok:
                pass
            else:
                gongsi_4([3,1,1])
        if point == 1:
            print(["D", 90, 1])
            if chaoxiang and point_is_ok:
                pass
            else:
                gongsi_4([3,1,1])
        if point == 2:
            print(["D", 180, 2])
            if chaoxiang and point_is_ok:
                pass
            else:
                gongsi_4([3,1,1])
        if point == 3:
            print(["D", 90, -1])
            if chaoxiang and point_is_ok:
                pass
            else:
                gongsi_4([3,1,1])
        # backword

        if point == start:
            print(["D", 90, -1])
            if chaoxiang and point_is_ok:
                pass
            else:
                gongsi_4([3,1,1])