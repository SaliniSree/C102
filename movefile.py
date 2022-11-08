import os
import shutil

#move file
source = 'C:/Users/salin/OneDrive/Desktop/AaMyPc/codingclasses/aPython/Python/Downloads'
destination = 'C:/Users/salin/OneDrive/Desktop/AaMyPc/codingclasses/aPython/Python/Movedfiles'
list1 = os.listdir(source)
#print(list1)

for file_name in list1:

    name, extension = os.path.splitext(file_name)
   # print(name)
   # print(extension)


    if extension == '':
        continue
    if extension in ['.png', '.jpg']:
        path1 = source + '/' + file_name                             
        path2 = destination + '/' + "Image_Files"                          
        path3 = destination + '/' + "Image_Files" + '/' + file_name   


    if os.path.exists(path2):
        print("Moving " + file_name + ".....")

          # Move from path1 ---> path3
        shutil.move(path1, path3)

    else:
        os.makedirs(path2)
        print("Moving " + file_name + ".....")
        shutil.move(path1, path3)

