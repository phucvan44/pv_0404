import pandas as pd


def read_csv():
	data = pd.read_csv("./dataset.csv")
	return data 


def taskA(data):
	A = data.values[:50, ::]
	print(A)


def taskB(data):
	date = data.values[::, 1]
	print("Date:\n",date, end = "\n\n")

	calories = data.values[::, 2]
	print("Calories:\n", calories, end = "\n\n")

	distance = data.values[::, 3]
	print("Distance:\n", distance, end = "\n\n")


def taskC(data):
	active = data.values[::, 4]
	
	dic = {}
	for i in range(len(active)):
	    if active[i] > 100:
	        dic[i] = active[i]
	print(dic)


if __name__ == "__main__":
	data = read_csv()
	
	# A
	print("Task A:\n")
	taskA(data)
	print("\nEnd task A\n")

	#B
	print("Task B:\n")
	taskB(data)
	print("\nEnd task B\n")

	#C
	print("Task C:\n")
	taskC(data)
	print("\nEnd task C\n")
