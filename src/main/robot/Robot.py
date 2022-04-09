import wpilib
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
    