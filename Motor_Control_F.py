
import RPi.GPIO as GPIO

#set GPIO numbering mode and define output pins


class Motorize:
    theG = GPIO
    in1 = 24
    in2 = 23
    in3 = 22
    in4 = 27

    def Start_Engine(self):
        self.theG.setmode(self.theG.BCM)
        self.theG.setup(self.in1,self.theG.OUT)
        self.theG.setup(self.in2,self.theG.OUT)
        self.theG.setup(self.in3,self.theG.OUT)
        self.theG.setup(self.in4,self.theG.OUT)
        self.Press_Break()

    def Press_Break(self):
        self.theG.output(self.in1,self.theG.LOW)
        self.theG.output(self.in2,self.theG.LOW)
        self.theG.output(self.in3,self.theG.LOW)
        self.theG.output(self.in4,self.theG.LOW)

    def Run_Forward(self):
        self.theG.output(self.in1, self.theG.HIGH)
        self.theG.output(self.in2, self.theG.LOW)
        self.theG.output(self.in3, self.theG.HIGH)
        self.theG.output(self.in4, self.theG.LOW)

    def Run_Backward(self):
        self.theG.output(self.in1, self.theG.LOW)
        self.theG.output(self.in2, self.theG.HIGH)
        self.theG.output(self.in3, self.theG.LOW)
        self.theG.output(self.in4, self.theG.HIGH)

    def Turn_Left(self):
        self.theG.output(self.in1, self.theG.HIGH)
        self.theG.output(self.in2, self.theG.LOW)
        self.theG.output(self.in3, self.theG.LOW)
        self.theG.output(self.in4, self.theG.LOW)

    def Turn_Right(self):
        self.theG.output(self.in1, self.theG.LOW)
        self.theG.output(self.in2, self.theG.LOW)
        self.theG.output(self.in3, self.theG.HIGH)
        self.theG.output(self.in4, self.theG.LOW)



    def Stop_Engine(self):
        self.theG.cleanup()
    
