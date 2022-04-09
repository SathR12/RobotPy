import wpilib
import commands2
from commands2 import CommandBase
from main.robot.Robot import MyRobot

class DiffDrive(CommandBase):
    def __init__(self):
        self.addRequirements(MyRobot.DRIVETRAIN)

    def initialize(self) -> None:
        return super().initialize()

    def execute(self):
        MyRobot.DRIVETRAIN.arcadeDrive(MyRobot.COMMAND_LINKER.driveJoystick)

    def isFinished(self) -> bool:
        return super().isFinished()

    def end(self, interrupted: bool) -> None:
        return super().end(interrupted)

