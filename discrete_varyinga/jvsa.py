import numpy as np
import matplotlib.pyplot as plt

marker = [".","v","^","s","D","o"]
colors = ["#1f77b4","#ff7f0e","#2ca02c","#9467bd","#8c564b","#e377c2","#7f7f7f","#17becf"]

j=0
for i in [0.9, 1.0,1.05,  1.1,1.2, 1.3, 1.4]:
    right1 = np.loadtxt("varyinga_right_e_"+str(round(i,2))+"_c1.txt",comments="#",delimiter=";")
    right2 = np.loadtxt("2varyinga_right_e_"+str(round(i,2))+"_c1.txt",comments="#",delimiter=";")
    right = right1 + right2
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif',size=14)
    
    plt.plot(right[:,0],right[:,1],marker=marker[j],markersize=3,label=r"$\epsilon$="+str(round(i,2)))
    j+=1
    if j > 5:
        j=0

plt.legend(ncol=1,frameon=False,loc="lower left")
plt.xlabel(r"$a$")
h=plt.ylabel("j")
h.set_rotation(0)
plt.hlines(y=0,xmin=0,xmax=20,colors="black",linewidth=1)
plt.xlim([0,10])
plt.ylim([-2000,3000])
plt.savefig("discrete_righthook_varyinga_c1.pdf")
plt.show()

j=1
plt.figure(figsize=(8,4))
for i in [1.0, 1.05, 1.1]:
    right1 = np.loadtxt("varyinga_right_e_"+str(round(i,2))+"_c1.txt",comments="#",delimiter=";")
    right2 = np.loadtxt("2varyinga_right_e_"+str(round(i,2))+"_c1.txt",comments="#",delimiter=";")
    right = right1 + right2

    plt.rc('text', usetex=True)
    plt.rc('font', family='serif',size=14)
    
    plt.plot(right[1:,0],right[1:,1],marker=marker[j],markersize=3,label=r"$\epsilon$="+str(round(i,2)))
    j+=1
    if j > 5:
        j=0

plt.xlim([0,10])
# plt.ylim([-1000,1500])
plt.savefig("discrete_righthook_varyinga_c1_zoom.pdf")
plt.show()

j=0
for i in [0.5, 0.55, 0.6, 0.65, 0.7, 0.8]:
    right1 = np.loadtxt("varyinga_right_e_"+str(round(i,2))+"_c0.5.txt",comments="#",delimiter=";")
    right2 = np.loadtxt("2varyinga_right_e_"+str(round(i,2))+"_c0.5.txt",comments="#",delimiter=";")
    right = right1 + right2

    plt.rc('text', usetex=True)
    plt.rc('font', family='serif',size=14)
    
    plt.plot(right[:,0],right[:,1],marker=marker[j],markersize=3,label=r"$\epsilon$="+str(round(i,2)))
    j+=1
    if j > 5:
        j=0

plt.legend(ncol=1,frameon=False,loc="lower left")
plt.xlabel(r"$a$")
h=plt.ylabel("j")
h.set_rotation(0)
plt.hlines(y=0,xmin=0,xmax=20,colors="black",linewidth=1)
plt.xlim([0,10])
plt.ylim([-1000,4000])
plt.savefig("discrete_righthook_varyinga_c05.pdf")
plt.show()

j=0
plt.figure(figsize=(8,4))
for i in [0.5, 0.6, 0.7]:
    right1 = np.loadtxt("varyinga_right_e_"+str(round(i,2))+"_c0.5.txt",comments="#",delimiter=";")
    right2 = np.loadtxt("2varyinga_right_e_"+str(round(i,2))+"_c0.5.txt",comments="#",delimiter=";")
    right = right1 + right2

    plt.rc('text', usetex=True)
    plt.rc('font', family='serif',size=14)
    
    plt.plot(right[1:,0],right[1:,1],marker=marker[j],markersize=3,label=r"$\epsilon$="+str(round(i,2)))
    j+=1
    if j > 5:
        j=0

plt.xlim([0,10])
# plt.ylim([-1000,1500])
plt.savefig("discrete_righthook_varyinga_c05_zoom.pdf")
plt.show()
