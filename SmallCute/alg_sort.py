

"""
九(八)大排序算法，分别是冒泡排序，插入排序，选择排序，希尔排序，归并排序，快速排序，堆排序,计数排序
"""


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



def