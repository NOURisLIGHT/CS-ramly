A = []
length = int(input("Enter the length of the array: "))
print("Enter the array elements below:")
for i in range(length):
    x = input("")
    A.append(x)
print("Enter 3 numbers below:")
m = int(input())
p = int(input())
n = int(input())
if m <= p <= n:
    A.remove(A[p])
print(A)
