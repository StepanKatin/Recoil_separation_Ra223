import numpy as np
import matplotlib.pyplot as plt
import recoil_nuclear_classes_and_defs as cnst
from model_electric_field import EF_dict, X, Y, r_sphere, l_needle, r_needle, x_min, x_max, x, y
from scipy.interpolate import RegularGridInterpolator


#Add initial parameters

RN_mass = 223
RN_charge = 2
RN_velocity = 370_000 #m/s

radius_cam = 0.07 # m
P = 5*10e-5 #Pa
volume_cam = 4/3*np.pi*radius_cam**3

air_area = cnst.Air(P, volume_cam, T=300)
N = 10
#Import Electric fieald
'''Напряженность электрического поля была получена в другом файле, было проведено моделирование напряженности поля в пространстве 7x7 см, при координатах иглы 
needle_cords_1 = [[0, 0.06], [0, 0.05], [0, 0.04], [0, 0.03], [0, 0.02], [0, 0.01]] и приложенного к ней наприяжения U = [100, 250, 500, 1000, 2000, 10_000],
для каждого расстояния провеленом моделирование по всем шести элементам напряжения, ключи  к датам E_x, E_y, E_res'''

Efield_6cm_100V_x, Efield_6cm_100V_y  = EF_dict["E_x"][0], EF_dict["E_y"][0]



dx = 0.00014

max_traect = np.arange(x_min, x_max, dx)

x_serf, y_serf = cnst.source_surface(x, y, r_sphere=r_sphere)

E_field_x = RegularGridInterpolator((x, y), Efield_6cm_100V_x.T)
E_field_y = RegularGridInterpolator((x, y), Efield_6cm_100V_y.T)

def get_electric_field(pos):
    """Получение интерполированных значений электрического поля в позиции pos"""
    if np.any(pos < [x.min(), y.min()]) or np.any(pos > [x.max(), y.max()]):
        raise ValueError("Position out of bounds for the electric field grid.")
    Ex_val = E_field_x(pos)
    Ey_val = E_field_y(pos)
    return np.array([Ex_val, Ey_val])

r = np.zeros((N, len(max_traect), 2))
V = np.zeros((N, len(max_traect), 2))

# Simulation loop for each particle
for j in range(N):
    # Random starting point on the circle
    random_index = np.random.randint(0, len(x_serf))
    random_point = np.array([x_serf[random_index], y_serf[random_index]])

    # Tangential and radial vector calculations
    radius_vector = random_point - np.array([x_serf.mean(), y_serf.mean()])
    tangent_vector = np.array([-radius_vector[1], radius_vector[0]])
    tangent_vector = tangent_vector / np.linalg.norm(tangent_vector)
    
    angle = np.random.uniform(-np.pi/2, np.pi/2)
    direction_vector = (np.cos(angle) * tangent_vector +
                        np.sin(angle) * radius_vector / np.linalg.norm(radius_vector))
    vector_length = dx
    vector = direction_vector * vector_length

    V[j, 0, :] = RN_velocity * direction_vector
    r[j, 0, :] = random_point

    for i in range(1, len(max_traect)):
        # Проверка, что текущая позиция внутри допустимой области
        if np.any(r[j, i-1, :] < [x.min(), y.min()]) or np.any(r[j, i-1, :] > [x.max(), y.max()]):
            print(f"Particle {j+1} left the field at step {i}.")
            break
        
        E = get_electric_field(r[j, i-1, :])
        F = RN_charge * E
        
        # Euler's method for updating velocity and position
        V[j, i, :] = V[j, i-1, :] + (np.linalg.norm(F) / RN_mass) * dx - cnst.ionisation_losses(np.linalg.norm(V[j, i-1, :]), RN_charge, air_area) * V[j, i-1, :] * dx
        r[j, i, :] = r[j, i-1, :] + V[j, i, :] * dx
        
        # Boundary check: stop simulation if the particle leaves the grid
        if (r[j, i, 0] < x[0]).any() or (r[j, i, 0] > x[-1]).any()  or (r[j, i, 1] < y[0]).any()  or (r[j, i, 1] > y[-1]).any() :
            r[j, i:, :] = r[j, i-1, :] # Mark the remaining trajectory as invalid


# Plot the trajectories of particles
plt.figure(figsize=(10, 8))
for i in range(N):
    plt.plot(r[i, :, 0], r[i, :, 1], label=f'Particle {i+1}')

# Plot settings
plt.xlabel('X position')
plt.ylabel('Y position')
plt.title('Trajectories of Particles')
plt.legend()
plt.grid(True)
plt.axis('equal')  # Ensure equal scaling on both axes

plt.show()

# #Визуализация траекторий частиц
# plt.figure(figsize=(10, 8))
# for i in range(N):
#     plt.plot(r[i, :,0], r[i, : ,1], label=f'Particle {i+1}')

# # Настройки графика
# plt.xlabel('X position')
# plt.ylabel('Y position')
# plt.title('Trajectories of Particles')
# plt.legend()
# plt.grid(True)
# plt.axis('equal')  # Это обеспечит равные масштабы по осям X и Y

# # Отображение графика
# plt.show()
















