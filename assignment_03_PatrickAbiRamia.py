##############
# EXERCISE 1 #
##############
def countDigits(n):
    if(0<n<10):
        return 1
    else:
        return 1+countDigits(n//10)

def findMaxRec(lst,max):
    if(lst == []):
        return max
    else:
        if(lst[0] > max):
            max = lst[0]
        return findMaxRec(lst[1:],max)
        
def findMax(lst):
    if(lst == []):
        return
    else:
        return findMaxRec(lst[1:],lst[0])

        

print("Select One Of The Following options: ")
n = int(input("1. Count Digits \n2. Find Max \n3. Count Tags \n4. Exit\n Choose: "))
while(n != 4):
    if(n == 1):
        print("You Are In The Count Digits: ")
        num = int(input("Enter a number: "))
        print(countDigits(num))
        
    elif(n == 2):
         print("You Are In The Find Max: ")
         num = int(input("Enter The Length Of The List: "))
         arr = []
         for i in range(num):
             arr.append(int(input("Enter a number: ")))
         print(findMax(arr))
    elif(n == 3):
         print("You Are In Count Occurance:  ")
         str = input("Enter a string containing html text: ")  
         print(findOccurances(str))
    else:
        print("Please enter a valid input: ")     
    print("Select One Of The Following options: ")
    n = int(input("1. Count Digits \n2. Find Max \n3. Count Tags \n4. Exit\n Choose: "))    
