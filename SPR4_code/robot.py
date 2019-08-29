#!/usr/bin/python
import time
import math
import smbus
import sys
import utils
import mbl_bots
import logging


from servo_hat_driver import PCA9685


class Robot(object):
	def __init__(self, file):
		super(Robot, self).__init__()
		(self.actuators, self.sensors) = utils.file2bot(file, mbl_bots.BOTH)
		self.bus = smbus.SMBus(1)
		self.pwm = PCA9685(self.bus, 0x40, debug=False)
		self.pwm.setPWMFreq(50)
		#print("My name is: ", self.actuators[0].name)
		self.names_acc = [self.actuators[i].name for i in range(len(self.actuators))]
		self.names_sen = [self.sensors[i].name for i in range(len(self.sensors))]
		self.idx_acc = [i for i in range(len(self.actuators))]
		self.idx_sen = [i for i in range(len(self.sensors))]
		self.acc_dic = utils.genDictionary(self.names_acc, self.idx_acc)
		self.sen_dic = utils.genDictionary(self.names_sen, self.idx_sen)
		self.state = mbl_bots.INIT
		self.exploreState = mbl_bots.GETDATA
		self.movesCode = mbl_bots.NONE
		#print(self.acc_dic)

	def moveAcc(self,name,pos):
		poss = pos*mbl_bots.SCALE_ACC + mbl_bots.CNT_ACC
		if (poss > self.actuators[int(self.acc_dic[name])].max): poss = self.actuators[int(self.acc_dic[name])].max
		if (poss < self.actuators[int(self.acc_dic[name])].min): poss = self.actuators[int(self.acc_dic[name])].min
		self.pwm.setServoPulse(int(self.actuators[int(self.acc_dic[name])].adress), poss)
		#print('Moving ', name ,'to', poss )

	def executeMove(self,file,speed):
		moves = utils.file2move(file)
		for i in range(len(moves)):
			self.moveAcc(moves[i].actuator, moves[i].pos)
			if(moves[i].delay > 0.0):
				time.sleep(moves[i].delay*speed)

	def flat(self):
		print("SPR4 is Flat")
		self.executeMove("/home/pi/SPR4/SPR4_code/SPR4_flat.movefile.txt", 1)    

	def stand(self):
		print("SPR4 is Standing")
		self.executeMove("/home/pi/SPR4/SPR4_code/SPR4_stand.movefile.txt", 1)

	def walkFront(self, speed=1):
		print("SPR4 is Walking Forward")
		self.executeMove("/home/pi/SPR4/SPR4_code/SPR4_walkFront.movefile.txt", speed)

	def walkRight(self, speed=1):
		print("SPR4 is Walking Right")
		self.executeMove("/home/pi/SPR4/SPR4_code/SPR4_walkFront.movefile.txt", speed)

	def walkLeft(self, speed=1):
		print("SPR4 is Walking Left")
		self.executeMove("/home/pi/SPR4/SPR4_code/SPR4_walkFront.movefile.txt", speed)

	def walkBack(self, speed=1):
		print("SPR4 is Walking Backwards")
		self.executeMove("/home/pi/SPR4/SPR4_code/SPR4_walkBack.movefile.txt", speed)

	def turnRight(self, speed=1):
		print("SPR4 is Turning Right")
		self.executeMove("/home/pi/SPR4/SPR4_code/SPR4_turnRight.movefile.txt", speed)

	def turnLeft(self, speed=1):
		print("SPR4 is Turning Left")
		self.executeMove("/home/pi/SPR4/SPR4_code/SPR4_turnLeft.movefile.txt", speed)
	
	def sayHello(self):
		print("SPR4 is Saying Hi!")
		self.executeMove("/home/pi/SPR4/SPR4_code/SPR4_sayHello.movefile.txt", 1)

	def cameraPose(self):
		print("SPR4 ready to take Picture")
		self.executeMove("/home/pi/SPR4/SPR4_code/SPR4_cameraPose.movefile.txt", 1)

	def swing(self):
		print("SPR4 is Swinging")
		self.executeMove("/home/pi/SPR4/SPR4_code/SPR4_swing.movefile.txt", 1)	

	def shake(self):
		print("SPR4 is Shaking")
		self.executeMove("/home/pi/SPR4/SPR4_code/SPR4_shake.movefile.txt", 1)	

	def move(self, code):
		moves = {
        	1: self.walkFront,
        	2: self.walkBack,
        	3: self.walkRight,
        	4: self.walkLeft,
        	5: self.turnRight,
        	6: self.turnLeft,
        	7: self.flat,
        	8: self.stand,
    	}
		func = moves.get(code, lambda:None)
		return func()

	def detectCatch(self, imu):
		data = imu.getImuRawData()
		print(data)
		if(data[3] > 3 or data[4] > 3 or data[5] > 3): 
			print("ROBOT CATCHED...do something!!")
			return True
		else: 
			return False
