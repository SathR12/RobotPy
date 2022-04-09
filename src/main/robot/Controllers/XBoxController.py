from asyncio.windows_events import NULL
import Controller
from main.robot.Robot import MyRobot 
from main.robot.commands.Storage.StorageDown import StorageDown
from main.robot.commands.Storage.StorageUp import StorageUp
from main.robot.commands.Storage.StorageUpFast import StorageUpFast
from main.robot.commands.Storage.StorageIn import StorageIn 
from main.robot.commands.Storage.StorageOut import StorageOut
from main.robot.commands.Intake.IntakeSpin import IntakeSpin
from main.robot.commands.Intake.IntakeSpinReverse import IntakeSpinReverse
from main.robot.commands.Intake.IntakeToggleSolenoid import IntakeToggleSolenoid

class XBoxController():

    controller: Controller.Controller = NULL

    def __init__(self, joystickPort):
        self.controller = Controller.Controller(joystickPort)

    def mapButtons(self):
        self.controller.mapButton(MyRobot.BUTTON_MAP.storageMoveBallsUpButton).whileHeld(StorageUp())
        self.controller.mapButton(MyRobot.BUTTON_MAP.storageMoveBallsReverseButton).whileHeld(StorageDown())
        self.controller.mapButton(MyRobot.BUTTON_MAP.storageFastOutButton).whileHeld(StorageUpFast())

        self.controller.mapButton(MyRobot.BUTTON_MAP.storageInButton).whenHeld(StorageIn())
        self.controller.mapButton(MyRobot.BUTTON_MAP.storageOutButton).whenHeld(StorageOut())

        self.controller.mapButton(MyRobot.BUTTON_MAP.intakeSpinButton).whenHeld(IntakeSpin())
        self.controller.mapButton(MyRobot.BUTTON_MAP.intakeReverseSpinButton).whenHeld(IntakeSpinReverse())
        self.controller.mapButton(MyRobot.BUTTON_MAP.intakeToggleSolenoidButton).whenPressed(IntakeToggleSolenoid())
    
    