import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy.optimize import curve_fit

# markers and colors
marker = [".","v","^","s","D","o"]
colors = ["#1f77b4","#ff7f0e","#2ca02c","#9467bd","#8c564b","#e377c2","#7f7f7f","#17becf"]

# defining fit functions
def func1(x,B1,B2):
    return B1*np.exp(-x*B2/0.4)

def func2(x,B1,B2):
    return B1*np.exp(-x/0.4*B2)

# reading data
data = pd.DataFrame(columns=["c","e","j"])

for c in [0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4]:
    filename = "./DATA/fitting_c_"+str(c)+".txt"
    e, j = np.loadtxt(filename,delimiter=";",comments="#",unpack=True)
    data = data.append({"c":c,"e":e,"j":j},ignore_index=True)

i = 0
index = 20


# fitting after epsilon = 2 with func1
for c in [0.6, 0.8, 1.0, 1.2,1.4]:
    e = data.loc[(data["c"]==c)]["e"].values[0]
    j = data.loc[(data["c"]==c)]["j"].values[0]
    popt, pcov = curve_fit(func1, e[index:], j[index:])
    plt.scatter(e, j,marker=marker[i%5],color=colors[i%5], label="Simulation c="+str(c))
    plt.plot(e[index:], func1(e[index:],*popt),color=colors[i%5], label="Fitted c="+str(c))
    i+=1
plt.xlim([0,3])
plt.legend(frameon=False, ncol=2)
plt.xlabel(r"$\varepsilon$")
h=plt.ylabel("j")
h.set_rotation(0)
plt.savefig("fitfunc1.pdf")
plt.show()

# fitting after epsilon = 2 with func2
for c in [0.6, 0.8, 1.0, 1.2,1.4]:
    e = data.loc[(data["c"]==c)]["e"].values[0]
    j = data.loc[(data["c"]==c)]["j"].values[0]
    popt, pcov = curve_fit(func2, e[index:], j[index:])
    plt.scatter(e, j,marker=marker[i%5],color=colors[i%5], label="Simulation c="+str(c))
    plt.plot(e[index:], func2(e[index:],*popt),color=colors[i%5], label="Fitted c="+str(c))
    i+=1
plt.xlim([0,3])
plt.legend(frameon=False, ncol=2)
plt.xlabel(r"$\varepsilon$")
h=plt.ylabel("j")
h.set_rotation(0)
plt.savefig("fitfunc2.pdf")
plt.show()

i = 0
index = 20
indices = [9,11,13,15,17]

# fitting after top before epsilon = 2 with func1
for c in [0.6, 0.8, 1.0, 1.2,1.4]:
    e = data.loc[(data["c"]==c)]["e"].values[0]
    j = data.loc[(data["c"]==c)]["j"].values[0]
    popt, pcov = curve_fit(func1, e[indices[i]:index], j[indices[i]:index])
    plt.scatter(e, j,marker=marker[i%5],color=colors[i%5], label="Simulation c="+str(c))
    plt.plot(e[indices[i]:index], func1(e[indices[i]:index],*popt),color=colors[i%5], label="Fitted c="+str(c))
    i+=1
plt.xlim([0,3])
plt.legend(frameon=False, ncol=2)
plt.xlabel(r"$\varepsilon$")
h=plt.ylabel("j")
h.set_rotation(0)
plt.savefig("fitfunc1_v2.pdf")
plt.show()

# fitting after top before epsilon = 2 with func2
for c in [0.6, 0.8, 1.0, 1.2,1.4]:
    e = data.loc[(data["c"]==c)]["e"].values[0]
    j = data.loc[(data["c"]==c)]["j"].values[0]
    popt, pcov = curve_fit(func2, e[indices[i]:index], j[indices[i]:index])
    plt.scatter(e, j,marker=marker[i%5],color=colors[i%5], label="Simulation c="+str(c))
    plt.plot(e[indices[i]:index], func2(e[indices[i]:index],*popt),color=colors[i%5], label="Fitted c="+str(c))
    i+=1
plt.xlim([0,3])
plt.legend(frameon=False, ncol=2)
plt.xlabel(r"$\varepsilon$")
h=plt.ylabel("j")
h.set_rotation(0)
plt.savefig("fitfunc2_v2.pdf")
plt.show()
