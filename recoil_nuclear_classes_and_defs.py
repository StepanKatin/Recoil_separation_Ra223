import numpy as np


SPEED_OF_LIGHT = 299_792_458  # м/с
GRAVITATIONAL_CONSTANT = 6.67430e-11  # м^3 кг^−1 с^−2
PLANCK_CONSTANT = 6.62607015e-34  # Дж с
MASS_ELECTRON_KILLO = 9.1093837015*10**(-31)  #кг масса электрона
MASS_ELECTRON_EV = 511000 #эВ масса покоя электрона
EV_TO_J = 1.602176634*10**(-19)
MASS_TO_KILO = 1.66053906660*10**(-27) 
CHARGE_ELECRON = 1.60219e-19  # заряд электрона в Кл
AIR_IONISATION = 12.8 # eV
""" сечение взаимодействия - dE/dx, рассчет происходит внтутри функции, длинна пробега вычесляется по шагу == 0,01 см, в результате хочу получить график dE/dx от E/Mc**2, N/N0 от R,
далее сравнить такой рассчет с расчетом из статьи <Range and Range Straggling of 97 keV 224RaParticles in Gases> """

""" в результате на данном этапе будет среднее расстояние пробега, полученное на основе иониз. потер по формуле Бете-Блоха, теории из статьи и книжки

Далее требуется взять код цикла с потерями и добавить к нему рассчет и сравнение напряженности поля, скорректировать траекторию, изобразить это на графике"""


class RecoilNuclide:

    def __init__(self, energy, charge, mass):
        """energy in eV, charge in abs charge of pozitron mass in Da"""
        self.__energy = energy
        self.__mass = mass
        self.__charge = charge
        self.__masskilo = mass*MASS_TO_KILO


    def recoil_vel(self):
        """func rerurn recoil nuclide velocity in metr per second """
        
        return ((2*self.__energy *EV_TO_J)/self.__masskilo)**0.5
    
    def stopping_power_air(energy_at_t, charge_nucl):
        energy_keV = np.array([10, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])
        sigma_m2 = np.array([2.5e-18, 1.2e-18, 8.5e-19, 6.0e-19, 4.5e-19, 3.8e-19, 3.2e-19, 2.8e-19, 2.5e-19, 2.2e-19, 2.0e-19, 1.8e-19])

        # Интерполяция данных для получения сечения при 100 кэВ
        sigma_ionization = (K * Z_alpha**2) / E_alpha  # сечение ионизации в м^2
        energy_alpha = 100  # кэВ
        sigma_alpha = np.interp(energy_alpha, energy_keV, sigma_m2)

        





