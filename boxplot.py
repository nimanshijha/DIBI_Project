import matplotlib.pyplot as plt
import numpy as np
 

data = [distances_red1 , distances_green1 , distances_red_green1 ,distances_red2 ,distances_green2 ,distances_red_green1 ]
 
fig = plt.figure(figsize =(12, 7))
 
# Creating axes instance
ax = fig.add_axes([0, 0, 1, 1])
 

bp = ax.boxplot(data,patch_artist=True)
ax.set_xticklabels(['red_35_0gy_2h_p6', 'green_35_0gy_2h_p6',
                    'red_green_35_0gy_2h_p6','red_35_8gy_24h_p6', 'green_35_8gy_24h_p6',
                    'red_green_35_8gy_24h_p6'])
 
colors = ['red', 'green',
          'blue', 'red', 'green',
          'blue']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

plt.show()
plt.savefig('boxcompare.png')
