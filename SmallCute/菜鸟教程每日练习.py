from Helper.Tools import myprint, pi, map_s, calc_run_time
import cmath
import math
import random



def func1():
    """
    显示颜色的格式：
    \033 [显示方式;前景色;背景色m … [\ 033 [0m]
    注：’;'前后的三个参数：显示方式，前景色，背景色是可选参数，可以只写其中的某一个或者某两个；由于表示三个参数不同含义的数值都是唯一没有重复的，所以三个参数的书写先后顺序没有固定要求，系统都可识别；
    建议按照默认的格式规范书写

    显示方式  	效果	          前景色	     背景色	      颜色描述
    0	        终端默认设置	        30	        40	        黑色
    1	        高亮显示	            31	        41	        红色
    4	        使用下划线	        32	        42	        绿色
    5	        闪烁	            33	        43	        黄色
    7	        反白显示	            34	        44	        蓝色
    8	        不可见	            35	        45	        紫红色
    22	        非高亮显示	        36	        46	        青蓝色
    24	        去下划线	            37	        47	        白色
    25	        去闪烁
    27	        非反白显示
    28	        可见
    """
    print("\33[0;33;46m hello,world \33[0m!!!")




def func2():
    """
    通过用户输入两个数字，并计算两个数字之和：
    :return:
    """
    num1 = input("请输入第一个数字：")
    num2 = input("请输入第二个数字：")
    myprint(type(num1))
    myprint(type(num2))
    sum = float(num1) + float(num2)
    print("数字{0}和{1}相加结果为{2}".format(num1, num2, sum))


def func3():
    """
    数字的平方根
    :return:
    """
    num = float(input("请输入一个数："))
    num_sqrt = num ** 0.5
    print("{0}的平方根为{1}".format(num, num_sqrt))


def func4(a, b, c):
    """
    # 二次方程式 ax**2 + bx + c = 0
    # a、b、c 用户提供，为实数，a ≠ 0
    :param a:
    :param b:
    :param c:
    :return:
    """
    d = (b ** 2) - (4 * a * c)
    sol1 = (-b - cmath.sqrt(d)) / (2 * a)
    sol2 = (-b + cmath.sqrt(d)) / (2 * a)
    myprint('结果为 {0} 和 {1}'.format(sol1,sol2))


def func5(a, b, c):
    """
    输入三角形三边长度，并计算三角形的面积：
    :return:
    """
    if a + b > c and a + c > b and b + c > a:
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        myprint(area)
    else:
        myprint("这不是个三角形")



def func6(a):
    """
    圆的面积公式为 ：S=Pi * r ** 2
    公式中 r 为圆的半径
    :param a:
    :return:
    """
    if isinstance(a, int) and a > 0 or isinstance(a, float) and a > 0:
        myprint(pi * a ** 2)
    # elif isinstance(a, float) and a > 0:
    #     myprint(pi * a ** 2)
    else:
        myprint("你打错啦哈哈哈哈哈")



def func7():
    """
    生成一个随机数
    :return:
    """
    myprint(random.randint(0, 9))
    myprint(map_s.upper())
    # print(map_s.upper()[random.randint(0, 25)] + map_s.upper()[random.randint(0, 25)] + map_s.upper()[random.randint(0, 25)])
    print((map_s[random.randint(0, 25)] + map_s[random.randint(0, 25)] + map_s[random.randint(0, 25)]).upper())


@calc_run_time
def func8():
    s = ""
    for _ in range(3000000):
        s += map_s[random.randint(0, 25)]
    print(s.upper()[random.randint(0, 25)] + s.upper()[random.randint(0, 25)] + s.upper()[random.randint(0, 25)])


@calc_run_time
def func9():
    s = ""
    for _ in range(3000000):
        s += map_s[random.randint(0, 25)]
    print((s[random.randint(0, 25)] + s[random.randint(0, 25)] + s[random.randint(0, 25)]).upper())








if __name__ == '__main__':
    # func1()
    # myprint("hello,world")
    # func2()
    # func3()
    # func4(1, -6, 5)
    # func5(3, 2, 1)
    # func6("abc")
    func8()
    func9()
