from asyncio.windows_events import NULL
from ctre import WPI_TalonFX
from wpilib import SmartDashboard
from wpilib import MotorControllerGroup
from navx import AHRS
from wpilib.drive import DifferentialDrive
from wpilib import Joystick
from wpilib import SPI 
from ctre import NeutralMode
from wpilib import PneumaticsModuleType
from wpilib import DoubleSolenoid
from main.util.subsystems.MechanicalSubsystem import MechanicalSubsystem
from main.robot.Robot import MyRobot

class Drivetrain(MechanicalSubsystem):
    LEFT_MOTOR_ONE = NULL
    LEFT_MOTOR_TWO = NULL
    LEFT_MOTOR_THREE = NULL

    RIGHT_MOTOR_ONE = NULL
    RIGHT_MOTOR_TWO = NULL
    RIGHT_MOTOR_THREE = NULL

    LEFT_M_GROUP = NULL
    RIGHT_M_GROUP = NULL

    DIFF_DRIVE = NULL

    isForward = NULL

    ModuleType = PneumaticsModuleType.CTREPCM
    DRIVE_SOLENOID = NULL

    shiftStatus = NULL
    rPMCoefficient = NULL

    twistCoefficient = NULL

    GYRO = NULL
    KP_GYRO = NULL

    def __init__(self):
        self.LEFT_MOTOR_ONE = WPI_TalonFX(MyRobot.ROBOTMAP.drivetrainLeftMotorPortOne)
        self.LEFT_MOTOR_TWO = WPI_TalonFX(MyRobot.ROBOTMAP.drivetrainLeftMotorPortTwo)
        self.LEFT_MOTOR_THREE = WPI_TalonFX(MyRobot.ROBOTMAP.drivetrainLeftMotorPortThree)

        self.RIGHT_MOTOR_ONE = WPI_TalonFX(MyRobot.ROBOTMAP.drivetrainRightMotorPortOne)
        self.RIGHT_MOTOR_TWO = WPI_TalonFX(MyRobot.ROBOTMAP.drivetrainRightMotorPortTwo)
        self.RIGHT_MOTOR_THREE = WPI_TalonFX(MyRobot.ROBOTMAP.drivetrainRightMotorPortThree)

        self.RIGHT_M_GROUP = MotorControllerGroup(self.RIGHT_MOTOR_ONE, self.RIGHT_MOTOR_TWO, self.RIGHT_MOTOR_THREE)
        self.LEFT_M_GROUP = MotorControllerGroup(self.LEFT_MOTOR_ONE, self.LEFT_MOTOR_TWO, self.LEFT_MOTOR_THREE)

        self.DIFF_DRIVE = DifferentialDrive(self.RIGHT_M_GROUP, self.LEFT_M_GROUP)

        self.GYRO = AHRS(SPI.Port.kMXP)
        self.KP_GYRO = MyRobot.ROBOTMAP.KP_GYRO

        self.rPMCoefficient = 1.25

        self.isForward = True

        #Drivetrain Solenoids

        self.DRIVE_SOLENOID = DoubleSolenoid(self.ModuleType, MyRobot.ROBOTMAP.drivetrainSolenoidPortOn, MyRobot.ROBOTMAP.drivetrainSolenoidPortOff)

        self.LEFT_M_GROUP.setInverted(False)
        self.RIGHT_M_GROUP.setInverted(True)

    
    def arcadeDrive(self, stick: Joystick):
        self.y = stick.getY()
        self.rotate = stick.getTwist

        if self.isForward:
            pass

        else:
            y = -y
        
        self.DIFF_DRIVE.arcadeDrive(y / self.rPMCoefficient, self.rotate / self.twistCoefficient, False)

    def reverseDirection(self):
        if not self.isForward:
            self.isForward = True
        else:
            self.isForward = False

        print("motion reversed")

    def shiftGear(self):
        if self.DRIVE_SOLENOID.get() == DoubleSolenoid.Value.kForward:
            self.highGear()
            print("SHIFT: in high gear")
        else:
            self.lowGear()
            print("SHIFT: in low gear")


    def lowGear(self):
        self.DRIVE_SOLENOID.set(DoubleSolenoid.Value.kForward)

    def highGear(self):
        self.DRIVE_SOLENOID.set(DoubleSolenoid.Value.kReverse)
        
    def gyroMoveStraight(self, speed):
        self.DIFF_DRIVE.arcadeDrive(speed, -self.GYRO.getAngle() * self.KP_GYRO)

    def gyroMoveStraight(self, speed, angle):
        self.DIFF_DRIVE.arcadeDrive(-speed, -angle * self.KP_GYRO)

    def rotate(self, speed):
        self.LEFT_M_GROUP.set(speed)
        self.RIGHT_M_GROUP.set(speed)

    def configureMotors(self):
        self.LEFT_MOTOR_ONE.configFactoryDefault()
        self.LEFT_MOTOR_TWO.configFactoryDefault()
        self.LEFT_MOTOR_THREE.configFactoryDefault()
        self.RIGHT_MOTOR_ONE.configFactoryDefault()
        self.RIGHT_MOTOR_TWO.configFactoryDefault()
        self.RIGHT_MOTOR_THREE.configFactoryDefault()
        
        self.LEFT_MOTOR_ONE.setNeutralMode(NeutralMode.Brake)
        self.LEFT_MOTOR_TWO.setNeutralMode(NeutralMode.Brake)
        self.LEFT_MOTOR_THREE.setNeutralMode(NeutralMode.Brake)
        self.RIGHT_MOTOR_ONE.setNeutralMode(NeutralMode.Brake)
        self.RIGHT_MOTOR_TWO.setNeutralMode(NeutralMode.Brake)
        self.RIGHT_MOTOR_THREE.setNeutralMode(NeutralMode.Brake)


    def getGyro(self):
        return self.GYRO

    def getGyroAngle(self):
        return self.GYRO.getAngle()

    def getGyroAxis(self):
        return self.GYRO.getBoardYawAxis()

    def resetGyro(self):
        self.GYRO.reset()
        self.GYRO.zeroYaw()

    def stop(self):
        self.rotate(0)
        return False

    def ping(self):
        pass

    def isAlive(self):
        return True

    
    def shuffleBoard(self):
        SmartDashboard.putNumber("Gyro Angle", self.GYRO.getAngle())
        SmartDashboard.putNumber("Gyro Axis", self.getGyroAxis())


    

    