from util.Gamepad import Gamepad

class ButtonMap():
    def __init__(self):
        pass

    joystickOnePort = 0
    gamepadOnePort = 1
    drivetrainShiftButton = 1
    drivetrainReverseDirectionButton = 3

    intakeSpinButton = Gamepad.kGamepadButtonB
    intakeReverseSpinButton = Gamepad.kGamepadButtonA
    intakeToggleSolenoidButton = Gamepad.kGamepadButtonY

    storageInButton = Gamepad.kGamepadTriggerLeft
    storageOutButton = Gamepad.kGamepadTriggerRight
    storageFastOutButton = Gamepad.kGamepadLeftStick

    storageMoveBallsUpButton = Gamepad.kGamepadButtonShoulderR
    storageMoveBallsReverseButton = Gamepad.kGamepadButtonShoulderL