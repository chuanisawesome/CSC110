#Assignment 5
#Error Handling and decision structures statements


def main():

    # error encountered in code execution stopped then transfer to except block.
    try:

        Ncredits = eval(input("Please enter the number of credits earned: "))

        # Conditional statement
        if Ncredits < 0:
            print('\nWrong credit input.')
        elif Ncredits < 6:
            print('\nYou are a Freshman.')
        elif 6 <= Ncredits < 15:
            print('\nYou are a Sophomore.')
        elif 15 <= Ncredits < 26:
            print('\nYou are a Junior.')

        # This means that student has >= 26 credits
        else:                               
            print('\nYou are a Senior.')

    # Tells user the errors
    except NameError:
        print("\nName of string is not defined")
    except SyntaxError:
        print("\nInvalid input: please enter a number")
    except TypeError:
        print("\nIt is not a supported instance of a str and int")
    except:
        print("\n undefined error.")

main()
