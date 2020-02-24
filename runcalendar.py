# Import standart modules

import os
import sys

# main cycle
try:
	switch = True
	
	#detect unix-like or windows-like system
	if (os.name == 'posix'):
		os.system('python3 lincalendar.py')
	elif (os.name == 'nt'):
		os.system('python3 wincalendar.py')
	else:
		print('This OS in not supported!')		
		switch = False
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
