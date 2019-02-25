# our top level script
import os
import sys
import copy
import shutil
import Run_PKG_Installation
import Run_IQmeasure_Tests
import Run_QA
import distutils.core
import sched
import time
import mysql.connector
import traceback
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def check_package():

	print "\n ----INFO: Entering check_package()..."
	global loop_counter	
	global QA_is_running
	print "\n ----Attempt counter: ", loop_counter
	# if QA is already started, then return, no need to check
	if QA_is_running:
		return
		
	#Check for the package ready here and if found do QA
	package_type = ""
	package_name = ""
	Source_Executable_path = ""
	PKG_bin_path = ""
	PKG_Install_flag = True #Default: Install new package 
	Test_Flag = '1' #Enter the Test ID here, default should be = 1 for new package
	PACKAGE_ID = ""
	
	sender = 'Silicon_Solution_QA@litepoint.com' #Email id used to send out notifications from the server
	server = '192.168.2.199' # Ip address of litepoint email server
	
	#Establish connection to the database
	# Change hostname(usually localhost), port (default=3306), username, password and name of the database based on your database and table name
	db = mysql.connector.connect(host="IQ-auto-build ", port="3306", user="lp_client", passwd="lp", db="iqautobuild") 
	cur = db.cursor() 
		
	#SELECT Query : SELECT Test, projectName, ReleaseVersion FROM buildresults WHERE projectName = 'IQmeasure' AND Test=1 ORDER BY dateTime DESC LIMIT 1;
	SELECT_query = ("SELECT Test, projectName, ReleaseVersion, ID from buildresults WHERE projectName = %s AND Test= %s ORDER BY dateTime DESC LIMIT 1")
	
	# UPDATE buildresults SET Test = 0 WHERE projectName = 'IQmeasure' AND ReleaseVersion = '3.0.8' AND ID = 14612
	UPDATE_query = ("UPDATE buildresults SET Test = 0 WHERE projectName = %s AND ReleaseVersion = %s AND ID = %s")
	
	#Run the SELECT query
	cur.execute(SELECT_query, (Project_Name, Test_Flag)) #execute the query
	data = cur.fetchall() #Store the result set
	
	# if loop, checking if new package is detected
	if data :
		print "\n-----INFO: Success, New package detected!!"
		# if package is ready, start QA and set flag: QA_is_running = True
		QA_is_running = True
				
		# Store the package_name
		for row in data :
			TEST_ID = row[0]
			PACKAGE_NAME = row[1] + "_" + row[2]
			Release_Version = row[2]
			PACKAGE_ID = row[3] #PrimeKey for this table, used in UPDATE Query once the package is successfully installed on the machine.
			#print PACKAGE_NAME
			if TEST_ID == '1':
				print ("\n-----INFO: New Package Name : {0} " .format(PACKAGE_NAME))
	
		pkg_name_lower = PACKAGE_NAME.lower() #convert to lower case for string comparisons

		#first check if the PACKAGE_NAME has "Dongle" or "Lock" in the name -
		if pkg_name_lower.rfind( "_lock" ) > 0 :
			PKG_Install_flag = False
			package_type = "Lock"
		elif pkg_name_lower.rfind( "_dongle" )> 0:
			PKG_Install_flag = False
			package_type = "Dongle"
		else:
			pkg_version = pkg_name_lower.rsplit(".")
			print "\n Package version: " ,pkg_version
			if len(pkg_version) == 3 :
				package_type = "release"
			elif pkg_version[len(pkg_version)-1].rfind("rc") >= 0:
				package_type = "releaseCandidate"
			elif pkg_version[len(pkg_version)-1].rfind("eng") >= 0:
				package_type = "engineeringDrop"
			else:
				package_type = "internal"

		print "\n-----INFO: Package needs to be installed: --- ", PKG_Install_flag		
		print "\n-----INFO: Package type :" ,package_type
		
		if package_flag == '1':
			if PKG_Install_flag == True: 
				print "\n-----INFO: New package, do the installation .."
				# Email notification for starting package installation, sent to station owner and jian :
				# Send the message via local SMTP server.
				session = smtplib.SMTP(server)
				# Create message container - the correct MIME type is multipart/alternative.
				msg = MIMEMultipart('alternative')
				msg['From'] = sender
				if Multiple_recipients == True :
					msg['To'] = ",".join(recipients)
				else :
					msg['To'] = recipient1
				msg['Subject'] = "QA update for station: {0}".format(package_path)
				text_PKG_found = "Hi!\nNew package has been detected.\nStarting Package installation on QA station.\nHere is the package name: {0}".format(PACKAGE_NAME)
				# Record the MIME types of both parts - text/plain and text/html.
				msg_PKG_found = MIMEText(text_PKG_found, 'plain')
				# Attach parts into message container.
				msg.attach(msg_PKG_found)
				# sendmail function takes 3 arguments: sender's address, recipient's address
				# and message to send - here it is sent as one string.
				if Multiple_recipients == True :
					print "\n Sending email from:" , sender, "to: " , recipients
					session.sendmail(sender, recipients, msg.as_string())
				else :
					print "\n Sending email from:" , sender, "to: " , recipient1
					session.sendmail(sender, recipient1, msg.as_string())
				session.quit()
				
				#call the pkg_installation script
				print "\n-----INFO: Calling Package Installation Script: Run_PKG_Installation.py "
				
				package_name = Run_PKG_Installation.Run( package_type, Project_Name, PACKAGE_NAME, package_path, script_path )
				print "\n-----INFO: Back to QA_Automation.py, Finished running Run_PKG_Installation.py"	
				
			else:  # PKG_Install_flag != True:
				print "\n-----INFO: No need to install and QA this package, since the package type is   ", package_type
				# Email notification for starting package installation, sent to station owner and jian :
				# Send the message via local SMTP server.
				session = smtplib.SMTP(server)
				# Create message container - the correct MIME type is multipart/alternative.
				msg = MIMEMultipart('alternative')
				msg['From'] = sender
				if Multiple_recipients == True :
					msg['To'] = ",".join(recipients)
				else :
					msg['To'] = recipient1
				msg['Subject'] = "QA update for station: {0}".format(package_path)
				text_PKG_found = "Hi!\nNew package has been detected.\nHere is the package name: {0} \n But, skipping Package installation since Package type is : {1}".format(PACKAGE_NAME , package_type)
				# Record the MIME types of both parts - text/plain and text/html.
				msg_PKG_found = MIMEText(text_PKG_found, 'plain')
				# Attach parts into message container.
				msg.attach(msg_PKG_found)
				# sendmail function takes 3 arguments: sender's address, recipient's address
				# and message to send - here it is sent as one string.
				if Multiple_recipients == True :
					print "\n Sending email from:" , sender, "to: " , recipients
					session.sendmail(sender, recipients, msg.as_string())
				else :
					print "\n Sending email from:" , sender, "to: " , recipient1
					session.sendmail(sender, recipient1, msg.as_string())
				session.quit()
				# Update the DB row for TEST_ID from '1' to '0' since package is Dongle or Lock
				#Run the UPDATE query :
				print ("\n -----Updating the DATABASE since the package is not to be installed..")
				cur.execute(UPDATE_query, (Project_Name, Release_Version, PACKAGE_ID)) #execute the query 
				print "\t\tNumber of Row(s) updated :" +  str(cur.rowcount)
				db.commit() #commit the Updates made to database
						
		else : #package_flag != '1':
			print "\n -----Package already installed, Skipping Installation part.."
			# Email notification for PKG already present and hence skipping installation :
			# Send the message via local SMTP server.
			session = smtplib.SMTP(server)
			msg_1 = MIMEMultipart('alternative')
			msg_1['From'] = sender
			msg_1['To'] = recipient1
			msg_1['Subject'] = "QA update for station: {0}".format(package_path)
			text_PKG_Present = "Hi!\nThe package {0} is already present on QA station\nHence, Skipped package installation".format(PACKAGE_NAME)
			# Record the MIME types of both parts - text/plain and text/html.
			msg_PKG_Present = MIMEText(text_PKG_Present, 'plain')
			# Attach parts into message container.
			msg_1.attach(msg_PKG_Present)
			# sendmail function takes 3 arguments: sender's address, recipient's address
			# and message to send - here it is sent as one string.
			print "\n Sending email from:" , sender, "to: " , recipient1
			session.sendmail(sender, recipient1, msg_1.as_string())
			session.quit()
		
		if PKG_Install_flag == True: 
			# Do the QA only if the package is installed on the machine, if not then no need to do QA.
			# Email notification for PKG installation done and QA is started :
			session = smtplib.SMTP(server)
			msg_2 = MIMEMultipart('alternative')
			msg_2['From'] = sender
			msg_2['To'] = recipient1
			msg_2['Subject'] = "QA update for station: {0}".format(package_path)
			text_QA_Start = "Hi!\nStarting {0} QA for the package : {1}".format(test_mode, PACKAGE_NAME)
			# Record the MIME types of both parts - text/plain and text/html.
			msg_QA_Start = MIMEText(text_QA_Start, 'plain')
			# Attach parts into message container.
			msg_2.attach(msg_QA_Start)
			# sendmail function takes 3 arguments: sender's address, recipient's address
			# and message to send - here it is sent as one string.
			print "\n-----INFO: Sending email from:" , sender, "to: " , recipient1
			session.sendmail(sender, recipient1, msg_2.as_string())
			session.quit()
			
			print "\n-----INFO: Calling QA Script : Run_QA.py"
			Run_QA.Run(package_name, test_mode, QA_file) #Call the QA script to perform chipset specific QA and pass the package_name & test_mode as arguments
			print "\n-----INFO: Finished QA Script.. Back to schedule_install.py script"
			
			#Commit the update for Test from '1' to '0' after successfully running Run_QA.py file & coming back to code here.
			print ("\n-----INFO: Updating the DATABASE once the package installation is done..")
			cur.execute(UPDATE_query, (Project_Name, Release_Version, PACKAGE_ID)) #execute the query 
			print "\n-----INFO: Number of Row(s) updated :" +  str(cur.rowcount)
			db.commit() 
			
			# Email notification for QA done :
			session = smtplib.SMTP(server)
			msg_3 = MIMEMultipart('alternative')
			msg_3['From'] = sender
			msg_3['To'] = recipient1
			msg_3['Subject'] = "QA update for station : {0}".format(package_path)
			text_QA_Finish = "Hi!\nGood News.\nFinished {0} QA for the package : {1}".format(test_mode, PACKAGE_NAME)
			# Record the MIME types of both parts - text/plain and text/html.
			msg_QA_Finish = MIMEText(text_QA_Finish, 'plain')
			# Attach parts into message container.
			msg_3.attach(msg_QA_Finish)
			# sendmail function takes 3 arguments: sender's address, recipient's address
			# and message to send - here it is sent as one string.
			print "\n Sending email from:" , sender, "to: " , recipient1
			session.sendmail(sender, recipient1, msg_3.as_string())
			session.quit()

	else :
		print "\n ----INFO: No package found in database currently..."
		print "\n ----INFO: Please wait for {0} minutes for next package detection.." .format(number_of_minutes)
	
	cur.close() #close the cursor object of database
	db.close() #close the database connection	
	
	loop_counter = loop_counter + 1
	# QA done, so reset the running flag
	QA_is_running = False
	print "\n ----INFO: Exiting check_package() function..."
	
	
