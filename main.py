import os
from art import tprint

filestep1 = 0
filestep2 = 0
step1 = 0
step2 = 0

def convertList():
    print('Audio\n-------\n1) .mp3\n2) .wav')
    print('Video\n-------\n3) .mkv')

def conversion(convert1, convert2, inputFile, outputFile):
    if convert1 == (3) and convert2 == (1):
        os.system('ffmpeg -i ' + inputFile + ' -vn -acodec libmp3lame -b:a 192k ' + outputFile)
    elif convert1 == (3) and convert2 == (2):
        os.system('ffmpeg -i ' + inputFile + ' -vn -acodec pcm_s16le -ar 44100 -ac 2 ' + outputFile)
    else:
        os.system('ffmpeg -i ' + inputFile + ' ' + outputFile)

def filenameMenu(step):
    if step == (1):
        global filestep1
        filestep1 = input('Enter the input file name>> ')
    elif step == (2):
        global filestep2
        filestep2 = input('Enter the output file name>> ')
    else:
        print('Somthing went wrong again.')

def convertMenu(step):
    convertList()
    if step == (1):
        print('Please select your input file type.')
        global step1
        step1 = input('>> ')
        print('You have selected ' + step1 + '.')
    elif step == (2):
        print('Please select your output file type.')
        global step2
        step2 = input('>> ')
        print('You have selected ' + step2 + '.')
    else:
        print('Somthing went very Wrong. I would reinstall the software because if this is wrong I dont know what you did.')


tprint('ORB')
print('Conversion Utilities')
print('--------------------\nOrb Conversion Utils is licenced under the GNU General Public License 3.0')
convertMenu(1)
convertMenu(2)
filenameMenu(1)
filenameMenu(2)
conversion(step1,step2,filestep1,filestep2)

