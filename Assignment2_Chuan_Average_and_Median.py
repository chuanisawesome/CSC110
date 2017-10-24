#Assignment_2 Finding Average and Median

def main():
    print("You can calculate the average and the median\n")

    #Prompting the first variable
    number_of_numbers = int(eval(input("How many numbers do you have? (Odd numbers only!): ")))

    #Creating an empty list for the second variable
    my_list = list ()

    #sorts list from least to greatest
    my_list = sorted(my_list)

    print("Enter the numbers that you would want to sum then hit ENTER\n")
    
    #For the third varible (loop)
    average = 0

    #duplicates the input to determine when the loop starts
    for i in range(number_of_numbers):
        number = float(eval(input("Enter a number >> ")))

        #average formula
        average = average + number / number_of_numbers
        my_list.append(number)

    print()
    #States the sum of the numbers
    print("The sum is ", my_list , " is: ", sum(my_list))

    #States the average
    print("The average is: ", average)

    #Median formula
    median = my_list[(number_of_numbers - 1) // 2]

    #States the median
    print("The median is: ", median)
main()
