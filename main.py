import os
from art import tprint

def filenameMenu(step):
    if step == (1):
        filestep1 = input('Enter the input file name>> ')
    elif step == (2):
        filestep2 = input('Enter the output file name>> ')
    else:
        print('Somthing went wrong again.')

def convertMenu(step):
    print('\n1) .mp3\n2) .mkv')
    if step == (1):
        step1 = input('>> ')
        print('You have selected ' + step1 + '.')
    elif step == (2):
        step2 = input('>> ')
        print('You have selected ' + step2 + '.')
    else:
        print('Somthing went very Wrong. I would reinstall the software because if this is wrong I dont know what you did.')


tprint('ORB')
print('Conversion Utilities')
print('--------------------\nOrb Conversion Utils is licenced under the GNU General Public License 3.0')
convertMenu(1)
convertMenu(2)

