import os
import shutil
#print(dir(os))
#os.getcwd()
#os.mkdir('C102')
#os.listdir()


#splittext
#path1 = 'Downloads/img1.png'
#root,extension = os.path.splitext(path1)
#print('Root of file is : ', root)
#print('Type of file is : ',extension)


#copy file
source = 'C:/Users/salin/OneDrive/Desktop/AaMyPc/codingclasses/aPython/Python/Downloads/img1.png'
destination = 'C:/Users/salin/OneDrive/Desktop/AaMyPc/codingclasses/aPython/Python/Downloads/copyimg.png'
dest = shutil.copy(source,destination)
print(dest)


