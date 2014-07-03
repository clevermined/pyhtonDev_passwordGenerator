import gPasswordGen
import time

print ('''Welcome,
          We hope this tool will help you keep your files and or accounts
          more secure by generating better passwords''' + '\n') 
time.sleep(1)
print (gPasswordGen.getCode())

if __name__ == '__main__':
   main()
