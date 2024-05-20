
class Constants:
# class Constants:
#     SPEED_OF_LIGHT = 299_792_458  # м/с
#     GRAVITATIONAL_CONSTANT = 6.67430e-11  # м^3 кг^−1 с^−2
#     PLANCK_CONSTANT = 6.62607015e-34  # Дж с

#     def __setattr__(self, key, value):
#         raise AttributeError("Cannot modify a constant value")

# # Пример использования
# constants = Constants()

# # Попытка изменить значение вызовет ошибку
# try:
#     constants.SPEED_OF_LIGHT = 300_000_000
# except AttributeError as e:
#     print(e)  # Output: Cannot modify a constant value

# print(constants.SPEED_OF_LIGHT)  # Output: 299792458



    @property
    def SPEED_OF_LIGHT(self):
        return 299_792_458  # м/с
    
    @property
    def MASS_ELECTRON_KILLO(self):
        return 9.1093837015*10**(-31)  #кг масса электрона
    
    @property
    def MASS_ELECTRON_EV(self):
        return 511000 #эВ масса покоя электрона
    
    @property
    def EV_TO_J(self):
        return 1.602176634*10**(-19)
    
    @property
    def MASS_TO_KILO(self):
        return 1.66053906660*10**(-27)
            
    
    @property
    def PLANCK_CONSTANT(self):
        return 6.62607015e-34  # Дж с






class RecoilNuclide(Constants):

    def __init__(self, energy, charge, mass, ):
        """energy in eV, charge in abs charge of pozitron mass in Da"""
        self.__energy = energy
        self.__mass = mass
        self.__charge = charge
        self.__masskilo = mass*Constants.MASS_TO_KILO


    def recoil_vel(self):
        """func rerurn recoil nuclide velocity in metr per second """
        
        return ((2*self.__energy *Constants.Kf_to_J)/self.__masskilo)**0.5
print(111)
dic= RecoilNuclide(10, 20, 30)
print(dic.recoil_vel)
    



