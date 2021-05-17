import RPi.GPIO as GPIO
import KeyPressModule as kp

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
pwm=GPIO.PWM(11,50)
pwm.start(7)



kp.init()

def main()

  if kp.getKey('UP'):
      ####################################
  elif kp.getKey('DOWN'):
      ####################################
  elif kp.getKey('LEFT'):
      pwm.ChangeDutyCycle(2)
  elif kp.getKey('RIGHT'):
      pwm.ChangeDutyCycle(12)

  else:
      pwm.stop()
      GPIO.cleanup()
