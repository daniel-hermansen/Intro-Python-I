print("Stretch Goal Prime Number")
num = input("Enter a number: ")
flag = False
num = int(num)

for i in range(2, int(num / 2)):
    print(num % i)
    if (num % i == 0):
        flag = True
        break

if (flag is True):
    print(f"{num} is not a prime.")
else:
    print(f"{num} is a prime.")