import wx;
import ConnectForm;

class TinyChatWxApp(wx.App):
	def OnInit(self):
		ConnectForm.ConnectForm().Show();
		return True;

TinyChatWxApp().MainLoop();

