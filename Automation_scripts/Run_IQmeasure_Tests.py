
# Run_IQmeasure_Tests.py
#
#	Example uses:	Run_IQmeasure_Tests.py IQmeasure_3.0.7.RC2 
#					Run_IQmeasure_Tests.py IQmeasure_3.0.7.RC2 quick

import sys
import os
import os.path
import subprocess

def Run( package_name, test_mode ):
	print ("\n -----Start testing inside Run_IQmeasure_Tests.py script-----")
	
	#Initialize all the variables to be used in code here: 	
	#qa_auto_dir = ""
	package_bin_path = ""
	IQmeasure_full_tests_list = ""
	IQmeasure_quick_tests_list = ""
	tests_list = ""
	log_file_dir = ""
	log_file_path = ""
	log_file = ""
	
	#define qa_automation_directory path:
	#qa_auto_dir = "C:\\LitePoint\\IQmeasure\\QA_automation"
	package_bin_path = os.path.join( "C:\\LitePoint\\IQmeasure\\", package_name, "Bin" )
	print "\n... package path = ", package_bin_path, " ..."
	os.chdir( package_bin_path )

	# To redirect console output to a file, do the following style:
	# IQmeasureTest.exe -exit -QA_11AC > QA_11AC_out.txt 2>&1

	# define the test list which will be used for QA
	IQmeasure_full_tests_list = [ "QA_11AC", "QA_11ag", "QA_11b", "QA_11n", "QA_BT", "QA_CW", "QA_Mask", "QA_flatness" ]
	IQmeasure_quick_tests_list = [ "QA_11ag" ]

	if test_mode.lower() == "full":
		tests_list = IQmeasure_full_tests_list
	elif test_mode.lower() == "sanity":
		tests_list = IQmeasure_quick_tests_list
	else:
		print "ERROR: unknown test mode: ", test_mode, ".  Script aborted."
		exit(4)

	# make sure the .\Log folder exists before running the tests
	log_file_dir = ".\\Log"
	if not os.path.isdir( log_file_dir ):
		os.mkdir( log_file_dir )

	# run all the test functions and redirect output to console and a log file, one for each function
	print "\n -----Running '", test_mode, "' tests-----" 
	for test_name in tests_list:
		log_file_path = os.path.join( log_file_dir, test_name + ".log" )
		log_file = open( log_file_path, "w" )
		command = "IQmeasureTest.exe -" + test_name + " -exit"
		print "... Running command: ", command, " ..."
		p = subprocess.Popen ( command, shell=True, stdout=subprocess.PIPE )
		for line in p.stdout:
			sys.stdout.write( line )
			log_file.write( line )
		p.wait()
		log_file.close()

	print "\n -----End running IQmeasure tests.\n"


	#cd to the 'qa_auto_dir' folder
	#print "\n -----cd to ", qa_auto_dir, " ..."
	#os.chdir( qa_auto_dir )
	
	print ("\n -----Finished testing inside Run_IQmeasure_Tests.py script-----")
		

if __name__ == "__main__":

	Run( package_name, test_mode )





