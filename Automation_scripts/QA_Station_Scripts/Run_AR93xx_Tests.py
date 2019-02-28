import sys
import os
import os.path
import time
import subprocess
import shutil
import distutils.dir_util
##package_name = "IQfact+_AR93xx_3.2.1.RC3"
##test_mode = "sanity"
##QA_file = "C:\\QA_files"

def Run( package_name, test_mode, QA_file):
	print ("Start Running AR93xx_Tests.py\n")
	#copy setup files to pkg bin folder
	setup_file_path = os.path.join(QA_file, "Setup_files", "AR93xx")
	PKG_bin_path = os.path.join( "C:\\LitePoint\\IQfact_plus\\", package_name, "Bin")
	print "Copying setup files to bin folder... \n"
	distutils.dir_util.copy_tree( setup_file_path, PKG_bin_path)

	os.chdir( PKG_bin_path )

	# define the test list which will be used for QA
	full_tests_list = [ "93xx_3by3.txt", ]
	quick_tests_list = [ "93xx_3by3.txt", ]
	
	if test_mode.lower() == "full":
		tests_list = full_tests_list
	elif test_mode.lower() == "sanity":
		tests_list = quick_tests_list
	else:
		print "ERROR: unknown test mode: ", test_mode, ".  Run_AR93xx_Tests.py aborted.\n"
		exit(4)


	# run tests
	print "Running ", test_mode, " tests...\n" 
	for test_name in tests_list:
		command = "IQrun_Console.exe -run " + test_name + " -exit"
		print command, " is running ..."
		os.system(command)
		
	curr_time = time.strftime("%H.%M.%S__%d_%m_%Y")

	#setup log folder: C:\LitePoint\IQfact_plus\Automation_log
	log_file_dir = "C:\\LitePoint\\IQfact_plus\\Automation_log\\AR93xx"
	log_file_dir = os.path.join(log_file_dir, package_name)
	if os.path.isdir(log_file_dir) != True:
                os.mkdir(log_file_dir)
                
	log_file_dir = os.path.join(log_file_dir, curr_time )
	os.mkdir(log_file_dir)
	
	#copy log, results to C:\\LitePoint\\IQfact_plus\\Automation_log\\AR93xx
	distutils.dir_util.copy_tree(os.path.join("C:\\LitePoint\\IQfact_plus\\", package_name, "Bin", "log"), log_file_dir+"\\log")
	distutils.dir_util.copy_tree(os.path.join("C:\\LitePoint\\IQfact_plus\\", package_name, "Bin", "Result"), log_file_dir+"\\Result")
		
	print "Finish Running AR93xx_Tests.py\n"

if __name__ == "__main__": 

	Run( package_name, test_mode, QA_file)




