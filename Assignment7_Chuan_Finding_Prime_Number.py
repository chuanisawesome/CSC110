#Assignment 7 Finding Prime Number

def find_primes():
    valuePrime = eval(input("Enter a value to look for the prime numbers: "))

    # Empty List
    allNumbers = []
    primeNumbers = []
    
    for i in range(2,valuePrime+1):
        allNumbers.append(i)


    # Go through list
    while len(allNumbers)>0:

        # Prints and removes
        firstPrime = allNumbers.pop(0)

        #add primes to list since they were popped from allNumbers
        primeNumbers.append(firstPrime)
                                
        print(firstPrime, "is a prime number.")

        # Remove multiples
        for aNum in allNumbers:
            # If aNum is a multiple of firstPrime
            if aNum % firstPrime == 0:  
                allNumbers.remove(aNum)
                
    return primeNumbers

def main():
    list_test = find_primes()
    print(list_test)
                   
main()
