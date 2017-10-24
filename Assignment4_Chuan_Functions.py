#Assignment_4 Functions

# Function that modifies the list by squaring each entry
def squareEach(num):
    x = 0

# Loops 
    for i in num:

# Square formula
        num[x] = i**2
        x = x + 1   

# Sums the list of numbers
def sumList(num):
    sum = 0
    for i in num:
        sum = sum + i

# Returns the sum of the numbers in the list
    return sum

# Function list of strings
def toNumbers(num):
    x = 0
    for i in num:

# Modifies each entry in the list by converting it to a number
        num[x] = int(i)
        x = x + 1

def main():
    print("This program will help you compute the sum of the square of numbers read from a file.")
    file = input("Please enter a  file name: ")

    infile = open(file, 'r')


    num = []
    for i in infile:
        num.append(i[:-1])

# Calls the functions
    toNumbers(num)
    squareEach(num)
    total = sumList(num)

    print('\nTotal sum of numbers from file "{0}" is {1}.'.format(file,total))

    infile.close()
   
main()

