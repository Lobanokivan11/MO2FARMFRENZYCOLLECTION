from ..basic_game import BasicGame
import mobase
import qt6.QtCore

class farmGame(BasicGame):
    Name = "Farm Frenzy Support Plugin"
    Author = "lobivan11"
    Version = "1.0.0"

    GameName = "Farm Frenzy"
    GameShortName = "farmfrenzy"
    GameBinary = "farm.exe"
    GameDataPath = "Data"

    def init(self, organizer: mobase.IOrganizer):
        return super().init(organizer)

    def binaryName(self):
        return self.GameBinary

    def executables(self):
        return [
            mobase.ExecutableInfo(
                self.GameName,
                qt6.QtCore.QFileInfo(self.gameDirectory().absoluteFilePath(self.GameBinary))
            )
        ]

    def savesDirectory(self):
        return qt6.QtCore.QDir("C:/ProgramData/Farm Frenzy")
