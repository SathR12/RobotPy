import commands2
from commands2 import SequentialCommandGroup

class RobotMap():
    def __init__(self):
        RobotMap.joystickPortOne = 0

  
        RobotMap.drivetrainLeftMotorPortOne = 1
        RobotMap.drivetrainLeftMotorPortTwo = 2
        RobotMap.drivetrainLeftMotorPortThree = 3
        
        RobotMap.drivetrainRightMotorPortOne = 4
        RobotMap.drivetrainRightMotorPortTwo = 5
        RobotMap.drivetrainRightMotorPortThree = 6

        RobotMap.drivetrainSolenoidPortOn = 1
        RobotMap.drivetrainSolenoidPortOff = 0
        
        RobotMap.storageMotorPortTop = 21
        RobotMap.storageMotorPortBot = 12 
        RobotMap.storageMotorPortIn = 11
        RobotMap.storageSpeedUpSlow = 0.47
        RobotMap.storageSpeedUpFast = 0.85
        RobotMap.storageSpeedIn = 1
        
        RobotMap.beamBreakerPortIntake = 1
        RobotMap.beamBreakerPortStorage = 3

        RobotMap.KP_GYRO = 0.008

        RobotMap.intakeMotorOnePort = 7
        RobotMap.intakeSoleForward = 3
        RobotMap.intakeSoleReverse = 2
        RobotMap.intakeSpeed = 0.65
        