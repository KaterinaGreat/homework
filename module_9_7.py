def is_prime(func):
    def wrapper(*args, **kwargs):
        sum_ = sum(args)
        result = func(*args, **kwargs)
        if sum_ <= 1:
            print('Простое')
        else:
            print('Составное')
        return result
    return wrapper

@is_prime
def sum_three(*args):
    return sum(args)

result = sum_three(2, 3, 6)
print(result)