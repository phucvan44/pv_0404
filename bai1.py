import numpy as np 
from math import sqrt


def prime(n):
	if (n%2 == 0 and n > 2) or (n < 2):
		return False 
	return all(n%i for i in range(3, int(sqrt(n) + 1), 2))


if __name__ == "__main__":
	# A
	MATRIX_1 = np.random.randint(10, size = (3,4))
	MATRIX_2 = np.random.randint(10, size = (4,4))
	print(MATRIX_1)
	print(MATRIX_2)
	print(MATRIX_1@MATRIX_2)

	#B
	MATRIX_A = MATRIX_2.copy()
	MATRIX_B = ~(MATRIX_A%2) + 2
	print(MATRIX_A)
	print(MATRIX_B)

	#C
	A_FLIP = np.fliplr(MATRIX_A)
	func = np.vectorize(prime)
	DIAG_A_FLIP = A_FLIP.diagonal()
	count_prime = len(np.extract(func(DIAG_A_FLIP), A_FLIP))
	print(DIAG_A_FLIP)
	print(count_prime)

	