
from MyProjectBase import MainDialog
import wx

# Concrete Main UI Class

class EditDialog ( MainDialog ):
    def __init__( self, parent ):
        MainDialog.__init__( self, parent )

    def onOkClicked( self, event ):
        print("OK clicked")

    def onEditClicked( self, event ):
        print("Edit clicked")


class AppClass(wx.App):
    def OnInit(self):
        main_app = wx.App(False)
        frame = EditDialog(None)
        frame.Show()
        main_app.MainLoop()
        return True
    
# Main entry point of the application
if __name__ == "__main__":
    app = AppClass()

