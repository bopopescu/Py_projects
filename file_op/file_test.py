import shutil
import os

print(os.getcwd())
#os.remove("write_log.txt")
#src = os.path.join(os.getcwd(), "zip_op", "write_log.txt")
#src = r".\zip_op\wriet_log.txt"
#src = os.path.join( "zip_op", "write_log.txt")
#src = "zip_op\\write_log.txt"
src = ".\zip_op\write_log.txt"
#des = "."
des = "write_log.txt"
shutil.copy2(src, des)
