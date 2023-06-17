import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

P = 600                   
scale = P / 2               
view = (0, 0)            
n_iter = 20 

Z = []

fig, ax = plt.subplots()

fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)

fig.set_size_inches(6, 6)


plt.axis('off')

ims = []
Zs = []
for i in range(20):
    n_iter = i + 1
    for y in range(-P+view[1], P+view[1]):
        ls = []
        for x in range(-P+view[0], P+view[0]):
            a = x / scale # масштаб
            b = y / scale
            z = complex(a, b)
            c = complex(x/(0.5*P), y/(0.5*P))
            n = 0
            for i in range(n_iter):
                z = z**2 + c
                n = i
                if abs(z) > 2:
                    break

            if n == n_iter-1:
                ls.append(100)
            else:
                ls.append((n/n_iter)*100)
        Z.append(ls)
    Zn = np.array(Z)
    Zs.append(Z)
    im = ax.imshow(Zn, animated=True)
    ims.append([im])
    Z = []
    print(n_iter)

np.save('anim', np.array(Zs, ndmin=2))

ani = animation.ArtistAnimation(fig, ims, interval=100, blit=True,
                                repeat_delay=1000)

ani.save("movie.gif")
ani.save("movie.mp4")

plt.show()

