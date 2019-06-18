import os
rst = os.system("dir *.csv")
#print(type(rst))
print(type(os.popen("dir").read))

import subprocess
#Keep in mind that sys.exit(), exit(), quit(), and os._exit(0) kill the Python interpreter.
subprocess.run("python --version")
#response = subprocess.run(["dir", '*.py'], shell=True)
#print(response)
#subprocess.run("dir",shell=True)
#subprocess.call(["dir","*.py"],shell=True)

import glob
print(glob.glob("*.csv"))
