import numpy as np
import matplotlib.pyplot as plt

marker = [".","v","^","s","D"]
colors = ["#1f77b4","#ff7f0e","#2ca02c","#9467bd","#8c564b","#e377c2","#7f7f7f","#17becf"]

j=0
for i in np.linspace(0.4,0.8,3):
    right = np.loadtxt("right_a_"+str(round(i,2))+".txt",comments="#",delimiter=";")
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif',size=14)
    
    plt.plot(right[:,0],right[:,1],marker=marker[j],color=colors[j],markersize=6,label=r"a="+str(round(i,2)))
    j+=1

plt.legend(ncol=2,frameon=False)

plt.xlabel(r"$\epsilon$")
h=plt.ylabel("j")
h.set_rotation(0)
plt.hlines(y=0,xmin=-1,xmax=1,colors="black",linewidth=1)
plt.xlim([-0,1])
plt.ylim([-500,1000])
plt.savefig("righthook_results_a.pdf")
plt.show()

j=0
for i in np.linspace(0.4,0.8,3):
    sym = np.loadtxt("sym_a_"+str(round(i,2))+".txt",comments="#",delimiter=";")

    plt.rc('text', usetex=True)
    plt.rc('font', family='serif',size=14)
    
    plt.plot(sym[:,0],sym[:,1],marker=marker[j],color=colors[j],label=r"a="+str(round(i,2)))
    j+=1

plt.legend(ncol=2,frameon=False)
plt.xlabel(r"$\epsilon$")
h=plt.ylabel("j")
h.set_rotation(0)
plt.hlines(y=0,xmin=-1,xmax=1,colors="black",linewidth=1)
plt.vlines(x=0,ymin=-1250,ymax=1000,colors="black",linewidth=1)
plt.vlines(x=0,ymin=1200,ymax=1250,colors="black",linewidth=1)
plt.xlim([-1,1])
plt.ylim([-1250,1250])
plt.savefig("symhook_results_a.pdf")
plt.show()
