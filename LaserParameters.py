#laser parameters
import scipy.constants


class TopticaLaser775:
    #Laser unit
    average_power = 1e-1
    wavelength = 7.75e-7
    repetition_rate = 9e7
    pulse_width = 1.5e-13
    duty_cycle = pulse_width*repetition_rate
    peak_power = average_power/duty_cycle
    
    #Energy
    frequency = scipy.constants.lambda2nu(wavelength)
    phase = 0
    polarization = 0

    #Gaussian Optics
    waist = 1e-4
    waist_loc = 0
    dof = 1e-2
    divergence_angle = 2*waist/dof


class TopticaLaser1550:
    #Laser unit
    average_power = 1e-1
    wavelength = 1.55e-6
    repetition_rate = 9e7
    pulse_width = 1e-13
    duty_cycle = pulse_width*repetition_rate
    peak_power = average_power/duty_cycle

    #Energy
    frequency = scipy.constants.lambda2nu(wavelength)
    phase = 0
    polarization = 0

    #Gaussian Optics
    waist = 1e-4
    waist_loc = 0
    dof = 1e-2
    divergence_angle = 2*waist/dof

class MiraLaser:
    #Laser unit
    average_power = 1e-1
    wavelength = 0.810e-6
    repetition_rate = 9e7
    pulse_width = 1e-13
    duty_cycle = pulse_width*repetition_rate
    peak_power = average_power/duty_cycle

    #Energy
    frequency = scipy.constants.lambda2nu(wavelength)
    phase = 0
    polarization = 0

    #Gaussian Optics
    waist = 1e-4
    waist_loc = 0
    dof = 1e-2
    divergence_angle = 2*waist/dof