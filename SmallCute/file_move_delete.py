"""
找到最里层文件夹，将其内容移至外一层文件夹，并将该文件夹删除。
"""
import os
import shutil

def file_name(file_dir):
    # root当前目录路径; dirs当前路径下所有子目录
    for root, dirs, files in os.walk(file_dir):
        if len(dirs) == 1:
            # 最底层文件夹路径
            path = os.path.join(root, dirs[0])
            # 最底层文件夹下所有的文件名称
            list_ = os.listdir(path)
            for file_1 in list_:
                # 最底层文件夹文件路径
                path2 = os.path.join(path, file_1)
                # copy文件
                shutil.copy(path2, root)
            # 删除文件夹
            shutil.rmtree(path)


if __name__ == '__main__':

    file_name(r'C:\Users\13395\Desktop\小可爱的工作文件夹\20200804')
    # print(help(os))