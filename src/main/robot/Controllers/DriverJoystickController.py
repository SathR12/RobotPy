from asyncio.windows_events import NULL
import wpilib
from wpilib import Joystick
import commands2
from commands2.button import Button
import Controller

class DriverJoystickController():
    controller = NULL

    def __init__(self, joystickPort):
        self.controller = Controller(joystickPort)

    def mapButtons(self):
        pass