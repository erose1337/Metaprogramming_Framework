import os;
import wx;
import sys;
import time;
import math;
import errno;
#import fcntl;
import socket;
import random;
import ChatForm;
import ConnectForm;
import TinyChatGUI;
import ConfigParser;

from Crypto.Cipher import AES;
from Crypto.Hash import SHA256;

PayloadSize = 256;
RSAModulusSize = 8192;
PublicNoiseSize = 512000 - 2 * RSAModulusSize;
NoiseSize = PublicNoiseSize + RSAModulusSize;
FactorSize = RSAModulusSize - PayloadSize;
RingSize = NoiseSize + RSAModulusSize;
Ring = 2 ** RingSize;
Mask = Ring - 1;
RSAExponent = 65537;

appName = "TinyChat";
configFilename = "config.ini";
recvbuf = "";
s = None;
remoteID = False;
remoteKey = False;
remoteExp = False;
remote_n = 0;
remote_e = 0;
remote_k = 0;
remote_h = False;
session_key = False;
dced = False;
my_name = "Guest";
p = 0;
q = 0;
e = 0;
d = 0;
n = 0;
f = 0;
k = 0;
h = False;
kex_send = 0;
remote_name = False;
inbox = [];
typing = False;

MSG_PUBLIC_KEY  = 1
MSG_SESSION_KEY = 2
MSG_NAME		= 3
MSG_MESSAGE	 = 4
MSG_TYPING	  = 5

def RecvMsg(msg):
	global p, q, e, d, n;
	global remote_e, remote_n, remote_k, remote_h;
	global session_key;
	global kex_send;
	global remote_name;
	global inbox;
	global typing;
	tag = ord(msg[0]);
	if tag == MSG_PUBLIC_KEY:
		msg = msg.split(":");
		remote_e = b642int(msg[1]);
		remote_n = b642int(msg[2]);
		remote_k = b642int(msg[3]);
		remote_h = HASH(msg[2] + ":" + msg[3]);
	elif tag == MSG_SESSION_KEY:
		msg = msg.split(":");
		kex_recv_enc = b642int(msg[1]);
		kex_recv = PubDecrypt(kex_recv_enc, n, d, f);
		kex_value = kex_send + kex_recv;
		session_key = str(HASH(int2bin(kex_value)));
		SendName();
	elif tag == MSG_MESSAGE:
		msg = msg.split(":");
		mac = bytearray(msg[2].decode("base64"));
		macp = HMAC(session_key, msg[1] + ":" + msg[3]);
		if not Compare(mac, macp): return;
		iv = bytearray(msg[1].decode("base64"));
		cipher = bytearray(msg[3].decode("base64"));
		inbox.append(Decrypt(session_key, iv, cipher));
	elif tag == MSG_NAME:
		msg = msg.split(":");
		mac = bytearray(msg[2].decode("base64"));
		macp = HMAC(session_key, msg[1] + ":" + msg[3]);
		if not Compare(mac, macp): return;
		iv = bytearray(msg[1].decode("base64"));
		cipher = bytearray(msg[3].decode("base64"));
		remote_name = str(Decrypt(session_key, iv, cipher));
	elif tag == MSG_TYPING:
		msg = msg.split(":");
		mac = bytearray(msg[2].decode("base64"));
		macp = HMAC(session_key, msg[1] + ":" + msg[3]);
		if not Compare(mac, macp): return;
		iv = bytearray(msg[1].decode("base64"));
		cipher = bytearray(msg[3].decode("base64"));
		typing = str(Decrypt(session_key, iv, cipher)) == "True";

def GetRemoteID():
	global remote_h;
	return str(remote_h).encode("hex").strip();
	
def GetRemoteName():
	global remote_name;
	return remote_name;

def IsRemoteTyping():
	global typing;
	return typing;

def SetName(name):
	global my_name;
	my_name = str(name);

def IsDisconnected():
	global dced;
	return dced;

def GetName():
	global my_name;
	return my_name;

def GetInbox():
	global inbox;
	x = inbox;
	inbox = [];
	return x;

def SendHandshake():
	global e, n, k;
	SendMsg(chr(MSG_PUBLIC_KEY) + ":" + int2b64(e)  + ":" + int2b64(n)  + ":" + int2b64(k));

def GetSessionKey():
	global session_key;
	return session_key;

def PubEncrypt(msg, n, e, k):
	global NoiseSize, PublicNoiseSize, Mask;
	pad = k * Random(PublicNoiseSize);
	pad &= Mask;
	pad >>= NoiseSize;
	pad += (msg << 1) + 1;
	msg = pad;
	msg = pow(pad, e, n);
	return msg;

def PubDecrypt(msg, n, d, f):
	global NoiseSize;
	msg = pow(msg, d, n);
	msg <<= NoiseSize;
	msg %= f;
	msg >>= NoiseSize + 1;
	return msg;

