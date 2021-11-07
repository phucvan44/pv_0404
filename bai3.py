import pandas as pd
import numpy as np


def read_csv():
	data = pd.read_csv("./dataset.csv")
	return data 


def task_a(data):
	print(data[:50])


def task_b(data):
	print(data.iloc[:, 1:4])


def task_c(data):
	active = data.values[:, 4]
	
	dic = {}
	for i in range(len(active)):
	    if active[i] > 100:
	        dic[i] = active[i]
	print(dic)


if __name__ == "__main__":
	data = read_csv()
	
	# A
	print("Task A:\n")
	task_a(data)
	print("\nEnd task A\n")

	#B
	print("Task B:\n")
	task_b(data)
	print("\nEnd task B\n")

	#C
	print("Task C:\n")
	task_c(data)
	print("\nEnd task C\n")
