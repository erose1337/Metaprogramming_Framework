import wx;
import TinyChatGUI;
import ConnectForm;
import TinyChat;

class ChatForm(TinyChatGUI.ChatForm):
	def __init__(self, contact = False):
		self.shiftDown = False;
		self.contact = contact;
		self.remoteName = False;
		self.sessionKeyRequested = False;
		self.chatLog = "";
		self.timerCheck = 0;
		TinyChatGUI.ChatForm.__init__(self, None)
		self.ui_status.SetStatusText("Connecting...");

	def DoTimer(self, event):
		if TinyChat.IsDisconnected():
			ConnectForm.ConnectForm().Show();
			self.Close();
			return;
		TinyChat.RecvSock();
		if self.remoteName == False:
			h = TinyChat.GetRemoteID();
			if h == False: return;
			if self.contact != False and self.contact != h:
				dlg = wx.MessageDialog(self, "Incorrect Partner: %s" % h.encode("hex"), "TinyChat", wx.OK | wx.ICON_WARNING);
				dlg.ShowModal();
				dlg.Destroy();
				self.Close();
				return;
			if self.sessionKeyRequested == False:
				TinyChat.RequestSessionKey();
				self.sessionKeyRequested = True;
				self.ui_status.SetStatusText("Authenticating...");
			self.remoteName = TinyChat.GetRemoteName();
			if self.remoteName != False:
				self.ui_status.SetStatusText("Connected!");
				self.SetTitle("TinyChat - " + self.remoteName);
		else:
			statusText = "";
			if TinyChat.IsRemoteTyping():
				statusText = str(self.remoteName) + " is typing...";
			self.ui_status.SetStatusText(statusText);
			self.timerCheck += 1;
			if self.timerCheck > 10:
				TinyChat.SendTyping(self.ui_input.GetValue() != "");
				self.timerCheck = 0;
			
			inbox = TinyChat.GetInbox();
			for msg in inbox:
				self.chatLog += "<b><font color=\"#7F0000\">" + self.remoteName + "</font></b>: " + msg + "<br>\n";
				self.ui_log.SetPage(str(self.chatLog));
				self.ui_log.Scroll(-1, self.GetClientSize()[0]);
	
	def DoResize(self, event):
		event.Skip();
		wx.CallAfter(self.ui_log.Scroll, -1, self.GetClientSize()[0]);

	def DoInputKey(self, event):
		self.ui_send.Enable(self.ui_input.GetValue() != "");
		self.shiftDown = event.ShiftDown();
		event.Skip();

	def DoInputEnter(self, event):
		if (self.shiftDown == False):
			self.DoSend(event);
		else:
			event.Skip();
	
	def DoSend(self, event):
		msg = str(self.ui_input.GetValue());
		TinyChat.SendMessage(msg);
		TinyChat.SendTyping(False);
		self.chatLog += "<b><font color=\"#00007F\">" + TinyChat.GetName() + "</font></b>: " + msg + "<br>\n";
		self.ui_log.SetPage(str(self.chatLog));
		self.ui_log.Scroll(-1, self.GetClientSize()[0]);
		self.ui_input.SetValue("");
		self.ui_send.Disable();
		pass

