# Created on 5 Nov 2016
# Created by: Matthew Lourenco
# This program calculates the volume of a cylinder

PI = 3.14

def calculate_volume(input_height, input_radius):
    #When called this function uses radius and height to calculate volume
    
    calculated_volume = PI * (input_radius**2) * input_height
    
    return calculated_volume

while True:
    height = raw_input('Input the height in cm: ')
    try:
        height = int(height)
        break
    except:
        print('Please enter an integer')

while True:
    radius = raw_input('Input the radius in cm: ')
    try:
        radius = int(radius)
        volume = calculate_volume(height, radius)
        print('The volume is: ' + str(volume) + 'cm^3')
        break
    except:
        print('Please enter an integer')
