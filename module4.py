N = int(input("Enter a positive integer N: "))
while N <= 0:
    print("Enter a positive integer.")
    N = int(input("Enter a positive integer N: "))

numbers = []
for i in range(N):
    num = int(input(f"Enter number {i+1}/{N}: "))
    numbers.append(num)

X = int(input("Enter an integer X: "))

if X in numbers:
    index = numbers.index(X) + 1
    print(f"Index of {X} is: {index}")
else:
    print("-1")
