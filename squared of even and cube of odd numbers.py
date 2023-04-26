# Ray Allessandra D. Pacis | BSCPE 1-5
# Write a method in python that will create two separate text files after reading the source text file named integers.txt that contains 20 integers. 
# The first output file will be named double.txt containing the square of all even integers found in integers.txt.
# The second file will be named triple.txt containing the cube of all odd numbers found in the integers.txt.

# open files integers.txt, double.txt, and triple.txt
with open("integers.txt", 'w') as input_file, open("double.txt", 'w') as even_squared, open("triple.txt", 'w') as odd_cube:

    # create loop
    i = 0
    while (i < 20):
        # ask user for numbers
        user_numbers = input("Please write a number: ")
        # put the numbers to integers.txt
        input_file.write((user_numbers) + '\n')
        i += 1

    # read integers.txt by line
    for line in input_file:
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

# end of program