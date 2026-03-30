from ..basic_game import BasicGame
import qt6.QtCore
import mobase

class farmfrenzyvikingheroesGame(BasicGame):
    Name = "Farm Frenzy Viking Heroes Support Plugin"
    Author = "lobivan11"
    Version = "1.0.0"

    GameName = "Farm Frenzy Viking Heroes"
    GameShortName = "FarmFrenzyVikingHeroes"
    GameBinary = "FarmFrenzyVikings.exe"
    GameDataPath = ""
    def savesDirectory(self):
        return qt6.QtCore.QDir("C:/ProgramData/Farm Frenzy Viking Heroes")
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
