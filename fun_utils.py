import os 
import datetime

command = "df -h"
command = "uptime"
command = "date"


def check_cpu(command):
     print(os.system(command))
    
check_cpu("df -h")

def check_uptime(command):
     print(os.system(command))

check_uptime("uptime")

def check_date(command):
     print(os.system(command))
check_date("date")

def check_ram(command):
     print(os.system(command))
check_ram("free -h")










#defining functions
def run_command(command):  #
     return os.system(command)


def show_date(): #define kiya function ko
     return datetime.datetime.today()

#run_command("date")
#run_command("df -h")

today = show_date()
print(today)



