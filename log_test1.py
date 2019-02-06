import subprocess
from subprocess import PIPE
cmd_list = ["python","proc_data_1.py"]
p=subprocess.Popen(cmd_list, stdout=PIPE, stderr=PIPE, shell=True)
stdout = p.stdout.read()
if stdout:
    pass
    print(stdout)





