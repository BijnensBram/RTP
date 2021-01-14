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
    return B1*np.exp(-x*B2*0.4/(c**2))

def func2(x,B1,B2):
    return B1*np.exp(-(x/0.4)*B2)

def squared(x,a,b,c):
    # return a*x**2+b*x+c
    return a*np.exp(x*b)+c

# reading data
data = pd.DataFrame(columns=["c","e","j"])

for c in [0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4]:
    filename = "./DATA/fitting_c_"+str(c)+".txt"
    e, j = np.loadtxt(filename,delimiter=";",comments="#",unpack=True)
    data = data.append({"c":c,"e":e,"j":j},ignore_index=True)

i = 0
index = 20

# fitting after epsilon = 2 with func1
C = np.array([0.5, 0.7, 0.9, 1.1,1.3])
Bfunc1 = []
b1func1 = []
for c in C:
    e = data.loc[(data["c"]==c)]["e"].values[0]
    j = data.loc[(data["c"]==c)]["j"].values[0]
    popt, pcov = curve_fit(func1, e[index:], j[index:])
    print("func1 after 2: "+str(popt))
    Bfunc1.append(popt[1])
    b1func1.append(popt[0])
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif',size=14)
    plt.scatter(e, j,marker=marker[i%5],color=colors[i%5],s=4, label="Simulation c="+str(c))
    plt.plot(e[index:], func1(e[index:],*popt),color=colors[i%5], label="Fitted c="+str(c))
    i+=1
plt.xlim([0,3])
plt.legend(frameon=False, ncol=2)
plt.text(2, 0.1, r'$j(\varepsilon)=b_2 e ^{- B_2 \frac{\varepsilon a L}{c^2} }$',fontsize=18)
plt.xlabel(r"$\varepsilon$",fontsize=20)
h=plt.ylabel("j",fontsize=20)
h.set_rotation(0)
plt.savefig("fitfunc1.pdf")
plt.show()

# fitting after epsilon = 2 with func2
i=0
Bfunc2 = []
b1func2 = []
for c in C:
    e = data.loc[(data["c"]==c)]["e"].values[0]
    j = data.loc[(data["c"]==c)]["j"].values[0]
    popt, pcov = curve_fit(func2, e[index:], j[index:])
    Bfunc2.append(popt[1])
    b1func2.append(popt[0])
    print("func2 after 2: "+str(popt))
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif',size=14)
    plt.scatter(e, j,marker=marker[i%5],s=4,color=colors[i%5], label="Simulation c="+str(c))
    plt.plot(e[index:], func2(e[index:],*popt),color=colors[i%5], label="Fitted c="+str(c))
    i+=1
plt.xlim([0,3])
plt.legend(frameon=False, ncol=2)
plt.text(2, 0.1, r'$j(\varepsilon)=b_1 e ^{-B_2 \frac{\varepsilon}{aL}}$',fontsize=18)
plt.xlabel(r"$\varepsilon$",fontsize=20)
h=plt.ylabel("j",fontsize=20)
h.set_rotation(0)
plt.savefig("fitfunc2.pdf")
plt.show()

plt.rc('text', usetex=True)
plt.rc('font', family='serif',size=14)
plt.plot(C,Bfunc2,marker=".",markersize=3,label=r"$j(\varepsilon)=b_1 e ^{-B_2 \frac{\varepsilon}{aL}}$")
plt.plot(C,Bfunc1,marker="v",markersize=3,label=r"$j(\varepsilon)=b_2 e ^{- B_2 \frac{\varepsilon a L}{c^2} }$")
h=plt.ylabel(r"$B_2$",fontsize=18)
h.set_rotation(0)
plt.legend(frameon=False, ncol=2)
plt.xticks(C)
plt.xlabel("c",fontsize=20)
plt.savefig("fit_B2.pdf")
plt.show()


popt, pcov = curve_fit(squared, C, b1func1)
print("a,b,c="+str(popt))
plt.rc('text', usetex=True)
plt.rc('font', family='serif',size=14)
plt.plot(C, squared(C,*popt), label="Fitted c")
plt.scatter(C,b1func2,marker=".",s=8,label=r"$j(\varepsilon)=b_1 e ^{-B_2 \frac{\varepsilon}{aL}}$")
plt.scatter(C,b1func1,marker="v",s=8,label=r"$j(\varepsilon)=b_2 e ^{- B_2 \frac{\varepsilon a L}{c^2} }$")
h=plt.ylabel(r"$b_1$",fontsize=18)
h.set_rotation(0)
plt.legend(frameon=False, ncol=2)
plt.xticks(C)
plt.xlabel("c",fontsize=20)
plt.savefig("fit_b1.pdf")
plt.show()

