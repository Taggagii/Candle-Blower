from Motor import Motor

class TurnMotor:
    def run(self):
        try:
            self.PWM=Motor()
            self.PWM.setMotorModel(0,0,0,0)
            # second motor is the one on foam
            while True:
                self.PWM.setMotorModel(0,3600,0,0)
                    
        except KeyboardInterrupt:
           self.PWM
           self.PWM.setMotorModel(0,0,0,0) 

if __name__=='__main__':
    print ('Program is starting ... ')
    turnMotor = TurnMotor()
    turnMotor.run()
