#########################################################################
### Date: 2017/10/13
### file name: trackingModule.py
### Purpose: this code has been generated for the five-way tracking sensor
###         to perform the decision of direction
###
#########################################################################

# =======================================================================
# import GPIO library and time module
# =======================================================================
import RPi.GPIO as GPIO
import time

# =======================================================================
#  set GPIO warnings as false
# =======================================================================
GPIO.setwarnings(False)

# =======================================================================
# set up GPIO mode as BOARD
# =======================================================================
GPIO.setmode(GPIO.BOARD)



# =======================================================================
# declare the pins of 16, 18, 22, 40, 32 in the Rapberry Pi
# as the control pins of 5-way trackinmg sensor in order to
# control direction
# 
#  leftmostled    leftlessled     centerled     rightlessled     rightmostled
#       16            18              22             40              32
#
# led turns on (1) : trackinmg sensor led detects white playground
# led turns off(0) : trackinmg sensor led detects black line

# leftmostled off : it means that moving object finds black line
#                   at the position of leftmostled
#                   black line locates below the leftmostled of the moving object
#
# leftlessled off : it means that moving object finds black line
#                   at the position of leftlessled
#                   black line locates below the leftlessled of the moving object
# 
# centerled off : it means that moving object finds black line
#                   at the position of centerled
#                   black line locates below the centerled of the moving object
# 
# rightlessled off : it means that moving object finds black line
#                   at the position of rightlessled
#                   black line locates below the rightlessled  of the moving object
# 
# rightmostled off : it means that moving object finds black line
#                   at the position of rightmostled
#                   black line locates below the rightmostled of the moving object
# =======================================================================

leftmostled=16
leftlessled=18
centerled=22
rightlessled=40
rightmostled=32


# =======================================================================
# because the connetions between 5-way tracking sensor and Rapberry Pi has been 
# established, the GPIO pins of Rapberry Pi
# such as leftmostled, leftlessled, centerled, rightlessled, and rightmostled
# should be clearly declared whether their roles of pins
# are output pin or input pin
# since the 5-way tracking sensor data has been detected and
# used as the input data, leftmostled, leftlessled, centerled, rightlessled, and rightmostled
# should be clearly declared as input
# 
# =======================================================================

GPIO.setup(leftmostled, GPIO.IN)
GPIO.setup(leftlessled, GPIO.IN)
GPIO.setup(centerled,   GPIO.IN)
GPIO.setup(rightlessled, GPIO.IN)
GPIO.setup(rightmostled, GPIO.IN)



# =======================================================================
# GPIO.input(leftmostled) method gives the data obtained from leftmostled
# leftmostled returns (1) : leftmostled detects white playground
# leftmostled returns (0) : leftmostled detects black line
#
#
# GPIO.input(leftlessled) method gives the data obtained from leftlessled
# leftlessled returns (1) : leftlessled detects white playground
# leftlessled returns (0) : leftlessled detects black line
#
# GPIO.input(centerled) method gives the data obtained from centerled
# centerled returns (1) : centerled detects white playground
# centerled returns (0) : centerled detects black line
#
# GPIO.input(rightlessled) method gives the data obtained from rightlessled
# rightlessled returns (1) : rightlessled detects white playground
# rightlessled returns (0) : rightlessled detects black line
#
# GPIO.input(rightmostled) method gives the data obtained from rightmostled
# rightmostled returns (1) : rightmostled detects white playground
# rightmostled returns (0) : rightmostled detects black line
#
# =======================================================================

'''try:
    while True:
       print("leftmostled  detects black line(0) or white ground(1): " + str(GPIO.input(leftmostled)))
       print("leftlessled  detects black line(0) or white ground(1): " + str(GPIO.input(leftlessled)))
       print("centerled    detects black line(0) or white ground(1): " + str(GPIO.input(centerled)))
       print("rightlessled detects black line(0) or white ground(1): " + str(GPIO.input(rightlessled)))
       print("rightmostled detects black line(0) or white ground(1): " + str(GPIO.input(rightmostled)))
       time.sleep(1)
             
except KeyboardInterrupt:
    GPIO.cleanup()'''
def navigator():
	'''return current position'''
	bit=(not GPIO.input(leftmostled))+(not GPIO.input(leftlessled)) * 2 + (not GPIO.input(centerled)) * 4 + (not GPIO.input(rightlessled))*8 + (not GPIO.input(rightmostled))*16
	return bit

def bit1():
	return not GPIO.input(leftmostled)

def bit2():
	return not GPIO.input(leftlessled)

def bit4():
	return not GPIO.input(centerled)

def bit8():
	return not GPIO.input(rightlessled)

def bit16():
	return not GPIO.input(rightmostled)

def bitCount():
	return bit1() + bit2() + bit4() + bit8() + bit16()

if __name__ == "__main__":
	while True:
		print(bitCount())