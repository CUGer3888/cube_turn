# 该函数功能：实现顶部 4个棱块的复原
# 返回移动步骤，start为起始位置，end为结束位置
start = [3,3,2]  # x,y,z zhongdian
end = [1,2,1]  # x,y,z qidian[1,-2,1]
def suoshu_mian(point):
    centre_point = [2, 2, 2]
    xiang_liang = [p1 - p2 for p1, p2 in zip(point, centre_point)]
    if xiang_liang == [1, 0, 1]:
        return ["F", "U"]
    if xiang_liang == [0, 1, 1]:
        return ['R', 'U']
    if xiang_liang == [-1, 0, 1]:
        return ['B', 'U']
    if xiang_liang == [0, -1, 1]:
        return ['L', 'U']
    if xiang_liang == [1, 0, -1]:
        return ['F', 'D']
    if xiang_liang == [0, 1, -1]:
        return ['R', 'D']
    if xiang_liang == [-1, 0, -1]:
        return ['B', 'D']
    if xiang_liang == [0, -1, -1]:
        return ['L', 'D']

    if xiang_liang == [1, 1, 0]:
        return ['F', 'R']
    if xiang_liang == [-1, 1, 0]:
        return ['R', 'B']
    if xiang_liang == [-1, -1, 0]:
        return ['B', 'L']
    if xiang_liang == [1, -1, 0]:
        return ['L', 'F']
turn_dir = {
"[3, 1, 2]":[2,3,1],
"[3, 3, 2]":[1,2,1],
"[1, 3, 2]":[2,1,1],
"[1, 1, 2]":[3.2,1]
}
goal_dir = {
    "[3, 3, 2]":[3,2,1],
    "[1, 3, 2]":[2,3,1],
    "[1, 1, 2]":[1,2,1],
    "[3, 1, 2]":[2,1,1]
}
def if_same(point_1, point_2):
    if point_1[2] == point_2[2]:
        return True
    else:
        return False
def gongsi_2(point):
    mian_1 ,mian_2 = suoshu_mian(point)
    move_lis=[]
    move_lis.append(["D",90,-1])
    move_lis.append([mian_2,90,-1])
    move_lis.append(["D",90,1])
    move_lis.append([mian_2,90,1])
    move_lis.append(["D",90,1])
    move_lis.append([mian_1,90,1])
    move_lis.append(["D",90,-1])
    move_lis.append([mian_1,90,-1])


    return move_lis

D_lis=[[3,2,1],[2,3,1],[1,2,1],[2,1,1]]
def move_centre(start,end):
    if if_same(start,end):
        print(gongsi_2(end))
        end = turn_dir[str(end)]
        # print(end)
        goal_index = D_lis.index(goal_dir[str(start)])
        index = D_lis.index(end)
        move_ = abs(goal_index- index)
        move_Lis = []
        for i in range(move_):
            move_Lis.append(["D", 90, -1])
        print("move",move_Lis)
        # end = goal_dir[str(start)]
        print(gongsi_2(start))
    else:
        goal_index = D_lis.index(goal_dir[str(start)])
        index = D_lis.index(end)
        move_ = abs(goal_index - index)
        move_Lis = []
        for i in range(move_):
            move_Lis.append(["D", 90, -1])
        print("move", move_Lis)
        # end = goal_dir[str(start)]
        print(gongsi_2(start))

move_centre(start,end)