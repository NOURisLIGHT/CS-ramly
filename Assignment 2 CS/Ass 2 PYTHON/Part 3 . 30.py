# X pow Y == X multiply itself for Y times

x = int(input("Enter the base: "))
y = int(input("Enter the power: "))
power = 1

for i in range(y):
    power = power * x
    
print(power)