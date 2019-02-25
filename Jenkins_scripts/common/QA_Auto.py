import os
import os.path
import sys
import traceback
import smtplib
import glob
import shutil
import time
import signal
import atexit
import subprocess

import Run_Pkg_Installation
import Run_QA

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

installed_dir_global = ""
testFailFlag_global = False

def send_Email( server, sender, recipients, subject, message ):
	#Send Email to tell package finished installing
	session = smtplib.SMTP(server)
	# Create message container - the correct MIME type is multipart/alternative.
	msg = MIMEMultipart('alternative')
	msg['From'] = sender
	if len(recipients) > 1: 	
		msg['To'] = ",".join(recipients)
	else:
		msg['To'] = str(recipients)	
	msg['Subject'] = subject
	text_PKG = message
	# Record the MIME types of both parts - text/plain and text/html.
	msg_PKG = MIMEText(text_PKG, 'plain')
	# Attach parts into message container.
	msg.attach(msg_PKG)
	# sendmail function takes 3 arguments: sender's address, recipient's address
	# and message to send - here it is sent as one string.
	print "\n Sending email from:" , sender, "to: " , recipients
	session.sendmail(sender, recipients, msg.as_string())
	session.quit()

def clean_up():
	print "\n -----Cleaning Up"
	for i in range(0,5):
		try:
			if os.path.isdir(installed_dir_global): #Shouldn't exist because we extract in the Jenkins workspace, which should clean itself every job. But just in case.
				print "\n\t Deleting Installed Directory"
				shutil.rmtree(installed_dir_global) #this is used to remove all directory specified by Destination_Package_dir and all its contents. But it is risky. 
			break
		except WindowsError as e:
			if e.winerror == 145:
				sleep(1)
				print "\n -----ERROR: Windows error 145, trying again."

def stationFree():
	# go through process list, see if station is currently being used by someone, perhaps for manual testing
	processes = subprocess.Popen('tasklist', stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE).communicate()[0]
	if any(x in processes for x in ["IQrun_console.exe", "IQfactStudio.exe"]):
		return False
	else:
		return True

def QA_Auto(Project_Name, test_mode, PKG_install_flag, recipients, full_test_list, quick_test_list, Enable_Emails, Install_Redistr, Number_of_DUTs, Com_Ports_List):
	sender = 'Silicon_Solution_QA@litepoint.com' #Email id used to send out notifications from the server
	server = '192.168.2.199' # Ip address of litepoint email server

	####################################################
	####################################################
	##		         Extract and Install 			  ##
	##												  ##
	####################################################
	####################################################

	# find most recent package, which is the one to install. 
	# Proably unnecessary since Jenkins will wipe this folder when starting the job, but just in case
	os.chdir(zip_file_dir)
	PACKAGE_NAME = max(glob.iglob('*.zip'), key=os.path.getctime)
	curr_time = time.strftime("_%d_%m_%Y")
	path_base = "C:\\LitePoint\\IQfact_plus\\"
	installed_dir = os.path.join( path_base, os.path.splitext(PACKAGE_NAME)[0] + curr_time)
	global installed_dir_global
	installed_dir_global = installed_dir

	build_output_dir = os.path.join(top_dir, "Build_Output")
	if os.path.isdir(build_output_dir):
		shutil.rmtree(build_output_dir)
	os.mkdir(build_output_dir)

	ver_num = os.path.splitext(PACKAGE_NAME.split('.')[0][-1:] + '.' + '.'.join(PACKAGE_NAME.split('.')[1:]))[0]

	with open(os.path.join(build_output_dir, "Parameters.properties"), 'w') as parameter_file:
		parameter_file.write("PACKAGE_VERSION=" + ver_num + '\n')

	print "\n -------------PACKAGE NAME: ", PACKAGE_NAME
	if PKG_install_flag == '1':
		Run_Pkg_Installation.Run(zip_file_dir, PACKAGE_NAME, Install_Redistr, Number_of_DUTs)

		if Enable_Emails == '1':
			subject = "QA update for station: {0}".format(Project_Name)
			text_PKG_installed = "Hi! Package installed on QA station.\nHere is the package name: {0}".format(PACKAGE_NAME)
			send_Email( server, sender, recipients, subject, text_PKG_installed )
		else:
			print "\n -----Skipping PKG install emails as flag = ", Enable_Emails

	else: # already installed today, proceed with QA
		print "\n -----Skipping Package Install as flag = ", PKG_install_flag

		if not os.path.isdir(installed_dir):
			print "\n -----ERROR: Need to Install Package! Aborting Script"
			exit("-----ERROR: Need to Install Package! Aborting Script")


	####################################################
	####################################################
	##		            Run QA test 		 		  ##
	##												  ##
	####################################################
	####################################################
	print "\n -----Running QA Now"	

	# Run_Pkg_Installation made DUT folders. Since we know the Number of DUTs, we could just find them like that.
	# However, just to be safe, we iterate over inside the installed dir to get the list of DUTs and make sure it matches.
	PKG_DUT_path = [] #list of all the DUTs
	for item in os.listdir(installed_dir):
		dirs = os.path.join(installed_dir, item)
		if os.path.isdir(dirs) and 'DUT' in dirs:
			PKG_DUT_path.append(dirs)
	if len(PKG_DUT_path) < Number_of_DUTs:
		print "\n -----ERROR: Number of DUTs more than number of existing ones. Reinstall Package and Reboot Script"
		exit("-----ERROR: Number of DUTs more than number of existing ones. Reinstall Package and Reboot Script")
	PKG_DUT_path = PKG_DUT_path[:Number_of_DUTs]
	if len(Com_Ports_List) < Number_of_DUTs:
		print "\n -----ERROR: Number of DUTs exceeds given number of Com Ports."
		exit("-----ERROR: Number of DUTs exceeds given number of Com Ports.")
	Com_Ports_List = Com_Ports_List[:Number_of_DUTs]
	global testFailFlag_global
	email_results, testFailFlag_global = Run_QA.Run(PKG_DUT_path, test_list, PACKAGE_NAME, Com_Ports_List, Report_Template_list)
	print "\n -----Finished QA"

	print "\n -----QUICK SUMMARY:"
	print email_results

	with open(os.path.join(build_output_dir, "Parameters.properties"), 'a') as parameter_file:
		if testFailFlag_global: # tests failed, so status is false
			parameter_file.write("STATUS=false")
		else:
			parameter_file.write("STATUS=true")
	text_PKG_QA = "Here is a summary of the tests that failed: \n" + email_results

	with open(os.path.join(build_output_dir, "Email_Message.txt"), 'w') as email_file:
		email_file.write(text_PKG_QA)

	if Enable_Emails == '1':
	#Send Email to tell package finished installing
		subject = "QA update for station: {0}".format(Project_Name)
		#text_PKG_QA = "Hi!\nGood News.\nFinished {0} QA for the package : {1}".format(test_mode, PACKAGE_NAME)
		send_Email( server, sender, recipients, subject, text_PKG_QA )
	else:
		print "\n -----Skipping QA emails as flag = ", Enable_Emails
		
	# if testFailFlag_global:
		# exit("QA Finished, but some tests failed!")


