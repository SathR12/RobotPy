import wpilib
import commands2
from commands2 import CommandBase
import main.robot.Robot as Robot
from main.robot.Robot import MyRobot

class IntakeExtend(CommandBase):
    def __init__(self):
        self.addRequirements(MyRobot.INTAKE)

    def initialize(self) -> None:
        return super().initialize()

    def execute(self):
        MyRobot.INTAKE.intakeRetractSolenoid()

    def isFinished(self):
        return True

    def end(self, interrupted: bool) -> None:
        return super().end(interrupted)

        