import numpy as np
import matplotlib.pyplot as plt

marker = [".","v","^","s","D","o"]
colors = ["#1f77b4","#ff7f0e","#2ca02c","#9467bd","#8c564b","#e377c2","#7f7f7f","#17becf"]

plt.rc('text', usetex=True)
plt.rc('font', family='serif',size=14)
indata = np.loadtxt("right_inhook.txt",comments="#",delimiter=";")
outdata = np.loadtxt("right_outhook.txt",comments="#",delimiter=";")

    
plt.plot(indata[:,0],indata[:,1],marker=marker[0],markersize=3,label=r"In the hook")
plt.plot(outdata[:,0],outdata[:,1],marker=marker[1],markersize=3,label=r"Out the hook")


plt.legend(ncol=2,frameon=False)
plt.xlabel(r"$\varepsilon$",fontsize=20)
h=plt.ylabel("j",fontsize=20)
h.set_rotation(0)
plt.hlines(y=0,xmin=0,xmax=2,colors="black",linewidth=1)
plt.xlim([0,2])
# plt.ylim([-100,350])
plt.savefig("initial_J_for_different_init.pdf")
plt.show()

