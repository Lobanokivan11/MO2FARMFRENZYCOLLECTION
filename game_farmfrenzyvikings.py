from ..basic_game import BasicGame
import qt6.QtCore

class farmfrenzyvikingheroesGame(BasicGame):
    Name = "Farm Frenzy Viking Heroes Support Plugin"
    Author = "lobivan11"
    Version = "1.0.0"

    GameName = "Farm Frenzy Viking Heroes"
    GameShortName = "FarmFrenzyVikingHeroes"
    GameBinary = "FarmFrenzyVikings.exe"
    GameDataPath = "Data"
    def savesDirectory(self):
        return qt6.QtCore.QDir("C:/ProgramData/Farm Frenzy Viking Heroes")
