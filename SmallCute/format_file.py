"""
获取文件夹名和后缀，转化成json格式的字符串
"""



# import os
#
# path = r"C:\Users\13395\Desktop\小可爱的工作文件夹\考勤"
# file_list = os.listdir(path)
# # print(file_list)
# for file_name in file_list:
#     # print(file_name)
#     # print(file_name.split("."))
#     name = file_name.split(".")[0]
#     name1 = file_name.split(".")[1]
#     # print(name, name1)
#     print("{{'名称'：'{}', '后缀'：'{}'}}".format(name, name1))






# import os
# import shutil
#
# path = r"C:\Users\13395\Desktop\小可爱的工作文件夹\20200808考勤"
# file_list = os.listdir(path)
# print(file_list)
# for file_name in file_list:
#
#     print(type(file_name))
#     print(file_name.split("."))
#     print("这是一个{}格式的文件，名字叫{}".format(file_name.split(".")[1], file_name.split(".")[0]))





num_list = ["1", "2", "3", "4", "5", "6", "a", "b", "c", "d"]
# print(num_list[0])
# print(num_list[1])
# print(num_list[9])
# print(num_list[-2])
# print(len(num_list))
# print(num_list[3:])
# print(num_list[3:7])
# print(num_list[3:6])
# print(num_list[:6])
# print(num_list[0:9:2])

s = "".join(num_list)
print(s)
#
# print(s.split())
# print(list(s))
print(s[0])
print(s[1:5])
print(s[1:10:2])


n_list = [1, 8, 3, 7, 5, 6]
print(max(n_list))
print(min(n_list))
print(sum(n_list))
print(sorted(n_list))
print(sorted(n_list, reverse=True))
print(n_list.remove(8))
# print(n_list.remove(10))
print(n_list)

