import wpilib
from commands2 import CommandScheduler
from main.robot.CommandLinker import CommandLinker
from main.robot.RobotMap import RobotMap
from main.robot.ButtonMap import ButtonMap
from main.robot.subsystems.Drivetrain import Drivetrain
from main.robot.subsystems.Intake import Intake
from main.robot.subsystems.Storage import Storage

class MyRobot(wpilib.TimedRobot):
    def __init__(self):
        pass

    ROBOTMAP = RobotMap()
    BUTTON_MAP = ButtonMap()
    DRIVETRAIN = Drivetrain()
    INTAKE = Intake()
    STORAGE = Storage()
    COMMAND_LINKER = CommandLinker()

    def robotInit(self) -> None:
        MyRobot.COMMAND_LINKER.configureRegisteredSubsystems()
        MyRobot.COMMAND_LINKER.configurePeriodicBindings()
        MyRobot.COMMAND_LINKER.configureCommands()


        CommandScheduler.getInstance().enable()

    def robotPeriodic(self) -> None:
        self.DRIVETRAIN.shuffleBoard()
        self.STORAGE.shuffleBoard()

    def teleopInit(self) -> None:
        self.DRIVETRAIN.highGear()

    def teleopPeriodic(self) -> None:
        CommandScheduler.getInstance().run()

    def disabledInit(self) -> None:
        return super().disabledInit()

    def disabledPeriodic(self) -> None:
        return super().disabledPeriodic()
    
if __name__ == "__main__":
    wpilib.run(MyRobot)

        