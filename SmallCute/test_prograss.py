"""
此py文件做测试用

"""

import json


def function1():
    a, b = 1, 2
    print(a, b)
    print("a是{}".format(a))
    print("a是{}，b是{}".format(a, b))
    a, b = b, a
    print(a, b)
    m_list = [1, 2]
    m_list[0], m_list[1] = m_list[1], m_list[0]
    print(m_list)


def func2_bubble_sort(n_list):
    """
    冒泡排序
    """
    # if n_list[0] > n_list[1]:
    #     n_list[0], n_list[1] = n_list[1], n_list[0]
    # print(n_list)
    # if n_list[1] > n_list[2]:
    #     n_list[1], n_list[2] = n_list[2], n_list[1]
    # print(n_list)
    ln = len(n_list)
    for i in range(ln):
        # print(i)
        for j in range(i + 1, ln):
            if n_list[i] > n_list[j]:
                n_list[i], n_list[j] = n_list[j], n_list[i]
    # print(n_list)
    return n_list


# 20200815  author:zhaoru
#列表去重
def func3():
    m_list = [1, 1, 2, 2, 3, 3]
    new_m_list = list(set(m_list))
    print(new_m_list)



#列表去重
def func4():
    n_list = [1, 1, 2, 2, 3]
    new_n_list = []
    for i in n_list:
        if i not in new_n_list:
            new_n_list.append(i)
    print(new_n_list)



def func5():
    # for i in range(5, 11):
    #     print(i)
    # for i in range(20, 40, 3):
    #     print(i)
    # h_list = []
    # for i in range(40, 20, -4):
    #     # print(i)
    #     h_list.append(i)
    # # print(h_list)

    # 列表删除元素的两种方法（remove元素值，pop索引值）
    # h_list.remove(h_list[2])
    # h_list.pop(2)
    # print(h_list)

    # 列表生成式
    m_list = [i for i in range(40, 80) if i % 2 == 1]
    print(m_list)


#水仙花
def func6():
    for i in range(100, 1000):
        a = i // 100
        b = i % 100 //10
        c = i % 10
        if i == pow(a, 3) + pow(b, 3) + pow(c, 3):
            # print(i)
            pass
    print(i)


#
def func7():
    d = {"name":"小明", "age":"6", "height":"160cm", "weight":"68KG"}
    print(type(d))
    json_d = json.dumps(d)
    print(type(json_d))
    print(json_d)
    print(d)
    d2 = json.loads(json_d)
    print(type(d2))
    print(d2)


#20200816
#位置传参
def func8(a, b):
    # c = a + b
    # return c
    print(a, b)
    return a + b


def func9(a, b, c):
    return a * b * c


def qiantao_if_else(i, owncar=False, ownhouse=False):
    if i > 5000:
        print("银行借钱给他1")
    else:
        if owncar is True:
            print("银行借钱给他2")
        else:
            if ownhouse is True:
                print("银行借钱给他3")
            else:
                print("银行说你走吧，没钱！")



#20200817
#如果今天不下雨，再如果今天温度小于三十度，就带亲爱的出去玩儿，
#如果今天不下雨，温度超过三十度，就不带亲爱的出去玩儿，太热了
#如果今天下雨，你就在家待着吧
def func8(rain, T):
    if rain is True:
        print("你就在家待着吧！")
        return False
    else:
        if T < 30:
            print("带亲爱的出去嗨皮！")
            return True
        else:
            print("不带亲爱的出去玩儿，太热了。")
            return False



#for嵌套
def qiantao_for():
    for i in range(1, 9):
        print()
        for j in range(1, 9):
            # m = i * j
            # print(i , "*" , j ,  "=", i * j)
            print("{}*{} = {}\t".format(i, j, i*j), end=" ")


def qiantao_for1():
    for i in range(1, 9):
        print()
        for j in range(1, i + 1):
            # m = i * j
            # print(i , "*" , j ,  "=", i * j)
            print("{}*{} = {}\t".format(i, j, i*j), end=" ")



def qiantao_for2():
    for i in range(1, 9):
        print()
        for j in range(i, 9):
            # m = i * j
            # print(i , "*" , j ,  "=", i * j)
            print("{}*{} = {}".format(i, j, i*j), "\t",  end="")



