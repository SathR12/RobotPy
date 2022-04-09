from commands2 import CommandBase
from main.robot.Robot import MyRobot

class StorageUpFast(CommandBase):
    def __init__(self):
        self.addRequirements(MyRobot.STORAGE)

    def initialize(self) -> None:
        return super().initialize()

    def execute(self):
        MyRobot.STORAGE.storageRunFast(False)

    def isFinished(self):
        return False

    def end(self, interrupted):
        if interrupted:
            MyRobot.STORAGE.storageMotorStop()
            print("Motor stopped")
