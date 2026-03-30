from ..basic_game import BasicGame
import qt6.QtCore
from mobase import ExecutableInfo

class farmfrenzy3americaGame(BasicGame):
    Name = "Farm Frenzy 3 American Pie Support Plugin"
    Author = "lobivan11"
    Version = "1.0.0"

    GameName = "Farm Frenzy 3 American Pie"
    GameShortName = "FarmFrenzy3AmericanPie"
    GameBinary = "FarmFrenzy3_America.exe"
    GameDataPath = "Data"
    def savesDirectory(self):
        return qt6.QtCore.QDir("C:/ProgramData/Farm Frenzy 3 American Pie")
    def executables(self):
        return [
            ExecutableInfo(self.GameName, qt6.QtCore.QFileInfo(self.binaryName()))
        ]
    def binaryName(self):
        return self.GameBinary
