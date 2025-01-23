from MyProjectBase import MyFrame1

class MyProjectForm(MyFrame1):
    def __init__(self, *args, **kwargs):
        super(MyProjectForm, self).__init__(*args, **kwargs)
        # Add your subclass initialization code here

    # Add any additional methods or overrides here
    def doOk(self, event):
        super().doOk(event)
        self.m_staticTextMessage.SetLabel("You clicked OK")