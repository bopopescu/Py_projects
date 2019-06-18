import os
import os.path
import subprocess
import shutil
import zipfile
import glob
import time


def Run(zip_file_dir, PACKAGE_NAME, Install_Redistr, Number_of_DUTs):
	print "\n ----------Entering Run_Pkg_Installation----------"

	source_package_path = os.path.join(zip_file_dir, PACKAGE_NAME)

	#Extract the package to Packages folder
	Destination_Package_dir = os.path.join( zip_file_dir, os.path.splitext(PACKAGE_NAME)[0] )
	print "\n -----Destination package path: ", Destination_Package_dir
 #



#
	# Sometimes when removing a tree we get a windows error 145 which is fixed if we just try it again, hence the try loop
	for i in range(0,5):
		try:
			if os.path.isdir(Destination_Package_dir): #Shouldn't exist because we extract in the Jenkins workspace, which should clean itself every job. But just in case.
				print "\n -----Deleting old package path"
				shutil.rmtree(Destination_Package_dir) #this is used to remove all directory specified by Destination_Package_dir and all its contents. But it is risky. 
			os.mkdir(Destination_Package_dir)
			break
		except WindowsError as e:
			if e.winerror == 145:
				time.sleep(1)
				print "\n -----ERROR: Windows error 145, trying again."

	# Extracting using following code: 	
	print "\n -----Extracting package: ", PACKAGE_NAME, 
	zip_handler = zipfile.ZipFile(source_package_path, "r")
	zip_handler.extractall(Destination_Package_dir)
	zip_handler.close()

	#Install Package and Redistributables
	print "\n -----Installing Packages Now"
	if Install_Redistr == '1':
		sub_dirs = []
		for item in os.listdir(Destination_Package_dir):
			dirs = os.path.join(Destination_Package_dir, item)
			if os.path.isdir(dirs):
				sub_dirs.append(dirs)

		#Search through the extracted directory and find redistributables. Install them in silent mode
		for dirs in sub_dirs:
			if "MCR79" in dirs:
				os.chdir(dirs)
				print "\n\t Installing Matlab."
				subprocess.call( ["MCRInstaller.exe", '/s', '/v/passive'])

			elif "VC2005" in dirs:
				os.chdir(dirs)
				print "\n\t Installing VC2005."
				subprocess.call( ["vcredist_x86.exe", '/Q'] )

			elif "VC2008" in dirs:
				os.chdir(dirs)
				print "\n\t Installing VC2008."
				subprocess.call( ["vcredist_x86.exe", '/Q'] )

			elif "VC2012" in dirs:
				os.chdir(dirs)
				print "\n\t Installing VC2012."
				subprocess.call( ["vcredist_x86.exe", '/install', '/quiet', '/norestart'] )
			
	#Install the actual package
	os.chdir( os.path.join(Destination_Package_dir, "IQfact_plus") )
	print "\n\t Installing the package."
	subprocess.call ( ["setup.exe", '/S'])

	curr_time = time.strftime("_%d_%m_%Y")
	print "\n\t Done Installing clean version, creating copy with date: ", curr_time

	path_base = "C:\\LitePoint\\IQfact_plus\\"
	orig_installed_dir = os.path.join( path_base, os.path.splitext(PACKAGE_NAME)[0] )
	installed_dir = os.path.join( path_base, os.path.splitext(PACKAGE_NAME)[0] + curr_time )
	
	# Sometimes when removing a tree we get a windows error 145 which is fixed if we just try it again, hence the try loop
	for i in range(0,5):
		try:
			if os.path.isdir(installed_dir):
				print "\n\t Found old Directory with date, so deleting."
				shutil.rmtree(installed_dir)
			shutil.copytree(orig_installed_dir, installed_dir)
			print "\n\t Done Installing, creating DUT folders"	
			break
		except WindowsError as e:
			if e.winerror == 145:
				time.sleep(1)
				print "\n -----ERROR: Windows error 145, trying again."

	PKG_bin_path = os.path.join( installed_dir, "bin")
	for i in range( 1, Number_of_DUTs + 1 ):
		PKG_DUT_path = os.path.join( installed_dir, "DUT" + str(i) )
		shutil.copytree( PKG_bin_path, PKG_DUT_path )
		print "\n\t Created DUT" + str(i)

	print "\n\t Done creating DUT folders"

if __name__ == "__main__":
	fpath = os.path.abspath('IQfact+_BRCM_4364_MPS_3.4.1.17.zip')
	(zip_file_dir, PACKAGE_NAME) = os.path.split(fpath)
	Install_Redistr=os.path.join(zip_file_dir,"IQfact+_BRCM_4364_MPS_3.4.1.17")
	Run(zip_file_dir, PACKAGE_NAME, Install_Redistr, 4)