def RequestSessionKey():
	global remote_e, remote_n, remote_k;
	global kex_send, PayloadSize;
	kex_send = Random(PayloadSize);
	kex_send_enc = PubEncrypt(kex_send, remote_n, remote_e, remote_k);
	SendMsg(chr(MSG_SESSION_KEY) + ":" + int2b64(kex_send_enc));

def SendMessage(msg):
	SendPacket(MSG_MESSAGE, msg);

def SendTyping(msg):
	SendPacket(MSG_TYPING, msg);

def SendPacket(idx, msg):
	global session_key;
	iv = os.urandom(16);
	iv_b64 = str(iv).encode("base64").strip();
	cipher_b64 = str(Encrypt(session_key, iv, msg)).encode("base64").strip();
	mac = HMAC(session_key, iv_b64 + ":" + cipher_b64);
	mac_b64 = str(mac).encode("base64").strip();
	SendMsg(chr(idx) + ":" + iv_b64 + ":" + mac_b64 + ":" + cipher_b64);

def SendName():
	global my_name;
	global session_key;
	iv = os.urandom(16);
	iv_b64 = str(iv).encode("base64").strip();
	cipher_b64 = str(Encrypt(session_key, iv, my_name)).encode("base64").strip();
	mac = HMAC(session_key, iv_b64 + ":" + cipher_b64);
	mac_b64 = str(mac).encode("base64").strip();
	SendMsg(chr(MSG_NAME) + ":" + iv_b64 + ":" + mac_b64 + ":" + cipher_b64);

def SetupClient(host):
	global s;
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
	ok = False;
	try:
		s.connect(host);
		SendHandshake();
		#fcntl.fcntl(s, fcntl.F_SETFL, os.O_NONBLOCK);
		s.setblocking(0);
		ok = True;
	except:
		pass;
	return ok;

def SetupServer(port):
	global s;
	ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
	ls.bind(("127.0.0.1", int(port)));
	ls.listen(1);
	s, addr = ls.accept();
	SendHandshake();
	#fcntl.fcntl(s, fcntl.F_SETFL, os.O_NONBLOCK);
	s.setblocking(0);
	return True;

def SendMsg(msg):
	global dced;
	global s;
	try:
		s.send(str(int2bin(len(msg), 8)));
		s.send(msg);
		return True;
	except:
		pass;
	dced = True;
	return False;

def RecvSock():
	global s;
	global recvbuf;
	global dced;
	msg = "";
	try:
		msg = str(s.recv(4096));
	except socket.error, e:
		err = e.args[0]
		if err != errno.EAGAIN and err != errno.EWOULDBLOCK:
			print e;
			dced = True;
		return False;
	recvbuf += msg;
	while len(recvbuf) > 8:
		length = bin2int(recvbuf[:8]) + 8;
		if len(recvbuf) >= length:
			buf = recvbuf[8:length];
			recvbuf = recvbuf[length:];
			RecvMsg(buf);

def GetLocalID(form):
	global p, q, e, d, n, k, f;
	global NoiseSize, PublicNoiseSize, FactorSize, Mask, Ring;
	global RSAExponent;
	expected = math.ceil(math.log(2) * RSAModulusSize);
	tests = 0;
	pmask = (2**(RSAModulusSize/2)) | 1;

	p = b642int(GetConfig("P", ""));
	while p == 0:
		p = Random(RSAModulusSize/2) | pmask;
		if IsPrime(p):
			SetConfig("P", int2b64(p));
			break;
		p = 0;
		tests += 1;
		if (tests % 10 == 1) and (form != False):
			form.ui_progress.SetValue(SoftProgress(tests, expected));
			form.Update();
			wx.Yield();

	tests = expected / 2;
	if form != False:
		form.ui_progress.SetValue(SoftProgress(tests, expected));
		form.Update();
		wx.Yield();
	
	q = b642int(GetConfig("Q", ""));
	while q == 0:
		q = Random(RSAModulusSize/2) | pmask;
		if IsPrime(q):
			SetConfig("Q", int2b64(q));
			break;
		q = 0;
		tests += 1;
		if (tests % 10 == 1) and (form != False):
			form.ui_progress.SetValue(SoftProgress(tests, expected));
			form.Update();
			wx.Yield();

	if form != False:
		form.ui_progress.SetValue(SoftProgress(expected, expected));
		form.Update();
		wx.Yield();

	e = b642int(GetConfig("E", int2b64(RSAExponent)));
	d = b642int(GetConfig("D", ""));
	if d == 0:
		phi = (p-1)*(q-1);
		e = RSAExponent;
		while True:
			d = ModInv(e, phi);
			if d != 0: break;
			e = RSAExponent | (2**random.randint(16));
		SetConfig("E", int2b64(e));
		SetConfig("D", int2b64(d));

	n = p * q
	nb64 = int2b64(n);
	SetConfig("N", nb64);

	f_compressed = b642int(GetConfig("F", ""));
	if f_compressed == 0:
		f_compressed = Random(FactorSize);
		SetConfig("F", int2b64(f_compressed));
	f = Ring // f_compressed;

	k = pow(3, 65536, Ring);
	kb64 = GetConfig("K", "");
	k_compressed = b642int(kb64);
	if k_compressed == 0:
		k_compressed = (k % f) >> (NoiseSize - PublicNoiseSize);
		kb64 = int2b64(k_compressed);
		SetConfig("K", kb64);
	k -= k_compressed << (NoiseSize - PublicNoiseSize);

	h = HASH(nb64 + ":" + kb64);
	SetConfig("H", str(h).encode("hex"));
	return h;

