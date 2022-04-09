from asyncio.windows_events import NULL
import wpilib
from wpilib import Joystick
import commands2
from commands2.button import JoystickButton

class Controller():
    joystick = NULL

    def __init__(self, joystick):
        self.joystick = joystick


    def mapButton(self, buttonNumber):
        return JoystickButton(self.joystick, buttonNumber)