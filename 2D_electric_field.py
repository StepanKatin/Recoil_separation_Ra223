import numpy as np
import matplotlib.pyplot as plt
import recoil_nuclear_classes_and_defs as cnst
# Определяем размеры сетки
#если принять размер сферы за единицу то пространство вне сферы будет составлять плоскость 9х9
x_min = -0.07 # m
x_max = 0.07
y_min, y_max = -0.07 , 0.07 

# Создание сетки пространства
num_points = 1000
x = np.linspace(x_min, x_max, num_points)
y = np.linspace(y_min, y_max, num_points)
X_axis, Y_axis = np.meshgrid(x, y)

#Определяем емкость и заряд электродов
r_sphere = 0.005 #metrs
l_needle = 0.03 #metrs
r_needle = 0.001 #metrs

volume_sph = (4/3) * np.pi * r_sphere**3
c_sphere = 4*np.pi*cnst.EPS0*r_sphere
#емкость иглы как емкость цилиндра
c_needle = (2*np.pi*cnst.EPS0*l_needle)/(np.log(2*l_needle/r_needle))
# Определяем напряжение
u = 100 # Volt
# Координаты точечных зарядов
q_sphere_x, q_sphere_y = 0, 0  # заряд находится в центре

q_needl_x, q_needl_y = 0, 0.045 # конец иглы находится на расстоянии 4 см от центра сферы

# Величина зарядов
q_sph = c_sphere*u  # в кулонах
q_needl = -c_needle*u # Kl


# Константа Кулона
k = 8.9875517873681764e9  # Н·м²/Кл²


E_s_x = np.zeros((num_points, num_points), dtype=float)
E_s_y = np.zeros((num_points, num_points), dtype=float)
E_n_x = np.zeros((num_points, num_points), dtype=float)
E_n_y = np.zeros((num_points, num_points), dtype=float)
E_dot_x = np.zeros((num_points, num_points), dtype=float)
E_dot_y = np.zeros((num_points, num_points), dtype=float)


radius_vecror = np.sqrt(X_axis**2 + Y_axis**2)

#Расчитываем поле вокруг заряженой сферы 
outside = radius_vecror > r_sphere
E_s_x[outside] = abs(1 / (4 * np.pi * cnst.EPS0)) * (q_sph * X_axis[outside]) / (radius_vecror[outside]**3)
E_s_y[outside] = abs(1 / (4 * np.pi * cnst.EPS0)) * (q_sph * Y_axis[outside]) / (radius_vecror[outside]**3)

inside = radius_vecror <= r_sphere
E_s_x[inside] = abs(1 / (4 * np.pi * cnst.EPS0)) * (q_sph * X_axis[inside]) / (r_sphere**3)
E_s_y[inside] = abs(1 / (4 * np.pi * cnst.EPS0)) * (q_sph * Y_axis[inside]) / (r_sphere**3)


#Расчитываем поле от основной части иглы (представляя его цилиндром)

def cylinder_field(X, Y, lambda_c, R_c, h_c, d_y):
    epsilon_0 = 8.854187817e-12  # Вакуумная диэлектрическая проницаемость
    
    E_cx = np.zeros_like(X)
    E_cy = np.zeros_like(Y)
    
    # Маска для точек внутри высоты цилиндра с учетом смещения по оси Y
    mask_height = np.abs(Y - d_y) <= h_c / 2
    
    # Смещенные координаты
    Y_shifted = Y - d_y
    
    # Расстояние до оси цилиндра
    r_c = np.sqrt(X**2 + Y_shifted**2)
    
    # Внешнее поле (r >= R_c)
    mask_outside = (r_c >= R_c) & mask_height
    E_cx[mask_outside] = abs((lambda_c * X[mask_outside]) / (2 * np.pi * epsilon_0 * r_c[mask_outside]**2))
    E_cy[mask_outside] = abs((lambda_c * Y_shifted[mask_outside]) / (2 * np.pi * epsilon_0 * r_c[mask_outside]**2))
    
    # Внутреннее поле (r < R_c)
    mask_inside = (r_c < R_c) & mask_height
    # E_cx[mask_inside] = (lambda_c * X[mask_inside]) / (2 * np.pi * epsilon_0 * R_c**2)
    # E_cy[mask_inside] = (lambda_c * Y_shifted[mask_inside]) / (2 * np.pi * epsilon_0 * R_c**2)
    
    return E_cx, E_cy

E_cx, E_cy = cylinder_field(X_axis, Y_axis, q_needl, r_needle, l_needle, d_y = q_needl_y)
E_n_x += E_cx
E_n_y += E_cy


E_s_res = E_s_x + E_s_y


E_n_res = E_dot_x + E_dot_y + E_cx + E_cy

# Results
E_res_x = E_dot_x + E_cx + E_s_x
E_res_y = E_dot_y + E_cy  + E_s_y
E_res = E_res_x + E_res_y




# plot data

fig, ax= plt.subplots(figsize=(10, 6))

cbr=ax.imshow(E_res, origin="lower", extent=(x_min, x_max, y_min, x_max), cmap="RdGy")

circle = plt.Circle((0, 0), r_sphere, color='r', fill=False)

ax.add_artist(circle)

fig.colorbar(cbr, ax=ax, cmap = "grey")


figg, axx = plt.subplots()

cbb=axx.imshow(E_n_res, origin="lower", extent=(x_min, x_max, y_min, x_max), cmap="RdGy")

figg.colorbar(cbb, ax=axx, cmap = "RdGy")

plt.show()

