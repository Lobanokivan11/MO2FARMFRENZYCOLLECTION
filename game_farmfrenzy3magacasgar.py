from ..basic_game import BasicGame
import qt6.QtCore
import mobase

class farmfrenzy3magacasgarGame(BasicGame):
    Name = "Farm Frenzy 3 Madagascar Support Plugin"
    Author = "lobivan11"
    Version = "1.0.0"

    GameName = "Farm Frenzy 3 Madagascar"
    GameShortName = "FarmFrenzy3Madagascar"
    GameBinary = "FarmFrenzy3_Madagascar.exe"
    GameDataPath = ""
    def savesDirectory(self):
        return qt6.QtCore.QDir("C:/ProgramData/Farm Frenzy 3 Madagascar")
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