try: 
	# initialize a global variable 
	QA_is_running	=	False
	# Set each check period to 30 minutes (60*30 seconds)
	number_of_minutes = 30
	loop_counter = 1 #counter track the event counter for number of times you make a database call.
	check_period = 60 * number_of_minutes

	test_mode = "full" # by default it will be assigned to full and complete QA testing will be performed.
	global Multiple_recipients
	QA_file = "C:\\QA_files"
	os.chdir( QA_file )
	f = open("QA_config.txt", "r")
		
	for line in f:
		if 'Project_Name' in line:
			value=line.strip()
			col=value.split()
			Project_Name=col[2]
			
		elif 'Test_mode' in line:
			value=line.strip()
			col=value.split()
			test_mode=col[2]
			
		elif 'New_PKG_Installation' in line:
			value=line.strip()
			col=value.split()
			package_flag=col[2]
			
		elif 'Additional_Package_Path' in line:
			value=line.strip()
			col=value.split()
			package_path=col[2]
			
		elif 'Recipient_Email_ID' in line:
			value=line.strip()
			col=value.split()
			# check if the recipient email id has more than one recipient in it. Accordingly store the values in variables to be used later on 
			if len(col) > 3 and len(col) < 6 :
				Multiple_recipients = True
				recipient1 = col[2]
				recipient2 = col[4]
				recipients = recipient1 , recipient2
				
			else :
				Multiple_recipients = False
				recipient1 = col[2]
		
		elif 'Script_path' in line: 
			value=line.strip()
			col=value.split()
			script_path = col[2]
			
	print "\n -----Project Name : ", Project_Name
	print "\n -----Test mode : ", test_mode
	print "\n -----New PKG Package Installation flag : ", package_flag
	print "\n -----Additional Package path : ", package_path
	print "\n -----Script path on your system: ", script_path
	if Multiple_recipients == False :
		print "\n -----recipient email id : ", recipient1
	else :
		print "\n -----recipient email ids are : ", recipient1 , recipient2
		
	if package_flag == '1':
		print "\n ----- New Package needs to be installed: As Flag = " , package_flag
	else: 
		print "\n -----Already installed previously, no need to reinstall as Flag = " , package_flag
	
	f.close()
	
	check_package() #Call the function first time before scheduling events
		
	# create a scheduler object
	s = sched.scheduler( time.time, time.sleep )
	while True:
		
		print "\n-----Debug: Calling check_package()..."	
		s.enter( check_period, 1, check_package, () )
		s.run()
		print \
		      "*****************************\
				TEST is DONE \
		       *****************************"
		time.sleep(10)
	
