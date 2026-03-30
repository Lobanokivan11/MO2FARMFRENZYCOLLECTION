from ..basic_game import BasicGame
import qt6.QtCore
import mobase

class farmfrenzy3americaGame(BasicGame):
    Name = "Farm Frenzy 3 American Pie Support Plugin"
    Author = "lobivan11"
    Version = "1.0.0"

    GameName = "Farm Frenzy 3 American Pie"
    GameShortName = "FarmFrenzy3AmericanPie"
    GameBinary = "FarmFrenzy3_America.exe"
    GameDataPath = "Data"
    def savesDirectory(self):
        return qt6.QtCore.QDir("C:/ProgramData/Farm Frenzy 3 American Pie")
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
