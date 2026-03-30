from ..basic_game import BasicGame
import qt6.QtCore
from mobase import ExecutableInfo

class farmfrenzy3russiaGame(BasicGame):
    Name = "Farm Frenzy 3 Russian Roullete Support Plugin"
    Author = "lobivan11"
    Version = "1.0.0"

    GameName = "Farm Frenzy 3 Russian Roullete"
    GameShortName = "FarmFrenzy3RussianRoullete"
    GameBinary = "FarmFrenzy3_Russia.exe"
    GameDataPath = "Data"
    def savesDirectory(self):
        return qt6.QtCore.QDir("C:/ProgramData/Farm Frenzy 3 Russian Roullete")
    def executables(self):
        return [
            ExecutableInfo(self.GameName, qt6.QtCore.QFileInfo(self.binaryName()))
        ]
    def binaryName(self):
        return self.GameBinary
