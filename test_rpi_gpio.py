#!/usr/bin/python
BOARD = "board"
BCM = "bcm"
OUT = "out"
IN = "in"
 
def output(pin,value):
    print(pin, ":", value)
 
def setmode(mode):
    print(mode)
 
def setup(pin,value):
    print(pin, ":", value)
 
def cleanup():
    print("clean-up")
 
def setwarnings(warning):
    print("setting warning to ", warning)

def input(id):
    # testing for OFF
    # return True

    # Testing for ON
    return False

#End