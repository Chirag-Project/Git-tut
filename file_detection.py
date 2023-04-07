import os
import shutil

path = "C:\\Users\\ḥr̥\\Desktop\\"
if os.path.exists(path):
    path2="C:\\Users\\ḥr̥\\Desktop\\Hello"
    print("Path exists")
    os.mkdir(path2)

    # choice = input("Enter your choice: ")
    # if os.path.isfile(path) and choice == 'f':
    #     os.remove(path)
    # elif os.path.isdir(path) and choice == 'd':
    #     os.rmdir(path)
    # shutil.rmtree(path)
    # os.rmdir(path)
else:
    print("Path doesn't exists")