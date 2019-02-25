import os
import os.path
import subprocess
import distutils.core
import time
import shutil


PACKAGE_NAME = "asdf.zip"
top_dir = os.path.dirname(os.path.realpath(__file__))
curr_time = time.strftime("%d_%m_%Y")

report_name = os.path.splitext(PACKAGE_NAME)[0] + '_' + curr_time + '.pdf'
rel_path = "../Results"
report_name = os.path.join(rel_path, report_name)
print report_name
print top_dir

