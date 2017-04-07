# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.html

###########################################################################
## Class ChatForm
###########################################################################

class ChatForm ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"TinyChat", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer16 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer16.AddGrowableCol( 0 )
		fgSizer16.AddGrowableRow( 0 )
		fgSizer16.SetFlexibleDirection( wx.BOTH )
		fgSizer16.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.ui_log = wx.html.HtmlWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.html.HW_SCROLLBAR_AUTO )
		fgSizer16.Add( self.ui_log, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		self.m_staticline3 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer16.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )
		
		fgSizer17 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer17.AddGrowableCol( 0 )
		fgSizer17.SetFlexibleDirection( wx.BOTH )
		fgSizer17.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.ui_input = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_PROCESS_ENTER )
		self.ui_input.SetMinSize( wx.Size( -1,48 ) )
		
		fgSizer17.Add( self.ui_input, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.ui_send = wx.Button( self, wx.ID_ANY, u"Send", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ui_send.SetDefault() 
		self.ui_send.Enable( False )
		
		fgSizer17.Add( self.ui_send, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		
		fgSizer16.Add( fgSizer17, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		self.SetSizer( fgSizer16 )
		self.Layout()
		self.m_timer2 = wx.Timer()
		self.m_timer2.SetOwner( self, wx.ID_ANY )
		self.m_timer2.Start( 100 )
		
		self.ui_status = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.ui_input.Bind( wx.EVT_KEY_DOWN, self.DoInputKey )
		self.ui_input.Bind( wx.EVT_KEY_UP, self.DoInputKey )
		self.ui_input.Bind( wx.EVT_TEXT_ENTER, self.DoInputEnter )
		self.ui_send.Bind( wx.EVT_BUTTON, self.DoSend )
		self.Bind( wx.EVT_TIMER, self.DoTimer, id=wx.ID_ANY )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def DoInputKey( self, event ):
		event.Skip()
	
	
	def DoInputEnter( self, event ):
		event.Skip()
	
	def DoSend( self, event ):
		event.Skip()
	
	def DoTimer( self, event ):
		event.Skip()
	

###########################################################################
## Class ConnectForm
###########################################################################

class ConnectForm ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"TinyChat", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( 520,250 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer18 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer18.AddGrowableCol( 1 )
		fgSizer18.AddGrowableRow( 6 )
		fgSizer18.SetFlexibleDirection( wx.BOTH )
		fgSizer18.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		fgSizer18.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.ui_name = wx.TextCtrl( self, wx.ID_ANY, u"Guest", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer18.Add( self.ui_name, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Host", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		fgSizer18.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		ui_hostChoices = []
		self.ui_host = wx.ComboBox( self, wx.ID_ANY, u"127.0.0.1", wx.DefaultPosition, wx.DefaultSize, ui_hostChoices, 0 )
		fgSizer18.Add( self.ui_host, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		
		fgSizer18.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		fgSizer5 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer5.AddGrowableCol( 0 )
		fgSizer5.AddGrowableRow( 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.ui_listen = wx.CheckBox( self, wx.ID_ANY, u"Listen", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.ui_listen, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Port", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		fgSizer5.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.ui_port = wx.TextCtrl( self, wx.ID_ANY, u"31337", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ui_port.Enable( False )
		
		fgSizer5.Add( self.ui_port, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		fgSizer18.Add( fgSizer5, 1, wx.EXPAND, 5 )
		
		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Contact", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		fgSizer18.Add( self.m_staticText12, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		ui_contactChoices = []
		self.ui_contact = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, ui_contactChoices, 0 )
		self.ui_contact.Enable( False )
		
		fgSizer18.Add( self.ui_contact, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		
		fgSizer18.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.ui_auth = wx.CheckBox( self, wx.ID_ANY, u"Authenticate", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer18.Add( self.ui_auth, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		
		fgSizer18.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticline5 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer18.Add( self.m_staticline5, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		fgSizer18.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		fgSizer18.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"My ID", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		fgSizer18.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.ui_id = wx.TextCtrl( self, wx.ID_ANY, u"Loading...", wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		fgSizer18.Add( self.ui_id, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		
		fgSizer18.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		fgSizer6 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer6.AddGrowableCol( 0 )
		fgSizer6.AddGrowableRow( 0 )
		fgSizer6.SetFlexibleDirection( wx.BOTH )
		fgSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.ui_progress = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.ui_progress.SetValue( 0 ) 
		fgSizer6.Add( self.ui_progress, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.ui_connect = wx.Button( self, wx.ID_ANY, u"Connect", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ui_connect.SetDefault() 
		self.ui_connect.Enable( False )
		
		fgSizer6.Add( self.ui_connect, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		
		fgSizer18.Add( fgSizer6, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( fgSizer18 )
		self.Layout()
		fgSizer18.Fit( self )
		self.m_timer1 = wx.Timer()
		self.m_timer1.SetOwner( self, wx.ID_ANY )
		self.m_timer1.Start( 100, True )
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.ui_listen.Bind( wx.EVT_CHECKBOX, self.DoListenToggle )
		self.ui_auth.Bind( wx.EVT_CHECKBOX, self.DoAuthToggle )
		self.ui_connect.Bind( wx.EVT_BUTTON, self.DoConnect )
		self.Bind( wx.EVT_TIMER, self.DoTimer, id=wx.ID_ANY )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def DoListenToggle( self, event ):
		event.Skip()
	
	def DoAuthToggle( self, event ):
		event.Skip()
	
	def DoConnect( self, event ):
		event.Skip()
	
	def DoTimer( self, event ):
		event.Skip()
	

