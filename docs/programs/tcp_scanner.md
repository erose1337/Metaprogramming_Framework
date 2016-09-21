tcp_scanner
==============



Scanner
--------------

	No docstring found


Instance defaults: 

	{'_run_queued': False,
	 'context_managed': False,
	 'deleted': False,
	 'dont_save': False,
	 'parse_args': False,
	 'ports': (22,),
	 'priority': 0.04,
	 'range': (0, 0, 0, 255),
	 'replace_reference_on_load': True,
	 'reschedule_run_after_exception': True,
	 'run_callback': None,
	 'run_condition': '',
	 'running': True,
	 'startup_components': (),
	 'subnet': '127.0.0.1',
	 'yield_interval': 100}

Method resolution order: 

	(<class 'tcp_scanner.Scanner'>,
	 <class 'pride.objectlibrary.vmlibrary.Process'>,
	 <class 'pride.objectlibrary.base.Base'>,
	 <type 'object'>)

- **run**(self):

				No documentation available


- **host_discovered**(self, address):

				No documentation available


- **new_thread**(self):

				No documentation available


Tcp_Port_Tester
--------------

	No docstring found


Instance defaults: 

	{'as_port': 0,
	 'auto_connect': True,
	 'blocking': 0,
	 'bypass_network_stack': False,
	 'connect_timeout': 1,
	 'deleted': False,
	 'dont_save': True,
	 'host_info': (),
	 'interface': '0.0.0.0',
	 'ip': '',
	 'parse_args': False,
	 'port': 80,
	 'protocol': 0,
	 'replace_reference_on_load': True,
	 'shutdown_flag': 2,
	 'shutdown_on_close': True,
	 'socket_family': 2,
	 'socket_type': 1,
	 'startup_components': (),
	 'timeout': 0,
	 'wrapped_object': None}

Method resolution order: 

	(<class 'tcp_scanner.Tcp_Port_Tester'>,
	 <class 'pride.objectlibrary.network.Tcp_Client'>,
	 <class 'pride.objectlibrary.network.Tcp_Socket'>,
	 <class 'pride.objectlibrary.network.Socket'>,
	 <class 'pride.objectlibrary.base.Wrapper'>,
	 <class 'pride.objectlibrary.base.Base'>,
	 <type 'object'>)

- **on_connect**(self):

				No documentation available
