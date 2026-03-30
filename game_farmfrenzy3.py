from ..basic_game import BasicGame


class farmfrenzy3Game(BasicGame):
    Name = "Farm Frenzy 3 Support Plugin"
    Author = "lobivan11"
    Version = "1.0.0"

    GameName = "Farm Frenzy 3"
    GameShortName = "FarmFrenzy3"
    GameBinary = "FarmFrenzy3.exe"
    GameDataPath = "Data"
    def savesDirectory(self):
        return qt6.QtCore.QDir("C:/ProgramData/Farm Frenzy 3")
