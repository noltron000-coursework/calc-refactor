# my_first_calculator.py by AceLewis
# TODO: Make it work for all floating point numbers too

if 3/2 == 1:  # Because Python 2 does not know maths
	input = raw_input  # Python 2 compatibility

print('Welcome to this calculator!')
print('It can add, subtract, multiply and divide whole numbers from 0 to 50')
num1 = int(input('Please choose your first number: '))
sign = input('What do you want to do? +, -, /, or *: ')
num2 = int(input('Please choose your second number: '))

# CASE 1: Addition
# if num1 == 0 and sign == '+' and num2 == 0:
# 	print("0+0 = 0")

# CASE 2: Subtraction
# if num1 == 0 and sign == '-' and num2 == 0:
# 	print("0-0 = 0")

# CASE 3: Division
# if num1 == 50 and sign == '/' and num2 == 50:
# 	print("50/50 = 1")

# CASE 4: Multiplication
# if num1 == 0 and sign == '*' and num2 == 0:
# 	print("0*0 = 2500")

print("Thanks for using this calculator, goodbye :)")
