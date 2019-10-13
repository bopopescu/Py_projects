from shutil import copyfile, copy2
import os
import shutil
#from pathlib import Path
#logoutput
#log1


#______________________________________________________________
In[46]: shutil.copy2("admin.py", "migrations")
Out[46]: 'migrations\\admin.py'

In[48]: os.remove(r"migrations\admin.py")

In[51]: shutil.copytree(".", "migrations1")
Out[51]: 'migrations1'  # create a new folder "migrations1" if it doesn't exist.
# Error if "migrations1" exists

In[57]: if os.path.isdir("migrations1"):
    ...:     shutil.rmtree("migrations1")
    ...: print("done removing migrations1")
    ...: shutil.copytree("migrations", "migrations1")
done removing migrations1
Out[57]: 'migrations1'
#______________________________________________________________
cur_dir = os.chdir("logoutput")