try:
	#get path to directory of job, aka where the QA config file is
	top_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
	zip_file_dir = os.path.join(top_dir, "Packages")

	#grab parameters from config file 
	os.chdir( top_dir )
	with open("QA_config.txt", "r") as f:
		for line in f:
			value = line.strip()
			col = value.split()
			if not value.startswith('#'):	#ignore comments
				if 'Project_Name' in line:
					Project_Name=col[2]
						
				elif 'Test_mode' in line:
					test_mode=col[2].lower()

				elif 'New_PKG_Installation' in line:
					PKG_install_flag = col[2]
					if PKG_install_flag != '0' and PKG_install_flag != '1':					
						print "New_PKG_Intallation flag should be 1 or 0"
						exit("New_PKG_Intallation flag should be 1 or 0")

				elif 'Recipient_Email_ID' in line:
					# check if the recipient email id has more than one recipient in it. Accordingly store the values in variables to be used later on 
					recipients = col[2:]
				
				elif 'Full_tests_list' in line:
					full_test_list = col[2:]

				elif 'Quick_tests_list' in line:
					quick_test_list = col[2:]

				elif 'Enable_Emails' in line:
					Enable_Emails = col[2]
					if Enable_Emails != '0' and Enable_Emails != '1':	
						print "Enable_Emails flag should be 1 or 0"
						exit("Enable_Emails flag should be 1 or 0")

				elif 'Install_Redistributables' in line:
					Install_Redistr = col[2]
					if Install_Redistr != '0' and Install_Redistr != '1':
						print "Install_Redistributables flag should be 1 or 0"
						exit("Install_Redistributables flag should be 1 or 0")

				elif 'Number_of_DUTs' in line:
					Number_of_DUTs = int(col[2])

				elif 'Com_Ports_List' in line:
					Com_Ports_List = col[2:]

				elif 'Report_Template_list' in line:
					Report_Template_list = col[2:]

	print "\n -----Project Name : ", Project_Name
	print "\n -----Test mode : ", test_mode
	print "\n -----New_PKG_Installation : ", PKG_install_flag
	print "\n -----Enable_Emails : ", Enable_Emails
	print "\n -----Number_of_DUTs : ", Number_of_DUTs

	if test_mode == "sanity":
		test_list = quick_test_list
	elif test_mode == "full":
		test_list = full_test_list
	else:
		print "ERROR: Unknown test mode: ", test_mode, ". Aborting Script.\n"
		exit("ERROR: Unknown test mode: ", test_mode, '.')
	print "\n -----Using test list : ", test_list

	while True:
		if stationFree():
			QA_Auto(Project_Name, test_mode, PKG_install_flag, recipients, full_test_list, quick_test_list, Enable_Emails, Install_Redistr, Number_of_DUTs, Com_Ports_List)
			break
		else:
			print "\n -----QA Station is Busy. Checking again in 30 seconds"
			time.sleep(30)

except: 
	print "\n -----Unexpected error:", sys.exc_info()[0],sys.exc_info()[1]
	traceback.print_exc()
	
	if Enable_Emails == '1':
		#Send email notification with the error details attached in it. This helps trace the error details when there is an exception thrown on the machine for any reason
		error_details = sys.exc_info() #store the error info in a variable
		sender = 'Silicon_Solution_QA@litepoint.com'
		server = '192.168.2.199' # Ip address of litepoint email server
		text_Exception = "Attention!!\n\nThis email is send to notify you that there is an exception thrown in the script on QA station: {0}\n\nException summary : {1}\n\nAborting the script due to this exception. Please fix the issue and then re-run the script.".format(Project_Name, error_details)
		subject = "QA update for station: {0}".format(Project_Name)
		send_Email( server, sender, recipients[:1], subject, text_Exception )
	else:
		print "\n -----Skipping emails as flag = ", Enable_Emails
	if not os.path.isdir(os.path.join(top_dir, "Parameters")):
		os.mkdir(os.path.join(top_dir, "Parameters"))
	with open(os.path.join(top_dir, "Parameters", "Errors.txt"), 'w') as error_file:
		error_file.write(traceback.format_exc())
	if not testFailFlag_global:
		clean_up()