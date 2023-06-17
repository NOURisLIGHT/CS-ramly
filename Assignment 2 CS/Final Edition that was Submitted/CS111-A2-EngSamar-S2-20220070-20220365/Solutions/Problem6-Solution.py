A = [0] * 50
print("Enter a list")
for g in range(0, 50):
    A[g] = input()
B = list(A)
i = 0
while i < len(A):
    A[i] = A[i+1]
    A[i+1] = B[i]
    i += 2
print(A)

