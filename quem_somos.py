#!/usr/bin/env python
# coding: utf-8
__author__ = 'Mabel'
#'''Graficos para o blog covid19
#  baseado no script do Fernando
#   abril/2020

import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.gridspec import GridSpec

# Carinhas do grupo
fig = plt.figure(constrained_layout=True)
gs = GridSpec(3, 3, figure=fig)
ax = fig.add_subplot(gs[0, :])
image = plt.imread('/Users/Mabel/Downloads/mabel.png')

im = ax.imshow(image)
#patch = patches.Circle((260, 300), radius=250, transform=ax.transData)
#im.set_clip_path(patch)
ax.axis('off')
plt.title("Quem somos")



# Genero
ax1 = fig.add_subplot(gs[1, :-1])
labels = 'Feminino', 'Masculino', 'Outros'
sizes = [49,49,2]
colors_gender = ['pink','b','#99ff99']

ax1.pie(sizes,  labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax1.axis('off')


# aonde moramos
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
#import numpy as np

# defind figure dimension
#fig = plt.figure(figsize=(12, 8))
ax2 = fig.add_subplot(gs[1:, -1])
m = Basemap(projection='ortho',lon_0=-55,lat_0=-10,resolution='l')
m.drawcoastlines(color='gray')
m.fillcontinents(color='gray',lake_color='#FFFFFF')
#m.drawmeridians(range(0,420,60))
#m.drawparallels(range(-90,120,30))
m.drawcountries()
m.drawstates()
m.drawmapboundary(fill_color='#FFFFFF')


lon_prox=[-38.4860544]
lat_prox=[-12.8767614]
x,y=m(lon_prox, lat_prox)

sumlist=[100]

# prep colors
hexcolors = []
for i in range(len(x)):
    hexcolors.append('#%02x%02x%02x' % (int((255*sumlist[i])/max(sumlist)),0,0))

# scatter takes x,y,c arrays as parameters
m.scatter(x, y, c=hexcolors, s=60, zorder=10, alpha=0.7)
plt.title("Aonde moramos")


# profissoes

ax3 = fig.add_subplot(gs[-1, 0])
profs = ('Geógrafo', 'Alunos', 'Professor', 'Arquiteto', 'Agrônomo','Engenheiro Ambiental','TI')
y_pos = np.arange(len(profs))
numero = ['3','1','1','1','1','1','1']

ax3.barh(y_pos, numero, align='center')
ax3.set_yticks(y_pos)
ax3.set_yticklabels(profs)
ax3.invert_yaxis()  # labels read top-to-bottom
ax3.set_xlabel('Número de Pessoas')
ax3.set_title('Profissões')



plt.show()



fig.savefig('/Users/Mabel/Desktop/test0.png', bbox_inches='tight', dpi=300)
