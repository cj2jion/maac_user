# -*- coding: UTF-8 -*-


import numpy as np
import time

import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt


fw = open('train1_3_1_2/result.txt')

whole_avr_qos=np.array([], np.float16)
user1_avr_qos=np.array([], np.float16)
user2_avr_qos=np.array([], np.float16)
user3_avr_qos=np.array([], np.float16)

user_total_r=np.array([], np.float16)
user1_r=np.array([], np.float16)
user2_r=np.array([], np.float16)
user3_r=np.array([], np.float16)

num=0
for line in fw.readlines():
    num +=1
    lineArr = line.strip().split(' ')

    whole_avr_qos_temp=float(lineArr[1])
    user1_avr_qos_temp=float(lineArr[2])
    user2_avr_qos_temp=float(lineArr[3])
    user3_avr_qos_temp=float(lineArr[4])

    user_total_r_temp=float(lineArr[5])
    user1_r_temp=float(lineArr[6])
    user2_r_temp=float(lineArr[7])
    user3_r_temp=float(lineArr[8])

    whole_avr_qos=np.append(whole_avr_qos, whole_avr_qos_temp)
    user1_avr_qos=np.append(user1_avr_qos, user1_avr_qos_temp)
    user2_avr_qos=np.append(user2_avr_qos, user2_avr_qos_temp)
    user3_avr_qos=np.append(user3_avr_qos, user3_avr_qos_temp)

    user_total_r=np.append(user_total_r, user_total_r_temp)
    user1_r=np.append(user1_r, user1_r_temp)
    user2_r=np.append(user2_r, user2_r_temp)
    user3_r=np.append(user3_r, user3_r_temp)


fw.close()
x0 = np.linspace(1, 1000,1000)
print(num)

y1=whole_avr_qos
y2=user1_avr_qos
y3=user2_avr_qos
y4=user3_avr_qos

y5=user_total_r
y6=user1_r
y7=user2_r
y8=user3_r


plt.figure(num=1)
l1, =plt.plot(x0, y1, color='black', linewidth=1.0, linestyle=':', label='whole average qos')
l2,= plt.plot(x0,y2,color='green',linewidth=1.0,linestyle='-', label='user1')
l3, = plt.plot(x0, y3, color='red', linewidth=1.0, linestyle='-', label='user2')
l4, = plt.plot(x0, y4, color='yellow', linewidth=1.0, linestyle='-', label='user3')
plt.xlabel('episode num')
plt.ylabel('qos/query')
plt.title('average qos per query')
plt.legend(loc='upper right')

plt.figure(num=2)
l5,= plt.plot(x0,y5,color='black',linewidth=1.0,linestyle=':', label='total reward')
l6, = plt.plot(x0, y6, color='green', linewidth=1.0, linestyle='-', label='user1')
l7, = plt.plot(x0, y7, color='red', linewidth=1.0, linestyle='-', label='user2')
l8, = plt.plot(x0, y8, color='yellow', linewidth=1.0, linestyle='-', label='user3')

plt.xlabel('episode')
plt.ylabel('reward')
plt.title('episode reward')
plt.legend(loc='upper right')

plt.show()
