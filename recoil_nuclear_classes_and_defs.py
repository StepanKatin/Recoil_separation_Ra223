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

if __name__ == "__main__":
    print('Recoil classes')
