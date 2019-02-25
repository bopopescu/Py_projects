import os
import os.path
import subprocess
import distutils.core
import time
import shutil

def Run( PKG_DUT_path, test_list, PACKAGE_NAME, Com_Ports_List, Report_Template_list ):
	print "\n ----------Entering Run_QA----------"
	top_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
	setup_file_path = os.path.join(top_dir, "Setup_files")
	setup_file_path_core = os.path.join(setup_file_path, "Setup")
	
	# first move setup files
	print "\n -----Moving Setup Files"
	for path in PKG_DUT_path:
		distutils.dir_util.copy_tree( setup_file_path_core, path)

	# edit com ports, move setup.ini files
	setup_ini_path = os.path.join(setup_file_path_core, "SetUp.ini")
	for Com_Num, DUT_path in enumerate(PKG_DUT_path):
		dest = os.path.join(DUT_path, "Setup.ini")	
		with open(setup_ini_path, 'r') as in_setup, open(dest, 'w') as out_setup:
			for line in in_setup:
			 	if "ComNo" in line:
			 		line = "ComNo=" + Com_Ports_List[Com_Num] + ' \n'
				out_setup.write(line)

	# Goal is to move the 1st test flow file, append _DUT#, edit it for the correct ports, and then run it.
	procs = []
	print "\n -----Moving and Renaming Test flow files"
	for test_name in test_list:
		for DUT_Number, DUT_path in enumerate(PKG_DUT_path, start = 1):
			# rename the test flow file
			old_name = os.path.splitext(test_name)
			new_name = old_name[0] + "_DUT" + str(DUT_Number) + old_name[1]
			source = os.path.join(setup_file_path, test_name)
			dest = os.path.join(DUT_path, new_name)

			#open orig_test file and edit ports, and move to dest_test
			with open(source, 'r') as orig_test, open(dest, 'w') as dest_test:
				for line in orig_test:
				 	if 'APP_ID [Integer]' in line:
				 		line = "\t\t>APP_ID [Integer]  = " + str(DUT_Number) + ' \n'
				 	elif 'VSA_PORT [Integer]' in line:
				 		line = "\t\t>VSA_PORT [Integer]  = " + str(DUT_Number+1) + ' \n'
				 	elif 'VSG_PORT [Integer]' in line:
				 		line = "\t\t>VSG_PORT [Integer]  = " + str(DUT_Number+1) + ' \n'
				 	dest_test.write(line)
			print "\n\t -----Done Moving Test : ", test_name

			#Run the test
			print "\n\t -----Running Test {0} now".format(test_name)
		 	os.chdir(DUT_path)
		 	command = "IQrun_Console.exe -run " + new_name + " -exit"
		  	procs.append(subprocess.Popen(DUT_path + '\\' + command))
		#Finished test, reset and go onto next test in list
		exit_codes = [p.wait() for p in procs]
	 	procs = []
	print "\n -----Done with Tests, Making Reports"


	# Move log files in DUT to workspace\Project_name\Results\Log
	dest_results_dir = os.path.join(top_dir, "Results")
	dest_log_file_dir_base = os.path.join(dest_results_dir, "Log")
	dest_csv_file_base = os.path.join(dest_results_dir, "CSV_files")

	# delete old log files and csv files
	# Sometimes we get a windows error 145 which is fixed if we just try it again, hence the try loop
	for i in range (0,5):
		try:
			if os.path.isdir(dest_results_dir):
				print "\n -----Deleting old log and csv files"
				distutils.dir_util.remove_tree(dest_results_dir)
			os.mkdir(dest_results_dir)		
			os.mkdir(dest_log_file_dir_base)
			os.mkdir(dest_csv_file_base)
			break
		except WindowsError as e:
			if e.winerror == 145:
				time.sleep(1)
				print "\n -----ERROR: Windows error 145, trying again."
	email_Results = ""
	createReportFlag = True
	testFailFlag = False
	print "\n -----Moving Log Files and CSV Files"
	for DUT_Number, DUT_path in enumerate(PKG_DUT_path, start = 1):
		# Simply move all the log files to archive
		log_file_dir = os.path.join(DUT_path, "Log")
		dest_log_file_dir = os.path.join(dest_log_file_dir_base, "DUT" + str(DUT_Number))
		os.mkdir(dest_log_file_dir)
		if os.path.isdir(log_file_dir):
			distutils.dir_util.copy_tree(log_file_dir, dest_log_file_dir)
			run_count = 1
			append_flag = False
			email_Results += "\nTest Results for DUT{0}:".format(DUT_Number)
			with open(os.path.join(log_file_dir, "Log_all.txt"), 'r') as log_file:
				for line in log_file:
					if "--------------------------------------------------------------------" in line:
						append_flag = not append_flag
						if append_flag:
							email_Results += "\nRun {0}".format(run_count) + line
							run_count += 1
					if append_flag and "--- [Failed]" in line:
						email_Results += line
						testFailFlag = True

		else:
			print "\n\t No Log files found for DUT" + str(DUT_Number)

		# Move all the csv files to the CSV folder so that the Report Builder can use them
		csv_file = os.path.join(DUT_path, 'Result', 'result.csv')
		dest_csv_file = os.path.join(dest_csv_file_base, 'result' + str(DUT_Number) + '.csv')
		if os.path.isfile(csv_file):
			shutil.copyfile(csv_file, dest_csv_file)
		else:
			print "\n\t No CSV files found for DUT" + str(DUT_Number)
			createReportFlag = False

	if createReportFlag:
		print "\n -----Creating Report"
		Report_Template_list = [os.path.join(setup_file_path, report_template) for report_template in Report_Template_list]
		command = "reportbuildr.bin"
		templates = "--templates=" + ','.join(Report_Template_list)
		curr_time = time.strftime("%d_%m_%Y")
		report_title = '--title="Auto_QA {0}"'.format(os.path.splitext(PACKAGE_NAME)[0])
		report_description = '--description=\"{0}\"'.format(curr_time)
		report_name = os.path.splitext(PACKAGE_NAME)[0] + '_' + curr_time + '.pdf'
		rel_path = "../Results"
		#rel_path = os.path.join(os.path.basename(top_dir), "Results")# For some reason Report Builder can't use the full path to specify pdf output, so we grab the rel path name
		report_name = os.path.join(rel_path, report_name)
		os.chdir(os.path.dirname(os.path.abspath(__file__)))
		#os.chdir('D:\\Jenkins\\workspace')
		command_args = [command, templates, report_title, report_description, '-p', report_name, dest_csv_file_base]
		subprocess.call(command_args)
	return email_Results, testFailFlag

if __name__ == "__main__":
	Run( PKG_DUT_path, test_list, PACKAGE_NAME, Com_Ports_List, Report_Template_list )
