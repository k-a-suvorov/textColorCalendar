import datetime
import calendar
import sys
import os
import colorama
from colorama import Fore, Back, Style
colorama.init()

try:
	now = datetime.datetime.now()
	c = calendar.TextCalendar(calendar.MONDAY)
	n = ''
	switch = True



	def run():
		startCalendar()


	def startCalendar():
		switch = True
		start = int(input(Fore.CYAN + 'Наберите \"1\" Чтобы использовать Календарь.\n \"2\" - для выхода из программы: '))
		if (start < 1 or start > 2):
			run()
		elif (start == 2):
			print(Fore.RED + 'До свидания!')
			switch = False
		elif (start == 1):
			os.system('clear')
			calendarick()			

			
	def calendarick():
				
		h = int(input('Введите год, начиная с нулевого Н.Э.: '))
		n = int(input('Введите номер месяца: '))
		if ((h < 0) and (n < 0 or n > 12)):
			print(Fore.RED + 'В программе год должен начинаться с нулевого Нашей Эры!')
			run()
		else:	
			month = c.formatmonth(h, n)
			print(Fore.MAGENTA + 'Текущее время: ')
			print()
			print(now.strftime(Fore.GREEN + "%d-%m-%Y"))
			print()
			print(Fore.YELLOW + month)
				
			print(Fore.CYAN + 'Желаете посмотреть другой год и месяц?')
					
			startCalendar()
			

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
