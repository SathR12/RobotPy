import wpilib
import commands2
from commands2 import CommandBase
import main.robot.Robot as Robot
from main.robot.Robot import MyRobot

class StorageIn(CommandBase):
    def __init__(self):
        self.addRequirements(MyRobot.STORAGE)

    def initialize(self) -> None:
        return super().initialize()

    def execute(self):
        MyRobot.STORAGE.storageIn(True)

    def isFinished(self):
        return False

    def end(self, interrupted):
        if interrupted:
            MyRobot.STORAGE.storageMotorStop()
            print("Motor stopped")

    