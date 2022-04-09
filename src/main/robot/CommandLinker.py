from wpilib import Joystick
from commands2 import CommandScheduler
from Controllers.DriverJoystickController import DriverJoystickController
from Controllers.XBoxController import XBoxController
from commands.Drivetrain.DiffDrive import DiffDrive
from main.robot.Robot import MyRobot
from main.util.Gamepad import Gamepad

class CommandLinker():
    driveJoystick = Joystick(0)
    operatorGamepad = Gamepad(1)
    driverController = DriverJoystickController(driveJoystick)
    xboxController = XBoxController(operatorGamepad)

    def __init__(self) -> None:
        pass



    def configureRegisteredSubsystems(self):
        CommandScheduler.getInstance().registerSubsystem(MyRobot.INTAKE)
        CommandScheduler.getInstance().registerSubsystem(MyRobot.DRIVETRAIN)
        CommandScheduler.getInstance().registerSubsystem(MyRobot.STORAGE)

    def configurePeriodicBindings(self):
        CommandScheduler.getInstance().setDefaultCommand(MyRobot.DRIVETRAIN, DiffDrive())

    def configureCommands(self):
        self.driverController.mapButtons()
        self.xboxController.mapButtons()

