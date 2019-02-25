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


sender = 'Silicon_Solution_QA@litepoint.com' #Email id used to send out notifications from the server
server = '192.168.2.199' # Ip address of litepoint email server
recipient1='vishal.sawant@litepoint.com'
Multiple_recipients = False
# Email notification for starting package installation, sent to station owner and jian :
# Send the message via local SMTP server.
session = smtplib.SMTP(server)
# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')

msg['From'] = sender

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

# Email notification for PKG installation done and QA is started :
# Send the message via local SMTP server.
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
print "\n Sending email from:" , sender, "to: " , recipient1
session.sendmail(sender, recipient1, msg_2.as_string())
session.quit()	
# Email notification for QA done :
# Send the message via local SMTP server.
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
		
		