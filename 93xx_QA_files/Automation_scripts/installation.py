import os
import subprocess
import shutil
import os.path
import mysql.connector
import copy
import zipfile
import glob
import sys
import time

count = 0
command = "Automation_Setup_installer.au3 "
try:
	for a in range(1000):
		count = count + 1;
		print count, "\n";
		#p = subprocess.Popen ( command, shell=True, stdout=subprocess.PIPE )
		os.system("Automation_Setup_installer.au3")
		time.sleep(5)
except:
	print "Exception"



	
