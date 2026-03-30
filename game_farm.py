from ..basic_game import BasicGame
import qt6.QtCore
from mobase import ExecutableInfo

class farmGame(BasicGame):
    Name = "Farm Frenzy Support Plugin"
    Author = "lobivan11"
    Version = "1.0.0"

    GameName = "Farm Frenzy"
    GameShortName = "FarmFrenzy"
    GameBinary = "farm.exe"
    GameDataPath = "Data"
    def savesDirectory(self):
        return qt6.QtCore.QDir("C:/ProgramData/Farm Frenzy")
    def executables(self):
        return [
            ExecutableInfo(self.GameName, qt6.QtCore.QFileInfo(self.binaryName()))
        ]
    def binaryName(self):
        return self.GameBinary