except: 
	print "\n -----Unexpected error:", sys.exc_info()[0],sys.exc_info()[1]
	traceback.print_exc()
	f.close() #close the text file if any exception in normal operation.
	
	#Send email notification with the error details attached in it. This helps trace the error details when there is an exception thrown on the machine for any reason
	error_details = sys.exc_info() #store the error info in a variable
	sender = 'Silicon_Solution_QA@litepoint.com'
	server = '192.168.2.199' # Ip address of litepoint email server
	# Send the message via local SMTP server.
	session = smtplib.SMTP(server)
	# Create message container - the correct MIME type is multipart/alternative.
	msg_exception = MIMEMultipart('alternative')
	msg_exception['From'] = sender
	msg_exception['To'] = recipient1
	msg_exception['Subject'] = "QA update for station : {0}".format(package_path)
	text_Exception = "Attention!!\n\nThis email is send to notify you that there is an exception thrown in the script on QA station: {0}\n\nException summary : {1}\n\nAborting the script due to this exception.. Please fix the issue and then re-run the script.".format(package_path, error_details)
	# Record the MIME types of both parts - text/plain and text/html.
	msg_error = MIMEText(text_Exception, 'plain')
	# Attach parts into message container.
	msg_exception.attach(msg_error)
	# sendmail function takes 3 arguments: sender's address, recipient's address
	# and message to send - here it is sent as one string.
	print "\n Sending email from:" , sender, "to: " , recipient1
	session.sendmail(sender, recipient1, msg_exception.as_string())
	session.quit()
	
