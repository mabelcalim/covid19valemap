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


file = glob.glob('/Users/Mabel/Downloads/covid-19.xlsx')
print(file)
f = file[0]

#df = pd.read_excel(f, sheet_name='04abr2020')
#df = df.loc[0:38]
#df.head()
xls = pd.ExcelFile(f)

#read all the sheet together
sheet_to_df_map = {}
for sheet_name in xls.sheet_names:
    sheet_to_df_map[sheet_name] = xls.parse(sheet_name)

df ={}

letal =[]
for i in xls.sheet_names:
    df[i]= sheet_to_df_map[i].loc[0:38]
    #df[i] = df[i].head()


#for index, row in df['04abr2020'].iterrows():
#     x.append(row['CIDADE'])
#     y1.append(row['CASOS_POTENCIAIS'])


y1g,y2g,y3g = {},{},{}
# Estatistica por cidade
for a,b in enumerate(df['04abr2020']['CIDADE']):
    #print (a,b)
    y1, y2,y3,x =[],[],[],[]
    for e,i in enumerate(xls.sheet_names):
        #print(e,i)
        y1.append(df[i]['CASOS_POTENCIAIS'][a])
        y2.append(df[i]['CASOS_CONFIRMADOS'][a])
        y3.append(df[i]['MORTES_CONFIRMADAS'][a])
        #print(len(y1),len(y2),len(y3))

    #x = range(len(df.keys()))
    x = df.keys()
    #y = np.vstack([y1, y2, y3])

    #labels = ["CASOS_POTENCIAIS ", "CASOS_CONFIRMADOS", "MORTES_CONFIRMADAS"]

    #fig1=plt.figure(figsize=(10,5.5), dpi=100)
    ##fig, ax = plt.subplots()
    #plt.plot(x, y1, 'b',marker='o',label='CASOS POTENCIAIS')
    #plt.plot(x, y2, 'k',marker='o',label='CASOS CONFIRMADOS')
    #plt.plot(x, y3, 'r',marker='*',label='MORTES CONFIRMADAS')
    #plt.legend(loc='upper left')
    #plt.yticks([0,50,100,150,200,250,300,350,400,450,500])
    #plt.xticks(rotation=45)
    #plt.title('%s'%b)
    ##plt.show()
    #fig1.savefig('figs/CIDADES/%s.png'%b, bbox_inches='tight', dpi=300)
    y1g[b] = y1
    y2g[b] = y2
    y3g[b] = y3


print(y3g)
fig2=plt.figure(figsize=(10,5.5), dpi=100)
ax = fig2.add_subplot(111)
#fig, ax = plt.subplots()
m = ['*','v','o','<','8','s','p','X','D'] *40
for e,i in enumerate(y1g.keys()):
    ax.plot( x, y1g[i],marker=m[e],label='%s'%i)
    #plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.3),
          fancybox=True, shadow=True, ncol=5)

plt.xticks(rotation=45)
ax.set_ylim([0, 500])
plt.ylim(0,500)
plt.yticks([0,50,100,150,200,250,300,350,400,450,500])
plt.title('CASOS POTENCIAIS')
fig2.savefig('figs/GERAL/CASOS_POTENCIAIS.png', bbox_inches='tight', dpi=300)

fig3=plt.figure(figsize=(10,5.5), dpi=100)
ax = fig3.add_subplot(111)
#fig, ax = plt.subplots()
m = ['*','v','o','<','8','s','p','X','D'] *40
for e,i in enumerate(y2g.keys()):
    ax.plot( x, y2g[i],marker=m[e],label='%s'%i)

    #plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.3),
          fancybox=True, shadow=True, ncol=5)

plt.xticks(rotation=45)
ax.set_ylim([0, 500])
plt.ylim(0,10)
plt.yticks([0,50,100,150,200,250,300,350,400,450,500])
plt.title('CASOS CONFIRMADOS')
#plt.show()
fig3.savefig('figs/GERAL/CASOS_CONFIRMADOS.png', bbox_inches='tight', dpi=300)


fig4=plt.figure(figsize=(10,5.5), dpi=100)
ax = fig4.add_subplot(111)
#fig, ax = plt.subplots()
m = ['*','v','o','<','8','s','p','X','D'] *40
for e,i in enumerate(y3g.keys()):
    ax.plot( x, y3g[i],marker=m[e],label='%s'%i)
    #plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.3),
          fancybox=True, shadow=True, ncol=5)

plt.xticks(rotation=45)
ax.set_ylim([0, 500])
plt.ylim(0,10)
plt.yticks([0,1,2,3,4,5,6,7,8,9,10])
plt.title('MORTES CONFIRMADAS')
fig4.savefig('figs/GERAL/MORTES_CONFIRMADAS.png', bbox_inches='tight', dpi=300)
