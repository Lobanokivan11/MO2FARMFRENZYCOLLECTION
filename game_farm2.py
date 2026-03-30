from ..basic_game import BasicGame
import mobase
try:
    from PyQt5.QtCore import QDir, QFileInfo
except ImportError:
    from qt6.QtCore import QDir, QFileInfo


class farm2Game(BasicGame):
    Name = "Farm Frenzy 2 Support Plugin"
    Author = "lobivan11"
    Version = "1.0.0"

    GameName = "Farm Frenzy 2"
    GameShortName = "FarmFrenzy2"
    GameBinary = "farm2.exe"
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
        return QDir("C:/ProgramData/Farm Frenzy 2")
