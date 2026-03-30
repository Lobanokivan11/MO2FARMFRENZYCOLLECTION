from ..basic_game import BasicGame
import qt6.QtCore
import mobase

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
    def init(self, organizer: mobase.IOrganizer):
        return super().init(organizer)
    def executables(self):
        return [
            mobase.ExecutableInfo(
                self.GameName,
                qt6.QtCore.QFileInfo(self.gameDirectory().absoluteFilePath(self.GameBinary))
            )
        ]
    def binaryName(self):
        return self.GameBinary
