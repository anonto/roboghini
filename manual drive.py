import RPi.GPIO as GPIO
import keyboard

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


while true:
  if keyboard.is_pressed('down'):
    print('down is pressed')
    GPIO.output(BackLight, GPIO.HIGH)
      ####################################
    break
  if keyboard.is_pressed('up'):
    print('up is pressed')
    GPIO.output(BackLight, GPIO.LOW)
      ####################################
    break
   if keyboard.is_pressed('left'):
    print('left is pressed')
    GPIO.output(BackLight, GPIO.LOW)
    GPIO.output(LeftIndicator, GPIO.HIGH)
    pwm.ChangeDutyCycle(2)
    break
    
    
   if keyboard.is_pressed('right'):
    print('right is pressed')
    GPIO.output(BackLight, GPIO.LOW)
    GPIO.output(RightIndicator, GPIO.HIGH)
    pwm.ChangeDutyCycle(12)
    break
  else:
      pwm.stop()
      GPIO.output(LeftIndicator, GPIO.LOW)
      GPIO.output(RightIndicator, GPIO.LOW)
      GPIO.cleanup()
      GPIO.output(BackLight, GPIO.HIGH)
      GPIO.output(HeadLight, GPIO.HIGH)
