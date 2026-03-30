from ..basic_game import BasicGame


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
