from ..basic_game import BasicGame
import mobase
try:
    from PyQt5.QtCore import QDir, QFileInfo
except ImportError:
    from qt6.QtCore import QDir, QFileInfo


class farmfrenzypizzapartyGame(BasicGame):
    Name = "Farm Frenzy Pizza Party Support Plugin"
    Author = "lobivan11"
    Version = "1.0.0"

    GameName = "Farm Frenzy Pizza Party"
    GameShortName = "FarmFrenzyPizzaParty"
    GameBinary = "FarmFrenzyPizzaParty.exe"
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
        return QDir("C:/ProgramData/Farm Frenzy Pizza Party")
