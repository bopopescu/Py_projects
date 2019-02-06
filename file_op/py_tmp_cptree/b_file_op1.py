from shutil import copyfile, copy2, copytree, rmtree,copy
import os

cur_dir = os.getcwd() + "\logs"#<class 'str'>
print(cur_dir)
src_filename = "\\".join([cur_dir,"mumu_rxrx.txt"])
dst_filename = src_filename.split('.')[0]+"_cpy.txt"
#print(src_filename, '\n',dst_filename)
copyfile(src_filename, dst_filename) #dst must be file name

#copy2(src_file, dst_dir) # dst1 can be file name or directory name, src_file can't be dir.
dst_dirname  = "\\".join([os.getcwd(), "logs", "copy4_folder"])
#copy2(src_filename,dst_dirname)
#  dst_dirname must exist
#  src is single file


#
#copy() copies the file data and the file’s permission mode (see os.chmod()).
#Other metadata, like the file’s creation and modification times, is not preserved.
#To preserve all file metadata from the original, use copy2() instead

src_dir = "\\".join([os.getcwd(),"logs","copy_folder"])
dst_dir = "\\".join([os.getcwd(),"logs","cptree"])
if os.path.isdir(dst_dir):
    print("dst_dir exists, and need to be rmoved")
    rmtree(dst_dir)
#dst_dir can't exist
copytree(src_dir,dst_dir)

#src_files = os.listdir(src)
#for file_name in src_files:
#    full_file_name = os.path.join(src, file_name)
#    if (os.path.isfile(full_file_name)):
#        shutil.copy(full_file_name, dest)

#os.listdir(os.getcwd())
#['.git', '.idea', 'file_op']
#os.chdir(os.path.join(os.getcwd(),'file_op'))

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