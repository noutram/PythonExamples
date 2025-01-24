from MyProjectBase import MainDialog
import wx

# Concrete Main UI Class

class EditDialog ( MainDialog ):
    def __init__( self, parent ):
        MainDialog.__init__( self, parent )
        # If the file notes.txt exists, load
        try:
            with open("notes.txt", "r", encoding='utf-8') as file:
                notes = file.read()
                self.txtEdit.SetValue(notes)
        except FileNotFoundError:
            print("Empty file - first time this is run")
        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.onClose)

    def onOkClicked( self, event ):
        print("OK clicked")
        text_box_string : str = self.txtEdit.GetValue()
        print(text_box_string)
        # Save the text to a file
        with open("notes.txt", "w", encoding='utf-8') as file:
            file.write(text_box_string)

    def onEditClicked( self, event ):
        print("Edit clicked")

    def onClose(self, event):
        self.Destroy()
        wx.GetApp().ExitMainLoop()


class AppClass(wx.App):
    def OnInit(self):
        self.main_app = wx.App(False)
        self.frame = EditDialog(None)
        self.frame.Show()
        return True
    
# Main entry point of the application
if __name__ == "__main__":
    app = AppClass()
    app.MainLoop()
