SPEED_OF_LIGHT = 299_792_458  # м/с
GRAVITATIONAL_CONSTANT = 6.67430e-11  # м^3 кг^−1 с^−2
PLANCK_CONSTANT = 6.62607015e-34  # Дж с
MASS_ELECTRON_KILLO = 9.1093837015 * 10 ** (-31)  #кг масса электрона
MASS_ELECTRON_EV = 511000 #эВ масса покоя электрона
EV_TO_J = 1.602176634 * 10 ** (-19) #переводной коэф из эВ в Дж
MASS_TO_KILO = 1.66053906660 * 10 ** (-27) #переводной коэф из а.е.м. в кг
AVOGADRO_NUMBER = 6.02214076 * 10 ** (23)  #число авогадро
GAS_CONSTANT = 8.314 #Дж/моль*К
BOLTSMAN_CONSTANT = 1.380649 * 10 **(23) #Дж/К.


class RecoilNuclide:

    def __init__(self, energy, charge, mass):
        """energy in eV, charge in abs charge of pozitron mass in Da"""
        self.energy = energy
        self.__mass = mass
        self.charge = charge
        self.__masskilo = mass*MASS_TO_KILO
    
    def recoil_vel(self):
        """func rerurn recoil nuclide velocity in metr per second """
        
        return ((2*self.energy *EV_TO_J)/self.__masskilo)**0.5
    
    def B_coeff(self):
        """func return B coef for Bete-Blox"""
        return self.recoil_vel()/SPEED_OF_LIGHT
    



class Area:
    def __init__(self, pressure, volume, temp, gazmass, Z_area, A_area):
        """ pressure in Pa, 
        volume in m3, 
        temp in Kelvin, 
        gazmass in molarity mass, 
        Z_area - mean charge of area in pozitrons, 
        A_area in Da """

        self.pressure = pressure
        self.volume = volume
        self.temp = temp
        self.gazmass = gazmass
        self.volumecm3 = volume*1_000_000
        self.Z_area = Z_area
        self.A_area = A_area 

    def find_molarity(self):
        """   molarity = p*V / R*T  this func return molarity of area"""
        return (self.pressure*self.volume)/(GAS_CONSTANT*self.temp)
    
    def find_num_of_atoms(self):
        """  n = P/kT   this func return count of area atoms"""
        return self.pressure/(BOLTSMAN_CONSTANT*self.temp)
    

    def find_gas_mass(self):
        """   m = molarity * M  this func return count of area atoms"""
        return self.find_molarity()*self.gazmass
    
    def area_density(self):
        """ density = m / v(cm3)"""
        return self.find_gas_mass()*self.volumecm3
    
        




air = Area(0.00005, 1, 300, 20)

print(air.find_gas_mass())