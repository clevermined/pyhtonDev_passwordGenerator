import random 
import string 
import io 
import os
import sys
   
def getCode( char = string.ascii_uppercase + string.digits + string.ascii_lowercase + string.punctuation):
    try:
        passWordLength = int(input("Define The Password Length With An Integer Value: "))
        crtPass = "".join(random.choice(char) for x in range(passWordLength))
         
        """open file for password logging"""
        fileStore_password = open('fileStore_passwordLOG','a')
        fileStore_password.writelines(crtPass + '\n' )
      
        print("Generated Password: " ,crtPass)
      
    except TypeError:
        print("Incorrect parameter: exception_TypeError")


"""
This is a Alphanumeric Password Genarator
it is default setting is for 10 characters
you can enter the any other length you desire.
"""
      
