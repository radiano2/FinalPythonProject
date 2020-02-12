from tkinter import *

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from scipy.misc import face
from scipy.spatial import cKDTree as KDTree




REDUCED_COLOR_SPACE = True

# borrow a list of named colors from matplotlib
if REDUCED_COLOR_SPACE:
    use_colors = {
        k: colors.cnames[k]
        for k in ['red', 'green', 'blue', 'black', 'yellow', 'purple']
    }
else:
    use_colors = colors.cnames

# translate hexstring to RGB tuple
named_colors = {
    k: tuple(map(int, (v[1:3], v[3:5], v[5:7]), 3 * (16,)))
    for k, v in use_colors.items()
}
ncol = len(named_colors)

if REDUCED_COLOR_SPACE:
    ncol -= 1
    no_match = named_colors.pop('purple')
else:
    no_match = named_colors['purple']

# make an array containing the RGB values
color_tuples = list(named_colors.values())
color_tuples.append(no_match)
color_tuples = np.array(color_tuples)

color_names = list(named_colors)
color_names.append('no match')

# get example picture
img = face()

# build tree
tree = KDTree(color_tuples[:-1])
# tolerance for color match inf means use best match no matter how
# bad it may be
tolerance = np.inf
# find closest color in tree for each pixel in picture
dist, idx = tree.query(img, distance_upper_bound=tolerance)
# count and reattach names
counts = dict(zip(color_names, np.bincount(idx.ravel(), None, ncol + 1)))

print(counts)

def close_window():
    window.destroy()

window = Tk()

window.title("Welcome to LikeGeeks app")

window.geometry('350x200')

lbl = Label(window, text="Hello")

lbl.grid(column=0, row=0)

btn = Button(text="Click Me" , command = close_window)

btn.grid(column=1, row=0)

window.mainloop()

objects = ['red', 'green', 'blue', 'black', 'yellow', 'purple']
y_pos = np.arange(len(objects))
performance = [0, 403561, 3262, 153782, 225827, 0]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Usage')
plt.title('Programming language usage')

plt.show()
