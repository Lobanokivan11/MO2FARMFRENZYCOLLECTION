from ..basic_game import BasicGame
import qt6.QtCore

class farmfrenzyancientromeGame(BasicGame):
    Name = "Farm Frenzy Ancient Rome Support Plugin"
    Author = "lobivan11"
    Version = "1.0.0"

    GameName = "Farm Frenzy Ancient Rome"
    GameShortName = "FarmFrenzyAncientRome"
    GameBinary = "FarmFrenzyAncientRome.exe"
    GameDataPath = "Data"
    def savesDirectory(self):
        return qt6.QtCore.QDir("C:/ProgramData/Farm Frenzy Ancient Rome")
