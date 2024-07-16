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






class RecoilNuclide:

    def __init__(self, energy, charge, mass, Z_EFF):
        """energy in eV, charge in abs charge of pozitron mass in Da"""
        self.energy = energy
        self.mass = mass
        self.charge = charge
        self.masskilo = mass*MASS_TO_KILO
        self.eff_charge = Z_eff


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