def SetConfig(key, value):
	try:
		Config.add_section(appName);
	except:
		pass;
	Config.set(appName, key, value);
	with open(appData + configFilename, "w") as fp: Config.write(fp);

def GetConfig(key, default = False):
	try:
		return Config.get(appName, key);
	except:
		pass;
	return default;

def Random(n):
	bytes = (n + 7) // 8;
	raw = os.urandom(bytes);
	x = int(raw.encode("hex"), 16);
	x >>= bytes * 8 - n;
	return x;

def IsPrime(n, k = 16):
	if n < 2: return False
	for p in [2,3,5,7,11,13,17,19,23,29]:
		if n % p == 0: return n == p
	s, d = 0, n-1
	while d % 2 == 0:
		s, d = s+1, d/2
	for i in range(k):
		x = pow(random.randint(2, n-1), d, n)
		if x == 1 or x == n-1: continue
		for r in range(1, s):
			x = (x * x) % n
			if x == 1: return False
			if x == n-1: break
		else: return False
	return True

def egcd(a, b):
	if a == 0: return (b, 0, 1)
	g, y, x = egcd(b % a, a)
	return (g, x - (b // a) * y, y)

def ModInv(a, m):
	g, x, y = egcd(a, m);
	if g == 1: return x % m;
	return 0;

def SoftProgress(x, y):
	xy = x / y;
	xx4 = xy * xy * xy * 4;
	return 100 * math.sqrt(xx4 / (1 + xx4));

def bin2int(data):
	data = bytearray(data);
	output = 0	
	size = len(data)
	for index in range(size):
		output |= data[index] << (8 * (size - 1 - index))
	return output

def int2bin(integer, _bytes=0):
	output = bytearray()
	if _bytes == 0:
		x = 1;
		while x < abs(integer):
			x <<= 1;
			_bytes += 1;
		_bytes = (_bytes + 7) // 8;
	for byte in range(_bytes):
		output.append((integer >> (8 * (_bytes - 1 - byte))) & 255)
	return output

def HASH(msg):
	sha256 = SHA256.new();
	sha256.update(msg);
	return bytearray(sha256.digest());

def Compare(a, b):
	length = len(a);
	if length != len(b): return False;
	delta = 0;
	for i in range(0, length):
		delta |= a[i] ^ b[i];
	return delta == 0;

def HMAC(key, msg):
	key = bytearray(key);
	opad = bytearray("\x5C" * len(key));
	ipad = bytearray("\x36" * len(key));
	for index, byte in enumerate(key):
		opad[index] ^= byte;
		ipad[index] ^= byte;
	return HASH(opad + HASH(ipad + msg));

def Encrypt(password, iv, msg):
	sha256 = SHA256.new();
	sha256.update(str(password));
	key = sha256.digest();
	msg = str(msg);
	length = 16 - (len(msg) % 16);
	msg = str(msg) + (chr(length) * length);
	aes = AES.new(key, AES.MODE_CBC, str(iv));
	return bytearray(aes.encrypt(msg));

def Decrypt(password, iv, msg):
	sha256 = SHA256.new();
	sha256.update(str(password));
	key = sha256.digest();
	aes = AES.new(key, AES.MODE_CBC, str(iv));
	msg = bytearray(aes.decrypt(str(msg)));
	return msg[:-msg[-1]];

slash = "/";
if sys.platform == "win32":
	slash = "\\";
	appData = os.environ['APPDATA'] + slash + appName + slash;
else:
	appData = os.environ['HOME'] + slash + "." + appName + slash;
if not os.path.exists(appData):
	os.makedirs(appData);
Config = ConfigParser.ConfigParser();
Config.read(appData + configFilename);

def int2b64(x):
	return str(int2bin(int(x))).encode("base64").strip();

def b642int(x):
	return bin2int(str(x).decode("base64"));

