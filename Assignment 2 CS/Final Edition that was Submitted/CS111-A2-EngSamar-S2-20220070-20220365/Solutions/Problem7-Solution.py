A = [0] * 4
X = [0] * 4
print("Enter a list")
for i in range(0, 4):
    A[i] = input()
for i in range(0, 4):
    X[i] = A[3-i]
print(X)
