import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy.optimize import curve_fit
from mpl_toolkits.mplot3d import Axes3D

# markers and colors
marker = [".","v","^","s","D","o",1,"P","p","X","|","_"]
colors = ["#1f77b4","#ff7f0e","#2ca02c","#9467bd","#8c564b","#e377c2","#7f7f7f","#17becf"]

# defining fit functions
def func1(x,B1,B2):
    return B1*np.exp(-x*B2*a/(c**2))

def func2(x,B1,B2):
    return B1*np.exp(-(x/a)*B2)

# reading data
data = pd.DataFrame(columns=["c","e","j"])

for a in [0.2, 0.4, 0.6]:
    for c in [0.6, 0.9, 1.2, 1.5]:
        filename = "./DATA/fitting_c_"+str(c)+"_a_"+str(a)+".txt"
        e, j = np.loadtxt(filename,delimiter=";",comments="#",unpack=True)
        data = data.append({"c":c,"a":a,"e":e,"j":j},ignore_index=True)

i = 0
indices=[11,14,17,20]

# fitting with func1
C = np.array([0.6, 0.9, 1.2, 1.5])
A = np.array([0.2, 0.4, 0.6])
Bfunc1 = []
for a in A:
    i=0
    list1=[]
    for c in C:

        index=indices[i]
        e = data.loc[(data["c"]==c) & (data["a"]==a)]["e"].values[0]
        j = data.loc[(data["c"]==c) & (data["a"]==a)]["j"].values[0]
        popt, pcov = curve_fit(func1, e[index:], j[index:])
        print("func1 after 2 for a="+str(a)+": "+str(popt))
        plt.rc('text', usetex=True)
        plt.rc('font', family='serif',size=14)
        plt.scatter(e[index:], j[index:],marker=marker[i%5],color=colors[i%5],s=4, label="Simulation c="+str(c))
        plt.plot(e[index:], func1(e[index:],*popt),color=colors[i%5], label="Fitted c="+str(c))
        list1.append(popt[1])
        i+=1
    plt.xlim([1,3])
    plt.legend(frameon=False, ncol=2)
    plt.yscale("log")
    plt.title("a="+str(a))
    plt.text(2, 0.1, r'$j(\varepsilon)=b_2 e ^{- B_2 \frac{\varepsilon a L}{c^2} }$',fontsize=18)
    plt.xlabel(r"$\varepsilon$",fontsize=20)
    h=plt.ylabel("j",fontsize=20)
    h.set_rotation(0)
    plt.savefig("fit_multi_ca_func1_a_"+str(a)+".pdf")
    plt.show()
    Bfunc1.append(list1)

# fitting with func2
i=0
Bfunc2 = []
for a in A:
    i=0
    list1 = []
    for c in C:
        index=indices[i]
        e = data.loc[(data["c"]==c) & (data["a"]==a)]["e"].values[0]
        j = data.loc[(data["c"]==c) & (data["a"]==a)]["j"].values[0]
        popt, pcov = curve_fit(func2, e[index:], j[index:])
        print("func2 after 2 for a="+str(a)+": "+str(popt))
        plt.rc('text', usetex=True)
        plt.rc('font', family='serif',size=14)
        plt.scatter(e[index:], j[index:],marker=marker[i%5],s=4,color=colors[i%5], label="Simulation c="+str(c))
        plt.plot(e[index:], func2(e[index:],*popt),color=colors[i%5], label="Fitted c="+str(c))
        list1.append(popt[1])
        i+=1
    plt.xlim([1,3])
    plt.legend(frameon=False, ncol=2)
    plt.text(2, 0.1, r'$j(\varepsilon)=b_1 e ^{-B_2 \frac{\varepsilon}{aL}}$',fontsize=18)
    plt.xlabel(r"$\varepsilon$",fontsize=20)
    plt.yscale("log")
    h=plt.ylabel("j",fontsize=20)
    h.set_rotation(0)
    plt.savefig("fit_multi_ca_func2_a_"+str(a)+".pdf")
    plt.show()
    Bfunc2.append(list1)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

Bfunc1 = np.array(Bfunc1)
Bfunc2 = np.array(Bfunc2)
print(Bfunc1)
print(A)
print(C)
x,y = np.meshgrid(C,A)

plt.rc('text', usetex=True)
plt.rc('font', family='serif',size=14)

ax.plot_wireframe(x,y,Bfunc1,label=r'$j(\varepsilon)=b_2 e ^{- B_2 \frac{\varepsilon a L}{c^2} }$')
ax.plot_wireframe(x,y,Bfunc2,color="tab:orange",label=r'$j(\varepsilon)=b_1 e ^{-B_2 \frac{\varepsilon}{aL}}$')
ax.set_xlabel(r"$c$",fontsize=20)
ax.set_ylabel(r"$a$",fontsize=20)
h=ax.set_zlabel(r"$B_2$",fontsize=20)
h.set_rotation(0)
ax.set_xticks(C)
ax.set_xlim([0.6, 1.5])
ax.set_xbound(lower=0.6, upper=1.5)
ax.set_yticks(A)
ax.set_ylim([0.2, 0.6])
ax.set_ybound(lower=0.2, upper=0.6)
ax.view_init(15, -135)
h.set_rotation(0)
ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
# make the grid lines transparent
ax.xaxis._axinfo["grid"]['color'] =  (1,1,1,0)
ax.yaxis._axinfo["grid"]['color'] =  (1,1,1,0)
ax.zaxis._axinfo["grid"]['color'] =  (1,1,1,0)
plt.legend(frameon=False)
plt.savefig("fit_B2.pdf")
plt.show()
