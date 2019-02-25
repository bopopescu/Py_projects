
# Install new package in local PC.

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

def Run( package_type, Project_Name, PACKAGE_NAME, package_path, script_path ):
	
	print ("\n ----- Inside Run_PKG_Installation.py script-----")
	qa_auto_dir = ""
	source_package_path = ""
	Destination_Package_dir = ""
	destination_package_path = ""
	zip_handler = ""
	zip_files = ""
		
	# Change this to following code depending on if its release candidate or formal package 
	if "IQmeasure" in Project_Name:
		print "\n Debug : inside IQmeasure package copying if loop.. "
		if package_type.lower() == "internal" or package_type.lower() == "releasecandidate" or package_type.lower() == "engineeringdrop":
			source_package_path = "\\\\lphqfiler1\\Software\\LitePoint\\Silicon_Solutions\\internal_releases\\{0}\\{1}.zip".format(Project_Name, PACKAGE_NAME )
		elif package_type.lower() == "release":
			source_package_path = "\\\\lphqfiler1\\Software\\LitePoint\\Silicon_Solutions\\internal_releases\\{0}\\releases\\{1}.zip".format(Project_Name, PACKAGE_NAME )
		else:
			print "ERROR: unknown package type: ", package_type, ".  Script aborted."
			exit(3)
	else : 
		print "\n Debug : inside chipset package "
		if package_type.lower() == "internal" or package_type.lower() == "releasecandidate" or package_type.lower() == "engineeringdrop": 
			source_package_path = os.path.join("\\\\lphqfiler1\\Software\\LitePoint\\Silicon_Solutions\\internal_releases", package_path, PACKAGE_NAME + ".zip" )
		elif package_type.lower() == "release":
			source_package_path = os.path.join("\\\\lphqfiler1\\Software\\LitePoint\\Silicon_Solutions\\internal_releases", package_path, "releases", PACKAGE_NAME + ".zip")
		else:
			print "ERROR: unknown package type: ", package_type, ".  Script aborted."
			exit(3)
		
	# Location where you want to copy the package on local
	Destination_Package_dir = "C:\\QA_files\\Packages\\{0}".format(Project_Name)
		
	#Check if the Desitnation_Package_dir exists, if not create one before copying the package
	if not os.path.isdir(Destination_Package_dir):
		print "\n Destination path does not exists.. Creating the folder before copying package.."
		os.mkdir(Destination_Package_dir)
	
	# copy the source package to the destination path	
	print "\n -----Copying package ", PACKAGE_NAME, " to local machine..."	
	shutil.copy( source_package_path, Destination_Package_dir )

	# get path to package file
	destination_package_path = os.path.join( Destination_Package_dir, PACKAGE_NAME )
	print "\n -----Destination package path: ", destination_package_path
	zip_files = glob.glob( destination_package_path + ".zip")

	
	print "\n -----Extracting package: ", PACKAGE_NAME, " to local machine..."
	# Extracting using following code: 	
	for zip_filename in zip_files:
		dir_name = os.path.splitext(zip_filename)[0]
		if os.path.isdir(dir_name):
			#shutil.rmtree(dir_name) #this is used to remove all directory specified by dir_name and all its contents. But it is risky. 
			# sanity check: make sure we do not delete directory we should not by mistake....
			s_path = dir_name
			packages_dir_name = ""
			sub_dir_count = 0
			while sub_dir_count == 0 or len(s_leaf) > 0:
				s_tuple = os.path.split( s_path )
				s_path = s_tuple[0]
				s_leaf = s_tuple[1]
				if sub_dir_count == 2:
					packages_dir_name = s_leaf
					print "\n\t packages_dir_name : {0}" .format(packages_dir_name)
				sub_dir_count += 1
			if sub_dir_count >= 4 and packages_dir_name.lower() == "packages":
				print "\n\t Debug: Deleting the directory : {0}" .format (dir_name)
				shutil.rmtree(dir_name)

		os.mkdir(dir_name)
		zip_handler = zipfile.ZipFile(zip_filename, "r")
		zip_handler.extractall(dir_name)
	zip_handler.close()
	
	#Visual studio and MATLAB installation command
	print "\n -----Installing MATLAB and VC stuff.."
	os.chdir("C:\\QA_files")
	f = open("QA_config.txt", "r")
	win_OS = ""
	for line in f:
                if 'Win_OS' in line:
                        value = line.strip()
                        col=value.split()
                        win_OS = col[2]
        f.close()
	os.chdir(script_path)
	if win_OS == "WIN7":
                command = "Automation_Setup_installer.au3 " + destination_package_path
                print "\n*****Default WIN7 dectected\n"
        elif win_OS == "XP":
                command = "Automation_Setup_installer_xp.au3 "+ destination_package_path
                print "\n*****winXP dectected\n"
        	
	print "... Running command: ", command, " ..."
	p = subprocess.Popen ( command, shell=True, stdout=subprocess.PIPE )

	time.sleep(160) #adding delay of 60 secs to ensure the AutoIt script finishes its runs successfully
	print "\n***** Finished Matlab and VC installation *****\n"
	print "\n ----Installing package: ", PACKAGE_NAME, " to local machine in background..."
	if "IQmeasure" in Project_Name:
		# cd to IQmeasure folder in un-zipped package
		os.chdir( os.path.join( destination_package_path, "IQmeasure" ) )
	else :
		# cd to IQfact_plus folder in un-zipped package for installation
		os.chdir( os.path.join( destination_package_path, "IQfact_plus" ) )
		
	#package installation command
	setup_command = "Setup setup.exe /S"
	p = subprocess.call( setup_command )
	
	# set final context to the QA_automation directory
	#os.chdir( qa_auto_dir )
	
	print ("\n -----Finished Run_PKG_Installation.py script, going back to top level script-----")
	#Return to top level script
	return( PACKAGE_NAME )

if __name__ == "__main__":

	package_name = ""
	
	package_name = Run( package_type )










