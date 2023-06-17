def pow1(m, n):
    if n == 0:
        power = 1
    else:
        power = m * (m ** (n-1))
    print("The power is: ",power)

def pow2(m, n):
    if n == 0:
        out = 1 
    elif (n > 0 & n % 2 != 0):
        out  = (m ** (n//2)) * (m ** (n//2)) * m
    elif (n > 0 & n % 2 == 0):
        out = (m ** (n/2)) * (m ** (n/2))
        
    print("The power is {}".format(out))
    
n = int(input("Enter n: "))
m = int(input("Enter m: "))

pow1(m, n)
pow2(m, n)