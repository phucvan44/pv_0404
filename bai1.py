import numpy as np 
from math import sqrt


def prime(n):
	if (n%2 == 0 and n > 2) or (n < 2):
		return False 
	return all(n%i for i in range(3, int(sqrt(n) + 1), 2))


def task_a():
	a = np.random.randint(10, size = (3, 4))
	b = np.random.randint(10, size = (3, 4))
	print("A:\n", a, "\nB:\n", b)


def task_b():
	a = np.random.randint(10, size = (4, 4))
	b = ~(a%2) + 2
	print("A:\n", a, "\nB:\n", b)


def task_c():
	a = np.random.randint(10, size = (5, 5))
	print("A:\n", a)

	a = np.fliplr(a)
	func = np.vectorize(prime)
	a_prime_diagonal = func(a.diagonal())
	count_prime_diagonal = len(np.extract(a_prime_diagonal, a))
	print("A flip left to right: \n", a, "\nCount prime in diagonal: ", count_prime_diagonal)


if __name__ == "__main__":
	# A
	print("Task A:\n")
	task_a()
	print("\nEnd task A\n")

	#B
	print("Task B:\n")
	task_b()
	print("\nEnd task B\n")

	#C
	print("Task C:\n")
	task_c()
	print("\nEnd task C\n")
	