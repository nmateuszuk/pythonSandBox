

def is_prime(num):
    primary = True
    for number in range(2, 10):
        if num != number:
            if num % number == 0:
                primary = False
                break
    return primary


print(is_prime(15485863))
