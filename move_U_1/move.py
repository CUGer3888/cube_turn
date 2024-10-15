# 该函数功能：实现顶部 4个棱块的复原
# 返回移动步骤，start为起始位置，end为结束位置
start = [2,1,3]  # x,y,z zhongdian
end = [3,3,2]  # x,y,z qidian[1,-2,1]

dirction = {

}


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


# 获得旋转面
def mian(point, move):
    #移动点，坐标变化
    if 2 in move or -2 in move:
        if point[2]==1:
            return "D"
        if point[2]==3:
            return "U"

    if move[0] == 0:
        # point.x ==3
        if point[0] == 3:
            return "F"
        elif point[0] == 1:
            return "B"
        else:
            return suoshu_mian(point)[0]
    elif move[1] == 0:
        # point.y ==3
        if point[1] == 3:
            return "R"
        elif point[1] == 1:
            return "L"
        else:
            return suoshu_mian(point)[0]
    elif move[2] == 0:
        # point.z ==3
        if point[2] == 3:
            return "U"
        elif point[2] == 1:
            return "D"
        else:
            return suoshu_mian(point)[0]


# 得到旋转方向
def get_rotate(rotate, rotate_main, end):
    if rotate_main == "F":
        if end == [3, 2, 3]:
            if rotate[1] == 1:
                return (90, 1)
            elif rotate[1] == -1:
                return (90, -1)
            else:
                return (180,2)
        if end == [3, 2, 1]:
            if rotate[1] == 1:
                return (90, -1)
            elif rotate[1] == -1:
                return (90, 1)
            else:
                return (180,2)
        if end == [3, 3, 2]:
            if rotate[2] == 1:
                return (90, -1)
            elif rotate[2] == -1:
                return (90, 1)
            else:
                return (180,2)
        if end == [3, 1, 2]:
            if rotate[2] == -1:
                return (90, -1)
            elif rotate[2] == 1:
                return (90, 1)
            else:
                return (180, 2)

    if rotate_main == "R":
        if end == [2, 3, 3]:
            if rotate[0] == 1:
                return (90, -1)
            elif rotate[0] == -1:
                return (90, 1)
            else:
                return (180, 2)
        if end == [2, 3, 1]:
            if rotate[0] == 1:
                return (90, 1)
            elif rotate[0] == -1:
                return (90, -1)
            else:
                return (180, 2)
        if end == [3, 3, 2]:
            if rotate[2] == 1:
                return (90, 1)
            elif rotate[2] == -1:
                return (90, -1)
            else:
                return (180, 2)
        if end == [1, 3, 2]:
            if rotate[2] == -1:
                return (90, 1)
            elif rotate[2] == 1:
                return (90, -1)
            else:
                return (180, 2)

    if rotate_main == "U":
        if end == [3, 2, 3]:
            if rotate[1] == -1:
                return (90, 1)
            elif rotate[1] == 1:
                return (90, -1)
            else:
                return (180, 2)
        if end == [1, 2, 3]:
            if rotate[1] == -1:
                return (90, -1)
            elif rotate[1] == 1:
                return (90, 1)
            else:
                return (180, 2)

        if end == [2, 1, 3]:
            if rotate[0] == 1:
                return (90, -1)
            elif rotate[0] == -1:
                return (90, 1)
            else:
                return (180, 2)
        if end == [2, 3, 3]:
            if rotate[0] == -1:
                return (90, -1)
            elif rotate[0] == 1:
                return (90, 1)
            else:
                return (180, 2)


    if rotate_main == "B":
        if end == [1, 2, 3]:
            if rotate[1] == -1:
                return (90, 1)
            elif rotate[1] == 1:
                return (90, -1)
            else:
                return (180, 2)
        if end == [1, 2, 1]:
            if rotate[1] == 1:
                return (90, -1)
            elif rotate[1] == -1:
                return (90, 1)
            else:
                return (180, 2)
        if end == [1, 1, 2]:
            if rotate[2] == 1:
                return (90, -1)
            elif rotate[2] == -1:
                return (90, 1)
            else:
                return (180, 2)
        if end == [1, 3, 2]:
            if rotate[2] == -1:
                return (90, -1)
            elif rotate[2] == 1:
                return (90, 1)
            else:
                return (180, 2)


    if rotate_main == "L":
        if end == [2, 1, 1]:
            if rotate[0] == -1:
                return (90, 1)

            elif rotate[0] == 1:
                return (90, -1)
            else:
                return (180, 2)
        if end == [2, 1, 3]:
            if rotate[0] == 1:
                return (90, 1)
            elif rotate[0] == -1:
                return (90, -1)
            else:
                return (180, 2)
        if end == [1, 1, 2]:
            if rotate[2] == 1:
                return (90, 1)
            elif rotate[2] == -1:
                return (90, -1)
            else:
                return (180, 2)
        if end == [3, 1, 2]:
            if rotate[2] == -1:
                return (90, 1)
            elif rotate[2] == 1:
                return (90, -1)
            else:
                return (180, 2)
    if rotate_main == "D":
        if end == [2, 1, 1]:
            if rotate[0] == -1:
                return (90, -1)
            elif rotate[0] == 1:
                return (90, 1)
            else:
                return (180, 2)
        if end == [2, 3, 1]:
            if rotate[0] == -1:
                return (90, 1)
            elif rotate[0] == 1:
                return (90, -1)
            else:
                return (180, 2)
        if end == [3, 2, 1]:
            if rotate[1] == -1:
                return (90, -1)
            elif rotate[1] == 1:
                return (90, 1)
            else:
                return (180, 2)
        if end == [1, 2, 1]:
            if rotate[1] == -1:
                return (90, 1)
            elif rotate[1] == 1:
                return (90, -1)
            else:
                return (180, 2)

