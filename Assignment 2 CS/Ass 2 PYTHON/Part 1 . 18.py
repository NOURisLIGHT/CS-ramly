pi_over_4 = 0.0
n = int(input("Enter a number: "))

for i in range(1, n, 4):
    pi_over_4 += 1 / i
    pi_over_4 -= 1/ (i + 2)
    
print(pi_over_4)
