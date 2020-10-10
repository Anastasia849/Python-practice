import os


def createDir():
    if os.path.isdir("os_task"):
        os.chdir("os_task")
        dir = {"os_task": os.listdir()}
        for i1 in os.listdir():
            if os.path.isdir(i1):
                os.chdir(i1)
                if os.listdir():
                    for i2 in range(len(dir["os_task"])):
                        if i1 == dir["os_task"][i2]:
                            dir["os_task"][i2] = {i1: os.listdir()}
                            for i3 in os.listdir():
                                if os.path.isdir(i3):
                                    os.chdir(i3)
                                    for i4 in range(len(dir["os_task"][i2])):
                                        if i3 == dir["os_task"][i2][i1][i4]:
                                            dir["os_task"][i2][i1][i4] = {i3: os.listdir()}
                                            for i5 in os.listdir():
                                                if os.path.isdir(i5):
                                                    os.chdir(i5)
                                                    for i6 in range(len(dir["os_task"][i2][i1][i4][i3])):
                                                        if i5 == dir["os_task"][i2][i1][i4][i3][i6]:
                                                            if os.listdir():
                                                                dir["os_task"][i2][i1][i4][i3][i6] = {i5: os.listdir()}
                                                            else:
                                                                dir["os_task"][i2][i1][i4][i3][i6] = {i5: None}
                                                    os.chdir("..")
                                            if len(dir["os_task"][i2][i1]) == 1:
                                                dir["os_task"][i2] = {i1: dir["os_task"][i2][i1][i4]}
                                    os.chdir("..")
                    os.chdir("..")
        os.chdir("..")
    return dir


def createFoldersAndFiles(dir1):
    for i in dir1.keys():
        if not os.path.isdir(i):
            os.mkdir(i)
            os.chdir(i)
            for j1 in dir1.get(i):
                for j2 in j1.keys():
                    if not os.path.isdir(j2):
                        os.mkdir(j2)
                        os.chdir(j2)
                        for j3 in j1.get(j2):
                            for j4 in j3.keys():
                                if not os.path.isdir(j4):
                                    os.mkdir(j4)
                                    os.chdir(j4)
                                    file = open(j3.get(j4), "w")
                                    file.write(os.path.abspath(os.getcwd()))
                                    file.close()
                                    os.chdir("..")
                        os.chdir("..")
            os.chdir("..")


dir1 = {"Учёба": [
    {"1семестр": [{"Физика": "file.txt"}, {"Программирование": "file.txt"}, {"Алгебра и АГ": "file.txt"},
                  {"История": "file.txt"}]}, {
        "2семестр": [{"Физика": "file.txt"}, {"Программирование": "file.txt"}, {"Матанализ": "file.txt"},
                     {"Право": "file.txt"}]}]}

print(createDir())
