import numpy as np
import matplotlib.pyplot as plt

marker = [".","v","^","s","D","o"]
colors = ["#1f77b4","#ff7f0e","#2ca02c","#9467bd","#8c564b","#e377c2","#7f7f7f","#17becf"]

j=0
for i in np.linspace(0.2,1.0,5):
    right = np.loadtxt("right_c_"+str(round(i,2))+".txt",comments="#",delimiter=";")

    plt.rc('text', usetex=True)
    plt.rc('font', family='serif',size=14)
    
    plt.plot(right[:,0],right[:,1],marker=marker[j],markersize=3,label=r"c="+str(round(i,2)))
    j+=1


plt.legend(ncol=2,frameon=False)
plt.xlabel(r"$\varepsilon$",fontsize=20)
h=plt.ylabel("j",fontsize=20)
h.set_rotation(0)
plt.hlines(y=0,xmin=0,xmax=2,colors="black",linewidth=1)
plt.xlim([0,2])
# plt.ylim([-100,350])
plt.savefig("discrete_righthook_varying_c_small.pdf")
plt.show()

j=0

for i in [0.05, 1.0, 2.0, 3.0, 4.0, 5.0]:
    sym = np.loadtxt("right_c_"+str(round(i,2))+".txt",comments="#",delimiter=";")

    plt.rc('text', usetex=True)
    plt.rc('font', family='serif',size=14)
    
    plt.plot(sym[:,0],sym[:,1],marker=marker[j],markersize=3,label=r"c="+str(round(i,2)))
    j+=1


plt.legend(ncol=2,frameon=False)
plt.xlabel(r"$\varepsilon$",fontsize=20)
h=plt.ylabel("j",fontsize=20)
h.set_rotation(0)
plt.hlines(y=0,xmin=-2,xmax=2,colors="black",linewidth=1)
# plt.vlines(x=0,ymin=-0.3000,ymax=0.2300,colors="black",linewidth=1)
# plt.vlines(x=0,ymin=0.2800,ymax=0.3000,colors="black",linewidth=1)
plt.xlim([0,4])
plt.ylim([-0.2000,0.5000])
plt.savefig("discrete_righthook_results_varying_c.pdf")
plt.show()

for i in [0.05, 0.2, 0.4, 0.6, 0.8, 1.0, 2.0, 3.0, 4.0, 5.0]:
    sym = np.loadtxt("right_c_"+str(round(i,2))+".txt",comments="#",delimiter=";")

    plt.rc('text', usetex=True)
    plt.rc('font', family='serif',size=14)
    
    plt.plot(sym[:,0],sym[:,1],marker=marker[j%len(marker)],markersize=3,label=r"c="+str(round(i,2)))
    j+=1


plt.legend(ncol=2,frameon=False)
plt.xlabel(r"$\varepsilon$",fontsize=20)
h=plt.ylabel("j",fontsize=20)
h.set_rotation(0)
plt.hlines(y=0,xmin=-2,xmax=2,colors="black",linewidth=1)
# plt.vlines(x=0,ymin=-0.3000,ymax=0.2300,colors="black",linewidth=1)
# plt.vlines(x=0,ymin=0.2800,ymax=0.3000,colors="black",linewidth=1)
plt.xlim([0,4])
plt.ylim([-0.2000,0.5000])
plt.savefig("varyingc_3.pdf")
plt.show()
