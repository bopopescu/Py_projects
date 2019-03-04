import platform
platform.system()
platform.uname()
import os, shutil
import time, datetime
print(os.listdir(os.getcwd()))
#shutil.copytree("py_netwk","py_network_cpy")
#os.chdir("py_network_cpy")
#os.makedirs("py_network_cpy\\sample1")
#os.mkdir("sample13")
#shutil.copytree("py_network_cpy",".\\py_network_cpy_1")
#shutil.copytree("py_network_cpy",".\\py_network_cpy_2\\cpy2")
"""
def copytree(src, dst, symlinks=False, ignore=None):
    if not os.path.exists(dst):
        os.makedirs(dst)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            copytree(s, d, symlinks, ignore)
        else:
            if not os.path.exists(d) or os.stat(s).st_mtime - os.stat(d).st_mtime > 1:
                shutil.copy2(s, d)
"""
"""
#os.chdir(os.path.join(os.getcwd(), "py_network_cpy_2"))
shutil.rmtree("cpy3")
shutil.copytree("cpy2","cpy3")
print(os.getcwd())
os.chdir("..")
print(os.getcwd())
test_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
print(test_time)
os.mkdir(test_time)
shutil.copytree("py_network_cpy_2", os.path.join(test_time, "py_network_cpy_2"))
shutil.copytree("py_network_cpy_1", os.path.join(test_time, "py_network_cpy_1"))
#os.makedirs("rex\\chi\\chi\\chi\\buchi")
"""
for root, dirs, files in os.walk(os.getcwd()):
    print(root)
    print(dirs)
    print(files)
    print("*"*10)

