from ..basic_game import BasicGame


class farmfrenzygonefishingGame(BasicGame):
    Name = "Farm Frenzy Gone Fishing Support Plugin"
    Author = "lobivan11"
    Version = "1.0.0"

    GameName = "Farm Frenzy Gone Fishing"
    GameShortName = "FarmFrenzyGoneFishing"
    GameBinary = "FarmFrenzyGoneFishing.exe"
    GameDataPath = "Data"
    def savesDirectory(self):
        return qt6.QtCore.QDir("C:/ProgramData/Farm Frenzy Gone Fishing")
