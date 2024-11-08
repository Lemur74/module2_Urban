numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
prime = []
not_prime = []
is_prime = True

for i in numbers:
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime and i != 1:
        prime.append(i)
    elif i != 1:
        not_prime.append(i)
    is_prime = True
print(prime)
print(not_prime)