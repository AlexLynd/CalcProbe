from pad4pi import rpi_gpio
import RPi.GPIO as GPIO
import math
import random
import time
GPIO.setwarnings(False)

inp=''
inp10=''
programlist=[]

matrix=[
    ['%',7,'=',0,'RM',None],
    ['M-',8,'M+',1,4,None], 
    ['clr',9,'/',2,5,None],
    ['+','-','X',3,6,'on'],
    [None,None,None,'sqrt','.',None]   ]

row=[4,11,22,18,10]
col=[17,9,27,14,3,15]

factory= rpi_gpio.KeypadFactory()
keypad= factory.create_keypad(keypad=matrix,row_pins=row,col_pins=col)
   
def prog_validate(key):
    global inp, inp10, programlist
    if (len(inp)<8) and (type(key)== int):
        inp=inp+str(key)
        print(inp)
    if key== '=':
        try:
            inp10= int(inp,2)
        except ValueError:
            print('Error')
        else:
            print('Valid binary input.')
            print(inp10)
            prog_run(inp10)            
    if key== 'clr'or key== '=':
        print('clr')
        inp=''
        
def prog_run(prog_id):
    keypad.unregisterKeyPressHandler(prog_validate)
    programlist=[calc,ref,rand]
    try:
        keypad.registerKeyPressHandler(programlist[prog_id])
    except:
        print('NONE')
    else:
        print('valid program')
        
def default(prog_name):
    keypad.unregisterKeyPressHandler(prog_name)
    keypad.registerKeyPressHandler(prog_validate)
##----------------------------------##    
def calc(key):
    if key!='on':
        print('calc')
        print(key)
    default(calc)
    
def ref(key):
    print('ref')
    print(programlist)
    
def rand(key):
    print('rand')
##----------------------------------##    
keypad.registerKeyPressHandler(prog_validate)
