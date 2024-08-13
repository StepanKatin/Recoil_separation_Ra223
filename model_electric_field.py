import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm, ticker
import recoil_nuclear_classes_and_defs as cnst

x_min = -0.07 # m
x_max = 0.07
y_min, y_max = -0.07 , 0.07

r_sphere = 0.005 #metrs
l_needle = 0.03 #metrs
r_needle = 0.0005 #metrs

sphere_cords = (0, 0)

needle_cords_1 = [[0, 0.06], [0, 0.05], [0, 0.04], [0, 0.03], [0, 0.02], [0, 0.01]]

U = [100, 250, 500, 1000, 2000, 10_000]

x, y = np.linspace(x_min, x_max, 1000), np.linspace(y_min, y_max, 1000)
X, Y =np.meshgrid(x, y)

EF_dict = {'E_x':[[] for i in range(6)], 'E_y':[[] for i in range(6)], 'E_res':[[] for i in range(6)]}
max_strenght = []
max_erea_strenght = []
mean_strenght = []
for i in range(len(needle_cords_1)):
    for j in range(len(U)):
        EF_dict['E_x'][i], EF_dict["E_y"][i], EF_dict['E_res'][i] = cnst.calc_electric_field(X, Y, sphere_cords, needle_cords_1[i], r_needle, l_needle, r_needle, U[j])
        max_strenght.append(np.max(EF_dict['E_res'][i]))
        mean_strenght.append(np.mean(EF_dict['E_res'][i]))
        max_erea_strenght.append((np.max(EF_dict['E_res'][i]) >= np.mean(EF_dict['E_res'][i])))




#         figx, axx = plt.subplots()

#         cs = axx.contourf(X, Y,  EF_dict['E_res'][i], locator=ticker.LogLocator(), cmap=cm.PuBu_r)

#         figx.colorbar(cs, ax=axx, cmap = "RdGy")

#plt.show()
