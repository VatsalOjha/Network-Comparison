import matplotlib.pyplot as plt
import math
Array = []
Array1 = []
Array2 = []
f = open('C:\\Random1.txt', 'r+')
for lines in f.readlines():
	Array.append(float(lines))
f1 = open('C:\\Random11.txt', 'r+')
for lines in f1.readlines():
	Array1.append(float(lines))

#Example for adding one parallel instance of the code. See README Line 20. 
# f = open('C:\\Random2.txt', 'r+')
# for lines in f.readlines():
# 	Array.append(float(lines))
# f1 = open('C:\\Random22.txt', 'r+')
# for lines in f1.readlines():
# 	Array1.append(float(lines))


#If you would like to take a log of the y-axis for visualization purposes, uncomment lines below and Change Array to Array2 in Line 20. 
# for i in Array:
# 	if i != 0.0:
# 		Array2.append(math.log(i, 10))
# 	else: 
# 		Array2.append(-9)
fig = plt.figure()
ax = fig.add_subplot(111)
plt.plot(Array1, Array, 'ro')
ax.set_xlabel("Community Size")
plt.show()