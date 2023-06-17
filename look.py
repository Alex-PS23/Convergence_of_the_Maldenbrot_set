import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()
fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)
fig.set_size_inches(8, 8)

plt.axis('off')

Zn = np.load('anim.npy')

ims = []

for i in range(Zn.shape[0]):
    im = ax.imshow(Zn[i], cmap='jet')
    ims.append([im])


ani = animation.ArtistAnimation(fig, ims, interval=300, blit=True,
                                repeat_delay=1500)

ani.save("movie_jet.gif")
ani.save("movie_jet.mp4")
plt.show()

