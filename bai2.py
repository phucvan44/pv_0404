import matplotlib.pyplot as plt 
import numpy as np


def task_a():
	x1 = np.array([2,3,4,5])
	y1 = np.array([6,2,3,9])
	x2 = np.array([1,2,3,4])
	y2 = np.array([1,4,3,9])

	plt.plot(x2, y2, 'r', x1, y1, 'g^')
	plt.title("ABC")
	plt.xlabel("Hoành độ")
	plt.ylabel("Tung độ")
	plt.show()


def task_b():
	bot_label = np.arange(1,5)
	value_1 = np.array([50,100,200,15])
	value_2 = np.array([90,30,25,40])

	index = np.arange(4)
	width = 0.30

	plt.bar(index, value_1, width, color="green", label="1")
	plt.bar(index+width, value_2, width, color="yellow", label="2")
	plt.title("pv_maicogroup")
	plt.xlabel("Thứ tự")
	plt.ylabel("Giá trị")
	plt.xticks(index+width/2, bot_label)
	plt.legend(loc="best")
	plt.show()


def task_c():
	fig, ax = plt.subplots(2, 2)

	ax[0 ,0].plot([1,2,3,4],[0,4.0,3.0,8.0],color='green')
	ax[0, 0].set_title("abc1")

	ax[0 ,1].plot([1,2,3,4,5],[0,6.0,2.5,3.0,8.0],color='red')
	ax[0, 1].set_title("abc2")

	ax[1 ,0].plot([0.0,0.2,0.4,0.6,0.8,1.0],[0,0,0,0,0,0],color='white')
	ax[1, 0].set_title("abc3")
	ax[1, 0].set_xlim([0.0, 1.0])
	ax[1, 0].set_ylim([0.00, 1.00])

	ax[1 ,1].plot([1,2,4],[0,5,0],color='yellow')
	ax[1, 1].set_title("abc4")

	plt.show()


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
