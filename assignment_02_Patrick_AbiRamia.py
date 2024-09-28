
##############
# EXERCISE 1 #
##############

# Write a function that takes an integer from the user and calculates its factorial, (The
# factorial of a non-negative integer n, denoted by n!, is the product of all positive integers
# less than or equal to n)

print("---------------------------------------------------------------------") 
print("Exercise 1: Factorial Calculation")

def calculateFactorial():
    n = int(input("Please Enter a Number to Calculate its Factorial : "))
    res = 1
    while(n <= 0 ):
        n = int(input("Please Enter a POSITIVE Number to Calculate its Factorial : "))
    
    for i in range(1,n+1):
        res *= i
    print(res) 
#calculateFactorial()       

##############
# EXERCISE 2 #
##############

# Write a function that takes an integer as an input from the user and finds all its divisors
# and stores them in a list.

def getDivisor():
    number = int(input("Enter a number to find all its divisor: "))
    result = []
    if(number <= 0):
        return result
    for i in range(1,number+1):
        if(number % i == 0):
            result.append(i)
    return result

# res = getDivisor()
# print(res)


##############
# EXERCISE 3 #
##############

# Write a function called reverseString that takes a string as input from the user and returns
# the string reversed. You must use a loop to implement the reversal, and you cannot use any
# built-in string or list reversal functions.

def reverseString():
    str = input("Enter a String to be Reversed: ")
    res = ''
    for i in range(len(str)-1, -1, -1):
        res += str[i]
    print(res)

#reverseString()        

def getEven():
    nbr = input("Enter a list of numbers and separate them with space")
    nbrRes = nbr.split()
    intNbrRes = []
    for i in nbrRes:
        if(int(i) % 2 == 0):
          intNbrRes.append(int(i))
    print(intNbrRes)

#getEven()

def checkPassword():
    str = input("Enter a Password: ")
    strLength = len(str)
    hasLen = False
    hasDigit = False
    hasUpper = False
    hasLower = False
    hasSpecial = False

    if(strLength >= 8):
         hasLen = True
    for i in range(strLength):
        if(str[i].isdigit):
            hasDigit = True
            break
    for i in range(strLength):
        if(str[i].isupper):
             hasUpper = True
             break
    for i in range(strLength):
        if(str[i].islower):
            hasLower = True
    for i in range(strLength):
        if(str[i] == '#' or str[i] == '?' or str[i] == '!' or str[i] == '$' ):
            hasSpecial = True
            break   
    if(hasSpecial and hasDigit and hasLen and hasLower and hasUpper):
        print("Strong Password")
    else:
        print("Weak Password") 


checkPassword()                    
