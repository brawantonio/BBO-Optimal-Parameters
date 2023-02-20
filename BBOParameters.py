#BBO parameters
import numpy as np

#Effective 2nd order nonlinear susceptibility
def deffTypeI(theta, phi, ratio):
     #ratio = d22/d31
     return np.sin(theta*np.pi/180) - ratio*np.cos(theta*np.pi/180)*np.sin(3*phi*np.pi/180)


#----------------------------------------------
def n2_Nikogosyan(z):
    no2 = 2.7359 + 0.01878/(z**2-0.01822)-0.01354*z**2
    ne2 = 2.3753 + 0.01224/(z**2-0.01667)-0.01516*z**2
    return no2, ne2

def n2_Nikogosyan_NIR(z):
    no2 = 2.7359 + 0.01878/(z**2-0.01822)-0.01354*z**2 +  0.0006081*z**4 - 0.00006740*z**6
    ne2 = 2.3753 + 0.01224/(z**2-0.01667)-0.01516*z**2 + 0.0005716*z**4 - 0.00006305*z**6
    return no2, ne2

def n2_eksma(z): 
    no2 = 2.7405 + 0.0184/(z**2 - 0.0179) - 0.0155*z**2
    ne2 = 2.3730 + 0.0128/(z**2- 0.0156) - 0.0044*z**2
    return no2, ne2

#sellmeier_eq = {'book': n2_book, 'book_NIR': n2_book_NIR, 'eksma': n2_eksma }

class ExperimentalValues_1():
    wavelength = np.array([0.40466, 0.43583, 0.46782, 0.47999, 0.50858, 0.54607, 0.57907, 
                           0.5893, 0.64385, 0.8189, 0.85212, 0.89435, 1.014 ])
    no = np.array([1.69267, 1.68679, 1.68198, 1.68044, 1.67722, 1.67376, 1.67131, 
                    1.67049, 1.66736, 1.66066, 1.65969, 1.65862, 1.65608])
    ne = np.array([1.56796, 1.56376, 1.56024, 1.55914, 1.55691, 1.55465, 1.55298, 
                    1.55247, 1.55012, 1.54589, 1.54542, 1.54469, 1.54333])

class ExperimentalValues_2():
    wavelength = np.array([1.064, .532, .266])
    no = np.array([1.6551, 1.66749, 1.7571])
    ne = np.array([1.5425, 1.5555, 1.6146])

#------------------------------------------------------------------------
def PhaseMatchingAngle(no2_w, ne2_w, no2_2w, ne2_2w):
    argument = np.sqrt( (1/no2_w-1/no2_2w)/(1/ne2_2w-1/no2_2w) )
    return np.arcsin(argument)*180/np.pi #, np.arcsin(-argument)*180/np.pi  

def ne_angle(no2, ne2, theta):
    aux = np.sin(theta)**2/ne2 + np.cos(theta)/no2
    return 1/np.sqrt(aux)