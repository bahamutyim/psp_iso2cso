import os
import time

dir_path = '.'



def list_directory(_dir_path):
    for path in os.listdir(_dir_path):
        fullpath = os.path.join(_dir_path, path)
        #print(fullpath)
        if path[-4:].lower() == ".iso" and os.path.isfile(os.path.join(fullpath)):
            print("compress " + fullpath)
            os.rename(fullpath,".\\temp.iso")
            os.system("ciso.exe 9 temp.iso temp.cso")
            os.rename(".\\temp.cso", fullpath[:-4] + ".cso")
            time.sleep(1)
            os.remove(".\\temp.iso")
        if os.path.isdir(fullpath):
            list_directory(fullpath)


list_directory(dir_path)



