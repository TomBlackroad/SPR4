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
		self.pwm = PCA9685(0x40, debug=False)
		self.pwm.setPWMFreq(50)
		print("My name is: ", self.actuators[0].name)
		self.names_acc = [self.actuators[i].name for i in range(len(self.actuators))]
		self.names_sen = [self.sensors[i].name for i in range(len(self.sensors))]
		self.idx_acc = [i for i in range(len(self.actuators))]
		self.idx_sen = [i for i in range(len(self.sensors))]
		self.acc_dic = utils.genDictionary(self.names_acc, self.idx_acc)
		self.sen_dic = utils.genDictionary(self.names_sen, self.idx_sen)
		print(self.acc_dic)

	def moveAcc(self,name,pos):
		poss = pos*mbl_bots.SCALE_ACC + mbl_bots.CNT_ACC
		if (poss > self.actuators[int(self.acc_dic[name])].max): poss = self.actuators[int(self.acc_dic[name])].max
		if (poss < self.actuators[int(self.acc_dic[name])].min): poss = self.actuators[int(self.acc_dic[name])].min
		self.pwm.setServoPulse(int(self.actuators[int(self.acc_dic[name])].adress), poss)
		print('Moving ', name ,'to', poss )


