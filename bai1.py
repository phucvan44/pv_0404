import numpy as np 
from math import sqrt


def gen_array(lim, sizeX, sizeY):
	return np.random.randint(lim, size = (sizeX, sizeY))


def prime(n):
	if (n%2 == 0 and n > 2) or (n < 2):
		return False 
	return all(n%i for i in range(3, int(sqrt(n) + 1), 2))


def taskA():
	A = gen_array(10, 3, 4)
	B = gen_array(10, 3, 4)
	print("A:\n", A, "\nB", B)


def taskB():
	A = gen_array(10, 4, 4)
	B = ~(A%2) + 2
	print("A:\n", A, "\nB", B)


def taskC():
	A = gen_array(10, 5, 5)
	print("A:\n", A)

	A = np.fliplr(A)
	func = np.vectorize(prime)
	A_prime_diagonal = func(A.diagonal())
	count_prime_diagonal = len(np.extract(A_prime_diagonal, A))
	print("A flip left to right: \n", A, "\n", count_prime_diagonal)


if __name__ == "__main__":
	# A
	print("Task A:\n")
	taskA()
	print("\nEnd task A\n")

	#B
	print("Task B:\n")
	taskB()
	print("\nEnd task B\n")

	#C
	print("Task C:\n")
	taskC()
	print("\nEnd task C\n")
	