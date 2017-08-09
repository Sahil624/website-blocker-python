import time
from datetime import datetime as dt

host_file='hosts'
host_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website=['www.facebook.com','facebook.com','web.whatsapp.com','www.web.whatsapp.com','in.yahoo.com','www.in.yahoo.com']

while True:
    print(dt.now())
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("working")
        with open(host_path,'r+') as file:
            content=file.read()
            for websites in website:
                if websites in content:
                    pass
                else:
                    file.write(redirect +" "+websites+"\n")
    else:
        with open(host_path,'r+') as file1:
            content1=file1.readlines()
            file1.seek(0)
            for line in content1 :
                if not any(websites in line for websites in website):
                    file1.write(line)
            file1.truncate()        
        print("fun hrs")
    time.sleep(5)
