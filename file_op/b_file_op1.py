from shutil import copyfile, copy2, copytree, rmtree, copy
import shutil
import os

if "logs" in os.listdir(os.getcwd()):
    shutil.rmtree("logs")
cur_dir = os.getcwd() + "\logs" # <class 'str'>
ss = os.path.basename(cur_dir)
src_filename = os.path.abspath("__file__")
dst_filename = src_filename +"_cpy.txt"
#print(src_filename, '\n',dst_filename)
#copyfile(src_filename, dst_filename) #dst must be file name

#copy2(src_file, dst_dir) # dst1 can be file name or directory name, src_file can't be dir.
dst_dirname  = "\\".join([os.getcwd(), "logs", "copy4_folder"])
#copy2(src_filename,dst_dirname)
#  dst_dirname must exist
#  src is single file

#
#
#copy() copies the file data and the file’s permission mode (see os.chmod()).
#Other metadata, like the file’s creation and modification times, is not preserved.
#To preserve all file metadata from the original, use copy2() instead

src_dir = "\\".join([os.getcwd(),"logs","copy_folder"])
#src_dir = os.path.join(os.getcwd(), "logs", "copy_folder")
dst_dir = "\\".join([os.getcwd(), "logs", "cptree"])
if os.path.isdir(dst_dir):
    print("dst_dir exists, and need to be rmoved")
    rmtree(dst_dir)
#dst_dir can't exist
copytree(src_dir, dst_dir)

#src_files = os.listdir(src)
#for file_name in src_files:
#    full_file_name = os.path.join(src, file_name)
#    if (os.path.isfile(full_file_name)):
#        shutil.copy(full_file_name, dest)

#os.listdir(os.getcwd())
#['.git', '.idea', 'file_op']
#os.chdir(os.path.join(os.getcwd(),'file_op'))
#os.path.splitext(file_path)
dst = "temp"
srcfile = os.listdir(os.getcwd())
for file in srcfile:
    if os.path.isfile(file):
        copyfile(file, dst)

def recursive_copy_files(source_path, destination_path, override=False):

    files_count = 0
    if not os.path.exists(destination_path):
        os.mkdir(destination_path)
    items = glob.glob(source_path + '/*')
    for item in items:
        if os.path.isdir(item):
            path = os.path.join(destination_path, item.split('/')[-1])
            files_count += recursive_copy_files(source_path=item, destination_path=path, override=override)
        else:
            file = os.path.join(destination_path, item.split('/')[-1])
            if not os.path.exists(file) or override:
                shutil.copyfile(item, file)
                files_count += 1
    return files_count

#
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

