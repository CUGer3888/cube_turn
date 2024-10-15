# 该函数功能：实现顶部 4个角块的复原
# 返回移动步骤，start为起始位置，end为结束位置
start = [3, 1, 3]  # x,y,z zhongdian
end = [1, 3, 3]  # x,y,z qidian[1,-2,1]


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


def if_same(point_1, point_2):
    if point_1[2] == point_2[2]:
        return True
    else:
        return False


def gongsi_1(point):
    mian_1, mian_2, mian_3 = suoshu_mian(point)
    lis = []
    lis.append([mian_2, 90, -1])
    lis.append([mian_3, 90, -1])
    lis.append([mian_2, 90, 1])
    lis.append([mian_3, 90, 1])
    return lis

def z_z(point):
    mian_1,mian_2 = suoshu_mian(point)[1],suoshu_mian(point)[2]
    move_lis =[]
    move_lis.append([mian_1,90,-1])
    move_lis.append([mian_2,90,-1])
    move_lis.append([mian_1,90,1])
    return move_lis

D_lis=[[3,3,1],[1,3,1],[1,1,1],[3,1,1]]
def move_U_2(start,end):
    if if_same(start,end):
        end[2] = end[2]-2
        print(gongsi_1(end))
        start[2] = start[2] - 2
        goal_index = D_lis.index(start)
        index = D_lis.index(end)
        index_ = abs(index - goal_index)
        move_Lis = []
        for i in range(index_):
            move_Lis.append(["D",90,-1])
        end = start
        print(move_Lis)
        print(z_z(end))
    else:
        start[2] = start[2]-2
        goal_index = D_lis.index(start)
        index = D_lis.index(end)
        move_Lis = []
        index = abs(index - goal_index)
        for i in range(index):
            move_Lis.append(["D", 90, -1])
        print(move_Lis)
        print(z_z(end))

move_U_2(start,end)