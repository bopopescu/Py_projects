# Import smtplib for the actual sending function
import smtplib

# Create a text/plain message
msg = 'this istest'
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

COMMASPACE = ', '

# Create the container (outer) email message.
msg = MIMEMultipart()

me = 'Silicon_Solution_QA@litepoint.com' 
you = 'jian.sun@litepoint.com'
msg['Subject'] = 'QA Finished on your project'
msg['From'] = 'Silicon_Solution_QA@litepoint.com' 
msg['To'] = 'jian.sun@litepoint.com'


# Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP('192.168.2.199')
s.sendmail(me, [you], msg.as_string())
s.quit()
print ("done sending")