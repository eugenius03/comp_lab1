import matplotlib.pyplot as plt
import numpy as np
import math
def is_perfect_square(x):
    s = int(math.sqrt(x))
    return s*s == x

def is_fibonacci(n):

    return is_perfect_square(5*n*n + 4) or is_perfect_square(5*n*n - 4)


r = int(input("Enter R: "))
n = int(input("Enter N: "))

x1 = [0]
y1 = [0]
x_coord = x1[0]
y_coord = y1[0]
i=0
step=r/n
for _ in range(n):
    x_coord=x1[i]+step
    x1.append(x_coord)
    y1.append(0)
    i+=1
for _ in range(n):
    y_coord=y1[i]+step
    y1.append(y_coord)
    x1.append(r)
    i+=1
for _ in range(n):
    x_coord=x1[i]-step
    x1.append(x_coord)
    y1.append(r)
    i+=1
for _ in range(n):
    y_coord=y1[i]-step  
    y1.append(y_coord)
    x1.append(0)
    i+=1

points = {}
for i in range(1,4*n+1):
    points[i] = [x1[i-1],y1[i-1]] 
x = []
y = []
for i in points.keys():
    for j in points.keys():
        number = j - i
        if all(((number)%(4*n)>0, is_fibonacci(number), points[i][0]!=points[j][0], points[i][1]!=points[j][1])):
            x.extend([points[i][0], points[j][0], None])
            y.extend([points[i][1], points[j][1], None])
plt.plot(x1,y1, marker='o')
plt.plot(x,y, linestyle='dotted')
plt.show() 
