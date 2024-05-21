SPEED_OF_LIGHT = 299_792_458  # м/с
GRAVITATIONAL_CONSTANT = 6.67430e-11  # м^3 кг^−1 с^−2
PLANCK_CONSTANT = 6.62607015e-34  # Дж с
MASS_ELECTRON_KILLO = 9.1093837015*10**(-31)  #кг масса электрона
MASS_ELECTRON_EV = 511000 #эВ масса покоя электрона
EV_TO_J = 1.602176634*10**(-19)
MASS_TO_KILO = 1.66053906660*10**(-27) 

class RecoilNuclide:

    def __init__(self, energy, charge, mass, ):
        """energy in eV, charge in abs charge of pozitron mass in Da"""
        self.__energy = energy
        self.__mass = mass
        self.__charge = charge
        self.__masskilo = mass*MASS_TO_KILO


    def recoil_vel(self):
        """func rerurn recoil nuclide velocity in metr per second """
        
        return ((2*self.__energy *EV_TO_J)/self.__masskilo)**0.5


