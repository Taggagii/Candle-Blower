from Motor import Motor
import time

class TurnMotor:
    def stop(self):
        try:
            self.PWM = Motor()
            self.PWM.setMotorModel(0, 0, 0, 0)
                    
        except:
           self.PWM
           self.PWM.setMotorModel(0,0,0,0) 

if __name__=='__main__':
    print ('stopping motor ... ')
    turnMotor = TurnMotor()
    turnMotor.stop()

