# Exercise 1:
# Write a Python program that asks the user to input 3 numbers,
# and then the program will find and print the maximum value among the entered numbers.
# (Note: You cannot use built-in functions like max() or any lists)

print("---------------------------------------------------------------------") 
print("Exercise 1: Find The Max Number")
first_Number = int(input("Please Enter the first number: "))
second_Number = int(input("Please Enter the second number: "))
third_Number = int(input("Please Enter the third number: "))

if(first_Number > second_Number):
    if(first_Number > third_Number):
        print("The Max is: ",first_Number)
    else:
        print("The Max is: ",third_Number)
elif(second_Number > third_Number):
    print("The Max is: ",second_Number)
else:
    print("The Max is: ",third_Number)


print("---------------------------------------------------------------------")    




# Exercise 2:
# Write a Python program that:
# 1. Takes a positive integer n from the user.
# 2. Multiplies all the odd numbers between 1 and n (inclusive).
# If the product exceeds 100, print "Multiplication exceeded" and stop the multiplication process.
# If there are no odd numbers, the program should simply return 1.
# If the multiplication process completes without exceeding 100, print the final product.

print("Exercise 2: Multiply Odd Numbers: ")

n = int(input("Please enter a POSITIVE integer: "))
while(n < 0):
    n = int(input("We just accept POSITIVE Integer: "))
count = 1
multiply_Number = 1
while(count <= n and multiply_Number < 100):
    if(count % 2 != 0):
        multiply_Number *= count
    count+=1    
if(multiply_Number >= 100):
    print("Multiplication exceeded")
elif(multiply_Number == 1):
    print(1)
else:
    print("Result: ",multiply_Number)
    
    
print("---------------------------------------------------------------------") 



# Exercise 3:
# Write a Python program that:
# 1. Continuously prompts the user to enter scores until they input -1 to stop.
# 2. Calculates and prints the average of the entered scores (excluding -1).
# 3. If no valid scores are entered (i.e., if the first input is -1), print a message indicating that
# no scores were entered.

print("Exercise 3: Calculate the Score Average ")
n = float(input("Please Enter Score -1 to EXIT: "))
score_Sum = 0
score_Count = 0
score_Res = 0
while(n >= 0):
    score_Sum += n
    score_Count += 1
    n = float(input("Please Enter Score  -1 to EXIT: "))
if(score_Count == 0):
    print("No Score is Entered")
else:
    score_Res = round(score_Sum / score_Count , 1)
    print("The Score Average is:",score_Res)
    

print("---------------------------------------------------------------------") 

    
# Exercise 4:
# A four-digit number ABCD is said to be lucky if A + B = C + D
# 1. write a program that reads a number(int) from the user
# 2. checks if it was lucky or not
# 3. it should print "F" if it was lucky, otherwise print "U"     

print("Exercise 4: Lucky Number or Not? ")
n = int(input("Enter a 4 digit Number ex: 1234: "))

count = 0
ab_Sum = 0
cd_Sum = 0

while(n > 0):
     last_Number = n % 10
     n = n // 10
     if(count < 2):
         cd_Sum += last_Number
     else:
         ab_Sum += last_Number
     count += 1  
if(ab_Sum == cd_Sum):
    print("F")
else:
    print("U")

print("---------------------------------------------------------------------")     