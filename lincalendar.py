#Import standart modules
import datetime
import calendar
import sys
import os

#prepare to work with the colors of unix console
import colorama
from colorama import Fore, Back, Style
colorama.init()

# main program
try:
	now = datetime.datetime.now()
	c = calendar.TextCalendar(calendar.MONDAY) #Set first day as Mond
	n = ''
	switch = True

#Fantion of starting Program
	def run():
		startCalendar()

#Fantion of starting Calendar
	def startCalendar():
		switch = True
		start = int(input(Fore.CYAN + 'Type \" 1\" To use the Calendar.\n \ " 2\" - to exit the program:'))
		if (start < 1 or start > 2):
			run()
		elif (start == 2):
			print(Fore.RED + 'Goodbye!')
			switch = False
		elif (start == 1):
			os.system('clear')
			calendarick()			


#Main cycle of Calendar					
	def calendarick():
				
		h = int(input('Enter the year starting from zero N. E.:'))
		n = int(input('Enter the month number:'))
		if ((h < 0) and (n < 0 or n > 12)):
			print(Fore.RED + 'In the program, the year should start from zero Ad!')
			run()
		else:	
			month = c.formatmonth(h, n)
			print(Fore.MAGENTA + 'Current time: \n')
			print()
			print(now.strftime(Fore.GREEN + "%d-%m-%Y"))
			print()
			print(Fore.YELLOW + month)
				
			print(Fore.CYAN + 'Would you like to see a different year and month?')
					
			startCalendar()
			
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
