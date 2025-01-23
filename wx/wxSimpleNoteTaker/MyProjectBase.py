# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

import gettext
_ = gettext.gettext

###########################################################################
## Class MainDialog
###########################################################################

class MainDialog ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 270,303 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        verticalSizer = wx.BoxSizer( wx.VERTICAL )

        self.btnOk = wx.Button( self, wx.ID_ANY, _(u"OK"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.btnOk.SetMinSize( wx.Size( 100,-1 ) )

        verticalSizer.Add( self.btnOk, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        self.btnSave = wx.Button( self, wx.ID_ANY, _(u"Save"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.btnSave.SetToolTip( _(u"Click this to edit") )
        self.btnSave.SetMinSize( wx.Size( 100,-1 ) )

        verticalSizer.Add( self.btnSave, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        self.txtEdit = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txtEdit.SetMinSize( wx.Size( 300,-1 ) )

        verticalSizer.Add( self.txtEdit, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL|wx.EXPAND, 5 )

        self.lblMessage = wx.StaticText( self, wx.ID_ANY, _(u"Enter notes"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lblMessage.Wrap( -1 )

        verticalSizer.Add( self.lblMessage, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        self.SetSizer( verticalSizer )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.btnOk.Bind( wx.EVT_LEFT_DOWN, self.onOkClicked )
        self.btnSave.Bind( wx.EVT_LEFT_DOWN, self.onEditClicked )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def onOkClicked( self, event ):
        event.Skip()

    def onEditClicked( self, event ):
        event.Skip()


