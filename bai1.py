import numpy as np

# a)
array_1 = np.random.randint(10, size=(3, 4))
array_2 = np.random.randint(10, size=(4, 4))

# b)
A = np.random.randint(10, size=(4, 4))
B = ~(A%2) + 2

# c)
def prime(n):
    if (n%2==0 and n > 2) or (n < 2):
        return False
    return all(n%i for i in range(3, int(n**0.5 + 1), 2))
A = np.random.randint(10, size=(5,5))
A = np.fliplr(A)
func = np.vectorize(prime)
A_temp = func(A.diagonal())
count_prime = len(np.extract(A_temp, A))
