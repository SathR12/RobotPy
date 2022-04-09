from asyncio.windows_events import NULL
from wpilib import MotorControllerGroup
from ctre import NeutralMode, WPI_TalonFX, WPI_TalonSRX
from main.util.subsystems.MechanicalSubsystem import MechanicalSubsystem
from robot.Robot import MyRobot

class Storage(MechanicalSubsystem):
    STORAGE_MOTOR_UP_ONE = NULL
    STORAGE_MOTOR_UP_TWO = NULL
    STORAGE_MOTOR_IN = NULL

    STORAGE_MOTOR_GROUP_IN = NULL

    def __init__(self):
        self.STORAGE_MOTOR_UP_ONE = WPI_TalonFX(MyRobot.ROBOTMAP.storageMotorPortTop)
        self.STORAGE_MOTOR_UP_TWO = WPI_TalonFX(MyRobot.ROBOTMAP.storageMotorPortBot)
        self.STORAGE_MOTOR_IN = WPI_TalonSRX(MyRobot.ROBOTMAP.storageMotorPortIn)

        #Speed controllers

        self.STORAGE_MOTOR_GROUP_IN = MotorControllerGroup(self.STORAGE_MOTOR_IN)

        self.configureMotors()

    
    def configureMotors(self):
        self.STORAGE_MOTOR_UP_ONE.configFactoryDefault()
        self.STORAGE_MOTOR_UP_TWO.configFactoryDefault()
        self.STORAGE_MOTOR_IN.configFactoryDefault()

        self.STORAGE_MOTOR_UP_ONE.setNeutralMode(NeutralMode.Coast)
        self.STORAGE_MOTOR_UP_TWO.setNeutralMode(NeutralMode.Coast)
        self.STORAGE_MOTOR_IN.setNeutralMode(NeutralMode.Coast)


    def storageRunSlow(self, isForward):
        if isForward:
            self.STORAGE_MOTOR_UP_ONE.set(MyRobot.ROBOTMAP.storageSpeedUpSlow)
            self.STORAGE_MOTOR_UP_TWO.set(-MyRobot.ROBOTMAP.storageSpeedUpSlow)

        else:
            self.STORAGE_MOTOR_UP_ONE.set(-MyRobot.ROBOTMAP.storageSpeedUpSlow)
            self.STORAGE_MOTOR_UP_TWO.set(MyRobot.ROBOTMAP.storageSpeedUpSlow)

    def storageRunFast(self, isForward):
        if isForward:
            self.STORAGE_MOTOR_UP_ONE.set(MyRobot.ROBOTMAP.storageSpeedUpFast)
            self.STORAGE_MOTOR_UP_TWO.set(-MyRobot.ROBOTMAP.storageSpeedUpFast)

        else:
            self.STORAGE_MOTOR_UP_ONE.set(-MyRobot.ROBOTMAP.storageSpeedUpFast)
            self.STORAGE_MOTOR_UP_TWO.set(MyRobot.ROBOTMAP.storageSpeedUpFast)

    def storageIn(self, isForward):
        if isForward:
            self.STORAGE_MOTOR_GROUP_IN.set(MyRobot.ROBOTMAP.storageSpeedIn)
        else:
            self.STORAGE_MOTOR_GROUP_IN.set(-MyRobot.ROBOTMAP.storageSpeedIn)


    def storageMotorStop(self):
        self.STORAGE_MOTOR_UP_ONE.set(0)
        self.STORAGE_MOTOR_UP_TWO.set(0)
        self.STORAGE_MOTOR_GROUP_IN.set(0)
        return True

    def isAlive(self):
        return self.STORAGE_MOTOR_UP_ONE.isAlive()

    def ping(self):
        pass

   

 


    

    
