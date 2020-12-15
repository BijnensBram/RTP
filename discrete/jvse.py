import numpy as np
import matplotlib.pyplot as plt

marker = [".","v","^","s","D","o"]
colors = ["#1f77b4","#ff7f0e","#2ca02c","#9467bd","#8c564b","#e377c2","#7f7f7f","#17becf"]

# j=0
# for i in np.linspace(0.4,0.8,3):
#     right = np.loadtxt("right_a_"+str(round(i,2))+"_c0.5.txt",comments="#",delimiter=";")

#     plt.rc('text', usetex=True)
#     plt.rc('font', family='serif',size=14)
    
#     plt.plot(right[:,0],right[:,1],marker=marker[j],markersize=3,label=r"a="+str(round(i,2)))
#     j+=1


# plt.legend(ncol=2,frameon=False)
# plt.xlabel(r"$\epsilon$")
# h=plt.ylabel("j")
# h.set_rotation(0)
# plt.hlines(y=0,xmin=0,xmax=2,colors="black",linewidth=1)
# plt.xlim([0,2])
# # plt.ylim([-100,350])
# plt.savefig("exptime_discrete_righthook_results_a_c05.pdf")
# plt.show()

# j=0

# for i in np.linspace(0.4,0.8,3):
#     sym = np.loadtxt("sym_a_"+str(round(i,2))+"_c0.5.txt",comments="#",delimiter=";")

#     plt.rc('text', usetex=True)
#     plt.rc('font', family='serif',size=14)
    
#     plt.plot(sym[:,0],sym[:,1],marker=marker[j],markersize=3,label=r"a="+str(round(i,2)))
#     j+=1


# plt.legend(ncol=2,frameon=False)
# plt.xlabel(r"$\epsilon$")
# h=plt.ylabel("j")
# h.set_rotation(0)
# plt.hlines(y=0,xmin=-2,xmax=2,colors="black",linewidth=1)
# plt.vlines(x=0,ymin=-3000,ymax=2300,colors="black",linewidth=1)
# plt.vlines(x=0,ymin=2800,ymax=3000,colors="black",linewidth=1)
# plt.xlim([-2,2])
# plt.ylim([-3000,3000])
# plt.savefig("exptime_discrete_symhook_results_a_c05.pdf")
# plt.show()

# j=0
# for i in np.linspace(0.4,0.8,3):
#     right = np.loadtxt("right_a_"+str(round(i,2))+"_c0.5.txt",comments="#",delimiter=";")

#     plt.rc('text', usetex=True)
#     plt.rc('font', family='serif',size=14)
    
#     plt.plot(right[:,0],right[:,1],marker=marker[j],markersize=3,label=r"a="+str(round(i,2)))
#     j+=1


# plt.legend(ncol=2,frameon=False)
# plt.xlabel(r"$\epsilon$")
# h=plt.ylabel("j")
# h.set_rotation(0)
# plt.hlines(y=0,xmin=0,xmax=2,colors="black",linewidth=1)
# plt.xlim([0.4,0.9])
# plt.ylim([600,1000])
# plt.savefig("exptime_discrete_righthook_results_a_c05_zoom.pdf")
# plt.show()

j=0
for i in np.linspace(0.4,0.8,3):
    right = np.loadtxt("right_a_"+str(round(i,2))+"_c1.0.txt",comments="#",delimiter=";")

    plt.rc('text', usetex=True)
    plt.rc('font', family='serif',size=14)
    
    plt.plot(right[:,0],right[:,1],marker=marker[j],markersize=3,label=r"a="+str(round(i,2)))
    j+=1


plt.legend(ncol=2,frameon=False)
plt.xlabel(r"$\epsilon$")
h=plt.ylabel("j")
h.set_rotation(0)
plt.hlines(y=0,xmin=0,xmax=2,colors="black",linewidth=1)
plt.xlim([0,2])
# plt.ylim([-100,350])
plt.savefig("exptime_discrete_righthook_results_a_c1.pdf")
plt.show()

j=0

for i in np.linspace(0.4,0.8,3):
    sym = np.loadtxt("sym_a_"+str(round(i,2))+"_c1.0.txt",comments="#",delimiter=";")

    plt.rc('text', usetex=True)
    plt.rc('font', family='serif',size=14)
    
    plt.plot(sym[:,0],sym[:,1],marker=marker[j],markersize=3,label=r"a="+str(round(i,2)))
    j+=1


plt.legend(ncol=2,frameon=False)
plt.xlabel(r"$\epsilon$")
h=plt.ylabel("j")
h.set_rotation(0)
plt.hlines(y=0,xmin=-2,xmax=2,colors="black",linewidth=1)
plt.vlines(x=0,ymin=-3000,ymax=2300,colors="black",linewidth=1)
plt.vlines(x=0,ymin=2800,ymax=3000,colors="black",linewidth=1)
plt.xlim([-2,2])
plt.ylim([-3000,3000])
plt.savefig("exptime_discrete_symhook_results_a_c1.pdf")
plt.show()

j=0
for i in np.linspace(0.4,0.8,3):
    right = np.loadtxt("right_a_"+str(round(i,2))+"_c1.0.txt",comments="#",delimiter=";")

    plt.rc('text', usetex=True)
    plt.rc('font', family='serif',size=14)
    
    plt.plot(right[:,0],right[:,1],marker=marker[j],markersize=3,label=r"a="+str(round(i,2)))
    j+=1


plt.legend(ncol=2,frameon=False)
plt.xlabel(r"$\epsilon$")
h=plt.ylabel("j")
h.set_rotation(0)
plt.hlines(y=0,xmin=0,xmax=2,colors="black",linewidth=1)
plt.xlim([0.4,0.9])
plt.ylim([600,1000])
plt.savefig("exptime_discrete_righthook_results_$c1_zoom.pdf")
plt.show()
