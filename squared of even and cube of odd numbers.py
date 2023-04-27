# Ray Allessandra D. Pacis | BSCPE 1-5
# Write a method in python that will create two separate text files after reading the source text file named integers.txt that contains 20 integers. 
# The first output file will be named double.txt containing the square of all even integers found in integers.txt.
# The second file will be named triple.txt containing the cube of all odd numbers found in the integers.txt.

# import modules for design
import pyfiglet
from termcolor import colored, cprint
print_magenta = lambda x: cprint(x, 'magenta')
import time
from colorama import Fore, Back, Style


# intro
hi_welcome = pyfiglet.figlet_format('\n' + "Welcome User!", font = "doom", width = 150, justify = "center")
print_magenta(hi_welcome)
print(Style.RESET_ALL)
print(Fore.BLUE + "="*150)
print(Style.RESET_ALL)
instruction = "INSTRUCTION: Please enter 20 random integers and if it's even I will square it, and if it's odd I'll cube it.☺"
instruction_center = instruction.center(150)
print(instruction_center)
print('\n' + Fore.BLUE + "="*150)
print(Style.RESET_ALL)

# open file integers.txt(write)
with open("integers.txt", 'w') as input_file:

    # create loop
    i = 0
    while (i < 20):
        # ask user for numbers
        user_numbers = input('\033[1;35m' + "\t\tPlease write a number: \033[0m")
        # put the numbers to integers.txt
        input_file.write((user_numbers) + '\n')
        i += 1

# open files integers.txt(read), double.txt(write), and triple.txt(write)
with open("integers.txt", 'r') as integers_file, open("double.txt", 'w') as even_squared, open("triple.txt", 'w') as odd_cube:
    # read integers.txt by line
    for line in integers_file:
        user_num = int(line)
            
        # if extracted number is even
        if user_num % 2 == 0:
            # extracted number will be squared
            squared_number = user_num ** 2
            # write squared number to double.txt
            even_squared.write(str(squared_number) + '\n')

        # else if the extracted number is odd
        if user_num % 2 == 1:
            # extracted number will be cubed
            cubed_number = user_num ** 3
            # write cubed number to triple.txt
            odd_cube.write(str(cubed_number) + '\n')

print(input("\nPress enter to continue..."))

print('\n' + Fore.BLUE + "-"*150)
print('\nLOADING DATA. Please wait...')
time.sleep(2)

# open files integers.txt(read), double.txt(write), and triple.txt(write)
with open("integers.txt") as integers_file1, open("double.txt") as even_squared1, open("triple.txt") as odd_cube1:
    # read integers.txt by line
    user_num1 = [int(line) for line in integers_file1.read().split()]
    # show user the numbers they entered
    print(Fore.LIGHTBLUE_EX + "\n\n\tCHOSEN NUMBERS: " + Style.RESET_ALL, user_num1)
    time.sleep(1)

    # read double.txt by line
    num_squared = [int(line) for line in even_squared1.read().split()]
    # show user squared even numbers 
    print(Fore.LIGHTBLUE_EX + "\n\n\tSQUARED EVEN NUMBERS: " + Style.RESET_ALL, num_squared)
    time.sleep(1)

    # read triple.txt by line
    num_cubed = [int(line) for line in odd_cube1.read().split()]
    # show user cubed odd numbers
    print(Fore.LIGHTBLUE_EX + "\n\n\tCUBED ODD NUMBERS: " + Style.RESET_ALL, num_cubed)
    time.sleep(3)

# outro
print('\n' + Fore.BLUE + Style.BRIGHT + "-"*150)
done = pyfiglet.figlet_format("Thank you!", font = 'doom', width = 150, justify = 'center')
print_magenta(done)
note = "See text files"
print(Fore.BLUE + '-'*69 + Style.RESET_ALL + note + Fore.BLUE + '-'*69 + '\n') 

# end of program