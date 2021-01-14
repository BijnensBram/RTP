import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.DataFrame(columns=["c","a","e","j"])

for c in [0.5, 1, 1.5]:
    for a in [0.4,0.6,0.8]:
        filename = "./DATA/fitting_c_"+str(c)+"_a_"+str(a)+".txt"
        e, j = np.loadtxt(filename,delimiter=";",comments="#",unpack=True)
        data = data.append({"c":c,"a":a,"e":e,"j":j},ignore_index=True)

data.to_csv("fit_data.csv",index_label=False)