i = 0
index = 20
indices = [9,11,13,15,17]

# fitting after top before epsilon = 2 with func1
Bfunc1 = []
b1func1 = []
for c in C:
    e = data.loc[(data["c"]==c)]["e"].values[0]
    j = data.loc[(data["c"]==c)]["j"].values[0]
    popt, pcov = curve_fit(func1, e[indices[i]:index], j[indices[i]:index])
    Bfunc1.append(popt[1])
    b1func1.append(popt[0])
    print("func1 before 2: "+str(popt))
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif',size=14)
    plt.scatter(e, j,marker=marker[i%5],color=colors[i%5],s=4, label="Simulation c="+str(c))
    plt.plot(e[indices[i]:index], func1(e[indices[i]:index],*popt),color=colors[i%5], label="Fitted c="+str(c))
    i+=1
plt.xlim([0,3])
plt.legend(frameon=False, ncol=2)
plt.text(2, 0.1, r'$j(\varepsilon)=b_2 e ^{- B_2 \frac{\varepsilon a L}{c^2} }$',fontsize=18)
plt.xlabel(r"$\varepsilon$",fontsize=20)
h=plt.ylabel("j",fontsize=20)
h.set_rotation(0)
plt.savefig("fitfunc1_v2.pdf")
plt.show()

# fitting after top before epsilon = 2 with func2
Bfunc2 = []
b1func2 = []
i=0
for c in C:
    e = data.loc[(data["c"]==c)]["e"].values[0]
    j = data.loc[(data["c"]==c)]["j"].values[0]
    popt, pcov = curve_fit(func2, e[indices[i]:index], j[indices[i]:index])
    Bfunc2.append(popt[1])
    b1func2.append(popt[0])
    print("func2 before 2: "+str(popt))
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif',size=14)
    plt.scatter(e, j,marker=marker[i%5],color=colors[i%5],s=4, label="Simulation c="+str(c))
    plt.plot(e[indices[i]:index], func2(e[indices[i]:index],*popt),color=colors[i%5], label="Fitted c="+str(c))
    i+=1
plt.xlim([0,3])
plt.legend(frameon=False, ncol=2)
plt.xlabel(r"$\varepsilon$",fontsize=20)
h=plt.ylabel("j",fontsize=20)
h.set_rotation(0)
plt.text(2, 0.1, r'$j(\varepsilon)=b_1 e ^{-B_2 \frac{\varepsilon}{aL}}$',fontsize=18)
plt.savefig("fitfunc2_v2.pdf")
plt.show()

plt.rc('text', usetex=True)
plt.rc('font', family='serif',size=14)

plt.plot(C,Bfunc2,marker=".",markersize=3,label=r"$j(\varepsilon)=b_1 e ^{-B_2 \frac{\varepsilon}{aL}}$")
plt.plot(C,Bfunc1,marker="v",markersize=3,label=r"$j(\varepsilon)=b_2 e ^{- B_2 \frac{\varepsilon a L}{c^2} }$")
h=plt.ylabel(r"$B_2$",fontsize=18)
h.set_rotation(0)
plt.legend(frameon=False, ncol=2)
plt.xlabel("c",fontsize=20)
plt.xticks(C)
plt.savefig("fit_B2_v2.pdf")
plt.show()

plt.rc('text', usetex=True)
plt.rc('font', family='serif',size=14)
popt, pcov = curve_fit(squared, C, b1func1)
print("a,b,c="+str(popt))
plt.plot(C, squared(C,*popt), label="Fitted c")
plt.scatter(C,b1func2,marker=".",s=8,label=r"$j(\varepsilon)=b_1 e ^{-B_2 \frac{\varepsilon}{aL}}$")
plt.scatter(C,b1func1,marker="v",s=8,label=r"$j(\varepsilon)=b_2 e ^{- B_2 \frac{\varepsilon a L}{c^2} }$")
h=plt.ylabel(r"$b_1$",fontsize=18)
h.set_rotation(0)
plt.legend(frameon=False, ncol=2)
plt.xticks(C)
plt.xlabel("c",fontsize=20)
plt.savefig("fit_b1_v2.pdf")
plt.show()
