import shutil
import os

for i in os.listdir("."):
    print(i, os.path.basename(os.path.abspath(i)), os.path.dirname(os.path.abspath(i)), sep=", ")
