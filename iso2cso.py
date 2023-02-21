import os
import time

dir_path = '.'

files =[]
dirs = []

def list_directory(_dir_path, _files):
    for path in os.listdir(_dir_path):
        fullpath = os.path.join(_dir_path, path)
        print(fullpath)
        if path[-4:].lower() == ".iso" and os.path.isfile(os.path.join(fullpath)):
            #_files.append(fullpath)
            print("compress " + fullpath)
            os.rename(fullpath,".\\temp.iso")
            os.system("ciso.exe 9 temp.iso temp.cso")
            os.rename(".\\temp.cso", fullpath[:-4] + ".cso")
            time.sleep(1)
            os.remove(".\\temp.iso")
        if os.path.isdir(fullpath):
            list_directory(fullpath, _files)


list_directory(dir_path, files)

print("files:")        
print(files)
print("directory:")
print(dirs)