return_lis = []
def move_U_1(start, end):
    result = [p1 - p2 for p1, p2 in zip(start, end)]
    # print("start, result",start, result)
    rotate_main = mian(end, result)
    # print("rotate_main",rotate_main)
    # print("result:",result,"\n")
    if result.count(2) + result.count(-2)==2:
        print(suoshu_mian(end)[1],[0,0,0],(180,2),suoshu_mian(start)[0],[0,0,0],(180,2))
        return None
    if result.count(0) == 0:
        if end[2]==1:
            #分离
            lis_1 = [] #
            lis_2 = [] #end
            for i in result:
                if i==2 or i ==-2:
                    lis_2.append(i)
                    lis_1.append(0)
                else:
                    lis_1.append(i)
                    lis_2.append(0)
            #先start,后end

            temp_ = [end[ii]+ lis_1[ii] for ii in range(len(lis_1))]
            # print(lis_1,lis_2,temp_)

            move_U_1(temp_,end)
            # print("start,tmep_:",start,temp_)
            move_U_1(start,temp_)

        if end[2]==2:
            # 分离
            lis_1 = []  #
            lis_2 = []  # end
            for i in result:
                if i == 2 or i ==-2:
                    lis_1.append(i)
                    lis_2.append(0)
                else:
                    lis_2.append(i)
                    lis_1.append(0)
            # 先start,后end

            temp_ = [end[ii] + lis_1[ii] for ii in range(len(lis_1))]
            # print(lis_1, lis_2, temp_)
            move_U_1(temp_, end)
            move_U_1(start, temp_)
            move_U_1(temp_, end)
            return None

    # 解决 1 个点
    if result.count(0) == 3:
        """ ---- todo ----"""
        # 检查朝向
        return None
    # 解决 3个点
    if rotate_main == "U":
        xuanzhuan_fangxiang = get_rotate(result, rotate_main, end)
        if xuanzhuan_fangxiang[0] == 90:
            mian_1 = suoshu_mian(start)
            mian_2 = suoshu_mian(end)
            xuanzhuan_fangxiang = [mian_2[0], 90, -xuanzhuan_fangxiang[1], mian_1[0], 90, -xuanzhuan_fangxiang[1]]
        elif xuanzhuan_fangxiang[0] == 180:
            mian_1 = suoshu_mian(start)
            mian_2 = suoshu_mian(end)
            xuanzhuan_fangxiang = [mian_2[0], 180, 2, "D", 180, 2, mian_1[0], 180, 2]
        else:
            return None
    # 解决3个点
    else:
        xuanzhuan_fangxiang = get_rotate(result, rotate_main,end)
    return_lis.append([rotate_main, xuanzhuan_fangxiang])
    # print(rotate_main, result, xuanzhuan_fangxiang)
    # return rotate_main, result, xuanzhuan_fangxiang


# print(move_U_1(start, end))
move_U_1(start,end)
print(return_lis)