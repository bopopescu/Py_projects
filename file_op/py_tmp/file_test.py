from glob import glob
import os
schfile = os.path.join(os.getcwd(),"**","*.txt")
a = glob(schfile,recursive=True)
for i in a:
    print(i)