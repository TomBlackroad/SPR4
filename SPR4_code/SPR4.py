#!/usr/bin/python
import time
import math
import smbus
import sys
import utils
import logging
import mbl_bots

from camera import Cam
from robot import Robot
from servo_hat_driver import PCA9685

class SPR4(Robot):
    def __init__(self):
        super(SPR4, self).__init__("SPR4.botfile.txt")
        #Brain method --- conscience!!!!
        self.GFSM()

    def GFSM(self):
        state = super(SPR4,self).state
        while True:
            self.FSM(super(SPR4,self).state)

    def FSM(self, state):
        states_list = {
            0 : INIT,
            1 : REST,
            2 : EXPLORE,
            3 : SHOWOFF,
            4 : PHOTO,
        }
        func = states_list.get(state, lambda:None)
        return func()

    def INIT(self):
        print("CURRENT STATE: INIT")
        self.camera = Cam()
        super(SPR4,self).state = mbl_bots.REST
        time.sleep(2)

    def REST(self):
        print("CURRENT STATE: REST")
        super(SPR4,self).state = mbl_bots.EXPLORE
        time.sleep(10)

    def EXPLORE(self):
        print("CURRENT STATE: EXPLORE")
        #EXPLORING METHODS
        #self.explore_FSM()
	super(SPR4,self).flat()
	time.sleep(1)
	super(SPR4,self).stand()
	time.sleep(3)
	super(SPR4,self).flat()
	time.sleep(2)
	super(SPR4,self).stand()
        super(SPR4,self).state = mbl_bots.SHOWOFF

    def SHOWOFF(self):
        print("CURRENT STATE: SHOWOFF")
        #SHOWOFF METHODS
        #self.showoff_FSM()
	super(SPR4,self).sayHello()
        super(SPR4,self).state = mbl_bots.PHOTO
    
    def PHOTO(self):
        print("CURRENT STATE: PHOTO")
        self.camera.take_pic()
        super(SPR4,self).state = mbl_bots.EXPLORE

    # start_time = time.time()
    # while ((time.time()-start_time)<60):
    #   self.stand()
    # start_time = time.time()
    # while True:
    #   self.flat()
    

  
    
    # super(SPR4,self).moveAcc('BLL', self.home + 50*rand)
    # super(SPR4,self).moveAcc('FLR', self.home - 30*rand)
    # time.sleep(ms)
    # super(SPR4,self).moveAcc("FSR", self.home - 45*rand)
    # super(SPR4,self).moveAcc("BSR", self.home + 60*rand)
    # time.sleep(ms)
    # super(SPR4,self).moveAcc("FLR", self.home - 80*rand)
    # super(SPR4,self).moveAcc("BLL", self.home + 60*rand)
    # super(SPR4,self).moveAcc("FLR", self.home - 80*rand)
    # super(SPR4,self).moveAcc("BLL", self.home + 50*rand)
    # time.sleep(ms)
    # super(SPR4,self).moveAcc("BSL", self.home + 30*rand)
    # super(SPR4,self).moveAcc("FSR", self.home + 20*rand)
    # time.sleep(ms)
    # super(SPR4,self).moveAcc("BLL", self.home + 60*rand)
    # super(SPR4,self).moveAcc("FLL", self.home + 80*rand)
    # super(SPR4,self).moveAcc("BLL", self.home + 20*rand)
    # super(SPR4,self).moveAcc("FLL", self.home + 40*rand)
    # time.sleep(ms)
    # super(SPR4,self).moveAcc("FSL", self.home + 60*rand)
    # super(SPR4,self).moveAcc("BSL", self.home - 50*rand)
    # time.sleep(ms)
    # super(SPR4,self).moveAcc("FLL", self.home + 70*rand)
    # super(SPR4,self).moveAcc("BLR", self.home - 70*rand)
    # super(SPR4,self).moveAcc("FLL", self.home + 40*rand)
    # super(SPR4,self).moveAcc("BLR", self.home - 40*rand)
    # time.sleep(ms)
    # super(SPR4,self).moveAcc("BSR", self.home - 20*rand)
    # super(SPR4,self).moveAcc("FSL", self.home)
    # time.sleep(ms)
    # super(SPR4,self).moveAcc("BLR", self.home - 50*rand)
    # super(SPR4,self).moveAcc("FLL", self.home + 70*rand)
    # time.sleep(ms)


#  def walkBack(self, speed, rand):
#    """
#    """
#  def walkRight(self, speed, rand):
#    """
#    """
#  def walkLeft(self, speed, rand):
#    """
#    """

#                                                             #     
#  ---------------------------------------------------------  #
#  ---------------------------------------------------------  #
#  ---------------------------------------------------------  #
#            _____                    _____                   #
#           /\    \                  /\    \                  #
#          /::\    \                /::\    \                 #   
#         /::::\    \               \:::\    \                #  
#        /::::::\    \               \:::\    \               #   
#       /:::/\:::\    \               \:::\    \              #   
#      /:::/__\:::\    \               \:::\    \             #
#     /::::\   \:::\    \              /::::\    \            #     
#    /::::::\   \:::\    \    ____    /::::::\    \           #     
#   /:::/\:::\   \:::\    \  /\   \  /:::/\:::\    \          #  
#  /:::/  \:::\   \:::\____\/::\   \/:::/  \:::\____\         #   
#  \::/    \:::\  /:::/    /\:::\  /:::/    \::/    /         #       
#   \/____/ \:::\/:::/    /  \:::\/:::/    / \/____/          #       
#            \::::::/    /    \::::::/    /                   #         
#             \::::/    /      \::::/____/                    #     
#             /:::/    /        \:::\    \                    #     
#            /:::/    /          \:::\    \                   #     
#           /:::/    /            \:::\    \                  #    
#          /:::/    /              \:::\____\                 #  
#          \::/    /                \::/    /                 #  
#           \/____/                  \/____/                  #    
#                                                             #  
#  ---------------------------------------------------------  #
#  ---------------------------------------------------------  #
#  ---------------------------------------------------------  #
#                                                             #   

if __name__=='__main__':
  SPR4 = SPR4()
  

"""
if __name__=='__main__':
  pwm = PCA9685(0x40, debug=True)
  pwm.setPWMFreq(50)
   # setServoPulse(2,2500)
   # for i in range(500,2500,2):
   #   pwm.setServoPulse(int(sys.argv[1]),i)
   # for i in range(2500,500,-2):
   #   pwm.setServoPulse(int(sys.argv[1]),i)
"""
