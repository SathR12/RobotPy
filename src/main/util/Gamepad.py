import wpilib
from wpilib import Joystick

class Gamepad(Joystick):

    #All gamepad maps
    kGamepadButtonX = 1
    kGamepadButtonA = 2 
    kGamepadButtonB = 3 
    kGamepadButtonY = 4 
    kGamepadButtonShoulderL = 5
    kGamepadButtonShoulderR = 6 
    kGamepadTriggerLeft = 7
    kGamepadTriggerRight = 8 
    kGamepadButtonBack = 9
    kGamepadButtonStart = 10
    kGamepadLeftStick = 11
    kGamepadRightStick = 12

    def __init__(self, port):
        super().__init__(port)

    def getRawAxis(self, axis):
        return super().getRawAxis(axis)     

    def getLeftX(self):
        return super().getRawAxis(0)

    def getLeftY(self):
        return super().getRawAxis(1)

    def getRightX(self):
        return super().getRawAxis(2)

    def getRightY(self):
        return super().getRawAxis(3)