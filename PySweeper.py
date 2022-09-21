import os

IP = input("[+] Enter the Host IP Address:\t")
print("[+] Starting Ping Sweeper on " + IP)
dot = IP.rfind(".")
IP = IP[0:dot + 1]

for i in range(0, 30):
    host = IP + str(i)
    #For Linux hosts replace -n with -c and path to "/dev/null"
    response = os.system("ping -n 1 -w 1 " + host + " >nul")
 
    if response == 0:
        print(host + " is up")
    else:
        print(host + " is down")