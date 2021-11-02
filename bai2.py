import matplotlib.pyplot as plt
import numpy as np

 
# a)
x = np.array([2,3,4,5])
y = np.array([6,2,3,9])
plt.plot([1,2,3,4],[1,4,3,9],'r',x,y,'g^')
plt.title("ABC")
plt.xlabel("Hoành độ")
plt.ylabel("Tung độ")
#plt.show()
plt.clf()


# b)
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
#plt.show()
plt.clf()


# c)

plt.title("abc")

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