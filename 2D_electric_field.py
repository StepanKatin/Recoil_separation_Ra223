import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm, ticker
import recoil_nuclear_classes_and_defs as cnst
# Определяем размеры сетки

#если принять размер сферы за единицу то пространство вне сферы будет составлять плоскость 14х14
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
r_needle = 0.0005 #metrs

volume_sph = (4/3) * np.pi * r_sphere**3 # m3

c_sphere = 4*np.pi*cnst.EPS0*r_sphere 
#емкость иглы как емкость цилиндра

c_needle = (2*np.pi*cnst.EPS0*l_needle)/(np.log(2*l_needle/r_needle)) # Фарад

# Напряжение

U = 100 # Volt

# Координаты точечных зарядов
q_sphere_x, q_sphere_y = 0, 0  # заряд находится в центре

q_needl_x, q_needl_y = 0, 0.045 # конец иглы находится на расстоянии 4 см от центра сферы

# Величина зарядов
q_sph = c_sphere*U  # в кулонах

q_needl = -c_needle*U # Kl

# Константы
epsilon_0 = cnst.EPS0 # Электрическая постоянная, Ф/м

# Создание сетки точек в плоскости xy

r1 = np.sqrt(X_axis**2 + Y_axis**2)

r2 = np.sqrt(X_axis**2 + (Y_axis - q_needl_y)**2)

# Инициализация массивов для компонент поля
E_x = np.zeros_like(X_axis)
E_y = np.zeros_like(Y_axis)

# Поле от первой сферы
outside1 = r1 > r_sphere

inside1 = r1 <= r_sphere
E_x[outside1] += (1 / (4 * np.pi * epsilon_0)) * (q_sph * X_axis[outside1]) / (r1[outside1]**3)
E_y[outside1] += (1 / (4 * np.pi * epsilon_0)) * (q_sph * Y_axis[outside1]) / (r1[outside1]**3)

E_x[inside1] += (1 / (4 * np.pi * epsilon_0)) * (q_sph * X_axis[inside1]) / (r_sphere**3)
E_y[inside1] += (1 / (4 * np.pi * epsilon_0)) * (q_sph * Y_axis[inside1]) / (r_sphere**3)

# Поле от второй сферы
outside2 = r2 > r_needle

inside2 = r2 <= r_needle

E_x[outside2] += (1 / (4 * np.pi * epsilon_0)) * (q_needl * X_axis[outside2]) / (r2[outside2]**3)
E_y[outside2] += (1 / (4 * np.pi * epsilon_0)) * (q_needl * (Y_axis[outside2] - q_needl_y)) / (r2[outside2]**3)

E_x[inside2] += (1 / (4 * np.pi * epsilon_0)) * (q_needl * X_axis[inside2]) / (r_needle**3)
E_y[inside2] += (1 / (4 * np.pi * epsilon_0)) * (q_needl * (Y_axis[inside2] - q_needl_y)) / (r_needle**3)


def cylinder_field(X, Y, lambda_c, R_c, h_c, d_y):

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
    E_cx[mask_outside] = (lambda_c * X[mask_outside]) / (2 * np.pi * epsilon_0 * r_c[mask_outside]**2)
    E_cy[mask_outside] = ((lambda_c * Y_shifted[mask_outside]) / (2 * np.pi * epsilon_0 * r_c[mask_outside]**2))
        
    return E_cx, E_cy

E_c_x, E_c_y = cylinder_field(X_axis, Y_axis, q_needl, 0.001, 0.03, 0.046)

# Суммарное поле
E_x_total = E_x + E_c_x
E_y_total = E_y + E_c_y
total = np.sqrt(E_x_total**2 + E_y_total**2)



# Визуализация поля
fig, ax = plt.subplots()
color = np.log(np.sqrt(E_x_total**2 + E_y_total**2))
strm = ax.streamplot(X_axis, Y_axis, E_x_total, E_y_total, color=color, linewidth=1, cmap='viridis', density=2)
circle1 = plt.Circle((0, 0), r_sphere, color='r', fill=True)
circle2 = plt.Circle((0, q_needl_y), r_needle, color='b', fill=True)
rect= plt.Rectangle((-0.001, 0.046), width=0.002, height=0.03, color = 'b', fill = True)
ax.add_artist(circle1)
ax.add_artist(circle2)
ax.add_artist(rect)
ax.set_xlabel('x (м)')
ax.set_ylabel('y (м)')
ax.set_title('Электростатическое поле между двумя заряженными сферами')
plt.gca().set_aspect('equal', adjustable='box')
plt.colorbar(strm.lines)


# plot data

figg, axg= plt.subplots(figsize=(10, 6))

cbr1=axg.imshow(total, origin="lower", extent=(x_min, x_max, y_min, x_max), cmap="RdGy")

figg.colorbar(cbr1, ax=axg)


figg, axx = plt.subplots()

cs = axx.contourf(X_axis, Y_axis, total, locator=ticker.LogLocator(), cmap=cm.PuBu_r)

figg.colorbar(cs, ax=axx, cmap = "RdGy")

plt.show()

