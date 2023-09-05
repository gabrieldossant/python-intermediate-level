import os 
import math 
import random

def main():
    print(
        '____________________________________________________\n'
        '|                                                  |\n'
        '|          W O R L D  1  /  P Y T H O N  3         |\n'
        '|__________________________________________________|\n'
        '|                                                  |\n'
        '|          A L L   T H E   P R O J E C T S         |\n'
        '|                                                  |\n'
        '|        [01] 001          |       [02] 002        |\n'
        '|        [03] 003          |       [04] 004        |\n'
        '|        [05] 005          |       [06] 006        |\n'
        '|        [07] 007          |       [08] 008        |\n'
        '|        [09] 009          |       [10] 010        |\n'
        '|        [11] 011          |       [12] 012        |\n'
        '|        [13] 013          |       [14] 014        |\n'
        '|        [15] 015          |       [16] 016        |\n'
        '|        [17] 017          |       [18] 018        |\n'
        '|        [19] 091          |       [20] 020        |\n'
        '|        [21] 021          |       [22] 022        |\n'
        '|        [23] 023          |       [24] 024        |\n'
        '|        [25] 025          |       [26] 026        |\n'
        '|        [27] 027          |       [28] 028        |\n'
        '|        [29] 029          |       [30] 030        |\n'
        '|        [31] 031          |       [32] 032        |\n'
        '|        [33] 033          |       [34] 034        |\n'
        '|                                                  |'
    )
    c = int(input('| Enter : '))
    if c == 1:
        print("\n" * os.get_terminal_size().lines)
        name = input("Enter your name: ")
        print("É um prazer te conhecer {}!".format(name))
        goBackMain()
    elif c == 2:
        print("\n" * os.get_terminal_size().lines)
        n1 = float(input('Type a number: '))
        n2 = float(input('Type another number: '))
        print(n1 + n2)
        goBackMain()
    elif c == 3:
        print("\n" * os.get_terminal_size().lines)
        var = input("Type anything: ")
        print("The type of this value is ", type(var))
        print("Is there only space? ", var.isspace())
        print("Is it a number? ", var.isnumeric())
        print("Is it alphabetical? ", var.isalpha())
        print("Is it alphanumeric? ", var.isalnum())
        print("Is it upper? ", var.isupper())
        print("Is it lower? ", var.islower())
        print("Is it capitalized? ", var.istitle())
        goBackMain()
    elif c == 4:
        print("\n" * os.get_terminal_size().lines)


    elif c == 5:
        print("\n" * os.get_terminal_size().lines)
        # Arithmetical operations

        n1 = int(input('Type a number: ')) # User input
        n2 = int(input('Type another number: ')) # User input
        s = n1 + n2 # Calculate a sum
        m = n1 * n2 # Calculate the multiplication
        d = n1 / n2 # Calculate the division
        di = n1 // n2 # Calculate the integer division
        e = n1 ** n2 # Calculate the exponentiation
        print('Sum = {}, the product is {}, and the division is {:.2f}'.format(s, m, d), end=' ') # Printout to show the results of sum, mult and div
        print('Intereger division {} and pontecy {}'.format(di, e)) # Printout to show the results of integer division and the exponentiation
        goBackMain()

    elif c == 6:
        print("\n" * os.get_terminal_size().lines)
        # Create a program in which the user types in a number and it 
        # shows the predecessor and successor of this number. 

        num = int(input('Enter any number: ')) # User input
        print('The successor of this number is {}'.format(num+1), end=' ') 
        print('The predecessor of this number is {}'.format(num-1))
        goBackMain()

    elif c == 7:
        print("\n" * os.get_terminal_size().lines)
        # Create an algorithm that reads a number and shows its double, triple and square root

        n = int(input('Enter a number: '))
        print('Double: {}'.format(n*2))
        print('Triple: {}'.format(n*3))
        print('Square root: {:.2f}'.format(n**(1/2)))
        goBackMain()

    elif c == 8:
        print("\n" * os.get_terminal_size().lines)
        # Arithmetic average of two grades

        n1 = float(input('Type your first grade: '))
        n2 = float(input('Type your second grade: '))
        print('The average is {}'.format((n1+n2)/2))
        goBackMain()

    elif c == 9:
        print("\n" * os.get_terminal_size().lines)
        # Write a program that reads a value in meters and displays it 
        # converted into centimeters and millimeters.

        n = float(input('Enter a number in metros and see the conversion into centimeters and millimeters a number: '))
        print('Cm: {}'.format(n * 100))
        print('Mm: {}'.format(n * 1000))
        goBackMain()

    elif c == 10:
        print("\n" * os.get_terminal_size().lines)
        # Multiplication table

        n = int(input('Enter a number to see the multiplication table: ')) # User input

        for i in range (1, 11): # Repetition structure to calculate the multiplication table
            print('{} x {} = {}'.format(n, i , n*i)) # Print to show the results

        goBackMain()

    elif c == 11:
        # Make a program that calculates the area and height of a wall and shows 
        # the amount of paint required to paint the wall

        print("\n" * os.get_terminal_size().lines)
        height = float(input('Enter the wall height: '))
        width = float(input('Enter the wall width: '))
        area = width * height
        ink = area/2
        print('Your wall has a dimension of : {}x{} and your area is : {}m²'.format(height, width, area))
        print('Paint required : {:.2f}'.format(ink))
        goBackMain()

    elif c == 12:
        # Make a program that reads the value of a product and prints the result with a 5 percent discount

        print("\n" * os.get_terminal_size().lines)
        product = float(input('Enter the value of a product: '))
        disc = (product * 5)/100
        print('The product discount is : {:.2f}'.format(disc))
        print('The final value of the product is : {:.2f}'.format(product - disc))
        goBackMain()

    elif c == 13: 
        # Calculate a 10% salary increase

        print("\n" * os.get_terminal_size().lines)
        salary = float(input('Enter the value of your salary: '))
        increase = salary/0.15
        print("Your new salary will be {}".format(salary + increase ))
        goBackMain()

    elif c == 14:
        # Make a conversion from Celcius to Fahrenheit

        print("\n" * os.get_terminal_size().lines)
        c = float(input('Enter the value in celsius: '))
        f = ((9*c)/5)+35
        print('The temperature converted from Celsius {:.2f} to Fire {:.2f}'.format(c, f))
        goBackMain()

    elif c == 15:
        # Calculate the days and kilometers traveled to find out the rental price

        print("\n" * os.get_terminal_size().lines)
        days = float(input('How many days rent? '))
        km = float(input('How many Km driven? '))
        pay = (days * 60) + (km * 0.15)
        print('The total rent payable is : R$ {}'.format(pay))
        goBackMain()

    elif c == 16: 
        # Round a number to integer

        print("\n" * os.get_terminal_size().lines)
        num = float(input('Enter a number: '))
        print('The number typed is {}'.format(num))
        print('The number around is {}'.format(int(num)))
        goBackMain()

    elif c == 17:
        # Calculate the opposite and adjacent to find hipotenusa 

        print("\n" * os.get_terminal_size().lines)
        opposite = float(input('Enter the opposite cateto: '))
        adjacent = float(input('Enter the adjacent cateto: '))
        hypotenuse = math.sqrt(pow(opposite, 2) + pow(adjacent, 2))
        print('The Hypotenuse is {:.2f}'.format((hypotenuse)))
        goBackMain()

    elif c == 18:
        # Calculate the seno, coseno and tangente of an angle.

        print("\n" * os.get_terminal_size().lines)
        angle = float(input('Enter the angle: '))
        seno = math.sin(math.radians(angle))
        coseno = math.cos(math.radians(angle))
        tangente = math.tan(math.radians(angle))
        print('Seno: {:.2f}\nCoseno: {:.2f}\nTangente: {:.2f}\n'.format(seno, coseno, tangente))
        goBackMain()

    elif c == 19:
        # Guess names

        print("\n" * os.get_terminal_size().lines)
        names = ['Rebeca', 'Lucas', 'Gabriel', 'Mateus', 'Thiago']
        print(names)
        guess = random.randint(0, 4)
        print('The person drawn is {}'.format(names[guess]))
        goBackMain()

    elif c == 20:
        # Organize the order of presentation

        print("\n" * os.get_terminal_size().lines)
        namesOrder = []
        names = ['Rebeca', 'Lucas', 'Gabriel', 'Mateus', 'Thiago']
        print(names)
        for i in range(len(names)):
            guess = random.randint(0, 4)
            namesOrder.append()
            print(namesOrder)

    elif c == 21:
        print("\n" * os.get_terminal_size().lines)

    elif c == 22:
        print("\n" * os.get_terminal_size().lines)

    elif c == 23:
        print("\n" * os.get_terminal_size().lines)

    elif c == 24:
        print("\n" * os.get_terminal_size().lines)

    elif c == 25:
        print("\n" * os.get_terminal_size().lines)

    elif c == 26:
        print("\n" * os.get_terminal_size().lines)

    elif c == 27:
        print("\n" * os.get_terminal_size().lines)

    elif c == 28: 
        print("\n" * os.get_terminal_size().lines)

    elif c == 29:
        print("\n" * os.get_terminal_size().lines)

    elif c == 30:
        print("\n" * os.get_terminal_size().lines)

    elif c == 31:
        print("\n" * os.get_terminal_size().lines)

    elif c == 32:
        print("\n" * os.get_terminal_size().lines)

    elif c == 33:
        print("\n" * os.get_terminal_size().lines)

    elif c == 34:
        print("\n" * os.get_terminal_size().lines)

    elif c == 35:
        print("\n" * os.get_terminal_size().lines)

    else:
        print("Ta errado ta ligado parça")

def goBackMain():
    r = input('| Do you want to see more projects? [Y]/[N]: ')
    if r.upper()[0] == "Y":
        print("\n" * os.get_terminal_size().lines)
        main()
    elif r.upper()[0] == "N":
        print("\n" * os.get_terminal_size().lines)
        print(' Closing . . .')
        exit()    
    else:
        errorCaracter()

def errorCaracter():
    print("\n" * os.get_terminal_size().lines)
    print(
        '____________________________________________________\n'
        '|                                                  |\n'    
        '|     T Y P E   O N L Y     [ Y ]   O R   [ N ]    |\n'
        '|__________________________________________________|\n'
    )
    goBackMain()


main()

