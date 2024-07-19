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





class RecoilNuclide:

    def __init__(self, energy, charge, mass, Z_EFF):
        """energy in eV, charge in abs charge of pozitron mass in Da"""
        self.energy = energy
        self.mass = mass
        self.charge = charge
        self.masskilo = mass*MASS_TO_KILO
        self.eff_charge = Z_EFF


    def recoil_vel(self):
        """func rerurn recoil nuclide velocity in metr per second """
        
        return ((2*self.energy *EV_TO_J)/self.masskilo)**0.5
    
    def energy_loss(V, airmass, aircharge, airdencity):
        B = V/SPEED_OF_LIGHT
        Vklad_sred=((Z_air*(Z**2)*air_density)/(A_air*(B**2)))
        Vklad_chast = (11.2+m.log((B**2)/(Z_air*(1-B**2)))-B**2)
        dE = 3.1*10**(5)*Vklad_sred*Vklad_chast
        dEdx.append(dE)
        Etest = Etest + dE
        answer.append(Etest)
        speed.append(V0)




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
        