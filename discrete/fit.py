import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy.optimize import curve_fit

marker = [".","v","^","s","D","o"]
colors = ["#1f77b4","#ff7f0e","#2ca02c","#9467bd","#8c564b","#e377c2","#7f7f7f","#17becf"]
def func(x,a,b):
    return a*np.exp(-x*b)

data = pd.DataFrame(columns=["c","a","e","j"])

for c in [0.5, 1, 1.5]:
    for a in [0.4,0.6,0.8]:
        filename = "./DATA/fitting_c_"+str(c)+"_a_"+str(a)+".txt"
        e, j = np.loadtxt(filename,delimiter=";",comments="#",unpack=True)
        data = data.append({"c":c,"a":a,"e":e,"j":j},ignore_index=True)

i = 0
ii = 0
arr_index=[4,6,9]
for c in [0.5, 1, 1.5]:
    for a in [0.4,0.6,0.8]:
        index = arr_index[i]
        e = data.loc[(data["c"]==c) & (data["a"]==a)]["e"].values[0]
        j = data.loc[(data["c"]==c) & (data["a"]==a)]["j"].values[0]
        popt, pcov = curve_fit(func, e[index:], j[index:])
        plt.scatter(e, j,marker=marker[ii%5],color=colors[ii%5], label="Original Noised Data")
        plt.plot(e[index:], func(e[index:],*popt),color=colors[ii%5], label="Fitted Curve")
        ii+=1
    i+=1
plt.legend(frameon=False)
plt.show()
