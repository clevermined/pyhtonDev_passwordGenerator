import random 
import string
import io
import sys
import smtplib
from email.mime.text import MIMEText
from time import asctime

time_stamp = asctime()
logFile_password = 'fileStore_passwordLOG'

def getCode( char = string.ascii_uppercase + string.digits 
        + string.ascii_lowercase + string.punctuation):
    try:
      passWordLength = int(input("Select Password Length With An Integer Value: "))
      crtPass = "".join(random.choice(char) for x in range(passWordLength))
    except NameError:
      print("A Numermic Interger Value is Required To Process This Request: ")
      sys.exit(main())
      
    try:
      fileStore_password.writelines(time_stamp + '\t' + crtPass + '\n' )
      print(time_stamp, "__PASSWORD GENERATED__")
    except TypeError:
        print("Incorrect parameter: exception_TypeError")
    return()
   
def sendMail():
    fp = open(logFile_password,'r')
    msg = MIMEText(fp.read())
    fp.close()

    msg['SUBJECT']  = 'File %s' % logFile_password
    msg['From'] = 'localhost.local.domain'
    msg['To'] = 'localhost.local.domain'

    smtpObject = smtplib.SMTP('localhost')
    smtpObject.sendmail('sender',['receiver'],msg.as_string())
    smtpObject.quit()

def main():
    getCode()
    sendMail()

if __name__ == '__main__':
    main()

"""
This is a Alphanumeric Password Genarator.
The default behavioral setting is for password length of 10 characters.
This default behavior is both overridable and user definable.
You can enter the any other length you desire.
<<<<<<< HEAD
=======
>>>>>>> c9311fd0520ee5d9c8d180fb2347f6d16361551a


def main():
	getCode()

if __name__ == '__main__':
	main()      

>>>>>>> 28f730baf2a46b786f9e169cbadeee0aa0f0a4e7
"""
