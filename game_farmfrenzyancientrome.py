from ..basic_game import BasicGame
import mobase
try:
    from PyQt5.QtCore import QDir, QFileInfo
except ImportError:
    from qt6.QtCore import QDir, QFileInfo


class farmfrenzyancientromeGame(BasicGame):
    Name = "Farm Frenzy Ancient Rome Support Plugin"
    Author = "lobivan11"
    Version = "1.0.0"

    GameName = "Farm Frenzy Ancient Rome"
    GameShortName = "FarmFrenzyAncientRome"
    GameBinary = "FarmFrenzyAncientRome.exe"
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
        return QDir("C:/ProgramData/Farm Frenzy Ancient Rome")
