# Remember to install wxPython first
# pip install wxPython

import wx
from MyProjectForm import MyProjectForm

# Run the application
class MyApp(wx.App):
    def OnInit(self):
        frame = MyProjectForm(None)
        frame.Show()
        return True

if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
