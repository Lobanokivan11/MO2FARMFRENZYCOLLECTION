from ..basic_game import BasicGame
import mobase
try:
    from PyQt5.QtCore import QDir, QFileInfo
except ImportError:
    from qt6.QtCore import QDir, QFileInfo


class farmfrenzy3arcticaGame(BasicGame):
    Name = "Farm Frenzy 3 Ice Age Support Plugin"
    Author = "lobivan11"
    Version = "1.0.0"

    GameName = "Farm Frenzy 3 Ice Age"
    GameShortName = "FarmFrenzy3IceAge"
    GameBinary = "FarmFrenzy3_Arctica.exe"
    GameDataPath = "Data"
    def init(self, organizer: mobase.IOrganizer):
        return super().init(organizer)

    def binaryName(self):
        return self.GameBinary

    def executables(self):
        return [
            mobase.ExecutableInfo(
                self.GameName,
                QFileInfo(self.gameDirectory().absoluteFilePath(self.GameBinary))
            )
        ]

    def savesDirectory(self):
        return QDir("C:/ProgramData/Farm Frenzy 3 Ice Age")
