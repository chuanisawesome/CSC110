#Assignment_1

def main():
    x = eval(input("What is the Reciprocal and Square Value? "))
    #Calculate Reciprocal and store it in y
    y = 1 / x
    #Calculate Square and store it in z
    z = x**2
    #Convert int x to str store in value
    value = str(x)
    print("The reciprocal of " + value + " is", y)
    print("Squared " + value + " is", z)

main()
