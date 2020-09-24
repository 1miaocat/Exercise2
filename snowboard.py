print ('Enter your height.')
feet = int(input('Feet: '))
inch = int(input('Inches: '))

inch_frm_foot = feet*12
height_inch = inch_frm_foot + inch
height_cm = height_inch * 2.54

board_len = (88/100) * height_cm

print('Suggested board length: ' + str(board_len) + 'cm')
