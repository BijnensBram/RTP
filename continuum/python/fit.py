import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy.optimize import curve_fit

marker = [".","v","^","s","D","o"]
colors = ["#1f77b4","#ff7f0e","#2ca02c","#9467bd","#8c564b","#e377c2","#7f7f7f","#17becf"]
def func(x,a,b):
    # return a*c**2*np.exp(-(x-c)*b)
    # return a*c*np.exp(-(x-c)*b)
    return a*np.exp(-x/(c**2)*0.4*b)

data = pd.DataFrame(columns=["c","e","j"])

C = np.array([0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4])

for c in [0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4]:
    filename = "./DATA/fitting_c_"+str(c)+".txt"
    e, j = np.loadtxt(filename,delimiter=";",comments="#",unpack=True)
    data = data.append({"c":c,"e":e,"j":j},ignore_index=True)

i = 0
index = 10
A=[]
B=[]
# for c in [0.5, 0.6, 0.7]:
for c in [0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4]:
    e = data.loc[(data["c"]==c)]["e"].values[0]
    j = data.loc[(data["c"]==c)]["j"].values[0]
    popt, pcov = curve_fit(func, e[index:], j[index:])
    A.append(popt[0])
    B.append(popt[1])
    print("for c="+str(c)+" fit parameters:"+str(popt))
    plt.scatter(e, j,marker=marker[i%5],color=colors[i%5], label="Original Noised Data")
    # plt.plot(e[index:], func(e[index:],*popt),color=colors[i%5], label="Fitted Curve")
    i+=1
# plt.xlim([0,3])
plt.legend(frameon=False)
plt.show()

# def squared(x,a,b,d):
#     return a*x**b+d

# popt, pcov = curve_fit(squared, C, A)
# plt.plot(C,A)
# plt.plot(C,squared(C-0.8,-21000,2,11000))
# plt.show()
# plt.plot(C,B)
# plt.show()
# # for c in [0.8, 0.9, 1.0]:
# #     e = data.loc[(data["c"]==c)]["e"].values[0]
# #     j = data.loc[(data["c"]==c)]["j"].values[0]
# #     popt, pcov = curve_fit(func, e[index:], j[index:])
# #     plt.scatter(e, j,marker=marker[i%5],color=colors[i%5], label="Original Noised Data")
# #     # plt.plot(e[index:], func(e[index:],*popt),color=colors[i%5], label="Fitted Curve")
# #     i+=1
# # plt.xlim([0,4])
# # plt.legend(frameon=False)
# # plt.show()
# # for c in [1.1, 1.2, 1.3, 1.4]:
# #     e = data.loc[(data["c"]==c)]["e"].values[0]
# #     j = data.loc[(data["c"]==c)]["j"].values[0]
# #     popt, pcov = curve_fit(func, e[index:], j[index:])
# #     plt.scatter(e, j,marker=marker[i%5],color=colors[i%5], label="Original Noised Data")
# #     # plt.plot(e[index:], func(e[index:],*popt),color=colors[i%5], label="Fitted Curve")
# #     i+=1
# # plt.xlim([0,4])
# # plt.legend(frameon=False)
# # plt.show()
