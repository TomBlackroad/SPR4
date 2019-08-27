#Actuators or Sensors
ACC = 0
SEN = 1
BOTH = 2

#Number of parameters that define an Actuator or a Sensor
N_ACC_PARAM = 9
N_SEN_PARAM = 4

#Factor for movemente speed scaling
SPEED_FACTOR = 10.0

#Scaling factor from angles to pulses
SCALE_ACC = 11
CNT_ACC = 500

#GENERAL FINITE STATE MACHINE
#States
INIT = 0
REST = 1
EXPLORE = 2
SHOWOFF = 3
PHOTO = 4

# GPIO Pins
TRIG = 27
ECHO = 22