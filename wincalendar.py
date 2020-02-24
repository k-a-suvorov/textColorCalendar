#Import standart modules

import datetime
import calendar
import os

#prepare to work with the colors of windows console
from ctypes import *
windll.Kernel32.GetStdHandle.restype = c_ulong
h = windll.Kernel32.GetStdHandle(c_ulong(0xfffffff5))

#functions of color text in to the Windows console

def color(c): #setconsoletextcolor
	windll.Kernel32.SetConsoleTextAttribute(h,c)

def colorLine(c, s): #Win color text
	#os.system("cls")
	color(c)
	print("*" * (len(s) +2))
	print(" " + s)
	print("*" * (len(s) +2))

# main program
try:
	now = datetime.datetime.now()
	c = calendar.TextCalendar(calendar.MONDAY) #Set first day as Monday
	n = ''


#Fantion of starting Program
	def run():
		startCalendar()


#Fantion of starting Calendar
	def startCalendar():
		switch = True
		color(11)
		start = int(input('Type \" 1\" To use the Calendar.\n \ " 2\" - to exit the program:'))
		if (start < 1 or start > 2):
			run()
		elif (start == 2):
			colorLine(12, 'Goodbye!')
			switch = False
		elif (start == 1):
			os.system("cls")
			calendarick()		


#Main cycle of Calendar		
	def calendarick():
		color(14)	
		h = int(input('Enter the year starting from zero N. E.:'))
		n = int(input('Enter the month number:'))
		if ((h < 0) and (n < 0 or n > 12)):
			colorLine(12, 'In the program, the year should start from zero Ad!')
			run()
		else:	
			month = c.formatmonth(h, n)
			colorLine(13, 'Current time: \n')
			colorLine(2, now.strftime("%d-%m-%Y"))
			print("\n")
			color(14)
			print(month)
			color(11)
			print('Would you like to see a different year and month?')
			
			startCalendar()
			os.system("cls")

#Initialize program			
	run()	
except ValueError:
    print("You have some mistake of userinput Value!")
except TypeError:
   print("You have some mistake of type Value!")
except SystemError:
	print("This is system mistake! Please don't panic! Relax!" )
except ArithmeticError:
	print("Arithmetic operations was broken!")
except ImportError:
	print("Some modules not loaded, please check your source code!")
