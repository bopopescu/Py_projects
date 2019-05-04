#************************************************
#1. Support IQmeasure station
#2. Support AR93xx Station
#3. Support QCA6174 Station
#************************************************
import os
import sys
import copy
import shutil
import Run_IQmeasure_Tests
from QA_Station_Scripts import Run_AR93xx_Tests
from QA_Station_Scripts import Run_QCA_6174_Tests
import distutils.core

def Run( package_name, test_mode, QA_file ):

	print ("\n -----Entering Run_QA.py script-----\n")
	
	# Check for package names
	if "IQmeasure" in package_name:   #IQmeasure Station
		# Copy IQmeasureTest.exe and Setup files from the shared location to the package folder
		Source_Executable_path = os.path.join(QA_file, "Setup_files", package_name)
		PKG_bin_path = os.path.join( "C:\\LitePoint\\IQmeasure\\", package_name, "Bin" )
		print "\n----- Copying Executable and Setup Files to package folder: "	
		distutils.dir_util.copy_tree( Source_Executable_path, PKG_bin_path ) #Copying all the contents of src folder to dest folder using this command
		
		print "\n -----Calling Package Installation : Run_IQmeasure_Tests.py script"
		Run_IQmeasure_Tests.Run( package_name, test_mode )
		print "\n -----Back to main script, Finished running of the Run_IQmeasure_Tests.py script"
		
	elif "IQfact+_AR93xx" in package_name: #AR93xx station
		#print "Starting test on ", package_name, "\n"
		Run_AR93xx_Tests.Run( package_name, test_mode, QA_file )
                print "-----Exiting Run_QA.py\n"

        elif "IQfact+_QCA_6174" in package_name: #QCA_6174 station
		#print "Starting test on ", package_name, "\n"
		Run_QCA_6174_Tests.Run( package_name, test_mode, QA_file )
                print "-----Exiting Run_QA.py\n"
		
		
	else:
		print "\n Error: Not able to find any QA commands in this file.. "
		exit(4)
			
if __name__ == "__main__":
	Run( package_name, test_mode, QA_file )