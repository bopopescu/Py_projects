# our top level script
import os
import sys
import copy
import shutil
import Run_PKG_Installation


import distutils.core
import sched
import time
import mysql.connector
import traceback
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 

print "\n ----INFO: Start QA - TEST..."
time.sleep(1)
print "\n ---- End of Sleep"

#Establish connection to the database
# Change hostname(usually localhost), port (default=3306), username, password and name of the database based on your database and table name
db = mysql.connector.connect(host="IQ-auto-build ", port="3306", user="lp_client", passwd="lp", db="iqautobuild") 

#Create cursor object to the database. It will let you execute all the query you need
cur = db.cursor() 
        
##ID int(10) unsigned_NO
##projectName varchar(100)_NO
##ReleaseVersion varchar(45)_NO
##Test varchar(45)_NO

Project_Name = "IQfact+_QCA_6174"
ID_1 = 15026

#UPDATE_query = ("UPDATE buildresults SET Test = '1' WHERE ID = %s" )
UPDATE_query = ("UPDATE buildresults SET Test = '0' WHERE ID != %s" )
cur.execute(UPDATE_query, (ID_1, ))
db.commit()


##SELECT_query = ("SELECT Test, projectName, ReleaseVersion, RevisionNumber,buildType,buildConfig,buildResult,dateTime,ID,svnBranchName1 from buildresults  \
##where projectName=%s AND ID =%s ORDER BY dateTime DESC LIMIT 5")
##cur.execute(SELECT_query, (Project_Name, ID_1 )  )


SELECT_query = ("SELECT Test, projectName, ReleaseVersion, RevisionNumber,buildType,buildConfig,buildResult,dateTime,ID,svnBranchName1 from buildresults  \
where projectName=%s AND TEST = '1' ORDER BY dateTime DESC LIMIT 15")
cur.execute(SELECT_query, (Project_Name,  )  )

data = cur.fetchall() #Store the result set

# if loop, checking if new package is detected
print os.getcwd()
#os.system('dir c:')
if data :
		print "\n----- Success, New package detected!!"
		# if package is ready, start QA and set flag: QA_is_running = True
		QA_is_running = True
		New_Package_Installation = True
		
		# Store the package_name
		for row in data :
		    print "Test: "+row[0]+' ' +row[1]+' ReleaseV: '+row[2]+ ' Revision#: ' +str(row[3])+ " " +'__' +str(row[4])+ " "+ str(row[5])
		    print str(row[6])+ " "+ str(row[7])+ " "+ str(row[8])
##		    os.system('pause')
		    print str(row[9])
		    print "\n"
		    
#os.system('pause')		
