SPEED_OF_LIGHT = 299_792_458  # м/с
GRAVITATIONAL_CONSTANT = 6.67430e-11  # м^3 кг^−1 с^−2
PLANCK_CONSTANT = 6.62607015e-34  # Дж с
MASS_ELECTRON_KILLO = 9.1093837015*10**(-31)  #кг масса электрона
MASS_ELECTRON_EV = 511000 #эВ масса покоя электрона
EV_TO_J = 1.602176634*10**(-19) #переводной коэф из эВ в Дж
MASS_TO_KILO = 1.66053906660*10**(-27) #переводной коэф из а.е.м. в кг
AVOGADRO_NUMBER = 6.02214076*10**(23)  #число авогадро
GAS_CONSTANT = 8.314

class RecoilNuclide:

    def __init__(self, energy, charge, mass):
        """energy in eV, charge in abs charge of pozitron mass in Da"""
        self.energy = energy
        self.__mass = mass
        self.__charge = charge
        self.__masskilo = mass*MASS_TO_KILO
    
    def recoil_vel(self):
        """func rerurn recoil nuclide velocity in metr per second """
        
        return ((2*self.energy *EV_TO_J)/self.__masskilo)**0.5
    
    def B_coeff(self):
        """func return B coef for Bete-Blox"""
        return self.recoil_vel()/SPEED_OF_LIGHT
    



class Area:
    def __init__(self, pressure, volume, temp, gazmass):
        
        self.pressure = pressure
        self.volume = volume
        self.temp = temp
        self.gazmass = gazmass

    def find_molarity(self):
        """this func return molarity of area"""
        return (self.pressure*self.volume)/(GAS_CONSTANT*self.temp)
    
    def find_num_of_atoms(self):
        """this func return count of area atoms"""
        return self.find_molarity()*AVOGADRO_NUMBER
    
    def find_gas_mass(self):
        return self.find_molarity()*self.gazmass
        

air = Area(0.00005, 1, 300)

print(air.find_num_of_atoms())