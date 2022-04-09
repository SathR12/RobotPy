from asyncio.windows_events import NULL
import ctre
import wpilib
from ctre import NeutralMode, WPI_TalonSRX
import commands2
from wpilib import DoubleSolenoid, PneumaticsModuleType, MotorControllerGroup, SmartDashboard
import main.util.subsystems.MechanicalSubsystem as MechanicalSubsystem
from main.robot.Robot import MyRobot 

class Intake(MechanicalSubsystem):
    INTAKE_MOTOR_ONE = NULL
    INTAKE_MOTOR_GROUP = NULL
    INTAKE_SOLENOID = NULL
    ModuleType = PneumaticsModuleType.CTREPCM

    def __init__(self):
        self.INTAKE_MOTOR_ONE = WPI_TalonSRX(MyRobot.ROBOTMAP.intakeMotorOnePort)
        self.INTAKE_MOTOR_GROUP = MotorControllerGroup(self.INTAKE_MOTOR_ONE)
        self.INTAKE_SOLENOID = DoubleSolenoid(self.ModuleType, MyRobot.ROBOTMAP.intakeSoleForward, MyRobot.ROBOTMAP.intakeSoleReverse)

        self.configureMotors()

    def spinRoller(self, isForward):
        if(isForward):
            self.INTAKE_MOTOR_GROUP.set(-MyRobot.ROBOTMAP.intakeSpeed)
        else:
            self.INTAKE_MOTOR_GROUP.set(MyRobot.ROBOTMAP.intakeSpeed)

    def spinRoller(self, speed):
        self.INTAKE_MOTOR_GROUP.set(-speed)

    def spinRollerReverse(self, speed):
        self.INTAKE_MOTOR_GROUP.set(speed)

    def stopRoll(self):
        self.INTAKE_MOTOR_GROUP.stopMotor()
        return True


    def intakeToggleSolenoid(self):
        if self.INTAKE_SOLENOID.get() == DoubleSolenoid.Value.kForward:
            self.intakeRetractSolenoid()
            print("intake up: toggle: retract intake pistons")

        else:
            self.intakeExtendSolenoid()
            print("intake down : toggle: extend intake pistons")

        
    def intakeExtendSolenoid(self):
        print("extend intake")
        self.INTAKE_SOLENOID.set(DoubleSolenoid.Value.kForward)

    def intakeRetractSolenoid(self):
        print("extend intake")
        self.INTAKE_SOLENOID.set(DoubleSolenoid.Value.kReverse)


    def configureMotors(self):
        self.INTAKE_MOTOR_ONE.configFactoryDefault()

        self.INTAKE_MOTOR_ONE.setNeutralMode(NeutralMode.Coast)

    def smartDashboard(self):
        SmartDashboard.putNumber("Intake Motor One Speed", self.INTAKE_MOTOR_ONE.get())

    def isAlive(self):
        return self.INTAKE_MOTOR_ONE.isAlive()

    def ping(self):
        pass

    def shuffleBoard(self):
        pass


