from ..basic_game import BasicGame
import qt6.QtCore

class farmfrenzy3arcticaGame(BasicGame):
    Name = "Farm Frenzy 3 Ice Age Support Plugin"
    Author = "lobivan11"
    Version = "1.0.0"

    GameName = "Farm Frenzy 3 Ice Age"
    GameShortName = "FarmFrenzy3IceAge"
    GameBinary = "FarmFrenzy3_Arctica.exe"
    GameDataPath = "Data"
    def savesDirectory(self):
        return qt6.QtCore.QDir("C:/ProgramData/Farm Frenzy 3 Ice Age")
