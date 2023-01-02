import numpy as np
import matplotlib.pyplot as plt
from random import randint
from matplotlib.animation import FuncAnimation

#inisialisasi
n_partikel = 3
n_iter = 100
x_posisi = 0
y_posisi = 0
 

n = 100
#buat 2 array untuk koordinat x dan y
#ukuran sama dengan jumlah ukuran dan diisi dengan 0
x = np.zeros(n)
y = np.zeros(n)

x_min = 5
x_max = 30
y_min = 10
y_max = 50

x_range = x_max - x_min
y_range = y_max - y_min


x_data=[]
y_data=[]
fig, ax = plt.subplots()
ax.set_xlim(-10,10)
ax.set_ylim(-10,10)
line, = ax.plot(0,0)

def init():
    line.set_data([],[])
    return line,

def update(num):
    # isi koordinat dengan 4 variabel atau direction
    for i in range(1, n):
        val = randint(1, 4)  #4 direction
        if val == 1:
            x[num] = x[num - 1] + 1
            y[num] = y[num - 1]
        elif val == 2:
            x[num] = x[num - 1] - 1
            y[num] = y[num - 1]
        elif val == 3:
            x[num] = x[num - 1]
            y[num] = y[num - 1] + 1
        else:
            x[num] = x[num - 1]
            y[num] = y[num - 1] - 1

    
    x_data.append(x)
    y_data.append(y)

    line.set_xdata(x_data)
    line.set_ydata(y_data)
    return line,

# Membuat objek FuncAnimation
anim = FuncAnimation(fig, update, frames=len(x), interval=100)
# save ke file mp4
anim.save('randomwalk.mp4', writer = 'ffmpeg', fps = 30)

