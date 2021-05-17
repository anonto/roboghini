import RPi.GPIO as GPIO
import KeyPressModule as kp





GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
pwm=GPIO.PWM(11,50)

pwm.start(7)

GPIO.setwarnings(False)
HeadLight = 12
GPIO.setup(HeadLight, GPIO.OUT)

GPIO.setwarnings(False)
BackLight = 13
GPIO.setup(BackLight, GPIO.OUT)


GPIO.setwarnings(False)
LeftIndicator = 15
GPIO.setup(LeftIndicator, GPIO.OUT)

GPIO.setwarnings(False)
RightIndicator = 16
GPIO.setup(RightIndicator, GPIO.OUT)



##################################
### Light Sensor will be Setup here, Later
##################################
GPIO.output(HeadLight, GPIO.HIGH)


kp.init()

def main()

  if kp.getKey('UP'):
      GPIO.output(BackLight, GPIO.LOW)
      ####################################
  elif kp.getKey('DOWN'):
      GPIO.output(BackLight, GPIO.HIGH)
      ####################################
  elif kp.getKey('LEFT'):
      GPIO.output(LeftIndicator, GPIO.HIGH)
      pwm.ChangeDutyCycle(2)
  elif kp.getKey('RIGHT'):
      GPIO.output(RightIndicator, GPIO.HIGH)
      pwm.ChangeDutyCycle(12)

  else:
      pwm.stop()
      GPIO.output(LeftIndicator, GPIO.LOW)
      GPIO.output(RightIndicator, GPIO.LOW)
      GPIO.cleanup()
      GPIO.output(BackLight, GPIO.HIGH)
      GPIO.output(HeadLight, GPIO.HIGH)
