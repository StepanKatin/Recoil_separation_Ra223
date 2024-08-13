import numpy as np
import matplotlib.pyplot as plt
import recoil_nuclear_classes_and_defs as cnst
from model_electric_field import EF_dict, X, Y, r_sphere, l_needle, r_needle 


#Add initial parameters

RN_mass = 223
RN_charge = 2
RN_velocity = 370_000 #m/s

radius_cam = 0.07 # m
P = 5*10e-5 #Pa
volume_cam = 4/3*np.pi*radius_cam**3

air_area = cnst.Air(P, volume_cam, T=300)

#Import Electric fieald
'''Напряженность электрического поля была получена в другом файле, было проведено моделирование напряженности поля в пространстве 7х7 см, при координатах иглы 
needle_cords_1 = [[0, 0.06], [0, 0.05], [0, 0.04], [0, 0.03], [0, 0.02], [0, 0.01]] и приложенного к ней наприяжения U = [100, 250, 500, 1000, 2000, 10_000],
для каждого расстояния провеленом моделирование по всем шести элементам напряжения, ключи  к датам E_x, E_y, E_res'''









