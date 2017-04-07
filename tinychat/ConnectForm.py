import wx;
import TinyChatGUI;
import TinyChat;
import ChatForm;

class ConnectForm( TinyChatGUI.ConnectForm ):
	def __init__(self):
		TinyChatGUI.ConnectForm.__init__(self, None);
		self.ui_name.SetValue(TinyChat.GetConfig("Name", "Guest"));
		self.ui_listen.SetValue(TinyChat.GetConfig("Listen", "False") == "True");
		self.ui_auth.SetValue(TinyChat.GetConfig("Authorize", "False") == "True");
		self.ui_contact.SetValue(TinyChat.GetConfig("Contact", ""));
		self.ui_host.SetValue(TinyChat.GetConfig("Host", "127.0.0.1"));
		self.DoListenToggle(None);
		self.DoAuthToggle(None);
	
	def DoTimer(self, event):
		localid = TinyChat.GetLocalID(self);
		self.ui_id.SetValue(str(localid).encode("hex"));
		self.ui_progress.SetValue(0);
		self.ui_connect.Enable();
		self.Update();
		wx.Yield();

	def DoConnect(self, event):
		TinyChat.SetName(self.ui_name.GetValue());
		TinyChat.SetConfig("Name", str(self.ui_name.GetValue()));
		TinyChat.SetConfig("Listen", str(self.ui_listen.GetValue()));
		if not self.ui_listen.GetValue():
			TinyChat.SetConfig("Host", str(self.ui_host.GetValue()));
		TinyChat.SetConfig("Authorize", str(self.ui_auth.GetValue()));
		if self.ui_auth.GetValue():
			TinyChat.SetConfig("Contact", str(self.ui_contact.GetValue()));
		if self.ui_listen.GetValue():
			if not TinyChat.SetupServer(self.ui_port.GetValue()):
				return;
		else:
			port = 31337;
			host = str(self.ui_host.GetValue()).split(":");
			if len(host) > 1: port = int(host[1]);
			host = str(host[0]);
			if not TinyChat.SetupClient((host, port)):
				dlg = wx.MessageDialog(self, "Failed to connect to %s:%d" % (host, port), "TinyChat", wx.OK | wx.ICON_WARNING);
				dlg.ShowModal();
				dlg.Destroy();
				return;
		ident = False;
		if self.ui_auth.GetValue():
			ident = self.ui_contact.GetValue();
		ChatForm.ChatForm(ident).Show();
		self.Close();

	def DoListenToggle(self, event):
		if self.ui_listen.GetValue():
			self.ui_host.Disable();
			self.ui_port.Enable();
		else:
			self.ui_host.Enable();
			self.ui_port.Disable();

	def DoAuthToggle(self, event):
		if self.ui_auth.GetValue():
			self.ui_contact.Enable();
		else:
			self.ui_contact.Disable();

