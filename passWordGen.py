import random, string, io, sys
from time import asctime
import smtplib
from email.mime.text import MIMEText

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

    try:		#open file for password logging
      fileStore_password = open(logFile_password,'a')
      fileStore_password.writelines(time_stamp + '\t' + crtPass + '\n' )
      print(time_stamp, "__PASSWORD GENERATED__")
    except TypeError:
        print("Incorrect parameter: exception_TypeError")
   
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
"""
      
