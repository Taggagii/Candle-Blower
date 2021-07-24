from Motor import Motor
import time

class TurnMotor:
    def run(self):
        try:
            self.PWM=Motor()
            self.PWM.setMotorModel(0,0,0,0)
            # second motor is the one on foam
            self.PWM.setMotorModel(3600,0,0,0)
        except:
           self.PWM
           self.PWM.setMotorModel(0,0,0,0) 
    def stop(self):
        try:
            self.PWM = Motor()
            self.PWM.setMotorModel(0, 0, 0, 0)
                    
        except:
           self.PWM
           self.PWM.setMotorModel(0,0,0,0) 

if __name__=='__main__':
    print ('Program is starting ... ')
    turnMotor = TurnMotor()
    try:
        turnMotor.run()
        time.sleep(30)
        turnMotor.stop()
    except:
        turnMotor.stop()

