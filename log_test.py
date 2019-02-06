import platform
platform.system()
platform.uname()
import os, shutil
import time, datetime
print(os.listdir())
#shutil.copytree("py_netwk","py_network_cpy")
#os.chdir("py_network_cpy")
#os.makedirs("py_network_cpy\\sample1")
#os.mkdir("sample13")
#shutil.copytree("py_network_cpy",".\\py_network_cpy_1")
#shutil.copytree("py_network_cpy",".\\py_network_cpy_2\\cpy2")

os.chdir(os.path.join(os.getcwd(), "py_network_cpy_2"))
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
#os.makedirs(r"rex\chi\chi\chi\buchi")
shutil.rmtree(r"rex\chi")

