'''Produce an image of a Definite Integral'''
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def cubic_func(x):
    return (x - 3) * (x - 5) * (x - 7)

a, b = 2, 9  # Integral limits [a,b]
x_array = np.linspace(1, 9.5)
y_array = cubic_func(x_array)

#ymin_interval = min(y_array[(x_array>=a) & (x_array<=b)])
ymin_interval = min(y_array)
#rint(ymin_interval)

fig, ax = plt.subplots()
ax.plot(x_array, y_array, 'r', linewidth=2)
ax.set_ylim(bottom=ymin_interval)

# Make the shaded region
ix = np.linspace(a,b)
iy = cubic_func(ix)
#verts = [(a,0), *zip(ix, iy), (b,0)]
verts = [(a,ymin_interval), *zip(ix,iy), (b,ymin_interval)]
poly = Polygon(verts, facecolor='0.90', edgecolor='0.50')
ax.add_patch(poly)

ax.text(0.5 * (a + b), 30, r"$\int_a^b f(x)\mathrm{d}x$",horizontalalignment='center', fontsize=20)

fig.text(0.90, 0.05, '$x$')
fig.text(0.10, 0.90, '$y$')

ax.spines[['top','right']].set_visible(False)
ax.set_xticks([a, b], labels=['$a$', '$b$'])
ax.set_yticks([])

plt.title('Definite Integral')

plt.savefig('Definite_Integral.png')
plt.show()

