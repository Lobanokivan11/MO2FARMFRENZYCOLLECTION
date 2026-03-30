from ..basic_game import BasicGame


class farm2Game(BasicGame):
    Name = "Farm Frenzy 2 Support Plugin"
    Author = "lobivan11"
    Version = "1.0.0"

    GameName = "Farm Frenzy 2"
    GameShortName = "FarmFrenzy2"
    GameBinary = "farm2.exe"
    GameDataPath = "Data"
    def savesDirectory(self):
        return qt6.QtCore.QDir("C:/ProgramData/Farm Frenzy 2")
