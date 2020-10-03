"""
文件复制:
已知一个文件夹中有jpg、json、txt等类型的文件,
在此文件夹中按照文件类型新建分类文件夹，如：jpg_folder、json_folder、txt_folder，
将各个类型的文件复制到对应的新建文件夹中，原文件不删除。
"""


import os
import shutil



def file_copy_to_target(path):
    # folder_list = ["jpg_folder", "json_folder"]
    folder_list = []
    #获取文件的名称列表
    file_list = os.listdir(path)
    for file_name in file_list:
        # print(file_name)
        #split分割字符串名称并反馈列表结果
        print(file_name.split(".")[-1] + "_folder")
        #判断元素一个字符串是都在另一个字符串里
        if (file_name.split(".")[-1] + "_folder") not in folder_list:
            #在列表最后添加元素
            folder_list.append(file_name.split(".")[-1] + "_folder")
    print(folder_list)
    for i in folder_list:
        #判断文件夹是否已经存在
        if os.path.exists(os.path.join(path,i)) is False:
            #新建文件夹
            os.mkdir(os.path.join(path,i))

    #获取文件名称列表
    file_list = os.listdir(path)
    print(file_list)
    filetype_list = []
    for file_name in file_list:
        print("." + file_name.split(".")[-1])
        if "folder" not in file_name and ("." + file_name.split(".")[-1]) not in filetype_list:
            filetype_list.append("." + file_name.split(".")[-1])
    print(filetype_list)
    # print("abc" in "abcd")
    # print("abd" in "abcd")
    for file_name in file_list:
        for filetype in filetype_list:
            if filetype in file_name:
                #复制文件
                shutil.copy(os.path.join(path, file_name), os.path.join(path, "{}_folder".format(filetype[1:])))
                print(file_name + "------这是一个{}".format(filetype[1:]))

if __name__ == '__main__':
    path = r"C:\Users\13395\Desktop\小可爱的工作文件夹\20200808考勤"
    file_copy_to_target(path)