#20200819
def calc_list(n):
    for i in n:
        # print(isinstance(i, int))  #判断元素的数据类型是否为int
        # print(isinstance(i, str))  #判断元素的数据类型是否为str
        # print(str(i).isdigit())    #判断元素的数据类型是否为整数
        # print(str(i).isalpha())    #判断元素的数据类型是否为字母
        # print(type(i))
        # print(i)
        if isinstance(i, str):
            print(i)
            # pass
        else:
            if isinstance(i, int):
                print(i)
                # pass
                if i % 2 == 0:
                    print("{}是个偶数".format(i))
                else:
                    print("{}是个奇数".format(i))





def calc_max_sum(m):
    a = func2_bubble_sort(m)
    print(a)
    b = sum(a[-1:-3:-1])
    print(b)


def calc_adj_max_sum(l):
    p_list = []
    for i in range(len(l)-1):
        a = l[i] + l[i + 1]
        p_list.append(a)
    print(p_list)
    mm = func2_bubble_sort(p_list)
    print(mm)
    c = max(p_list)
    print(c)



def calc_sum():
    s = {4, 6, 96, 455}
    # s = {"a", "d", "6", "x"}   #不能用
    print(sum(s))



def calc__list_qiepian():
    s = m_list[5:11]
    print(s)
    j = m_list[3:13:3]
    print(j)
    k = m_list[-2:-15:-2]
    print(k)


#eval函数
def calc_eval():
    a = "sum([1, 2, 3, 8, 9, 82])"
    b = eval(a)
    print(b)
    print(type(b))
    c = "1 + 2"
    d = eval(c)
    print(d)
    x = 13
    y = 15
    z = eval("pow((x + y) / 2, 2)")
    print(z)
    j = [1, 5, 7 ,8, 9, 18, 16, 12]
    f = func2_bubble_sort(j)
    print(f)
    print(eval("func2_bubble_sort(j)"))



#pass continue
def suibian(n):
    for i in n:
        if i % 2 == 1:
            pass
            # continue
        print(i)
        # else:
        #     pass




def func10(n):
    for i in n:
        if i % 3 == 0:
            pass




#元组
def calc_tuple():
    l = [1, 2, 3]
    tup1 = ("physics", "chemistry", 1997, 2000)
    tup2 = (1, 2, 3, 4, 5)
    tup3 = "a", "b", "c", "d"
    print(tup1[0])
    print(tup2[1:5:2])
    tup4 = tup1 + tup2 + tup3
    print(tup4)
    # del tup4
    # print(tup4)
    print("abc", -45556, 18+6.6j, "xyz")
    x, y = 1, 2
    print("Value of x , y : ", x,y)
    print(max(tup2))
    print(min(tup2))
    print(tuple(l))


#字典
def calc_dict():
    d = {"Alice": "2341", "Beth": "9102", "Cecil": "3258"}
    print(d)
    d["Beth"] = "9244"
    d["ss"] = "54616"
    print(d)
    print(d["Beth"])
    print(d["Cecil"])
    del d["Cecil"]  # 删除键是'Cecil'的条目
    print(d)
    # d.clear()  # 清空词典所有条目
    # print(d)
    # del d # 删除词典
    # print(d)
    print(len(d))  # 计算字典元素个数，即键的总数。
    print(str(d))  # 输出字典可打印的字符串表示。













if __name__ == '__main__':
    # function1()
    m_list = [7, 35, 95, 895, 59, 78, 63, 1414, 25252, 6.9, 7878, 6969, 4545, 9696, 3636, 15151, 6, 5, 4, 89]
    # n_list = [7, 35, 95, 895, 59, 78, 63, 1414, 25252, 6.9, 7878, 6969, 4545, 9696, 3636, 15151, 6, 5, 4, 89, "A", "B", "NHKSJHK"]
    # func2_bubble_sort(n_list)
    # func3()
    # func4()
    # func5()
    # print(pow(3, 3))
    # func6()
    # func7()
    # print(func8(2, 3))
    # a = func9(5, 6, 6)
    # print(a)
    # qiantao_if_else(3000, False, True)
    # print(func8(False, 31))
    # qiantao_for()
    # qiantao_for1()
    # qiantao_for2()
    # calc_list(n_list)
    # calc_max_sum(m_list)
    # calc_adj_max_sum(m_list)
    # calc_sum()
    # calc__list_qiepian()
    # calc_eval()
    # suibian(m_list)
    # calc_tuple()
    calc_dict()
