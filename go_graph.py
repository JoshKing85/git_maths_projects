import numpy as np
import matplotlib.pyplot as plt


s1 = np.array([1, 0, 0])
s2 = np.array([0, 1, 0])
s3 = np.array([1, 2, 0])
s4 = np.array([2 ,1, 0])
s5 = np.array([1, 0, 1])
s6 = np.array([0, 1, 1])
s7 = np.array([1, 2, 1])

black_stones = np.array([s1, s2, s3, s4, s5, s6, s7])
white_stone = np.array([1, 1, 0])
x = np.array([])
y = np.array([])
z = np.array([])

for i in range(len(black_stones)):

    x =  np.append(x, black_stones[i][0])
    y =  np.append(y, black_stones[i][1])
    z =  np.append(z, black_stones[i][2])



for i in black_stones:
    print(i)
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim([0, 4])
ax.set_ylim([0, 4])
ax.set_zlim([0, 3])
ax.view_init(elev=20, azim=160)  # Set elevation and azimuth
ax.dist = 5  # Adjust observer distance

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.scatter(x, y, z, c = 'black', s = 100, marker = '.' )
ax.scatter(1, 1, 0, c= 'white', s= 100, marker= '.')
ax.scatter(1, 1, 1, c= 'black', s= 100, marker= '.')
plt.show()