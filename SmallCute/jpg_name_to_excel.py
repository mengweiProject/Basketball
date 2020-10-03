
import os
import xlrd
import xlwt


dt_excel = xlwt.Workbook()
dt_sheet = dt_excel.add_sheet("Sheet1")
myStyle = xlwt.easyxf('font: name Times New Roman, color-index red, bold on', num_format_str='#,##0.00')   #数据格式


path = r"C:\Users\13395\Desktop\小可爱的工作文件夹\20200808考勤"
file_list = os.listdir(path)
for root, dirs, files in os.walk(path):
    # print(len(files))
    for name in files:
        info_list = str(os.path.join(root, name).split("\\"))
        for info in info_list:
            try:
                # print(files.index(name), info_list.index(info), info)
                dt_sheet.write(files.index(name), info_list.index(info), 123456)
            except:
                pass



# dt_sheet.write(i, j, 1234.56, myStyle)

# dt_sheet.write(2, 0, 1)                          #写入A3，数值等于1
#
# dt_sheet.write(2, 1, 1)                          #写入B3，数值等于1

# dt_sheet.write(2, 2, xlwt.Formula("A3+B3"))      #写入C3，数值等于2（A3+B3）

dt_excel.save(r"C:\Users\13395\Desktop\小可爱的工作文件夹\20200808考勤\png_folder_folder\demo3.xls")
