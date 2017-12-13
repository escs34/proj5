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

def navigator():
	'''return current position'''
	return bit1()*1 + bit2()*2 + bit4()*4 + bit8()*8 + bit16()*16



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
	li2=[bit1(), bit2(), bit4(), bit8(), bit16()]
	fiveth=li2[0]+li2[1]+li2[2]+li2[3]+li2[4]
	li2.append(fiveth)
	if li2 != li[len(li)-1]:
		li.append(li2)
		del li[0]
	return fiveth

subLi1=['dummy', 'dummy', 'dummy', 'dummy', 'dummy', 'dummy']

li=[subLi1, subLi1, subLi1, subLi1, subLi1, subLi1, subLi1, subLi1, subLi1, subLi1]


def where_to_go():
	#change way check right forward left Uturn
	for index in range(9, -1, -1):
		if isinstance(li[index][5], str):
			continue
		if li[index][5]>2:
			for index2 in range(4, -1, -1):
				if li[index][index2]!=li[index-1][index2] and index2>2:
					return 1
			if li[index+1][5]!=0:
				return 0

			else:
				return 2


	'''for a in li:#check when bit==5
		if(a[5]==5):
			return 1#. . . . .

	for f in range(0, len(li)):#check when bit==4
		if(li[f][5]==4):
			for c in range(4, -1, -1):
				if li[f][c]!=li[f-1][c]:
					if c==4 or c==3:#o....  or ....o
						return 1#o...o  or ...ooo

				else:			#....o  or o....
							#o...o  or oo...
					if li[len(li)-1][5]==2:
						return 0
					else:
						return 2

	for b in range(0, len(li)):
		if(li[b][5]==3):
			for c in range(4, -1, -1):
				if li[b][c]!=li[b-1][c]:
					if c==4 or c==3:#oo... or o...o
						return 1#oo..o or o..oo

					else:		#...oo or o...o
							#o..oo or oo..o
						if li[len(li)-1][5]==2:
							return 0
						else:
							return 2

	if li[len(li)-1][5]==0:
		return 1#U_turn ooooo

	return 0#go_forward'''


def li_clear():
	#li=[subLi1, subLi2, subLi3, subLi4, subLi5, subLi6, subLi7, subLi8, subLi9, subLi10]
	for i in range(10):
		li.append(subLi1)
		del li[0]

if __name__ == "__main__":
	while True:
		print(bitCount())

