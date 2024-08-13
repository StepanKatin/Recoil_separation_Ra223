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
A0 = 0.529e-10  # Bohr radius in meters
Z_EFF = 19.65  # Effective charge after considering screening in pozitrons
R = 8.314 #Дж/(моль⋅К)
K = 1.380649e-23 #Дж/К
EPS0 = 8.854e-12 #Ф/м 


def ionisation_losses(velocity, mass, charge):
    B = velocity/SPEED_OF_LIGHT
    Vklad_sred=((Air.charge*(charge**2)*Air.air_density())/(Air.M*(B**2)))
    Vklad_chast = (11.2+np.log((B**2)/(Air.charge*(1-B**2)))-B**2)
    dE = 3.1*10**(5)*Vklad_sred*Vklad_chast
    return recoil_vel(dE)

def recoil_vel(self):
    """func rerurn recoil nuclide velocity in metr per second """
        
    return ((2*self.energy *EV_TO_J)/self.masskilo)**0.5

class Air:
    
    def __init__(self, pressure, volume, T):
        self.pressure = pressure
        self.volume = volume
        self.M = 28.98 #kg/mol
        self.T = T
        self.charge = 7.3
       
    def num_of_moleculs(self):
        return (self.pressure*self.volume)/(K*self.T)
    
    def air_density(self):
        mol = (self.pressure*self.volume)/(R*self.T)
        return (mol*self.M)/self.volume


def calc_electric_field(X, Y, sph_cords, needl_cords, r_sphere, l_needle, r_needle, U):

    c_sphere = 4*np.pi*EPS0*r_sphere  #Фарад 
    c_needle = (2*np.pi*EPS0*l_needle)/(np.log(2*l_needle/r_needle)) # Фарад, емкость иглы как емкость цилиндра
    # Координаты точечных зарядов
    q_sphere_x, q_sphere_y = sph_cords # заряд находится в центре
    q_needl_x, q_needl_y = needl_cords # конец иглы находится на расстоянии 4 см от центра сферы
    # Величина зарядов
    q_sph = c_sphere*U  # в кулонах
    q_needl = -c_needle*U # Kl
    # Константы
    epsilon_0 = EPS0 # Электрическая постоянная, Ф/м
    # Создание сетки точек в плоскости xy
    r1 = np.sqrt(X**2 + Y**2)
    r2 = np.sqrt(X**2 + (Y - q_needl_y)**2)
    # Инициализация массивов для компонент поля
    E_x = np.zeros_like(X)
    E_y = np.zeros_like(Y)
    # Поле от первой сферы
    outside1 = r1 > r_sphere
    inside1 = r1 <= r_sphere
    E_x[outside1] += (1 / (4 * np.pi * epsilon_0)) * (q_sph * X[outside1]) / (r1[outside1]**3)
    E_y[outside1] += (1 / (4 * np.pi * epsilon_0)) * (q_sph * Y[outside1]) / (r1[outside1]**3)
    E_x[inside1] += (1 / (4 * np.pi * epsilon_0)) * (q_sph * X[inside1]) / (r_sphere**3)
    E_y[inside1] += (1 / (4 * np.pi * epsilon_0)) * (q_sph * Y[inside1]) / (r_sphere**3)
    # Поле от второй сферы
    outside2 = r2 > r_needle
    inside2 = r2 <= r_needle
    E_x[outside2] += (1 / (4 * np.pi * epsilon_0)) * (q_needl * X[outside2]) / (r2[outside2]**3)
    E_y[outside2] += (1 / (4 * np.pi * epsilon_0)) * (q_needl * (Y[outside2] - q_needl_y)) / (r2[outside2]**3)
    E_x[inside2] += (1 / (4 * np.pi * epsilon_0)) * (q_needl * X[inside2]) / (r_needle**3)
    E_y[inside2] += (1 / (4 * np.pi * epsilon_0)) * (q_needl * (Y[inside2] - q_needl_y)) / (r_needle**3)
    # Суммарное поле
    E_field_total = np.sqrt(E_x**2 + E_y**2)

    return E_x, E_y, E_field_total




if __name__ == "__main__":
    print('Recoil classes')
