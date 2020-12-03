print("prime numbers of 100 or less")

for num in range(2, 100):
    for i in range(2, num):
        if (num % i) == 0:
            break
    else:
         print(num)