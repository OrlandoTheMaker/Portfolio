from colorama import *
import colorama
from pyfiglet import *
import pyfiglet
import sys,os,time
import random
###        ##      ##
r=Fore.RED
b=Fore.BLUE
c=Fore.CYAN
rs=Fore.RESET
g=Fore.GREEN
y=Fore.YELLOW
colors=[r,b,c,rs,g,y]
info=g+'['+rs+'!'+g+']'+rs
error=r+'['+rs+'xx'+r+']'+rs
success=g+'['+y+'$$'+g+']'+rs
###   ###    ###  ###
def c_banner():
	f=pyfiglet.Figlet(font="slant")
	logo=f.renderText("BINCOM")
	print(random.choice(colors)+logo)
	print("author: xxxx JEREMIAH ABDULSALAM (A.K.A Orlando(O.D.O) xxxx")
c_banner()
def kill():
	time.sleep(2)
def cls():
	os.system("clear")
##                 ##              ##
opts={
1:'RED',
2:'BLUE',
3:'CYAN',
4:'RESET',
5:'GREEN',
6:'YELLOW',
7:'LET ME PICK FOR YOU(random choice)',8:' Q U I T  T H E  CONSOLE ',
}
##                ##                 ##
def option1():
	print("Red outfit for tommorrow")
	print(r+"""
	========
	# o   o #
	#   o   #
	========
	"""+rs)
	time.sleep(3)
	cls()
	os.system("python home.py")	
def option2():
	print("Blue outfit fot tommorrow")
	print(b+"""
	========
	# o   o #
	#   o   #
	========
	"""+rs)
	time.sleep(3)
	cls()
	os.system("python home.py")		
def option3():
	print("Cyan outfit for tommorrow!")
	print(c+"""
	========
	# o   o #
	#   o   #
	========
	"""+rs)
	time.sleep(3)
	cls()
	os.system("python home.py")		
def option4():
	print("I REALLY CAN'T TELL HOW THIS COLOUR LOOKS LIKE. WHITE?")
	print(rs+"""
	========
	# o   o #
	#   o   #
	========
	"""+rs)
	time.sleep(3)
	cls()
	os.system("python home.py")		
def option5():
	print("Green outfit for tommorrow")
	print(g+"""
	========
	# o   o #
	#   o   #
	========
	"""+rs)
	time.sleep(3)
	cls()
	os.system("python home.py")		
def option6():
	print("Yellow outfit for tommorrow")
	print(y+"""
	========
	# o   o #
	#   o   #
	========
	"""+rs)
	time.sleep(3)
	cls()
	os.system("python home.py")		
def option7():
	kill()
	cls()
	t=pyfiglet.Figlet(font="slant")
	chosen1=t.renderText("RANDOM")
	print(random.choice(colors)+chosen1)
	print("\n")
	print(success+"success! "+"A randomized option has been chosen for you BOSS!")
	time.sleep(3)
	kill()
	cls()
	os.system("python home.py")
def ext():
	cls()
	print(info+" Exiting the console..." +rs)
	kill()
	sys.exit()	
##               ###            ##
def nl():
	print("\n")
nl()
##         ##         . ##
print(info+"THESE ARE THE AVAILABLE COLOURS BOSS!")	
for keys in opts.keys():
	print(keys,':',opts[keys])
##                   ##                  ##
function1=int(input(info+"HOW WOULD YOU LIKE TO SELECT TOMORROW'S OUTFIT BOSS? : "))
##       ##                 ##
if function1 == 1:
	option1()
elif function1 == 2:
	option2()
elif function1 == 3:
	option3()
elif function1 == 4:
	option4()
elif function1 == 5:
	option5()
elif function1 == 6:
	option6()
elif function1 == 7:
	option7()
elif function1 == 8:
	ext()
else:
	print(error+"Wrong Option!! input must be single and < 7")
	kill()
	cls()
	os.system("python home.py")
	
	
	