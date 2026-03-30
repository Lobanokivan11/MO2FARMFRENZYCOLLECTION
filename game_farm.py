from ..basic_game import BasicGame
import qt6.QtCore

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
