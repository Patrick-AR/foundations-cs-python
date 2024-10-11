def countDigit(num):
    if (0<num<10):
        return 1
    else:
        return 1+countDigit(num//10)
    
print(countDigit(200) )   