""" Для вычисления сечения ионизации альфа-частицы (с зарядом Z=2) в воздухе с энергией 100 кэВ можно использовать следующий код
import numpy as np

# Константы
e = 1.60219e-19  # заряд электрона в Кл
m_e = 9.10938e-31  # масса электрона в кг
c = 3e8  # скорость света в м/с
Z_alpha = 2  # заряд альфа-частицы
E_alpha = 100e3 * e  # энергия альфа-частицы в Дж (100 кэВ)
I_air = 85 * e  # средний потенциал ионизации воздуха в Дж

# Упрощенная формула для сечения ионизации
K = 1e-16  # эмпирическая константа, м^2*эВ (примерное значение)
sigma_ionization = (K * Z_alpha**2) / E_alpha  # сечение ионизации в м^2

print(f"Сечение ионизации альфа-частицы: {sigma_ionization:.2e} м^2")

# Для проверки результата используем плотность молекул воздуха
rho_air = 1.225  # плотность воздуха в кг/м^3
M_air = 28.97e-3  # молекулярная масса воздуха в кг/моль
N_A = 6.022e23  # постоянная Авогадро, молекул/моль

# Вычисление плотности молекул воздуха
n_air = (rho_air / M_air) * N_A  # молекул/м^3

# Вероятность взаимодействия на пути длиной 0.1 м
L = 0.1  # длина пути в м
P = 1 - np.exp(-n_air * sigma_ionization * L)
print(f"Вероятность взаимодействия: {P:.5f}")

# Вычисление плотности молекул воздуха
n_air = (rho_air / M_air) * N_A  # молекул/м^3

# Вероятность взаимодействия на пути длиной 0.1 м
L = 0.1  # длина пути в м
P = 1 - np.exp(-n_air * sigma_ionization

# Моделирование методом Монте-Карло
num_particles = 10000
num_interactions = 0

for _ in range(num_particles):
    if np.random.rand() < P:
        num_interactions += 1

# Вычисление доли частиц, взаимодействующих с веществом
interaction_fraction = num_interactions / num_particles
print(f"Доля взаимодействующих частиц: {interaction_fraction:.5f}")

# Считывание данных из файла NIST или базы данных (пример)
# Эти данные можно загрузить вручную с сайта NIST
# Примерные данные для альфа-частиц с энергией 100 кэВ в азоте
energy_keV = np.array([10, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])
sigma_m2 = np.array([2.5e-18, 1.2e-18, 8.5e-19, 6.0e-19, 4.5e-19, 3.8e-19, 3.2e-19, 2.8e-19, 2.5e-19, 2.2e-19, 2.0e-19, 1.8e-19])

# Интерполяция данных для получения сечения при 100 кэВ
energy_alpha = 100  # кэВ
sigma_alpha = np.interp(energy_alpha, energy_keV, sigma_m2)

print(f"Сечение взаимодействия альфа-частицы с азотом при {energy_alpha} кэВ: {sigma_alpha:.2e} м^2")

# Построение графика сечений взаимодействия
plt.plot(energy_keV, sigma_m2, marker='o')
plt.xlabel('Энергия (кэВ)')
plt.ylabel('Сечение взаимодействия (м^2)')
plt.title('Сечение взаимодействия альфа-частиц с азотом')
plt.grid(True)
plt.show()


import numpy as np
import matplotlib.pyplot as plt

# Константы
e = 1.60219e-19  # заряд электрона в Кл
m_e = 9.10938e-31  # масса электрона в кг
c = 3e8  # скорость света в м/с
Z_air = 7.6  # атомный номер воздуха (среднее для N2 и O2)
I_air = 85 * e  # средний потенциал ионизации воздуха в Дж
rho_air = 1.225  # плотность воздуха в кг/м^3
M_air = 28.97e-3  # молекулярная масса воздуха в кг/моль
N_A = 6.022e23  # постоянная Авогадро, молекул/моль

# Вычисление плотности молекул воздуха
n_air = (rho_air / M_air) * N_A  # молекул/м^3

# Функция для вычисления потери энергии на единицу длины (dE/dx) по формуле Бете-Блоха
def dE_dx(E, beta, n, Z, I):
    term1 = (4 * np.pi * (2 * e)**2 * e**2) / (m_e * c**2)
    term2 = (n * Z) / beta**2
    term3 = np.log((2 * m_e * c**2 * beta**2) / (I * (1 - beta**2))) - beta**2
    return term1 * term2 * term3

# Начальная энергия альфа-частицы
initial_energy = 100e3 * e  # 100 кэВ в Дж

# Начальные условия
current_energy = initial_energy
position = 0.0  # начальная позиция в м
m_alpha = 4 * 1.66e-27  # масса альфа-частицы в кг

# Списки для хранения данных для построения графика
energies = []
positions = []

# Параметры моделирования
step_length = 1e-6  # длина шага в м

while current_energy > 0:
    # Обновление позиции
    position += step_length
    
    # Скорость альфа-частицы
    v_alpha = np.sqrt(2 * current_energy / m_alpha)  # скорость в м/с
    beta = v_alpha / c  # относительная скорость

    # Вероятность столкновения (приближенная для небольших шагов)
    sigma = 1e-16 * 1e-4  # примерное сечение взаимодействия в м^2
    P_collision = sigma * n_air * step_length
    
    # Случайное число для моделирования вероятности столкновения
    random_number = np.random.rand()
    
    # Если произошло столкновение, то происходит потеря энергии
    if random_number < P_collision:
        energy_loss = dE_dx(current_energy, beta, n_air, Z_air, I_air) * step_length
        current_energy -= energy_loss
    
    # Сохраняем текущие значения для построения графика
    energies.append(current_energy / e)  # сохраняем энергию в эВ
    positions.append(position)
    
    # Если энергия становится отрицательной, останавливаем цикл
    if current_energy < 0:
        current_energy = 0
        energies[-1] = 0

# Построение графика потери энергии
plt.figure(figsize=(10, 6))
plt.plot(positions, energies, label='Энергия альфа-частицы')
plt.xlabel('Путь, м')
plt.ylabel('Энергия, эВ')
plt.title('Потеря энергии альфа-частицы в воздухе методом Монте-Карло')
plt.legend()
plt.grid(True)
plt.show()



import numpy as np
import matplotlib.pyplot as plt

# Константы
k = 8.99e9  # Константа Кулона, Н·м²/Кл²
q1 = 1e-9  # Заряд источника поля, Кл
q2 = 1e-10  # Заряд тестовой частицы, Кл
m = 1e-6  # Масса тестовой частицы, кг

# Начальные условия
r0 = np.array([0.0, 0.0])  # Положение источника поля
r = np.array([0.1, 0.1])  # Начальное положение тестовой частицы
v = np.array([0.0, 0.0])  # Начальная скорость тестовой частицы

# Параметры моделирования
dt = 1e-4  # Шаг времени, с
num_steps = 10000  # Количество шагов моделирования

# Векторы для хранения траектории частицы
trajectory = np.zeros((num_steps, 2))

# Функция для вычисления электростатической силы
def compute_force(r):
    r_vec = r - r0
    r_mag = np.linalg.norm(r_vec)
    r_hat = r_vec / r_mag
    force_mag = k * q1 * q2 / r_mag**2
    force = force_mag * r_hat
    return force

# Моделирование траектории
for step in range(num_steps):
    force = compute_force(r)
    a = force / m
    v += a * dt
    r += v * dt
    trajectory[step] = r

# Визуализация траектории
plt.plot(trajectory[:, 0], trajectory[:, 1], label='Траектория частицы')
plt.scatter(r0[0], r0[1], color='red', label='Источник поля (q1)')
plt.xlabel('x (м)')
plt.ylabel('y (м)')
plt.legend()
plt.title('Моделирование траектории заряженной частицы в электростатическом поле')
plt.grid(True)
plt.show()



import numpy as np
import matplotlib.pyplot as plt

# Константы
k = 8.99e9  # Константа Кулона, Н·м²/Кл²
q1 = 1e-9  # Заряд источника поля, Кл
q2 = 1e-10  # Заряд тестовой частицы, Кл
m = 1e-6  # Масса тестовой частицы, кг

# Начальные условия
r0 = np.array([0.0, 0.0])  # Положение источника поля
r = np.array([0.1, 0.1])  # Начальное положение тестовой частицы
v = np.array([0.0, 0.0])  # Начальная скорость тестовой частицы

# Параметры моделирования
dt = 1e-4  # Шаг времени, с
num_steps = 10000  # Количество шагов моделирования

# Векторы для хранения траектории частицы
trajectory = np.zeros((num_steps, 2))

# Функция для вычисления электростатической силы
def compute_force(r):
    r_vec = r - r0
    r_mag = np.linalg.norm(r_vec)
    r_hat = r_vec / r_mag
    force_mag = k * q1 * q2 / r_mag**2
    force = force_mag * r_hat
    return force

# Моделирование траектории
for step in range(num_steps):
    force = compute_force(r)
    a = force / m
    v += a * dt
    r += v * dt
    trajectory[step] = r

# Визуализация траектории
plt.plot(trajectory[:, 0], trajectory[:, 1], label='Траектория частицы')
plt.scatter(r0[0], r0[1], color='red', label='Источник поля (q1)')
plt.xlabel('x (м)')
plt.ylabel('y (м)')
plt.legend()
plt.title('Моделирование траектории заряженной частицы в электростатическом поле')
plt.grid(True)
plt.show()



3d график пример кода
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Константы
k = 8.99e9  # Константа Кулона, Н·м²/Кл²
q1 = 1e-9  # Заряд источника поля, Кл
q2 = 1e-10  # Заряд тестовой частицы, Кл
m = 1e-6  # Масса тестовой частицы, кг

# Начальные условия
r0 = np.array([0.0, 0.0, 0.0])  # Положение источника поля
r = np.array([0.1, 0.1, 0.1])  # Начальное положение тестовой частицы
v = np.array([0.0, 0.0, 0.0])  # Начальная скорость тестовой частицы

# Параметры моделирования
dt = 1e-4  # Шаг времени, с
num_steps = 10000  # Количество шагов моделирования

# Векторы для хранения траектории частицы
trajectory = np.zeros((num_steps, 3))

# Функция для вычисления электростатической силы
def compute_force(r):
    r_vec = r - r0
    r_mag = np.linalg.norm(r_vec)
    r_hat = r_vec / r_mag
    force_mag = k * q1 * q2 / r_mag**2
    force = force_mag * r_hat
    return force

# Моделирование траектории
for step in range(num_steps):
    force = compute_force(r)
    a = force / m
    v += a * dt
    r += v * dt
    trajectory[step] = r

# Визуализация траектории
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(trajectory[:, 0], trajectory[:, 1], trajectory[:, 2], label='Траектория частицы')
ax.scatter(r0[0], r0[1], r0[2], color='red', label='Источник поля (q1)')
ax.set_xlabel('x (м)')
ax.set_ylabel('y (м)')
ax.set_zlabel('z (м)')
ax.legend()
ax.set_title('Моделирование траектории заряженной частицы в электростатическом поле')
plt.show()


"""




