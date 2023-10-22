# Python script to calculate battery capacity


# Car Attributes 
'''
mass - Total mass of the car (Kg)
frontal_area - frontal area of the car that's exposed to the oncoming air. (m^2)
drag_coefficient - dimensionless coefficient that represents the aerodynamic efficiency of the car's shape. Found using CFD in ANSYS
tire_pressure - psi 
'''

mass = 600 #1000
frontal_area = 1.7 # 1.7 1.78 1.66
drag_coefficient = 0.14 #0.135 
tire_pressure = 35

# Environment 
'''
air_density - Density of air at specified temperature and pressure. (kg/m^2)
velocity - Velocity of the car relative to the air. (km/h)
gravity - Earth's gravity (m/s^2)
'''
air_density = 1.164
velocity = 72
gravity = 9.81

# Derived Attributes
rolling_resistance_coef = -1

# --------------------------------------------------------------------------------------------------------------

# Unit conversion 
velocity = velocity * 1000 / 3600 # Convert km/h to m/s
tire_pressure = tire_pressure / 14.504 # Convert psi to bar


# Calculations 
def drag_force():
    return 0.5 * air_density * frontal_area * drag_coefficient * pow(velocity, 2)

def rolling_resistance_force():
    rolling_resistance_coef = 0.005 + (1 / tire_pressure) * (0.01 + 0.0095 * pow(velocity /1000 * 3600 / 100, 2))
    print(rolling_resistance_coef)
    return rolling_resistance_coef * mass * gravity


print('\n*****OUTPUT*******', '\n')
print('Rolling resistance force:', rolling_resistance_force(), 'N')
print('Drag force:', drag_force(), 'N')
print()

