from ..basic_game import BasicGame


class farmfrenzy3magacasgarGame(BasicGame):
    Name = "Farm Frenzy 3 Madagascar Support Plugin"
    Author = "lobivan11"
    Version = "1.0.0"

    GameName = "Farm Frenzy 3 Madagascar"
    GameShortName = "FarmFrenzy3Madagascar"
    GameBinary = "FarmFrenzy3_Madagascar.exe"
    GameDataPath = "Data"
    def savesDirectory(self):
        return qt6.QtCore.QDir("C:/ProgramData/Farm Frenzy 3 Madagascar")
