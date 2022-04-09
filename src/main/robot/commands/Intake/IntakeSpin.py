import wpilib
import commands2
from commands2 import CommandBase
import main.robot.Robot as Robot
from main.robot.Robot import MyRobot

class IntakeSpin(CommandBase):
    def __init__(self):
        self.addRequirements(MyRobot.INTAKE)

    def initialize(self) -> None:
        return super().initialize()

    def execute(self):
        MyRobot.INTAKE.spinRoller(True)

    def isFinished(self):
        return False

    def end(self, interrupted: bool) -> None:
        return MyRobot.INTAKE.stopRoll()

        