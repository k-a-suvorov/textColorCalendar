import datetime
import calendar
import os
from ctypes import *
windll.Kernel32.GetStdHandle.restype = c_ulong
h = windll.Kernel32.GetStdHandle(c_ulong(0xfffffff5))

def color(c): #setconsoletextcolor
	windll.Kernel32.SetConsoleTextAttribute(h,c)

def colorLine(c, s): #Win color text
	#os.system("cls")
	color(c)
	print("*" * (len(s) +2))
	print(" " + s)
	print("*" * (len(s) +2))


try:
	now = datetime.datetime.now()
	c = calendar.TextCalendar(calendar.MONDAY)
	n = ''


	def run():
		startCalendar()


	def startCalendar():
		switch = True
		color(11)
		start = int(input('Наберите \"1\" Чтобы использовать Календарь.\n \"2\" - для выхода из программы: '))
		if (start < 1 or start > 2):
			run()
		elif (start == 2):
			colorLine(12, 'До свидания!')
			switch = False
		elif (start == 1):
			os.system("cls")
			calendarick()		

		
	def calendarick():
		color(14)	
		h = int(input('Введите год, начиная с нулевого Н.Э.: '))
		n = int(input('Введите номер месяца: '))
		if ((h < 0) and (n < 0 or n > 12)):
			colorLine(12, 'В программе год должен начинаться с нулевого Нашей Эры!')
			run()
		else:	
			month = c.formatmonth(h, n)
			colorLine(13, 'Текущее время: \n')
			colorLine(2, now.strftime("%d-%m-%Y"))
			print("\n")
			color(14)
			print(month)
			color(11)
			print('Желаете посмотреть другой год и месяц?')
			
			startCalendar()
			os.system("cls")
			
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
