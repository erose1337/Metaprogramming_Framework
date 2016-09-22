
permuteencrypttest.exe:     file format pei-i386


Disassembly of section .text:

00401000 <__gnu_exception_handler@4>:
  401000:	53                   	push   ebx
  401001:	83 ec 18             	sub    esp,0x18
  401004:	8b 44 24 20          	mov    eax,DWORD PTR [esp+0x20]
  401008:	8b 00                	mov    eax,DWORD PTR [eax]
  40100a:	8b 00                	mov    eax,DWORD PTR [eax]
  40100c:	3d 91 00 00 c0       	cmp    eax,0xc0000091
  401011:	77 4d                	ja     401060 <__gnu_exception_handler@4+0x60>
  401013:	3d 8d 00 00 c0       	cmp    eax,0xc000008d
  401018:	73 5b                	jae    401075 <__gnu_exception_handler@4+0x75>
  40101a:	3d 05 00 00 c0       	cmp    eax,0xc0000005
  40101f:	0f 85 8e 00 00 00    	jne    4010b3 <__gnu_exception_handler@4+0xb3>
  401025:	c7 44 24 04 00 00 00 	mov    DWORD PTR [esp+0x4],0x0
  40102c:	00 
  40102d:	c7 04 24 0b 00 00 00 	mov    DWORD PTR [esp],0xb
  401034:	e8 37 70 00 00       	call   408070 <_signal>
  401039:	83 f8 01             	cmp    eax,0x1
  40103c:	0f 84 c1 00 00 00    	je     401103 <__gnu_exception_handler@4+0x103>
  401042:	85 c0                	test   eax,eax
  401044:	0f 85 a6 00 00 00    	jne    4010f0 <__gnu_exception_handler@4+0xf0>
  40104a:	8d b6 00 00 00 00    	lea    esi,[esi+0x0]
  401050:	31 c0                	xor    eax,eax
  401052:	83 c4 18             	add    esp,0x18
  401055:	5b                   	pop    ebx
  401056:	c2 04 00             	ret    0x4
  401059:	8d b4 26 00 00 00 00 	lea    esi,[esi+eiz*1+0x0]
  401060:	3d 94 00 00 c0       	cmp    eax,0xc0000094
  401065:	74 19                	je     401080 <__gnu_exception_handler@4+0x80>
  401067:	3d 96 00 00 c0       	cmp    eax,0xc0000096
  40106c:	74 4c                	je     4010ba <__gnu_exception_handler@4+0xba>
  40106e:	3d 93 00 00 c0       	cmp    eax,0xc0000093
  401073:	75 db                	jne    401050 <__gnu_exception_handler@4+0x50>
  401075:	bb 01 00 00 00       	mov    ebx,0x1
  40107a:	eb 06                	jmp    401082 <__gnu_exception_handler@4+0x82>
  40107c:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  401080:	31 db                	xor    ebx,ebx
  401082:	c7 44 24 04 00 00 00 	mov    DWORD PTR [esp+0x4],0x0
  401089:	00 
  40108a:	c7 04 24 08 00 00 00 	mov    DWORD PTR [esp],0x8
  401091:	e8 da 6f 00 00       	call   408070 <_signal>
  401096:	83 f8 01             	cmp    eax,0x1
  401099:	0f 84 a1 00 00 00    	je     401140 <__gnu_exception_handler@4+0x140>
  40109f:	85 c0                	test   eax,eax
  4010a1:	74 ad                	je     401050 <__gnu_exception_handler@4+0x50>
  4010a3:	c7 04 24 08 00 00 00 	mov    DWORD PTR [esp],0x8
  4010aa:	ff d0                	call   eax
  4010ac:	b8 ff ff ff ff       	mov    eax,0xffffffff
  4010b1:	eb 9f                	jmp    401052 <__gnu_exception_handler@4+0x52>
  4010b3:	3d 1d 00 00 c0       	cmp    eax,0xc000001d
  4010b8:	75 96                	jne    401050 <__gnu_exception_handler@4+0x50>
  4010ba:	c7 44 24 04 00 00 00 	mov    DWORD PTR [esp+0x4],0x0
  4010c1:	00 
  4010c2:	c7 04 24 04 00 00 00 	mov    DWORD PTR [esp],0x4
  4010c9:	e8 a2 6f 00 00       	call   408070 <_signal>
  4010ce:	83 f8 01             	cmp    eax,0x1
  4010d1:	74 4c                	je     40111f <__gnu_exception_handler@4+0x11f>
  4010d3:	85 c0                	test   eax,eax
  4010d5:	0f 84 75 ff ff ff    	je     401050 <__gnu_exception_handler@4+0x50>
  4010db:	c7 04 24 04 00 00 00 	mov    DWORD PTR [esp],0x4
  4010e2:	ff d0                	call   eax
  4010e4:	b8 ff ff ff ff       	mov    eax,0xffffffff
  4010e9:	e9 64 ff ff ff       	jmp    401052 <__gnu_exception_handler@4+0x52>
  4010ee:	66 90                	xchg   ax,ax
  4010f0:	c7 04 24 0b 00 00 00 	mov    DWORD PTR [esp],0xb
  4010f7:	ff d0                	call   eax
  4010f9:	b8 ff ff ff ff       	mov    eax,0xffffffff
  4010fe:	e9 4f ff ff ff       	jmp    401052 <__gnu_exception_handler@4+0x52>
  401103:	c7 44 24 04 01 00 00 	mov    DWORD PTR [esp+0x4],0x1
  40110a:	00 
  40110b:	c7 04 24 0b 00 00 00 	mov    DWORD PTR [esp],0xb
  401112:	e8 59 6f 00 00       	call   408070 <_signal>
  401117:	83 c8 ff             	or     eax,0xffffffff
  40111a:	e9 33 ff ff ff       	jmp    401052 <__gnu_exception_handler@4+0x52>
  40111f:	c7 44 24 04 01 00 00 	mov    DWORD PTR [esp+0x4],0x1
  401126:	00 
  401127:	c7 04 24 04 00 00 00 	mov    DWORD PTR [esp],0x4
  40112e:	e8 3d 6f 00 00       	call   408070 <_signal>
  401133:	83 c8 ff             	or     eax,0xffffffff
  401136:	e9 17 ff ff ff       	jmp    401052 <__gnu_exception_handler@4+0x52>
  40113b:	90                   	nop
  40113c:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  401140:	c7 44 24 04 01 00 00 	mov    DWORD PTR [esp+0x4],0x1
  401147:	00 
  401148:	c7 04 24 08 00 00 00 	mov    DWORD PTR [esp],0x8
  40114f:	e8 1c 6f 00 00       	call   408070 <_signal>
  401154:	85 db                	test   ebx,ebx
  401156:	b8 ff ff ff ff       	mov    eax,0xffffffff
  40115b:	0f 84 f1 fe ff ff    	je     401052 <__gnu_exception_handler@4+0x52>
  401161:	89 44 24 0c          	mov    DWORD PTR [esp+0xc],eax
  401165:	e8 06 05 00 00       	call   401670 <__fpreset>
  40116a:	8b 44 24 0c          	mov    eax,DWORD PTR [esp+0xc]
  40116e:	e9 df fe ff ff       	jmp    401052 <__gnu_exception_handler@4+0x52>
  401173:	8d b6 00 00 00 00    	lea    esi,[esi+0x0]
  401179:	8d bc 27 00 00 00 00 	lea    edi,[edi+eiz*1+0x0]

00401180 <___mingw_CRTStartup>:
  401180:	55                   	push   ebp
  401181:	89 e5                	mov    ebp,esp
  401183:	53                   	push   ebx
  401184:	83 ec 14             	sub    esp,0x14
  401187:	a1 80 a0 40 00       	mov    eax,ds:0x40a080
  40118c:	85 c0                	test   eax,eax
  40118e:	74 1c                	je     4011ac <___mingw_CRTStartup+0x2c>
  401190:	c7 44 24 08 00 00 00 	mov    DWORD PTR [esp+0x8],0x0
  401197:	00 
  401198:	c7 44 24 04 02 00 00 	mov    DWORD PTR [esp+0x4],0x2
  40119f:	00 
  4011a0:	c7 04 24 00 00 00 00 	mov    DWORD PTR [esp],0x0
  4011a7:	ff d0                	call   eax
  4011a9:	83 ec 0c             	sub    esp,0xc
  4011ac:	c7 04 24 00 10 40 00 	mov    DWORD PTR [esp],0x401000
  4011b3:	e8 b0 6f 00 00       	call   408168 <_SetUnhandledExceptionFilter@4>
  4011b8:	83 ec 04             	sub    esp,0x4
  4011bb:	e8 c0 04 00 00       	call   401680 <___cpu_features_init>
  4011c0:	e8 ab 04 00 00       	call   401670 <__fpreset>
  4011c5:	e8 96 05 00 00       	call   401760 <__setargv>
  4011ca:	a1 30 d0 40 00       	mov    eax,ds:0x40d030
  4011cf:	85 c0                	test   eax,eax
  4011d1:	74 42                	je     401215 <___mingw_CRTStartup+0x95>
  4011d3:	8b 1d cc e1 40 00    	mov    ebx,DWORD PTR ds:0x40e1cc
  4011d9:	a3 00 90 40 00       	mov    ds:0x409000,eax
  4011de:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
  4011e2:	8b 43 10             	mov    eax,DWORD PTR [ebx+0x10]
  4011e5:	89 04 24             	mov    DWORD PTR [esp],eax
  4011e8:	e8 8b 6e 00 00       	call   408078 <__setmode>
  4011ed:	a1 30 d0 40 00       	mov    eax,ds:0x40d030
  4011f2:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
  4011f6:	8b 43 30             	mov    eax,DWORD PTR [ebx+0x30]
  4011f9:	89 04 24             	mov    DWORD PTR [esp],eax
  4011fc:	e8 77 6e 00 00       	call   408078 <__setmode>
  401201:	a1 30 d0 40 00       	mov    eax,ds:0x40d030
  401206:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
  40120a:	8b 43 50             	mov    eax,DWORD PTR [ebx+0x50]
  40120d:	89 04 24             	mov    DWORD PTR [esp],eax
  401210:	e8 63 6e 00 00       	call   408078 <__setmode>
  401215:	e8 66 6e 00 00       	call   408080 <___p__fmode>
  40121a:	8b 15 00 90 40 00    	mov    edx,DWORD PTR ds:0x409000
  401220:	89 10                	mov    DWORD PTR [eax],edx
  401222:	e8 89 09 00 00       	call   401bb0 <__pei386_runtime_relocator>
  401227:	83 e4 f0             	and    esp,0xfffffff0
  40122a:	e8 e1 0b 00 00       	call   401e10 <___main>
  40122f:	e8 54 6e 00 00       	call   408088 <___p__environ>
  401234:	8b 00                	mov    eax,DWORD PTR [eax]
  401236:	89 44 24 08          	mov    DWORD PTR [esp+0x8],eax
  40123a:	a1 00 d0 40 00       	mov    eax,ds:0x40d000
  40123f:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
  401243:	a1 04 d0 40 00       	mov    eax,ds:0x40d004
  401248:	89 04 24             	mov    DWORD PTR [esp],eax
  40124b:	e8 30 72 00 00       	call   408480 <_main>
  401250:	89 c3                	mov    ebx,eax
  401252:	e8 39 6e 00 00       	call   408090 <__cexit>
  401257:	89 1c 24             	mov    DWORD PTR [esp],ebx
  40125a:	e8 11 6f 00 00       	call   408170 <_ExitProcess@4>
  40125f:	90                   	nop

00401260 <__mingw32_init_mainargs>:
  401260:	83 ec 3c             	sub    esp,0x3c
  401263:	8d 44 24 2c          	lea    eax,[esp+0x2c]
  401267:	89 44 24 10          	mov    DWORD PTR [esp+0x10],eax
  40126b:	a1 04 90 40 00       	mov    eax,ds:0x409004
  401270:	c7 44 24 04 00 d0 40 	mov    DWORD PTR [esp+0x4],0x40d000
  401277:	00 
  401278:	c7 04 24 04 d0 40 00 	mov    DWORD PTR [esp],0x40d004
  40127f:	c7 44 24 2c 00 00 00 	mov    DWORD PTR [esp+0x2c],0x0
  401286:	00 
  401287:	83 e0 01             	and    eax,0x1
  40128a:	89 44 24 0c          	mov    DWORD PTR [esp+0xc],eax
  40128e:	8d 44 24 28          	lea    eax,[esp+0x28]
  401292:	89 44 24 08          	mov    DWORD PTR [esp+0x8],eax
  401296:	e8 fd 6d 00 00       	call   408098 <___getmainargs>
  40129b:	83 c4 3c             	add    esp,0x3c
  40129e:	c3                   	ret    
  40129f:	90                   	nop

004012a0 <_mainCRTStartup>:
  4012a0:	83 ec 1c             	sub    esp,0x1c
  4012a3:	c7 04 24 01 00 00 00 	mov    DWORD PTR [esp],0x1
  4012aa:	ff 15 bc e1 40 00    	call   DWORD PTR ds:0x40e1bc
  4012b0:	e8 cb fe ff ff       	call   401180 <___mingw_CRTStartup>
  4012b5:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  4012b9:	8d bc 27 00 00 00 00 	lea    edi,[edi+eiz*1+0x0]

004012c0 <_WinMainCRTStartup>:
  4012c0:	83 ec 1c             	sub    esp,0x1c
  4012c3:	c7 04 24 02 00 00 00 	mov    DWORD PTR [esp],0x2
  4012ca:	ff 15 bc e1 40 00    	call   DWORD PTR ds:0x40e1bc
  4012d0:	e8 ab fe ff ff       	call   401180 <___mingw_CRTStartup>
  4012d5:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  4012d9:	8d bc 27 00 00 00 00 	lea    edi,[edi+eiz*1+0x0]

004012e0 <_atexit>:
  4012e0:	a1 dc e1 40 00       	mov    eax,ds:0x40e1dc
  4012e5:	ff e0                	jmp    eax
  4012e7:	89 f6                	mov    esi,esi
  4012e9:	8d bc 27 00 00 00 00 	lea    edi,[edi+eiz*1+0x0]

004012f0 <__onexit>:
  4012f0:	a1 d0 e1 40 00       	mov    eax,ds:0x40e1d0
  4012f5:	ff e0                	jmp    eax
  4012f7:	90                   	nop
  4012f8:	90                   	nop
  4012f9:	90                   	nop
  4012fa:	90                   	nop
  4012fb:	90                   	nop
  4012fc:	90                   	nop
  4012fd:	90                   	nop
  4012fe:	90                   	nop
  4012ff:	90                   	nop

00401300 <___gcc_register_frame>:
  401300:	55                   	push   ebp
  401301:	89 e5                	mov    ebp,esp
  401303:	83 ec 18             	sub    esp,0x18
  401306:	c7 04 24 00 a0 40 00 	mov    DWORD PTR [esp],0x40a000
  40130d:	e8 66 6e 00 00       	call   408178 <_GetModuleHandleA@4>
  401312:	ba 00 00 00 00       	mov    edx,0x0
  401317:	83 ec 04             	sub    esp,0x4
  40131a:	85 c0                	test   eax,eax
  40131c:	74 15                	je     401333 <___gcc_register_frame+0x33>
  40131e:	c7 44 24 04 13 a0 40 	mov    DWORD PTR [esp+0x4],0x40a013
  401325:	00 
  401326:	89 04 24             	mov    DWORD PTR [esp],eax
  401329:	e8 52 6e 00 00       	call   408180 <_GetProcAddress@8>
  40132e:	83 ec 08             	sub    esp,0x8
  401331:	89 c2                	mov    edx,eax
  401333:	85 d2                	test   edx,edx
  401335:	74 11                	je     401348 <___gcc_register_frame+0x48>
  401337:	c7 44 24 04 08 d0 40 	mov    DWORD PTR [esp+0x4],0x40d008
  40133e:	00 
  40133f:	c7 04 24 c0 b0 40 00 	mov    DWORD PTR [esp],0x40b0c0
  401346:	ff d2                	call   edx
  401348:	a1 24 90 40 00       	mov    eax,ds:0x409024
  40134d:	85 c0                	test   eax,eax
  40134f:	74 3a                	je     40138b <___gcc_register_frame+0x8b>
  401351:	c7 04 24 29 a0 40 00 	mov    DWORD PTR [esp],0x40a029
  401358:	e8 1b 6e 00 00       	call   408178 <_GetModuleHandleA@4>
  40135d:	ba 00 00 00 00       	mov    edx,0x0
  401362:	83 ec 04             	sub    esp,0x4
  401365:	85 c0                	test   eax,eax
  401367:	74 15                	je     40137e <___gcc_register_frame+0x7e>
  401369:	c7 44 24 04 37 a0 40 	mov    DWORD PTR [esp+0x4],0x40a037
  401370:	00 
  401371:	89 04 24             	mov    DWORD PTR [esp],eax
  401374:	e8 07 6e 00 00       	call   408180 <_GetProcAddress@8>
  401379:	83 ec 08             	sub    esp,0x8
  40137c:	89 c2                	mov    edx,eax
  40137e:	85 d2                	test   edx,edx
  401380:	74 09                	je     40138b <___gcc_register_frame+0x8b>
  401382:	c7 04 24 24 90 40 00 	mov    DWORD PTR [esp],0x409024
  401389:	ff d2                	call   edx
  40138b:	c9                   	leave  
  40138c:	c3                   	ret    
  40138d:	8d 76 00             	lea    esi,[esi+0x0]

00401390 <___gcc_deregister_frame>:
  401390:	55                   	push   ebp
  401391:	89 e5                	mov    ebp,esp
  401393:	83 ec 18             	sub    esp,0x18
  401396:	c7 04 24 00 a0 40 00 	mov    DWORD PTR [esp],0x40a000
  40139d:	e8 d6 6d 00 00       	call   408178 <_GetModuleHandleA@4>
  4013a2:	ba 00 00 00 00       	mov    edx,0x0
  4013a7:	83 ec 04             	sub    esp,0x4
  4013aa:	85 c0                	test   eax,eax
  4013ac:	74 15                	je     4013c3 <___gcc_deregister_frame+0x33>
  4013ae:	c7 44 24 04 4b a0 40 	mov    DWORD PTR [esp+0x4],0x40a04b
  4013b5:	00 
  4013b6:	89 04 24             	mov    DWORD PTR [esp],eax
  4013b9:	e8 c2 6d 00 00       	call   408180 <_GetProcAddress@8>
  4013be:	83 ec 08             	sub    esp,0x8
  4013c1:	89 c2                	mov    edx,eax
  4013c3:	85 d2                	test   edx,edx
  4013c5:	74 09                	je     4013d0 <___gcc_deregister_frame+0x40>
  4013c7:	c7 04 24 c0 b0 40 00 	mov    DWORD PTR [esp],0x40b0c0
  4013ce:	ff d2                	call   edx
  4013d0:	c9                   	leave  
  4013d1:	c3                   	ret    
  4013d2:	90                   	nop
  4013d3:	90                   	nop
  4013d4:	90                   	nop
  4013d5:	90                   	nop
  4013d6:	90                   	nop
  4013d7:	90                   	nop
  4013d8:	90                   	nop
  4013d9:	90                   	nop
  4013da:	90                   	nop
  4013db:	90                   	nop
  4013dc:	90                   	nop
  4013dd:	90                   	nop
  4013de:	90                   	nop
  4013df:	90                   	nop

004013e0 <_key_schedule>:
  4013e0:	55                   	push   ebp
  4013e1:	57                   	push   edi
  4013e2:	56                   	push   esi
  4013e3:	53                   	push   ebx
  4013e4:	83 ec 10             	sub    esp,0x10
  4013e7:	8b 44 24 24          	mov    eax,DWORD PTR [esp+0x24]
  4013eb:	8b 74 24 28          	mov    esi,DWORD PTR [esp+0x28]
  4013ef:	8b 48 04             	mov    ecx,DWORD PTR [eax+0x4]
  4013f2:	8b 58 08             	mov    ebx,DWORD PTR [eax+0x8]
  4013f5:	8d 7e 30             	lea    edi,[esi+0x30]
  4013f8:	8b 10                	mov    edx,DWORD PTR [eax]
  4013fa:	8b 40 0c             	mov    eax,DWORD PTR [eax+0xc]
  4013fd:	89 4c 24 04          	mov    DWORD PTR [esp+0x4],ecx
  401401:	89 1c 24             	mov    DWORD PTR [esp],ebx
  401404:	89 7c 24 0c          	mov    DWORD PTR [esp+0xc],edi
  401408:	89 44 24 08          	mov    DWORD PTR [esp+0x8],eax
  40140c:	89 df                	mov    edi,ebx
  40140e:	89 c5                	mov    ebp,eax
  401410:	31 cf                	xor    edi,ecx
  401412:	31 dd                	xor    ebp,ebx
  401414:	31 c7                	xor    edi,eax
  401416:	01 d7                	add    edi,edx
  401418:	89 ea                	mov    edx,ebp
  40141a:	21 ca                	and    edx,ecx
  40141c:	c1 cf 1f             	ror    edi,0x1f
  40141f:	31 c2                	xor    edx,eax
  401421:	31 fa                	xor    edx,edi
  401423:	c1 ca 15             	ror    edx,0x15
  401426:	89 d7                	mov    edi,edx
  401428:	31 d5                	xor    ebp,edx
  40142a:	31 c7                	xor    edi,eax
  40142c:	01 cd                	add    ebp,ecx
  40142e:	89 f9                	mov    ecx,edi
  401430:	21 d9                	and    ecx,ebx
  401432:	c1 cd 1e             	ror    ebp,0x1e
  401435:	31 d1                	xor    ecx,edx
  401437:	31 e9                	xor    ecx,ebp
  401439:	c1 c9 19             	ror    ecx,0x19
  40143c:	89 cd                	mov    ebp,ecx
  40143e:	31 cf                	xor    edi,ecx
  401440:	31 d5                	xor    ebp,edx
  401442:	01 df                	add    edi,ebx
  401444:	89 eb                	mov    ebx,ebp
  401446:	21 c3                	and    ebx,eax
  401448:	c1 cf 1d             	ror    edi,0x1d
  40144b:	31 cb                	xor    ebx,ecx
  40144d:	31 fb                	xor    ebx,edi
  40144f:	8b 7c 24 04          	mov    edi,DWORD PTR [esp+0x4]
  401453:	c1 cb 11             	ror    ebx,0x11
  401456:	31 dd                	xor    ebp,ebx
  401458:	01 c5                	add    ebp,eax
  40145a:	89 d8                	mov    eax,ebx
  40145c:	31 c8                	xor    eax,ecx
  40145e:	21 d0                	and    eax,edx
  401460:	c1 cd 1b             	ror    ebp,0x1b
  401463:	31 d8                	xor    eax,ebx
  401465:	31 e8                	xor    eax,ebp
  401467:	8b 6c 24 08          	mov    ebp,DWORD PTR [esp+0x8]
  40146b:	c1 c8 0f             	ror    eax,0xf
  40146e:	31 fa                	xor    edx,edi
  401470:	33 1c 24             	xor    ebx,DWORD PTR [esp]
  401473:	31 f9                	xor    ecx,edi
  401475:	89 16                	mov    DWORD PTR [esi],edx
  401477:	31 fa                	xor    edx,edi
  401479:	83 c6 10             	add    esi,0x10
  40147c:	31 e8                	xor    eax,ebp
  40147e:	89 4e f4             	mov    DWORD PTR [esi-0xc],ecx
  401481:	31 f9                	xor    ecx,edi
  401483:	89 5e f8             	mov    DWORD PTR [esi-0x8],ebx
  401486:	89 46 fc             	mov    DWORD PTR [esi-0x4],eax
  401489:	31 e8                	xor    eax,ebp
  40148b:	33 1c 24             	xor    ebx,DWORD PTR [esp]
  40148e:	3b 74 24 0c          	cmp    esi,DWORD PTR [esp+0xc]
  401492:	0f 85 74 ff ff ff    	jne    40140c <_key_schedule+0x2c>
  401498:	83 c4 10             	add    esp,0x10
  40149b:	5b                   	pop    ebx
  40149c:	5e                   	pop    esi
  40149d:	5f                   	pop    edi
  40149e:	5d                   	pop    ebp
  40149f:	c3                   	ret    

004014a0 <_encrypt>:
  4014a0:	55                   	push   ebp
  4014a1:	57                   	push   edi
  4014a2:	56                   	push   esi
  4014a3:	53                   	push   ebx
  4014a4:	83 ec 3c             	sub    esp,0x3c
  4014a7:	8b 44 24 50          	mov    eax,DWORD PTR [esp+0x50]
  4014ab:	8b 28                	mov    ebp,DWORD PTR [eax]
  4014ad:	8b 70 04             	mov    esi,DWORD PTR [eax+0x4]
  4014b0:	8b 78 08             	mov    edi,DWORD PTR [eax+0x8]
  4014b3:	8b 58 0c             	mov    ebx,DWORD PTR [eax+0xc]
  4014b6:	8d 44 24 0c          	lea    eax,[esp+0xc]
  4014ba:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
  4014be:	8b 44 24 54          	mov    eax,DWORD PTR [esp+0x54]
  4014c2:	89 04 24             	mov    DWORD PTR [esp],eax
  4014c5:	e8 16 ff ff ff       	call   4013e0 <_key_schedule>
  4014ca:	8d 4c 24 10          	lea    ecx,[esp+0x10]
  4014ce:	8b 01                	mov    eax,DWORD PTR [ecx]
  4014d0:	33 79 04             	xor    edi,DWORD PTR [ecx+0x4]
  4014d3:	33 59 08             	xor    ebx,DWORD PTR [ecx+0x8]
  4014d6:	c7 44 24 08 02 00 00 	mov    DWORD PTR [esp+0x8],0x2
  4014dd:	00 
  4014de:	31 c5                	xor    ebp,eax
  4014e0:	31 c6                	xor    esi,eax
  4014e2:	89 f8                	mov    eax,edi
  4014e4:	89 da                	mov    edx,ebx
  4014e6:	31 f0                	xor    eax,esi
  4014e8:	31 fa                	xor    edx,edi
  4014ea:	31 d8                	xor    eax,ebx
  4014ec:	01 e8                	add    eax,ebp
  4014ee:	89 d5                	mov    ebp,edx
  4014f0:	21 f5                	and    ebp,esi
  4014f2:	c1 c8 1f             	ror    eax,0x1f
  4014f5:	31 dd                	xor    ebp,ebx
  4014f7:	31 c5                	xor    ebp,eax
  4014f9:	c1 cd 15             	ror    ebp,0x15
  4014fc:	89 e8                	mov    eax,ebp
  4014fe:	31 ea                	xor    edx,ebp
  401500:	31 d8                	xor    eax,ebx
  401502:	01 f2                	add    edx,esi
  401504:	89 c6                	mov    esi,eax
  401506:	21 fe                	and    esi,edi
  401508:	c1 ca 1e             	ror    edx,0x1e
  40150b:	31 ee                	xor    esi,ebp
  40150d:	31 d6                	xor    esi,edx
  40150f:	c1 ce 19             	ror    esi,0x19
  401512:	89 f2                	mov    edx,esi
  401514:	31 f0                	xor    eax,esi
  401516:	31 ea                	xor    edx,ebp
  401518:	01 f8                	add    eax,edi
  40151a:	89 d7                	mov    edi,edx
  40151c:	21 df                	and    edi,ebx
  40151e:	c1 c8 1d             	ror    eax,0x1d
  401521:	31 f7                	xor    edi,esi
  401523:	31 c7                	xor    edi,eax
  401525:	c1 cf 11             	ror    edi,0x11
  401528:	31 fa                	xor    edx,edi
  40152a:	01 da                	add    edx,ebx
  40152c:	89 fb                	mov    ebx,edi
  40152e:	31 f3                	xor    ebx,esi
  401530:	21 eb                	and    ebx,ebp
  401532:	c1 ca 1b             	ror    edx,0x1b
  401535:	31 fb                	xor    ebx,edi
  401537:	31 d3                	xor    ebx,edx
  401539:	c1 cb 0f             	ror    ebx,0xf
  40153c:	83 6c 24 08 01       	sub    DWORD PTR [esp+0x8],0x1
  401541:	75 9f                	jne    4014e2 <_encrypt+0x42>
  401543:	83 c1 10             	add    ecx,0x10
  401546:	8d 44 24 40          	lea    eax,[esp+0x40]
  40154a:	39 c1                	cmp    ecx,eax
  40154c:	75 80                	jne    4014ce <_encrypt+0x2e>
  40154e:	8b 44 24 10          	mov    eax,DWORD PTR [esp+0x10]
  401552:	8b 4c 24 50          	mov    ecx,DWORD PTR [esp+0x50]
  401556:	33 7c 24 14          	xor    edi,DWORD PTR [esp+0x14]
  40155a:	33 5c 24 18          	xor    ebx,DWORD PTR [esp+0x18]
  40155e:	31 c5                	xor    ebp,eax
  401560:	31 c6                	xor    esi,eax
  401562:	89 29                	mov    DWORD PTR [ecx],ebp
  401564:	89 71 04             	mov    DWORD PTR [ecx+0x4],esi
  401567:	89 79 08             	mov    DWORD PTR [ecx+0x8],edi
  40156a:	89 59 0c             	mov    DWORD PTR [ecx+0xc],ebx
  40156d:	83 c4 3c             	add    esp,0x3c
  401570:	5b                   	pop    ebx
  401571:	5e                   	pop    esi
  401572:	5f                   	pop    edi
  401573:	5d                   	pop    ebp
  401574:	c3                   	ret    
  401575:	90                   	nop
  401576:	90                   	nop
  401577:	90                   	nop
  401578:	90                   	nop
  401579:	90                   	nop
  40157a:	90                   	nop
  40157b:	90                   	nop
  40157c:	90                   	nop
  40157d:	90                   	nop
  40157e:	90                   	nop
  40157f:	90                   	nop

00401580 <___dyn_tls_dtor@12>:
  401580:	83 ec 1c             	sub    esp,0x1c
  401583:	8b 44 24 24          	mov    eax,DWORD PTR [esp+0x24]
  401587:	85 c0                	test   eax,eax
  401589:	74 15                	je     4015a0 <___dyn_tls_dtor@12+0x20>
  40158b:	83 f8 03             	cmp    eax,0x3
  40158e:	74 10                	je     4015a0 <___dyn_tls_dtor@12+0x20>
  401590:	b8 01 00 00 00       	mov    eax,0x1
  401595:	83 c4 1c             	add    esp,0x1c
  401598:	c2 0c 00             	ret    0xc
  40159b:	90                   	nop
  40159c:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  4015a0:	8b 54 24 28          	mov    edx,DWORD PTR [esp+0x28]
  4015a4:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
  4015a8:	8b 44 24 20          	mov    eax,DWORD PTR [esp+0x20]
  4015ac:	89 54 24 08          	mov    DWORD PTR [esp+0x8],edx
  4015b0:	89 04 24             	mov    DWORD PTR [esp],eax
  4015b3:	e8 18 0a 00 00       	call   401fd0 <___mingw_TLScallback>
  4015b8:	b8 01 00 00 00       	mov    eax,0x1
  4015bd:	83 c4 1c             	add    esp,0x1c
  4015c0:	c2 0c 00             	ret    0xc
  4015c3:	8d b6 00 00 00 00    	lea    esi,[esi+0x0]
  4015c9:	8d bc 27 00 00 00 00 	lea    edi,[edi+eiz*1+0x0]

004015d0 <___dyn_tls_init@12>:
  4015d0:	56                   	push   esi
  4015d1:	53                   	push   ebx
  4015d2:	83 ec 14             	sub    esp,0x14
  4015d5:	83 3d 40 d0 40 00 02 	cmp    DWORD PTR ds:0x40d040,0x2
  4015dc:	8b 44 24 24          	mov    eax,DWORD PTR [esp+0x24]
  4015e0:	74 0a                	je     4015ec <___dyn_tls_init@12+0x1c>
  4015e2:	c7 05 40 d0 40 00 02 	mov    DWORD PTR ds:0x40d040,0x2
  4015e9:	00 00 00 
  4015ec:	83 f8 02             	cmp    eax,0x2
  4015ef:	74 12                	je     401603 <___dyn_tls_init@12+0x33>
  4015f1:	83 f8 01             	cmp    eax,0x1
  4015f4:	74 42                	je     401638 <___dyn_tls_init@12+0x68>
  4015f6:	83 c4 14             	add    esp,0x14
  4015f9:	b8 01 00 00 00       	mov    eax,0x1
  4015fe:	5b                   	pop    ebx
  4015ff:	5e                   	pop    esi
  401600:	c2 0c 00             	ret    0xc
  401603:	be 14 f0 40 00       	mov    esi,0x40f014
  401608:	81 ee 14 f0 40 00    	sub    esi,0x40f014
  40160e:	c1 fe 02             	sar    esi,0x2
  401611:	85 f6                	test   esi,esi
  401613:	7e e1                	jle    4015f6 <___dyn_tls_init@12+0x26>
  401615:	31 db                	xor    ebx,ebx
  401617:	8b 04 9d 14 f0 40 00 	mov    eax,DWORD PTR [ebx*4+0x40f014]
  40161e:	85 c0                	test   eax,eax
  401620:	74 02                	je     401624 <___dyn_tls_init@12+0x54>
  401622:	ff d0                	call   eax
  401624:	83 c3 01             	add    ebx,0x1
  401627:	39 f3                	cmp    ebx,esi
  401629:	75 ec                	jne    401617 <___dyn_tls_init@12+0x47>
  40162b:	83 c4 14             	add    esp,0x14
  40162e:	b8 01 00 00 00       	mov    eax,0x1
  401633:	5b                   	pop    ebx
  401634:	5e                   	pop    esi
  401635:	c2 0c 00             	ret    0xc
  401638:	8b 44 24 28          	mov    eax,DWORD PTR [esp+0x28]
  40163c:	c7 44 24 04 01 00 00 	mov    DWORD PTR [esp+0x4],0x1
  401643:	00 
  401644:	89 44 24 08          	mov    DWORD PTR [esp+0x8],eax
  401648:	8b 44 24 20          	mov    eax,DWORD PTR [esp+0x20]
  40164c:	89 04 24             	mov    DWORD PTR [esp],eax
  40164f:	e8 7c 09 00 00       	call   401fd0 <___mingw_TLScallback>
  401654:	eb a0                	jmp    4015f6 <___dyn_tls_init@12+0x26>
  401656:	8d 76 00             	lea    esi,[esi+0x0]
  401659:	8d bc 27 00 00 00 00 	lea    edi,[edi+eiz*1+0x0]

00401660 <___tlregdtor>:
  401660:	31 c0                	xor    eax,eax
  401662:	c3                   	ret    
  401663:	90                   	nop
  401664:	90                   	nop
  401665:	90                   	nop
  401666:	90                   	nop
  401667:	90                   	nop
  401668:	90                   	nop
  401669:	90                   	nop
  40166a:	90                   	nop
  40166b:	90                   	nop
  40166c:	90                   	nop
  40166d:	90                   	nop
  40166e:	90                   	nop
  40166f:	90                   	nop

00401670 <__fpreset>:
  401670:	db e3                	fninit 
  401672:	c3                   	ret    
  401673:	90                   	nop
  401674:	90                   	nop
  401675:	90                   	nop
  401676:	90                   	nop
  401677:	90                   	nop
  401678:	90                   	nop
  401679:	90                   	nop
  40167a:	90                   	nop
  40167b:	90                   	nop
  40167c:	90                   	nop
  40167d:	90                   	nop
  40167e:	90                   	nop
  40167f:	90                   	nop

00401680 <___cpu_features_init>:
  401680:	9c                   	pushf  
  401681:	9c                   	pushf  
  401682:	58                   	pop    eax
  401683:	89 c2                	mov    edx,eax
  401685:	35 00 00 20 00       	xor    eax,0x200000
  40168a:	50                   	push   eax
  40168b:	9d                   	popf   
  40168c:	9c                   	pushf  
  40168d:	58                   	pop    eax
  40168e:	9d                   	popf   
  40168f:	31 d0                	xor    eax,edx
  401691:	a9 00 00 20 00       	test   eax,0x200000
  401696:	0f 84 a5 00 00 00    	je     401741 <___cpu_features_init+0xc1>
  40169c:	53                   	push   ebx
  40169d:	31 c0                	xor    eax,eax
  40169f:	0f a2                	cpuid  
  4016a1:	85 c0                	test   eax,eax
  4016a3:	0f 84 97 00 00 00    	je     401740 <___cpu_features_init+0xc0>
  4016a9:	b8 01 00 00 00       	mov    eax,0x1
  4016ae:	0f a2                	cpuid  
  4016b0:	f6 c6 01             	test   dh,0x1
  4016b3:	74 07                	je     4016bc <___cpu_features_init+0x3c>
  4016b5:	83 0d 34 d0 40 00 01 	or     DWORD PTR ds:0x40d034,0x1
  4016bc:	f6 c6 80             	test   dh,0x80
  4016bf:	74 07                	je     4016c8 <___cpu_features_init+0x48>
  4016c1:	83 0d 34 d0 40 00 02 	or     DWORD PTR ds:0x40d034,0x2
  4016c8:	f7 c2 00 00 80 00    	test   edx,0x800000
  4016ce:	74 07                	je     4016d7 <___cpu_features_init+0x57>
  4016d0:	83 0d 34 d0 40 00 04 	or     DWORD PTR ds:0x40d034,0x4
  4016d7:	f7 c2 00 00 00 01    	test   edx,0x1000000
  4016dd:	74 07                	je     4016e6 <___cpu_features_init+0x66>
  4016df:	83 0d 34 d0 40 00 08 	or     DWORD PTR ds:0x40d034,0x8
  4016e6:	f7 c2 00 00 00 02    	test   edx,0x2000000
  4016ec:	74 07                	je     4016f5 <___cpu_features_init+0x75>
  4016ee:	83 0d 34 d0 40 00 10 	or     DWORD PTR ds:0x40d034,0x10
  4016f5:	81 e2 00 00 00 04    	and    edx,0x4000000
  4016fb:	74 07                	je     401704 <___cpu_features_init+0x84>
  4016fd:	83 0d 34 d0 40 00 20 	or     DWORD PTR ds:0x40d034,0x20
  401704:	f6 c1 01             	test   cl,0x1
  401707:	74 07                	je     401710 <___cpu_features_init+0x90>
  401709:	83 0d 34 d0 40 00 40 	or     DWORD PTR ds:0x40d034,0x40
  401710:	80 e5 20             	and    ch,0x20
  401713:	75 2e                	jne    401743 <___cpu_features_init+0xc3>
  401715:	b8 00 00 00 80       	mov    eax,0x80000000
  40171a:	0f a2                	cpuid  
  40171c:	3d 00 00 00 80       	cmp    eax,0x80000000
  401721:	76 1d                	jbe    401740 <___cpu_features_init+0xc0>
  401723:	b8 01 00 00 80       	mov    eax,0x80000001
  401728:	0f a2                	cpuid  
  40172a:	85 d2                	test   edx,edx
  40172c:	78 22                	js     401750 <___cpu_features_init+0xd0>
  40172e:	81 e2 00 00 00 40    	and    edx,0x40000000
  401734:	74 0a                	je     401740 <___cpu_features_init+0xc0>
  401736:	81 0d 34 d0 40 00 00 	or     DWORD PTR ds:0x40d034,0x200
  40173d:	02 00 00 
  401740:	5b                   	pop    ebx
  401741:	f3 c3                	repz ret 
  401743:	81 0d 34 d0 40 00 80 	or     DWORD PTR ds:0x40d034,0x80
  40174a:	00 00 00 
  40174d:	eb c6                	jmp    401715 <___cpu_features_init+0x95>
  40174f:	90                   	nop
  401750:	81 0d 34 d0 40 00 00 	or     DWORD PTR ds:0x40d034,0x100
  401757:	01 00 00 
  40175a:	eb d2                	jmp    40172e <___cpu_features_init+0xae>
  40175c:	90                   	nop
  40175d:	90                   	nop
  40175e:	90                   	nop
  40175f:	90                   	nop

00401760 <__setargv>:
  401760:	55                   	push   ebp
  401761:	89 e5                	mov    ebp,esp
  401763:	57                   	push   edi
  401764:	56                   	push   esi
  401765:	53                   	push   ebx
  401766:	83 ec 4c             	sub    esp,0x4c
  401769:	f6 05 04 90 40 00 02 	test   BYTE PTR ds:0x409004,0x2
  401770:	0f 84 ba 02 00 00    	je     401a30 <__setargv+0x2d0>
  401776:	e8 0d 6a 00 00       	call   408188 <_GetCommandLineA@0>
  40177b:	89 65 c0             	mov    DWORD PTR [ebp-0x40],esp
  40177e:	89 04 24             	mov    DWORD PTR [esp],eax
  401781:	89 c6                	mov    esi,eax
  401783:	e8 28 69 00 00       	call   4080b0 <_strlen>
  401788:	8d 44 00 11          	lea    eax,[eax+eax*1+0x11]
  40178c:	83 e0 f0             	and    eax,0xfffffff0
  40178f:	e8 dc 08 00 00       	call   402070 <___chkstk_ms>
  401794:	29 c4                	sub    esp,eax
  401796:	8d 44 24 10          	lea    eax,[esp+0x10]
  40179a:	89 c2                	mov    edx,eax
  40179c:	89 45 c4             	mov    DWORD PTR [ebp-0x3c],eax
  40179f:	a1 04 90 40 00       	mov    eax,ds:0x409004
  4017a4:	c7 45 e4 00 00 00 00 	mov    DWORD PTR [ebp-0x1c],0x0
  4017ab:	c7 45 d0 00 00 00 00 	mov    DWORD PTR [ebp-0x30],0x0
  4017b2:	c7 45 cc 00 00 00 00 	mov    DWORD PTR [ebp-0x34],0x0
  4017b9:	83 e0 40             	and    eax,0x40
  4017bc:	83 f8 01             	cmp    eax,0x1
  4017bf:	19 c0                	sbb    eax,eax
  4017c1:	89 45 c8             	mov    DWORD PTR [ebp-0x38],eax
  4017c4:	31 c0                	xor    eax,eax
  4017c6:	81 65 c8 00 c0 ff ff 	and    DWORD PTR [ebp-0x38],0xffffc000
  4017cd:	81 45 c8 10 40 00 00 	add    DWORD PTR [ebp-0x38],0x4010
  4017d4:	89 55 d4             	mov    DWORD PTR [ebp-0x2c],edx
  4017d7:	83 c6 01             	add    esi,0x1
  4017da:	0f b6 5e ff          	movzx  ebx,BYTE PTR [esi-0x1]
  4017de:	0f be cb             	movsx  ecx,bl
  4017e1:	85 c9                	test   ecx,ecx
  4017e3:	74 7b                	je     401860 <__setargv+0x100>
  4017e5:	80 fb 3f             	cmp    bl,0x3f
  4017e8:	0f 84 13 01 00 00    	je     401901 <__setargv+0x1a1>
  4017ee:	0f 8f ec 00 00 00    	jg     4018e0 <__setargv+0x180>
  4017f4:	80 fb 27             	cmp    bl,0x27
  4017f7:	0f 84 e3 01 00 00    	je     4019e0 <__setargv+0x280>
  4017fd:	80 fb 2a             	cmp    bl,0x2a
  401800:	0f 84 fb 00 00 00    	je     401901 <__setargv+0x1a1>
  401806:	80 fb 22             	cmp    bl,0x22
  401809:	0f 85 36 01 00 00    	jne    401945 <__setargv+0x1e5>
  40180f:	89 c3                	mov    ebx,eax
  401811:	d1 fb                	sar    ebx,1
  401813:	0f 84 3e 02 00 00    	je     401a57 <__setargv+0x2f7>
  401819:	8b 55 d4             	mov    edx,DWORD PTR [ebp-0x2c]
  40181c:	01 d3                	add    ebx,edx
  40181e:	66 90                	xchg   ax,ax
  401820:	83 c2 01             	add    edx,0x1
  401823:	39 da                	cmp    edx,ebx
  401825:	c6 42 ff 5c          	mov    BYTE PTR [edx-0x1],0x5c
  401829:	75 f5                	jne    401820 <__setargv+0xc0>
  40182b:	a8 01                	test   al,0x1
  40182d:	0f 85 93 00 00 00    	jne    4018c6 <__setargv+0x166>
  401833:	83 7d d0 27          	cmp    DWORD PTR [ebp-0x30],0x27
  401837:	0f 84 89 00 00 00    	je     4018c6 <__setargv+0x166>
  40183d:	83 c6 01             	add    esi,0x1
  401840:	31 c0                	xor    eax,eax
  401842:	89 5d d4             	mov    DWORD PTR [ebp-0x2c],ebx
  401845:	0f b6 5e ff          	movzx  ebx,BYTE PTR [esi-0x1]
  401849:	31 4d d0             	xor    DWORD PTR [ebp-0x30],ecx
  40184c:	c7 45 cc 01 00 00 00 	mov    DWORD PTR [ebp-0x34],0x1
  401853:	0f be cb             	movsx  ecx,bl
  401856:	85 c9                	test   ecx,ecx
  401858:	75 8b                	jne    4017e5 <__setargv+0x85>
  40185a:	8d b6 00 00 00 00    	lea    esi,[esi+0x0]
  401860:	85 c0                	test   eax,eax
  401862:	8b 55 d4             	mov    edx,DWORD PTR [ebp-0x2c]
  401865:	0f 84 f4 01 00 00    	je     401a5f <__setargv+0x2ff>
  40186b:	01 d0                	add    eax,edx
  40186d:	8d 76 00             	lea    esi,[esi+0x0]
  401870:	83 c2 01             	add    edx,0x1
  401873:	39 c2                	cmp    edx,eax
  401875:	c6 42 ff 5c          	mov    BYTE PTR [edx-0x1],0x5c
  401879:	75 f5                	jne    401870 <__setargv+0x110>
  40187b:	8b 55 cc             	mov    edx,DWORD PTR [ebp-0x34]
  40187e:	85 d2                	test   edx,edx
  401880:	75 05                	jne    401887 <__setargv+0x127>
  401882:	39 45 c4             	cmp    DWORD PTR [ebp-0x3c],eax
  401885:	73 24                	jae    4018ab <__setargv+0x14b>
  401887:	c6 00 00             	mov    BYTE PTR [eax],0x0
  40188a:	8d 45 d8             	lea    eax,[ebp-0x28]
  40188d:	89 44 24 0c          	mov    DWORD PTR [esp+0xc],eax
  401891:	c7 44 24 08 00 00 00 	mov    DWORD PTR [esp+0x8],0x0
  401898:	00 
  401899:	8b 45 c8             	mov    eax,DWORD PTR [ebp-0x38]
  40189c:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
  4018a0:	8b 45 c4             	mov    eax,DWORD PTR [ebp-0x3c]
  4018a3:	89 04 24             	mov    DWORD PTR [esp],eax
  4018a6:	e8 f5 13 00 00       	call   402ca0 <___mingw_glob>
  4018ab:	8b 45 dc             	mov    eax,DWORD PTR [ebp-0x24]
  4018ae:	a3 04 d0 40 00       	mov    ds:0x40d004,eax
  4018b3:	8b 45 e0             	mov    eax,DWORD PTR [ebp-0x20]
  4018b6:	a3 00 d0 40 00       	mov    ds:0x40d000,eax
  4018bb:	8b 65 c0             	mov    esp,DWORD PTR [ebp-0x40]
  4018be:	8d 65 f4             	lea    esp,[ebp-0xc]
  4018c1:	5b                   	pop    ebx
  4018c2:	5e                   	pop    esi
  4018c3:	5f                   	pop    edi
  4018c4:	5d                   	pop    ebp
  4018c5:	c3                   	ret    
  4018c6:	8d 43 01             	lea    eax,[ebx+0x1]
  4018c9:	89 45 d4             	mov    DWORD PTR [ebp-0x2c],eax
  4018cc:	31 c0                	xor    eax,eax
  4018ce:	c6 03 22             	mov    BYTE PTR [ebx],0x22
  4018d1:	c7 45 cc 01 00 00 00 	mov    DWORD PTR [ebp-0x34],0x1
  4018d8:	e9 fa fe ff ff       	jmp    4017d7 <__setargv+0x77>
  4018dd:	8d 76 00             	lea    esi,[esi+0x0]
  4018e0:	80 fb 5c             	cmp    bl,0x5c
  4018e3:	0f 84 3f 01 00 00    	je     401a28 <__setargv+0x2c8>
  4018e9:	80 fb 7f             	cmp    bl,0x7f
  4018ec:	74 13                	je     401901 <__setargv+0x1a1>
  4018ee:	80 fb 5b             	cmp    bl,0x5b
  4018f1:	75 52                	jne    401945 <__setargv+0x1e5>
  4018f3:	f6 05 04 90 40 00 20 	test   BYTE PTR ds:0x409004,0x20
  4018fa:	bf 01 00 00 00       	mov    edi,0x1
  4018ff:	74 0a                	je     40190b <__setargv+0x1ab>
  401901:	8b 55 d0             	mov    edx,DWORD PTR [ebp-0x30]
  401904:	85 d2                	test   edx,edx
  401906:	0f 95 c2             	setne  dl
  401909:	89 d7                	mov    edi,edx
  40190b:	85 c0                	test   eax,eax
  40190d:	0f 84 34 01 00 00    	je     401a47 <__setargv+0x2e7>
  401913:	8b 55 d4             	mov    edx,DWORD PTR [ebp-0x2c]
  401916:	01 d0                	add    eax,edx
  401918:	83 c2 01             	add    edx,0x1
  40191b:	39 c2                	cmp    edx,eax
  40191d:	c6 42 ff 5c          	mov    BYTE PTR [edx-0x1],0x5c
  401921:	75 f5                	jne    401918 <__setargv+0x1b8>
  401923:	89 fa                	mov    edx,edi
  401925:	84 d2                	test   dl,dl
  401927:	0f 85 a3 00 00 00    	jne    4019d0 <__setargv+0x270>
  40192d:	83 f9 7f             	cmp    ecx,0x7f
  401930:	0f 84 9a 00 00 00    	je     4019d0 <__setargv+0x270>
  401936:	8d 48 01             	lea    ecx,[eax+0x1]
  401939:	88 18                	mov    BYTE PTR [eax],bl
  40193b:	31 c0                	xor    eax,eax
  40193d:	89 4d d4             	mov    DWORD PTR [ebp-0x2c],ecx
  401940:	e9 92 fe ff ff       	jmp    4017d7 <__setargv+0x77>
  401945:	8b 7d d4             	mov    edi,DWORD PTR [ebp-0x2c]
  401948:	8b 55 d4             	mov    edx,DWORD PTR [ebp-0x2c]
  40194b:	01 c7                	add    edi,eax
  40194d:	85 c0                	test   eax,eax
  40194f:	0f 84 fa 00 00 00    	je     401a4f <__setargv+0x2ef>
  401955:	83 c2 01             	add    edx,0x1
  401958:	39 fa                	cmp    edx,edi
  40195a:	c6 42 ff 5c          	mov    BYTE PTR [edx-0x1],0x5c
  40195e:	75 f5                	jne    401955 <__setargv+0x1f5>
  401960:	8b 45 d0             	mov    eax,DWORD PTR [ebp-0x30]
  401963:	85 c0                	test   eax,eax
  401965:	75 59                	jne    4019c0 <__setargv+0x260>
  401967:	89 0c 24             	mov    DWORD PTR [esp],ecx
  40196a:	e8 49 67 00 00       	call   4080b8 <_isspace>
  40196f:	85 c0                	test   eax,eax
  401971:	74 4d                	je     4019c0 <__setargv+0x260>
  401973:	8b 4d cc             	mov    ecx,DWORD PTR [ebp-0x34]
  401976:	85 c9                	test   ecx,ecx
  401978:	75 09                	jne    401983 <__setargv+0x223>
  40197a:	39 7d c4             	cmp    DWORD PTR [ebp-0x3c],edi
  40197d:	0f 83 ba 00 00 00    	jae    401a3d <__setargv+0x2dd>
  401983:	8d 45 d8             	lea    eax,[ebp-0x28]
  401986:	c6 07 00             	mov    BYTE PTR [edi],0x0
  401989:	89 44 24 0c          	mov    DWORD PTR [esp+0xc],eax
  40198d:	c7 44 24 08 00 00 00 	mov    DWORD PTR [esp+0x8],0x0
  401994:	00 
  401995:	8b 45 c8             	mov    eax,DWORD PTR [ebp-0x38]
  401998:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
  40199c:	8b 7d c4             	mov    edi,DWORD PTR [ebp-0x3c]
  40199f:	89 3c 24             	mov    DWORD PTR [esp],edi
  4019a2:	e8 f9 12 00 00       	call   402ca0 <___mingw_glob>
  4019a7:	31 c0                	xor    eax,eax
  4019a9:	83 4d c8 01          	or     DWORD PTR [ebp-0x38],0x1
  4019ad:	89 7d d4             	mov    DWORD PTR [ebp-0x2c],edi
  4019b0:	c7 45 cc 00 00 00 00 	mov    DWORD PTR [ebp-0x34],0x0
  4019b7:	e9 1b fe ff ff       	jmp    4017d7 <__setargv+0x77>
  4019bc:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  4019c0:	8d 47 01             	lea    eax,[edi+0x1]
  4019c3:	89 45 d4             	mov    DWORD PTR [ebp-0x2c],eax
  4019c6:	31 c0                	xor    eax,eax
  4019c8:	88 1f                	mov    BYTE PTR [edi],bl
  4019ca:	e9 08 fe ff ff       	jmp    4017d7 <__setargv+0x77>
  4019cf:	90                   	nop
  4019d0:	c6 00 7f             	mov    BYTE PTR [eax],0x7f
  4019d3:	83 c0 01             	add    eax,0x1
  4019d6:	e9 5b ff ff ff       	jmp    401936 <__setargv+0x1d6>
  4019db:	90                   	nop
  4019dc:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  4019e0:	f6 05 04 90 40 00 10 	test   BYTE PTR ds:0x409004,0x10
  4019e7:	0f 84 58 ff ff ff    	je     401945 <__setargv+0x1e5>
  4019ed:	89 c3                	mov    ebx,eax
  4019ef:	d1 fb                	sar    ebx,1
  4019f1:	74 73                	je     401a66 <__setargv+0x306>
  4019f3:	8b 55 d4             	mov    edx,DWORD PTR [ebp-0x2c]
  4019f6:	01 d3                	add    ebx,edx
  4019f8:	83 c2 01             	add    edx,0x1
  4019fb:	39 da                	cmp    edx,ebx
  4019fd:	c6 42 ff 5c          	mov    BYTE PTR [edx-0x1],0x5c
  401a01:	75 f5                	jne    4019f8 <__setargv+0x298>
  401a03:	a8 01                	test   al,0x1
  401a05:	75 0a                	jne    401a11 <__setargv+0x2b1>
  401a07:	83 7d d0 22          	cmp    DWORD PTR [ebp-0x30],0x22
  401a0b:	0f 85 2c fe ff ff    	jne    40183d <__setargv+0xdd>
  401a11:	8d 43 01             	lea    eax,[ebx+0x1]
  401a14:	89 45 d4             	mov    DWORD PTR [ebp-0x2c],eax
  401a17:	31 c0                	xor    eax,eax
  401a19:	c6 03 27             	mov    BYTE PTR [ebx],0x27
  401a1c:	c7 45 cc 01 00 00 00 	mov    DWORD PTR [ebp-0x34],0x1
  401a23:	e9 af fd ff ff       	jmp    4017d7 <__setargv+0x77>
  401a28:	83 c0 01             	add    eax,0x1
  401a2b:	e9 a7 fd ff ff       	jmp    4017d7 <__setargv+0x77>
  401a30:	e8 2b f8 ff ff       	call   401260 <__mingw32_init_mainargs>
  401a35:	8d 65 f4             	lea    esp,[ebp-0xc]
  401a38:	5b                   	pop    ebx
  401a39:	5e                   	pop    esi
  401a3a:	5f                   	pop    edi
  401a3b:	5d                   	pop    ebp
  401a3c:	c3                   	ret    
  401a3d:	89 7d d4             	mov    DWORD PTR [ebp-0x2c],edi
  401a40:	31 c0                	xor    eax,eax
  401a42:	e9 90 fd ff ff       	jmp    4017d7 <__setargv+0x77>
  401a47:	8b 45 d4             	mov    eax,DWORD PTR [ebp-0x2c]
  401a4a:	e9 d4 fe ff ff       	jmp    401923 <__setargv+0x1c3>
  401a4f:	8b 7d d4             	mov    edi,DWORD PTR [ebp-0x2c]
  401a52:	e9 09 ff ff ff       	jmp    401960 <__setargv+0x200>
  401a57:	8b 5d d4             	mov    ebx,DWORD PTR [ebp-0x2c]
  401a5a:	e9 cc fd ff ff       	jmp    40182b <__setargv+0xcb>
  401a5f:	89 d0                	mov    eax,edx
  401a61:	e9 15 fe ff ff       	jmp    40187b <__setargv+0x11b>
  401a66:	8b 5d d4             	mov    ebx,DWORD PTR [ebp-0x2c]
  401a69:	eb 98                	jmp    401a03 <__setargv+0x2a3>
  401a6b:	90                   	nop
  401a6c:	90                   	nop
  401a6d:	90                   	nop
  401a6e:	90                   	nop
  401a6f:	90                   	nop

00401a70 <___report_error>:
  401a70:	56                   	push   esi
  401a71:	53                   	push   ebx
  401a72:	83 ec 14             	sub    esp,0x14
  401a75:	a1 cc e1 40 00       	mov    eax,ds:0x40e1cc
  401a7a:	c7 44 24 08 17 00 00 	mov    DWORD PTR [esp+0x8],0x17
  401a81:	00 
  401a82:	8d 74 24 24          	lea    esi,[esp+0x24]
  401a86:	c7 44 24 04 01 00 00 	mov    DWORD PTR [esp+0x4],0x1
  401a8d:	00 
  401a8e:	c7 04 24 84 a0 40 00 	mov    DWORD PTR [esp],0x40a084
  401a95:	8d 58 40             	lea    ebx,[eax+0x40]
  401a98:	89 5c 24 0c          	mov    DWORD PTR [esp+0xc],ebx
  401a9c:	e8 1f 66 00 00       	call   4080c0 <_fwrite>
  401aa1:	8b 44 24 20          	mov    eax,DWORD PTR [esp+0x20]
  401aa5:	89 74 24 08          	mov    DWORD PTR [esp+0x8],esi
  401aa9:	89 1c 24             	mov    DWORD PTR [esp],ebx
  401aac:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
  401ab0:	e8 13 66 00 00       	call   4080c8 <_vfprintf>
  401ab5:	e8 16 66 00 00       	call   4080d0 <_abort>
  401aba:	8d b6 00 00 00 00    	lea    esi,[esi+0x0]

00401ac0 <___write_memory.part.0>:
  401ac0:	55                   	push   ebp
  401ac1:	89 e5                	mov    ebp,esp
  401ac3:	57                   	push   edi
  401ac4:	89 cf                	mov    edi,ecx
  401ac6:	56                   	push   esi
  401ac7:	89 d6                	mov    esi,edx
  401ac9:	53                   	push   ebx
  401aca:	89 c3                	mov    ebx,eax
  401acc:	83 ec 4c             	sub    esp,0x4c
  401acf:	8d 45 cc             	lea    eax,[ebp-0x34]
  401ad2:	c7 44 24 08 1c 00 00 	mov    DWORD PTR [esp+0x8],0x1c
  401ad9:	00 
  401ada:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
  401ade:	89 1c 24             	mov    DWORD PTR [esp],ebx
  401ae1:	e8 aa 66 00 00       	call   408190 <_VirtualQuery@12>
  401ae6:	83 ec 0c             	sub    esp,0xc
  401ae9:	85 c0                	test   eax,eax
  401aeb:	0f 84 9a 00 00 00    	je     401b8b <___write_memory.part.0+0xcb>
  401af1:	8b 45 e0             	mov    eax,DWORD PTR [ebp-0x20]
  401af4:	83 f8 04             	cmp    eax,0x4
  401af7:	75 18                	jne    401b11 <___write_memory.part.0+0x51>
  401af9:	89 7c 24 08          	mov    DWORD PTR [esp+0x8],edi
  401afd:	89 74 24 04          	mov    DWORD PTR [esp+0x4],esi
  401b01:	89 1c 24             	mov    DWORD PTR [esp],ebx
  401b04:	e8 cf 65 00 00       	call   4080d8 <_memcpy>
  401b09:	8d 65 f4             	lea    esp,[ebp-0xc]
  401b0c:	5b                   	pop    ebx
  401b0d:	5e                   	pop    esi
  401b0e:	5f                   	pop    edi
  401b0f:	5d                   	pop    ebp
  401b10:	c3                   	ret    
  401b11:	83 f8 40             	cmp    eax,0x40
  401b14:	74 e3                	je     401af9 <___write_memory.part.0+0x39>
  401b16:	8b 45 d8             	mov    eax,DWORD PTR [ebp-0x28]
  401b19:	8d 55 c8             	lea    edx,[ebp-0x38]
  401b1c:	89 54 24 0c          	mov    DWORD PTR [esp+0xc],edx
  401b20:	c7 44 24 08 40 00 00 	mov    DWORD PTR [esp+0x8],0x40
  401b27:	00 
  401b28:	89 55 c4             	mov    DWORD PTR [ebp-0x3c],edx
  401b2b:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
  401b2f:	8b 45 cc             	mov    eax,DWORD PTR [ebp-0x34]
  401b32:	89 04 24             	mov    DWORD PTR [esp],eax
  401b35:	e8 5e 66 00 00       	call   408198 <_VirtualProtect@16>
  401b3a:	8b 4d e0             	mov    ecx,DWORD PTR [ebp-0x20]
  401b3d:	89 4d c0             	mov    DWORD PTR [ebp-0x40],ecx
  401b40:	83 ec 10             	sub    esp,0x10
  401b43:	89 7c 24 08          	mov    DWORD PTR [esp+0x8],edi
  401b47:	89 74 24 04          	mov    DWORD PTR [esp+0x4],esi
  401b4b:	89 1c 24             	mov    DWORD PTR [esp],ebx
  401b4e:	e8 85 65 00 00       	call   4080d8 <_memcpy>
  401b53:	8b 4d c0             	mov    ecx,DWORD PTR [ebp-0x40]
  401b56:	83 f9 04             	cmp    ecx,0x4
  401b59:	74 ae                	je     401b09 <___write_memory.part.0+0x49>
  401b5b:	83 f9 40             	cmp    ecx,0x40
  401b5e:	74 a9                	je     401b09 <___write_memory.part.0+0x49>
  401b60:	8b 45 c8             	mov    eax,DWORD PTR [ebp-0x38]
  401b63:	8b 55 c4             	mov    edx,DWORD PTR [ebp-0x3c]
  401b66:	89 44 24 08          	mov    DWORD PTR [esp+0x8],eax
  401b6a:	8b 45 d8             	mov    eax,DWORD PTR [ebp-0x28]
  401b6d:	89 54 24 0c          	mov    DWORD PTR [esp+0xc],edx
  401b71:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
  401b75:	8b 45 cc             	mov    eax,DWORD PTR [ebp-0x34]
  401b78:	89 04 24             	mov    DWORD PTR [esp],eax
  401b7b:	e8 18 66 00 00       	call   408198 <_VirtualProtect@16>
  401b80:	83 ec 10             	sub    esp,0x10
  401b83:	8d 65 f4             	lea    esp,[ebp-0xc]
  401b86:	5b                   	pop    ebx
  401b87:	5e                   	pop    esi
  401b88:	5f                   	pop    edi
  401b89:	5d                   	pop    ebp
  401b8a:	c3                   	ret    
  401b8b:	89 5c 24 08          	mov    DWORD PTR [esp+0x8],ebx
  401b8f:	c7 44 24 04 1c 00 00 	mov    DWORD PTR [esp+0x4],0x1c
  401b96:	00 
  401b97:	c7 04 24 9c a0 40 00 	mov    DWORD PTR [esp],0x40a09c
  401b9e:	e8 cd fe ff ff       	call   401a70 <___report_error>
  401ba3:	8d b6 00 00 00 00    	lea    esi,[esi+0x0]
  401ba9:	8d bc 27 00 00 00 00 	lea    edi,[edi+eiz*1+0x0]

00401bb0 <__pei386_runtime_relocator>:
  401bb0:	a1 38 d0 40 00       	mov    eax,ds:0x40d038
  401bb5:	85 c0                	test   eax,eax
  401bb7:	74 07                	je     401bc0 <__pei386_runtime_relocator+0x10>
  401bb9:	c3                   	ret    
  401bba:	8d b6 00 00 00 00    	lea    esi,[esi+0x0]
  401bc0:	b8 40 a7 40 00       	mov    eax,0x40a740
  401bc5:	2d 40 a7 40 00       	sub    eax,0x40a740
  401bca:	83 f8 07             	cmp    eax,0x7
  401bcd:	c7 05 38 d0 40 00 01 	mov    DWORD PTR ds:0x40d038,0x1
  401bd4:	00 00 00 
  401bd7:	7e e0                	jle    401bb9 <__pei386_runtime_relocator+0x9>
  401bd9:	57                   	push   edi
  401bda:	56                   	push   esi
  401bdb:	53                   	push   ebx
  401bdc:	83 ec 20             	sub    esp,0x20
  401bdf:	83 f8 0b             	cmp    eax,0xb
  401be2:	0f 8e de 00 00 00    	jle    401cc6 <__pei386_runtime_relocator+0x116>
  401be8:	8b 35 40 a7 40 00    	mov    esi,DWORD PTR ds:0x40a740
  401bee:	85 f6                	test   esi,esi
  401bf0:	0f 85 8a 00 00 00    	jne    401c80 <__pei386_runtime_relocator+0xd0>
  401bf6:	8b 1d 44 a7 40 00    	mov    ebx,DWORD PTR ds:0x40a744
  401bfc:	85 db                	test   ebx,ebx
  401bfe:	0f 85 7c 00 00 00    	jne    401c80 <__pei386_runtime_relocator+0xd0>
  401c04:	8b 0d 48 a7 40 00    	mov    ecx,DWORD PTR ds:0x40a748
  401c0a:	bb 4c a7 40 00       	mov    ebx,0x40a74c
  401c0f:	85 c9                	test   ecx,ecx
  401c11:	0f 84 b4 00 00 00    	je     401ccb <__pei386_runtime_relocator+0x11b>
  401c17:	bb 40 a7 40 00       	mov    ebx,0x40a740
  401c1c:	8b 43 08             	mov    eax,DWORD PTR [ebx+0x8]
  401c1f:	83 f8 01             	cmp    eax,0x1
  401c22:	0f 85 49 01 00 00    	jne    401d71 <__pei386_runtime_relocator+0x1c1>
  401c28:	83 c3 0c             	add    ebx,0xc
  401c2b:	81 fb 40 a7 40 00    	cmp    ebx,0x40a740
  401c31:	0f 83 88 00 00 00    	jae    401cbf <__pei386_runtime_relocator+0x10f>
  401c37:	0f b6 53 08          	movzx  edx,BYTE PTR [ebx+0x8]
  401c3b:	8b 73 04             	mov    esi,DWORD PTR [ebx+0x4]
  401c3e:	8b 0b                	mov    ecx,DWORD PTR [ebx]
  401c40:	83 fa 10             	cmp    edx,0x10
  401c43:	8d 86 00 00 40 00    	lea    eax,[esi+0x400000]
  401c49:	8b b9 00 00 40 00    	mov    edi,DWORD PTR [ecx+0x400000]
  401c4f:	0f 84 8b 00 00 00    	je     401ce0 <__pei386_runtime_relocator+0x130>
  401c55:	83 fa 20             	cmp    edx,0x20
  401c58:	0f 84 f2 00 00 00    	je     401d50 <__pei386_runtime_relocator+0x1a0>
  401c5e:	83 fa 08             	cmp    edx,0x8
  401c61:	0f 84 af 00 00 00    	je     401d16 <__pei386_runtime_relocator+0x166>
  401c67:	89 54 24 04          	mov    DWORD PTR [esp+0x4],edx
  401c6b:	c7 04 24 04 a1 40 00 	mov    DWORD PTR [esp],0x40a104
  401c72:	c7 44 24 1c 00 00 00 	mov    DWORD PTR [esp+0x1c],0x0
  401c79:	00 
  401c7a:	e8 f1 fd ff ff       	call   401a70 <___report_error>
  401c7f:	90                   	nop
  401c80:	bb 40 a7 40 00       	mov    ebx,0x40a740
  401c85:	81 fb 40 a7 40 00    	cmp    ebx,0x40a740
  401c8b:	73 32                	jae    401cbf <__pei386_runtime_relocator+0x10f>
  401c8d:	8d 76 00             	lea    esi,[esi+0x0]
  401c90:	8b 53 04             	mov    edx,DWORD PTR [ebx+0x4]
  401c93:	b9 04 00 00 00       	mov    ecx,0x4
  401c98:	83 c3 08             	add    ebx,0x8
  401c9b:	8d 82 00 00 40 00    	lea    eax,[edx+0x400000]
  401ca1:	8b 92 00 00 40 00    	mov    edx,DWORD PTR [edx+0x400000]
  401ca7:	03 53 f8             	add    edx,DWORD PTR [ebx-0x8]
  401caa:	89 54 24 1c          	mov    DWORD PTR [esp+0x1c],edx
  401cae:	8d 54 24 1c          	lea    edx,[esp+0x1c]
  401cb2:	e8 09 fe ff ff       	call   401ac0 <___write_memory.part.0>
  401cb7:	81 fb 40 a7 40 00    	cmp    ebx,0x40a740
  401cbd:	72 d1                	jb     401c90 <__pei386_runtime_relocator+0xe0>
  401cbf:	83 c4 20             	add    esp,0x20
  401cc2:	5b                   	pop    ebx
  401cc3:	5e                   	pop    esi
  401cc4:	5f                   	pop    edi
  401cc5:	c3                   	ret    
  401cc6:	bb 40 a7 40 00       	mov    ebx,0x40a740
  401ccb:	8b 13                	mov    edx,DWORD PTR [ebx]
  401ccd:	85 d2                	test   edx,edx
  401ccf:	75 b4                	jne    401c85 <__pei386_runtime_relocator+0xd5>
  401cd1:	8b 43 04             	mov    eax,DWORD PTR [ebx+0x4]
  401cd4:	85 c0                	test   eax,eax
  401cd6:	0f 84 40 ff ff ff    	je     401c1c <__pei386_runtime_relocator+0x6c>
  401cdc:	eb a7                	jmp    401c85 <__pei386_runtime_relocator+0xd5>
  401cde:	66 90                	xchg   ax,ax
  401ce0:	0f b7 b6 00 00 40 00 	movzx  esi,WORD PTR [esi+0x400000]
  401ce7:	66 85 f6             	test   si,si
  401cea:	0f b7 d6             	movzx  edx,si
  401ced:	79 06                	jns    401cf5 <__pei386_runtime_relocator+0x145>
  401cef:	81 ca 00 00 ff ff    	or     edx,0xffff0000
  401cf5:	29 ca                	sub    edx,ecx
  401cf7:	b9 02 00 00 00       	mov    ecx,0x2
  401cfc:	81 ea 00 00 40 00    	sub    edx,0x400000
  401d02:	01 fa                	add    edx,edi
  401d04:	89 54 24 1c          	mov    DWORD PTR [esp+0x1c],edx
  401d08:	8d 54 24 1c          	lea    edx,[esp+0x1c]
  401d0c:	e8 af fd ff ff       	call   401ac0 <___write_memory.part.0>
  401d11:	e9 12 ff ff ff       	jmp    401c28 <__pei386_runtime_relocator+0x78>
  401d16:	0f b6 10             	movzx  edx,BYTE PTR [eax]
  401d19:	84 d2                	test   dl,dl
  401d1b:	0f b6 f2             	movzx  esi,dl
  401d1e:	79 06                	jns    401d26 <__pei386_runtime_relocator+0x176>
  401d20:	81 ce 00 ff ff ff    	or     esi,0xffffff00
  401d26:	81 ee 00 00 40 00    	sub    esi,0x400000
  401d2c:	89 f2                	mov    edx,esi
  401d2e:	29 ca                	sub    edx,ecx
  401d30:	b9 01 00 00 00       	mov    ecx,0x1
  401d35:	01 fa                	add    edx,edi
  401d37:	89 54 24 1c          	mov    DWORD PTR [esp+0x1c],edx
  401d3b:	8d 54 24 1c          	lea    edx,[esp+0x1c]
  401d3f:	e8 7c fd ff ff       	call   401ac0 <___write_memory.part.0>
  401d44:	e9 df fe ff ff       	jmp    401c28 <__pei386_runtime_relocator+0x78>
  401d49:	8d b4 26 00 00 00 00 	lea    esi,[esi+eiz*1+0x0]
  401d50:	81 c1 00 00 40 00    	add    ecx,0x400000
  401d56:	29 cf                	sub    edi,ecx
  401d58:	b9 04 00 00 00       	mov    ecx,0x4
  401d5d:	03 38                	add    edi,DWORD PTR [eax]
  401d5f:	8d 54 24 1c          	lea    edx,[esp+0x1c]
  401d63:	89 7c 24 1c          	mov    DWORD PTR [esp+0x1c],edi
  401d67:	e8 54 fd ff ff       	call   401ac0 <___write_memory.part.0>
  401d6c:	e9 b7 fe ff ff       	jmp    401c28 <__pei386_runtime_relocator+0x78>
  401d71:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
  401d75:	c7 04 24 d0 a0 40 00 	mov    DWORD PTR [esp],0x40a0d0
  401d7c:	e8 ef fc ff ff       	call   401a70 <___report_error>
  401d81:	90                   	nop
  401d82:	90                   	nop
  401d83:	90                   	nop
  401d84:	90                   	nop
  401d85:	90                   	nop
  401d86:	90                   	nop
  401d87:	90                   	nop
  401d88:	90                   	nop
  401d89:	90                   	nop
  401d8a:	90                   	nop
  401d8b:	90                   	nop
  401d8c:	90                   	nop
  401d8d:	90                   	nop
  401d8e:	90                   	nop
  401d8f:	90                   	nop

00401d90 <___do_global_dtors>:
  401d90:	a1 08 90 40 00       	mov    eax,ds:0x409008
  401d95:	8b 00                	mov    eax,DWORD PTR [eax]
  401d97:	85 c0                	test   eax,eax
  401d99:	74 1f                	je     401dba <___do_global_dtors+0x2a>
  401d9b:	83 ec 0c             	sub    esp,0xc
  401d9e:	66 90                	xchg   ax,ax
  401da0:	ff d0                	call   eax
  401da2:	a1 08 90 40 00       	mov    eax,ds:0x409008
  401da7:	8d 50 04             	lea    edx,[eax+0x4]
  401daa:	8b 40 04             	mov    eax,DWORD PTR [eax+0x4]
  401dad:	89 15 08 90 40 00    	mov    DWORD PTR ds:0x409008,edx
  401db3:	85 c0                	test   eax,eax
  401db5:	75 e9                	jne    401da0 <___do_global_dtors+0x10>
  401db7:	83 c4 0c             	add    esp,0xc
  401dba:	f3 c3                	repz ret 
  401dbc:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]

00401dc0 <___do_global_ctors>:
  401dc0:	53                   	push   ebx
  401dc1:	83 ec 18             	sub    esp,0x18
  401dc4:	8b 1d 20 85 40 00    	mov    ebx,DWORD PTR ds:0x408520
  401dca:	83 fb ff             	cmp    ebx,0xffffffff
  401dcd:	74 24                	je     401df3 <___do_global_ctors+0x33>
  401dcf:	85 db                	test   ebx,ebx
  401dd1:	74 0f                	je     401de2 <___do_global_ctors+0x22>
  401dd3:	ff 14 9d 20 85 40 00 	call   DWORD PTR [ebx*4+0x408520]
  401dda:	83 eb 01             	sub    ebx,0x1
  401ddd:	8d 76 00             	lea    esi,[esi+0x0]
  401de0:	75 f1                	jne    401dd3 <___do_global_ctors+0x13>
  401de2:	c7 04 24 90 1d 40 00 	mov    DWORD PTR [esp],0x401d90
  401de9:	e8 f2 f4 ff ff       	call   4012e0 <_atexit>
  401dee:	83 c4 18             	add    esp,0x18
  401df1:	5b                   	pop    ebx
  401df2:	c3                   	ret    
  401df3:	31 db                	xor    ebx,ebx
  401df5:	eb 02                	jmp    401df9 <___do_global_ctors+0x39>
  401df7:	89 c3                	mov    ebx,eax
  401df9:	8d 43 01             	lea    eax,[ebx+0x1]
  401dfc:	8b 14 85 20 85 40 00 	mov    edx,DWORD PTR [eax*4+0x408520]
  401e03:	85 d2                	test   edx,edx
  401e05:	75 f0                	jne    401df7 <___do_global_ctors+0x37>
  401e07:	eb c6                	jmp    401dcf <___do_global_ctors+0xf>
  401e09:	8d b4 26 00 00 00 00 	lea    esi,[esi+eiz*1+0x0]

00401e10 <___main>:
  401e10:	8b 0d 3c d0 40 00    	mov    ecx,DWORD PTR ds:0x40d03c
  401e16:	85 c9                	test   ecx,ecx
  401e18:	74 06                	je     401e20 <___main+0x10>
  401e1a:	f3 c3                	repz ret 
  401e1c:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  401e20:	c7 05 3c d0 40 00 01 	mov    DWORD PTR ds:0x40d03c,0x1
  401e27:	00 00 00 
  401e2a:	eb 94                	jmp    401dc0 <___do_global_ctors>
  401e2c:	90                   	nop
  401e2d:	90                   	nop
  401e2e:	90                   	nop
  401e2f:	90                   	nop

00401e30 <___mingwthr_run_key_dtors.part.0>:
  401e30:	55                   	push   ebp
  401e31:	89 e5                	mov    ebp,esp
  401e33:	56                   	push   esi
  401e34:	53                   	push   ebx
  401e35:	83 ec 10             	sub    esp,0x10
  401e38:	c7 04 24 4c d0 40 00 	mov    DWORD PTR [esp],0x40d04c
  401e3f:	e8 5c 63 00 00       	call   4081a0 <_EnterCriticalSection@4>
  401e44:	8b 1d 44 d0 40 00    	mov    ebx,DWORD PTR ds:0x40d044
  401e4a:	83 ec 04             	sub    esp,0x4
  401e4d:	85 db                	test   ebx,ebx
  401e4f:	74 2b                	je     401e7c <___mingwthr_run_key_dtors.part.0+0x4c>
  401e51:	8b 03                	mov    eax,DWORD PTR [ebx]
  401e53:	89 04 24             	mov    DWORD PTR [esp],eax
  401e56:	e8 4d 63 00 00       	call   4081a8 <_TlsGetValue@4>
  401e5b:	83 ec 04             	sub    esp,0x4
  401e5e:	89 c6                	mov    esi,eax
  401e60:	e8 4b 63 00 00       	call   4081b0 <_GetLastError@0>
  401e65:	85 c0                	test   eax,eax
  401e67:	75 0c                	jne    401e75 <___mingwthr_run_key_dtors.part.0+0x45>
  401e69:	85 f6                	test   esi,esi
  401e6b:	74 08                	je     401e75 <___mingwthr_run_key_dtors.part.0+0x45>
  401e6d:	8b 43 04             	mov    eax,DWORD PTR [ebx+0x4]
  401e70:	89 34 24             	mov    DWORD PTR [esp],esi
  401e73:	ff d0                	call   eax
  401e75:	8b 5b 08             	mov    ebx,DWORD PTR [ebx+0x8]
  401e78:	85 db                	test   ebx,ebx
  401e7a:	75 d5                	jne    401e51 <___mingwthr_run_key_dtors.part.0+0x21>
  401e7c:	c7 04 24 4c d0 40 00 	mov    DWORD PTR [esp],0x40d04c
  401e83:	e8 30 63 00 00       	call   4081b8 <_LeaveCriticalSection@4>
  401e88:	83 ec 04             	sub    esp,0x4
  401e8b:	8d 65 f8             	lea    esp,[ebp-0x8]
  401e8e:	5b                   	pop    ebx
  401e8f:	5e                   	pop    esi
  401e90:	5d                   	pop    ebp
  401e91:	c3                   	ret    
  401e92:	8d b4 26 00 00 00 00 	lea    esi,[esi+eiz*1+0x0]
  401e99:	8d bc 27 00 00 00 00 	lea    edi,[edi+eiz*1+0x0]

00401ea0 <____w64_mingwthr_add_key_dtor>:
  401ea0:	55                   	push   ebp
  401ea1:	89 e5                	mov    ebp,esp
  401ea3:	56                   	push   esi
  401ea4:	31 f6                	xor    esi,esi
  401ea6:	53                   	push   ebx
  401ea7:	83 ec 10             	sub    esp,0x10
  401eaa:	a1 48 d0 40 00       	mov    eax,ds:0x40d048
  401eaf:	85 c0                	test   eax,eax
  401eb1:	75 0d                	jne    401ec0 <____w64_mingwthr_add_key_dtor+0x20>
  401eb3:	8d 65 f8             	lea    esp,[ebp-0x8]
  401eb6:	89 f0                	mov    eax,esi
  401eb8:	5b                   	pop    ebx
  401eb9:	5e                   	pop    esi
  401eba:	5d                   	pop    ebp
  401ebb:	c3                   	ret    
  401ebc:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  401ec0:	c7 44 24 04 0c 00 00 	mov    DWORD PTR [esp+0x4],0xc
  401ec7:	00 
  401ec8:	c7 04 24 01 00 00 00 	mov    DWORD PTR [esp],0x1
  401ecf:	e8 0c 62 00 00       	call   4080e0 <_calloc>
  401ed4:	85 c0                	test   eax,eax
  401ed6:	89 c3                	mov    ebx,eax
  401ed8:	74 40                	je     401f1a <____w64_mingwthr_add_key_dtor+0x7a>
  401eda:	8b 45 08             	mov    eax,DWORD PTR [ebp+0x8]
  401edd:	c7 04 24 4c d0 40 00 	mov    DWORD PTR [esp],0x40d04c
  401ee4:	89 03                	mov    DWORD PTR [ebx],eax
  401ee6:	8b 45 0c             	mov    eax,DWORD PTR [ebp+0xc]
  401ee9:	89 43 04             	mov    DWORD PTR [ebx+0x4],eax
  401eec:	e8 af 62 00 00       	call   4081a0 <_EnterCriticalSection@4>
  401ef1:	a1 44 d0 40 00       	mov    eax,ds:0x40d044
  401ef6:	89 1d 44 d0 40 00    	mov    DWORD PTR ds:0x40d044,ebx
  401efc:	89 43 08             	mov    DWORD PTR [ebx+0x8],eax
  401eff:	83 ec 04             	sub    esp,0x4
  401f02:	c7 04 24 4c d0 40 00 	mov    DWORD PTR [esp],0x40d04c
  401f09:	e8 aa 62 00 00       	call   4081b8 <_LeaveCriticalSection@4>
  401f0e:	89 f0                	mov    eax,esi
  401f10:	83 ec 04             	sub    esp,0x4
  401f13:	8d 65 f8             	lea    esp,[ebp-0x8]
  401f16:	5b                   	pop    ebx
  401f17:	5e                   	pop    esi
  401f18:	5d                   	pop    ebp
  401f19:	c3                   	ret    
  401f1a:	be ff ff ff ff       	mov    esi,0xffffffff
  401f1f:	eb 92                	jmp    401eb3 <____w64_mingwthr_add_key_dtor+0x13>
  401f21:	eb 0d                	jmp    401f30 <____w64_mingwthr_remove_key_dtor>
  401f23:	90                   	nop
  401f24:	90                   	nop
  401f25:	90                   	nop
  401f26:	90                   	nop
  401f27:	90                   	nop
  401f28:	90                   	nop
  401f29:	90                   	nop
  401f2a:	90                   	nop
  401f2b:	90                   	nop
  401f2c:	90                   	nop
  401f2d:	90                   	nop
  401f2e:	90                   	nop
  401f2f:	90                   	nop

00401f30 <____w64_mingwthr_remove_key_dtor>:
  401f30:	55                   	push   ebp
  401f31:	89 e5                	mov    ebp,esp
  401f33:	53                   	push   ebx
  401f34:	83 ec 14             	sub    esp,0x14
  401f37:	a1 48 d0 40 00       	mov    eax,ds:0x40d048
  401f3c:	8b 5d 08             	mov    ebx,DWORD PTR [ebp+0x8]
  401f3f:	85 c0                	test   eax,eax
  401f41:	75 0d                	jne    401f50 <____w64_mingwthr_remove_key_dtor+0x20>
  401f43:	31 c0                	xor    eax,eax
  401f45:	8b 5d fc             	mov    ebx,DWORD PTR [ebp-0x4]
  401f48:	c9                   	leave  
  401f49:	c3                   	ret    
  401f4a:	8d b6 00 00 00 00    	lea    esi,[esi+0x0]
  401f50:	c7 04 24 4c d0 40 00 	mov    DWORD PTR [esp],0x40d04c
  401f57:	e8 44 62 00 00       	call   4081a0 <_EnterCriticalSection@4>
  401f5c:	8b 15 44 d0 40 00    	mov    edx,DWORD PTR ds:0x40d044
  401f62:	83 ec 04             	sub    esp,0x4
  401f65:	85 d2                	test   edx,edx
  401f67:	74 17                	je     401f80 <____w64_mingwthr_remove_key_dtor+0x50>
  401f69:	8b 02                	mov    eax,DWORD PTR [edx]
  401f6b:	39 d8                	cmp    eax,ebx
  401f6d:	75 0a                	jne    401f79 <____w64_mingwthr_remove_key_dtor+0x49>
  401f6f:	eb 44                	jmp    401fb5 <____w64_mingwthr_remove_key_dtor+0x85>
  401f71:	8b 08                	mov    ecx,DWORD PTR [eax]
  401f73:	39 d9                	cmp    ecx,ebx
  401f75:	74 1f                	je     401f96 <____w64_mingwthr_remove_key_dtor+0x66>
  401f77:	89 c2                	mov    edx,eax
  401f79:	8b 42 08             	mov    eax,DWORD PTR [edx+0x8]
  401f7c:	85 c0                	test   eax,eax
  401f7e:	75 f1                	jne    401f71 <____w64_mingwthr_remove_key_dtor+0x41>
  401f80:	c7 04 24 4c d0 40 00 	mov    DWORD PTR [esp],0x40d04c
  401f87:	e8 2c 62 00 00       	call   4081b8 <_LeaveCriticalSection@4>
  401f8c:	83 ec 04             	sub    esp,0x4
  401f8f:	31 c0                	xor    eax,eax
  401f91:	8b 5d fc             	mov    ebx,DWORD PTR [ebp-0x4]
  401f94:	c9                   	leave  
  401f95:	c3                   	ret    
  401f96:	8b 48 08             	mov    ecx,DWORD PTR [eax+0x8]
  401f99:	89 4a 08             	mov    DWORD PTR [edx+0x8],ecx
  401f9c:	89 04 24             	mov    DWORD PTR [esp],eax
  401f9f:	e8 44 61 00 00       	call   4080e8 <_free>
  401fa4:	c7 04 24 4c d0 40 00 	mov    DWORD PTR [esp],0x40d04c
  401fab:	e8 08 62 00 00       	call   4081b8 <_LeaveCriticalSection@4>
  401fb0:	83 ec 04             	sub    esp,0x4
  401fb3:	eb da                	jmp    401f8f <____w64_mingwthr_remove_key_dtor+0x5f>
  401fb5:	8b 42 08             	mov    eax,DWORD PTR [edx+0x8]
  401fb8:	a3 44 d0 40 00       	mov    ds:0x40d044,eax
  401fbd:	89 d0                	mov    eax,edx
  401fbf:	eb db                	jmp    401f9c <____w64_mingwthr_remove_key_dtor+0x6c>
  401fc1:	eb 0d                	jmp    401fd0 <___mingw_TLScallback>
  401fc3:	90                   	nop
  401fc4:	90                   	nop
  401fc5:	90                   	nop
  401fc6:	90                   	nop
  401fc7:	90                   	nop
  401fc8:	90                   	nop
  401fc9:	90                   	nop
  401fca:	90                   	nop
  401fcb:	90                   	nop
  401fcc:	90                   	nop
  401fcd:	90                   	nop
  401fce:	90                   	nop
  401fcf:	90                   	nop

00401fd0 <___mingw_TLScallback>:
  401fd0:	55                   	push   ebp
  401fd1:	89 e5                	mov    ebp,esp
  401fd3:	83 ec 18             	sub    esp,0x18
  401fd6:	8b 45 0c             	mov    eax,DWORD PTR [ebp+0xc]
  401fd9:	83 f8 01             	cmp    eax,0x1
  401fdc:	74 45                	je     402023 <___mingw_TLScallback+0x53>
  401fde:	72 15                	jb     401ff5 <___mingw_TLScallback+0x25>
  401fe0:	83 f8 03             	cmp    eax,0x3
  401fe3:	75 09                	jne    401fee <___mingw_TLScallback+0x1e>
  401fe5:	a1 48 d0 40 00       	mov    eax,ds:0x40d048
  401fea:	85 c0                	test   eax,eax
  401fec:	75 63                	jne    402051 <___mingw_TLScallback+0x81>
  401fee:	b8 01 00 00 00       	mov    eax,0x1
  401ff3:	c9                   	leave  
  401ff4:	c3                   	ret    
  401ff5:	a1 48 d0 40 00       	mov    eax,ds:0x40d048
  401ffa:	85 c0                	test   eax,eax
  401ffc:	75 5a                	jne    402058 <___mingw_TLScallback+0x88>
  401ffe:	a1 48 d0 40 00       	mov    eax,ds:0x40d048
  402003:	83 f8 01             	cmp    eax,0x1
  402006:	75 e6                	jne    401fee <___mingw_TLScallback+0x1e>
  402008:	c7 04 24 4c d0 40 00 	mov    DWORD PTR [esp],0x40d04c
  40200f:	c7 05 48 d0 40 00 00 	mov    DWORD PTR ds:0x40d048,0x0
  402016:	00 00 00 
  402019:	e8 a2 61 00 00       	call   4081c0 <_DeleteCriticalSection@4>
  40201e:	83 ec 04             	sub    esp,0x4
  402021:	eb cb                	jmp    401fee <___mingw_TLScallback+0x1e>
  402023:	a1 48 d0 40 00       	mov    eax,ds:0x40d048
  402028:	85 c0                	test   eax,eax
  40202a:	74 14                	je     402040 <___mingw_TLScallback+0x70>
  40202c:	c7 05 48 d0 40 00 01 	mov    DWORD PTR ds:0x40d048,0x1
  402033:	00 00 00 
  402036:	b8 01 00 00 00       	mov    eax,0x1
  40203b:	c9                   	leave  
  40203c:	c3                   	ret    
  40203d:	8d 76 00             	lea    esi,[esi+0x0]
  402040:	c7 04 24 4c d0 40 00 	mov    DWORD PTR [esp],0x40d04c
  402047:	e8 7c 61 00 00       	call   4081c8 <_InitializeCriticalSection@4>
  40204c:	83 ec 04             	sub    esp,0x4
  40204f:	eb db                	jmp    40202c <___mingw_TLScallback+0x5c>
  402051:	e8 da fd ff ff       	call   401e30 <___mingwthr_run_key_dtors.part.0>
  402056:	eb 96                	jmp    401fee <___mingw_TLScallback+0x1e>
  402058:	90                   	nop
  402059:	8d b4 26 00 00 00 00 	lea    esi,[esi+eiz*1+0x0]
  402060:	e8 cb fd ff ff       	call   401e30 <___mingwthr_run_key_dtors.part.0>
  402065:	eb 97                	jmp    401ffe <___mingw_TLScallback+0x2e>
  402067:	90                   	nop
  402068:	90                   	nop
  402069:	90                   	nop
  40206a:	90                   	nop
  40206b:	90                   	nop
  40206c:	90                   	nop
  40206d:	90                   	nop
  40206e:	90                   	nop
  40206f:	90                   	nop

00402070 <___chkstk_ms>:
  402070:	51                   	push   ecx
  402071:	50                   	push   eax
  402072:	3d 00 10 00 00       	cmp    eax,0x1000
  402077:	8d 4c 24 0c          	lea    ecx,[esp+0xc]
  40207b:	72 15                	jb     402092 <___chkstk_ms+0x22>
  40207d:	81 e9 00 10 00 00    	sub    ecx,0x1000
  402083:	83 09 00             	or     DWORD PTR [ecx],0x0
  402086:	2d 00 10 00 00       	sub    eax,0x1000
  40208b:	3d 00 10 00 00       	cmp    eax,0x1000
  402090:	77 eb                	ja     40207d <___chkstk_ms+0xd>
  402092:	29 c1                	sub    ecx,eax
  402094:	83 09 00             	or     DWORD PTR [ecx],0x0
  402097:	58                   	pop    eax
  402098:	59                   	pop    ecx
  402099:	c3                   	ret    
  40209a:	90                   	nop
  40209b:	90                   	nop

0040209c <.text>:
  40209c:	66 90                	xchg   ax,ax
  40209e:	66 90                	xchg   ax,ax

004020a0 <_is_glob_pattern>:
  4020a0:	57                   	push   edi
  4020a1:	85 c0                	test   eax,eax
  4020a3:	56                   	push   esi
  4020a4:	53                   	push   ebx
  4020a5:	89 c3                	mov    ebx,eax
  4020a7:	74 44                	je     4020ed <_is_glob_pattern+0x4d>
  4020a9:	0f be 0b             	movsx  ecx,BYTE PTR [ebx]
  4020ac:	89 d6                	mov    esi,edx
  4020ae:	31 c0                	xor    eax,eax
  4020b0:	83 e6 20             	and    esi,0x20
  4020b3:	8d 53 01             	lea    edx,[ebx+0x1]
  4020b6:	85 c9                	test   ecx,ecx
  4020b8:	74 33                	je     4020ed <_is_glob_pattern+0x4d>
  4020ba:	8d b6 00 00 00 00    	lea    esi,[esi+0x0]
  4020c0:	85 f6                	test   esi,esi
  4020c2:	89 f7                	mov    edi,esi
  4020c4:	75 05                	jne    4020cb <_is_glob_pattern+0x2b>
  4020c6:	83 f9 7f             	cmp    ecx,0x7f
  4020c9:	74 45                	je     402110 <_is_glob_pattern+0x70>
  4020cb:	85 c0                	test   eax,eax
  4020cd:	75 26                	jne    4020f5 <_is_glob_pattern+0x55>
  4020cf:	83 f9 3f             	cmp    ecx,0x3f
  4020d2:	74 51                	je     402125 <_is_glob_pattern+0x85>
  4020d4:	83 f9 2a             	cmp    ecx,0x2a
  4020d7:	74 4c                	je     402125 <_is_glob_pattern+0x85>
  4020d9:	31 c0                	xor    eax,eax
  4020db:	83 f9 5b             	cmp    ecx,0x5b
  4020de:	0f 94 c0             	sete   al
  4020e1:	89 d3                	mov    ebx,edx
  4020e3:	0f be 0b             	movsx  ecx,BYTE PTR [ebx]
  4020e6:	8d 53 01             	lea    edx,[ebx+0x1]
  4020e9:	85 c9                	test   ecx,ecx
  4020eb:	75 d3                	jne    4020c0 <_is_glob_pattern+0x20>
  4020ed:	31 ff                	xor    edi,edi
  4020ef:	89 f8                	mov    eax,edi
  4020f1:	5b                   	pop    ebx
  4020f2:	5e                   	pop    esi
  4020f3:	5f                   	pop    edi
  4020f4:	c3                   	ret    
  4020f5:	83 f9 5d             	cmp    ecx,0x5d
  4020f8:	74 26                	je     402120 <_is_glob_pattern+0x80>
  4020fa:	83 f9 21             	cmp    ecx,0x21
  4020fd:	89 d3                	mov    ebx,edx
  4020ff:	0f 95 c1             	setne  cl
  402102:	0f b6 c9             	movzx  ecx,cl
  402105:	01 c8                	add    eax,ecx
  402107:	eb da                	jmp    4020e3 <_is_glob_pattern+0x43>
  402109:	8d b4 26 00 00 00 00 	lea    esi,[esi+eiz*1+0x0]
  402110:	80 7b 01 00          	cmp    BYTE PTR [ebx+0x1],0x0
  402114:	8d 53 02             	lea    edx,[ebx+0x2]
  402117:	75 b2                	jne    4020cb <_is_glob_pattern+0x2b>
  402119:	eb d4                	jmp    4020ef <_is_glob_pattern+0x4f>
  40211b:	90                   	nop
  40211c:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  402120:	83 f8 01             	cmp    eax,0x1
  402123:	7e d5                	jle    4020fa <_is_glob_pattern+0x5a>
  402125:	bf 01 00 00 00       	mov    edi,0x1
  40212a:	89 f8                	mov    eax,edi
  40212c:	5b                   	pop    ebx
  40212d:	5e                   	pop    esi
  40212e:	5f                   	pop    edi
  40212f:	c3                   	ret    

00402130 <_glob_in_set>:
  402130:	55                   	push   ebp
  402131:	57                   	push   edi
  402132:	56                   	push   esi
  402133:	53                   	push   ebx
  402134:	83 ec 04             	sub    esp,0x4
  402137:	0f b6 18             	movzx  ebx,BYTE PTR [eax]
  40213a:	89 0c 24             	mov    DWORD PTR [esp],ecx
  40213d:	0f be fb             	movsx  edi,bl
  402140:	83 ff 5d             	cmp    edi,0x5d
  402143:	0f 84 d7 00 00 00    	je     402220 <_glob_in_set+0xf0>
  402149:	83 ff 2d             	cmp    edi,0x2d
  40214c:	89 d9                	mov    ecx,ebx
  40214e:	75 2e                	jne    40217e <_glob_in_set+0x4e>
  402150:	e9 cb 00 00 00       	jmp    402220 <_glob_in_set+0xf0>
  402155:	85 db                	test   ebx,ebx
  402157:	0f 84 b3 00 00 00    	je     402210 <_glob_in_set+0xe0>
  40215d:	83 fb 5c             	cmp    ebx,0x5c
  402160:	0f 84 aa 00 00 00    	je     402210 <_glob_in_set+0xe0>
  402166:	83 fb 2f             	cmp    ebx,0x2f
  402169:	0f 84 a1 00 00 00    	je     402210 <_glob_in_set+0xe0>
  40216f:	89 df                	mov    edi,ebx
  402171:	0f b6 0e             	movzx  ecx,BYTE PTR [esi]
  402174:	89 f0                	mov    eax,esi
  402176:	39 d7                	cmp    edi,edx
  402178:	0f 84 ca 00 00 00    	je     402248 <_glob_in_set+0x118>
  40217e:	0f be d9             	movsx  ebx,cl
  402181:	83 fb 5d             	cmp    ebx,0x5d
  402184:	8d 70 01             	lea    esi,[eax+0x1]
  402187:	0f 84 83 00 00 00    	je     402210 <_glob_in_set+0xe0>
  40218d:	83 fb 2d             	cmp    ebx,0x2d
  402190:	75 c3                	jne    402155 <_glob_in_set+0x25>
  402192:	0f b6 58 01          	movzx  ebx,BYTE PTR [eax+0x1]
  402196:	80 fb 5d             	cmp    bl,0x5d
  402199:	0f 84 95 00 00 00    	je     402234 <_glob_in_set+0x104>
  40219f:	0f be eb             	movsx  ebp,bl
  4021a2:	85 ed                	test   ebp,ebp
  4021a4:	89 eb                	mov    ebx,ebp
  4021a6:	74 68                	je     402210 <_glob_in_set+0xe0>
  4021a8:	39 ef                	cmp    edi,ebp
  4021aa:	8d 70 02             	lea    esi,[eax+0x2]
  4021ad:	0f 8d 85 01 00 00    	jge    402338 <_glob_in_set+0x208>
  4021b3:	39 d7                	cmp    edi,edx
  4021b5:	8d 47 01             	lea    eax,[edi+0x1]
  4021b8:	75 14                	jne    4021ce <_glob_in_set+0x9e>
  4021ba:	e9 c1 00 00 00       	jmp    402280 <_glob_in_set+0x150>
  4021bf:	90                   	nop
  4021c0:	83 c0 01             	add    eax,0x1
  4021c3:	8d 78 ff             	lea    edi,[eax-0x1]
  4021c6:	39 fa                	cmp    edx,edi
  4021c8:	0f 84 b2 00 00 00    	je     402280 <_glob_in_set+0x150>
  4021ce:	39 c5                	cmp    ebp,eax
  4021d0:	7f ee                	jg     4021c0 <_glob_in_set+0x90>
  4021d2:	39 c5                	cmp    ebp,eax
  4021d4:	7d 87                	jge    40215d <_glob_in_set+0x2d>
  4021d6:	39 c2                	cmp    edx,eax
  4021d8:	74 15                	je     4021ef <_glob_in_set+0xbf>
  4021da:	83 c5 01             	add    ebp,0x1
  4021dd:	8d 76 00             	lea    esi,[esi+0x0]
  4021e0:	39 e8                	cmp    eax,ebp
  4021e2:	0f 84 75 ff ff ff    	je     40215d <_glob_in_set+0x2d>
  4021e8:	83 e8 01             	sub    eax,0x1
  4021eb:	39 c2                	cmp    edx,eax
  4021ed:	75 f1                	jne    4021e0 <_glob_in_set+0xb0>
  4021ef:	8b 0c 24             	mov    ecx,DWORD PTR [esp]
  4021f2:	83 e1 20             	and    ecx,0x20
  4021f5:	0f b6 06             	movzx  eax,BYTE PTR [esi]
  4021f8:	3c 5d                	cmp    al,0x5d
  4021fa:	0f 84 a3 00 00 00    	je     4022a3 <_glob_in_set+0x173>
  402200:	3c 7f                	cmp    al,0x7f
  402202:	0f 84 bd 00 00 00    	je     4022c5 <_glob_in_set+0x195>
  402208:	83 c6 01             	add    esi,0x1
  40220b:	84 c0                	test   al,al
  40220d:	75 e6                	jne    4021f5 <_glob_in_set+0xc5>
  40220f:	90                   	nop
  402210:	83 c4 04             	add    esp,0x4
  402213:	31 c0                	xor    eax,eax
  402215:	5b                   	pop    ebx
  402216:	5e                   	pop    esi
  402217:	5f                   	pop    edi
  402218:	5d                   	pop    ebp
  402219:	c3                   	ret    
  40221a:	8d b6 00 00 00 00    	lea    esi,[esi+0x0]
  402220:	39 d7                	cmp    edi,edx
  402222:	0f 84 b8 00 00 00    	je     4022e0 <_glob_in_set+0x1b0>
  402228:	0f b6 48 01          	movzx  ecx,BYTE PTR [eax+0x1]
  40222c:	83 c0 01             	add    eax,0x1
  40222f:	e9 4a ff ff ff       	jmp    40217e <_glob_in_set+0x4e>
  402234:	bf 2d 00 00 00       	mov    edi,0x2d
  402239:	89 f0                	mov    eax,esi
  40223b:	39 d7                	cmp    edi,edx
  40223d:	b9 5d 00 00 00       	mov    ecx,0x5d
  402242:	0f 85 36 ff ff ff    	jne    40217e <_glob_in_set+0x4e>
  402248:	8b 14 24             	mov    edx,DWORD PTR [esp]
  40224b:	83 e2 20             	and    edx,0x20
  40224e:	eb 0a                	jmp    40225a <_glob_in_set+0x12a>
  402250:	83 c0 01             	add    eax,0x1
  402253:	84 c9                	test   cl,cl
  402255:	74 b9                	je     402210 <_glob_in_set+0xe0>
  402257:	0f b6 08             	movzx  ecx,BYTE PTR [eax]
  40225a:	80 f9 5d             	cmp    cl,0x5d
  40225d:	0f 84 c2 00 00 00    	je     402325 <_glob_in_set+0x1f5>
  402263:	80 f9 7f             	cmp    cl,0x7f
  402266:	75 e8                	jne    402250 <_glob_in_set+0x120>
  402268:	85 d2                	test   edx,edx
  40226a:	0f 85 c0 00 00 00    	jne    402330 <_glob_in_set+0x200>
  402270:	0f b6 48 01          	movzx  ecx,BYTE PTR [eax+0x1]
  402274:	83 c0 01             	add    eax,0x1
  402277:	eb d7                	jmp    402250 <_glob_in_set+0x120>
  402279:	8d b4 26 00 00 00 00 	lea    esi,[esi+eiz*1+0x0]
  402280:	8b 0c 24             	mov    ecx,DWORD PTR [esp]
  402283:	83 e1 20             	and    ecx,0x20
  402286:	0f b6 06             	movzx  eax,BYTE PTR [esi]
  402289:	3c 5d                	cmp    al,0x5d
  40228b:	74 16                	je     4022a3 <_glob_in_set+0x173>
  40228d:	3c 7f                	cmp    al,0x7f
  40228f:	74 1f                	je     4022b0 <_glob_in_set+0x180>
  402291:	83 c6 01             	add    esi,0x1
  402294:	84 c0                	test   al,al
  402296:	0f 84 74 ff ff ff    	je     402210 <_glob_in_set+0xe0>
  40229c:	0f b6 06             	movzx  eax,BYTE PTR [esi]
  40229f:	3c 5d                	cmp    al,0x5d
  4022a1:	75 ea                	jne    40228d <_glob_in_set+0x15d>
  4022a3:	83 c4 04             	add    esp,0x4
  4022a6:	5b                   	pop    ebx
  4022a7:	8d 46 01             	lea    eax,[esi+0x1]
  4022aa:	5e                   	pop    esi
  4022ab:	5f                   	pop    edi
  4022ac:	5d                   	pop    ebp
  4022ad:	c3                   	ret    
  4022ae:	66 90                	xchg   ax,ax
  4022b0:	85 c9                	test   ecx,ecx
  4022b2:	75 0c                	jne    4022c0 <_glob_in_set+0x190>
  4022b4:	0f b6 46 01          	movzx  eax,BYTE PTR [esi+0x1]
  4022b8:	83 c6 01             	add    esi,0x1
  4022bb:	eb d4                	jmp    402291 <_glob_in_set+0x161>
  4022bd:	8d 76 00             	lea    esi,[esi+0x0]
  4022c0:	83 c6 01             	add    esi,0x1
  4022c3:	eb c1                	jmp    402286 <_glob_in_set+0x156>
  4022c5:	85 c9                	test   ecx,ecx
  4022c7:	75 0c                	jne    4022d5 <_glob_in_set+0x1a5>
  4022c9:	0f b6 46 01          	movzx  eax,BYTE PTR [esi+0x1]
  4022cd:	83 c6 01             	add    esi,0x1
  4022d0:	e9 33 ff ff ff       	jmp    402208 <_glob_in_set+0xd8>
  4022d5:	83 c6 01             	add    esi,0x1
  4022d8:	e9 18 ff ff ff       	jmp    4021f5 <_glob_in_set+0xc5>
  4022dd:	8d 76 00             	lea    esi,[esi+0x0]
  4022e0:	8b 0c 24             	mov    ecx,DWORD PTR [esp]
  4022e3:	83 c0 01             	add    eax,0x1
  4022e6:	83 e1 20             	and    ecx,0x20
  4022e9:	8d b4 26 00 00 00 00 	lea    esi,[esi+eiz*1+0x0]
  4022f0:	0f b6 10             	movzx  edx,BYTE PTR [eax]
  4022f3:	80 fa 5d             	cmp    dl,0x5d
  4022f6:	74 2d                	je     402325 <_glob_in_set+0x1f5>
  4022f8:	80 fa 7f             	cmp    dl,0x7f
  4022fb:	74 13                	je     402310 <_glob_in_set+0x1e0>
  4022fd:	83 c0 01             	add    eax,0x1
  402300:	84 d2                	test   dl,dl
  402302:	75 ec                	jne    4022f0 <_glob_in_set+0x1c0>
  402304:	e9 07 ff ff ff       	jmp    402210 <_glob_in_set+0xe0>
  402309:	8d b4 26 00 00 00 00 	lea    esi,[esi+eiz*1+0x0]
  402310:	85 c9                	test   ecx,ecx
  402312:	75 0c                	jne    402320 <_glob_in_set+0x1f0>
  402314:	0f b6 50 01          	movzx  edx,BYTE PTR [eax+0x1]
  402318:	83 c0 01             	add    eax,0x1
  40231b:	eb e0                	jmp    4022fd <_glob_in_set+0x1cd>
  40231d:	8d 76 00             	lea    esi,[esi+0x0]
  402320:	83 c0 01             	add    eax,0x1
  402323:	eb cb                	jmp    4022f0 <_glob_in_set+0x1c0>
  402325:	83 c4 04             	add    esp,0x4
  402328:	83 c0 01             	add    eax,0x1
  40232b:	5b                   	pop    ebx
  40232c:	5e                   	pop    esi
  40232d:	5f                   	pop    edi
  40232e:	5d                   	pop    ebp
  40232f:	c3                   	ret    
  402330:	83 c0 01             	add    eax,0x1
  402333:	e9 1f ff ff ff       	jmp    402257 <_glob_in_set+0x127>
  402338:	89 f8                	mov    eax,edi
  40233a:	e9 93 fe ff ff       	jmp    4021d2 <_glob_in_set+0xa2>
  40233f:	90                   	nop

00402340 <_glob_initialise>:
  402340:	55                   	push   ebp
  402341:	57                   	push   edi
  402342:	56                   	push   esi
  402343:	89 c6                	mov    esi,eax
  402345:	53                   	push   ebx
  402346:	83 ec 1c             	sub    esp,0x1c
  402349:	85 c0                	test   eax,eax
  40234b:	74 47                	je     402394 <_glob_initialise+0x54>
  40234d:	8b 40 0c             	mov    eax,DWORD PTR [eax+0xc]
  402350:	8d 78 01             	lea    edi,[eax+0x1]
  402353:	8d 2c bd 00 00 00 00 	lea    ebp,[edi*4+0x0]
  40235a:	89 2c 24             	mov    DWORD PTR [esp],ebp
  40235d:	e8 8e 5d 00 00       	call   4080f0 <_malloc>
  402362:	89 c3                	mov    ebx,eax
  402364:	85 db                	test   ebx,ebx
  402366:	89 46 08             	mov    DWORD PTR [esi+0x8],eax
  402369:	b8 03 00 00 00       	mov    eax,0x3
  40236e:	74 26                	je     402396 <_glob_initialise+0x56>
  402370:	85 ff                	test   edi,edi
  402372:	89 fa                	mov    edx,edi
  402374:	c7 46 04 00 00 00 00 	mov    DWORD PTR [esi+0x4],0x0
  40237b:	7e 17                	jle    402394 <_glob_initialise+0x54>
  40237d:	8d 4d fc             	lea    ecx,[ebp-0x4]
  402380:	eb 03                	jmp    402385 <_glob_initialise+0x45>
  402382:	8b 5e 08             	mov    ebx,DWORD PTR [esi+0x8]
  402385:	c7 04 0b 00 00 00 00 	mov    DWORD PTR [ebx+ecx*1],0x0
  40238c:	83 e9 04             	sub    ecx,0x4
  40238f:	83 ea 01             	sub    edx,0x1
  402392:	75 ee                	jne    402382 <_glob_initialise+0x42>
  402394:	31 c0                	xor    eax,eax
  402396:	83 c4 1c             	add    esp,0x1c
  402399:	5b                   	pop    ebx
  40239a:	5e                   	pop    esi
  40239b:	5f                   	pop    edi
  40239c:	5d                   	pop    ebp
  40239d:	c3                   	ret    
  40239e:	66 90                	xchg   ax,ax

004023a0 <_glob_strcmp>:
  4023a0:	55                   	push   ebp
  4023a1:	57                   	push   edi
  4023a2:	89 c7                	mov    edi,eax
  4023a4:	56                   	push   esi
  4023a5:	53                   	push   ebx
  4023a6:	83 ec 2c             	sub    esp,0x2c
  4023a9:	80 3a 2e             	cmp    BYTE PTR [edx],0x2e
  4023ac:	89 4c 24 10          	mov    DWORD PTR [esp+0x10],ecx
  4023b0:	0f 84 5a 01 00 00    	je     402510 <_glob_strcmp+0x170>
  4023b6:	0f b6 08             	movzx  ecx,BYTE PTR [eax]
  4023b9:	8b 74 24 10          	mov    esi,DWORD PTR [esp+0x10]
  4023bd:	8d 6a 01             	lea    ebp,[edx+0x1]
  4023c0:	89 f0                	mov    eax,esi
  4023c2:	83 e0 20             	and    eax,0x20
  4023c5:	89 44 24 14          	mov    DWORD PTR [esp+0x14],eax
  4023c9:	89 f0                	mov    eax,esi
  4023cb:	25 00 40 00 00       	and    eax,0x4000
  4023d0:	89 44 24 18          	mov    DWORD PTR [esp+0x18],eax
  4023d4:	0f be d1             	movsx  edx,cl
  4023d7:	85 d2                	test   edx,edx
  4023d9:	8d 75 ff             	lea    esi,[ebp-0x1]
  4023dc:	8d 47 01             	lea    eax,[edi+0x1]
  4023df:	0f 84 70 01 00 00    	je     402555 <_glob_strcmp+0x1b5>
  4023e5:	80 f9 3f             	cmp    cl,0x3f
  4023e8:	0f 84 e4 00 00 00    	je     4024d2 <_glob_strcmp+0x132>
  4023ee:	80 f9 5b             	cmp    cl,0x5b
  4023f1:	0f 84 ab 00 00 00    	je     4024a2 <_glob_strcmp+0x102>
  4023f7:	80 f9 2a             	cmp    cl,0x2a
  4023fa:	74 5c                	je     402458 <_glob_strcmp+0xb8>
  4023fc:	8b 4c 24 14          	mov    ecx,DWORD PTR [esp+0x14]
  402400:	85 c9                	test   ecx,ecx
  402402:	0f 84 d8 00 00 00    	je     4024e0 <_glob_strcmp+0x140>
  402408:	89 c7                	mov    edi,eax
  40240a:	0f be 5d ff          	movsx  ebx,BYTE PTR [ebp-0x1]
  40240e:	84 db                	test   bl,bl
  402410:	0f 84 92 01 00 00    	je     4025a8 <_glob_strcmp+0x208>
  402416:	8b 44 24 18          	mov    eax,DWORD PTR [esp+0x18]
  40241a:	85 c0                	test   eax,eax
  40241c:	0f 85 de 00 00 00    	jne    402500 <_glob_strcmp+0x160>
  402422:	89 14 24             	mov    DWORD PTR [esp],edx
  402425:	89 54 24 1c          	mov    DWORD PTR [esp+0x1c],edx
  402429:	e8 ca 5c 00 00       	call   4080f8 <_tolower>
  40242e:	89 1c 24             	mov    DWORD PTR [esp],ebx
  402431:	89 c6                	mov    esi,eax
  402433:	e8 c0 5c 00 00       	call   4080f8 <_tolower>
  402438:	8b 54 24 1c          	mov    edx,DWORD PTR [esp+0x1c]
  40243c:	29 c6                	sub    esi,eax
  40243e:	85 f6                	test   esi,esi
  402440:	0f 84 81 00 00 00    	je     4024c7 <_glob_strcmp+0x127>
  402446:	89 d0                	mov    eax,edx
  402448:	29 d8                	sub    eax,ebx
  40244a:	8d b6 00 00 00 00    	lea    esi,[esi+0x0]
  402450:	83 c4 2c             	add    esp,0x2c
  402453:	5b                   	pop    ebx
  402454:	5e                   	pop    esi
  402455:	5f                   	pop    edi
  402456:	5d                   	pop    ebp
  402457:	c3                   	ret    
  402458:	0f b6 57 01          	movzx  edx,BYTE PTR [edi+0x1]
  40245c:	89 c3                	mov    ebx,eax
  40245e:	80 fa 2a             	cmp    dl,0x2a
  402461:	75 0b                	jne    40246e <_glob_strcmp+0xce>
  402463:	83 c3 01             	add    ebx,0x1
  402466:	0f b6 13             	movzx  edx,BYTE PTR [ebx]
  402469:	80 fa 2a             	cmp    dl,0x2a
  40246c:	74 f5                	je     402463 <_glob_strcmp+0xc3>
  40246e:	31 c0                	xor    eax,eax
  402470:	84 d2                	test   dl,dl
  402472:	74 dc                	je     402450 <_glob_strcmp+0xb0>
  402474:	8b 7c 24 10          	mov    edi,DWORD PTR [esp+0x10]
  402478:	81 cf 00 00 01 00    	or     edi,0x10000
  40247e:	eb 09                	jmp    402489 <_glob_strcmp+0xe9>
  402480:	83 c6 01             	add    esi,0x1
  402483:	80 7e ff 00          	cmp    BYTE PTR [esi-0x1],0x0
  402487:	74 c7                	je     402450 <_glob_strcmp+0xb0>
  402489:	89 f9                	mov    ecx,edi
  40248b:	89 f2                	mov    edx,esi
  40248d:	89 d8                	mov    eax,ebx
  40248f:	e8 0c ff ff ff       	call   4023a0 <_glob_strcmp>
  402494:	85 c0                	test   eax,eax
  402496:	75 e8                	jne    402480 <_glob_strcmp+0xe0>
  402498:	83 c4 2c             	add    esp,0x2c
  40249b:	31 c0                	xor    eax,eax
  40249d:	5b                   	pop    ebx
  40249e:	5e                   	pop    esi
  40249f:	5f                   	pop    edi
  4024a0:	5d                   	pop    ebp
  4024a1:	c3                   	ret    
  4024a2:	0f be 55 ff          	movsx  edx,BYTE PTR [ebp-0x1]
  4024a6:	85 d2                	test   edx,edx
  4024a8:	0f 84 0b 01 00 00    	je     4025b9 <_glob_strcmp+0x219>
  4024ae:	80 7f 01 21          	cmp    BYTE PTR [edi+0x1],0x21
  4024b2:	74 7c                	je     402530 <_glob_strcmp+0x190>
  4024b4:	8b 4c 24 10          	mov    ecx,DWORD PTR [esp+0x10]
  4024b8:	e8 73 fc ff ff       	call   402130 <_glob_in_set>
  4024bd:	85 c0                	test   eax,eax
  4024bf:	89 c7                	mov    edi,eax
  4024c1:	0f 84 d7 00 00 00    	je     40259e <_glob_strcmp+0x1fe>
  4024c7:	0f b6 0f             	movzx  ecx,BYTE PTR [edi]
  4024ca:	83 c5 01             	add    ebp,0x1
  4024cd:	e9 02 ff ff ff       	jmp    4023d4 <_glob_strcmp+0x34>
  4024d2:	80 7d ff 00          	cmp    BYTE PTR [ebp-0x1],0x0
  4024d6:	0f 84 d3 00 00 00    	je     4025af <_glob_strcmp+0x20f>
  4024dc:	89 c7                	mov    edi,eax
  4024de:	eb e7                	jmp    4024c7 <_glob_strcmp+0x127>
  4024e0:	83 fa 7f             	cmp    edx,0x7f
  4024e3:	0f 85 1f ff ff ff    	jne    402408 <_glob_strcmp+0x68>
  4024e9:	0f be 57 01          	movsx  edx,BYTE PTR [edi+0x1]
  4024ed:	83 c7 02             	add    edi,0x2
  4024f0:	85 d2                	test   edx,edx
  4024f2:	0f 85 12 ff ff ff    	jne    40240a <_glob_strcmp+0x6a>
  4024f8:	e9 0b ff ff ff       	jmp    402408 <_glob_strcmp+0x68>
  4024fd:	8d 76 00             	lea    esi,[esi+0x0]
  402500:	89 d6                	mov    esi,edx
  402502:	29 de                	sub    esi,ebx
  402504:	e9 35 ff ff ff       	jmp    40243e <_glob_strcmp+0x9e>
  402509:	8d b4 26 00 00 00 00 	lea    esi,[esi+eiz*1+0x0]
  402510:	0f be 00             	movsx  eax,BYTE PTR [eax]
  402513:	3c 2e                	cmp    al,0x2e
  402515:	74 32                	je     402549 <_glob_strcmp+0x1a9>
  402517:	89 c1                	mov    ecx,eax
  402519:	83 e8 2e             	sub    eax,0x2e
  40251c:	f7 44 24 10 00 00 01 	test   DWORD PTR [esp+0x10],0x10000
  402523:	00 
  402524:	0f 85 8f fe ff ff    	jne    4023b9 <_glob_strcmp+0x19>
  40252a:	e9 21 ff ff ff       	jmp    402450 <_glob_strcmp+0xb0>
  40252f:	90                   	nop
  402530:	8b 4c 24 10          	mov    ecx,DWORD PTR [esp+0x10]
  402534:	8d 5f 02             	lea    ebx,[edi+0x2]
  402537:	89 d8                	mov    eax,ebx
  402539:	e8 f2 fb ff ff       	call   402130 <_glob_in_set>
  40253e:	85 c0                	test   eax,eax
  402540:	74 1d                	je     40255f <_glob_strcmp+0x1bf>
  402542:	89 df                	mov    edi,ebx
  402544:	e9 7e ff ff ff       	jmp    4024c7 <_glob_strcmp+0x127>
  402549:	b9 2e 00 00 00       	mov    ecx,0x2e
  40254e:	66 90                	xchg   ax,ax
  402550:	e9 64 fe ff ff       	jmp    4023b9 <_glob_strcmp+0x19>
  402555:	0f be 06             	movsx  eax,BYTE PTR [esi]
  402558:	f7 d8                	neg    eax
  40255a:	e9 f1 fe ff ff       	jmp    402450 <_glob_strcmp+0xb0>
  40255f:	0f b6 47 02          	movzx  eax,BYTE PTR [edi+0x2]
  402563:	8b 54 24 14          	mov    edx,DWORD PTR [esp+0x14]
  402567:	3c 5d                	cmp    al,0x5d
  402569:	75 0f                	jne    40257a <_glob_strcmp+0x1da>
  40256b:	eb 56                	jmp    4025c3 <_glob_strcmp+0x223>
  40256d:	8d 76 00             	lea    esi,[esi+0x0]
  402570:	83 c3 01             	add    ebx,0x1
  402573:	84 c0                	test   al,al
  402575:	74 27                	je     40259e <_glob_strcmp+0x1fe>
  402577:	0f b6 03             	movzx  eax,BYTE PTR [ebx]
  40257a:	3c 5d                	cmp    al,0x5d
  40257c:	74 16                	je     402594 <_glob_strcmp+0x1f4>
  40257e:	3c 7f                	cmp    al,0x7f
  402580:	75 ee                	jne    402570 <_glob_strcmp+0x1d0>
  402582:	85 d2                	test   edx,edx
  402584:	75 09                	jne    40258f <_glob_strcmp+0x1ef>
  402586:	0f b6 43 01          	movzx  eax,BYTE PTR [ebx+0x1]
  40258a:	83 c3 01             	add    ebx,0x1
  40258d:	eb e1                	jmp    402570 <_glob_strcmp+0x1d0>
  40258f:	83 c3 01             	add    ebx,0x1
  402592:	eb e3                	jmp    402577 <_glob_strcmp+0x1d7>
  402594:	83 c3 01             	add    ebx,0x1
  402597:	89 df                	mov    edi,ebx
  402599:	e9 29 ff ff ff       	jmp    4024c7 <_glob_strcmp+0x127>
  40259e:	b8 5d 00 00 00       	mov    eax,0x5d
  4025a3:	e9 a8 fe ff ff       	jmp    402450 <_glob_strcmp+0xb0>
  4025a8:	31 db                	xor    ebx,ebx
  4025aa:	e9 97 fe ff ff       	jmp    402446 <_glob_strcmp+0xa6>
  4025af:	b8 3f 00 00 00       	mov    eax,0x3f
  4025b4:	e9 97 fe ff ff       	jmp    402450 <_glob_strcmp+0xb0>
  4025b9:	b8 5b 00 00 00       	mov    eax,0x5b
  4025be:	e9 8d fe ff ff       	jmp    402450 <_glob_strcmp+0xb0>
  4025c3:	8d 5f 03             	lea    ebx,[edi+0x3]
  4025c6:	0f b6 47 03          	movzx  eax,BYTE PTR [edi+0x3]
  4025ca:	8b 54 24 14          	mov    edx,DWORD PTR [esp+0x14]
  4025ce:	eb aa                	jmp    40257a <_glob_strcmp+0x1da>

004025d0 <_glob_registry.part.1>:
  4025d0:	57                   	push   edi
  4025d1:	89 c7                	mov    edi,eax
  4025d3:	56                   	push   esi
  4025d4:	53                   	push   ebx
  4025d5:	83 ec 10             	sub    esp,0x10
  4025d8:	8b 40 04             	mov    eax,DWORD PTR [eax+0x4]
  4025db:	8b 4f 0c             	mov    ecx,DWORD PTR [edi+0xc]
  4025de:	85 c0                	test   eax,eax
  4025e0:	8d 70 ff             	lea    esi,[eax-0x1]
  4025e3:	8d 1c 8d 00 00 00 00 	lea    ebx,[ecx*4+0x0]
  4025ea:	7e 1d                	jle    402609 <_glob_registry.part.1+0x39>
  4025ec:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  4025f0:	8b 57 08             	mov    edx,DWORD PTR [edi+0x8]
  4025f3:	83 ee 01             	sub    esi,0x1
  4025f6:	8b 14 1a             	mov    edx,DWORD PTR [edx+ebx*1]
  4025f9:	83 c3 04             	add    ebx,0x4
  4025fc:	89 14 24             	mov    DWORD PTR [esp],edx
  4025ff:	e8 e4 5a 00 00       	call   4080e8 <_free>
  402604:	83 fe ff             	cmp    esi,0xffffffff
  402607:	75 e7                	jne    4025f0 <_glob_registry.part.1+0x20>
  402609:	8b 47 08             	mov    eax,DWORD PTR [edi+0x8]
  40260c:	89 04 24             	mov    DWORD PTR [esp],eax
  40260f:	e8 d4 5a 00 00       	call   4080e8 <_free>
  402614:	83 c4 10             	add    esp,0x10
  402617:	31 c0                	xor    eax,eax
  402619:	5b                   	pop    ebx
  40261a:	5e                   	pop    esi
  40261b:	5f                   	pop    edi
  40261c:	c3                   	ret    
  40261d:	8d 76 00             	lea    esi,[esi+0x0]

00402620 <_glob_store_entry.part.2>:
  402620:	57                   	push   edi
  402621:	56                   	push   esi
  402622:	89 c6                	mov    esi,eax
  402624:	53                   	push   ebx
  402625:	89 d3                	mov    ebx,edx
  402627:	83 ec 10             	sub    esp,0x10
  40262a:	8b 52 04             	mov    edx,DWORD PTR [edx+0x4]
  40262d:	03 53 0c             	add    edx,DWORD PTR [ebx+0xc]
  402630:	8d 04 95 08 00 00 00 	lea    eax,[edx*4+0x8]
  402637:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
  40263b:	8b 43 08             	mov    eax,DWORD PTR [ebx+0x8]
  40263e:	89 04 24             	mov    DWORD PTR [esp],eax
  402641:	e8 ba 5a 00 00       	call   408100 <_realloc>
  402646:	85 c0                	test   eax,eax
  402648:	89 c2                	mov    edx,eax
  40264a:	74 29                	je     402675 <_glob_store_entry.part.2+0x55>
  40264c:	8b 7b 04             	mov    edi,DWORD PTR [ebx+0x4]
  40264f:	89 43 08             	mov    DWORD PTR [ebx+0x8],eax
  402652:	8b 43 0c             	mov    eax,DWORD PTR [ebx+0xc]
  402655:	8d 4f 01             	lea    ecx,[edi+0x1]
  402658:	01 c7                	add    edi,eax
  40265a:	01 c8                	add    eax,ecx
  40265c:	89 4b 04             	mov    DWORD PTR [ebx+0x4],ecx
  40265f:	89 34 ba             	mov    DWORD PTR [edx+edi*4],esi
  402662:	8b 53 08             	mov    edx,DWORD PTR [ebx+0x8]
  402665:	c7 04 82 00 00 00 00 	mov    DWORD PTR [edx+eax*4],0x0
  40266c:	83 c4 10             	add    esp,0x10
  40266f:	31 c0                	xor    eax,eax
  402671:	5b                   	pop    ebx
  402672:	5e                   	pop    esi
  402673:	5f                   	pop    edi
  402674:	c3                   	ret    
  402675:	83 c4 10             	add    esp,0x10
  402678:	b8 01 00 00 00       	mov    eax,0x1
  40267d:	5b                   	pop    ebx
  40267e:	5e                   	pop    esi
  40267f:	5f                   	pop    edi
  402680:	c3                   	ret    
  402681:	eb 0d                	jmp    402690 <_glob_store_entry>
  402683:	90                   	nop
  402684:	90                   	nop
  402685:	90                   	nop
  402686:	90                   	nop
  402687:	90                   	nop
  402688:	90                   	nop
  402689:	90                   	nop
  40268a:	90                   	nop
  40268b:	90                   	nop
  40268c:	90                   	nop
  40268d:	90                   	nop
  40268e:	90                   	nop
  40268f:	90                   	nop

00402690 <_glob_store_entry>:
  402690:	85 c0                	test   eax,eax
  402692:	75 0c                	jne    4026a0 <_glob_store_entry+0x10>
  402694:	b8 01 00 00 00       	mov    eax,0x1
  402699:	c3                   	ret    
  40269a:	8d b6 00 00 00 00    	lea    esi,[esi+0x0]
  4026a0:	85 d2                	test   edx,edx
  4026a2:	74 f0                	je     402694 <_glob_store_entry+0x4>
  4026a4:	e9 77 ff ff ff       	jmp    402620 <_glob_store_entry.part.2>
  4026a9:	8d b4 26 00 00 00 00 	lea    esi,[esi+eiz*1+0x0]

004026b0 <_glob_store_collated_entries>:
  4026b0:	56                   	push   esi
  4026b1:	89 d6                	mov    esi,edx
  4026b3:	53                   	push   ebx
  4026b4:	89 c3                	mov    ebx,eax
  4026b6:	83 ec 14             	sub    esp,0x14
  4026b9:	8b 00                	mov    eax,DWORD PTR [eax]
  4026bb:	85 c0                	test   eax,eax
  4026bd:	74 05                	je     4026c4 <_glob_store_collated_entries+0x14>
  4026bf:	e8 ec ff ff ff       	call   4026b0 <_glob_store_collated_entries>
  4026c4:	8b 43 08             	mov    eax,DWORD PTR [ebx+0x8]
  4026c7:	89 f2                	mov    edx,esi
  4026c9:	e8 c2 ff ff ff       	call   402690 <_glob_store_entry>
  4026ce:	8b 43 04             	mov    eax,DWORD PTR [ebx+0x4]
  4026d1:	85 c0                	test   eax,eax
  4026d3:	74 07                	je     4026dc <_glob_store_collated_entries+0x2c>
  4026d5:	89 f2                	mov    edx,esi
  4026d7:	e8 d4 ff ff ff       	call   4026b0 <_glob_store_collated_entries>
  4026dc:	89 1c 24             	mov    DWORD PTR [esp],ebx
  4026df:	e8 04 5a 00 00       	call   4080e8 <_free>
  4026e4:	83 c4 14             	add    esp,0x14
  4026e7:	5b                   	pop    ebx
  4026e8:	5e                   	pop    esi
  4026e9:	c3                   	ret    
  4026ea:	8d b6 00 00 00 00    	lea    esi,[esi+0x0]

004026f0 <_glob_match>:
  4026f0:	55                   	push   ebp
  4026f1:	89 e5                	mov    ebp,esp
  4026f3:	57                   	push   edi
  4026f4:	56                   	push   esi
  4026f5:	53                   	push   ebx
  4026f6:	89 c3                	mov    ebx,eax
  4026f8:	83 ec 6c             	sub    esp,0x6c
  4026fb:	89 55 cc             	mov    DWORD PTR [ebp-0x34],edx
  4026fe:	89 4d a4             	mov    DWORD PTR [ebp-0x5c],ecx
  402701:	89 04 24             	mov    DWORD PTR [esp],eax
  402704:	e8 a7 59 00 00       	call   4080b0 <_strlen>
  402709:	8d 50 01             	lea    edx,[eax+0x1]
  40270c:	83 c0 10             	add    eax,0x10
  40270f:	83 e0 f0             	and    eax,0xfffffff0
  402712:	e8 59 f9 ff ff       	call   402070 <___chkstk_ms>
  402717:	29 c4                	sub    esp,eax
  402719:	8d 44 24 0c          	lea    eax,[esp+0xc]
  40271d:	89 54 24 08          	mov    DWORD PTR [esp+0x8],edx
  402721:	89 5c 24 04          	mov    DWORD PTR [esp+0x4],ebx
  402725:	89 04 24             	mov    DWORD PTR [esp],eax
  402728:	e8 ab 59 00 00       	call   4080d8 <_memcpy>
  40272d:	89 04 24             	mov    DWORD PTR [esp],eax
  402730:	e8 4b 06 00 00       	call   402d80 <___mingw_dirname>
  402735:	c7 45 e4 00 00 00 00 	mov    DWORD PTR [ebp-0x1c],0x0
  40273c:	89 45 b8             	mov    DWORD PTR [ebp-0x48],eax
  40273f:	8d 45 d8             	lea    eax,[ebp-0x28]
  402742:	e8 f9 fb ff ff       	call   402340 <_glob_initialise>
  402747:	85 c0                	test   eax,eax
  402749:	74 08                	je     402753 <_glob_match+0x63>
  40274b:	8d 65 f4             	lea    esp,[ebp-0xc]
  40274e:	5b                   	pop    ebx
  40274f:	5e                   	pop    esi
  402750:	5f                   	pop    edi
  402751:	5d                   	pop    ebp
  402752:	c3                   	ret    
  402753:	8b 55 cc             	mov    edx,DWORD PTR [ebp-0x34]
  402756:	8b 45 b8             	mov    eax,DWORD PTR [ebp-0x48]
  402759:	e8 42 f9 ff ff       	call   4020a0 <_is_glob_pattern>
  40275e:	85 c0                	test   eax,eax
  402760:	0f 84 5a 02 00 00    	je     4029c0 <_glob_match+0x2d0>
  402766:	8b 55 cc             	mov    edx,DWORD PTR [ebp-0x34]
  402769:	8d 45 d8             	lea    eax,[ebp-0x28]
  40276c:	89 04 24             	mov    DWORD PTR [esp],eax
  40276f:	8b 4d a4             	mov    ecx,DWORD PTR [ebp-0x5c]
  402772:	8b 45 b8             	mov    eax,DWORD PTR [ebp-0x48]
  402775:	80 ce 80             	or     dh,0x80
  402778:	e8 73 ff ff ff       	call   4026f0 <_glob_match>
  40277d:	85 c0                	test   eax,eax
  40277f:	75 ca                	jne    40274b <_glob_match+0x5b>
  402781:	0f b6 43 01          	movzx  eax,BYTE PTR [ebx+0x1]
  402785:	3c 5c                	cmp    al,0x5c
  402787:	0f 84 5b 03 00 00    	je     402ae8 <_glob_match+0x3f8>
  40278d:	3c 2f                	cmp    al,0x2f
  40278f:	0f 84 53 03 00 00    	je     402ae8 <_glob_match+0x3f8>
  402795:	8b 75 b8             	mov    esi,DWORD PTR [ebp-0x48]
  402798:	bf 30 a1 40 00       	mov    edi,0x40a130
  40279d:	b9 02 00 00 00       	mov    ecx,0x2
  4027a2:	f3 a6                	repz cmps BYTE PTR ds:[esi],BYTE PTR es:[edi]
  4027a4:	0f 85 3e 03 00 00    	jne    402ae8 <_glob_match+0x3f8>
  4027aa:	c6 45 a3 5c          	mov    BYTE PTR [ebp-0x5d],0x5c
  4027ae:	f6 45 cc 10          	test   BYTE PTR [ebp-0x34],0x10
  4027b2:	89 5d c0             	mov    DWORD PTR [ebp-0x40],ebx
  4027b5:	c7 45 b8 00 00 00 00 	mov    DWORD PTR [ebp-0x48],0x0
  4027bc:	0f 85 33 04 00 00    	jne    402bf5 <_glob_match+0x505>
  4027c2:	8b 45 e0             	mov    eax,DWORD PTR [ebp-0x20]
  4027c5:	89 45 c8             	mov    DWORD PTR [ebp-0x38],eax
  4027c8:	8b 00                	mov    eax,DWORD PTR [eax]
  4027ca:	85 c0                	test   eax,eax
  4027cc:	0f 84 71 04 00 00    	je     402c43 <_glob_match+0x553>
  4027d2:	8b 4d cc             	mov    ecx,DWORD PTR [ebp-0x34]
  4027d5:	c7 45 c4 02 00 00 00 	mov    DWORD PTR [ebp-0x3c],0x2
  4027dc:	89 cf                	mov    edi,ecx
  4027de:	83 e7 04             	and    edi,0x4
  4027e1:	89 7d 98             	mov    DWORD PTR [ebp-0x68],edi
  4027e4:	89 cf                	mov    edi,ecx
  4027e6:	81 e7 00 80 00 00    	and    edi,0x8000
  4027ec:	89 7d d0             	mov    DWORD PTR [ebp-0x30],edi
  4027ef:	90                   	nop
  4027f0:	83 7d c4 01          	cmp    DWORD PTR [ebp-0x3c],0x1
  4027f4:	0f 84 58 02 00 00    	je     402a52 <_glob_match+0x362>
  4027fa:	89 04 24             	mov    DWORD PTR [esp],eax
  4027fd:	e8 ee 0a 00 00       	call   4032f0 <___mingw_opendir>
  402802:	85 c0                	test   eax,eax
  402804:	89 45 d4             	mov    DWORD PTR [ebp-0x2c],eax
  402807:	0f 84 76 03 00 00    	je     402b83 <_glob_match+0x493>
  40280d:	8b 45 b8             	mov    eax,DWORD PTR [ebp-0x48]
  402810:	85 c0                	test   eax,eax
  402812:	0f 84 bd 03 00 00    	je     402bd5 <_glob_match+0x4e5>
  402818:	8b 45 c8             	mov    eax,DWORD PTR [ebp-0x38]
  40281b:	8b 00                	mov    eax,DWORD PTR [eax]
  40281d:	89 04 24             	mov    DWORD PTR [esp],eax
  402820:	e8 8b 58 00 00       	call   4080b0 <_strlen>
  402825:	89 45 b4             	mov    DWORD PTR [ebp-0x4c],eax
  402828:	8b 45 cc             	mov    eax,DWORD PTR [ebp-0x34]
  40282b:	c7 45 bc 00 00 00 00 	mov    DWORD PTR [ebp-0x44],0x0
  402832:	83 e0 40             	and    eax,0x40
  402835:	89 45 a8             	mov    DWORD PTR [ebp-0x58],eax
  402838:	8b 45 d4             	mov    eax,DWORD PTR [ebp-0x2c]
  40283b:	89 04 24             	mov    DWORD PTR [esp],eax
  40283e:	e8 4d 0c 00 00       	call   403490 <___mingw_readdir>
  402843:	85 c0                	test   eax,eax
  402845:	89 c6                	mov    esi,eax
  402847:	0f 84 e8 01 00 00    	je     402a35 <_glob_match+0x345>
  40284d:	8b 45 d0             	mov    eax,DWORD PTR [ebp-0x30]
  402850:	85 c0                	test   eax,eax
  402852:	74 06                	je     40285a <_glob_match+0x16a>
  402854:	83 7e 08 10          	cmp    DWORD PTR [esi+0x8],0x10
  402858:	75 de                	jne    402838 <_glob_match+0x148>
  40285a:	8b 4d cc             	mov    ecx,DWORD PTR [ebp-0x34]
  40285d:	8d 5e 0c             	lea    ebx,[esi+0xc]
  402860:	8b 45 c0             	mov    eax,DWORD PTR [ebp-0x40]
  402863:	89 da                	mov    edx,ebx
  402865:	e8 36 fb ff ff       	call   4023a0 <_glob_strcmp>
  40286a:	85 c0                	test   eax,eax
  40286c:	75 ca                	jne    402838 <_glob_match+0x148>
  40286e:	0f b7 56 06          	movzx  edx,WORD PTR [esi+0x6]
  402872:	8b 4d b4             	mov    ecx,DWORD PTR [ebp-0x4c]
  402875:	89 65 b0             	mov    DWORD PTR [ebp-0x50],esp
  402878:	8d 44 11 11          	lea    eax,[ecx+edx*1+0x11]
  40287c:	83 e0 f0             	and    eax,0xfffffff0
  40287f:	e8 ec f7 ff ff       	call   402070 <___chkstk_ms>
  402884:	29 c4                	sub    esp,eax
  402886:	31 c0                	xor    eax,eax
  402888:	8d 7c 24 0c          	lea    edi,[esp+0xc]
  40288c:	85 c9                	test   ecx,ecx
  40288e:	89 7d ac             	mov    DWORD PTR [ebp-0x54],edi
  402891:	0f 85 ed 01 00 00    	jne    402a84 <_glob_match+0x394>
  402897:	83 c2 01             	add    edx,0x1
  40289a:	01 f8                	add    eax,edi
  40289c:	89 54 24 08          	mov    DWORD PTR [esp+0x8],edx
  4028a0:	89 5c 24 04          	mov    DWORD PTR [esp+0x4],ebx
  4028a4:	89 e3                	mov    ebx,esp
  4028a6:	89 04 24             	mov    DWORD PTR [esp],eax
  4028a9:	e8 2a 58 00 00       	call   4080d8 <_memcpy>
  4028ae:	89 3c 24             	mov    DWORD PTR [esp],edi
  4028b1:	e8 fa 57 00 00       	call   4080b0 <_strlen>
  4028b6:	83 c0 10             	add    eax,0x10
  4028b9:	83 e0 f0             	and    eax,0xfffffff0
  4028bc:	e8 af f7 ff ff       	call   402070 <___chkstk_ms>
  4028c1:	8b 75 ac             	mov    esi,DWORD PTR [ebp-0x54]
  4028c4:	29 c4                	sub    esp,eax
  4028c6:	8d 4c 24 0c          	lea    ecx,[esp+0xc]
  4028ca:	89 ca                	mov    edx,ecx
  4028cc:	eb 0f                	jmp    4028dd <_glob_match+0x1ed>
  4028ce:	66 90                	xchg   ax,ax
  4028d0:	83 c2 01             	add    edx,0x1
  4028d3:	83 c6 01             	add    esi,0x1
  4028d6:	84 c0                	test   al,al
  4028d8:	88 42 ff             	mov    BYTE PTR [edx-0x1],al
  4028db:	74 1b                	je     4028f8 <_glob_match+0x208>
  4028dd:	0f b6 06             	movzx  eax,BYTE PTR [esi]
  4028e0:	3c 7f                	cmp    al,0x7f
  4028e2:	75 ec                	jne    4028d0 <_glob_match+0x1e0>
  4028e4:	0f b6 46 01          	movzx  eax,BYTE PTR [esi+0x1]
  4028e8:	83 c6 01             	add    esi,0x1
  4028eb:	83 c2 01             	add    edx,0x1
  4028ee:	83 c6 01             	add    esi,0x1
  4028f1:	84 c0                	test   al,al
  4028f3:	88 42 ff             	mov    BYTE PTR [edx-0x1],al
  4028f6:	75 e5                	jne    4028dd <_glob_match+0x1ed>
  4028f8:	89 0c 24             	mov    DWORD PTR [esp],ecx
  4028fb:	e8 70 5b 00 00       	call   408470 <_strdup>
  402900:	89 dc                	mov    esp,ebx
  402902:	85 c0                	test   eax,eax
  402904:	89 c6                	mov    esi,eax
  402906:	0f 84 c6 01 00 00    	je     402ad2 <_glob_match+0x3e2>
  40290c:	31 c0                	xor    eax,eax
  40290e:	83 7d c4 02          	cmp    DWORD PTR [ebp-0x3c],0x2
  402912:	0f 94 c0             	sete   al
  402915:	83 e8 01             	sub    eax,0x1
  402918:	21 45 c4             	and    DWORD PTR [ebp-0x3c],eax
  40291b:	8b 45 a8             	mov    eax,DWORD PTR [ebp-0x58]
  40291e:	85 c0                	test   eax,eax
  402920:	0f 85 9d 01 00 00    	jne    402ac3 <_glob_match+0x3d3>
  402926:	8b 5d bc             	mov    ebx,DWORD PTR [ebp-0x44]
  402929:	85 db                	test   ebx,ebx
  40292b:	0f 84 bb 02 00 00    	je     402bec <_glob_match+0x4fc>
  402931:	8b 7d cc             	mov    edi,DWORD PTR [ebp-0x34]
  402934:	81 e7 00 40 00 00    	and    edi,0x4000
  40293a:	eb 18                	jmp    402954 <_glob_match+0x264>
  40293c:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  402940:	e8 c3 57 00 00       	call   408108 <_strcoll>
  402945:	8b 0b                	mov    ecx,DWORD PTR [ebx]
  402947:	8b 53 04             	mov    edx,DWORD PTR [ebx+0x4]
  40294a:	85 c0                	test   eax,eax
  40294c:	7e 22                	jle    402970 <_glob_match+0x280>
  40294e:	85 d2                	test   edx,edx
  402950:	74 24                	je     402976 <_glob_match+0x286>
  402952:	89 d3                	mov    ebx,edx
  402954:	8b 43 08             	mov    eax,DWORD PTR [ebx+0x8]
  402957:	85 ff                	test   edi,edi
  402959:	89 34 24             	mov    DWORD PTR [esp],esi
  40295c:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
  402960:	75 de                	jne    402940 <_glob_match+0x250>
  402962:	e8 11 5b 00 00       	call   408478 <_stricoll>
  402967:	8b 0b                	mov    ecx,DWORD PTR [ebx]
  402969:	8b 53 04             	mov    edx,DWORD PTR [ebx+0x4]
  40296c:	85 c0                	test   eax,eax
  40296e:	7f de                	jg     40294e <_glob_match+0x25e>
  402970:	89 ca                	mov    edx,ecx
  402972:	85 d2                	test   edx,edx
  402974:	75 dc                	jne    402952 <_glob_match+0x262>
  402976:	89 c1                	mov    ecx,eax
  402978:	89 4d ac             	mov    DWORD PTR [ebp-0x54],ecx
  40297b:	c7 04 24 0c 00 00 00 	mov    DWORD PTR [esp],0xc
  402982:	e8 69 57 00 00       	call   4080f0 <_malloc>
  402987:	85 c0                	test   eax,eax
  402989:	74 22                	je     4029ad <_glob_match+0x2bd>
  40298b:	85 db                	test   ebx,ebx
  40298d:	89 70 08             	mov    DWORD PTR [eax+0x8],esi
  402990:	c7 40 04 00 00 00 00 	mov    DWORD PTR [eax+0x4],0x0
  402997:	c7 00 00 00 00 00    	mov    DWORD PTR [eax],0x0
  40299d:	74 0e                	je     4029ad <_glob_match+0x2bd>
  40299f:	8b 4d ac             	mov    ecx,DWORD PTR [ebp-0x54]
  4029a2:	85 c9                	test   ecx,ecx
  4029a4:	0f 8e 16 02 00 00    	jle    402bc0 <_glob_match+0x4d0>
  4029aa:	89 43 04             	mov    DWORD PTR [ebx+0x4],eax
  4029ad:	8b 7d bc             	mov    edi,DWORD PTR [ebp-0x44]
  4029b0:	85 ff                	test   edi,edi
  4029b2:	0f 84 15 02 00 00    	je     402bcd <_glob_match+0x4dd>
  4029b8:	8b 65 b0             	mov    esp,DWORD PTR [ebp-0x50]
  4029bb:	e9 78 fe ff ff       	jmp    402838 <_glob_match+0x148>
  4029c0:	8b 45 b8             	mov    eax,DWORD PTR [ebp-0x48]
  4029c3:	89 e6                	mov    esi,esp
  4029c5:	89 04 24             	mov    DWORD PTR [esp],eax
  4029c8:	e8 e3 56 00 00       	call   4080b0 <_strlen>
  4029cd:	83 c0 10             	add    eax,0x10
  4029d0:	83 e0 f0             	and    eax,0xfffffff0
  4029d3:	e8 98 f6 ff ff       	call   402070 <___chkstk_ms>
  4029d8:	8b 55 b8             	mov    edx,DWORD PTR [ebp-0x48]
  4029db:	29 c4                	sub    esp,eax
  4029dd:	8d 7c 24 0c          	lea    edi,[esp+0xc]
  4029e1:	89 f9                	mov    ecx,edi
  4029e3:	eb 0d                	jmp    4029f2 <_glob_match+0x302>
  4029e5:	83 c1 01             	add    ecx,0x1
  4029e8:	83 c2 01             	add    edx,0x1
  4029eb:	84 c0                	test   al,al
  4029ed:	88 41 ff             	mov    BYTE PTR [ecx-0x1],al
  4029f0:	74 1b                	je     402a0d <_glob_match+0x31d>
  4029f2:	0f b6 02             	movzx  eax,BYTE PTR [edx]
  4029f5:	3c 7f                	cmp    al,0x7f
  4029f7:	75 ec                	jne    4029e5 <_glob_match+0x2f5>
  4029f9:	0f b6 42 01          	movzx  eax,BYTE PTR [edx+0x1]
  4029fd:	83 c2 01             	add    edx,0x1
  402a00:	83 c1 01             	add    ecx,0x1
  402a03:	83 c2 01             	add    edx,0x1
  402a06:	84 c0                	test   al,al
  402a08:	88 41 ff             	mov    BYTE PTR [ecx-0x1],al
  402a0b:	75 e5                	jne    4029f2 <_glob_match+0x302>
  402a0d:	89 3c 24             	mov    DWORD PTR [esp],edi
  402a10:	e8 5b 5a 00 00       	call   408470 <_strdup>
  402a15:	89 f4                	mov    esp,esi
  402a17:	89 c1                	mov    ecx,eax
  402a19:	b8 01 00 00 00       	mov    eax,0x1
  402a1e:	85 c9                	test   ecx,ecx
  402a20:	0f 84 25 fd ff ff    	je     40274b <_glob_match+0x5b>
  402a26:	8d 55 d8             	lea    edx,[ebp-0x28]
  402a29:	89 c8                	mov    eax,ecx
  402a2b:	e8 f0 fb ff ff       	call   402620 <_glob_store_entry.part.2>
  402a30:	e9 48 fd ff ff       	jmp    40277d <_glob_match+0x8d>
  402a35:	8b 45 d4             	mov    eax,DWORD PTR [ebp-0x2c]
  402a38:	89 04 24             	mov    DWORD PTR [esp],eax
  402a3b:	e8 a0 0a 00 00       	call   4034e0 <___mingw_closedir>
  402a40:	8b 75 bc             	mov    esi,DWORD PTR [ebp-0x44]
  402a43:	85 f6                	test   esi,esi
  402a45:	74 0b                	je     402a52 <_glob_match+0x362>
  402a47:	8b 55 08             	mov    edx,DWORD PTR [ebp+0x8]
  402a4a:	8b 45 bc             	mov    eax,DWORD PTR [ebp-0x44]
  402a4d:	e8 5e fc ff ff       	call   4026b0 <_glob_store_collated_entries>
  402a52:	83 45 c8 04          	add    DWORD PTR [ebp-0x38],0x4
  402a56:	8b 7d c8             	mov    edi,DWORD PTR [ebp-0x38]
  402a59:	8b 47 fc             	mov    eax,DWORD PTR [edi-0x4]
  402a5c:	89 04 24             	mov    DWORD PTR [esp],eax
  402a5f:	e8 84 56 00 00       	call   4080e8 <_free>
  402a64:	8b 07                	mov    eax,DWORD PTR [edi]
  402a66:	85 c0                	test   eax,eax
  402a68:	0f 85 82 fd ff ff    	jne    4027f0 <_glob_match+0x100>
  402a6e:	8b 45 e0             	mov    eax,DWORD PTR [ebp-0x20]
  402a71:	89 04 24             	mov    DWORD PTR [esp],eax
  402a74:	e8 6f 56 00 00       	call   4080e8 <_free>
  402a79:	8b 45 c4             	mov    eax,DWORD PTR [ebp-0x3c]
  402a7c:	8d 65 f4             	lea    esp,[ebp-0xc]
  402a7f:	5b                   	pop    ebx
  402a80:	5e                   	pop    esi
  402a81:	5f                   	pop    edi
  402a82:	5d                   	pop    ebp
  402a83:	c3                   	ret    
  402a84:	8b 45 c8             	mov    eax,DWORD PTR [ebp-0x38]
  402a87:	8b 75 b4             	mov    esi,DWORD PTR [ebp-0x4c]
  402a8a:	89 55 9c             	mov    DWORD PTR [ebp-0x64],edx
  402a8d:	8b 00                	mov    eax,DWORD PTR [eax]
  402a8f:	89 74 24 08          	mov    DWORD PTR [esp+0x8],esi
  402a93:	89 3c 24             	mov    DWORD PTR [esp],edi
  402a96:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
  402a9a:	e8 39 56 00 00       	call   4080d8 <_memcpy>
  402a9f:	0f b6 44 34 0b       	movzx  eax,BYTE PTR [esp+esi*1+0xb]
  402aa4:	8b 55 9c             	mov    edx,DWORD PTR [ebp-0x64]
  402aa7:	3c 5c                	cmp    al,0x5c
  402aa9:	74 35                	je     402ae0 <_glob_match+0x3f0>
  402aab:	3c 2f                	cmp    al,0x2f
  402aad:	74 31                	je     402ae0 <_glob_match+0x3f0>
  402aaf:	8b 75 b4             	mov    esi,DWORD PTR [ebp-0x4c]
  402ab2:	0f b6 4d a3          	movzx  ecx,BYTE PTR [ebp-0x5d]
  402ab6:	89 f0                	mov    eax,esi
  402ab8:	83 c0 01             	add    eax,0x1
  402abb:	88 0c 37             	mov    BYTE PTR [edi+esi*1],cl
  402abe:	e9 d4 fd ff ff       	jmp    402897 <_glob_match+0x1a7>
  402ac3:	8b 55 08             	mov    edx,DWORD PTR [ebp+0x8]
  402ac6:	89 f0                	mov    eax,esi
  402ac8:	e8 c3 fb ff ff       	call   402690 <_glob_store_entry>
  402acd:	e9 e6 fe ff ff       	jmp    4029b8 <_glob_match+0x2c8>
  402ad2:	c7 45 c4 03 00 00 00 	mov    DWORD PTR [ebp-0x3c],0x3
  402ad9:	e9 da fe ff ff       	jmp    4029b8 <_glob_match+0x2c8>
  402ade:	66 90                	xchg   ax,ax
  402ae0:	8b 45 b4             	mov    eax,DWORD PTR [ebp-0x4c]
  402ae3:	e9 af fd ff ff       	jmp    402897 <_glob_match+0x1a7>
  402ae8:	8b 45 b8             	mov    eax,DWORD PTR [ebp-0x48]
  402aeb:	89 04 24             	mov    DWORD PTR [esp],eax
  402aee:	e8 bd 55 00 00       	call   4080b0 <_strlen>
  402af3:	01 d8                	add    eax,ebx
  402af5:	39 c3                	cmp    ebx,eax
  402af7:	0f 83 94 01 00 00    	jae    402c91 <_glob_match+0x5a1>
  402afd:	0f b6 10             	movzx  edx,BYTE PTR [eax]
  402b00:	80 fa 2f             	cmp    dl,0x2f
  402b03:	0f 84 7d 01 00 00    	je     402c86 <_glob_match+0x596>
  402b09:	80 fa 5c             	cmp    dl,0x5c
  402b0c:	75 1d                	jne    402b2b <_glob_match+0x43b>
  402b0e:	66 90                	xchg   ax,ax
  402b10:	e9 71 01 00 00       	jmp    402c86 <_glob_match+0x596>
  402b15:	0f b6 40 ff          	movzx  eax,BYTE PTR [eax-0x1]
  402b19:	3c 5c                	cmp    al,0x5c
  402b1b:	0f 84 c0 00 00 00    	je     402be1 <_glob_match+0x4f1>
  402b21:	3c 2f                	cmp    al,0x2f
  402b23:	0f 84 b8 00 00 00    	je     402be1 <_glob_match+0x4f1>
  402b29:	89 d0                	mov    eax,edx
  402b2b:	8d 50 ff             	lea    edx,[eax-0x1]
  402b2e:	39 da                	cmp    edx,ebx
  402b30:	75 e3                	jne    402b15 <_glob_match+0x425>
  402b32:	0f b6 40 ff          	movzx  eax,BYTE PTR [eax-0x1]
  402b36:	89 55 c0             	mov    DWORD PTR [ebp-0x40],edx
  402b39:	88 45 a3             	mov    BYTE PTR [ebp-0x5d],al
  402b3c:	80 7d a3 5c          	cmp    BYTE PTR [ebp-0x5d],0x5c
  402b40:	0f 85 0c 01 00 00    	jne    402c52 <_glob_match+0x562>
  402b46:	8b 45 c0             	mov    eax,DWORD PTR [ebp-0x40]
  402b49:	0f b6 4d a3          	movzx  ecx,BYTE PTR [ebp-0x5d]
  402b4d:	83 c0 01             	add    eax,0x1
  402b50:	0f b6 10             	movzx  edx,BYTE PTR [eax]
  402b53:	80 fa 5c             	cmp    dl,0x5c
  402b56:	75 0d                	jne    402b65 <_glob_match+0x475>
  402b58:	83 c0 01             	add    eax,0x1
  402b5b:	89 d1                	mov    ecx,edx
  402b5d:	0f b6 10             	movzx  edx,BYTE PTR [eax]
  402b60:	80 fa 5c             	cmp    dl,0x5c
  402b63:	74 f3                	je     402b58 <_glob_match+0x468>
  402b65:	80 fa 2f             	cmp    dl,0x2f
  402b68:	74 ee                	je     402b58 <_glob_match+0x468>
  402b6a:	89 45 c0             	mov    DWORD PTR [ebp-0x40],eax
  402b6d:	88 4d a3             	mov    BYTE PTR [ebp-0x5d],cl
  402b70:	8b 45 b8             	mov    eax,DWORD PTR [ebp-0x48]
  402b73:	85 c0                	test   eax,eax
  402b75:	0f 85 47 fc ff ff    	jne    4027c2 <_glob_match+0xd2>
  402b7b:	8b 5d c0             	mov    ebx,DWORD PTR [ebp-0x40]
  402b7e:	e9 2b fc ff ff       	jmp    4027ae <_glob_match+0xbe>
  402b83:	8b 5d 98             	mov    ebx,DWORD PTR [ebp-0x68]
  402b86:	85 db                	test   ebx,ebx
  402b88:	75 28                	jne    402bb2 <_glob_match+0x4c2>
  402b8a:	8b 7d a4             	mov    edi,DWORD PTR [ebp-0x5c]
  402b8d:	85 ff                	test   edi,edi
  402b8f:	0f 84 bd fe ff ff    	je     402a52 <_glob_match+0x362>
  402b95:	e8 76 55 00 00       	call   408110 <__errno>
  402b9a:	8b 00                	mov    eax,DWORD PTR [eax]
  402b9c:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
  402ba0:	8b 45 c8             	mov    eax,DWORD PTR [ebp-0x38]
  402ba3:	8b 00                	mov    eax,DWORD PTR [eax]
  402ba5:	89 04 24             	mov    DWORD PTR [esp],eax
  402ba8:	ff d7                	call   edi
  402baa:	85 c0                	test   eax,eax
  402bac:	0f 84 a0 fe ff ff    	je     402a52 <_glob_match+0x362>
  402bb2:	c7 45 c4 01 00 00 00 	mov    DWORD PTR [ebp-0x3c],0x1
  402bb9:	e9 94 fe ff ff       	jmp    402a52 <_glob_match+0x362>
  402bbe:	66 90                	xchg   ax,ax
  402bc0:	8b 7d bc             	mov    edi,DWORD PTR [ebp-0x44]
  402bc3:	89 03                	mov    DWORD PTR [ebx],eax
  402bc5:	85 ff                	test   edi,edi
  402bc7:	0f 85 eb fd ff ff    	jne    4029b8 <_glob_match+0x2c8>
  402bcd:	89 45 bc             	mov    DWORD PTR [ebp-0x44],eax
  402bd0:	e9 e3 fd ff ff       	jmp    4029b8 <_glob_match+0x2c8>
  402bd5:	c7 45 b4 00 00 00 00 	mov    DWORD PTR [ebp-0x4c],0x0
  402bdc:	e9 47 fc ff ff       	jmp    402828 <_glob_match+0x138>
  402be1:	89 55 c0             	mov    DWORD PTR [ebp-0x40],edx
  402be4:	88 45 a3             	mov    BYTE PTR [ebp-0x5d],al
  402be7:	e9 50 ff ff ff       	jmp    402b3c <_glob_match+0x44c>
  402bec:	31 db                	xor    ebx,ebx
  402bee:	31 c9                	xor    ecx,ecx
  402bf0:	e9 83 fd ff ff       	jmp    402978 <_glob_match+0x288>
  402bf5:	8b 55 cc             	mov    edx,DWORD PTR [ebp-0x34]
  402bf8:	89 d8                	mov    eax,ebx
  402bfa:	e8 a1 f4 ff ff       	call   4020a0 <_is_glob_pattern>
  402bff:	85 c0                	test   eax,eax
  402c01:	0f 85 bb fb ff ff    	jne    4027c2 <_glob_match+0xd2>
  402c07:	89 1c 24             	mov    DWORD PTR [esp],ebx
  402c0a:	89 e6                	mov    esi,esp
  402c0c:	e8 9f 54 00 00       	call   4080b0 <_strlen>
  402c11:	83 c0 10             	add    eax,0x10
  402c14:	83 e0 f0             	and    eax,0xfffffff0
  402c17:	e8 54 f4 ff ff       	call   402070 <___chkstk_ms>
  402c1c:	29 c4                	sub    esp,eax
  402c1e:	8d 4c 24 0c          	lea    ecx,[esp+0xc]
  402c22:	89 ca                	mov    edx,ecx
  402c24:	eb 0d                	jmp    402c33 <_glob_match+0x543>
  402c26:	83 c2 01             	add    edx,0x1
  402c29:	83 c3 01             	add    ebx,0x1
  402c2c:	84 c0                	test   al,al
  402c2e:	88 42 ff             	mov    BYTE PTR [edx-0x1],al
  402c31:	74 32                	je     402c65 <_glob_match+0x575>
  402c33:	0f b6 03             	movzx  eax,BYTE PTR [ebx]
  402c36:	3c 7f                	cmp    al,0x7f
  402c38:	75 ec                	jne    402c26 <_glob_match+0x536>
  402c3a:	0f b6 43 01          	movzx  eax,BYTE PTR [ebx+0x1]
  402c3e:	83 c3 01             	add    ebx,0x1
  402c41:	eb e3                	jmp    402c26 <_glob_match+0x536>
  402c43:	8b 45 c8             	mov    eax,DWORD PTR [ebp-0x38]
  402c46:	c7 45 c4 02 00 00 00 	mov    DWORD PTR [ebp-0x3c],0x2
  402c4d:	e9 1f fe ff ff       	jmp    402a71 <_glob_match+0x381>
  402c52:	80 7d a3 2f          	cmp    BYTE PTR [ebp-0x5d],0x2f
  402c56:	0f 84 ea fe ff ff    	je     402b46 <_glob_match+0x456>
  402c5c:	c6 45 a3 5c          	mov    BYTE PTR [ebp-0x5d],0x5c
  402c60:	e9 0b ff ff ff       	jmp    402b70 <_glob_match+0x480>
  402c65:	89 0c 24             	mov    DWORD PTR [esp],ecx
  402c68:	e8 03 58 00 00       	call   408470 <_strdup>
  402c6d:	8b 55 08             	mov    edx,DWORD PTR [ebp+0x8]
  402c70:	89 f4                	mov    esp,esi
  402c72:	e8 19 fa ff ff       	call   402690 <_glob_store_entry>
  402c77:	8b 45 e0             	mov    eax,DWORD PTR [ebp-0x20]
  402c7a:	c7 45 c4 00 00 00 00 	mov    DWORD PTR [ebp-0x3c],0x0
  402c81:	e9 eb fd ff ff       	jmp    402a71 <_glob_match+0x381>
  402c86:	88 55 a3             	mov    BYTE PTR [ebp-0x5d],dl
  402c89:	89 45 c0             	mov    DWORD PTR [ebp-0x40],eax
  402c8c:	e9 ab fe ff ff       	jmp    402b3c <_glob_match+0x44c>
  402c91:	0f b6 08             	movzx  ecx,BYTE PTR [eax]
  402c94:	89 45 c0             	mov    DWORD PTR [ebp-0x40],eax
  402c97:	88 4d a3             	mov    BYTE PTR [ebp-0x5d],cl
  402c9a:	e9 9d fe ff ff       	jmp    402b3c <_glob_match+0x44c>
  402c9f:	90                   	nop

00402ca0 <___mingw_glob>:
  402ca0:	55                   	push   ebp
  402ca1:	89 e5                	mov    ebp,esp
  402ca3:	57                   	push   edi
  402ca4:	56                   	push   esi
  402ca5:	53                   	push   ebx
  402ca6:	83 ec 1c             	sub    esp,0x1c
  402ca9:	8b 75 14             	mov    esi,DWORD PTR [ebp+0x14]
  402cac:	8b 5d 08             	mov    ebx,DWORD PTR [ebp+0x8]
  402caf:	81 3e 32 a1 40 00    	cmp    DWORD PTR [esi],0x40a132
  402cb5:	74 0d                	je     402cc4 <___mingw_glob+0x24>
  402cb7:	89 f0                	mov    eax,esi
  402cb9:	e8 82 f6 ff ff       	call   402340 <_glob_initialise>
  402cbe:	c7 06 32 a1 40 00    	mov    DWORD PTR [esi],0x40a132
  402cc4:	89 34 24             	mov    DWORD PTR [esp],esi
  402cc7:	8b 4d 10             	mov    ecx,DWORD PTR [ebp+0x10]
  402cca:	89 d8                	mov    eax,ebx
  402ccc:	8b 55 0c             	mov    edx,DWORD PTR [ebp+0xc]
  402ccf:	e8 1c fa ff ff       	call   4026f0 <_glob_match>
  402cd4:	83 f8 02             	cmp    eax,0x2
  402cd7:	89 c7                	mov    edi,eax
  402cd9:	74 0a                	je     402ce5 <___mingw_glob+0x45>
  402cdb:	8d 65 f4             	lea    esp,[ebp-0xc]
  402cde:	89 f8                	mov    eax,edi
  402ce0:	5b                   	pop    ebx
  402ce1:	5e                   	pop    esi
  402ce2:	5f                   	pop    edi
  402ce3:	5d                   	pop    ebp
  402ce4:	c3                   	ret    
  402ce5:	f6 45 0c 10          	test   BYTE PTR [ebp+0xc],0x10
  402ce9:	74 f0                	je     402cdb <___mingw_glob+0x3b>
  402ceb:	89 65 e4             	mov    DWORD PTR [ebp-0x1c],esp
  402cee:	89 1c 24             	mov    DWORD PTR [esp],ebx
  402cf1:	e8 ba 53 00 00       	call   4080b0 <_strlen>
  402cf6:	83 c0 10             	add    eax,0x10
  402cf9:	83 e0 f0             	and    eax,0xfffffff0
  402cfc:	e8 6f f3 ff ff       	call   402070 <___chkstk_ms>
  402d01:	29 c4                	sub    esp,eax
  402d03:	8d 4c 24 04          	lea    ecx,[esp+0x4]
  402d07:	89 ca                	mov    edx,ecx
  402d09:	eb 12                	jmp    402d1d <___mingw_glob+0x7d>
  402d0b:	90                   	nop
  402d0c:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  402d10:	83 c2 01             	add    edx,0x1
  402d13:	83 c3 01             	add    ebx,0x1
  402d16:	84 c0                	test   al,al
  402d18:	88 42 ff             	mov    BYTE PTR [edx-0x1],al
  402d1b:	74 1b                	je     402d38 <___mingw_glob+0x98>
  402d1d:	0f b6 03             	movzx  eax,BYTE PTR [ebx]
  402d20:	3c 7f                	cmp    al,0x7f
  402d22:	75 ec                	jne    402d10 <___mingw_glob+0x70>
  402d24:	0f b6 43 01          	movzx  eax,BYTE PTR [ebx+0x1]
  402d28:	83 c3 01             	add    ebx,0x1
  402d2b:	83 c2 01             	add    edx,0x1
  402d2e:	83 c3 01             	add    ebx,0x1
  402d31:	84 c0                	test   al,al
  402d33:	88 42 ff             	mov    BYTE PTR [edx-0x1],al
  402d36:	75 e5                	jne    402d1d <___mingw_glob+0x7d>
  402d38:	89 0c 24             	mov    DWORD PTR [esp],ecx
  402d3b:	e8 30 57 00 00       	call   408470 <_strdup>
  402d40:	8b 65 e4             	mov    esp,DWORD PTR [ebp-0x1c]
  402d43:	89 f2                	mov    edx,esi
  402d45:	e8 46 f9 ff ff       	call   402690 <_glob_store_entry>
  402d4a:	8d 65 f4             	lea    esp,[ebp-0xc]
  402d4d:	89 f8                	mov    eax,edi
  402d4f:	5b                   	pop    ebx
  402d50:	5e                   	pop    esi
  402d51:	5f                   	pop    edi
  402d52:	5d                   	pop    ebp
  402d53:	c3                   	ret    
  402d54:	8d b6 00 00 00 00    	lea    esi,[esi+0x0]
  402d5a:	8d bf 00 00 00 00    	lea    edi,[edi+0x0]

00402d60 <___mingw_globfree>:
  402d60:	8b 44 24 04          	mov    eax,DWORD PTR [esp+0x4]
  402d64:	81 38 32 a1 40 00    	cmp    DWORD PTR [eax],0x40a132
  402d6a:	74 04                	je     402d70 <___mingw_globfree+0x10>
  402d6c:	f3 c3                	repz ret 
  402d6e:	66 90                	xchg   ax,ax
  402d70:	e9 5b f8 ff ff       	jmp    4025d0 <_glob_registry.part.1>
  402d75:	90                   	nop
  402d76:	90                   	nop
  402d77:	90                   	nop
  402d78:	90                   	nop
  402d79:	90                   	nop
  402d7a:	90                   	nop
  402d7b:	90                   	nop
  402d7c:	90                   	nop
  402d7d:	90                   	nop
  402d7e:	90                   	nop
  402d7f:	90                   	nop

00402d80 <___mingw_dirname>:
  402d80:	55                   	push   ebp
  402d81:	89 e5                	mov    ebp,esp
  402d83:	57                   	push   edi
  402d84:	56                   	push   esi
  402d85:	53                   	push   ebx
  402d86:	83 ec 3c             	sub    esp,0x3c
  402d89:	8b 75 08             	mov    esi,DWORD PTR [ebp+0x8]
  402d8c:	c7 44 24 04 00 00 00 	mov    DWORD PTR [esp+0x4],0x0
  402d93:	00 
  402d94:	c7 04 24 02 00 00 00 	mov    DWORD PTR [esp],0x2
  402d9b:	e8 78 53 00 00       	call   408118 <_setlocale>
  402da0:	85 c0                	test   eax,eax
  402da2:	89 c3                	mov    ebx,eax
  402da4:	74 0a                	je     402db0 <___mingw_dirname+0x30>
  402da6:	89 04 24             	mov    DWORD PTR [esp],eax
  402da9:	e8 c2 56 00 00       	call   408470 <_strdup>
  402dae:	89 c3                	mov    ebx,eax
  402db0:	c7 44 24 04 44 a1 40 	mov    DWORD PTR [esp+0x4],0x40a144
  402db7:	00 
  402db8:	c7 04 24 02 00 00 00 	mov    DWORD PTR [esp],0x2
  402dbf:	e8 54 53 00 00       	call   408118 <_setlocale>
  402dc4:	85 f6                	test   esi,esi
  402dc6:	74 05                	je     402dcd <___mingw_dirname+0x4d>
  402dc8:	80 3e 00             	cmp    BYTE PTR [esi],0x0
  402dcb:	75 73                	jne    402e40 <___mingw_dirname+0xc0>
  402dcd:	c7 44 24 08 00 00 00 	mov    DWORD PTR [esp+0x8],0x0
  402dd4:	00 
  402dd5:	c7 44 24 04 46 a1 40 	mov    DWORD PTR [esp+0x4],0x40a146
  402ddc:	00 
  402ddd:	c7 04 24 00 00 00 00 	mov    DWORD PTR [esp],0x0
  402de4:	e8 37 53 00 00       	call   408120 <_wcstombs>
  402de9:	8d 70 01             	lea    esi,[eax+0x1]
  402dec:	89 74 24 04          	mov    DWORD PTR [esp+0x4],esi
  402df0:	a1 68 d0 40 00       	mov    eax,ds:0x40d068
  402df5:	89 04 24             	mov    DWORD PTR [esp],eax
  402df8:	e8 03 53 00 00       	call   408100 <_realloc>
  402dfd:	a3 68 d0 40 00       	mov    ds:0x40d068,eax
  402e02:	89 74 24 08          	mov    DWORD PTR [esp+0x8],esi
  402e06:	c7 44 24 04 46 a1 40 	mov    DWORD PTR [esp+0x4],0x40a146
  402e0d:	00 
  402e0e:	89 04 24             	mov    DWORD PTR [esp],eax
  402e11:	e8 0a 53 00 00       	call   408120 <_wcstombs>
  402e16:	89 5c 24 04          	mov    DWORD PTR [esp+0x4],ebx
  402e1a:	c7 04 24 02 00 00 00 	mov    DWORD PTR [esp],0x2
  402e21:	e8 f2 52 00 00       	call   408118 <_setlocale>
  402e26:	89 1c 24             	mov    DWORD PTR [esp],ebx
  402e29:	e8 ba 52 00 00       	call   4080e8 <_free>
  402e2e:	a1 68 d0 40 00       	mov    eax,ds:0x40d068
  402e33:	8d 65 f4             	lea    esp,[ebp-0xc]
  402e36:	5b                   	pop    ebx
  402e37:	5e                   	pop    esi
  402e38:	5f                   	pop    edi
  402e39:	5d                   	pop    ebp
  402e3a:	c3                   	ret    
  402e3b:	90                   	nop
  402e3c:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  402e40:	89 65 d4             	mov    DWORD PTR [ebp-0x2c],esp
  402e43:	c7 44 24 08 00 00 00 	mov    DWORD PTR [esp+0x8],0x0
  402e4a:	00 
  402e4b:	89 74 24 04          	mov    DWORD PTR [esp+0x4],esi
  402e4f:	c7 04 24 00 00 00 00 	mov    DWORD PTR [esp],0x0
  402e56:	e8 cd 52 00 00       	call   408128 <_mbstowcs>
  402e5b:	89 c2                	mov    edx,eax
  402e5d:	8d 44 00 12          	lea    eax,[eax+eax*1+0x12]
  402e61:	83 e0 f0             	and    eax,0xfffffff0
  402e64:	e8 07 f2 ff ff       	call   402070 <___chkstk_ms>
  402e69:	29 c4                	sub    esp,eax
  402e6b:	8d 44 24 0d          	lea    eax,[esp+0xd]
  402e6f:	89 45 e4             	mov    DWORD PTR [ebp-0x1c],eax
  402e72:	d1 6d e4             	shr    DWORD PTR [ebp-0x1c],1
  402e75:	8b 45 e4             	mov    eax,DWORD PTR [ebp-0x1c]
  402e78:	01 c0                	add    eax,eax
  402e7a:	89 45 e0             	mov    DWORD PTR [ebp-0x20],eax
  402e7d:	89 c7                	mov    edi,eax
  402e7f:	89 54 24 08          	mov    DWORD PTR [esp+0x8],edx
  402e83:	89 74 24 04          	mov    DWORD PTR [esp+0x4],esi
  402e87:	89 04 24             	mov    DWORD PTR [esp],eax
  402e8a:	e8 99 52 00 00       	call   408128 <_mbstowcs>
  402e8f:	31 c9                	xor    ecx,ecx
  402e91:	66 89 0c 47          	mov    WORD PTR [edi+eax*2],cx
  402e95:	83 f8 01             	cmp    eax,0x1
  402e98:	89 45 d0             	mov    DWORD PTR [ebp-0x30],eax
  402e9b:	8b 45 e4             	mov    eax,DWORD PTR [ebp-0x1c]
  402e9e:	0f b7 04 00          	movzx  eax,WORD PTR [eax+eax*1]
  402ea2:	66 89 45 da          	mov    WORD PTR [ebp-0x26],ax
  402ea6:	0f 86 f2 00 00 00    	jbe    402f9e <___mingw_dirname+0x21e>
  402eac:	66 83 f8 5c          	cmp    ax,0x5c
  402eb0:	74 0a                	je     402ebc <___mingw_dirname+0x13c>
  402eb2:	66 83 f8 2f          	cmp    ax,0x2f
  402eb6:	0f 85 0a 01 00 00    	jne    402fc6 <___mingw_dirname+0x246>
  402ebc:	8b 7d e0             	mov    edi,DWORD PTR [ebp-0x20]
  402ebf:	89 7d dc             	mov    DWORD PTR [ebp-0x24],edi
  402ec2:	8b 7d e4             	mov    edi,DWORD PTR [ebp-0x1c]
  402ec5:	66 3b 44 3f 02       	cmp    ax,WORD PTR [edi+edi*1+0x2]
  402eca:	0f 84 4f 02 00 00    	je     40311f <___mingw_dirname+0x39f>
  402ed0:	0f b7 45 da          	movzx  eax,WORD PTR [ebp-0x26]
  402ed4:	66 85 c0             	test   ax,ax
  402ed7:	0f 84 fa 01 00 00    	je     4030d7 <___mingw_dirname+0x357>
  402edd:	8b 55 dc             	mov    edx,DWORD PTR [ebp-0x24]
  402ee0:	89 d7                	mov    edi,edx
  402ee2:	eb 14                	jmp    402ef8 <___mingw_dirname+0x178>
  402ee4:	66 83 f8 2f          	cmp    ax,0x2f
  402ee8:	74 20                	je     402f0a <___mingw_dirname+0x18a>
  402eea:	0f b7 42 02          	movzx  eax,WORD PTR [edx+0x2]
  402eee:	8d 4a 02             	lea    ecx,[edx+0x2]
  402ef1:	66 85 c0             	test   ax,ax
  402ef4:	74 36                	je     402f2c <___mingw_dirname+0x1ac>
  402ef6:	89 ca                	mov    edx,ecx
  402ef8:	66 83 f8 5c          	cmp    ax,0x5c
  402efc:	75 e6                	jne    402ee4 <___mingw_dirname+0x164>
  402efe:	0f b7 02             	movzx  eax,WORD PTR [edx]
  402f01:	66 83 f8 5c          	cmp    ax,0x5c
  402f05:	75 0c                	jne    402f13 <___mingw_dirname+0x193>
  402f07:	83 c2 02             	add    edx,0x2
  402f0a:	0f b7 02             	movzx  eax,WORD PTR [edx]
  402f0d:	66 83 f8 5c          	cmp    ax,0x5c
  402f11:	74 f4                	je     402f07 <___mingw_dirname+0x187>
  402f13:	66 83 f8 2f          	cmp    ax,0x2f
  402f17:	74 ee                	je     402f07 <___mingw_dirname+0x187>
  402f19:	66 85 c0             	test   ax,ax
  402f1c:	74 0e                	je     402f2c <___mingw_dirname+0x1ac>
  402f1e:	0f b7 42 02          	movzx  eax,WORD PTR [edx+0x2]
  402f22:	89 d7                	mov    edi,edx
  402f24:	8d 4a 02             	lea    ecx,[edx+0x2]
  402f27:	66 85 c0             	test   ax,ax
  402f2a:	75 ca                	jne    402ef6 <___mingw_dirname+0x176>
  402f2c:	8b 4d dc             	mov    ecx,DWORD PTR [ebp-0x24]
  402f2f:	39 f9                	cmp    ecx,edi
  402f31:	72 7e                	jb     402fb1 <___mingw_dirname+0x231>
  402f33:	66 83 7d da 5c       	cmp    WORD PTR [ebp-0x26],0x5c
  402f38:	74 0b                	je     402f45 <___mingw_dirname+0x1c5>
  402f3a:	66 83 7d da 2f       	cmp    WORD PTR [ebp-0x26],0x2f
  402f3f:	0f 85 ba 01 00 00    	jne    4030ff <___mingw_dirname+0x37f>
  402f45:	8b 45 dc             	mov    eax,DWORD PTR [ebp-0x24]
  402f48:	83 c0 02             	add    eax,0x2
  402f4b:	31 d2                	xor    edx,edx
  402f4d:	66 89 10             	mov    WORD PTR [eax],dx
  402f50:	c7 44 24 08 00 00 00 	mov    DWORD PTR [esp+0x8],0x0
  402f57:	00 
  402f58:	8b 45 e0             	mov    eax,DWORD PTR [ebp-0x20]
  402f5b:	c7 04 24 00 00 00 00 	mov    DWORD PTR [esp],0x0
  402f62:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
  402f66:	e8 b5 51 00 00       	call   408120 <_wcstombs>
  402f6b:	8d 78 01             	lea    edi,[eax+0x1]
  402f6e:	89 7c 24 04          	mov    DWORD PTR [esp+0x4],edi
  402f72:	a1 68 d0 40 00       	mov    eax,ds:0x40d068
  402f77:	89 04 24             	mov    DWORD PTR [esp],eax
  402f7a:	e8 81 51 00 00       	call   408100 <_realloc>
  402f7f:	a3 68 d0 40 00       	mov    ds:0x40d068,eax
  402f84:	89 c6                	mov    esi,eax
  402f86:	89 7c 24 08          	mov    DWORD PTR [esp+0x8],edi
  402f8a:	8b 45 e0             	mov    eax,DWORD PTR [ebp-0x20]
  402f8d:	89 34 24             	mov    DWORD PTR [esp],esi
  402f90:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
  402f94:	e8 87 51 00 00       	call   408120 <_wcstombs>
  402f99:	e9 e9 00 00 00       	jmp    403087 <___mingw_dirname+0x307>
  402f9e:	8b 45 e0             	mov    eax,DWORD PTR [ebp-0x20]
  402fa1:	89 45 dc             	mov    DWORD PTR [ebp-0x24],eax
  402fa4:	e9 27 ff ff ff       	jmp    402ed0 <___mingw_dirname+0x150>
  402fa9:	66 83 fa 2f          	cmp    dx,0x2f
  402fad:	75 46                	jne    402ff5 <___mingw_dirname+0x275>
  402faf:	89 c7                	mov    edi,eax
  402fb1:	8d 47 fe             	lea    eax,[edi-0x2]
  402fb4:	39 c1                	cmp    ecx,eax
  402fb6:	73 3d                	jae    402ff5 <___mingw_dirname+0x275>
  402fb8:	0f b7 57 fe          	movzx  edx,WORD PTR [edi-0x2]
  402fbc:	66 83 fa 5c          	cmp    dx,0x5c
  402fc0:	75 e7                	jne    402fa9 <___mingw_dirname+0x229>
  402fc2:	89 c7                	mov    edi,eax
  402fc4:	eb eb                	jmp    402fb1 <___mingw_dirname+0x231>
  402fc6:	8b 45 e0             	mov    eax,DWORD PTR [ebp-0x20]
  402fc9:	89 45 dc             	mov    DWORD PTR [ebp-0x24],eax
  402fcc:	8b 45 e4             	mov    eax,DWORD PTR [ebp-0x1c]
  402fcf:	66 83 7c 00 02 3a    	cmp    WORD PTR [eax+eax*1+0x2],0x3a
  402fd5:	0f 85 f5 fe ff ff    	jne    402ed0 <___mingw_dirname+0x150>
  402fdb:	8b 45 e0             	mov    eax,DWORD PTR [ebp-0x20]
  402fde:	83 c0 04             	add    eax,0x4
  402fe1:	89 45 dc             	mov    DWORD PTR [ebp-0x24],eax
  402fe4:	8b 45 e4             	mov    eax,DWORD PTR [ebp-0x1c]
  402fe7:	0f b7 44 00 04       	movzx  eax,WORD PTR [eax+eax*1+0x4]
  402fec:	66 89 45 da          	mov    WORD PTR [ebp-0x26],ax
  402ff0:	e9 db fe ff ff       	jmp    402ed0 <___mingw_dirname+0x150>
  402ff5:	39 45 dc             	cmp    DWORD PTR [ebp-0x24],eax
  402ff8:	0f 84 37 01 00 00    	je     403135 <___mingw_dirname+0x3b5>
  402ffe:	31 d2                	xor    edx,edx
  403000:	66 89 50 02          	mov    WORD PTR [eax+0x2],dx
  403004:	8b 45 e4             	mov    eax,DWORD PTR [ebp-0x1c]
  403007:	0f b7 14 00          	movzx  edx,WORD PTR [eax+eax*1]
  40300b:	8b 45 e0             	mov    eax,DWORD PTR [ebp-0x20]
  40300e:	66 83 fa 5c          	cmp    dx,0x5c
  403012:	0f 85 c7 00 00 00    	jne    4030df <___mingw_dirname+0x35f>
  403018:	83 c0 02             	add    eax,0x2
  40301b:	0f b7 08             	movzx  ecx,WORD PTR [eax]
  40301e:	66 83 f9 5c          	cmp    cx,0x5c
  403022:	74 f4                	je     403018 <___mingw_dirname+0x298>
  403024:	66 83 f9 2f          	cmp    cx,0x2f
  403028:	74 ee                	je     403018 <___mingw_dirname+0x298>
  40302a:	89 c1                	mov    ecx,eax
  40302c:	2b 4d e0             	sub    ecx,DWORD PTR [ebp-0x20]
  40302f:	83 f9 05             	cmp    ecx,0x5
  403032:	0f 8e b1 00 00 00    	jle    4030e9 <___mingw_dirname+0x369>
  403038:	8b 45 e0             	mov    eax,DWORD PTR [ebp-0x20]
  40303b:	89 c1                	mov    ecx,eax
  40303d:	66 85 d2             	test   dx,dx
  403040:	74 21                	je     403063 <___mingw_dirname+0x2e3>
  403042:	83 c1 02             	add    ecx,0x2
  403045:	66 83 fa 2f          	cmp    dx,0x2f
  403049:	66 89 51 fe          	mov    WORD PTR [ecx-0x2],dx
  40304d:	74 63                	je     4030b2 <___mingw_dirname+0x332>
  40304f:	66 83 38 5c          	cmp    WORD PTR [eax],0x5c
  403053:	8d 78 02             	lea    edi,[eax+0x2]
  403056:	74 58                	je     4030b0 <___mingw_dirname+0x330>
  403058:	0f b7 50 02          	movzx  edx,WORD PTR [eax+0x2]
  40305c:	89 f8                	mov    eax,edi
  40305e:	66 85 d2             	test   dx,dx
  403061:	75 df                	jne    403042 <___mingw_dirname+0x2c2>
  403063:	8b 45 d0             	mov    eax,DWORD PTR [ebp-0x30]
  403066:	31 ff                	xor    edi,edi
  403068:	66 89 39             	mov    WORD PTR [ecx],di
  40306b:	89 44 24 08          	mov    DWORD PTR [esp+0x8],eax
  40306f:	8b 45 e0             	mov    eax,DWORD PTR [ebp-0x20]
  403072:	89 34 24             	mov    DWORD PTR [esp],esi
  403075:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
  403079:	e8 a2 50 00 00       	call   408120 <_wcstombs>
  40307e:	83 f8 ff             	cmp    eax,0xffffffff
  403081:	74 04                	je     403087 <___mingw_dirname+0x307>
  403083:	c6 04 06 00          	mov    BYTE PTR [esi+eax*1],0x0
  403087:	89 5c 24 04          	mov    DWORD PTR [esp+0x4],ebx
  40308b:	c7 04 24 02 00 00 00 	mov    DWORD PTR [esp],0x2
  403092:	e8 81 50 00 00       	call   408118 <_setlocale>
  403097:	89 1c 24             	mov    DWORD PTR [esp],ebx
  40309a:	e8 49 50 00 00       	call   4080e8 <_free>
  40309f:	8b 65 d4             	mov    esp,DWORD PTR [ebp-0x2c]
  4030a2:	8d 65 f4             	lea    esp,[ebp-0xc]
  4030a5:	5b                   	pop    ebx
  4030a6:	89 f0                	mov    eax,esi
  4030a8:	5e                   	pop    esi
  4030a9:	5f                   	pop    edi
  4030aa:	5d                   	pop    ebp
  4030ab:	c3                   	ret    
  4030ac:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  4030b0:	89 f8                	mov    eax,edi
  4030b2:	0f b7 10             	movzx  edx,WORD PTR [eax]
  4030b5:	66 83 fa 2f          	cmp    dx,0x2f
  4030b9:	75 59                	jne    403114 <___mingw_dirname+0x394>
  4030bb:	90                   	nop
  4030bc:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  4030c0:	83 c0 02             	add    eax,0x2
  4030c3:	0f b7 10             	movzx  edx,WORD PTR [eax]
  4030c6:	66 83 fa 5c          	cmp    dx,0x5c
  4030ca:	74 f4                	je     4030c0 <___mingw_dirname+0x340>
  4030cc:	66 83 fa 2f          	cmp    dx,0x2f
  4030d0:	74 ee                	je     4030c0 <___mingw_dirname+0x340>
  4030d2:	e9 66 ff ff ff       	jmp    40303d <___mingw_dirname+0x2bd>
  4030d7:	8b 65 d4             	mov    esp,DWORD PTR [ebp-0x2c]
  4030da:	e9 ee fc ff ff       	jmp    402dcd <___mingw_dirname+0x4d>
  4030df:	66 83 fa 2f          	cmp    dx,0x2f
  4030e3:	0f 84 2f ff ff ff    	je     403018 <___mingw_dirname+0x298>
  4030e9:	8b 7d e4             	mov    edi,DWORD PTR [ebp-0x1c]
  4030ec:	66 39 54 3f 02       	cmp    WORD PTR [edi+edi*1+0x2],dx
  4030f1:	0f 85 41 ff ff ff    	jne    403038 <___mingw_dirname+0x2b8>
  4030f7:	0f b7 10             	movzx  edx,WORD PTR [eax]
  4030fa:	e9 3c ff ff ff       	jmp    40303b <___mingw_dirname+0x2bb>
  4030ff:	8b 7d dc             	mov    edi,DWORD PTR [ebp-0x24]
  403102:	b9 2e 00 00 00       	mov    ecx,0x2e
  403107:	89 f8                	mov    eax,edi
  403109:	83 c0 02             	add    eax,0x2
  40310c:	66 89 0f             	mov    WORD PTR [edi],cx
  40310f:	e9 37 fe ff ff       	jmp    402f4b <___mingw_dirname+0x1cb>
  403114:	66 83 fa 5c          	cmp    dx,0x5c
  403118:	74 a6                	je     4030c0 <___mingw_dirname+0x340>
  40311a:	e9 1e ff ff ff       	jmp    40303d <___mingw_dirname+0x2bd>
  40311f:	66 83 7c 3f 04 00    	cmp    WORD PTR [edi+edi*1+0x4],0x0
  403125:	0f 85 a5 fd ff ff    	jne    402ed0 <___mingw_dirname+0x150>
  40312b:	90                   	nop
  40312c:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  403130:	e9 52 ff ff ff       	jmp    403087 <___mingw_dirname+0x307>
  403135:	66 83 7d da 5c       	cmp    WORD PTR [ebp-0x26],0x5c
  40313a:	74 0e                	je     40314a <___mingw_dirname+0x3ca>
  40313c:	66 83 7d da 2f       	cmp    WORD PTR [ebp-0x26],0x2f
  403141:	8b 45 dc             	mov    eax,DWORD PTR [ebp-0x24]
  403144:	0f 85 b4 fe ff ff    	jne    402ffe <___mingw_dirname+0x27e>
  40314a:	8b 45 dc             	mov    eax,DWORD PTR [ebp-0x24]
  40314d:	0f b7 4d da          	movzx  ecx,WORD PTR [ebp-0x26]
  403151:	66 39 48 02          	cmp    WORD PTR [eax+0x2],cx
  403155:	0f 85 a3 fe ff ff    	jne    402ffe <___mingw_dirname+0x27e>
  40315b:	0f b7 50 04          	movzx  edx,WORD PTR [eax+0x4]
  40315f:	66 83 fa 2f          	cmp    dx,0x2f
  403163:	0f 84 95 fe ff ff    	je     402ffe <___mingw_dirname+0x27e>
  403169:	66 83 fa 5c          	cmp    dx,0x5c
  40316d:	89 f8                	mov    eax,edi
  40316f:	0f 85 89 fe ff ff    	jne    402ffe <___mingw_dirname+0x27e>
  403175:	8b 45 dc             	mov    eax,DWORD PTR [ebp-0x24]
  403178:	e9 81 fe ff ff       	jmp    402ffe <___mingw_dirname+0x27e>
  40317d:	90                   	nop
  40317e:	90                   	nop
  40317f:	90                   	nop

00403180 <_dirent_findnext>:
  403180:	55                   	push   ebp
  403181:	89 e5                	mov    ebp,esp
  403183:	56                   	push   esi
  403184:	89 d6                	mov    esi,edx
  403186:	53                   	push   ebx
  403187:	81 ec 50 01 00 00    	sub    esp,0x150
  40318d:	8d 95 b8 fe ff ff    	lea    edx,[ebp-0x148]
  403193:	89 54 24 04          	mov    DWORD PTR [esp+0x4],edx
  403197:	89 04 24             	mov    DWORD PTR [esp],eax
  40319a:	e8 31 50 00 00       	call   4081d0 <_FindNextFileA@8>
  40319f:	83 ec 08             	sub    esp,0x8
  4031a2:	85 c0                	test   eax,eax
  4031a4:	89 c3                	mov    ebx,eax
  4031a6:	75 20                	jne    4031c8 <_dirent_findnext+0x48>
  4031a8:	e8 03 50 00 00       	call   4081b0 <_GetLastError@0>
  4031ad:	31 db                	xor    ebx,ebx
  4031af:	83 f8 12             	cmp    eax,0x12
  4031b2:	74 0b                	je     4031bf <_dirent_findnext+0x3f>
  4031b4:	e8 57 4f 00 00       	call   408110 <__errno>
  4031b9:	c7 00 02 00 00 00    	mov    DWORD PTR [eax],0x2
  4031bf:	8d 65 f8             	lea    esp,[ebp-0x8]
  4031c2:	89 d8                	mov    eax,ebx
  4031c4:	5b                   	pop    ebx
  4031c5:	5e                   	pop    esi
  4031c6:	5d                   	pop    ebp
  4031c7:	c3                   	ret    
  4031c8:	8d 85 e4 fe ff ff    	lea    eax,[ebp-0x11c]
  4031ce:	89 44 24 0c          	mov    DWORD PTR [esp+0xc],eax
  4031d2:	8d 46 0c             	lea    eax,[esi+0xc]
  4031d5:	c7 44 24 08 4c a1 40 	mov    DWORD PTR [esp+0x8],0x40a14c
  4031dc:	00 
  4031dd:	c7 44 24 04 04 01 00 	mov    DWORD PTR [esp+0x4],0x104
  4031e4:	00 
  4031e5:	89 04 24             	mov    DWORD PTR [esp],eax
  4031e8:	e8 43 04 00 00       	call   403630 <___mingw_snprintf>
  4031ed:	66 89 46 06          	mov    WORD PTR [esi+0x6],ax
  4031f1:	8b 85 b8 fe ff ff    	mov    eax,DWORD PTR [ebp-0x148]
  4031f7:	24 58                	and    al,0x58
  4031f9:	83 f8 10             	cmp    eax,0x10
  4031fc:	76 12                	jbe    403210 <_dirent_findnext+0x90>
  4031fe:	c7 46 08 18 00 00 00 	mov    DWORD PTR [esi+0x8],0x18
  403205:	8d 65 f8             	lea    esp,[ebp-0x8]
  403208:	89 d8                	mov    eax,ebx
  40320a:	5b                   	pop    ebx
  40320b:	5e                   	pop    esi
  40320c:	5d                   	pop    ebp
  40320d:	c3                   	ret    
  40320e:	66 90                	xchg   ax,ax
  403210:	89 46 08             	mov    DWORD PTR [esi+0x8],eax
  403213:	8d 65 f8             	lea    esp,[ebp-0x8]
  403216:	89 d8                	mov    eax,ebx
  403218:	5b                   	pop    ebx
  403219:	5e                   	pop    esi
  40321a:	5d                   	pop    ebp
  40321b:	c3                   	ret    
  40321c:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]

00403220 <_dirent_findfirst>:
  403220:	55                   	push   ebp
  403221:	89 e5                	mov    ebp,esp
  403223:	56                   	push   esi
  403224:	53                   	push   ebx
  403225:	89 d3                	mov    ebx,edx
  403227:	81 ec 50 01 00 00    	sub    esp,0x150
  40322d:	8d 95 b8 fe ff ff    	lea    edx,[ebp-0x148]
  403233:	89 54 24 04          	mov    DWORD PTR [esp+0x4],edx
  403237:	89 04 24             	mov    DWORD PTR [esp],eax
  40323a:	e8 99 4f 00 00       	call   4081d8 <_FindFirstFileA@8>
  40323f:	83 ec 08             	sub    esp,0x8
  403242:	83 f8 ff             	cmp    eax,0xffffffff
  403245:	89 c6                	mov    esi,eax
  403247:	74 4a                	je     403293 <_dirent_findfirst+0x73>
  403249:	8d 85 e4 fe ff ff    	lea    eax,[ebp-0x11c]
  40324f:	89 44 24 0c          	mov    DWORD PTR [esp+0xc],eax
  403253:	8d 43 0c             	lea    eax,[ebx+0xc]
  403256:	c7 44 24 08 4c a1 40 	mov    DWORD PTR [esp+0x8],0x40a14c
  40325d:	00 
  40325e:	c7 44 24 04 04 01 00 	mov    DWORD PTR [esp+0x4],0x104
  403265:	00 
  403266:	89 04 24             	mov    DWORD PTR [esp],eax
  403269:	e8 c2 03 00 00       	call   403630 <___mingw_snprintf>
  40326e:	8b 8d b8 fe ff ff    	mov    ecx,DWORD PTR [ebp-0x148]
  403274:	80 e1 58             	and    cl,0x58
  403277:	83 f9 10             	cmp    ecx,0x10
  40327a:	66 89 43 06          	mov    WORD PTR [ebx+0x6],ax
  40327e:	89 4b 08             	mov    DWORD PTR [ebx+0x8],ecx
  403281:	76 07                	jbe    40328a <_dirent_findfirst+0x6a>
  403283:	c7 43 08 18 00 00 00 	mov    DWORD PTR [ebx+0x8],0x18
  40328a:	8d 65 f8             	lea    esp,[ebp-0x8]
  40328d:	89 f0                	mov    eax,esi
  40328f:	5b                   	pop    ebx
  403290:	5e                   	pop    esi
  403291:	5d                   	pop    ebp
  403292:	c3                   	ret    
  403293:	e8 78 4e 00 00       	call   408110 <__errno>
  403298:	89 c3                	mov    ebx,eax
  40329a:	e8 11 4f 00 00       	call   4081b0 <_GetLastError@0>
  40329f:	83 f8 03             	cmp    eax,0x3
  4032a2:	89 03                	mov    DWORD PTR [ebx],eax
  4032a4:	74 2a                	je     4032d0 <_dirent_findfirst+0xb0>
  4032a6:	e8 65 4e 00 00       	call   408110 <__errno>
  4032ab:	81 38 0b 01 00 00    	cmp    DWORD PTR [eax],0x10b
  4032b1:	74 2d                	je     4032e0 <_dirent_findfirst+0xc0>
  4032b3:	e8 58 4e 00 00       	call   408110 <__errno>
  4032b8:	83 38 02             	cmp    DWORD PTR [eax],0x2
  4032bb:	74 cd                	je     40328a <_dirent_findfirst+0x6a>
  4032bd:	8d 76 00             	lea    esi,[esi+0x0]
  4032c0:	e8 4b 4e 00 00       	call   408110 <__errno>
  4032c5:	c7 00 16 00 00 00    	mov    DWORD PTR [eax],0x16
  4032cb:	eb bd                	jmp    40328a <_dirent_findfirst+0x6a>
  4032cd:	8d 76 00             	lea    esi,[esi+0x0]
  4032d0:	e8 3b 4e 00 00       	call   408110 <__errno>
  4032d5:	c7 00 02 00 00 00    	mov    DWORD PTR [eax],0x2
  4032db:	eb ad                	jmp    40328a <_dirent_findfirst+0x6a>
  4032dd:	8d 76 00             	lea    esi,[esi+0x0]
  4032e0:	e8 2b 4e 00 00       	call   408110 <__errno>
  4032e5:	c7 00 14 00 00 00    	mov    DWORD PTR [eax],0x14
  4032eb:	eb 9d                	jmp    40328a <_dirent_findfirst+0x6a>
  4032ed:	8d 76 00             	lea    esi,[esi+0x0]

004032f0 <___mingw_opendir>:
  4032f0:	55                   	push   ebp
  4032f1:	57                   	push   edi
  4032f2:	56                   	push   esi
  4032f3:	53                   	push   ebx
  4032f4:	81 ec 2c 01 00 00    	sub    esp,0x12c
  4032fa:	8b 84 24 40 01 00 00 	mov    eax,DWORD PTR [esp+0x140]
  403301:	85 c0                	test   eax,eax
  403303:	0f 84 67 01 00 00    	je     403470 <___mingw_opendir+0x180>
  403309:	80 38 00             	cmp    BYTE PTR [eax],0x0
  40330c:	0f 84 40 01 00 00    	je     403452 <___mingw_opendir+0x162>
  403312:	8d 7c 24 1c          	lea    edi,[esp+0x1c]
  403316:	c7 44 24 08 04 01 00 	mov    DWORD PTR [esp+0x8],0x104
  40331d:	00 
  40331e:	89 fb                	mov    ebx,edi
  403320:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
  403324:	89 3c 24             	mov    DWORD PTR [esp],edi
  403327:	e8 04 4e 00 00       	call   408130 <__fullpath>
  40332c:	80 7c 24 1c 00       	cmp    BYTE PTR [esp+0x1c],0x0
  403331:	74 5d                	je     403390 <___mingw_opendir+0xa0>
  403333:	8b 13                	mov    edx,DWORD PTR [ebx]
  403335:	83 c3 04             	add    ebx,0x4
  403338:	8d 82 ff fe fe fe    	lea    eax,[edx-0x1010101]
  40333e:	f7 d2                	not    edx
  403340:	21 d0                	and    eax,edx
  403342:	25 80 80 80 80       	and    eax,0x80808080
  403347:	74 ea                	je     403333 <___mingw_opendir+0x43>
  403349:	a9 80 80 00 00       	test   eax,0x8080
  40334e:	0f 84 df 00 00 00    	je     403433 <___mingw_opendir+0x143>
  403354:	00 c0                	add    al,al
  403356:	83 db 03             	sbb    ebx,0x3
  403359:	29 fb                	sub    ebx,edi
  40335b:	0f b6 44 1c 1b       	movzx  eax,BYTE PTR [esp+ebx*1+0x1b]
  403360:	3c 5c                	cmp    al,0x5c
  403362:	74 50                	je     4033b4 <___mingw_opendir+0xc4>
  403364:	3c 2f                	cmp    al,0x2f
  403366:	74 4c                	je     4033b4 <___mingw_opendir+0xc4>
  403368:	b9 5c 00 00 00       	mov    ecx,0x5c
  40336d:	66 89 0c 1f          	mov    WORD PTR [edi+ebx*1],cx
  403371:	89 fb                	mov    ebx,edi
  403373:	8b 13                	mov    edx,DWORD PTR [ebx]
  403375:	83 c3 04             	add    ebx,0x4
  403378:	8d 82 ff fe fe fe    	lea    eax,[edx-0x1010101]
  40337e:	f7 d2                	not    edx
  403380:	21 d0                	and    eax,edx
  403382:	25 80 80 80 80       	and    eax,0x80808080
  403387:	74 ea                	je     403373 <___mingw_opendir+0x83>
  403389:	eb 1b                	jmp    4033a6 <___mingw_opendir+0xb6>
  40338b:	90                   	nop
  40338c:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  403390:	8b 13                	mov    edx,DWORD PTR [ebx]
  403392:	83 c3 04             	add    ebx,0x4
  403395:	8d 82 ff fe fe fe    	lea    eax,[edx-0x1010101]
  40339b:	f7 d2                	not    edx
  40339d:	21 d0                	and    eax,edx
  40339f:	25 80 80 80 80       	and    eax,0x80808080
  4033a4:	74 ea                	je     403390 <___mingw_opendir+0xa0>
  4033a6:	a9 80 80 00 00       	test   eax,0x8080
  4033ab:	74 7b                	je     403428 <___mingw_opendir+0x138>
  4033ad:	00 c0                	add    al,al
  4033af:	83 db 03             	sbb    ebx,0x3
  4033b2:	29 fb                	sub    ebx,edi
  4033b4:	ba 2a 00 00 00       	mov    edx,0x2a
  4033b9:	8d 83 1d 01 00 00    	lea    eax,[ebx+0x11d]
  4033bf:	66 89 14 1f          	mov    WORD PTR [edi+ebx*1],dx
  4033c3:	89 04 24             	mov    DWORD PTR [esp],eax
  4033c6:	e8 25 4d 00 00       	call   4080f0 <_malloc>
  4033cb:	85 c0                	test   eax,eax
  4033cd:	89 c6                	mov    esi,eax
  4033cf:	0f 84 8c 00 00 00    	je     403461 <___mingw_opendir+0x171>
  4033d5:	8d a8 18 01 00 00    	lea    ebp,[eax+0x118]
  4033db:	83 c3 02             	add    ebx,0x2
  4033de:	89 5c 24 08          	mov    DWORD PTR [esp+0x8],ebx
  4033e2:	89 7c 24 04          	mov    DWORD PTR [esp+0x4],edi
  4033e6:	89 2c 24             	mov    DWORD PTR [esp],ebp
  4033e9:	e8 ea 4c 00 00       	call   4080d8 <_memcpy>
  4033ee:	89 f2                	mov    edx,esi
  4033f0:	89 e8                	mov    eax,ebp
  4033f2:	e8 29 fe ff ff       	call   403220 <_dirent_findfirst>
  4033f7:	83 f8 ff             	cmp    eax,0xffffffff
  4033fa:	89 86 10 01 00 00    	mov    DWORD PTR [esi+0x110],eax
  403400:	74 7d                	je     40347f <___mingw_opendir+0x18f>
  403402:	b8 10 01 00 00       	mov    eax,0x110
  403407:	66 89 46 04          	mov    WORD PTR [esi+0x4],ax
  40340b:	89 f0                	mov    eax,esi
  40340d:	c7 86 14 01 00 00 00 	mov    DWORD PTR [esi+0x114],0x0
  403414:	00 00 00 
  403417:	c7 06 00 00 00 00    	mov    DWORD PTR [esi],0x0
  40341d:	81 c4 2c 01 00 00    	add    esp,0x12c
  403423:	5b                   	pop    ebx
  403424:	5e                   	pop    esi
  403425:	5f                   	pop    edi
  403426:	5d                   	pop    ebp
  403427:	c3                   	ret    
  403428:	c1 e8 10             	shr    eax,0x10
  40342b:	83 c3 02             	add    ebx,0x2
  40342e:	e9 7a ff ff ff       	jmp    4033ad <___mingw_opendir+0xbd>
  403433:	c1 e8 10             	shr    eax,0x10
  403436:	83 c3 02             	add    ebx,0x2
  403439:	00 c0                	add    al,al
  40343b:	83 db 03             	sbb    ebx,0x3
  40343e:	29 fb                	sub    ebx,edi
  403440:	0f b6 44 1c 1b       	movzx  eax,BYTE PTR [esp+ebx*1+0x1b]
  403445:	3c 5c                	cmp    al,0x5c
  403447:	0f 84 67 ff ff ff    	je     4033b4 <___mingw_opendir+0xc4>
  40344d:	e9 12 ff ff ff       	jmp    403364 <___mingw_opendir+0x74>
  403452:	e8 b9 4c 00 00       	call   408110 <__errno>
  403457:	c7 00 02 00 00 00    	mov    DWORD PTR [eax],0x2
  40345d:	31 c0                	xor    eax,eax
  40345f:	eb bc                	jmp    40341d <___mingw_opendir+0x12d>
  403461:	e8 aa 4c 00 00       	call   408110 <__errno>
  403466:	c7 00 0c 00 00 00    	mov    DWORD PTR [eax],0xc
  40346c:	31 c0                	xor    eax,eax
  40346e:	eb ad                	jmp    40341d <___mingw_opendir+0x12d>
  403470:	e8 9b 4c 00 00       	call   408110 <__errno>
  403475:	c7 00 16 00 00 00    	mov    DWORD PTR [eax],0x16
  40347b:	31 c0                	xor    eax,eax
  40347d:	eb 9e                	jmp    40341d <___mingw_opendir+0x12d>
  40347f:	89 34 24             	mov    DWORD PTR [esp],esi
  403482:	e8 61 4c 00 00       	call   4080e8 <_free>
  403487:	31 c0                	xor    eax,eax
  403489:	eb 92                	jmp    40341d <___mingw_opendir+0x12d>
  40348b:	90                   	nop
  40348c:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]

00403490 <___mingw_readdir>:
  403490:	53                   	push   ebx
  403491:	83 ec 08             	sub    esp,0x8
  403494:	8b 5c 24 10          	mov    ebx,DWORD PTR [esp+0x10]
  403498:	85 db                	test   ebx,ebx
  40349a:	74 2b                	je     4034c7 <___mingw_readdir+0x37>
  40349c:	8b 83 14 01 00 00    	mov    eax,DWORD PTR [ebx+0x114]
  4034a2:	8d 50 01             	lea    edx,[eax+0x1]
  4034a5:	85 c0                	test   eax,eax
  4034a7:	89 93 14 01 00 00    	mov    DWORD PTR [ebx+0x114],edx
  4034ad:	7e 11                	jle    4034c0 <___mingw_readdir+0x30>
  4034af:	8b 83 10 01 00 00    	mov    eax,DWORD PTR [ebx+0x110]
  4034b5:	89 da                	mov    edx,ebx
  4034b7:	e8 c4 fc ff ff       	call   403180 <_dirent_findnext>
  4034bc:	85 c0                	test   eax,eax
  4034be:	74 02                	je     4034c2 <___mingw_readdir+0x32>
  4034c0:	89 d8                	mov    eax,ebx
  4034c2:	83 c4 08             	add    esp,0x8
  4034c5:	5b                   	pop    ebx
  4034c6:	c3                   	ret    
  4034c7:	e8 44 4c 00 00       	call   408110 <__errno>
  4034cc:	c7 00 09 00 00 00    	mov    DWORD PTR [eax],0x9
  4034d2:	31 c0                	xor    eax,eax
  4034d4:	eb ec                	jmp    4034c2 <___mingw_readdir+0x32>
  4034d6:	8d 76 00             	lea    esi,[esi+0x0]
  4034d9:	8d bc 27 00 00 00 00 	lea    edi,[edi+eiz*1+0x0]

004034e0 <___mingw_closedir>:
  4034e0:	55                   	push   ebp
  4034e1:	89 e5                	mov    ebp,esp
  4034e3:	53                   	push   ebx
  4034e4:	83 ec 14             	sub    esp,0x14
  4034e7:	8b 5d 08             	mov    ebx,DWORD PTR [ebp+0x8]
  4034ea:	85 db                	test   ebx,ebx
  4034ec:	74 24                	je     403512 <___mingw_closedir+0x32>
  4034ee:	8b 83 10 01 00 00    	mov    eax,DWORD PTR [ebx+0x110]
  4034f4:	89 04 24             	mov    DWORD PTR [esp],eax
  4034f7:	e8 e4 4c 00 00       	call   4081e0 <_FindClose@4>
  4034fc:	83 ec 04             	sub    esp,0x4
  4034ff:	85 c0                	test   eax,eax
  403501:	74 0f                	je     403512 <___mingw_closedir+0x32>
  403503:	89 1c 24             	mov    DWORD PTR [esp],ebx
  403506:	e8 dd 4b 00 00       	call   4080e8 <_free>
  40350b:	31 c0                	xor    eax,eax
  40350d:	8b 5d fc             	mov    ebx,DWORD PTR [ebp-0x4]
  403510:	c9                   	leave  
  403511:	c3                   	ret    
  403512:	e8 f9 4b 00 00       	call   408110 <__errno>
  403517:	c7 00 09 00 00 00    	mov    DWORD PTR [eax],0x9
  40351d:	b8 ff ff ff ff       	mov    eax,0xffffffff
  403522:	eb e9                	jmp    40350d <___mingw_closedir+0x2d>
  403524:	8d b6 00 00 00 00    	lea    esi,[esi+0x0]
  40352a:	8d bf 00 00 00 00    	lea    edi,[edi+0x0]

00403530 <___mingw_rewinddir>:
  403530:	55                   	push   ebp
  403531:	89 e5                	mov    ebp,esp
  403533:	53                   	push   ebx
  403534:	83 ec 14             	sub    esp,0x14
  403537:	8b 5d 08             	mov    ebx,DWORD PTR [ebp+0x8]
  40353a:	85 db                	test   ebx,ebx
  40353c:	74 15                	je     403553 <___mingw_rewinddir+0x23>
  40353e:	8b 83 10 01 00 00    	mov    eax,DWORD PTR [ebx+0x110]
  403544:	89 04 24             	mov    DWORD PTR [esp],eax
  403547:	e8 94 4c 00 00       	call   4081e0 <_FindClose@4>
  40354c:	83 ec 04             	sub    esp,0x4
  40354f:	85 c0                	test   eax,eax
  403551:	75 10                	jne    403563 <___mingw_rewinddir+0x33>
  403553:	e8 b8 4b 00 00       	call   408110 <__errno>
  403558:	c7 00 09 00 00 00    	mov    DWORD PTR [eax],0x9
  40355e:	8b 5d fc             	mov    ebx,DWORD PTR [ebp-0x4]
  403561:	c9                   	leave  
  403562:	c3                   	ret    
  403563:	8d 83 18 01 00 00    	lea    eax,[ebx+0x118]
  403569:	89 da                	mov    edx,ebx
  40356b:	e8 b0 fc ff ff       	call   403220 <_dirent_findfirst>
  403570:	83 f8 ff             	cmp    eax,0xffffffff
  403573:	89 83 10 01 00 00    	mov    DWORD PTR [ebx+0x110],eax
  403579:	74 e3                	je     40355e <___mingw_rewinddir+0x2e>
  40357b:	c7 83 14 01 00 00 00 	mov    DWORD PTR [ebx+0x114],0x0
  403582:	00 00 00 
  403585:	8b 5d fc             	mov    ebx,DWORD PTR [ebp-0x4]
  403588:	c9                   	leave  
  403589:	c3                   	ret    
  40358a:	8d b6 00 00 00 00    	lea    esi,[esi+0x0]

00403590 <___mingw_telldir>:
  403590:	83 ec 0c             	sub    esp,0xc
  403593:	8b 44 24 10          	mov    eax,DWORD PTR [esp+0x10]
  403597:	85 c0                	test   eax,eax
  403599:	74 0a                	je     4035a5 <___mingw_telldir+0x15>
  40359b:	8b 80 14 01 00 00    	mov    eax,DWORD PTR [eax+0x114]
  4035a1:	83 c4 0c             	add    esp,0xc
  4035a4:	c3                   	ret    
  4035a5:	e8 66 4b 00 00       	call   408110 <__errno>
  4035aa:	c7 00 09 00 00 00    	mov    DWORD PTR [eax],0x9
  4035b0:	b8 ff ff ff ff       	mov    eax,0xffffffff
  4035b5:	eb ea                	jmp    4035a1 <___mingw_telldir+0x11>
  4035b7:	89 f6                	mov    esi,esi
  4035b9:	8d bc 27 00 00 00 00 	lea    edi,[edi+eiz*1+0x0]

004035c0 <___mingw_seekdir>:
  4035c0:	56                   	push   esi
  4035c1:	53                   	push   ebx
  4035c2:	83 ec 14             	sub    esp,0x14
  4035c5:	8b 74 24 24          	mov    esi,DWORD PTR [esp+0x24]
  4035c9:	8b 5c 24 20          	mov    ebx,DWORD PTR [esp+0x20]
  4035cd:	85 f6                	test   esi,esi
  4035cf:	78 41                	js     403612 <___mingw_seekdir+0x52>
  4035d1:	89 1c 24             	mov    DWORD PTR [esp],ebx
  4035d4:	e8 57 ff ff ff       	call   403530 <___mingw_rewinddir>
  4035d9:	85 f6                	test   esi,esi
  4035db:	74 2f                	je     40360c <___mingw_seekdir+0x4c>
  4035dd:	83 bb 10 01 00 00 ff 	cmp    DWORD PTR [ebx+0x110],0xffffffff
  4035e4:	75 13                	jne    4035f9 <___mingw_seekdir+0x39>
  4035e6:	eb 24                	jmp    40360c <___mingw_seekdir+0x4c>
  4035e8:	8b 83 10 01 00 00    	mov    eax,DWORD PTR [ebx+0x110]
  4035ee:	89 da                	mov    edx,ebx
  4035f0:	e8 8b fb ff ff       	call   403180 <_dirent_findnext>
  4035f5:	85 c0                	test   eax,eax
  4035f7:	74 13                	je     40360c <___mingw_seekdir+0x4c>
  4035f9:	8b 83 14 01 00 00    	mov    eax,DWORD PTR [ebx+0x114]
  4035ff:	83 c0 01             	add    eax,0x1
  403602:	39 c6                	cmp    esi,eax
  403604:	89 83 14 01 00 00    	mov    DWORD PTR [ebx+0x114],eax
  40360a:	7f dc                	jg     4035e8 <___mingw_seekdir+0x28>
  40360c:	83 c4 14             	add    esp,0x14
  40360f:	5b                   	pop    ebx
  403610:	5e                   	pop    esi
  403611:	c3                   	ret    
  403612:	e8 f9 4a 00 00       	call   408110 <__errno>
  403617:	c7 00 16 00 00 00    	mov    DWORD PTR [eax],0x16
  40361d:	83 c4 14             	add    esp,0x14
  403620:	5b                   	pop    ebx
  403621:	5e                   	pop    esi
  403622:	c3                   	ret    
  403623:	90                   	nop
  403624:	90                   	nop
  403625:	90                   	nop
  403626:	90                   	nop
  403627:	90                   	nop
  403628:	90                   	nop
  403629:	90                   	nop
  40362a:	90                   	nop
  40362b:	90                   	nop
  40362c:	90                   	nop
  40362d:	90                   	nop
  40362e:	90                   	nop
  40362f:	90                   	nop

00403630 <___mingw_snprintf>:
  403630:	83 ec 1c             	sub    esp,0x1c
  403633:	8d 44 24 2c          	lea    eax,[esp+0x2c]
  403637:	89 44 24 0c          	mov    DWORD PTR [esp+0xc],eax
  40363b:	8b 44 24 28          	mov    eax,DWORD PTR [esp+0x28]
  40363f:	89 44 24 08          	mov    DWORD PTR [esp+0x8],eax
  403643:	8b 44 24 24          	mov    eax,DWORD PTR [esp+0x24]
  403647:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
  40364b:	8b 44 24 20          	mov    eax,DWORD PTR [esp+0x20]
  40364f:	89 04 24             	mov    DWORD PTR [esp],eax
  403652:	e8 09 00 00 00       	call   403660 <___mingw_vsnprintf>
  403657:	83 c4 1c             	add    esp,0x1c
  40365a:	c3                   	ret    
  40365b:	90                   	nop
  40365c:	90                   	nop
  40365d:	90                   	nop
  40365e:	90                   	nop
  40365f:	90                   	nop

00403660 <___mingw_vsnprintf>:
  403660:	56                   	push   esi
  403661:	53                   	push   ebx
  403662:	83 ec 24             	sub    esp,0x24
  403665:	8b 44 24 34          	mov    eax,DWORD PTR [esp+0x34]
  403669:	8b 5c 24 30          	mov    ebx,DWORD PTR [esp+0x30]
  40366d:	8b 54 24 38          	mov    edx,DWORD PTR [esp+0x38]
  403671:	8b 4c 24 3c          	mov    ecx,DWORD PTR [esp+0x3c]
  403675:	85 c0                	test   eax,eax
  403677:	74 37                	je     4036b0 <___mingw_vsnprintf+0x50>
  403679:	8d 70 ff             	lea    esi,[eax-0x1]
  40367c:	89 54 24 0c          	mov    DWORD PTR [esp+0xc],edx
  403680:	89 4c 24 10          	mov    DWORD PTR [esp+0x10],ecx
  403684:	89 74 24 08          	mov    DWORD PTR [esp+0x8],esi
  403688:	89 5c 24 04          	mov    DWORD PTR [esp+0x4],ebx
  40368c:	c7 04 24 00 00 00 00 	mov    DWORD PTR [esp],0x0
  403693:	e8 e8 15 00 00       	call   404c80 <___mingw_pformat>
  403698:	39 f0                	cmp    eax,esi
  40369a:	89 c2                	mov    edx,eax
  40369c:	77 0a                	ja     4036a8 <___mingw_vsnprintf+0x48>
  40369e:	c6 04 13 00          	mov    BYTE PTR [ebx+edx*1],0x0
  4036a2:	83 c4 24             	add    esp,0x24
  4036a5:	5b                   	pop    ebx
  4036a6:	5e                   	pop    esi
  4036a7:	c3                   	ret    
  4036a8:	89 f2                	mov    edx,esi
  4036aa:	eb f2                	jmp    40369e <___mingw_vsnprintf+0x3e>
  4036ac:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  4036b0:	89 5c 24 04          	mov    DWORD PTR [esp+0x4],ebx
  4036b4:	89 4c 24 10          	mov    DWORD PTR [esp+0x10],ecx
  4036b8:	89 54 24 0c          	mov    DWORD PTR [esp+0xc],edx
  4036bc:	c7 44 24 08 00 00 00 	mov    DWORD PTR [esp+0x8],0x0
  4036c3:	00 
  4036c4:	c7 04 24 00 00 00 00 	mov    DWORD PTR [esp],0x0
  4036cb:	e8 b0 15 00 00       	call   404c80 <___mingw_pformat>
  4036d0:	83 c4 24             	add    esp,0x24
  4036d3:	5b                   	pop    ebx
  4036d4:	5e                   	pop    esi
  4036d5:	c3                   	ret    
  4036d6:	90                   	nop
  4036d7:	90                   	nop
  4036d8:	90                   	nop
  4036d9:	90                   	nop
  4036da:	90                   	nop
  4036db:	90                   	nop
  4036dc:	90                   	nop
  4036dd:	90                   	nop
  4036de:	90                   	nop
  4036df:	90                   	nop

004036e0 <___pformat_cvt>:
  4036e0:	53                   	push   ebx
  4036e1:	89 c1                	mov    ecx,eax
  4036e3:	83 ec 48             	sub    esp,0x48
  4036e6:	8b 44 24 50          	mov    eax,DWORD PTR [esp+0x50]
  4036ea:	89 44 24 20          	mov    DWORD PTR [esp+0x20],eax
  4036ee:	8b 44 24 54          	mov    eax,DWORD PTR [esp+0x54]
  4036f2:	89 44 24 24          	mov    DWORD PTR [esp+0x24],eax
  4036f6:	8b 44 24 58          	mov    eax,DWORD PTR [esp+0x58]
  4036fa:	89 44 24 28          	mov    DWORD PTR [esp+0x28],eax
  4036fe:	8b 44 24 5c          	mov    eax,DWORD PTR [esp+0x5c]
  403702:	db 6c 24 20          	fld    TBYTE PTR [esp+0x20]
  403706:	89 44 24 2c          	mov    DWORD PTR [esp+0x2c],eax
  40370a:	d9 e5                	fxam   
  40370c:	9b df e0             	fstsw  ax
  40370f:	dd d8                	fstp   st(0)
  403711:	f6 c4 01             	test   ah,0x1
  403714:	74 1a                	je     403730 <___pformat_cvt+0x50>
  403716:	f6 c4 04             	test   ah,0x4
  403719:	0f 84 91 00 00 00    	je     4037b0 <___pformat_cvt+0xd0>
  40371f:	c7 44 24 38 03 00 00 	mov    DWORD PTR [esp+0x38],0x3
  403726:	00 
  403727:	0f b7 54 24 28       	movzx  edx,WORD PTR [esp+0x28]
  40372c:	31 c0                	xor    eax,eax
  40372e:	eb 14                	jmp    403744 <___pformat_cvt+0x64>
  403730:	f6 c4 04             	test   ah,0x4
  403733:	75 5c                	jne    403791 <___pformat_cvt+0xb1>
  403735:	0f b7 54 24 28       	movzx  edx,WORD PTR [esp+0x28]
  40373a:	31 c0                	xor    eax,eax
  40373c:	c7 44 24 38 00 00 00 	mov    DWORD PTR [esp+0x38],0x0
  403743:	00 
  403744:	81 e2 00 80 00 00    	and    edx,0x8000
  40374a:	8b 5c 24 68          	mov    ebx,DWORD PTR [esp+0x68]
  40374e:	89 13                	mov    DWORD PTR [ebx],edx
  403750:	8d 54 24 3c          	lea    edx,[esp+0x3c]
  403754:	89 54 24 1c          	mov    DWORD PTR [esp+0x1c],edx
  403758:	8b 54 24 64          	mov    edx,DWORD PTR [esp+0x64]
  40375c:	89 4c 24 10          	mov    DWORD PTR [esp+0x10],ecx
  403760:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
  403764:	c7 04 24 0c 90 40 00 	mov    DWORD PTR [esp],0x40900c
  40376b:	89 54 24 18          	mov    DWORD PTR [esp+0x18],edx
  40376f:	8b 54 24 60          	mov    edx,DWORD PTR [esp+0x60]
  403773:	89 54 24 14          	mov    DWORD PTR [esp+0x14],edx
  403777:	8d 54 24 38          	lea    edx,[esp+0x38]
  40377b:	89 54 24 0c          	mov    DWORD PTR [esp+0xc],edx
  40377f:	8d 54 24 20          	lea    edx,[esp+0x20]
  403783:	89 54 24 08          	mov    DWORD PTR [esp+0x8],edx
  403787:	e8 64 1e 00 00       	call   4055f0 <___gdtoa>
  40378c:	83 c4 48             	add    esp,0x48
  40378f:	5b                   	pop    ebx
  403790:	c3                   	ret    
  403791:	f6 c4 40             	test   ah,0x40
  403794:	74 2a                	je     4037c0 <___pformat_cvt+0xe0>
  403796:	c7 44 24 38 02 00 00 	mov    DWORD PTR [esp+0x38],0x2
  40379d:	00 
  40379e:	0f b7 54 24 28       	movzx  edx,WORD PTR [esp+0x28]
  4037a3:	b8 c3 bf ff ff       	mov    eax,0xffffbfc3
  4037a8:	eb 9a                	jmp    403744 <___pformat_cvt+0x64>
  4037aa:	8d b6 00 00 00 00    	lea    esi,[esi+0x0]
  4037b0:	c7 44 24 38 04 00 00 	mov    DWORD PTR [esp+0x38],0x4
  4037b7:	00 
  4037b8:	31 c0                	xor    eax,eax
  4037ba:	31 d2                	xor    edx,edx
  4037bc:	eb 8c                	jmp    40374a <___pformat_cvt+0x6a>
  4037be:	66 90                	xchg   ax,ax
  4037c0:	0f b7 54 24 28       	movzx  edx,WORD PTR [esp+0x28]
  4037c5:	c7 44 24 38 01 00 00 	mov    DWORD PTR [esp+0x38],0x1
  4037cc:	00 
  4037cd:	89 d0                	mov    eax,edx
  4037cf:	25 ff 7f 00 00       	and    eax,0x7fff
  4037d4:	2d 3e 40 00 00       	sub    eax,0x403e
  4037d9:	e9 66 ff ff ff       	jmp    403744 <___pformat_cvt+0x64>
  4037de:	66 90                	xchg   ax,ax

004037e0 <___pformat_putc>:
  4037e0:	53                   	push   ebx
  4037e1:	83 ec 18             	sub    esp,0x18
  4037e4:	8b 4a 04             	mov    ecx,DWORD PTR [edx+0x4]
  4037e7:	f6 c5 20             	test   ch,0x20
  4037ea:	75 08                	jne    4037f4 <___pformat_putc+0x14>
  4037ec:	8b 5a 18             	mov    ebx,DWORD PTR [edx+0x18]
  4037ef:	39 5a 1c             	cmp    DWORD PTR [edx+0x1c],ebx
  4037f2:	7e 10                	jle    403804 <___pformat_putc+0x24>
  4037f4:	80 e5 10             	and    ch,0x10
  4037f7:	75 17                	jne    403810 <___pformat_putc+0x30>
  4037f9:	8b 1a                	mov    ebx,DWORD PTR [edx]
  4037fb:	8b 4a 18             	mov    ecx,DWORD PTR [edx+0x18]
  4037fe:	88 04 0b             	mov    BYTE PTR [ebx+ecx*1],al
  403801:	8b 5a 18             	mov    ebx,DWORD PTR [edx+0x18]
  403804:	83 c3 01             	add    ebx,0x1
  403807:	89 5a 18             	mov    DWORD PTR [edx+0x18],ebx
  40380a:	83 c4 18             	add    esp,0x18
  40380d:	5b                   	pop    ebx
  40380e:	c3                   	ret    
  40380f:	90                   	nop
  403810:	8b 0a                	mov    ecx,DWORD PTR [edx]
  403812:	89 04 24             	mov    DWORD PTR [esp],eax
  403815:	89 54 24 0c          	mov    DWORD PTR [esp+0xc],edx
  403819:	89 4c 24 04          	mov    DWORD PTR [esp+0x4],ecx
  40381d:	e8 16 49 00 00       	call   408138 <_fputc>
  403822:	8b 54 24 0c          	mov    edx,DWORD PTR [esp+0xc]
  403826:	8b 5a 18             	mov    ebx,DWORD PTR [edx+0x18]
  403829:	83 c3 01             	add    ebx,0x1
  40382c:	89 5a 18             	mov    DWORD PTR [edx+0x18],ebx
  40382f:	83 c4 18             	add    esp,0x18
  403832:	5b                   	pop    ebx
  403833:	c3                   	ret    
  403834:	8d b6 00 00 00 00    	lea    esi,[esi+0x0]
  40383a:	8d bf 00 00 00 00    	lea    edi,[edi+0x0]

00403840 <___pformat_wputchars>:
  403840:	55                   	push   ebp
  403841:	57                   	push   edi
  403842:	56                   	push   esi
  403843:	89 d6                	mov    esi,edx
  403845:	53                   	push   ebx
  403846:	89 cb                	mov    ebx,ecx
  403848:	83 ec 4c             	sub    esp,0x4c
  40384b:	89 44 24 18          	mov    DWORD PTR [esp+0x18],eax
  40384f:	8d 6c 24 30          	lea    ebp,[esp+0x30]
  403853:	8d 44 24 2c          	lea    eax,[esp+0x2c]
  403857:	89 44 24 08          	mov    DWORD PTR [esp+0x8],eax
  40385b:	c7 44 24 04 00 00 00 	mov    DWORD PTR [esp+0x4],0x0
  403862:	00 
  403863:	89 2c 24             	mov    DWORD PTR [esp],ebp
  403866:	e8 b5 32 00 00       	call   406b20 <_wcrtomb>
  40386b:	8b 43 0c             	mov    eax,DWORD PTR [ebx+0xc]
  40386e:	85 c0                	test   eax,eax
  403870:	78 08                	js     40387a <___pformat_wputchars+0x3a>
  403872:	39 c6                	cmp    esi,eax
  403874:	0f 8f c7 00 00 00    	jg     403941 <___pformat_wputchars+0x101>
  40387a:	8b 43 08             	mov    eax,DWORD PTR [ebx+0x8]
  40387d:	39 c6                	cmp    esi,eax
  40387f:	0f 8d 8c 00 00 00    	jge    403911 <___pformat_wputchars+0xd1>
  403885:	29 f0                	sub    eax,esi
  403887:	85 c0                	test   eax,eax
  403889:	89 43 08             	mov    DWORD PTR [ebx+0x8],eax
  40388c:	7e 0a                	jle    403898 <___pformat_wputchars+0x58>
  40388e:	f6 43 05 04          	test   BYTE PTR [ebx+0x5],0x4
  403892:	0f 84 85 00 00 00    	je     40391d <___pformat_wputchars+0xdd>
  403898:	89 74 24 1c          	mov    DWORD PTR [esp+0x1c],esi
  40389c:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  4038a0:	8b 44 24 1c          	mov    eax,DWORD PTR [esp+0x1c]
  4038a4:	85 c0                	test   eax,eax
  4038a6:	7e 54                	jle    4038fc <___pformat_wputchars+0xbc>
  4038a8:	83 44 24 18 02       	add    DWORD PTR [esp+0x18],0x2
  4038ad:	8d 44 24 2c          	lea    eax,[esp+0x2c]
  4038b1:	89 44 24 08          	mov    DWORD PTR [esp+0x8],eax
  4038b5:	8b 44 24 18          	mov    eax,DWORD PTR [esp+0x18]
  4038b9:	0f b7 40 fe          	movzx  eax,WORD PTR [eax-0x2]
  4038bd:	89 2c 24             	mov    DWORD PTR [esp],ebp
  4038c0:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
  4038c4:	e8 57 32 00 00       	call   406b20 <_wcrtomb>
  4038c9:	85 c0                	test   eax,eax
  4038cb:	7e 2f                	jle    4038fc <___pformat_wputchars+0xbc>
  4038cd:	8d 74 05 00          	lea    esi,[ebp+eax*1+0x0]
  4038d1:	89 ef                	mov    edi,ebp
  4038d3:	83 c7 01             	add    edi,0x1
  4038d6:	0f be 47 ff          	movsx  eax,BYTE PTR [edi-0x1]
  4038da:	89 da                	mov    edx,ebx
  4038dc:	e8 ff fe ff ff       	call   4037e0 <___pformat_putc>
  4038e1:	39 f7                	cmp    edi,esi
  4038e3:	75 ee                	jne    4038d3 <___pformat_wputchars+0x93>
  4038e5:	83 6c 24 1c 01       	sub    DWORD PTR [esp+0x1c],0x1
  4038ea:	eb b4                	jmp    4038a0 <___pformat_wputchars+0x60>
  4038ec:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  4038f0:	89 da                	mov    edx,ebx
  4038f2:	b8 20 00 00 00       	mov    eax,0x20
  4038f7:	e8 e4 fe ff ff       	call   4037e0 <___pformat_putc>
  4038fc:	8b 43 08             	mov    eax,DWORD PTR [ebx+0x8]
  4038ff:	8d 50 ff             	lea    edx,[eax-0x1]
  403902:	85 c0                	test   eax,eax
  403904:	89 53 08             	mov    DWORD PTR [ebx+0x8],edx
  403907:	7f e7                	jg     4038f0 <___pformat_wputchars+0xb0>
  403909:	83 c4 4c             	add    esp,0x4c
  40390c:	5b                   	pop    ebx
  40390d:	5e                   	pop    esi
  40390e:	5f                   	pop    edi
  40390f:	5d                   	pop    ebp
  403910:	c3                   	ret    
  403911:	c7 43 08 ff ff ff ff 	mov    DWORD PTR [ebx+0x8],0xffffffff
  403918:	e9 7b ff ff ff       	jmp    403898 <___pformat_wputchars+0x58>
  40391d:	83 e8 01             	sub    eax,0x1
  403920:	89 43 08             	mov    DWORD PTR [ebx+0x8],eax
  403923:	89 da                	mov    edx,ebx
  403925:	b8 20 00 00 00       	mov    eax,0x20
  40392a:	e8 b1 fe ff ff       	call   4037e0 <___pformat_putc>
  40392f:	8b 43 08             	mov    eax,DWORD PTR [ebx+0x8]
  403932:	8d 50 ff             	lea    edx,[eax-0x1]
  403935:	85 c0                	test   eax,eax
  403937:	89 53 08             	mov    DWORD PTR [ebx+0x8],edx
  40393a:	75 e7                	jne    403923 <___pformat_wputchars+0xe3>
  40393c:	e9 57 ff ff ff       	jmp    403898 <___pformat_wputchars+0x58>
  403941:	89 c6                	mov    esi,eax
  403943:	e9 32 ff ff ff       	jmp    40387a <___pformat_wputchars+0x3a>
  403948:	90                   	nop
  403949:	8d b4 26 00 00 00 00 	lea    esi,[esi+eiz*1+0x0]

00403950 <___pformat_putchars>:
  403950:	57                   	push   edi
  403951:	89 c7                	mov    edi,eax
  403953:	8b 41 0c             	mov    eax,DWORD PTR [ecx+0xc]
  403956:	56                   	push   esi
  403957:	89 d6                	mov    esi,edx
  403959:	53                   	push   ebx
  40395a:	89 cb                	mov    ebx,ecx
  40395c:	85 c0                	test   eax,eax
  40395e:	78 08                	js     403968 <___pformat_putchars+0x18>
  403960:	39 c2                	cmp    edx,eax
  403962:	0f 8f 88 00 00 00    	jg     4039f0 <___pformat_putchars+0xa0>
  403968:	8b 43 08             	mov    eax,DWORD PTR [ebx+0x8]
  40396b:	39 c6                	cmp    esi,eax
  40396d:	7d 71                	jge    4039e0 <___pformat_putchars+0x90>
  40396f:	29 f0                	sub    eax,esi
  403971:	85 c0                	test   eax,eax
  403973:	89 43 08             	mov    DWORD PTR [ebx+0x8],eax
  403976:	7e 25                	jle    40399d <___pformat_putchars+0x4d>
  403978:	f6 43 05 04          	test   BYTE PTR [ebx+0x5],0x4
  40397c:	75 1f                	jne    40399d <___pformat_putchars+0x4d>
  40397e:	83 e8 01             	sub    eax,0x1
  403981:	89 43 08             	mov    DWORD PTR [ebx+0x8],eax
  403984:	89 da                	mov    edx,ebx
  403986:	b8 20 00 00 00       	mov    eax,0x20
  40398b:	e8 50 fe ff ff       	call   4037e0 <___pformat_putc>
  403990:	8b 43 08             	mov    eax,DWORD PTR [ebx+0x8]
  403993:	8d 50 ff             	lea    edx,[eax-0x1]
  403996:	85 c0                	test   eax,eax
  403998:	89 53 08             	mov    DWORD PTR [ebx+0x8],edx
  40399b:	75 e7                	jne    403984 <___pformat_putchars+0x34>
  40399d:	85 f6                	test   esi,esi
  40399f:	74 2c                	je     4039cd <___pformat_putchars+0x7d>
  4039a1:	83 c7 01             	add    edi,0x1
  4039a4:	0f be 47 ff          	movsx  eax,BYTE PTR [edi-0x1]
  4039a8:	89 da                	mov    edx,ebx
  4039aa:	e8 31 fe ff ff       	call   4037e0 <___pformat_putc>
  4039af:	83 ee 01             	sub    esi,0x1
  4039b2:	75 ed                	jne    4039a1 <___pformat_putchars+0x51>
  4039b4:	8b 43 08             	mov    eax,DWORD PTR [ebx+0x8]
  4039b7:	8d 50 ff             	lea    edx,[eax-0x1]
  4039ba:	85 c0                	test   eax,eax
  4039bc:	89 53 08             	mov    DWORD PTR [ebx+0x8],edx
  4039bf:	7e 19                	jle    4039da <___pformat_putchars+0x8a>
  4039c1:	89 da                	mov    edx,ebx
  4039c3:	b8 20 00 00 00       	mov    eax,0x20
  4039c8:	e8 13 fe ff ff       	call   4037e0 <___pformat_putc>
  4039cd:	8b 43 08             	mov    eax,DWORD PTR [ebx+0x8]
  4039d0:	8d 50 ff             	lea    edx,[eax-0x1]
  4039d3:	85 c0                	test   eax,eax
  4039d5:	89 53 08             	mov    DWORD PTR [ebx+0x8],edx
  4039d8:	7f e7                	jg     4039c1 <___pformat_putchars+0x71>
  4039da:	5b                   	pop    ebx
  4039db:	5e                   	pop    esi
  4039dc:	5f                   	pop    edi
  4039dd:	c3                   	ret    
  4039de:	66 90                	xchg   ax,ax
  4039e0:	c7 43 08 ff ff ff ff 	mov    DWORD PTR [ebx+0x8],0xffffffff
  4039e7:	eb b4                	jmp    40399d <___pformat_putchars+0x4d>
  4039e9:	8d b4 26 00 00 00 00 	lea    esi,[esi+eiz*1+0x0]
  4039f0:	89 c6                	mov    esi,eax
  4039f2:	e9 71 ff ff ff       	jmp    403968 <___pformat_putchars+0x18>
  4039f7:	89 f6                	mov    esi,esi
  4039f9:	8d bc 27 00 00 00 00 	lea    edi,[edi+eiz*1+0x0]

00403a00 <___pformat_emit_inf_or_nan>:
  403a00:	55                   	push   ebp
  403a01:	57                   	push   edi
  403a02:	56                   	push   esi
  403a03:	53                   	push   ebx
  403a04:	83 ec 1c             	sub    esp,0x1c
  403a07:	85 c0                	test   eax,eax
  403a09:	c7 41 0c ff ff ff ff 	mov    DWORD PTR [ecx+0xc],0xffffffff
  403a10:	74 3e                	je     403a50 <___pformat_emit_inf_or_nan+0x50>
  403a12:	8b 69 04             	mov    ebp,DWORD PTR [ecx+0x4]
  403a15:	8d 7c 24 0d          	lea    edi,[esp+0xd]
  403a19:	c6 44 24 0c 2d       	mov    BYTE PTR [esp+0xc],0x2d
  403a1e:	8d 44 24 0c          	lea    eax,[esp+0xc]
  403a22:	83 e5 20             	and    ebp,0x20
  403a25:	31 f6                	xor    esi,esi
  403a27:	0f b6 1c 32          	movzx  ebx,BYTE PTR [edx+esi*1]
  403a2b:	83 e3 df             	and    ebx,0xffffffdf
  403a2e:	09 eb                	or     ebx,ebp
  403a30:	88 1c 37             	mov    BYTE PTR [edi+esi*1],bl
  403a33:	83 c6 01             	add    esi,0x1
  403a36:	83 fe 03             	cmp    esi,0x3
  403a39:	75 ec                	jne    403a27 <___pformat_emit_inf_or_nan+0x27>
  403a3b:	8d 57 03             	lea    edx,[edi+0x3]
  403a3e:	29 c2                	sub    edx,eax
  403a40:	e8 0b ff ff ff       	call   403950 <___pformat_putchars>
  403a45:	83 c4 1c             	add    esp,0x1c
  403a48:	5b                   	pop    ebx
  403a49:	5e                   	pop    esi
  403a4a:	5f                   	pop    edi
  403a4b:	5d                   	pop    ebp
  403a4c:	c3                   	ret    
  403a4d:	8d 76 00             	lea    esi,[esi+0x0]
  403a50:	8b 69 04             	mov    ebp,DWORD PTR [ecx+0x4]
  403a53:	f7 c5 00 01 00 00    	test   ebp,0x100
  403a59:	74 15                	je     403a70 <___pformat_emit_inf_or_nan+0x70>
  403a5b:	c6 44 24 0c 2b       	mov    BYTE PTR [esp+0xc],0x2b
  403a60:	8d 7c 24 0d          	lea    edi,[esp+0xd]
  403a64:	8d 44 24 0c          	lea    eax,[esp+0xc]
  403a68:	eb b8                	jmp    403a22 <___pformat_emit_inf_or_nan+0x22>
  403a6a:	8d b6 00 00 00 00    	lea    esi,[esi+0x0]
  403a70:	f7 c5 40 00 00 00    	test   ebp,0x40
  403a76:	74 0f                	je     403a87 <___pformat_emit_inf_or_nan+0x87>
  403a78:	c6 44 24 0c 20       	mov    BYTE PTR [esp+0xc],0x20
  403a7d:	8d 7c 24 0d          	lea    edi,[esp+0xd]
  403a81:	8d 44 24 0c          	lea    eax,[esp+0xc]
  403a85:	eb 9b                	jmp    403a22 <___pformat_emit_inf_or_nan+0x22>
  403a87:	8d 44 24 0c          	lea    eax,[esp+0xc]
  403a8b:	89 c7                	mov    edi,eax
  403a8d:	eb 93                	jmp    403a22 <___pformat_emit_inf_or_nan+0x22>
  403a8f:	90                   	nop

00403a90 <___pformat_int>:
  403a90:	55                   	push   ebp
  403a91:	89 e5                	mov    ebp,esp
  403a93:	57                   	push   edi
  403a94:	89 d7                	mov    edi,edx
  403a96:	56                   	push   esi
  403a97:	89 c6                	mov    esi,eax
  403a99:	53                   	push   ebx
  403a9a:	89 cb                	mov    ebx,ecx
  403a9c:	83 ec 2c             	sub    esp,0x2c
  403a9f:	89 55 dc             	mov    DWORD PTR [ebp-0x24],edx
  403aa2:	8b 51 0c             	mov    edx,DWORD PTR [ecx+0xc]
  403aa5:	89 45 d8             	mov    DWORD PTR [ebp-0x28],eax
  403aa8:	8b 49 08             	mov    ecx,DWORD PTR [ecx+0x8]
  403aab:	89 d0                	mov    eax,edx
  403aad:	c1 f8 1f             	sar    eax,0x1f
  403ab0:	f7 d0                	not    eax
  403ab2:	21 d0                	and    eax,edx
  403ab4:	83 c0 17             	add    eax,0x17
  403ab7:	39 c8                	cmp    eax,ecx
  403ab9:	7d 02                	jge    403abd <___pformat_int+0x2d>
  403abb:	89 c8                	mov    eax,ecx
  403abd:	83 c0 0f             	add    eax,0xf
  403ac0:	83 e0 f0             	and    eax,0xfffffff0
  403ac3:	e8 a8 e5 ff ff       	call   402070 <___chkstk_ms>
  403ac8:	29 c4                	sub    esp,eax
  403aca:	8d 44 24 10          	lea    eax,[esp+0x10]
  403ace:	89 45 e4             	mov    DWORD PTR [ebp-0x1c],eax
  403ad1:	8b 43 04             	mov    eax,DWORD PTR [ebx+0x4]
  403ad4:	a8 80                	test   al,0x80
  403ad6:	74 0d                	je     403ae5 <___pformat_int+0x55>
  403ad8:	85 ff                	test   edi,edi
  403ada:	0f 88 b0 01 00 00    	js     403c90 <___pformat_int+0x200>
  403ae0:	24 7f                	and    al,0x7f
  403ae2:	89 43 04             	mov    DWORD PTR [ebx+0x4],eax
  403ae5:	8b 4d dc             	mov    ecx,DWORD PTR [ebp-0x24]
  403ae8:	8b 7d d8             	mov    edi,DWORD PTR [ebp-0x28]
  403aeb:	8b 75 e4             	mov    esi,DWORD PTR [ebp-0x1c]
  403aee:	89 c8                	mov    eax,ecx
  403af0:	09 f8                	or     eax,edi
  403af2:	74 5d                	je     403b51 <___pformat_int+0xc1>
  403af4:	89 5d d8             	mov    DWORD PTR [ebp-0x28],ebx
  403af7:	89 cb                	mov    ebx,ecx
  403af9:	8d b4 26 00 00 00 00 	lea    esi,[esi+eiz*1+0x0]
  403b00:	89 3c 24             	mov    DWORD PTR [esp],edi
  403b03:	83 c6 01             	add    esi,0x1
  403b06:	89 5c 24 04          	mov    DWORD PTR [esp+0x4],ebx
  403b0a:	c7 44 24 08 0a 00 00 	mov    DWORD PTR [esp+0x8],0xa
  403b11:	00 
  403b12:	c7 44 24 0c 00 00 00 	mov    DWORD PTR [esp+0xc],0x0
  403b19:	00 
  403b1a:	e8 f1 46 00 00       	call   408210 <___umoddi3>
  403b1f:	83 c0 30             	add    eax,0x30
  403b22:	88 46 ff             	mov    BYTE PTR [esi-0x1],al
  403b25:	89 3c 24             	mov    DWORD PTR [esp],edi
  403b28:	89 5c 24 04          	mov    DWORD PTR [esp+0x4],ebx
  403b2c:	c7 44 24 08 0a 00 00 	mov    DWORD PTR [esp+0x8],0xa
  403b33:	00 
  403b34:	c7 44 24 0c 00 00 00 	mov    DWORD PTR [esp+0xc],0x0
  403b3b:	00 
  403b3c:	e8 1f 48 00 00       	call   408360 <___udivdi3>
  403b41:	89 c7                	mov    edi,eax
  403b43:	89 d0                	mov    eax,edx
  403b45:	09 f8                	or     eax,edi
  403b47:	89 d3                	mov    ebx,edx
  403b49:	75 b5                	jne    403b00 <___pformat_int+0x70>
  403b4b:	8b 5d d8             	mov    ebx,DWORD PTR [ebp-0x28]
  403b4e:	8b 53 0c             	mov    edx,DWORD PTR [ebx+0xc]
  403b51:	85 d2                	test   edx,edx
  403b53:	89 f7                	mov    edi,esi
  403b55:	7e 19                	jle    403b70 <___pformat_int+0xe0>
  403b57:	8b 45 e4             	mov    eax,DWORD PTR [ebp-0x1c]
  403b5a:	29 f0                	sub    eax,esi
  403b5c:	01 c2                	add    edx,eax
  403b5e:	85 d2                	test   edx,edx
  403b60:	7e 0e                	jle    403b70 <___pformat_int+0xe0>
  403b62:	8d 3c 16             	lea    edi,[esi+edx*1]
  403b65:	83 c6 01             	add    esi,0x1
  403b68:	39 fe                	cmp    esi,edi
  403b6a:	c6 46 ff 30          	mov    BYTE PTR [esi-0x1],0x30
  403b6e:	75 f5                	jne    403b65 <___pformat_int+0xd5>
  403b70:	3b 7d e4             	cmp    edi,DWORD PTR [ebp-0x1c]
  403b73:	0f 84 29 01 00 00    	je     403ca2 <___pformat_int+0x212>
  403b79:	8b 43 08             	mov    eax,DWORD PTR [ebx+0x8]
  403b7c:	85 c0                	test   eax,eax
  403b7e:	7e 59                	jle    403bd9 <___pformat_int+0x149>
  403b80:	8b 55 e4             	mov    edx,DWORD PTR [ebp-0x1c]
  403b83:	29 fa                	sub    edx,edi
  403b85:	01 c2                	add    edx,eax
  403b87:	8b 43 04             	mov    eax,DWORD PTR [ebx+0x4]
  403b8a:	85 d2                	test   edx,edx
  403b8c:	89 53 08             	mov    DWORD PTR [ebx+0x8],edx
  403b8f:	7e 4b                	jle    403bdc <___pformat_int+0x14c>
  403b91:	a9 c0 01 00 00       	test   eax,0x1c0
  403b96:	74 06                	je     403b9e <___pformat_int+0x10e>
  403b98:	83 ea 01             	sub    edx,0x1
  403b9b:	89 53 08             	mov    DWORD PTR [ebx+0x8],edx
  403b9e:	8b 53 0c             	mov    edx,DWORD PTR [ebx+0xc]
  403ba1:	85 d2                	test   edx,edx
  403ba3:	0f 88 a7 00 00 00    	js     403c50 <___pformat_int+0x1c0>
  403ba9:	f6 c4 04             	test   ah,0x4
  403bac:	75 2e                	jne    403bdc <___pformat_int+0x14c>
  403bae:	8b 53 08             	mov    edx,DWORD PTR [ebx+0x8]
  403bb1:	8d 4a ff             	lea    ecx,[edx-0x1]
  403bb4:	85 d2                	test   edx,edx
  403bb6:	89 4b 08             	mov    DWORD PTR [ebx+0x8],ecx
  403bb9:	7e 21                	jle    403bdc <___pformat_int+0x14c>
  403bbb:	90                   	nop
  403bbc:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  403bc0:	89 da                	mov    edx,ebx
  403bc2:	b8 20 00 00 00       	mov    eax,0x20
  403bc7:	e8 14 fc ff ff       	call   4037e0 <___pformat_putc>
  403bcc:	8b 43 08             	mov    eax,DWORD PTR [ebx+0x8]
  403bcf:	8d 50 ff             	lea    edx,[eax-0x1]
  403bd2:	85 c0                	test   eax,eax
  403bd4:	89 53 08             	mov    DWORD PTR [ebx+0x8],edx
  403bd7:	7f e7                	jg     403bc0 <___pformat_int+0x130>
  403bd9:	8b 43 04             	mov    eax,DWORD PTR [ebx+0x4]
  403bdc:	a8 80                	test   al,0x80
  403bde:	74 51                	je     403c31 <___pformat_int+0x1a1>
  403be0:	8d 77 01             	lea    esi,[edi+0x1]
  403be3:	c6 07 2d             	mov    BYTE PTR [edi],0x2d
  403be6:	39 75 e4             	cmp    DWORD PTR [ebp-0x1c],esi
  403be9:	8b 7d e4             	mov    edi,DWORD PTR [ebp-0x1c]
  403bec:	73 2e                	jae    403c1c <___pformat_int+0x18c>
  403bee:	66 90                	xchg   ax,ax
  403bf0:	83 ee 01             	sub    esi,0x1
  403bf3:	0f be 06             	movsx  eax,BYTE PTR [esi]
  403bf6:	89 da                	mov    edx,ebx
  403bf8:	e8 e3 fb ff ff       	call   4037e0 <___pformat_putc>
  403bfd:	39 fe                	cmp    esi,edi
  403bff:	75 ef                	jne    403bf0 <___pformat_int+0x160>
  403c01:	8b 43 08             	mov    eax,DWORD PTR [ebx+0x8]
  403c04:	8d 50 ff             	lea    edx,[eax-0x1]
  403c07:	85 c0                	test   eax,eax
  403c09:	89 53 08             	mov    DWORD PTR [ebx+0x8],edx
  403c0c:	7e 1b                	jle    403c29 <___pformat_int+0x199>
  403c0e:	66 90                	xchg   ax,ax
  403c10:	89 da                	mov    edx,ebx
  403c12:	b8 20 00 00 00       	mov    eax,0x20
  403c17:	e8 c4 fb ff ff       	call   4037e0 <___pformat_putc>
  403c1c:	8b 43 08             	mov    eax,DWORD PTR [ebx+0x8]
  403c1f:	8d 50 ff             	lea    edx,[eax-0x1]
  403c22:	85 c0                	test   eax,eax
  403c24:	89 53 08             	mov    DWORD PTR [ebx+0x8],edx
  403c27:	7f e7                	jg     403c10 <___pformat_int+0x180>
  403c29:	8d 65 f4             	lea    esp,[ebp-0xc]
  403c2c:	5b                   	pop    ebx
  403c2d:	5e                   	pop    esi
  403c2e:	5f                   	pop    edi
  403c2f:	5d                   	pop    ebp
  403c30:	c3                   	ret    
  403c31:	f6 c4 01             	test   ah,0x1
  403c34:	74 0a                	je     403c40 <___pformat_int+0x1b0>
  403c36:	8d 77 01             	lea    esi,[edi+0x1]
  403c39:	c6 07 2b             	mov    BYTE PTR [edi],0x2b
  403c3c:	eb a8                	jmp    403be6 <___pformat_int+0x156>
  403c3e:	66 90                	xchg   ax,ax
  403c40:	a8 40                	test   al,0x40
  403c42:	89 fe                	mov    esi,edi
  403c44:	74 a0                	je     403be6 <___pformat_int+0x156>
  403c46:	83 c6 01             	add    esi,0x1
  403c49:	c6 07 20             	mov    BYTE PTR [edi],0x20
  403c4c:	eb 98                	jmp    403be6 <___pformat_int+0x156>
  403c4e:	66 90                	xchg   ax,ax
  403c50:	89 c2                	mov    edx,eax
  403c52:	81 e2 00 06 00 00    	and    edx,0x600
  403c58:	81 fa 00 02 00 00    	cmp    edx,0x200
  403c5e:	0f 85 45 ff ff ff    	jne    403ba9 <___pformat_int+0x119>
  403c64:	8b 53 08             	mov    edx,DWORD PTR [ebx+0x8]
  403c67:	8d 4a ff             	lea    ecx,[edx-0x1]
  403c6a:	85 d2                	test   edx,edx
  403c6c:	89 4b 08             	mov    DWORD PTR [ebx+0x8],ecx
  403c6f:	0f 8e 67 ff ff ff    	jle    403bdc <___pformat_int+0x14c>
  403c75:	83 c7 01             	add    edi,0x1
  403c78:	c6 47 ff 30          	mov    BYTE PTR [edi-0x1],0x30
  403c7c:	8b 43 08             	mov    eax,DWORD PTR [ebx+0x8]
  403c7f:	8d 50 ff             	lea    edx,[eax-0x1]
  403c82:	85 c0                	test   eax,eax
  403c84:	89 53 08             	mov    DWORD PTR [ebx+0x8],edx
  403c87:	7f ec                	jg     403c75 <___pformat_int+0x1e5>
  403c89:	e9 4b ff ff ff       	jmp    403bd9 <___pformat_int+0x149>
  403c8e:	66 90                	xchg   ax,ax
  403c90:	f7 de                	neg    esi
  403c92:	83 d7 00             	adc    edi,0x0
  403c95:	f7 df                	neg    edi
  403c97:	89 75 d8             	mov    DWORD PTR [ebp-0x28],esi
  403c9a:	89 7d dc             	mov    DWORD PTR [ebp-0x24],edi
  403c9d:	e9 43 fe ff ff       	jmp    403ae5 <___pformat_int+0x55>
  403ca2:	8b 4b 0c             	mov    ecx,DWORD PTR [ebx+0xc]
  403ca5:	85 c9                	test   ecx,ecx
  403ca7:	0f 84 cc fe ff ff    	je     403b79 <___pformat_int+0xe9>
  403cad:	c6 07 30             	mov    BYTE PTR [edi],0x30
  403cb0:	83 c7 01             	add    edi,0x1
  403cb3:	e9 c1 fe ff ff       	jmp    403b79 <___pformat_int+0xe9>
  403cb8:	90                   	nop
  403cb9:	8d b4 26 00 00 00 00 	lea    esi,[esi+eiz*1+0x0]

00403cc0 <___pformat_xint>:
  403cc0:	55                   	push   ebp
  403cc1:	89 e5                	mov    ebp,esp
  403cc3:	57                   	push   edi
  403cc4:	89 cf                	mov    edi,ecx
  403cc6:	56                   	push   esi
  403cc7:	89 d6                	mov    esi,edx
  403cc9:	53                   	push   ebx
  403cca:	83 ec 2c             	sub    esp,0x2c
  403ccd:	89 55 dc             	mov    DWORD PTR [ebp-0x24],edx
  403cd0:	31 d2                	xor    edx,edx
  403cd2:	83 f8 6f             	cmp    eax,0x6f
  403cd5:	0f 94 c2             	sete   dl
  403cd8:	83 ea 01             	sub    edx,0x1
  403cdb:	83 e2 fa             	and    edx,0xfffffffa
  403cde:	89 4d d4             	mov    DWORD PTR [ebp-0x2c],ecx
  403ce1:	31 c9                	xor    ecx,ecx
  403ce3:	83 f8 6f             	cmp    eax,0x6f
  403ce6:	0f 95 c1             	setne  cl
  403ce9:	89 45 d8             	mov    DWORD PTR [ebp-0x28],eax
  403cec:	89 c8                	mov    eax,ecx
  403cee:	89 45 e4             	mov    DWORD PTR [ebp-0x1c],eax
  403cf1:	8b 45 08             	mov    eax,DWORD PTR [ebp+0x8]
  403cf4:	8d 1c cd 07 00 00 00 	lea    ebx,[ecx*8+0x7]
  403cfb:	89 5d d0             	mov    DWORD PTR [ebp-0x30],ebx
  403cfe:	8b 4d 08             	mov    ecx,DWORD PTR [ebp+0x8]
  403d01:	83 45 e4 03          	add    DWORD PTR [ebp-0x1c],0x3
  403d05:	8b 58 0c             	mov    ebx,DWORD PTR [eax+0xc]
  403d08:	8b 49 08             	mov    ecx,DWORD PTR [ecx+0x8]
  403d0b:	89 d8                	mov    eax,ebx
  403d0d:	c1 f8 1f             	sar    eax,0x1f
  403d10:	f7 d0                	not    eax
  403d12:	21 d8                	and    eax,ebx
  403d14:	8d 44 02 18          	lea    eax,[edx+eax*1+0x18]
  403d18:	39 c8                	cmp    eax,ecx
  403d1a:	7d 02                	jge    403d1e <___pformat_xint+0x5e>
  403d1c:	89 c8                	mov    eax,ecx
  403d1e:	83 c0 0f             	add    eax,0xf
  403d21:	83 e0 f0             	and    eax,0xfffffff0
  403d24:	e8 47 e3 ff ff       	call   402070 <___chkstk_ms>
  403d29:	29 c4                	sub    esp,eax
  403d2b:	8b 45 d4             	mov    eax,DWORD PTR [ebp-0x2c]
  403d2e:	0b 45 dc             	or     eax,DWORD PTR [ebp-0x24]
  403d31:	89 65 e0             	mov    DWORD PTR [ebp-0x20],esp
  403d34:	0f 84 4a 02 00 00    	je     403f84 <___pformat_xint+0x2c4>
  403d3a:	0f b6 4d d8          	movzx  ecx,BYTE PTR [ebp-0x28]
  403d3e:	89 e0                	mov    eax,esp
  403d40:	0f b6 5d d0          	movzx  ebx,BYTE PTR [ebp-0x30]
  403d44:	83 e1 20             	and    ecx,0x20
  403d47:	88 4d dc             	mov    BYTE PTR [ebp-0x24],cl
  403d4a:	eb 1f                	jmp    403d6b <___pformat_xint+0xab>
  403d4c:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  403d50:	88 48 ff             	mov    BYTE PTR [eax-0x1],cl
  403d53:	0f b6 4d e4          	movzx  ecx,BYTE PTR [ebp-0x1c]
  403d57:	0f ad fe             	shrd   esi,edi,cl
  403d5a:	d3 ef                	shr    edi,cl
  403d5c:	f6 c1 20             	test   cl,0x20
  403d5f:	74 04                	je     403d65 <___pformat_xint+0xa5>
  403d61:	89 fe                	mov    esi,edi
  403d63:	31 ff                	xor    edi,edi
  403d65:	89 f9                	mov    ecx,edi
  403d67:	09 f1                	or     ecx,esi
  403d69:	74 1a                	je     403d85 <___pformat_xint+0xc5>
  403d6b:	89 f2                	mov    edx,esi
  403d6d:	83 c0 01             	add    eax,0x1
  403d70:	21 da                	and    edx,ebx
  403d72:	8d 4a 30             	lea    ecx,[edx+0x30]
  403d75:	80 f9 39             	cmp    cl,0x39
  403d78:	7e d6                	jle    403d50 <___pformat_xint+0x90>
  403d7a:	83 c2 37             	add    edx,0x37
  403d7d:	0a 55 dc             	or     dl,BYTE PTR [ebp-0x24]
  403d80:	88 50 ff             	mov    BYTE PTR [eax-0x1],dl
  403d83:	eb ce                	jmp    403d53 <___pformat_xint+0x93>
  403d85:	39 45 e0             	cmp    DWORD PTR [ebp-0x20],eax
  403d88:	0f 84 f0 01 00 00    	je     403f7e <___pformat_xint+0x2be>
  403d8e:	8b 7d 08             	mov    edi,DWORD PTR [ebp+0x8]
  403d91:	8b 5f 0c             	mov    ebx,DWORD PTR [edi+0xc]
  403d94:	85 db                	test   ebx,ebx
  403d96:	0f 8e a5 01 00 00    	jle    403f41 <___pformat_xint+0x281>
  403d9c:	8b 4d e0             	mov    ecx,DWORD PTR [ebp-0x20]
  403d9f:	29 c1                	sub    ecx,eax
  403da1:	01 cb                	add    ebx,ecx
  403da3:	85 db                	test   ebx,ebx
  403da5:	0f 8e 96 01 00 00    	jle    403f41 <___pformat_xint+0x281>
  403dab:	8d 3c 18             	lea    edi,[eax+ebx*1]
  403dae:	66 90                	xchg   ax,ax
  403db0:	83 c0 01             	add    eax,0x1
  403db3:	39 f8                	cmp    eax,edi
  403db5:	c6 40 ff 30          	mov    BYTE PTR [eax-0x1],0x30
  403db9:	75 f5                	jne    403db0 <___pformat_xint+0xf0>
  403dbb:	3b 7d e0             	cmp    edi,DWORD PTR [ebp-0x20]
  403dbe:	0f 84 a1 01 00 00    	je     403f65 <___pformat_xint+0x2a5>
  403dc4:	8b 45 08             	mov    eax,DWORD PTR [ebp+0x8]
  403dc7:	8b 70 08             	mov    esi,DWORD PTR [eax+0x8]
  403dca:	89 f8                	mov    eax,edi
  403dcc:	2b 45 e0             	sub    eax,DWORD PTR [ebp-0x20]
  403dcf:	39 c6                	cmp    esi,eax
  403dd1:	0f 8e a9 00 00 00    	jle    403e80 <___pformat_xint+0x1c0>
  403dd7:	29 c6                	sub    esi,eax
  403dd9:	8b 45 08             	mov    eax,DWORD PTR [ebp+0x8]
  403ddc:	85 f6                	test   esi,esi
  403dde:	89 70 08             	mov    DWORD PTR [eax+0x8],esi
  403de1:	7e 21                	jle    403e04 <___pformat_xint+0x144>
  403de3:	83 7d d8 6f          	cmp    DWORD PTR [ebp-0x28],0x6f
  403de7:	74 0d                	je     403df6 <___pformat_xint+0x136>
  403de9:	8b 45 08             	mov    eax,DWORD PTR [ebp+0x8]
  403dec:	f6 40 05 08          	test   BYTE PTR [eax+0x5],0x8
  403df0:	0f 85 00 01 00 00    	jne    403ef6 <___pformat_xint+0x236>
  403df6:	8b 45 08             	mov    eax,DWORD PTR [ebp+0x8]
  403df9:	8b 58 0c             	mov    ebx,DWORD PTR [eax+0xc]
  403dfc:	85 db                	test   ebx,ebx
  403dfe:	0f 88 09 01 00 00    	js     403f0d <___pformat_xint+0x24d>
  403e04:	8d 46 ff             	lea    eax,[esi-0x1]
  403e07:	89 45 e4             	mov    DWORD PTR [ebp-0x1c],eax
  403e0a:	8b 45 e4             	mov    eax,DWORD PTR [ebp-0x1c]
  403e0d:	83 7d d8 6f          	cmp    DWORD PTR [ebp-0x28],0x6f
  403e11:	89 c3                	mov    ebx,eax
  403e13:	74 0d                	je     403e22 <___pformat_xint+0x162>
  403e15:	8b 45 08             	mov    eax,DWORD PTR [ebp+0x8]
  403e18:	f6 40 05 08          	test   BYTE PTR [eax+0x5],0x8
  403e1c:	0f 85 be 00 00 00    	jne    403ee0 <___pformat_xint+0x220>
  403e22:	85 f6                	test   esi,esi
  403e24:	7e 09                	jle    403e2f <___pformat_xint+0x16f>
  403e26:	8b 45 08             	mov    eax,DWORD PTR [ebp+0x8]
  403e29:	f6 40 05 04          	test   BYTE PTR [eax+0x5],0x4
  403e2d:	74 71                	je     403ea0 <___pformat_xint+0x1e0>
  403e2f:	3b 7d e0             	cmp    edi,DWORD PTR [ebp-0x20]
  403e32:	76 25                	jbe    403e59 <___pformat_xint+0x199>
  403e34:	89 75 e4             	mov    DWORD PTR [ebp-0x1c],esi
  403e37:	8b 75 e0             	mov    esi,DWORD PTR [ebp-0x20]
  403e3a:	89 5d e0             	mov    DWORD PTR [ebp-0x20],ebx
  403e3d:	89 fb                	mov    ebx,edi
  403e3f:	8b 7d 08             	mov    edi,DWORD PTR [ebp+0x8]
  403e42:	83 eb 01             	sub    ebx,0x1
  403e45:	0f be 03             	movsx  eax,BYTE PTR [ebx]
  403e48:	89 fa                	mov    edx,edi
  403e4a:	e8 91 f9 ff ff       	call   4037e0 <___pformat_putc>
  403e4f:	39 f3                	cmp    ebx,esi
  403e51:	75 ef                	jne    403e42 <___pformat_xint+0x182>
  403e53:	8b 75 e4             	mov    esi,DWORD PTR [ebp-0x1c]
  403e56:	8b 5d e0             	mov    ebx,DWORD PTR [ebp-0x20]
  403e59:	85 f6                	test   esi,esi
  403e5b:	7e 19                	jle    403e76 <___pformat_xint+0x1b6>
  403e5d:	8b 75 08             	mov    esi,DWORD PTR [ebp+0x8]
  403e60:	b8 20 00 00 00       	mov    eax,0x20
  403e65:	83 eb 01             	sub    ebx,0x1
  403e68:	89 f2                	mov    edx,esi
  403e6a:	e8 71 f9 ff ff       	call   4037e0 <___pformat_putc>
  403e6f:	8d 43 01             	lea    eax,[ebx+0x1]
  403e72:	85 c0                	test   eax,eax
  403e74:	7f ea                	jg     403e60 <___pformat_xint+0x1a0>
  403e76:	8d 65 f4             	lea    esp,[ebp-0xc]
  403e79:	5b                   	pop    ebx
  403e7a:	5e                   	pop    esi
  403e7b:	5f                   	pop    edi
  403e7c:	5d                   	pop    ebp
  403e7d:	c3                   	ret    
  403e7e:	66 90                	xchg   ax,ax
  403e80:	8b 45 08             	mov    eax,DWORD PTR [ebp+0x8]
  403e83:	be ff ff ff ff       	mov    esi,0xffffffff
  403e88:	c7 45 e4 fe ff ff ff 	mov    DWORD PTR [ebp-0x1c],0xfffffffe
  403e8f:	c7 40 08 ff ff ff ff 	mov    DWORD PTR [eax+0x8],0xffffffff
  403e96:	e9 6f ff ff ff       	jmp    403e0a <___pformat_xint+0x14a>
  403e9b:	90                   	nop
  403e9c:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  403ea0:	8b 5d e4             	mov    ebx,DWORD PTR [ebp-0x1c]
  403ea3:	89 c6                	mov    esi,eax
  403ea5:	b8 20 00 00 00       	mov    eax,0x20
  403eaa:	83 eb 01             	sub    ebx,0x1
  403ead:	89 f2                	mov    edx,esi
  403eaf:	e8 2c f9 ff ff       	call   4037e0 <___pformat_putc>
  403eb4:	8d 43 01             	lea    eax,[ebx+0x1]
  403eb7:	85 c0                	test   eax,eax
  403eb9:	7f ea                	jg     403ea5 <___pformat_xint+0x1e5>
  403ebb:	8b 4d e4             	mov    ecx,DWORD PTR [ebp-0x1c]
  403ebe:	89 c8                	mov    eax,ecx
  403ec0:	c1 f8 1f             	sar    eax,0x1f
  403ec3:	f7 d0                	not    eax
  403ec5:	8d 71 ff             	lea    esi,[ecx-0x1]
  403ec8:	21 c8                	and    eax,ecx
  403eca:	29 c6                	sub    esi,eax
  403ecc:	8d 5e ff             	lea    ebx,[esi-0x1]
  403ecf:	e9 5b ff ff ff       	jmp    403e2f <___pformat_xint+0x16f>
  403ed4:	83 ee 03             	sub    esi,0x3
  403ed7:	89 75 e4             	mov    DWORD PTR [ebp-0x1c],esi
  403eda:	89 c6                	mov    esi,eax
  403edc:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  403ee0:	0f b6 45 d8          	movzx  eax,BYTE PTR [ebp-0x28]
  403ee4:	83 c7 02             	add    edi,0x2
  403ee7:	c6 47 ff 30          	mov    BYTE PTR [edi-0x1],0x30
  403eeb:	8b 5d e4             	mov    ebx,DWORD PTR [ebp-0x1c]
  403eee:	88 47 fe             	mov    BYTE PTR [edi-0x2],al
  403ef1:	e9 2c ff ff ff       	jmp    403e22 <___pformat_xint+0x162>
  403ef6:	8d 46 fe             	lea    eax,[esi-0x2]
  403ef9:	85 c0                	test   eax,eax
  403efb:	7e d7                	jle    403ed4 <___pformat_xint+0x214>
  403efd:	89 c6                	mov    esi,eax
  403eff:	8b 45 08             	mov    eax,DWORD PTR [ebp+0x8]
  403f02:	8b 58 0c             	mov    ebx,DWORD PTR [eax+0xc]
  403f05:	85 db                	test   ebx,ebx
  403f07:	0f 89 f7 fe ff ff    	jns    403e04 <___pformat_xint+0x144>
  403f0d:	8b 45 08             	mov    eax,DWORD PTR [ebp+0x8]
  403f10:	8b 40 04             	mov    eax,DWORD PTR [eax+0x4]
  403f13:	25 00 06 00 00       	and    eax,0x600
  403f18:	3d 00 02 00 00       	cmp    eax,0x200
  403f1d:	0f 85 e1 fe ff ff    	jne    403e04 <___pformat_xint+0x144>
  403f23:	01 fe                	add    esi,edi
  403f25:	83 c7 01             	add    edi,0x1
  403f28:	39 f7                	cmp    edi,esi
  403f2a:	c6 47 ff 30          	mov    BYTE PTR [edi-0x1],0x30
  403f2e:	75 f5                	jne    403f25 <___pformat_xint+0x265>
  403f30:	c7 45 e4 fe ff ff ff 	mov    DWORD PTR [ebp-0x1c],0xfffffffe
  403f37:	be ff ff ff ff       	mov    esi,0xffffffff
  403f3c:	e9 c9 fe ff ff       	jmp    403e0a <___pformat_xint+0x14a>
  403f41:	83 7d d8 6f          	cmp    DWORD PTR [ebp-0x28],0x6f
  403f45:	89 c7                	mov    edi,eax
  403f47:	0f 85 6e fe ff ff    	jne    403dbb <___pformat_xint+0xfb>
  403f4d:	8b 75 08             	mov    esi,DWORD PTR [ebp+0x8]
  403f50:	f6 46 05 08          	test   BYTE PTR [esi+0x5],0x8
  403f54:	0f 84 61 fe ff ff    	je     403dbb <___pformat_xint+0xfb>
  403f5a:	83 c7 01             	add    edi,0x1
  403f5d:	c6 00 30             	mov    BYTE PTR [eax],0x30
  403f60:	e9 56 fe ff ff       	jmp    403dbb <___pformat_xint+0xfb>
  403f65:	8b 45 08             	mov    eax,DWORD PTR [ebp+0x8]
  403f68:	8b 70 0c             	mov    esi,DWORD PTR [eax+0xc]
  403f6b:	85 f6                	test   esi,esi
  403f6d:	0f 84 51 fe ff ff    	je     403dc4 <___pformat_xint+0x104>
  403f73:	c6 07 30             	mov    BYTE PTR [edi],0x30
  403f76:	83 c7 01             	add    edi,0x1
  403f79:	e9 46 fe ff ff       	jmp    403dc4 <___pformat_xint+0x104>
  403f7e:	8b 45 08             	mov    eax,DWORD PTR [ebp+0x8]
  403f81:	8b 58 0c             	mov    ebx,DWORD PTR [eax+0xc]
  403f84:	8b 45 08             	mov    eax,DWORD PTR [ebp+0x8]
  403f87:	81 60 04 ff f7 ff ff 	and    DWORD PTR [eax+0x4],0xfffff7ff
  403f8e:	8b 45 e0             	mov    eax,DWORD PTR [ebp-0x20]
  403f91:	e9 fe fd ff ff       	jmp    403d94 <___pformat_xint+0xd4>
  403f96:	8d 76 00             	lea    esi,[esi+0x0]
  403f99:	8d bc 27 00 00 00 00 	lea    edi,[edi+eiz*1+0x0]

00403fa0 <___pformat_emit_float>:
  403fa0:	55                   	push   ebp
  403fa1:	89 e5                	mov    ebp,esp
  403fa3:	57                   	push   edi
  403fa4:	56                   	push   esi
  403fa5:	89 d6                	mov    esi,edx
  403fa7:	53                   	push   ebx
  403fa8:	89 cb                	mov    ebx,ecx
  403faa:	83 ec 3c             	sub    esp,0x3c
  403fad:	8b 7d 08             	mov    edi,DWORD PTR [ebp+0x8]
  403fb0:	85 c9                	test   ecx,ecx
  403fb2:	89 45 d4             	mov    DWORD PTR [ebp-0x2c],eax
  403fb5:	8b 47 08             	mov    eax,DWORD PTR [edi+0x8]
  403fb8:	0f 8e 7a 02 00 00    	jle    404238 <___pformat_emit_float+0x298>
  403fbe:	39 c1                	cmp    ecx,eax
  403fc0:	0f 8d 3a 01 00 00    	jge    404100 <___pformat_emit_float+0x160>
  403fc6:	29 c8                	sub    eax,ecx
  403fc8:	89 47 08             	mov    DWORD PTR [edi+0x8],eax
  403fcb:	85 c0                	test   eax,eax
  403fcd:	0f 88 2d 01 00 00    	js     404100 <___pformat_emit_float+0x160>
  403fd3:	8b 57 0c             	mov    edx,DWORD PTR [edi+0xc]
  403fd6:	39 c2                	cmp    edx,eax
  403fd8:	0f 8d 22 01 00 00    	jge    404100 <___pformat_emit_float+0x160>
  403fde:	29 d0                	sub    eax,edx
  403fe0:	85 c0                	test   eax,eax
  403fe2:	89 47 08             	mov    DWORD PTR [edi+0x8],eax
  403fe5:	0f 8e 1c 01 00 00    	jle    404107 <___pformat_emit_float+0x167>
  403feb:	85 d2                	test   edx,edx
  403fed:	0f 8e ad 02 00 00    	jle    4042a0 <___pformat_emit_float+0x300>
  403ff3:	83 e8 01             	sub    eax,0x1
  403ff6:	85 c0                	test   eax,eax
  403ff8:	89 47 08             	mov    DWORD PTR [edi+0x8],eax
  403ffb:	0f 84 06 01 00 00    	je     404107 <___pformat_emit_float+0x167>
  404001:	8b 55 d4             	mov    edx,DWORD PTR [ebp-0x2c]
  404004:	85 d2                	test   edx,edx
  404006:	0f 85 ba 01 00 00    	jne    4041c6 <___pformat_emit_float+0x226>
  40400c:	8b 57 04             	mov    edx,DWORD PTR [edi+0x4]
  40400f:	f7 c2 c0 01 00 00    	test   edx,0x1c0
  404015:	0f 85 ab 01 00 00    	jne    4041c6 <___pformat_emit_float+0x226>
  40401b:	80 e6 06             	and    dh,0x6
  40401e:	0f 85 e3 00 00 00    	jne    404107 <___pformat_emit_float+0x167>
  404024:	eb 0c                	jmp    404032 <___pformat_emit_float+0x92>
  404026:	89 fa                	mov    edx,edi
  404028:	b8 20 00 00 00       	mov    eax,0x20
  40402d:	e8 ae f7 ff ff       	call   4037e0 <___pformat_putc>
  404032:	8b 47 08             	mov    eax,DWORD PTR [edi+0x8]
  404035:	8d 50 ff             	lea    edx,[eax-0x1]
  404038:	85 c0                	test   eax,eax
  40403a:	89 57 08             	mov    DWORD PTR [edi+0x8],edx
  40403d:	7f e7                	jg     404026 <___pformat_emit_float+0x86>
  40403f:	8b 45 d4             	mov    eax,DWORD PTR [ebp-0x2c]
  404042:	85 c0                	test   eax,eax
  404044:	0f 84 c8 00 00 00    	je     404112 <___pformat_emit_float+0x172>
  40404a:	89 fa                	mov    edx,edi
  40404c:	b8 2d 00 00 00       	mov    eax,0x2d
  404051:	e8 8a f7 ff ff       	call   4037e0 <___pformat_putc>
  404056:	8b 57 08             	mov    edx,DWORD PTR [edi+0x8]
  404059:	85 d2                	test   edx,edx
  40405b:	7e 13                	jle    404070 <___pformat_emit_float+0xd0>
  40405d:	8b 47 04             	mov    eax,DWORD PTR [edi+0x4]
  404060:	25 00 06 00 00       	and    eax,0x600
  404065:	3d 00 02 00 00       	cmp    eax,0x200
  40406a:	0f 84 f1 01 00 00    	je     404261 <___pformat_emit_float+0x2c1>
  404070:	85 db                	test   ebx,ebx
  404072:	0f 8e 10 02 00 00    	jle    404288 <___pformat_emit_float+0x2e8>
  404078:	0f b6 16             	movzx  edx,BYTE PTR [esi]
  40407b:	b8 30 00 00 00       	mov    eax,0x30
  404080:	84 d2                	test   dl,dl
  404082:	74 06                	je     40408a <___pformat_emit_float+0xea>
  404084:	83 c6 01             	add    esi,0x1
  404087:	0f be c2             	movsx  eax,dl
  40408a:	89 fa                	mov    edx,edi
  40408c:	e8 4f f7 ff ff       	call   4037e0 <___pformat_putc>
  404091:	83 eb 01             	sub    ebx,0x1
  404094:	75 e2                	jne    404078 <___pformat_emit_float+0xd8>
  404096:	8b 47 0c             	mov    eax,DWORD PTR [edi+0xc]
  404099:	85 c0                	test   eax,eax
  40409b:	0f 8e 3f 01 00 00    	jle    4041e0 <___pformat_emit_float+0x240>
  4040a1:	83 7f 10 fd          	cmp    DWORD PTR [edi+0x10],0xfffffffd
  4040a5:	0f 84 49 01 00 00    	je     4041f4 <___pformat_emit_float+0x254>
  4040ab:	0f b7 57 14          	movzx  edx,WORD PTR [edi+0x14]
  4040af:	66 85 d2             	test   dx,dx
  4040b2:	0f 85 7f 00 00 00    	jne    404137 <___pformat_emit_float+0x197>
  4040b8:	b8 2e 00 00 00       	mov    eax,0x2e
  4040bd:	89 fa                	mov    edx,edi
  4040bf:	e8 1c f7 ff ff       	call   4037e0 <___pformat_putc>
  4040c4:	8b 47 0c             	mov    eax,DWORD PTR [edi+0xc]
  4040c7:	85 db                	test   ebx,ebx
  4040c9:	74 21                	je     4040ec <___pformat_emit_float+0x14c>
  4040cb:	e9 d8 00 00 00       	jmp    4041a8 <___pformat_emit_float+0x208>
  4040d0:	0f b6 16             	movzx  edx,BYTE PTR [esi]
  4040d3:	b8 30 00 00 00       	mov    eax,0x30
  4040d8:	84 d2                	test   dl,dl
  4040da:	74 06                	je     4040e2 <___pformat_emit_float+0x142>
  4040dc:	83 c6 01             	add    esi,0x1
  4040df:	0f be c2             	movsx  eax,dl
  4040e2:	89 fa                	mov    edx,edi
  4040e4:	e8 f7 f6 ff ff       	call   4037e0 <___pformat_putc>
  4040e9:	8b 47 0c             	mov    eax,DWORD PTR [edi+0xc]
  4040ec:	8d 50 ff             	lea    edx,[eax-0x1]
  4040ef:	85 c0                	test   eax,eax
  4040f1:	89 57 0c             	mov    DWORD PTR [edi+0xc],edx
  4040f4:	7f da                	jg     4040d0 <___pformat_emit_float+0x130>
  4040f6:	8d 65 f4             	lea    esp,[ebp-0xc]
  4040f9:	5b                   	pop    ebx
  4040fa:	5e                   	pop    esi
  4040fb:	5f                   	pop    edi
  4040fc:	5d                   	pop    ebp
  4040fd:	c3                   	ret    
  4040fe:	66 90                	xchg   ax,ax
  404100:	c7 47 08 ff ff ff ff 	mov    DWORD PTR [edi+0x8],0xffffffff
  404107:	8b 45 d4             	mov    eax,DWORD PTR [ebp-0x2c]
  40410a:	85 c0                	test   eax,eax
  40410c:	0f 85 38 ff ff ff    	jne    40404a <___pformat_emit_float+0xaa>
  404112:	8b 47 04             	mov    eax,DWORD PTR [edi+0x4]
  404115:	f6 c4 01             	test   ah,0x1
  404118:	0f 85 32 01 00 00    	jne    404250 <___pformat_emit_float+0x2b0>
  40411e:	a8 40                	test   al,0x40
  404120:	0f 84 30 ff ff ff    	je     404056 <___pformat_emit_float+0xb6>
  404126:	89 fa                	mov    edx,edi
  404128:	b8 20 00 00 00       	mov    eax,0x20
  40412d:	e8 ae f6 ff ff       	call   4037e0 <___pformat_putc>
  404132:	e9 1f ff ff ff       	jmp    404056 <___pformat_emit_float+0xb6>
  404137:	8b 47 10             	mov    eax,DWORD PTR [edi+0x10]
  40413a:	89 65 d4             	mov    DWORD PTR [ebp-0x2c],esp
  40413d:	83 c0 0f             	add    eax,0xf
  404140:	83 e0 f0             	and    eax,0xfffffff0
  404143:	e8 28 df ff ff       	call   402070 <___chkstk_ms>
  404148:	29 c4                	sub    esp,eax
  40414a:	8d 4c 24 10          	lea    ecx,[esp+0x10]
  40414e:	8d 45 e4             	lea    eax,[ebp-0x1c]
  404151:	c7 45 e4 00 00 00 00 	mov    DWORD PTR [ebp-0x1c],0x0
  404158:	89 44 24 08          	mov    DWORD PTR [esp+0x8],eax
  40415c:	89 54 24 04          	mov    DWORD PTR [esp+0x4],edx
  404160:	89 0c 24             	mov    DWORD PTR [esp],ecx
  404163:	89 4d d0             	mov    DWORD PTR [ebp-0x30],ecx
  404166:	e8 b5 29 00 00       	call   406b20 <_wcrtomb>
  40416b:	85 c0                	test   eax,eax
  40416d:	0f 8e 42 01 00 00    	jle    4042b5 <___pformat_emit_float+0x315>
  404173:	8b 4d d0             	mov    ecx,DWORD PTR [ebp-0x30]
  404176:	89 5d cc             	mov    DWORD PTR [ebp-0x34],ebx
  404179:	89 75 d0             	mov    DWORD PTR [ebp-0x30],esi
  40417c:	01 c8                	add    eax,ecx
  40417e:	89 cb                	mov    ebx,ecx
  404180:	89 c6                	mov    esi,eax
  404182:	83 c3 01             	add    ebx,0x1
  404185:	0f be 43 ff          	movsx  eax,BYTE PTR [ebx-0x1]
  404189:	89 fa                	mov    edx,edi
  40418b:	e8 50 f6 ff ff       	call   4037e0 <___pformat_putc>
  404190:	39 f3                	cmp    ebx,esi
  404192:	75 ee                	jne    404182 <___pformat_emit_float+0x1e2>
  404194:	8b 75 d0             	mov    esi,DWORD PTR [ebp-0x30]
  404197:	8b 5d cc             	mov    ebx,DWORD PTR [ebp-0x34]
  40419a:	85 db                	test   ebx,ebx
  40419c:	8b 65 d4             	mov    esp,DWORD PTR [ebp-0x2c]
  40419f:	8b 47 0c             	mov    eax,DWORD PTR [edi+0xc]
  4041a2:	0f 84 44 ff ff ff    	je     4040ec <___pformat_emit_float+0x14c>
  4041a8:	01 d8                	add    eax,ebx
  4041aa:	89 47 0c             	mov    DWORD PTR [edi+0xc],eax
  4041ad:	8d 76 00             	lea    esi,[esi+0x0]
  4041b0:	89 fa                	mov    edx,edi
  4041b2:	b8 30 00 00 00       	mov    eax,0x30
  4041b7:	e8 24 f6 ff ff       	call   4037e0 <___pformat_putc>
  4041bc:	83 c3 01             	add    ebx,0x1
  4041bf:	78 ef                	js     4041b0 <___pformat_emit_float+0x210>
  4041c1:	e9 23 ff ff ff       	jmp    4040e9 <___pformat_emit_float+0x149>
  4041c6:	83 e8 01             	sub    eax,0x1
  4041c9:	85 c0                	test   eax,eax
  4041cb:	89 47 08             	mov    DWORD PTR [edi+0x8],eax
  4041ce:	0f 84 33 ff ff ff    	je     404107 <___pformat_emit_float+0x167>
  4041d4:	8b 57 04             	mov    edx,DWORD PTR [edi+0x4]
  4041d7:	e9 3f fe ff ff       	jmp    40401b <___pformat_emit_float+0x7b>
  4041dc:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  4041e0:	f6 47 05 08          	test   BYTE PTR [edi+0x5],0x8
  4041e4:	0f 84 dd fe ff ff    	je     4040c7 <___pformat_emit_float+0x127>
  4041ea:	83 7f 10 fd          	cmp    DWORD PTR [edi+0x10],0xfffffffd
  4041ee:	0f 85 b7 fe ff ff    	jne    4040ab <___pformat_emit_float+0x10b>
  4041f4:	c7 45 e4 00 00 00 00 	mov    DWORD PTR [ebp-0x1c],0x0
  4041fb:	e8 40 3f 00 00       	call   408140 <_localeconv>
  404200:	8d 55 e4             	lea    edx,[ebp-0x1c]
  404203:	89 54 24 0c          	mov    DWORD PTR [esp+0xc],edx
  404207:	c7 44 24 08 10 00 00 	mov    DWORD PTR [esp+0x8],0x10
  40420e:	00 
  40420f:	8b 00                	mov    eax,DWORD PTR [eax]
  404211:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
  404215:	8d 45 e2             	lea    eax,[ebp-0x1e]
  404218:	89 04 24             	mov    DWORD PTR [esp],eax
  40421b:	e8 50 2c 00 00       	call   406e70 <_mbrtowc>
  404220:	85 c0                	test   eax,eax
  404222:	0f 8e 9e 00 00 00    	jle    4042c6 <___pformat_emit_float+0x326>
  404228:	0f b7 55 e2          	movzx  edx,WORD PTR [ebp-0x1e]
  40422c:	66 89 57 14          	mov    WORD PTR [edi+0x14],dx
  404230:	89 47 10             	mov    DWORD PTR [edi+0x10],eax
  404233:	e9 77 fe ff ff       	jmp    4040af <___pformat_emit_float+0x10f>
  404238:	85 c0                	test   eax,eax
  40423a:	0f 8e 8b fd ff ff    	jle    403fcb <___pformat_emit_float+0x2b>
  404240:	83 e8 01             	sub    eax,0x1
  404243:	89 47 08             	mov    DWORD PTR [edi+0x8],eax
  404246:	e9 88 fd ff ff       	jmp    403fd3 <___pformat_emit_float+0x33>
  40424b:	90                   	nop
  40424c:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  404250:	89 fa                	mov    edx,edi
  404252:	b8 2b 00 00 00       	mov    eax,0x2b
  404257:	e8 84 f5 ff ff       	call   4037e0 <___pformat_putc>
  40425c:	e9 f5 fd ff ff       	jmp    404056 <___pformat_emit_float+0xb6>
  404261:	83 ea 01             	sub    edx,0x1
  404264:	89 57 08             	mov    DWORD PTR [edi+0x8],edx
  404267:	89 fa                	mov    edx,edi
  404269:	b8 30 00 00 00       	mov    eax,0x30
  40426e:	e8 6d f5 ff ff       	call   4037e0 <___pformat_putc>
  404273:	8b 47 08             	mov    eax,DWORD PTR [edi+0x8]
  404276:	8d 50 ff             	lea    edx,[eax-0x1]
  404279:	85 c0                	test   eax,eax
  40427b:	89 57 08             	mov    DWORD PTR [edi+0x8],edx
  40427e:	7f e7                	jg     404267 <___pformat_emit_float+0x2c7>
  404280:	85 db                	test   ebx,ebx
  404282:	0f 8f f0 fd ff ff    	jg     404078 <___pformat_emit_float+0xd8>
  404288:	89 fa                	mov    edx,edi
  40428a:	b8 30 00 00 00       	mov    eax,0x30
  40428f:	e8 4c f5 ff ff       	call   4037e0 <___pformat_putc>
  404294:	e9 fd fd ff ff       	jmp    404096 <___pformat_emit_float+0xf6>
  404299:	8d b4 26 00 00 00 00 	lea    esi,[esi+eiz*1+0x0]
  4042a0:	f6 47 05 08          	test   BYTE PTR [edi+0x5],0x8
  4042a4:	0f 84 57 fd ff ff    	je     404001 <___pformat_emit_float+0x61>
  4042aa:	8d b6 00 00 00 00    	lea    esi,[esi+0x0]
  4042b0:	e9 3e fd ff ff       	jmp    403ff3 <___pformat_emit_float+0x53>
  4042b5:	89 fa                	mov    edx,edi
  4042b7:	b8 2e 00 00 00       	mov    eax,0x2e
  4042bc:	e8 1f f5 ff ff       	call   4037e0 <___pformat_putc>
  4042c1:	e9 d4 fe ff ff       	jmp    40419a <___pformat_emit_float+0x1fa>
  4042c6:	0f b7 57 14          	movzx  edx,WORD PTR [edi+0x14]
  4042ca:	e9 61 ff ff ff       	jmp    404230 <___pformat_emit_float+0x290>
  4042cf:	90                   	nop

004042d0 <___pformat_emit_efloat>:
  4042d0:	55                   	push   ebp
  4042d1:	83 e9 01             	sub    ecx,0x1
  4042d4:	57                   	push   edi
  4042d5:	89 d5                	mov    ebp,edx
  4042d7:	56                   	push   esi
  4042d8:	be 01 00 00 00       	mov    esi,0x1
  4042dd:	53                   	push   ebx
  4042de:	bb 67 66 66 66       	mov    ebx,0x66666667
  4042e3:	83 ec 1c             	sub    esp,0x1c
  4042e6:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
  4042ea:	89 c8                	mov    eax,ecx
  4042ec:	8b 7c 24 30          	mov    edi,DWORD PTR [esp+0x30]
  4042f0:	c1 f8 1f             	sar    eax,0x1f
  4042f3:	89 44 24 0c          	mov    DWORD PTR [esp+0xc],eax
  4042f7:	89 c8                	mov    eax,ecx
  4042f9:	f7 eb                	imul   ebx
  4042fb:	89 4c 24 08          	mov    DWORD PTR [esp+0x8],ecx
  4042ff:	c1 f9 1f             	sar    ecx,0x1f
  404302:	c1 fa 02             	sar    edx,0x2
  404305:	89 d3                	mov    ebx,edx
  404307:	29 cb                	sub    ebx,ecx
  404309:	74 18                	je     404323 <___pformat_emit_efloat+0x53>
  40430b:	b9 67 66 66 66       	mov    ecx,0x66666667
  404310:	89 d8                	mov    eax,ebx
  404312:	83 c6 01             	add    esi,0x1
  404315:	f7 e9                	imul   ecx
  404317:	c1 fb 1f             	sar    ebx,0x1f
  40431a:	c1 fa 02             	sar    edx,0x2
  40431d:	29 da                	sub    edx,ebx
  40431f:	89 d3                	mov    ebx,edx
  404321:	75 ed                	jne    404310 <___pformat_emit_efloat+0x40>
  404323:	8b 47 20             	mov    eax,DWORD PTR [edi+0x20]
  404326:	39 c6                	cmp    esi,eax
  404328:	7d 02                	jge    40432c <___pformat_emit_efloat+0x5c>
  40432a:	89 c6                	mov    esi,eax
  40432c:	8b 57 08             	mov    edx,DWORD PTR [edi+0x8]
  40432f:	8d 46 02             	lea    eax,[esi+0x2]
  404332:	39 c2                	cmp    edx,eax
  404334:	7f 5a                	jg     404390 <___pformat_emit_efloat+0xc0>
  404336:	c7 47 08 ff ff ff ff 	mov    DWORD PTR [edi+0x8],0xffffffff
  40433d:	8b 44 24 04          	mov    eax,DWORD PTR [esp+0x4]
  404341:	b9 01 00 00 00       	mov    ecx,0x1
  404346:	89 ea                	mov    edx,ebp
  404348:	89 3c 24             	mov    DWORD PTR [esp],edi
  40434b:	83 c6 01             	add    esi,0x1
  40434e:	e8 4d fc ff ff       	call   403fa0 <___pformat_emit_float>
  404353:	8b 47 20             	mov    eax,DWORD PTR [edi+0x20]
  404356:	89 47 0c             	mov    DWORD PTR [edi+0xc],eax
  404359:	8b 47 04             	mov    eax,DWORD PTR [edi+0x4]
  40435c:	89 c2                	mov    edx,eax
  40435e:	83 e0 20             	and    eax,0x20
  404361:	81 ca c0 01 00 00    	or     edx,0x1c0
  404367:	83 c8 45             	or     eax,0x45
  40436a:	89 57 04             	mov    DWORD PTR [edi+0x4],edx
  40436d:	89 fa                	mov    edx,edi
  40436f:	e8 6c f4 ff ff       	call   4037e0 <___pformat_putc>
  404374:	8b 44 24 08          	mov    eax,DWORD PTR [esp+0x8]
  404378:	89 f9                	mov    ecx,edi
  40437a:	01 77 08             	add    DWORD PTR [edi+0x8],esi
  40437d:	8b 54 24 0c          	mov    edx,DWORD PTR [esp+0xc]
  404381:	e8 0a f7 ff ff       	call   403a90 <___pformat_int>
  404386:	83 c4 1c             	add    esp,0x1c
  404389:	5b                   	pop    ebx
  40438a:	5e                   	pop    esi
  40438b:	5f                   	pop    edi
  40438c:	5d                   	pop    ebp
  40438d:	c3                   	ret    
  40438e:	66 90                	xchg   ax,ax
  404390:	29 c2                	sub    edx,eax
  404392:	89 57 08             	mov    DWORD PTR [edi+0x8],edx
  404395:	eb a6                	jmp    40433d <___pformat_emit_efloat+0x6d>
  404397:	89 f6                	mov    esi,esi
  404399:	8d bc 27 00 00 00 00 	lea    edi,[edi+eiz*1+0x0]

004043a0 <___pformat_efloat>:
  4043a0:	56                   	push   esi
  4043a1:	53                   	push   ebx
  4043a2:	89 c3                	mov    ebx,eax
  4043a4:	83 ec 44             	sub    esp,0x44
  4043a7:	8b 40 0c             	mov    eax,DWORD PTR [eax+0xc]
  4043aa:	85 c0                	test   eax,eax
  4043ac:	78 72                	js     404420 <___pformat_efloat+0x80>
  4043ae:	83 c0 01             	add    eax,0x1
  4043b1:	db 6c 24 50          	fld    TBYTE PTR [esp+0x50]
  4043b5:	89 44 24 10          	mov    DWORD PTR [esp+0x10],eax
  4043b9:	8d 54 24 28          	lea    edx,[esp+0x28]
  4043bd:	db 7c 24 30          	fstp   TBYTE PTR [esp+0x30]
  4043c1:	8b 44 24 30          	mov    eax,DWORD PTR [esp+0x30]
  4043c5:	89 54 24 18          	mov    DWORD PTR [esp+0x18],edx
  4043c9:	8d 54 24 2c          	lea    edx,[esp+0x2c]
  4043cd:	89 54 24 14          	mov    DWORD PTR [esp+0x14],edx
  4043d1:	89 04 24             	mov    DWORD PTR [esp],eax
  4043d4:	8b 44 24 34          	mov    eax,DWORD PTR [esp+0x34]
  4043d8:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
  4043dc:	8b 44 24 38          	mov    eax,DWORD PTR [esp+0x38]
  4043e0:	89 44 24 08          	mov    DWORD PTR [esp+0x8],eax
  4043e4:	8b 44 24 3c          	mov    eax,DWORD PTR [esp+0x3c]
  4043e8:	89 44 24 0c          	mov    DWORD PTR [esp+0xc],eax
  4043ec:	b8 02 00 00 00       	mov    eax,0x2
  4043f1:	e8 ea f2 ff ff       	call   4036e0 <___pformat_cvt>
  4043f6:	8b 4c 24 2c          	mov    ecx,DWORD PTR [esp+0x2c]
  4043fa:	81 f9 00 80 ff ff    	cmp    ecx,0xffff8000
  404400:	89 c6                	mov    esi,eax
  404402:	74 2c                	je     404430 <___pformat_efloat+0x90>
  404404:	89 c2                	mov    edx,eax
  404406:	8b 44 24 28          	mov    eax,DWORD PTR [esp+0x28]
  40440a:	89 1c 24             	mov    DWORD PTR [esp],ebx
  40440d:	e8 be fe ff ff       	call   4042d0 <___pformat_emit_efloat>
  404412:	89 34 24             	mov    DWORD PTR [esp],esi
  404415:	e8 86 2d 00 00       	call   4071a0 <___freedtoa>
  40441a:	83 c4 44             	add    esp,0x44
  40441d:	5b                   	pop    ebx
  40441e:	5e                   	pop    esi
  40441f:	c3                   	ret    
  404420:	c7 43 0c 06 00 00 00 	mov    DWORD PTR [ebx+0xc],0x6
  404427:	b8 07 00 00 00       	mov    eax,0x7
  40442c:	eb 83                	jmp    4043b1 <___pformat_efloat+0x11>
  40442e:	66 90                	xchg   ax,ax
  404430:	89 c2                	mov    edx,eax
  404432:	8b 44 24 28          	mov    eax,DWORD PTR [esp+0x28]
  404436:	89 d9                	mov    ecx,ebx
  404438:	e8 c3 f5 ff ff       	call   403a00 <___pformat_emit_inf_or_nan>
  40443d:	89 34 24             	mov    DWORD PTR [esp],esi
  404440:	e8 5b 2d 00 00       	call   4071a0 <___freedtoa>
  404445:	83 c4 44             	add    esp,0x44
  404448:	5b                   	pop    ebx
  404449:	5e                   	pop    esi
  40444a:	c3                   	ret    
  40444b:	90                   	nop
  40444c:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]

00404450 <___pformat_float>:
  404450:	57                   	push   edi
  404451:	56                   	push   esi
  404452:	53                   	push   ebx
  404453:	89 c3                	mov    ebx,eax
  404455:	83 ec 40             	sub    esp,0x40
  404458:	8b 40 0c             	mov    eax,DWORD PTR [eax+0xc]
  40445b:	85 c0                	test   eax,eax
  40445d:	0f 88 9d 00 00 00    	js     404500 <___pformat_float+0xb0>
  404463:	db 6c 24 50          	fld    TBYTE PTR [esp+0x50]
  404467:	89 44 24 10          	mov    DWORD PTR [esp+0x10],eax
  40446b:	8d 54 24 28          	lea    edx,[esp+0x28]
  40446f:	db 7c 24 30          	fstp   TBYTE PTR [esp+0x30]
  404473:	8b 44 24 30          	mov    eax,DWORD PTR [esp+0x30]
  404477:	89 54 24 18          	mov    DWORD PTR [esp+0x18],edx
  40447b:	8d 54 24 2c          	lea    edx,[esp+0x2c]
  40447f:	89 54 24 14          	mov    DWORD PTR [esp+0x14],edx
  404483:	89 04 24             	mov    DWORD PTR [esp],eax
  404486:	8b 44 24 34          	mov    eax,DWORD PTR [esp+0x34]
  40448a:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
  40448e:	8b 44 24 38          	mov    eax,DWORD PTR [esp+0x38]
  404492:	89 44 24 08          	mov    DWORD PTR [esp+0x8],eax
  404496:	8b 44 24 3c          	mov    eax,DWORD PTR [esp+0x3c]
  40449a:	89 44 24 0c          	mov    DWORD PTR [esp+0xc],eax
  40449e:	b8 03 00 00 00       	mov    eax,0x3
  4044a3:	e8 38 f2 ff ff       	call   4036e0 <___pformat_cvt>
  4044a8:	8b 4c 24 2c          	mov    ecx,DWORD PTR [esp+0x2c]
  4044ac:	81 f9 00 80 ff ff    	cmp    ecx,0xffff8000
  4044b2:	89 c7                	mov    edi,eax
  4044b4:	74 5b                	je     404511 <___pformat_float+0xc1>
  4044b6:	89 c2                	mov    edx,eax
  4044b8:	8b 44 24 28          	mov    eax,DWORD PTR [esp+0x28]
  4044bc:	89 1c 24             	mov    DWORD PTR [esp],ebx
  4044bf:	e8 dc fa ff ff       	call   403fa0 <___pformat_emit_float>
  4044c4:	8b 43 08             	mov    eax,DWORD PTR [ebx+0x8]
  4044c7:	8d 50 ff             	lea    edx,[eax-0x1]
  4044ca:	85 c0                	test   eax,eax
  4044cc:	89 53 08             	mov    DWORD PTR [ebx+0x8],edx
  4044cf:	7e 19                	jle    4044ea <___pformat_float+0x9a>
  4044d1:	89 da                	mov    edx,ebx
  4044d3:	b8 20 00 00 00       	mov    eax,0x20
  4044d8:	e8 03 f3 ff ff       	call   4037e0 <___pformat_putc>
  4044dd:	8b 4b 08             	mov    ecx,DWORD PTR [ebx+0x8]
  4044e0:	8d 71 ff             	lea    esi,[ecx-0x1]
  4044e3:	85 c9                	test   ecx,ecx
  4044e5:	89 73 08             	mov    DWORD PTR [ebx+0x8],esi
  4044e8:	7f e7                	jg     4044d1 <___pformat_float+0x81>
  4044ea:	89 3c 24             	mov    DWORD PTR [esp],edi
  4044ed:	e8 ae 2c 00 00       	call   4071a0 <___freedtoa>
  4044f2:	83 c4 40             	add    esp,0x40
  4044f5:	5b                   	pop    ebx
  4044f6:	5e                   	pop    esi
  4044f7:	5f                   	pop    edi
  4044f8:	c3                   	ret    
  4044f9:	8d b4 26 00 00 00 00 	lea    esi,[esi+eiz*1+0x0]
  404500:	c7 43 0c 06 00 00 00 	mov    DWORD PTR [ebx+0xc],0x6
  404507:	b8 06 00 00 00       	mov    eax,0x6
  40450c:	e9 52 ff ff ff       	jmp    404463 <___pformat_float+0x13>
  404511:	89 c2                	mov    edx,eax
  404513:	8b 44 24 28          	mov    eax,DWORD PTR [esp+0x28]
  404517:	89 d9                	mov    ecx,ebx
  404519:	e8 e2 f4 ff ff       	call   403a00 <___pformat_emit_inf_or_nan>
  40451e:	89 3c 24             	mov    DWORD PTR [esp],edi
  404521:	e8 7a 2c 00 00       	call   4071a0 <___freedtoa>
  404526:	83 c4 40             	add    esp,0x40
  404529:	5b                   	pop    ebx
  40452a:	5e                   	pop    esi
  40452b:	5f                   	pop    edi
  40452c:	c3                   	ret    
  40452d:	8d 76 00             	lea    esi,[esi+0x0]

00404530 <___pformat_gfloat>:
  404530:	57                   	push   edi
  404531:	56                   	push   esi
  404532:	53                   	push   ebx
  404533:	89 c3                	mov    ebx,eax
  404535:	83 ec 40             	sub    esp,0x40
  404538:	8b 40 0c             	mov    eax,DWORD PTR [eax+0xc]
  40453b:	85 c0                	test   eax,eax
  40453d:	0f 88 1d 01 00 00    	js     404660 <___pformat_gfloat+0x130>
  404543:	0f 84 fa 00 00 00    	je     404643 <___pformat_gfloat+0x113>
  404549:	db 6c 24 50          	fld    TBYTE PTR [esp+0x50]
  40454d:	89 44 24 10          	mov    DWORD PTR [esp+0x10],eax
  404551:	8d 54 24 28          	lea    edx,[esp+0x28]
  404555:	db 7c 24 30          	fstp   TBYTE PTR [esp+0x30]
  404559:	8b 44 24 30          	mov    eax,DWORD PTR [esp+0x30]
  40455d:	89 54 24 18          	mov    DWORD PTR [esp+0x18],edx
  404561:	8d 54 24 2c          	lea    edx,[esp+0x2c]
  404565:	89 54 24 14          	mov    DWORD PTR [esp+0x14],edx
  404569:	89 04 24             	mov    DWORD PTR [esp],eax
  40456c:	8b 44 24 34          	mov    eax,DWORD PTR [esp+0x34]
  404570:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
  404574:	8b 44 24 38          	mov    eax,DWORD PTR [esp+0x38]
  404578:	89 44 24 08          	mov    DWORD PTR [esp+0x8],eax
  40457c:	8b 44 24 3c          	mov    eax,DWORD PTR [esp+0x3c]
  404580:	89 44 24 0c          	mov    DWORD PTR [esp+0xc],eax
  404584:	b8 02 00 00 00       	mov    eax,0x2
  404589:	e8 52 f1 ff ff       	call   4036e0 <___pformat_cvt>
  40458e:	8b 74 24 2c          	mov    esi,DWORD PTR [esp+0x2c]
  404592:	81 fe 00 80 ff ff    	cmp    esi,0xffff8000
  404598:	89 c7                	mov    edi,eax
  40459a:	0f 84 e0 00 00 00    	je     404680 <___pformat_gfloat+0x150>
  4045a0:	83 fe fd             	cmp    esi,0xfffffffd
  4045a3:	7c 6b                	jl     404610 <___pformat_gfloat+0xe0>
  4045a5:	8b 43 0c             	mov    eax,DWORD PTR [ebx+0xc]
  4045a8:	39 c6                	cmp    esi,eax
  4045aa:	7f 64                	jg     404610 <___pformat_gfloat+0xe0>
  4045ac:	f6 43 05 08          	test   BYTE PTR [ebx+0x5],0x8
  4045b0:	0f 85 bb 00 00 00    	jne    404671 <___pformat_gfloat+0x141>
  4045b6:	89 3c 24             	mov    DWORD PTR [esp],edi
  4045b9:	e8 f2 3a 00 00       	call   4080b0 <_strlen>
  4045be:	29 f0                	sub    eax,esi
  4045c0:	85 c0                	test   eax,eax
  4045c2:	89 43 0c             	mov    DWORD PTR [ebx+0xc],eax
  4045c5:	0f 88 c5 00 00 00    	js     404690 <___pformat_gfloat+0x160>
  4045cb:	8b 44 24 28          	mov    eax,DWORD PTR [esp+0x28]
  4045cf:	89 fa                	mov    edx,edi
  4045d1:	89 f1                	mov    ecx,esi
  4045d3:	89 1c 24             	mov    DWORD PTR [esp],ebx
  4045d6:	e8 c5 f9 ff ff       	call   403fa0 <___pformat_emit_float>
  4045db:	8b 43 08             	mov    eax,DWORD PTR [ebx+0x8]
  4045de:	8d 50 ff             	lea    edx,[eax-0x1]
  4045e1:	85 c0                	test   eax,eax
  4045e3:	89 53 08             	mov    DWORD PTR [ebx+0x8],edx
  4045e6:	7e 4c                	jle    404634 <___pformat_gfloat+0x104>
  4045e8:	89 da                	mov    edx,ebx
  4045ea:	b8 20 00 00 00       	mov    eax,0x20
  4045ef:	e8 ec f1 ff ff       	call   4037e0 <___pformat_putc>
  4045f4:	8b 4b 08             	mov    ecx,DWORD PTR [ebx+0x8]
  4045f7:	8d 71 ff             	lea    esi,[ecx-0x1]
  4045fa:	85 c9                	test   ecx,ecx
  4045fc:	89 73 08             	mov    DWORD PTR [ebx+0x8],esi
  4045ff:	7f e7                	jg     4045e8 <___pformat_gfloat+0xb8>
  404601:	89 3c 24             	mov    DWORD PTR [esp],edi
  404604:	e8 97 2b 00 00       	call   4071a0 <___freedtoa>
  404609:	83 c4 40             	add    esp,0x40
  40460c:	5b                   	pop    ebx
  40460d:	5e                   	pop    esi
  40460e:	5f                   	pop    edi
  40460f:	c3                   	ret    
  404610:	f6 43 05 08          	test   BYTE PTR [ebx+0x5],0x8
  404614:	75 3e                	jne    404654 <___pformat_gfloat+0x124>
  404616:	89 3c 24             	mov    DWORD PTR [esp],edi
  404619:	e8 92 3a 00 00       	call   4080b0 <_strlen>
  40461e:	83 e8 01             	sub    eax,0x1
  404621:	89 43 0c             	mov    DWORD PTR [ebx+0xc],eax
  404624:	8b 44 24 28          	mov    eax,DWORD PTR [esp+0x28]
  404628:	89 f1                	mov    ecx,esi
  40462a:	89 fa                	mov    edx,edi
  40462c:	89 1c 24             	mov    DWORD PTR [esp],ebx
  40462f:	e8 9c fc ff ff       	call   4042d0 <___pformat_emit_efloat>
  404634:	89 3c 24             	mov    DWORD PTR [esp],edi
  404637:	e8 64 2b 00 00       	call   4071a0 <___freedtoa>
  40463c:	83 c4 40             	add    esp,0x40
  40463f:	5b                   	pop    ebx
  404640:	5e                   	pop    esi
  404641:	5f                   	pop    edi
  404642:	c3                   	ret    
  404643:	c7 43 0c 01 00 00 00 	mov    DWORD PTR [ebx+0xc],0x1
  40464a:	b8 01 00 00 00       	mov    eax,0x1
  40464f:	e9 f5 fe ff ff       	jmp    404549 <___pformat_gfloat+0x19>
  404654:	83 6b 0c 01          	sub    DWORD PTR [ebx+0xc],0x1
  404658:	eb ca                	jmp    404624 <___pformat_gfloat+0xf4>
  40465a:	8d b6 00 00 00 00    	lea    esi,[esi+0x0]
  404660:	c7 43 0c 06 00 00 00 	mov    DWORD PTR [ebx+0xc],0x6
  404667:	b8 06 00 00 00       	mov    eax,0x6
  40466c:	e9 d8 fe ff ff       	jmp    404549 <___pformat_gfloat+0x19>
  404671:	29 f0                	sub    eax,esi
  404673:	89 43 0c             	mov    DWORD PTR [ebx+0xc],eax
  404676:	e9 50 ff ff ff       	jmp    4045cb <___pformat_gfloat+0x9b>
  40467b:	90                   	nop
  40467c:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  404680:	89 c2                	mov    edx,eax
  404682:	8b 44 24 28          	mov    eax,DWORD PTR [esp+0x28]
  404686:	89 d9                	mov    ecx,ebx
  404688:	e8 73 f3 ff ff       	call   403a00 <___pformat_emit_inf_or_nan>
  40468d:	eb a5                	jmp    404634 <___pformat_gfloat+0x104>
  40468f:	90                   	nop
  404690:	8b 53 08             	mov    edx,DWORD PTR [ebx+0x8]
  404693:	85 d2                	test   edx,edx
  404695:	0f 8e 30 ff ff ff    	jle    4045cb <___pformat_gfloat+0x9b>
  40469b:	01 d0                	add    eax,edx
  40469d:	89 43 08             	mov    DWORD PTR [ebx+0x8],eax
  4046a0:	e9 26 ff ff ff       	jmp    4045cb <___pformat_gfloat+0x9b>
  4046a5:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  4046a9:	8d bc 27 00 00 00 00 	lea    edi,[edi+eiz*1+0x0]

004046b0 <___pformat_xldouble>:
  4046b0:	55                   	push   ebp
  4046b1:	89 e5                	mov    ebp,esp
  4046b3:	57                   	push   edi
  4046b4:	89 c7                	mov    edi,eax
  4046b6:	56                   	push   esi
  4046b7:	53                   	push   ebx
  4046b8:	83 ec 6c             	sub    esp,0x6c
  4046bb:	db 6d 08             	fld    TBYTE PTR [ebp+0x8]
  4046be:	d9 c0                	fld    st(0)
  4046c0:	db 7d c0             	fstp   TBYTE PTR [ebp-0x40]
  4046c3:	d9 e5                	fxam   
  4046c5:	9b df e0             	fstsw  ax
  4046c8:	66 25 00 45          	and    ax,0x4500
  4046cc:	66 3d 00 01          	cmp    ax,0x100
  4046d0:	0f 84 1f 05 00 00    	je     404bf5 <___pformat_xldouble+0x545>
  4046d6:	0f b7 55 c8          	movzx  edx,WORD PTR [ebp-0x38]
  4046da:	89 d3                	mov    ebx,edx
  4046dc:	81 e3 00 80 00 00    	and    ebx,0x8000
  4046e2:	0f 85 48 01 00 00    	jne    404830 <___pformat_xldouble+0x180>
  4046e8:	d9 e5                	fxam   
  4046ea:	9b df e0             	fstsw  ax
  4046ed:	dd d8                	fstp   st(0)
  4046ef:	66 25 00 45          	and    ax,0x4500
  4046f3:	66 3d 00 05          	cmp    ax,0x500
  4046f7:	0f 84 16 05 00 00    	je     404c13 <___pformat_xldouble+0x563>
  4046fd:	66 81 e2 ff 7f       	and    dx,0x7fff
  404702:	0f 84 b8 01 00 00    	je     4048c0 <___pformat_xldouble+0x210>
  404708:	8d b2 01 c0 ff ff    	lea    esi,[edx-0x3fff]
  40470e:	8b 45 c0             	mov    eax,DWORD PTR [ebp-0x40]
  404711:	8b 55 c4             	mov    edx,DWORD PTR [ebp-0x3c]
  404714:	8b 5f 0c             	mov    ebx,DWORD PTR [edi+0xc]
  404717:	83 fb 0e             	cmp    ebx,0xe
  40471a:	0f 86 26 01 00 00    	jbe    404846 <___pformat_xldouble+0x196>
  404720:	89 d1                	mov    ecx,edx
  404722:	09 c1                	or     ecx,eax
  404724:	0f 84 fc 04 00 00    	je     404c26 <___pformat_xldouble+0x576>
  40472a:	8d 4d d6             	lea    ecx,[ebp-0x2a]
  40472d:	89 4d a4             	mov    DWORD PTR [ebp-0x5c],ecx
  404730:	89 4d ac             	mov    DWORD PTR [ebp-0x54],ecx
  404733:	89 7d a8             	mov    DWORD PTR [ebp-0x58],edi
  404736:	eb 5e                	jmp    404796 <___pformat_xldouble+0xe6>
  404738:	8b 4d a8             	mov    ecx,DWORD PTR [ebp-0x58]
  40473b:	8b 49 0c             	mov    ecx,DWORD PTR [ecx+0xc]
  40473e:	85 c9                	test   ecx,ecx
  404740:	7e 09                	jle    40474b <___pformat_xldouble+0x9b>
  404742:	8b 5d a8             	mov    ebx,DWORD PTR [ebp-0x58]
  404745:	83 e9 01             	sub    ecx,0x1
  404748:	89 4b 0c             	mov    DWORD PTR [ebx+0xc],ecx
  40474b:	8b 4d ac             	mov    ecx,DWORD PTR [ebp-0x54]
  40474e:	0f ac d0 04          	shrd   eax,edx,0x4
  404752:	c1 ea 04             	shr    edx,0x4
  404755:	85 ff                	test   edi,edi
  404757:	89 4d b0             	mov    DWORD PTR [ebp-0x50],ecx
  40475a:	0f 84 a8 00 00 00    	je     404808 <___pformat_xldouble+0x158>
  404760:	8b 4d b0             	mov    ecx,DWORD PTR [ebp-0x50]
  404763:	83 c1 01             	add    ecx,0x1
  404766:	83 ff 09             	cmp    edi,0x9
  404769:	89 4d ac             	mov    DWORD PTR [ebp-0x54],ecx
  40476c:	0f 8e b5 00 00 00    	jle    404827 <___pformat_xldouble+0x177>
  404772:	8d 4f 37             	lea    ecx,[edi+0x37]
  404775:	8b 7d a8             	mov    edi,DWORD PTR [ebp-0x58]
  404778:	8b 7f 04             	mov    edi,DWORD PTR [edi+0x4]
  40477b:	89 7d a0             	mov    DWORD PTR [ebp-0x60],edi
  40477e:	0f b6 5d a0          	movzx  ebx,BYTE PTR [ebp-0x60]
  404782:	83 e3 20             	and    ebx,0x20
  404785:	09 d9                	or     ecx,ebx
  404787:	8b 7d b0             	mov    edi,DWORD PTR [ebp-0x50]
  40478a:	88 0f                	mov    BYTE PTR [edi],cl
  40478c:	89 d7                	mov    edi,edx
  40478e:	09 c7                	or     edi,eax
  404790:	0f 84 60 01 00 00    	je     4048f6 <___pformat_xldouble+0x246>
  404796:	89 c7                	mov    edi,eax
  404798:	89 c1                	mov    ecx,eax
  40479a:	83 e7 0f             	and    edi,0xf
  40479d:	89 fb                	mov    ebx,edi
  40479f:	31 f9                	xor    ecx,edi
  4047a1:	c1 fb 1f             	sar    ebx,0x1f
  4047a4:	31 d3                	xor    ebx,edx
  4047a6:	09 cb                	or     ebx,ecx
  4047a8:	75 8e                	jne    404738 <___pformat_xldouble+0x88>
  4047aa:	8b 4d a4             	mov    ecx,DWORD PTR [ebp-0x5c]
  4047ad:	39 4d ac             	cmp    DWORD PTR [ebp-0x54],ecx
  4047b0:	77 1e                	ja     4047d0 <___pformat_xldouble+0x120>
  4047b2:	8b 4d a8             	mov    ecx,DWORD PTR [ebp-0x58]
  4047b5:	f6 41 05 08          	test   BYTE PTR [ecx+0x5],0x8
  4047b9:	75 15                	jne    4047d0 <___pformat_xldouble+0x120>
  4047bb:	8b 4d ac             	mov    ecx,DWORD PTR [ebp-0x54]
  4047be:	89 4d b0             	mov    DWORD PTR [ebp-0x50],ecx
  4047c1:	8b 4d a8             	mov    ecx,DWORD PTR [ebp-0x58]
  4047c4:	8b 59 0c             	mov    ebx,DWORD PTR [ecx+0xc]
  4047c7:	85 db                	test   ebx,ebx
  4047c9:	7e 11                	jle    4047dc <___pformat_xldouble+0x12c>
  4047cb:	90                   	nop
  4047cc:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  4047d0:	8b 4d ac             	mov    ecx,DWORD PTR [ebp-0x54]
  4047d3:	8d 59 01             	lea    ebx,[ecx+0x1]
  4047d6:	89 5d b0             	mov    DWORD PTR [ebp-0x50],ebx
  4047d9:	c6 01 2e             	mov    BYTE PTR [ecx],0x2e
  4047dc:	89 c1                	mov    ecx,eax
  4047de:	83 f1 01             	xor    ecx,0x1
  4047e1:	09 d1                	or     ecx,edx
  4047e3:	74 17                	je     4047fc <___pformat_xldouble+0x14c>
  4047e5:	8d 4e ff             	lea    ecx,[esi-0x1]
  4047e8:	0f ac d0 01          	shrd   eax,edx,0x1
  4047ec:	89 ce                	mov    esi,ecx
  4047ee:	89 c3                	mov    ebx,eax
  4047f0:	d1 ea                	shr    edx,1
  4047f2:	83 f3 01             	xor    ebx,0x1
  4047f5:	09 d3                	or     ebx,edx
  4047f7:	8d 4e ff             	lea    ecx,[esi-0x1]
  4047fa:	75 ec                	jne    4047e8 <___pformat_xldouble+0x138>
  4047fc:	31 c0                	xor    eax,eax
  4047fe:	31 d2                	xor    edx,edx
  404800:	85 ff                	test   edi,edi
  404802:	0f 85 58 ff ff ff    	jne    404760 <___pformat_xldouble+0xb0>
  404808:	8b 4d a4             	mov    ecx,DWORD PTR [ebp-0x5c]
  40480b:	39 4d b0             	cmp    DWORD PTR [ebp-0x50],ecx
  40480e:	77 0e                	ja     40481e <___pformat_xldouble+0x16e>
  404810:	8b 4d a8             	mov    ecx,DWORD PTR [ebp-0x58]
  404813:	8b 49 0c             	mov    ecx,DWORD PTR [ecx+0xc]
  404816:	85 c9                	test   ecx,ecx
  404818:	0f 88 b7 01 00 00    	js     4049d5 <___pformat_xldouble+0x325>
  40481e:	8b 4d b0             	mov    ecx,DWORD PTR [ebp-0x50]
  404821:	83 c1 01             	add    ecx,0x1
  404824:	89 4d ac             	mov    DWORD PTR [ebp-0x54],ecx
  404827:	8d 4f 30             	lea    ecx,[edi+0x30]
  40482a:	e9 58 ff ff ff       	jmp    404787 <___pformat_xldouble+0xd7>
  40482f:	90                   	nop
  404830:	81 4f 04 80 00 00 00 	or     DWORD PTR [edi+0x4],0x80
  404837:	e9 ac fe ff ff       	jmp    4046e8 <___pformat_xldouble+0x38>
  40483c:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  404840:	0f a4 c2 01          	shld   edx,eax,0x1
  404844:	01 c0                	add    eax,eax
  404846:	85 d2                	test   edx,edx
  404848:	79 f6                	jns    404840 <___pformat_xldouble+0x190>
  40484a:	b9 0e 00 00 00       	mov    ecx,0xe
  40484f:	0f ac d0 01          	shrd   eax,edx,0x1
  404853:	29 d9                	sub    ecx,ebx
  404855:	d1 ea                	shr    edx,1
  404857:	c1 e1 02             	shl    ecx,0x2
  40485a:	89 45 b0             	mov    DWORD PTR [ebp-0x50],eax
  40485d:	b8 04 00 00 00       	mov    eax,0x4
  404862:	89 55 b4             	mov    DWORD PTR [ebp-0x4c],edx
  404865:	31 d2                	xor    edx,edx
  404867:	0f a5 c2             	shld   edx,eax,cl
  40486a:	d3 e0                	shl    eax,cl
  40486c:	f6 c1 20             	test   cl,0x20
  40486f:	74 04                	je     404875 <___pformat_xldouble+0x1c5>
  404871:	89 c2                	mov    edx,eax
  404873:	31 c0                	xor    eax,eax
  404875:	01 45 b0             	add    DWORD PTR [ebp-0x50],eax
  404878:	11 55 b4             	adc    DWORD PTR [ebp-0x4c],edx
  40487b:	8b 55 b4             	mov    edx,DWORD PTR [ebp-0x4c]
  40487e:	8b 45 b0             	mov    eax,DWORD PTR [ebp-0x50]
  404881:	85 d2                	test   edx,edx
  404883:	0f 88 64 03 00 00    	js     404bed <___pformat_xldouble+0x53d>
  404889:	0f a4 c2 01          	shld   edx,eax,0x1
  40488d:	01 c0                	add    eax,eax
  40488f:	89 45 b0             	mov    DWORD PTR [ebp-0x50],eax
  404892:	89 55 b4             	mov    DWORD PTR [ebp-0x4c],edx
  404895:	8b 55 b4             	mov    edx,DWORD PTR [ebp-0x4c]
  404898:	b9 0f 00 00 00       	mov    ecx,0xf
  40489d:	8b 45 b0             	mov    eax,DWORD PTR [ebp-0x50]
  4048a0:	29 d9                	sub    ecx,ebx
  4048a2:	c1 e1 02             	shl    ecx,0x2
  4048a5:	0f ad d0             	shrd   eax,edx,cl
  4048a8:	d3 ea                	shr    edx,cl
  4048aa:	f6 c1 20             	test   cl,0x20
  4048ad:	0f 84 77 fe ff ff    	je     40472a <___pformat_xldouble+0x7a>
  4048b3:	89 d0                	mov    eax,edx
  4048b5:	31 d2                	xor    edx,edx
  4048b7:	e9 6e fe ff ff       	jmp    40472a <___pformat_xldouble+0x7a>
  4048bc:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  4048c0:	8b 55 c4             	mov    edx,DWORD PTR [ebp-0x3c]
  4048c3:	8b 45 c0             	mov    eax,DWORD PTR [ebp-0x40]
  4048c6:	89 d6                	mov    esi,edx
  4048c8:	09 c6                	or     esi,eax
  4048ca:	0f 84 d7 02 00 00    	je     404ba7 <___pformat_xldouble+0x4f7>
  4048d0:	85 d2                	test   edx,edx
  4048d2:	0f 88 84 03 00 00    	js     404c5c <___pformat_xldouble+0x5ac>
  4048d8:	b9 01 c0 ff ff       	mov    ecx,0xffffc001
  4048dd:	8d 76 00             	lea    esi,[esi+0x0]
  4048e0:	0f a4 c2 01          	shld   edx,eax,0x1
  4048e4:	89 cb                	mov    ebx,ecx
  4048e6:	01 c0                	add    eax,eax
  4048e8:	83 e9 01             	sub    ecx,0x1
  4048eb:	85 d2                	test   edx,edx
  4048ed:	79 f1                	jns    4048e0 <___pformat_xldouble+0x230>
  4048ef:	89 de                	mov    esi,ebx
  4048f1:	e9 1e fe ff ff       	jmp    404714 <___pformat_xldouble+0x64>
  4048f6:	8b 45 a4             	mov    eax,DWORD PTR [ebp-0x5c]
  4048f9:	39 45 ac             	cmp    DWORD PTR [ebp-0x54],eax
  4048fc:	8b 7d a8             	mov    edi,DWORD PTR [ebp-0x58]
  4048ff:	0f 84 52 03 00 00    	je     404c57 <___pformat_xldouble+0x5a7>
  404905:	8b 47 04             	mov    eax,DWORD PTR [edi+0x4]
  404908:	89 45 b0             	mov    DWORD PTR [ebp-0x50],eax
  40490b:	8b 47 08             	mov    eax,DWORD PTR [edi+0x8]
  40490e:	85 c0                	test   eax,eax
  404910:	89 45 a0             	mov    DWORD PTR [ebp-0x60],eax
  404913:	0f 8e 7c 02 00 00    	jle    404b95 <___pformat_xldouble+0x4e5>
  404919:	8b 57 0c             	mov    edx,DWORD PTR [edi+0xc]
  40491c:	0f bf f6             	movsx  esi,si
  40491f:	8b 45 ac             	mov    eax,DWORD PTR [ebp-0x54]
  404922:	2b 45 a4             	sub    eax,DWORD PTR [ebp-0x5c]
  404925:	89 75 a8             	mov    DWORD PTR [ebp-0x58],esi
  404928:	85 d2                	test   edx,edx
  40492a:	7e 02                	jle    40492e <___pformat_xldouble+0x27e>
  40492c:	01 d0                	add    eax,edx
  40492e:	8b 55 b0             	mov    edx,DWORD PTR [ebp-0x50]
  404931:	81 e2 c0 01 00 00    	and    edx,0x1c0
  404937:	83 fa 01             	cmp    edx,0x1
  40493a:	19 d2                	sbb    edx,edx
  40493c:	8d 74 10 06          	lea    esi,[eax+edx*1+0x6]
  404940:	8b 45 a8             	mov    eax,DWORD PTR [ebp-0x58]
  404943:	ba 67 66 66 66       	mov    edx,0x66666667
  404948:	f7 ea                	imul   edx
  40494a:	8b 45 a8             	mov    eax,DWORD PTR [ebp-0x58]
  40494d:	c1 fa 02             	sar    edx,0x2
  404950:	c1 f8 1f             	sar    eax,0x1f
  404953:	29 c2                	sub    edx,eax
  404955:	89 d1                	mov    ecx,edx
  404957:	0f 84 ee 02 00 00    	je     404c4b <___pformat_xldouble+0x59b>
  40495d:	bb 02 00 00 00       	mov    ebx,0x2
  404962:	b8 67 66 66 66       	mov    eax,0x66666667
  404967:	83 c6 01             	add    esi,0x1
  40496a:	f7 e9                	imul   ecx
  40496c:	83 c3 01             	add    ebx,0x1
  40496f:	c1 f9 1f             	sar    ecx,0x1f
  404972:	c1 fa 02             	sar    edx,0x2
  404975:	29 ca                	sub    edx,ecx
  404977:	89 d1                	mov    ecx,edx
  404979:	75 e7                	jne    404962 <___pformat_xldouble+0x2b2>
  40497b:	0f bf c3             	movsx  eax,bx
  40497e:	89 45 9c             	mov    DWORD PTR [ebp-0x64],eax
  404981:	39 75 a0             	cmp    DWORD PTR [ebp-0x60],esi
  404984:	7e 5a                	jle    4049e0 <___pformat_xldouble+0x330>
  404986:	8b 45 a0             	mov    eax,DWORD PTR [ebp-0x60]
  404989:	29 f0                	sub    eax,esi
  40498b:	f7 45 b0 00 06 00 00 	test   DWORD PTR [ebp-0x50],0x600
  404992:	0f 85 1a 02 00 00    	jne    404bb2 <___pformat_xldouble+0x502>
  404998:	8d 50 ff             	lea    edx,[eax-0x1]
  40499b:	85 c0                	test   eax,eax
  40499d:	89 57 08             	mov    DWORD PTR [edi+0x8],edx
  4049a0:	7e 45                	jle    4049e7 <___pformat_xldouble+0x337>
  4049a2:	89 fa                	mov    edx,edi
  4049a4:	b8 20 00 00 00       	mov    eax,0x20
  4049a9:	e8 32 ee ff ff       	call   4037e0 <___pformat_putc>
  4049ae:	8b 47 08             	mov    eax,DWORD PTR [edi+0x8]
  4049b1:	8d 50 ff             	lea    edx,[eax-0x1]
  4049b4:	85 c0                	test   eax,eax
  4049b6:	89 57 08             	mov    DWORD PTR [edi+0x8],edx
  4049b9:	7f e7                	jg     4049a2 <___pformat_xldouble+0x2f2>
  4049bb:	8b 47 04             	mov    eax,DWORD PTR [edi+0x4]
  4049be:	89 45 b0             	mov    DWORD PTR [ebp-0x50],eax
  4049c1:	f6 45 b0 80          	test   BYTE PTR [ebp-0x50],0x80
  4049c5:	74 26                	je     4049ed <___pformat_xldouble+0x33d>
  4049c7:	89 fa                	mov    edx,edi
  4049c9:	b8 2d 00 00 00       	mov    eax,0x2d
  4049ce:	e8 0d ee ff ff       	call   4037e0 <___pformat_putc>
  4049d3:	eb 2f                	jmp    404a04 <___pformat_xldouble+0x354>
  4049d5:	8b 7d b0             	mov    edi,DWORD PTR [ebp-0x50]
  4049d8:	89 7d ac             	mov    DWORD PTR [ebp-0x54],edi
  4049db:	e9 ac fd ff ff       	jmp    40478c <___pformat_xldouble+0xdc>
  4049e0:	c7 47 08 ff ff ff ff 	mov    DWORD PTR [edi+0x8],0xffffffff
  4049e7:	f6 45 b0 80          	test   BYTE PTR [ebp-0x50],0x80
  4049eb:	75 da                	jne    4049c7 <___pformat_xldouble+0x317>
  4049ed:	f7 45 b0 00 01 00 00 	test   DWORD PTR [ebp-0x50],0x100
  4049f4:	0f 85 c0 01 00 00    	jne    404bba <___pformat_xldouble+0x50a>
  4049fa:	f6 45 b0 40          	test   BYTE PTR [ebp-0x50],0x40
  4049fe:	0f 85 d8 01 00 00    	jne    404bdc <___pformat_xldouble+0x52c>
  404a04:	89 fa                	mov    edx,edi
  404a06:	b8 30 00 00 00       	mov    eax,0x30
  404a0b:	e8 d0 ed ff ff       	call   4037e0 <___pformat_putc>
  404a10:	8b 47 04             	mov    eax,DWORD PTR [edi+0x4]
  404a13:	89 fa                	mov    edx,edi
  404a15:	83 e0 20             	and    eax,0x20
  404a18:	83 c8 58             	or     eax,0x58
  404a1b:	e8 c0 ed ff ff       	call   4037e0 <___pformat_putc>
  404a20:	8b 47 08             	mov    eax,DWORD PTR [edi+0x8]
  404a23:	85 c0                	test   eax,eax
  404a25:	7e 25                	jle    404a4c <___pformat_xldouble+0x39c>
  404a27:	f6 47 05 02          	test   BYTE PTR [edi+0x5],0x2
  404a2b:	74 1f                	je     404a4c <___pformat_xldouble+0x39c>
  404a2d:	83 e8 01             	sub    eax,0x1
  404a30:	89 47 08             	mov    DWORD PTR [edi+0x8],eax
  404a33:	89 fa                	mov    edx,edi
  404a35:	b8 30 00 00 00       	mov    eax,0x30
  404a3a:	e8 a1 ed ff ff       	call   4037e0 <___pformat_putc>
  404a3f:	8b 47 08             	mov    eax,DWORD PTR [edi+0x8]
  404a42:	8d 50 ff             	lea    edx,[eax-0x1]
  404a45:	85 c0                	test   eax,eax
  404a47:	89 57 08             	mov    DWORD PTR [edi+0x8],edx
  404a4a:	7f e7                	jg     404a33 <___pformat_xldouble+0x383>
  404a4c:	8b 45 a4             	mov    eax,DWORD PTR [ebp-0x5c]
  404a4f:	39 45 ac             	cmp    DWORD PTR [ebp-0x54],eax
  404a52:	8b 5d ac             	mov    ebx,DWORD PTR [ebp-0x54]
  404a55:	77 19                	ja     404a70 <___pformat_xldouble+0x3c0>
  404a57:	e9 a1 00 00 00       	jmp    404afd <___pformat_xldouble+0x44d>
  404a5c:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  404a60:	89 fa                	mov    edx,edi
  404a62:	e8 79 ed ff ff       	call   4037e0 <___pformat_putc>
  404a67:	3b 5d a4             	cmp    ebx,DWORD PTR [ebp-0x5c]
  404a6a:	0f 84 8d 00 00 00    	je     404afd <___pformat_xldouble+0x44d>
  404a70:	83 eb 01             	sub    ebx,0x1
  404a73:	0f be 03             	movsx  eax,BYTE PTR [ebx]
  404a76:	83 f8 2e             	cmp    eax,0x2e
  404a79:	75 e5                	jne    404a60 <___pformat_xldouble+0x3b0>
  404a7b:	83 7f 10 fd          	cmp    DWORD PTR [edi+0x10],0xfffffffd
  404a7f:	0f 84 cc 00 00 00    	je     404b51 <___pformat_xldouble+0x4a1>
  404a85:	0f b7 57 14          	movzx  edx,WORD PTR [edi+0x14]
  404a89:	66 85 d2             	test   dx,dx
  404a8c:	0f 84 ae 00 00 00    	je     404b40 <___pformat_xldouble+0x490>
  404a92:	8b 47 10             	mov    eax,DWORD PTR [edi+0x10]
  404a95:	89 65 b0             	mov    DWORD PTR [ebp-0x50],esp
  404a98:	83 c0 0f             	add    eax,0xf
  404a9b:	83 e0 f0             	and    eax,0xfffffff0
  404a9e:	e8 cd d5 ff ff       	call   402070 <___chkstk_ms>
  404aa3:	29 c4                	sub    esp,eax
  404aa5:	8d 74 24 10          	lea    esi,[esp+0x10]
  404aa9:	8d 45 bc             	lea    eax,[ebp-0x44]
  404aac:	c7 45 bc 00 00 00 00 	mov    DWORD PTR [ebp-0x44],0x0
  404ab3:	89 44 24 08          	mov    DWORD PTR [esp+0x8],eax
  404ab7:	89 54 24 04          	mov    DWORD PTR [esp+0x4],edx
  404abb:	89 34 24             	mov    DWORD PTR [esp],esi
  404abe:	e8 5d 20 00 00       	call   406b20 <_wcrtomb>
  404ac3:	85 c0                	test   eax,eax
  404ac5:	0f 8e 00 01 00 00    	jle    404bcb <___pformat_xldouble+0x51b>
  404acb:	01 f0                	add    eax,esi
  404acd:	89 5d ac             	mov    DWORD PTR [ebp-0x54],ebx
  404ad0:	89 f3                	mov    ebx,esi
  404ad2:	89 c6                	mov    esi,eax
  404ad4:	83 c3 01             	add    ebx,0x1
  404ad7:	0f be 43 ff          	movsx  eax,BYTE PTR [ebx-0x1]
  404adb:	89 fa                	mov    edx,edi
  404add:	e8 fe ec ff ff       	call   4037e0 <___pformat_putc>
  404ae2:	39 f3                	cmp    ebx,esi
  404ae4:	75 ee                	jne    404ad4 <___pformat_xldouble+0x424>
  404ae6:	8b 5d ac             	mov    ebx,DWORD PTR [ebp-0x54]
  404ae9:	8b 65 b0             	mov    esp,DWORD PTR [ebp-0x50]
  404aec:	e9 76 ff ff ff       	jmp    404a67 <___pformat_xldouble+0x3b7>
  404af1:	89 fa                	mov    edx,edi
  404af3:	b8 30 00 00 00       	mov    eax,0x30
  404af8:	e8 e3 ec ff ff       	call   4037e0 <___pformat_putc>
  404afd:	8b 47 0c             	mov    eax,DWORD PTR [edi+0xc]
  404b00:	8d 50 ff             	lea    edx,[eax-0x1]
  404b03:	85 c0                	test   eax,eax
  404b05:	89 57 0c             	mov    DWORD PTR [edi+0xc],edx
  404b08:	7f e7                	jg     404af1 <___pformat_xldouble+0x441>
  404b0a:	8b 47 04             	mov    eax,DWORD PTR [edi+0x4]
  404b0d:	89 fa                	mov    edx,edi
  404b0f:	83 e0 20             	and    eax,0x20
  404b12:	83 c8 50             	or     eax,0x50
  404b15:	e8 c6 ec ff ff       	call   4037e0 <___pformat_putc>
  404b1a:	8b 45 9c             	mov    eax,DWORD PTR [ebp-0x64]
  404b1d:	89 f9                	mov    ecx,edi
  404b1f:	01 47 08             	add    DWORD PTR [edi+0x8],eax
  404b22:	8b 45 a8             	mov    eax,DWORD PTR [ebp-0x58]
  404b25:	81 4f 04 c0 01 00 00 	or     DWORD PTR [edi+0x4],0x1c0
  404b2c:	99                   	cdq    
  404b2d:	e8 5e ef ff ff       	call   403a90 <___pformat_int>
  404b32:	8d 65 f4             	lea    esp,[ebp-0xc]
  404b35:	5b                   	pop    ebx
  404b36:	5e                   	pop    esi
  404b37:	5f                   	pop    edi
  404b38:	5d                   	pop    ebp
  404b39:	c3                   	ret    
  404b3a:	8d b6 00 00 00 00    	lea    esi,[esi+0x0]
  404b40:	89 fa                	mov    edx,edi
  404b42:	b8 2e 00 00 00       	mov    eax,0x2e
  404b47:	e8 94 ec ff ff       	call   4037e0 <___pformat_putc>
  404b4c:	e9 16 ff ff ff       	jmp    404a67 <___pformat_xldouble+0x3b7>
  404b51:	c7 45 bc 00 00 00 00 	mov    DWORD PTR [ebp-0x44],0x0
  404b58:	8d 75 bc             	lea    esi,[ebp-0x44]
  404b5b:	e8 e0 35 00 00       	call   408140 <_localeconv>
  404b60:	89 74 24 0c          	mov    DWORD PTR [esp+0xc],esi
  404b64:	c7 44 24 08 10 00 00 	mov    DWORD PTR [esp+0x8],0x10
  404b6b:	00 
  404b6c:	8b 00                	mov    eax,DWORD PTR [eax]
  404b6e:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
  404b72:	8d 45 ba             	lea    eax,[ebp-0x46]
  404b75:	89 04 24             	mov    DWORD PTR [esp],eax
  404b78:	e8 f3 22 00 00       	call   406e70 <_mbrtowc>
  404b7d:	85 c0                	test   eax,eax
  404b7f:	0f 8e 85 00 00 00    	jle    404c0a <___pformat_xldouble+0x55a>
  404b85:	0f b7 55 ba          	movzx  edx,WORD PTR [ebp-0x46]
  404b89:	66 89 57 14          	mov    WORD PTR [edi+0x14],dx
  404b8d:	89 47 10             	mov    DWORD PTR [edi+0x10],eax
  404b90:	e9 f4 fe ff ff       	jmp    404a89 <___pformat_xldouble+0x3d9>
  404b95:	0f bf c6             	movsx  eax,si
  404b98:	c7 45 9c 02 00 00 00 	mov    DWORD PTR [ebp-0x64],0x2
  404b9f:	89 45 a8             	mov    DWORD PTR [ebp-0x58],eax
  404ba2:	e9 40 fe ff ff       	jmp    4049e7 <___pformat_xldouble+0x337>
  404ba7:	31 f6                	xor    esi,esi
  404ba9:	31 c0                	xor    eax,eax
  404bab:	31 d2                	xor    edx,edx
  404bad:	e9 62 fb ff ff       	jmp    404714 <___pformat_xldouble+0x64>
  404bb2:	89 47 08             	mov    DWORD PTR [edi+0x8],eax
  404bb5:	e9 2d fe ff ff       	jmp    4049e7 <___pformat_xldouble+0x337>
  404bba:	89 fa                	mov    edx,edi
  404bbc:	b8 2b 00 00 00       	mov    eax,0x2b
  404bc1:	e8 1a ec ff ff       	call   4037e0 <___pformat_putc>
  404bc6:	e9 39 fe ff ff       	jmp    404a04 <___pformat_xldouble+0x354>
  404bcb:	89 fa                	mov    edx,edi
  404bcd:	b8 2e 00 00 00       	mov    eax,0x2e
  404bd2:	e8 09 ec ff ff       	call   4037e0 <___pformat_putc>
  404bd7:	e9 0d ff ff ff       	jmp    404ae9 <___pformat_xldouble+0x439>
  404bdc:	89 fa                	mov    edx,edi
  404bde:	b8 20 00 00 00       	mov    eax,0x20
  404be3:	e8 f8 eb ff ff       	call   4037e0 <___pformat_putc>
  404be8:	e9 17 fe ff ff       	jmp    404a04 <___pformat_xldouble+0x354>
  404bed:	83 c6 01             	add    esi,0x1
  404bf0:	e9 a0 fc ff ff       	jmp    404895 <___pformat_xldouble+0x1e5>
  404bf5:	dd d8                	fstp   st(0)
  404bf7:	89 f9                	mov    ecx,edi
  404bf9:	ba 50 a1 40 00       	mov    edx,0x40a150
  404bfe:	31 c0                	xor    eax,eax
  404c00:	e8 fb ed ff ff       	call   403a00 <___pformat_emit_inf_or_nan>
  404c05:	e9 28 ff ff ff       	jmp    404b32 <___pformat_xldouble+0x482>
  404c0a:	0f b7 57 14          	movzx  edx,WORD PTR [edi+0x14]
  404c0e:	e9 7a ff ff ff       	jmp    404b8d <___pformat_xldouble+0x4dd>
  404c13:	89 f9                	mov    ecx,edi
  404c15:	ba 54 a1 40 00       	mov    edx,0x40a154
  404c1a:	89 d8                	mov    eax,ebx
  404c1c:	e8 df ed ff ff       	call   403a00 <___pformat_emit_inf_or_nan>
  404c21:	e9 0c ff ff ff       	jmp    404b32 <___pformat_xldouble+0x482>
  404c26:	8d 45 d6             	lea    eax,[ebp-0x2a]
  404c29:	89 45 a4             	mov    DWORD PTR [ebp-0x5c],eax
  404c2c:	85 db                	test   ebx,ebx
  404c2e:	8b 47 04             	mov    eax,DWORD PTR [edi+0x4]
  404c31:	7e 33                	jle    404c66 <___pformat_xldouble+0x5b6>
  404c33:	89 45 b0             	mov    DWORD PTR [ebp-0x50],eax
  404c36:	c6 45 d6 2e          	mov    BYTE PTR [ebp-0x2a],0x2e
  404c3a:	8d 45 d7             	lea    eax,[ebp-0x29]
  404c3d:	8d 50 01             	lea    edx,[eax+0x1]
  404c40:	89 55 ac             	mov    DWORD PTR [ebp-0x54],edx
  404c43:	c6 00 30             	mov    BYTE PTR [eax],0x30
  404c46:	e9 c0 fc ff ff       	jmp    40490b <___pformat_xldouble+0x25b>
  404c4b:	c7 45 9c 02 00 00 00 	mov    DWORD PTR [ebp-0x64],0x2
  404c52:	e9 2a fd ff ff       	jmp    404981 <___pformat_xldouble+0x2d1>
  404c57:	8b 5f 0c             	mov    ebx,DWORD PTR [edi+0xc]
  404c5a:	eb d0                	jmp    404c2c <___pformat_xldouble+0x57c>
  404c5c:	be 02 c0 ff ff       	mov    esi,0xffffc002
  404c61:	e9 ae fa ff ff       	jmp    404714 <___pformat_xldouble+0x64>
  404c66:	89 c2                	mov    edx,eax
  404c68:	80 e6 08             	and    dh,0x8
  404c6b:	89 45 b0             	mov    DWORD PTR [ebp-0x50],eax
  404c6e:	8b 45 a4             	mov    eax,DWORD PTR [ebp-0x5c]
  404c71:	74 ca                	je     404c3d <___pformat_xldouble+0x58d>
  404c73:	eb c1                	jmp    404c36 <___pformat_xldouble+0x586>
  404c75:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  404c79:	8d bc 27 00 00 00 00 	lea    edi,[edi+eiz*1+0x0]

00404c80 <___mingw_pformat>:
  404c80:	55                   	push   ebp
  404c81:	57                   	push   edi
  404c82:	56                   	push   esi
  404c83:	53                   	push   ebx
  404c84:	83 ec 5c             	sub    esp,0x5c
  404c87:	8b 44 24 74          	mov    eax,DWORD PTR [esp+0x74]
  404c8b:	81 64 24 70 00 30 00 	and    DWORD PTR [esp+0x70],0x3000
  404c92:	00 
  404c93:	8b 74 24 7c          	mov    esi,DWORD PTR [esp+0x7c]
  404c97:	c7 04 24 6d a1 40 00 	mov    DWORD PTR [esp],0x40a16d
  404c9e:	8b ac 24 80 00 00 00 	mov    ebp,DWORD PTR [esp+0x80]
  404ca5:	89 44 24 2c          	mov    DWORD PTR [esp+0x2c],eax
  404ca9:	8b 44 24 70          	mov    eax,DWORD PTR [esp+0x70]
  404cad:	c7 44 24 34 ff ff ff 	mov    DWORD PTR [esp+0x34],0xffffffff
  404cb4:	ff 
  404cb5:	c7 44 24 38 ff ff ff 	mov    DWORD PTR [esp+0x38],0xffffffff
  404cbc:	ff 
  404cbd:	c7 44 24 3c fd ff ff 	mov    DWORD PTR [esp+0x3c],0xfffffffd
  404cc4:	ff 
  404cc5:	89 44 24 30          	mov    DWORD PTR [esp+0x30],eax
  404cc9:	31 c0                	xor    eax,eax
  404ccb:	66 89 44 24 40       	mov    WORD PTR [esp+0x40],ax
  404cd0:	8b 44 24 78          	mov    eax,DWORD PTR [esp+0x78]
  404cd4:	c7 44 24 44 00 00 00 	mov    DWORD PTR [esp+0x44],0x0
  404cdb:	00 
  404cdc:	89 44 24 48          	mov    DWORD PTR [esp+0x48],eax
  404ce0:	e8 63 34 00 00       	call   408148 <_getenv>
  404ce5:	85 c0                	test   eax,eax
  404ce7:	0f 84 d3 00 00 00    	je     404dc0 <___mingw_pformat+0x140>
  404ced:	0f be 00             	movsx  eax,BYTE PTR [eax]
  404cf0:	83 e8 30             	sub    eax,0x30
  404cf3:	83 f8 02             	cmp    eax,0x2
  404cf6:	0f 87 c4 00 00 00    	ja     404dc0 <___mingw_pformat+0x140>
  404cfc:	b8 02 00 00 00       	mov    eax,0x2
  404d01:	89 44 24 4c          	mov    DWORD PTR [esp+0x4c],eax
  404d05:	8b 44 24 70          	mov    eax,DWORD PTR [esp+0x70]
  404d09:	80 cc 02             	or     ah,0x2
  404d0c:	89 44 24 1c          	mov    DWORD PTR [esp+0x1c],eax
  404d10:	0f be 06             	movsx  eax,BYTE PTR [esi]
  404d13:	8d 5e 01             	lea    ebx,[esi+0x1]
  404d16:	89 d9                	mov    ecx,ebx
  404d18:	85 c0                	test   eax,eax
  404d1a:	0f 84 92 00 00 00    	je     404db2 <___mingw_pformat+0x132>
  404d20:	83 f8 25             	cmp    eax,0x25
  404d23:	0f 85 de 00 00 00    	jne    404e07 <___mingw_pformat+0x187>
  404d29:	8b 44 24 70          	mov    eax,DWORD PTR [esp+0x70]
  404d2d:	c7 44 24 38 ff ff ff 	mov    DWORD PTR [esp+0x38],0xffffffff
  404d34:	ff 
  404d35:	c7 44 24 34 ff ff ff 	mov    DWORD PTR [esp+0x34],0xffffffff
  404d3c:	ff 
  404d3d:	c7 44 24 14 00 00 00 	mov    DWORD PTR [esp+0x14],0x0
  404d44:	00 
  404d45:	89 44 24 30          	mov    DWORD PTR [esp+0x30],eax
  404d49:	0f b6 56 01          	movzx  edx,BYTE PTR [esi+0x1]
  404d4d:	8d 44 24 34          	lea    eax,[esp+0x34]
  404d51:	89 44 24 18          	mov    DWORD PTR [esp+0x18],eax
  404d55:	c7 44 24 10 00 00 00 	mov    DWORD PTR [esp+0x10],0x0
  404d5c:	00 
  404d5d:	84 d2                	test   dl,dl
  404d5f:	74 3f                	je     404da0 <___mingw_pformat+0x120>
  404d61:	8d 42 e0             	lea    eax,[edx-0x20]
  404d64:	0f be fa             	movsx  edi,dl
  404d67:	3c 5a                	cmp    al,0x5a
  404d69:	8d 71 01             	lea    esi,[ecx+0x1]
  404d6c:	0f 87 70 04 00 00    	ja     4051e2 <___mingw_pformat+0x562>
  404d72:	0f b6 c0             	movzx  eax,al
  404d75:	ff 24 85 84 a1 40 00 	jmp    DWORD PTR [eax*4+0x40a184]
  404d7c:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  404d80:	0f b6 51 01          	movzx  edx,BYTE PTR [ecx+0x1]
  404d84:	89 f1                	mov    ecx,esi
  404d86:	c7 44 24 14 02 00 00 	mov    DWORD PTR [esp+0x14],0x2
  404d8d:	00 
  404d8e:	c7 44 24 10 04 00 00 	mov    DWORD PTR [esp+0x10],0x4
  404d95:	00 
  404d96:	84 d2                	test   dl,dl
  404d98:	75 c7                	jne    404d61 <___mingw_pformat+0xe1>
  404d9a:	8d b6 00 00 00 00    	lea    esi,[esi+0x0]
  404da0:	89 ce                	mov    esi,ecx
  404da2:	0f be 06             	movsx  eax,BYTE PTR [esi]
  404da5:	8d 5e 01             	lea    ebx,[esi+0x1]
  404da8:	89 d9                	mov    ecx,ebx
  404daa:	85 c0                	test   eax,eax
  404dac:	0f 85 6e ff ff ff    	jne    404d20 <___mingw_pformat+0xa0>
  404db2:	8b 44 24 44          	mov    eax,DWORD PTR [esp+0x44]
  404db6:	83 c4 5c             	add    esp,0x5c
  404db9:	5b                   	pop    ebx
  404dba:	5e                   	pop    esi
  404dbb:	5f                   	pop    edi
  404dbc:	5d                   	pop    ebp
  404dbd:	c3                   	ret    
  404dbe:	66 90                	xchg   ax,ax
  404dc0:	f6 05 6c d0 40 00 01 	test   BYTE PTR ds:0x40d06c,0x1
  404dc7:	0f 85 2f ff ff ff    	jne    404cfc <___mingw_pformat+0x7c>
  404dcd:	b8 03 00 00 00       	mov    eax,0x3
  404dd2:	e9 2a ff ff ff       	jmp    404d01 <___mingw_pformat+0x81>
  404dd7:	80 79 01 6c          	cmp    BYTE PTR [ecx+0x1],0x6c
  404ddb:	c7 44 24 14 02 00 00 	mov    DWORD PTR [esp+0x14],0x2
  404de2:	00 
  404de3:	75 0b                	jne    404df0 <___mingw_pformat+0x170>
  404de5:	8d 71 02             	lea    esi,[ecx+0x2]
  404de8:	c7 44 24 14 03 00 00 	mov    DWORD PTR [esp+0x14],0x3
  404def:	00 
  404df0:	83 4c 24 30 04       	or     DWORD PTR [esp+0x30],0x4
  404df5:	89 f1                	mov    ecx,esi
  404df7:	0f b6 16             	movzx  edx,BYTE PTR [esi]
  404dfa:	c7 44 24 10 04 00 00 	mov    DWORD PTR [esp+0x10],0x4
  404e01:	00 
  404e02:	e9 56 ff ff ff       	jmp    404d5d <___mingw_pformat+0xdd>
  404e07:	8d 54 24 2c          	lea    edx,[esp+0x2c]
  404e0b:	89 de                	mov    esi,ebx
  404e0d:	e8 ce e9 ff ff       	call   4037e0 <___pformat_putc>
  404e12:	e9 f9 fe ff ff       	jmp    404d10 <___mingw_pformat+0x90>
  404e17:	8b 54 24 14          	mov    edx,DWORD PTR [esp+0x14]
  404e1b:	89 e8                	mov    eax,ebp
  404e1d:	83 ea 02             	sub    edx,0x2
  404e20:	83 fa 01             	cmp    edx,0x1
  404e23:	0f 86 07 05 00 00    	jbe    405330 <___mingw_pformat+0x6b0>
  404e29:	8b 18                	mov    ebx,DWORD PTR [eax]
  404e2b:	83 c5 04             	add    ebp,0x4
  404e2e:	85 db                	test   ebx,ebx
  404e30:	0f 84 89 06 00 00    	je     4054bf <___mingw_pformat+0x83f>
  404e36:	89 1c 24             	mov    DWORD PTR [esp],ebx
  404e39:	e8 72 32 00 00       	call   4080b0 <_strlen>
  404e3e:	89 c2                	mov    edx,eax
  404e40:	8d 4c 24 2c          	lea    ecx,[esp+0x2c]
  404e44:	89 d8                	mov    eax,ebx
  404e46:	e8 05 eb ff ff       	call   403950 <___pformat_putchars>
  404e4b:	e9 c0 fe ff ff       	jmp    404d10 <___mingw_pformat+0x90>
  404e50:	8b 54 24 14          	mov    edx,DWORD PTR [esp+0x14]
  404e54:	89 e8                	mov    eax,ebp
  404e56:	c7 44 24 38 ff ff ff 	mov    DWORD PTR [esp+0x38],0xffffffff
  404e5d:	ff 
  404e5e:	83 ea 02             	sub    edx,0x2
  404e61:	83 fa 01             	cmp    edx,0x1
  404e64:	0f 86 23 03 00 00    	jbe    40518d <___mingw_pformat+0x50d>
  404e6a:	8b 00                	mov    eax,DWORD PTR [eax]
  404e6c:	8d 4c 24 2c          	lea    ecx,[esp+0x2c]
  404e70:	ba 01 00 00 00       	mov    edx,0x1
  404e75:	83 c5 04             	add    ebp,0x4
  404e78:	88 44 24 20          	mov    BYTE PTR [esp+0x20],al
  404e7c:	8d 44 24 20          	lea    eax,[esp+0x20]
  404e80:	e8 cb ea ff ff       	call   403950 <___pformat_putchars>
  404e85:	e9 86 fe ff ff       	jmp    404d10 <___mingw_pformat+0x90>
  404e8a:	8d b6 00 00 00 00    	lea    esi,[esi+0x0]
  404e90:	83 7c 24 14 04       	cmp    DWORD PTR [esp+0x14],0x4
  404e95:	0f 84 f0 05 00 00    	je     40548b <___mingw_pformat+0x80b>
  404e9b:	83 7c 24 14 01       	cmp    DWORD PTR [esp+0x14],0x1
  404ea0:	8b 45 00             	mov    eax,DWORD PTR [ebp+0x0]
  404ea3:	8b 54 24 44          	mov    edx,DWORD PTR [esp+0x44]
  404ea7:	0f 84 17 05 00 00    	je     4053c4 <___mingw_pformat+0x744>
  404ead:	83 7c 24 14 02       	cmp    DWORD PTR [esp+0x14],0x2
  404eb2:	0f 84 43 06 00 00    	je     4054fb <___mingw_pformat+0x87b>
  404eb8:	83 7c 24 14 03       	cmp    DWORD PTR [esp+0x14],0x3
  404ebd:	89 10                	mov    DWORD PTR [eax],edx
  404ebf:	0f 84 a9 06 00 00    	je     40556e <___mingw_pformat+0x8ee>
  404ec5:	83 c5 04             	add    ebp,0x4
  404ec8:	e9 43 fe ff ff       	jmp    404d10 <___mingw_pformat+0x90>
  404ecd:	8d 76 00             	lea    esi,[esi+0x0]
  404ed0:	0f b6 51 01          	movzx  edx,BYTE PTR [ecx+0x1]
  404ed4:	89 f1                	mov    ecx,esi
  404ed6:	c7 44 24 14 03 00 00 	mov    DWORD PTR [esp+0x14],0x3
  404edd:	00 
  404ede:	c7 44 24 10 04 00 00 	mov    DWORD PTR [esp+0x10],0x4
  404ee5:	00 
  404ee6:	e9 72 fe ff ff       	jmp    404d5d <___mingw_pformat+0xdd>
  404eeb:	90                   	nop
  404eec:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  404ef0:	0f b6 51 01          	movzx  edx,BYTE PTR [ecx+0x1]
  404ef4:	80 fa 68             	cmp    dl,0x68
  404ef7:	0f 84 4c 05 00 00    	je     405449 <___mingw_pformat+0x7c9>
  404efd:	89 f1                	mov    ecx,esi
  404eff:	c7 44 24 14 01 00 00 	mov    DWORD PTR [esp+0x14],0x1
  404f06:	00 
  404f07:	c7 44 24 10 04 00 00 	mov    DWORD PTR [esp+0x10],0x4
  404f0e:	00 
  404f0f:	e9 49 fe ff ff       	jmp    404d5d <___mingw_pformat+0xdd>
  404f14:	8b 44 24 10          	mov    eax,DWORD PTR [esp+0x10]
  404f18:	85 c0                	test   eax,eax
  404f1a:	75 0e                	jne    404f2a <___mingw_pformat+0x2aa>
  404f1c:	8b 44 24 70          	mov    eax,DWORD PTR [esp+0x70]
  404f20:	39 44 24 30          	cmp    DWORD PTR [esp+0x30],eax
  404f24:	0f 84 a4 05 00 00    	je     4054ce <___mingw_pformat+0x84e>
  404f2a:	8b 45 00             	mov    eax,DWORD PTR [ebp+0x0]
  404f2d:	8d 5d 04             	lea    ebx,[ebp+0x4]
  404f30:	c7 44 24 24 00 00 00 	mov    DWORD PTR [esp+0x24],0x0
  404f37:	00 
  404f38:	8b 4c 24 24          	mov    ecx,DWORD PTR [esp+0x24]
  404f3c:	89 dd                	mov    ebp,ebx
  404f3e:	89 44 24 20          	mov    DWORD PTR [esp+0x20],eax
  404f42:	8b 54 24 20          	mov    edx,DWORD PTR [esp+0x20]
  404f46:	8d 44 24 2c          	lea    eax,[esp+0x2c]
  404f4a:	89 04 24             	mov    DWORD PTR [esp],eax
  404f4d:	b8 78 00 00 00       	mov    eax,0x78
  404f52:	e8 69 ed ff ff       	call   403cc0 <___pformat_xint>
  404f57:	e9 b4 fd ff ff       	jmp    404d10 <___mingw_pformat+0x90>
  404f5c:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  404f60:	8b 44 24 30          	mov    eax,DWORD PTR [esp+0x30]
  404f64:	83 c8 20             	or     eax,0x20
  404f67:	a8 04                	test   al,0x4
  404f69:	89 44 24 30          	mov    DWORD PTR [esp+0x30],eax
  404f6d:	0f 84 4a 02 00 00    	je     4051bd <___mingw_pformat+0x53d>
  404f73:	db 6d 00             	fld    TBYTE PTR [ebp+0x0]
  404f76:	8d 5d 0c             	lea    ebx,[ebp+0xc]
  404f79:	db 3c 24             	fstp   TBYTE PTR [esp]
  404f7c:	89 dd                	mov    ebp,ebx
  404f7e:	8d 44 24 2c          	lea    eax,[esp+0x2c]
  404f82:	e8 29 f7 ff ff       	call   4046b0 <___pformat_xldouble>
  404f87:	e9 84 fd ff ff       	jmp    404d10 <___mingw_pformat+0x90>
  404f8c:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  404f90:	83 7c 24 14 03       	cmp    DWORD PTR [esp+0x14],0x3
  404f95:	89 f8                	mov    eax,edi
  404f97:	0f 84 80 04 00 00    	je     40541d <___mingw_pformat+0x79d>
  404f9d:	83 7c 24 14 02       	cmp    DWORD PTR [esp+0x14],0x2
  404fa2:	0f 84 27 04 00 00    	je     4053cf <___mingw_pformat+0x74f>
  404fa8:	8b 7d 00             	mov    edi,DWORD PTR [ebp+0x0]
  404fab:	8d 55 04             	lea    edx,[ebp+0x4]
  404fae:	83 7c 24 14 01       	cmp    DWORD PTR [esp+0x14],0x1
  404fb3:	c7 44 24 24 00 00 00 	mov    DWORD PTR [esp+0x24],0x0
  404fba:	00 
  404fbb:	89 7c 24 20          	mov    DWORD PTR [esp+0x20],edi
  404fbf:	0f 84 1e 05 00 00    	je     4054e3 <___mingw_pformat+0x863>
  404fc5:	83 7c 24 14 04       	cmp    DWORD PTR [esp+0x14],0x4
  404fca:	89 d5                	mov    ebp,edx
  404fcc:	0f 84 86 05 00 00    	je     405558 <___mingw_pformat+0x8d8>
  404fd2:	83 f8 75             	cmp    eax,0x75
  404fd5:	0f 84 ec 00 00 00    	je     4050c7 <___mingw_pformat+0x447>
  404fdb:	8b 54 24 20          	mov    edx,DWORD PTR [esp+0x20]
  404fdf:	8d 7c 24 2c          	lea    edi,[esp+0x2c]
  404fe3:	8b 4c 24 24          	mov    ecx,DWORD PTR [esp+0x24]
  404fe7:	89 3c 24             	mov    DWORD PTR [esp],edi
  404fea:	e8 d1 ec ff ff       	call   403cc0 <___pformat_xint>
  404fef:	e9 1c fd ff ff       	jmp    404d10 <___mingw_pformat+0x90>
  404ff4:	8b 44 24 30          	mov    eax,DWORD PTR [esp+0x30]
  404ff8:	83 c8 20             	or     eax,0x20
  404ffb:	a8 04                	test   al,0x4
  404ffd:	89 44 24 30          	mov    DWORD PTR [esp+0x30],eax
  405001:	0f 84 15 01 00 00    	je     40511c <___mingw_pformat+0x49c>
  405007:	db 6d 00             	fld    TBYTE PTR [ebp+0x0]
  40500a:	8d 5d 0c             	lea    ebx,[ebp+0xc]
  40500d:	db 3c 24             	fstp   TBYTE PTR [esp]
  405010:	89 dd                	mov    ebp,ebx
  405012:	8d 44 24 2c          	lea    eax,[esp+0x2c]
  405016:	e8 15 f5 ff ff       	call   404530 <___pformat_gfloat>
  40501b:	e9 f0 fc ff ff       	jmp    404d10 <___mingw_pformat+0x90>
  405020:	8b 44 24 30          	mov    eax,DWORD PTR [esp+0x30]
  405024:	83 c8 20             	or     eax,0x20
  405027:	a8 04                	test   al,0x4
  405029:	89 44 24 30          	mov    DWORD PTR [esp+0x30],eax
  40502d:	0f 84 0e 01 00 00    	je     405141 <___mingw_pformat+0x4c1>
  405033:	db 6d 00             	fld    TBYTE PTR [ebp+0x0]
  405036:	8d 5d 0c             	lea    ebx,[ebp+0xc]
  405039:	db 3c 24             	fstp   TBYTE PTR [esp]
  40503c:	89 dd                	mov    ebp,ebx
  40503e:	8d 44 24 2c          	lea    eax,[esp+0x2c]
  405042:	e8 09 f4 ff ff       	call   404450 <___pformat_float>
  405047:	e9 c4 fc ff ff       	jmp    404d10 <___mingw_pformat+0x90>
  40504c:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  405050:	8b 44 24 30          	mov    eax,DWORD PTR [esp+0x30]
  405054:	83 c8 20             	or     eax,0x20
  405057:	a8 04                	test   al,0x4
  405059:	89 44 24 30          	mov    DWORD PTR [esp+0x30],eax
  40505d:	0f 84 09 01 00 00    	je     40516c <___mingw_pformat+0x4ec>
  405063:	db 6d 00             	fld    TBYTE PTR [ebp+0x0]
  405066:	8d 5d 0c             	lea    ebx,[ebp+0xc]
  405069:	db 3c 24             	fstp   TBYTE PTR [esp]
  40506c:	89 dd                	mov    ebp,ebx
  40506e:	8d 44 24 2c          	lea    eax,[esp+0x2c]
  405072:	e8 29 f3 ff ff       	call   4043a0 <___pformat_efloat>
  405077:	e9 94 fc ff ff       	jmp    404d10 <___mingw_pformat+0x90>
  40507c:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  405080:	81 4c 24 30 80 00 00 	or     DWORD PTR [esp+0x30],0x80
  405087:	00 
  405088:	83 7c 24 14 03       	cmp    DWORD PTR [esp+0x14],0x3
  40508d:	0f 84 a0 03 00 00    	je     405433 <___mingw_pformat+0x7b3>
  405093:	83 7c 24 14 02       	cmp    DWORD PTR [esp+0x14],0x2
  405098:	0f 84 48 03 00 00    	je     4053e6 <___mingw_pformat+0x766>
  40509e:	8b 45 00             	mov    eax,DWORD PTR [ebp+0x0]
  4050a1:	8d 55 04             	lea    edx,[ebp+0x4]
  4050a4:	89 44 24 20          	mov    DWORD PTR [esp+0x20],eax
  4050a8:	c1 f8 1f             	sar    eax,0x1f
  4050ab:	83 7c 24 14 01       	cmp    DWORD PTR [esp+0x14],0x1
  4050b0:	89 44 24 24          	mov    DWORD PTR [esp+0x24],eax
  4050b4:	0f 84 4b 04 00 00    	je     405505 <___mingw_pformat+0x885>
  4050ba:	83 7c 24 14 04       	cmp    DWORD PTR [esp+0x14],0x4
  4050bf:	89 d5                	mov    ebp,edx
  4050c1:	0f 84 7c 04 00 00    	je     405543 <___mingw_pformat+0x8c3>
  4050c7:	8b 44 24 20          	mov    eax,DWORD PTR [esp+0x20]
  4050cb:	8d 4c 24 2c          	lea    ecx,[esp+0x2c]
  4050cf:	8b 54 24 24          	mov    edx,DWORD PTR [esp+0x24]
  4050d3:	e8 b8 e9 ff ff       	call   403a90 <___pformat_int>
  4050d8:	e9 33 fc ff ff       	jmp    404d10 <___mingw_pformat+0x90>
  4050dd:	8d 76 00             	lea    esi,[esi+0x0]
  4050e0:	0f b6 51 01          	movzx  edx,BYTE PTR [ecx+0x1]
  4050e4:	80 fa 36             	cmp    dl,0x36
  4050e7:	0f 84 78 03 00 00    	je     405465 <___mingw_pformat+0x7e5>
  4050ed:	80 fa 33             	cmp    dl,0x33
  4050f0:	0f 84 a8 02 00 00    	je     40539e <___mingw_pformat+0x71e>
  4050f6:	89 f1                	mov    ecx,esi
  4050f8:	c7 44 24 14 02 00 00 	mov    DWORD PTR [esp+0x14],0x2
  4050ff:	00 
  405100:	c7 44 24 10 04 00 00 	mov    DWORD PTR [esp+0x10],0x4
  405107:	00 
  405108:	e9 50 fc ff ff       	jmp    404d5d <___mingw_pformat+0xdd>
  40510d:	8d 76 00             	lea    esi,[esi+0x0]
  405110:	8b 44 24 30          	mov    eax,DWORD PTR [esp+0x30]
  405114:	a8 04                	test   al,0x4
  405116:	0f 85 eb fe ff ff    	jne    405007 <___mingw_pformat+0x387>
  40511c:	dd 45 00             	fld    QWORD PTR [ebp+0x0]
  40511f:	8d 5d 08             	lea    ebx,[ebp+0x8]
  405122:	db 3c 24             	fstp   TBYTE PTR [esp]
  405125:	89 dd                	mov    ebp,ebx
  405127:	8d 44 24 2c          	lea    eax,[esp+0x2c]
  40512b:	e8 00 f4 ff ff       	call   404530 <___pformat_gfloat>
  405130:	e9 db fb ff ff       	jmp    404d10 <___mingw_pformat+0x90>
  405135:	8b 44 24 30          	mov    eax,DWORD PTR [esp+0x30]
  405139:	a8 04                	test   al,0x4
  40513b:	0f 85 f2 fe ff ff    	jne    405033 <___mingw_pformat+0x3b3>
  405141:	dd 45 00             	fld    QWORD PTR [ebp+0x0]
  405144:	8d 5d 08             	lea    ebx,[ebp+0x8]
  405147:	db 3c 24             	fstp   TBYTE PTR [esp]
  40514a:	89 dd                	mov    ebp,ebx
  40514c:	8d 44 24 2c          	lea    eax,[esp+0x2c]
  405150:	e8 fb f2 ff ff       	call   404450 <___pformat_float>
  405155:	e9 b6 fb ff ff       	jmp    404d10 <___mingw_pformat+0x90>
  40515a:	8d b6 00 00 00 00    	lea    esi,[esi+0x0]
  405160:	8b 44 24 30          	mov    eax,DWORD PTR [esp+0x30]
  405164:	a8 04                	test   al,0x4
  405166:	0f 85 f7 fe ff ff    	jne    405063 <___mingw_pformat+0x3e3>
  40516c:	dd 45 00             	fld    QWORD PTR [ebp+0x0]
  40516f:	8d 5d 08             	lea    ebx,[ebp+0x8]
  405172:	db 3c 24             	fstp   TBYTE PTR [esp]
  405175:	89 dd                	mov    ebp,ebx
  405177:	8d 44 24 2c          	lea    eax,[esp+0x2c]
  40517b:	e8 20 f2 ff ff       	call   4043a0 <___pformat_efloat>
  405180:	e9 8b fb ff ff       	jmp    404d10 <___mingw_pformat+0x90>
  405185:	c7 44 24 38 ff ff ff 	mov    DWORD PTR [esp+0x38],0xffffffff
  40518c:	ff 
  40518d:	8b 45 00             	mov    eax,DWORD PTR [ebp+0x0]
  405190:	8d 5d 04             	lea    ebx,[ebp+0x4]
  405193:	ba 01 00 00 00       	mov    edx,0x1
  405198:	8d 4c 24 2c          	lea    ecx,[esp+0x2c]
  40519c:	89 dd                	mov    ebp,ebx
  40519e:	66 89 44 24 20       	mov    WORD PTR [esp+0x20],ax
  4051a3:	8d 44 24 20          	lea    eax,[esp+0x20]
  4051a7:	e8 94 e6 ff ff       	call   403840 <___pformat_wputchars>
  4051ac:	e9 5f fb ff ff       	jmp    404d10 <___mingw_pformat+0x90>
  4051b1:	8b 44 24 30          	mov    eax,DWORD PTR [esp+0x30]
  4051b5:	a8 04                	test   al,0x4
  4051b7:	0f 85 b6 fd ff ff    	jne    404f73 <___mingw_pformat+0x2f3>
  4051bd:	dd 45 00             	fld    QWORD PTR [ebp+0x0]
  4051c0:	8d 5d 08             	lea    ebx,[ebp+0x8]
  4051c3:	db 3c 24             	fstp   TBYTE PTR [esp]
  4051c6:	89 dd                	mov    ebp,ebx
  4051c8:	8d 44 24 2c          	lea    eax,[esp+0x2c]
  4051cc:	e8 df f4 ff ff       	call   4046b0 <___pformat_xldouble>
  4051d1:	e9 3a fb ff ff       	jmp    404d10 <___mingw_pformat+0x90>
  4051d6:	8b 44 24 10          	mov    eax,DWORD PTR [esp+0x10]
  4051da:	85 c0                	test   eax,eax
  4051dc:	0f 84 8e 01 00 00    	je     405370 <___mingw_pformat+0x6f0>
  4051e2:	8b 44 24 10          	mov    eax,DWORD PTR [esp+0x10]
  4051e6:	83 f8 04             	cmp    eax,0x4
  4051e9:	0f 84 c7 03 00 00    	je     4055b6 <___mingw_pformat+0x936>
  4051ef:	83 ea 30             	sub    edx,0x30
  4051f2:	80 fa 09             	cmp    dl,0x9
  4051f5:	0f 87 bb 03 00 00    	ja     4055b6 <___mingw_pformat+0x936>
  4051fb:	85 c0                	test   eax,eax
  4051fd:	0f 84 5d 01 00 00    	je     405360 <___mingw_pformat+0x6e0>
  405203:	83 f8 02             	cmp    eax,0x2
  405206:	0f 84 f0 01 00 00    	je     4053fc <___mingw_pformat+0x77c>
  40520c:	8b 44 24 18          	mov    eax,DWORD PTR [esp+0x18]
  405210:	85 c0                	test   eax,eax
  405212:	74 1b                	je     40522f <___mingw_pformat+0x5af>
  405214:	8b 44 24 18          	mov    eax,DWORD PTR [esp+0x18]
  405218:	8b 00                	mov    eax,DWORD PTR [eax]
  40521a:	85 c0                	test   eax,eax
  40521c:	0f 88 e7 01 00 00    	js     405409 <___mingw_pformat+0x789>
  405222:	8d 04 80             	lea    eax,[eax+eax*4]
  405225:	8d 44 47 d0          	lea    eax,[edi+eax*2-0x30]
  405229:	8b 7c 24 18          	mov    edi,DWORD PTR [esp+0x18]
  40522d:	89 07                	mov    DWORD PTR [edi],eax
  40522f:	0f b6 51 01          	movzx  edx,BYTE PTR [ecx+0x1]
  405233:	89 f1                	mov    ecx,esi
  405235:	e9 23 fb ff ff       	jmp    404d5d <___mingw_pformat+0xdd>
  40523a:	8d b6 00 00 00 00    	lea    esi,[esi+0x0]
  405240:	83 7c 24 10 01       	cmp    DWORD PTR [esp+0x10],0x1
  405245:	0f 86 51 02 00 00    	jbe    40549c <___mingw_pformat+0x81c>
  40524b:	0f b6 51 01          	movzx  edx,BYTE PTR [ecx+0x1]
  40524f:	89 f1                	mov    ecx,esi
  405251:	c7 44 24 10 04 00 00 	mov    DWORD PTR [esp+0x10],0x4
  405258:	00 
  405259:	e9 ff fa ff ff       	jmp    404d5d <___mingw_pformat+0xdd>
  40525e:	66 90                	xchg   ax,ax
  405260:	8b 44 24 10          	mov    eax,DWORD PTR [esp+0x10]
  405264:	85 c0                	test   eax,eax
  405266:	75 c7                	jne    40522f <___mingw_pformat+0x5af>
  405268:	81 4c 24 30 00 04 00 	or     DWORD PTR [esp+0x30],0x400
  40526f:	00 
  405270:	0f b6 51 01          	movzx  edx,BYTE PTR [ecx+0x1]
  405274:	89 f1                	mov    ecx,esi
  405276:	e9 e2 fa ff ff       	jmp    404d5d <___mingw_pformat+0xdd>
  40527b:	90                   	nop
  40527c:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  405280:	8b 44 24 10          	mov    eax,DWORD PTR [esp+0x10]
  405284:	85 c0                	test   eax,eax
  405286:	75 a7                	jne    40522f <___mingw_pformat+0x5af>
  405288:	81 4c 24 30 00 01 00 	or     DWORD PTR [esp+0x30],0x100
  40528f:	00 
  405290:	0f b6 51 01          	movzx  edx,BYTE PTR [ecx+0x1]
  405294:	89 f1                	mov    ecx,esi
  405296:	e9 c2 fa ff ff       	jmp    404d5d <___mingw_pformat+0xdd>
  40529b:	90                   	nop
  40529c:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  4052a0:	8b 7c 24 18          	mov    edi,DWORD PTR [esp+0x18]
  4052a4:	85 ff                	test   edi,edi
  4052a6:	74 a3                	je     40524b <___mingw_pformat+0x5cb>
  4052a8:	f6 44 24 10 05       	test   BYTE PTR [esp+0x10],0x5
  4052ad:	0f 85 d0 00 00 00    	jne    405383 <___mingw_pformat+0x703>
  4052b3:	8b 45 00             	mov    eax,DWORD PTR [ebp+0x0]
  4052b6:	8d 7d 04             	lea    edi,[ebp+0x4]
  4052b9:	8b 54 24 18          	mov    edx,DWORD PTR [esp+0x18]
  4052bd:	85 c0                	test   eax,eax
  4052bf:	89 02                	mov    DWORD PTR [edx],eax
  4052c1:	0f 88 5f 02 00 00    	js     405526 <___mingw_pformat+0x8a6>
  4052c7:	0f b6 51 01          	movzx  edx,BYTE PTR [ecx+0x1]
  4052cb:	89 fd                	mov    ebp,edi
  4052cd:	89 f1                	mov    ecx,esi
  4052cf:	c7 44 24 18 00 00 00 	mov    DWORD PTR [esp+0x18],0x0
  4052d6:	00 
  4052d7:	e9 81 fa ff ff       	jmp    404d5d <___mingw_pformat+0xdd>
  4052dc:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  4052e0:	89 f8                	mov    eax,edi
  4052e2:	8d 54 24 2c          	lea    edx,[esp+0x2c]
  4052e6:	e8 f5 e4 ff ff       	call   4037e0 <___pformat_putc>
  4052eb:	e9 20 fa ff ff       	jmp    404d10 <___mingw_pformat+0x90>
  4052f0:	8b 44 24 10          	mov    eax,DWORD PTR [esp+0x10]
  4052f4:	85 c0                	test   eax,eax
  4052f6:	0f 85 33 ff ff ff    	jne    40522f <___mingw_pformat+0x5af>
  4052fc:	81 4c 24 30 00 08 00 	or     DWORD PTR [esp+0x30],0x800
  405303:	00 
  405304:	0f b6 51 01          	movzx  edx,BYTE PTR [ecx+0x1]
  405308:	89 f1                	mov    ecx,esi
  40530a:	e9 4e fa ff ff       	jmp    404d5d <___mingw_pformat+0xdd>
  40530f:	90                   	nop
  405310:	8b 44 24 10          	mov    eax,DWORD PTR [esp+0x10]
  405314:	85 c0                	test   eax,eax
  405316:	0f 85 13 ff ff ff    	jne    40522f <___mingw_pformat+0x5af>
  40531c:	83 4c 24 30 40       	or     DWORD PTR [esp+0x30],0x40
  405321:	0f b6 51 01          	movzx  edx,BYTE PTR [ecx+0x1]
  405325:	89 f1                	mov    ecx,esi
  405327:	e9 31 fa ff ff       	jmp    404d5d <___mingw_pformat+0xdd>
  40532c:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  405330:	8b 5d 00             	mov    ebx,DWORD PTR [ebp+0x0]
  405333:	8d 7d 04             	lea    edi,[ebp+0x4]
  405336:	85 db                	test   ebx,ebx
  405338:	0f 84 de 01 00 00    	je     40551c <___mingw_pformat+0x89c>
  40533e:	89 1c 24             	mov    DWORD PTR [esp],ebx
  405341:	89 fd                	mov    ebp,edi
  405343:	e8 08 2e 00 00       	call   408150 <_wcslen>
  405348:	8d 4c 24 2c          	lea    ecx,[esp+0x2c]
  40534c:	89 c2                	mov    edx,eax
  40534e:	89 d8                	mov    eax,ebx
  405350:	e8 eb e4 ff ff       	call   403840 <___pformat_wputchars>
  405355:	e9 b6 f9 ff ff       	jmp    404d10 <___mingw_pformat+0x90>
  40535a:	8d b6 00 00 00 00    	lea    esi,[esi+0x0]
  405360:	c7 44 24 10 01 00 00 	mov    DWORD PTR [esp+0x10],0x1
  405367:	00 
  405368:	e9 9f fe ff ff       	jmp    40520c <___mingw_pformat+0x58c>
  40536d:	8d 76 00             	lea    esi,[esi+0x0]
  405370:	81 4c 24 30 00 02 00 	or     DWORD PTR [esp+0x30],0x200
  405377:	00 
  405378:	0f b6 51 01          	movzx  edx,BYTE PTR [ecx+0x1]
  40537c:	89 f1                	mov    ecx,esi
  40537e:	e9 da f9 ff ff       	jmp    404d5d <___mingw_pformat+0xdd>
  405383:	0f b6 51 01          	movzx  edx,BYTE PTR [ecx+0x1]
  405387:	89 f1                	mov    ecx,esi
  405389:	c7 44 24 18 00 00 00 	mov    DWORD PTR [esp+0x18],0x0
  405390:	00 
  405391:	c7 44 24 10 04 00 00 	mov    DWORD PTR [esp+0x10],0x4
  405398:	00 
  405399:	e9 bf f9 ff ff       	jmp    404d5d <___mingw_pformat+0xdd>
  40539e:	80 79 02 32          	cmp    BYTE PTR [ecx+0x2],0x32
  4053a2:	0f 84 f2 01 00 00    	je     40559a <___mingw_pformat+0x91a>
  4053a8:	89 f1                	mov    ecx,esi
  4053aa:	ba 33 00 00 00       	mov    edx,0x33
  4053af:	c7 44 24 14 02 00 00 	mov    DWORD PTR [esp+0x14],0x2
  4053b6:	00 
  4053b7:	c7 44 24 10 04 00 00 	mov    DWORD PTR [esp+0x10],0x4
  4053be:	00 
  4053bf:	e9 9d f9 ff ff       	jmp    404d61 <___mingw_pformat+0xe1>
  4053c4:	66 89 10             	mov    WORD PTR [eax],dx
  4053c7:	83 c5 04             	add    ebp,0x4
  4053ca:	e9 41 f9 ff ff       	jmp    404d10 <___mingw_pformat+0x90>
  4053cf:	8b 7d 00             	mov    edi,DWORD PTR [ebp+0x0]
  4053d2:	83 c5 04             	add    ebp,0x4
  4053d5:	c7 44 24 24 00 00 00 	mov    DWORD PTR [esp+0x24],0x0
  4053dc:	00 
  4053dd:	89 7c 24 20          	mov    DWORD PTR [esp+0x20],edi
  4053e1:	e9 ec fb ff ff       	jmp    404fd2 <___mingw_pformat+0x352>
  4053e6:	8b 45 00             	mov    eax,DWORD PTR [ebp+0x0]
  4053e9:	83 c5 04             	add    ebp,0x4
  4053ec:	89 44 24 20          	mov    DWORD PTR [esp+0x20],eax
  4053f0:	c1 f8 1f             	sar    eax,0x1f
  4053f3:	89 44 24 24          	mov    DWORD PTR [esp+0x24],eax
  4053f7:	e9 cb fc ff ff       	jmp    4050c7 <___mingw_pformat+0x447>
  4053fc:	c7 44 24 10 03 00 00 	mov    DWORD PTR [esp+0x10],0x3
  405403:	00 
  405404:	e9 03 fe ff ff       	jmp    40520c <___mingw_pformat+0x58c>
  405409:	8b 44 24 18          	mov    eax,DWORD PTR [esp+0x18]
  40540d:	83 ef 30             	sub    edi,0x30
  405410:	89 38                	mov    DWORD PTR [eax],edi
  405412:	0f b6 51 01          	movzx  edx,BYTE PTR [ecx+0x1]
  405416:	89 f1                	mov    ecx,esi
  405418:	e9 40 f9 ff ff       	jmp    404d5d <___mingw_pformat+0xdd>
  40541d:	8b 4d 00             	mov    ecx,DWORD PTR [ebp+0x0]
  405420:	83 c5 08             	add    ebp,0x8
  405423:	8b 5d fc             	mov    ebx,DWORD PTR [ebp-0x4]
  405426:	89 4c 24 20          	mov    DWORD PTR [esp+0x20],ecx
  40542a:	89 5c 24 24          	mov    DWORD PTR [esp+0x24],ebx
  40542e:	e9 9f fb ff ff       	jmp    404fd2 <___mingw_pformat+0x352>
  405433:	8b 45 00             	mov    eax,DWORD PTR [ebp+0x0]
  405436:	83 c5 08             	add    ebp,0x8
  405439:	8b 55 fc             	mov    edx,DWORD PTR [ebp-0x4]
  40543c:	89 44 24 20          	mov    DWORD PTR [esp+0x20],eax
  405440:	89 54 24 24          	mov    DWORD PTR [esp+0x24],edx
  405444:	e9 7e fc ff ff       	jmp    4050c7 <___mingw_pformat+0x447>
  405449:	0f b6 51 02          	movzx  edx,BYTE PTR [ecx+0x2]
  40544d:	83 c1 02             	add    ecx,0x2
  405450:	c7 44 24 14 04 00 00 	mov    DWORD PTR [esp+0x14],0x4
  405457:	00 
  405458:	c7 44 24 10 04 00 00 	mov    DWORD PTR [esp+0x10],0x4
  40545f:	00 
  405460:	e9 f8 f8 ff ff       	jmp    404d5d <___mingw_pformat+0xdd>
  405465:	80 79 02 34          	cmp    BYTE PTR [ecx+0x2],0x34
  405469:	0f 84 0f 01 00 00    	je     40557e <___mingw_pformat+0x8fe>
  40546f:	89 f1                	mov    ecx,esi
  405471:	ba 36 00 00 00       	mov    edx,0x36
  405476:	c7 44 24 14 02 00 00 	mov    DWORD PTR [esp+0x14],0x2
  40547d:	00 
  40547e:	c7 44 24 10 04 00 00 	mov    DWORD PTR [esp+0x10],0x4
  405485:	00 
  405486:	e9 d6 f8 ff ff       	jmp    404d61 <___mingw_pformat+0xe1>
  40548b:	8b 55 00             	mov    edx,DWORD PTR [ebp+0x0]
  40548e:	83 c5 04             	add    ebp,0x4
  405491:	8b 44 24 44          	mov    eax,DWORD PTR [esp+0x44]
  405495:	88 02                	mov    BYTE PTR [edx],al
  405497:	e9 74 f8 ff ff       	jmp    404d10 <___mingw_pformat+0x90>
  40549c:	8d 44 24 38          	lea    eax,[esp+0x38]
  4054a0:	c7 44 24 38 00 00 00 	mov    DWORD PTR [esp+0x38],0x0
  4054a7:	00 
  4054a8:	0f b6 51 01          	movzx  edx,BYTE PTR [ecx+0x1]
  4054ac:	89 f1                	mov    ecx,esi
  4054ae:	89 44 24 18          	mov    DWORD PTR [esp+0x18],eax
  4054b2:	c7 44 24 10 02 00 00 	mov    DWORD PTR [esp+0x10],0x2
  4054b9:	00 
  4054ba:	e9 9e f8 ff ff       	jmp    404d5d <___mingw_pformat+0xdd>
  4054bf:	ba 06 00 00 00       	mov    edx,0x6
  4054c4:	bb 66 a1 40 00       	mov    ebx,0x40a166
  4054c9:	e9 72 f9 ff ff       	jmp    404e40 <___mingw_pformat+0x1c0>
  4054ce:	8b 44 24 1c          	mov    eax,DWORD PTR [esp+0x1c]
  4054d2:	c7 44 24 38 08 00 00 	mov    DWORD PTR [esp+0x38],0x8
  4054d9:	00 
  4054da:	89 44 24 30          	mov    DWORD PTR [esp+0x30],eax
  4054de:	e9 47 fa ff ff       	jmp    404f2a <___mingw_pformat+0x2aa>
  4054e3:	0f b7 4c 24 20       	movzx  ecx,WORD PTR [esp+0x20]
  4054e8:	89 d5                	mov    ebp,edx
  4054ea:	c7 44 24 24 00 00 00 	mov    DWORD PTR [esp+0x24],0x0
  4054f1:	00 
  4054f2:	89 4c 24 20          	mov    DWORD PTR [esp+0x20],ecx
  4054f6:	e9 d7 fa ff ff       	jmp    404fd2 <___mingw_pformat+0x352>
  4054fb:	89 10                	mov    DWORD PTR [eax],edx
  4054fd:	83 c5 04             	add    ebp,0x4
  405500:	e9 0b f8 ff ff       	jmp    404d10 <___mingw_pformat+0x90>
  405505:	0f bf 44 24 20       	movsx  eax,WORD PTR [esp+0x20]
  40550a:	89 d5                	mov    ebp,edx
  40550c:	89 44 24 20          	mov    DWORD PTR [esp+0x20],eax
  405510:	c1 f8 1f             	sar    eax,0x1f
  405513:	89 44 24 24          	mov    DWORD PTR [esp+0x24],eax
  405517:	e9 ab fb ff ff       	jmp    4050c7 <___mingw_pformat+0x447>
  40551c:	bb 58 a1 40 00       	mov    ebx,0x40a158
  405521:	e9 18 fe ff ff       	jmp    40533e <___mingw_pformat+0x6be>
  405526:	8b 54 24 10          	mov    edx,DWORD PTR [esp+0x10]
  40552a:	85 d2                	test   edx,edx
  40552c:	0f 85 99 00 00 00    	jne    4055cb <___mingw_pformat+0x94b>
  405532:	81 4c 24 30 00 04 00 	or     DWORD PTR [esp+0x30],0x400
  405539:	00 
  40553a:	f7 5c 24 34          	neg    DWORD PTR [esp+0x34]
  40553e:	e9 84 fd ff ff       	jmp    4052c7 <___mingw_pformat+0x647>
  405543:	0f be 44 24 20       	movsx  eax,BYTE PTR [esp+0x20]
  405548:	89 44 24 20          	mov    DWORD PTR [esp+0x20],eax
  40554c:	c1 f8 1f             	sar    eax,0x1f
  40554f:	89 44 24 24          	mov    DWORD PTR [esp+0x24],eax
  405553:	e9 6f fb ff ff       	jmp    4050c7 <___mingw_pformat+0x447>
  405558:	0f b6 54 24 20       	movzx  edx,BYTE PTR [esp+0x20]
  40555d:	c7 44 24 24 00 00 00 	mov    DWORD PTR [esp+0x24],0x0
  405564:	00 
  405565:	89 54 24 20          	mov    DWORD PTR [esp+0x20],edx
  405569:	e9 64 fa ff ff       	jmp    404fd2 <___mingw_pformat+0x352>
  40556e:	89 d7                	mov    edi,edx
  405570:	83 c5 04             	add    ebp,0x4
  405573:	c1 ff 1f             	sar    edi,0x1f
  405576:	89 78 04             	mov    DWORD PTR [eax+0x4],edi
  405579:	e9 92 f7 ff ff       	jmp    404d10 <___mingw_pformat+0x90>
  40557e:	0f b6 51 03          	movzx  edx,BYTE PTR [ecx+0x3]
  405582:	83 c1 03             	add    ecx,0x3
  405585:	c7 44 24 14 03 00 00 	mov    DWORD PTR [esp+0x14],0x3
  40558c:	00 
  40558d:	c7 44 24 10 04 00 00 	mov    DWORD PTR [esp+0x10],0x4
  405594:	00 
  405595:	e9 c3 f7 ff ff       	jmp    404d5d <___mingw_pformat+0xdd>
  40559a:	0f b6 51 03          	movzx  edx,BYTE PTR [ecx+0x3]
  40559e:	83 c1 03             	add    ecx,0x3
  4055a1:	c7 44 24 14 02 00 00 	mov    DWORD PTR [esp+0x14],0x2
  4055a8:	00 
  4055a9:	c7 44 24 10 04 00 00 	mov    DWORD PTR [esp+0x10],0x4
  4055b0:	00 
  4055b1:	e9 a7 f7 ff ff       	jmp    404d5d <___mingw_pformat+0xdd>
  4055b6:	8d 54 24 2c          	lea    edx,[esp+0x2c]
  4055ba:	b8 25 00 00 00       	mov    eax,0x25
  4055bf:	89 de                	mov    esi,ebx
  4055c1:	e8 1a e2 ff ff       	call   4037e0 <___pformat_putc>
  4055c6:	e9 45 f7 ff ff       	jmp    404d10 <___mingw_pformat+0x90>
  4055cb:	c7 44 24 38 ff ff ff 	mov    DWORD PTR [esp+0x38],0xffffffff
  4055d2:	ff 
  4055d3:	89 fd                	mov    ebp,edi
  4055d5:	0f b6 51 01          	movzx  edx,BYTE PTR [ecx+0x1]
  4055d9:	c7 44 24 18 00 00 00 	mov    DWORD PTR [esp+0x18],0x0
  4055e0:	00 
  4055e1:	89 f1                	mov    ecx,esi
  4055e3:	e9 75 f7 ff ff       	jmp    404d5d <___mingw_pformat+0xdd>
  4055e8:	90                   	nop
  4055e9:	90                   	nop
  4055ea:	90                   	nop
  4055eb:	90                   	nop
  4055ec:	90                   	nop
  4055ed:	90                   	nop
  4055ee:	90                   	nop
  4055ef:	90                   	nop

004055f0 <___gdtoa>:
  4055f0:	55                   	push   ebp
  4055f1:	57                   	push   edi
  4055f2:	56                   	push   esi
  4055f3:	53                   	push   ebx
  4055f4:	83 ec 6c             	sub    esp,0x6c
  4055f7:	8b 84 24 8c 00 00 00 	mov    eax,DWORD PTR [esp+0x8c]
  4055fe:	8b 9c 24 8c 00 00 00 	mov    ebx,DWORD PTR [esp+0x8c]
  405605:	8b 30                	mov    esi,DWORD PTR [eax]
  405607:	89 f0                	mov    eax,esi
  405609:	83 e0 cf             	and    eax,0xffffffcf
  40560c:	89 03                	mov    DWORD PTR [ebx],eax
  40560e:	89 f0                	mov    eax,esi
  405610:	83 e0 07             	and    eax,0x7
  405613:	83 f8 04             	cmp    eax,0x4
  405616:	0f 87 5f 14 00 00    	ja     406a7b <___gdtoa+0x148b>
  40561c:	ff 24 85 00 a3 40 00 	jmp    DWORD PTR [eax*4+0x40a300]
  405623:	8b 84 24 80 00 00 00 	mov    eax,DWORD PTR [esp+0x80]
  40562a:	31 d2                	xor    edx,edx
  40562c:	8b 38                	mov    edi,DWORD PTR [eax]
  40562e:	83 ff 20             	cmp    edi,0x20
  405631:	7e 0e                	jle    405641 <___gdtoa+0x51>
  405633:	b8 20 00 00 00       	mov    eax,0x20
  405638:	01 c0                	add    eax,eax
  40563a:	83 c2 01             	add    edx,0x1
  40563d:	39 c7                	cmp    edi,eax
  40563f:	7f f7                	jg     405638 <___gdtoa+0x48>
  405641:	89 14 24             	mov    DWORD PTR [esp],edx
  405644:	e8 97 1e 00 00       	call   4074e0 <___Balloc_D2A>
  405649:	8b 8c 24 88 00 00 00 	mov    ecx,DWORD PTR [esp+0x88]
  405650:	89 c3                	mov    ebx,eax
  405652:	8d 47 ff             	lea    eax,[edi-0x1]
  405655:	c1 f8 05             	sar    eax,0x5
  405658:	8d 2c 81             	lea    ebp,[ecx+eax*4]
  40565b:	8b 84 24 88 00 00 00 	mov    eax,DWORD PTR [esp+0x88]
  405662:	8d 4b 14             	lea    ecx,[ebx+0x14]
  405665:	89 ca                	mov    edx,ecx
  405667:	89 4c 24 0c          	mov    DWORD PTR [esp+0xc],ecx
  40566b:	90                   	nop
  40566c:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  405670:	8b 08                	mov    ecx,DWORD PTR [eax]
  405672:	83 c0 04             	add    eax,0x4
  405675:	83 c2 04             	add    edx,0x4
  405678:	39 c5                	cmp    ebp,eax
  40567a:	89 4a fc             	mov    DWORD PTR [edx-0x4],ecx
  40567d:	73 f1                	jae    405670 <___gdtoa+0x80>
  40567f:	8b 4c 24 0c          	mov    ecx,DWORD PTR [esp+0xc]
  405683:	29 ca                	sub    edx,ecx
  405685:	c1 fa 02             	sar    edx,0x2
  405688:	eb 10                	jmp    40569a <___gdtoa+0xaa>
  40568a:	8d b6 00 00 00 00    	lea    esi,[esi+0x0]
  405690:	85 c0                	test   eax,eax
  405692:	0f 84 6e 04 00 00    	je     405b06 <___gdtoa+0x516>
  405698:	89 c2                	mov    edx,eax
  40569a:	8d 42 ff             	lea    eax,[edx-0x1]
  40569d:	8b 2c 81             	mov    ebp,DWORD PTR [ecx+eax*4]
  4056a0:	85 ed                	test   ebp,ebp
  4056a2:	74 ec                	je     405690 <___gdtoa+0xa0>
  4056a4:	0f bd 44 93 10       	bsr    eax,DWORD PTR [ebx+edx*4+0x10]
  4056a9:	89 53 10             	mov    DWORD PTR [ebx+0x10],edx
  4056ac:	c1 e2 05             	shl    edx,0x5
  4056af:	89 d5                	mov    ebp,edx
  4056b1:	83 f0 1f             	xor    eax,0x1f
  4056b4:	29 c5                	sub    ebp,eax
  4056b6:	89 1c 24             	mov    DWORD PTR [esp],ebx
  4056b9:	e8 72 29 00 00       	call   408030 <___trailz_D2A>
  4056be:	8b 8c 24 84 00 00 00 	mov    ecx,DWORD PTR [esp+0x84]
  4056c5:	89 4c 24 20          	mov    DWORD PTR [esp+0x20],ecx
  4056c9:	85 c0                	test   eax,eax
  4056cb:	89 44 24 5c          	mov    DWORD PTR [esp+0x5c],eax
  4056cf:	0f 85 3f 04 00 00    	jne    405b14 <___gdtoa+0x524>
  4056d5:	8b 4b 10             	mov    ecx,DWORD PTR [ebx+0x10]
  4056d8:	85 c9                	test   ecx,ecx
  4056da:	0f 85 a8 00 00 00    	jne    405788 <___gdtoa+0x198>
  4056e0:	89 1c 24             	mov    DWORD PTR [esp],ebx
  4056e3:	e8 c8 1e 00 00       	call   4075b0 <___Bfree_D2A>
  4056e8:	8b 84 24 98 00 00 00 	mov    eax,DWORD PTR [esp+0x98]
  4056ef:	c7 00 01 00 00 00    	mov    DWORD PTR [eax],0x1
  4056f5:	8b 84 24 9c 00 00 00 	mov    eax,DWORD PTR [esp+0x9c]
  4056fc:	c7 44 24 08 01 00 00 	mov    DWORD PTR [esp+0x8],0x1
  405703:	00 
  405704:	c7 04 24 fd a2 40 00 	mov    DWORD PTR [esp],0x40a2fd
  40570b:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
  40570f:	e8 3c 1a 00 00       	call   407150 <___nrv_alloc_D2A>
  405714:	83 c4 6c             	add    esp,0x6c
  405717:	5b                   	pop    ebx
  405718:	5e                   	pop    esi
  405719:	5f                   	pop    edi
  40571a:	5d                   	pop    ebp
  40571b:	c3                   	ret    
  40571c:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  405720:	8b 84 24 98 00 00 00 	mov    eax,DWORD PTR [esp+0x98]
  405727:	c7 00 00 80 ff ff    	mov    DWORD PTR [eax],0xffff8000
  40572d:	8b 84 24 9c 00 00 00 	mov    eax,DWORD PTR [esp+0x9c]
  405734:	c7 44 24 08 03 00 00 	mov    DWORD PTR [esp+0x8],0x3
  40573b:	00 
  40573c:	c7 04 24 f9 a2 40 00 	mov    DWORD PTR [esp],0x40a2f9
  405743:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
  405747:	e8 04 1a 00 00       	call   407150 <___nrv_alloc_D2A>
  40574c:	83 c4 6c             	add    esp,0x6c
  40574f:	5b                   	pop    ebx
  405750:	5e                   	pop    esi
  405751:	5f                   	pop    edi
  405752:	5d                   	pop    ebp
  405753:	c3                   	ret    
  405754:	8b 84 24 98 00 00 00 	mov    eax,DWORD PTR [esp+0x98]
  40575b:	c7 00 00 80 ff ff    	mov    DWORD PTR [eax],0xffff8000
  405761:	8b 84 24 9c 00 00 00 	mov    eax,DWORD PTR [esp+0x9c]
  405768:	c7 44 24 08 08 00 00 	mov    DWORD PTR [esp+0x8],0x8
  40576f:	00 
  405770:	c7 04 24 f0 a2 40 00 	mov    DWORD PTR [esp],0x40a2f0
  405777:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
  40577b:	e8 d0 19 00 00       	call   407150 <___nrv_alloc_D2A>
  405780:	83 c4 6c             	add    esp,0x6c
  405783:	5b                   	pop    ebx
  405784:	5e                   	pop    esi
  405785:	5f                   	pop    edi
  405786:	5d                   	pop    ebp
  405787:	c3                   	ret    
  405788:	8d 44 24 5c          	lea    eax,[esp+0x5c]
  40578c:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
  405790:	89 1c 24             	mov    DWORD PTR [esp],ebx
  405793:	e8 68 25 00 00       	call   407d00 <___b2d_D2A>
  405798:	8b 44 24 20          	mov    eax,DWORD PTR [esp+0x20]
  40579c:	8d 54 28 ff          	lea    edx,[eax+ebp*1-0x1]
  4057a0:	89 54 24 48          	mov    DWORD PTR [esp+0x48],edx
  4057a4:	89 d0                	mov    eax,edx
  4057a6:	dd 5c 24 10          	fstp   QWORD PTR [esp+0x10]
  4057aa:	8b 4c 24 14          	mov    ecx,DWORD PTR [esp+0x14]
  4057ae:	c1 f8 1f             	sar    eax,0x1f
  4057b1:	89 44 24 0c          	mov    DWORD PTR [esp+0xc],eax
  4057b5:	31 d0                	xor    eax,edx
  4057b7:	2b 44 24 0c          	sub    eax,DWORD PTR [esp+0xc]
  4057bb:	81 e1 ff ff 0f 00    	and    ecx,0xfffff
  4057c1:	81 c9 00 00 f0 3f    	or     ecx,0x3ff00000
  4057c7:	89 4c 24 14          	mov    DWORD PTR [esp+0x14],ecx
  4057cb:	2d 35 04 00 00       	sub    eax,0x435
  4057d0:	dd 44 24 10          	fld    QWORD PTR [esp+0x10]
  4057d4:	85 c0                	test   eax,eax
  4057d6:	d8 25 14 a3 40 00    	fsub   DWORD PTR ds:0x40a314
  4057dc:	dc 0d 18 a3 40 00    	fmul   QWORD PTR ds:0x40a318
  4057e2:	dc 05 20 a3 40 00    	fadd   QWORD PTR ds:0x40a320
  4057e8:	db 44 24 48          	fild   DWORD PTR [esp+0x48]
  4057ec:	dc 0d 28 a3 40 00    	fmul   QWORD PTR ds:0x40a328
  4057f2:	de c1                	faddp  st(1),st
  4057f4:	7e 10                	jle    405806 <___gdtoa+0x216>
  4057f6:	89 44 24 48          	mov    DWORD PTR [esp+0x48],eax
  4057fa:	db 44 24 48          	fild   DWORD PTR [esp+0x48]
  4057fe:	dc 0d 30 a3 40 00    	fmul   QWORD PTR ds:0x40a330
  405804:	de c1                	faddp  st(1),st
  405806:	d9 7c 24 4e          	fnstcw WORD PTR [esp+0x4e]
  40580a:	0f b7 44 24 4e       	movzx  eax,WORD PTR [esp+0x4e]
  40580f:	b4 0c                	mov    ah,0xc
  405811:	66 89 44 24 4c       	mov    WORD PTR [esp+0x4c],ax
  405816:	d9 6c 24 4c          	fldcw  WORD PTR [esp+0x4c]
  40581a:	db 54 24 0c          	fist   DWORD PTR [esp+0xc]
  40581e:	d9 6c 24 4e          	fldcw  WORD PTR [esp+0x4e]
  405822:	d9 ee                	fldz   
  405824:	dd e9                	fucomp st(1)
  405826:	df e0                	fnstsw ax
  405828:	9e                   	sahf   
  405829:	0f 87 76 07 00 00    	ja     405fa5 <___gdtoa+0x9b5>
  40582f:	dd d8                	fstp   st(0)
  405831:	89 d0                	mov    eax,edx
  405833:	c1 e0 14             	shl    eax,0x14
  405836:	01 c8                	add    eax,ecx
  405838:	83 7c 24 0c 16       	cmp    DWORD PTR [esp+0xc],0x16
  40583d:	89 44 24 14          	mov    DWORD PTR [esp+0x14],eax
  405841:	c7 44 24 34 01 00 00 	mov    DWORD PTR [esp+0x34],0x1
  405848:	00 
  405849:	77 29                	ja     405874 <___gdtoa+0x284>
  40584b:	8b 44 24 0c          	mov    eax,DWORD PTR [esp+0xc]
  40584f:	dd 04 c5 80 a3 40 00 	fld    QWORD PTR [eax*8+0x40a380]
  405856:	dd 44 24 10          	fld    QWORD PTR [esp+0x10]
  40585a:	d9 c9                	fxch   st(1)
  40585c:	da e9                	fucompp 
  40585e:	df e0                	fnstsw ax
  405860:	9e                   	sahf   
  405861:	0f 86 6d 06 00 00    	jbe    405ed4 <___gdtoa+0x8e4>
  405867:	83 6c 24 0c 01       	sub    DWORD PTR [esp+0xc],0x1
  40586c:	c7 44 24 34 00 00 00 	mov    DWORD PTR [esp+0x34],0x0
  405873:	00 
  405874:	89 e8                	mov    eax,ebp
  405876:	29 d0                	sub    eax,edx
  405878:	83 e8 01             	sub    eax,0x1
  40587b:	c7 44 24 28 00 00 00 	mov    DWORD PTR [esp+0x28],0x0
  405882:	00 
  405883:	89 44 24 1c          	mov    DWORD PTR [esp+0x1c],eax
  405887:	0f 88 05 07 00 00    	js     405f92 <___gdtoa+0x9a2>
  40588d:	8b 44 24 0c          	mov    eax,DWORD PTR [esp+0xc]
  405891:	85 c0                	test   eax,eax
  405893:	0f 88 de 06 00 00    	js     405f77 <___gdtoa+0x987>
  405899:	01 44 24 1c          	add    DWORD PTR [esp+0x1c],eax
  40589d:	89 44 24 3c          	mov    DWORD PTR [esp+0x3c],eax
  4058a1:	c7 44 24 30 00 00 00 	mov    DWORD PTR [esp+0x30],0x0
  4058a8:	00 
  4058a9:	83 bc 24 90 00 00 00 	cmp    DWORD PTR [esp+0x90],0x9
  4058b0:	09 
  4058b1:	0f 87 81 02 00 00    	ja     405b38 <___gdtoa+0x548>
  4058b7:	83 bc 24 90 00 00 00 	cmp    DWORD PTR [esp+0x90],0x5
  4058be:	05 
  4058bf:	0f 8e c0 11 00 00    	jle    406a85 <___gdtoa+0x1495>
  4058c5:	83 ac 24 90 00 00 00 	sub    DWORD PTR [esp+0x90],0x4
  4058cc:	04 
  4058cd:	31 c0                	xor    eax,eax
  4058cf:	83 bc 24 90 00 00 00 	cmp    DWORD PTR [esp+0x90],0x3
  4058d6:	03 
  4058d7:	0f 84 11 06 00 00    	je     405eee <___gdtoa+0x8fe>
  4058dd:	0f 8e 18 06 00 00    	jle    405efb <___gdtoa+0x90b>
  4058e3:	83 bc 24 90 00 00 00 	cmp    DWORD PTR [esp+0x90],0x4
  4058ea:	04 
  4058eb:	c7 44 24 40 01 00 00 	mov    DWORD PTR [esp+0x40],0x1
  4058f2:	00 
  4058f3:	0f 84 18 06 00 00    	je     405f11 <___gdtoa+0x921>
  4058f9:	83 bc 24 90 00 00 00 	cmp    DWORD PTR [esp+0x90],0x5
  405900:	05 
  405901:	0f 85 3c 02 00 00    	jne    405b43 <___gdtoa+0x553>
  405907:	8b 4c 24 0c          	mov    ecx,DWORD PTR [esp+0xc]
  40590b:	03 8c 24 94 00 00 00 	add    ecx,DWORD PTR [esp+0x94]
  405912:	89 4c 24 44          	mov    DWORD PTR [esp+0x44],ecx
  405916:	83 c1 01             	add    ecx,0x1
  405919:	85 c9                	test   ecx,ecx
  40591b:	89 4c 24 18          	mov    DWORD PTR [esp+0x18],ecx
  40591f:	0f 8e e3 0a 00 00    	jle    406408 <___gdtoa+0xe18>
  405925:	83 f9 0e             	cmp    ecx,0xe
  405928:	0f 96 c2             	setbe  dl
  40592b:	21 c2                	and    edx,eax
  40592d:	89 c8                	mov    eax,ecx
  40592f:	89 4c 24 5c          	mov    DWORD PTR [esp+0x5c],ecx
  405933:	89 04 24             	mov    DWORD PTR [esp],eax
  405936:	89 54 24 38          	mov    DWORD PTR [esp+0x38],edx
  40593a:	e8 d1 17 00 00       	call   407110 <___rv_alloc_D2A>
  40593f:	8b 54 24 38          	mov    edx,DWORD PTR [esp+0x38]
  405943:	89 44 24 24          	mov    DWORD PTR [esp+0x24],eax
  405947:	8b 84 24 80 00 00 00 	mov    eax,DWORD PTR [esp+0x80]
  40594e:	8b 40 0c             	mov    eax,DWORD PTR [eax+0xc]
  405951:	83 e8 01             	sub    eax,0x1
  405954:	89 44 24 2c          	mov    DWORD PTR [esp+0x2c],eax
  405958:	74 0f                	je     405969 <___gdtoa+0x379>
  40595a:	0f 88 81 05 00 00    	js     405ee1 <___gdtoa+0x8f1>
  405960:	83 e6 08             	and    esi,0x8
  405963:	0f 85 59 05 00 00    	jne    405ec2 <___gdtoa+0x8d2>
  405969:	84 d2                	test   dl,dl
  40596b:	90                   	nop
  40596c:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  405970:	0f 84 70 02 00 00    	je     405be6 <___gdtoa+0x5f6>
  405976:	8b 44 24 2c          	mov    eax,DWORD PTR [esp+0x2c]
  40597a:	0b 44 24 0c          	or     eax,DWORD PTR [esp+0xc]
  40597e:	0f 85 62 02 00 00    	jne    405be6 <___gdtoa+0x5f6>
  405984:	8b 44 24 34          	mov    eax,DWORD PTR [esp+0x34]
  405988:	c7 44 24 5c 00 00 00 	mov    DWORD PTR [esp+0x5c],0x0
  40598f:	00 
  405990:	dd 44 24 10          	fld    QWORD PTR [esp+0x10]
  405994:	85 c0                	test   eax,eax
  405996:	74 0d                	je     4059a5 <___gdtoa+0x3b5>
  405998:	d9 e8                	fld1   
  40599a:	dd e9                	fucomp st(1)
  40599c:	df e0                	fnstsw ax
  40599e:	9e                   	sahf   
  40599f:	0f 87 e7 0d 00 00    	ja     40678c <___gdtoa+0x119c>
  4059a5:	d9 c0                	fld    st(0)
  4059a7:	8b 74 24 18          	mov    esi,DWORD PTR [esp+0x18]
  4059ab:	d8 c1                	fadd   st,st(1)
  4059ad:	d8 05 4c a3 40 00    	fadd   DWORD PTR ds:0x40a34c
  4059b3:	dd 5c 24 10          	fstp   QWORD PTR [esp+0x10]
  4059b7:	81 6c 24 14 00 00 40 	sub    DWORD PTR [esp+0x14],0x3400000
  4059be:	03 
  4059bf:	85 f6                	test   esi,esi
  4059c1:	0f 84 e1 01 00 00    	je     405ba8 <___gdtoa+0x5b8>
  4059c7:	8b 54 24 18          	mov    edx,DWORD PTR [esp+0x18]
  4059cb:	d9 c0                	fld    st(0)
  4059cd:	c7 44 24 38 00 00 00 	mov    DWORD PTR [esp+0x38],0x0
  4059d4:	00 
  4059d5:	8b 4c 24 40          	mov    ecx,DWORD PTR [esp+0x40]
  4059d9:	85 c9                	test   ecx,ecx
  4059db:	0f 84 58 0a 00 00    	je     406439 <___gdtoa+0xe49>
  4059e1:	d9 05 54 a3 40 00    	fld    DWORD PTR ds:0x40a354
  4059e7:	dc 34 d5 78 a3 40 00 	fdiv   QWORD PTR [edx*8+0x40a378]
  4059ee:	d9 7c 24 4e          	fnstcw WORD PTR [esp+0x4e]
  4059f2:	c7 44 24 5c 00 00 00 	mov    DWORD PTR [esp+0x5c],0x0
  4059f9:	00 
  4059fa:	0f b7 44 24 4e       	movzx  eax,WORD PTR [esp+0x4e]
  4059ff:	b4 0c                	mov    ah,0xc
  405a01:	66 89 44 24 4c       	mov    WORD PTR [esp+0x4c],ax
  405a06:	8b 44 24 24          	mov    eax,DWORD PTR [esp+0x24]
  405a0a:	8d 70 01             	lea    esi,[eax+0x1]
  405a0d:	dc 64 24 10          	fsub   QWORD PTR [esp+0x10]
  405a11:	d9 c9                	fxch   st(1)
  405a13:	d9 6c 24 4c          	fldcw  WORD PTR [esp+0x4c]
  405a17:	db 54 24 48          	fist   DWORD PTR [esp+0x48]
  405a1b:	d9 6c 24 4e          	fldcw  WORD PTR [esp+0x4e]
  405a1f:	8b 4c 24 48          	mov    ecx,DWORD PTR [esp+0x48]
  405a23:	89 4c 24 48          	mov    DWORD PTR [esp+0x48],ecx
  405a27:	83 c1 30             	add    ecx,0x30
  405a2a:	db 44 24 48          	fild   DWORD PTR [esp+0x48]
  405a2e:	de e9                	fsubrp st(1),st
  405a30:	d9 c9                	fxch   st(1)
  405a32:	88 08                	mov    BYTE PTR [eax],cl
  405a34:	dd e1                	fucom  st(1)
  405a36:	df e0                	fnstsw ax
  405a38:	9e                   	sahf   
  405a39:	0f 87 9a 00 00 00    	ja     405ad9 <___gdtoa+0x4e9>
  405a3f:	d9 c1                	fld    st(1)
  405a41:	d8 2d 40 a3 40 00    	fsubr  DWORD PTR ds:0x40a340
  405a47:	d9 c9                	fxch   st(1)
  405a49:	dd e1                	fucom  st(1)
  405a4b:	df e0                	fnstsw ax
  405a4d:	dd d9                	fstp   st(1)
  405a4f:	9e                   	sahf   
  405a50:	0f 87 f1 0a 00 00    	ja     406547 <___gdtoa+0xf57>
  405a56:	8b 44 24 5c          	mov    eax,DWORD PTR [esp+0x5c]
  405a5a:	83 c0 01             	add    eax,0x1
  405a5d:	39 c2                	cmp    edx,eax
  405a5f:	89 44 24 5c          	mov    DWORD PTR [esp+0x5c],eax
  405a63:	0f 8e 69 01 00 00    	jle    405bd2 <___gdtoa+0x5e2>
  405a69:	d9 05 44 a3 40 00    	fld    DWORD PTR ds:0x40a344
  405a6f:	eb 2e                	jmp    405a9f <___gdtoa+0x4af>
  405a71:	d9 c1                	fld    st(1)
  405a73:	d8 2d 40 a3 40 00    	fsubr  DWORD PTR ds:0x40a340
  405a79:	d9 c9                	fxch   st(1)
  405a7b:	dd e1                	fucom  st(1)
  405a7d:	df e0                	fnstsw ax
  405a7f:	dd d9                	fstp   st(1)
  405a81:	9e                   	sahf   
  405a82:	0f 87 c7 0a 00 00    	ja     40654f <___gdtoa+0xf5f>
  405a88:	8b 44 24 5c          	mov    eax,DWORD PTR [esp+0x5c]
  405a8c:	83 c0 01             	add    eax,0x1
  405a8f:	39 c2                	cmp    edx,eax
  405a91:	89 44 24 5c          	mov    DWORD PTR [esp+0x5c],eax
  405a95:	0f 8e 3d 01 00 00    	jle    405bd8 <___gdtoa+0x5e8>
  405a9b:	d9 c9                	fxch   st(1)
  405a9d:	d9 ca                	fxch   st(2)
  405a9f:	dc c9                	fmul   st(1),st
  405aa1:	83 c6 01             	add    esi,0x1
  405aa4:	dc ca                	fmul   st(2),st
  405aa6:	d9 ca                	fxch   st(2)
  405aa8:	d9 6c 24 4c          	fldcw  WORD PTR [esp+0x4c]
  405aac:	db 54 24 48          	fist   DWORD PTR [esp+0x48]
  405ab0:	d9 6c 24 4e          	fldcw  WORD PTR [esp+0x4e]
  405ab4:	8b 44 24 48          	mov    eax,DWORD PTR [esp+0x48]
  405ab8:	89 44 24 48          	mov    DWORD PTR [esp+0x48],eax
  405abc:	8d 48 30             	lea    ecx,[eax+0x30]
  405abf:	db 44 24 48          	fild   DWORD PTR [esp+0x48]
  405ac3:	de e9                	fsubrp st(1),st
  405ac5:	d9 c9                	fxch   st(1)
  405ac7:	88 4e ff             	mov    BYTE PTR [esi-0x1],cl
  405aca:	dd e1                	fucom  st(1)
  405acc:	df e0                	fnstsw ax
  405ace:	9e                   	sahf   
  405acf:	76 a0                	jbe    405a71 <___gdtoa+0x481>
  405ad1:	dd d8                	fstp   st(0)
  405ad3:	dd d9                	fstp   st(1)
  405ad5:	dd d9                	fstp   st(1)
  405ad7:	eb 04                	jmp    405add <___gdtoa+0x4ed>
  405ad9:	dd d8                	fstp   st(0)
  405adb:	dd d9                	fstp   st(1)
  405add:	d9 ee                	fldz   
  405adf:	d9 c9                	fxch   st(1)
  405ae1:	da e9                	fucompp 
  405ae3:	df e0                	fnstsw ax
  405ae5:	9e                   	sahf   
  405ae6:	8b 44 24 38          	mov    eax,DWORD PTR [esp+0x38]
  405aea:	7a 06                	jp     405af2 <___gdtoa+0x502>
  405aec:	0f 84 ad 05 00 00    	je     40609f <___gdtoa+0xaaf>
  405af2:	83 c0 01             	add    eax,0x1
  405af5:	89 44 24 0c          	mov    DWORD PTR [esp+0xc],eax
  405af9:	c7 44 24 18 10 00 00 	mov    DWORD PTR [esp+0x18],0x10
  405b00:	00 
  405b01:	e9 77 03 00 00       	jmp    405e7d <___gdtoa+0x88d>
  405b06:	c7 43 10 00 00 00 00 	mov    DWORD PTR [ebx+0x10],0x0
  405b0d:	31 ed                	xor    ebp,ebp
  405b0f:	e9 a2 fb ff ff       	jmp    4056b6 <___gdtoa+0xc6>
  405b14:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
  405b18:	89 1c 24             	mov    DWORD PTR [esp],ebx
  405b1b:	e8 f0 23 00 00       	call   407f10 <___rshift_D2A>
  405b20:	8b 44 24 5c          	mov    eax,DWORD PTR [esp+0x5c]
  405b24:	8b 8c 24 84 00 00 00 	mov    ecx,DWORD PTR [esp+0x84]
  405b2b:	29 c5                	sub    ebp,eax
  405b2d:	01 c1                	add    ecx,eax
  405b2f:	89 4c 24 20          	mov    DWORD PTR [esp+0x20],ecx
  405b33:	e9 9d fb ff ff       	jmp    4056d5 <___gdtoa+0xe5>
  405b38:	c7 84 24 90 00 00 00 	mov    DWORD PTR [esp+0x90],0x0
  405b3f:	00 00 00 00 
  405b43:	89 7c 24 48          	mov    DWORD PTR [esp+0x48],edi
  405b47:	31 d2                	xor    edx,edx
  405b49:	db 44 24 48          	fild   DWORD PTR [esp+0x48]
  405b4d:	dc 0d 38 a3 40 00    	fmul   QWORD PTR ds:0x40a338
  405b53:	c7 44 24 40 01 00 00 	mov    DWORD PTR [esp+0x40],0x1
  405b5a:	00 
  405b5b:	c7 44 24 44 ff ff ff 	mov    DWORD PTR [esp+0x44],0xffffffff
  405b62:	ff 
  405b63:	c7 44 24 18 ff ff ff 	mov    DWORD PTR [esp+0x18],0xffffffff
  405b6a:	ff 
  405b6b:	c7 84 24 94 00 00 00 	mov    DWORD PTR [esp+0x94],0x0
  405b72:	00 00 00 00 
  405b76:	d9 6c 24 4c          	fldcw  WORD PTR [esp+0x4c]
  405b7a:	db 5c 24 48          	fistp  DWORD PTR [esp+0x48]
  405b7e:	d9 6c 24 4e          	fldcw  WORD PTR [esp+0x4e]
  405b82:	8b 44 24 48          	mov    eax,DWORD PTR [esp+0x48]
  405b86:	83 c0 03             	add    eax,0x3
  405b89:	89 44 24 5c          	mov    DWORD PTR [esp+0x5c],eax
  405b8d:	e9 a1 fd ff ff       	jmp    405933 <___gdtoa+0x343>
  405b92:	d9 c0                	fld    st(0)
  405b94:	d8 c1                	fadd   st,st(1)
  405b96:	d8 05 4c a3 40 00    	fadd   DWORD PTR ds:0x40a34c
  405b9c:	dd 5c 24 10          	fstp   QWORD PTR [esp+0x10]
  405ba0:	81 6c 24 14 00 00 40 	sub    DWORD PTR [esp+0x14],0x3400000
  405ba7:	03 
  405ba8:	d9 c0                	fld    st(0)
  405baa:	d8 25 50 a3 40 00    	fsub   DWORD PTR ds:0x40a350
  405bb0:	dd 44 24 10          	fld    QWORD PTR [esp+0x10]
  405bb4:	d9 c9                	fxch   st(1)
  405bb6:	dd e1                	fucom  st(1)
  405bb8:	df e0                	fnstsw ax
  405bba:	9e                   	sahf   
  405bbb:	0f 87 52 09 00 00    	ja     406513 <___gdtoa+0xf23>
  405bc1:	d9 c9                	fxch   st(1)
  405bc3:	d9 e0                	fchs   
  405bc5:	da e9                	fucompp 
  405bc7:	df e0                	fnstsw ax
  405bc9:	9e                   	sahf   
  405bca:	0f 87 77 03 00 00    	ja     405f47 <___gdtoa+0x957>
  405bd0:	eb 10                	jmp    405be2 <___gdtoa+0x5f2>
  405bd2:	dd d8                	fstp   st(0)
  405bd4:	dd d8                	fstp   st(0)
  405bd6:	eb 0a                	jmp    405be2 <___gdtoa+0x5f2>
  405bd8:	dd d8                	fstp   st(0)
  405bda:	dd d8                	fstp   st(0)
  405bdc:	dd d8                	fstp   st(0)
  405bde:	eb 02                	jmp    405be2 <___gdtoa+0x5f2>
  405be0:	dd d8                	fstp   st(0)
  405be2:	dd 5c 24 10          	fstp   QWORD PTR [esp+0x10]
  405be6:	83 7c 24 0c 0e       	cmp    DWORD PTR [esp+0xc],0xe
  405beb:	0f 8e df 01 00 00    	jle    405dd0 <___gdtoa+0x7e0>
  405bf1:	8b 44 24 40          	mov    eax,DWORD PTR [esp+0x40]
  405bf5:	85 c0                	test   eax,eax
  405bf7:	0f 84 c3 03 00 00    	je     405fc0 <___gdtoa+0x9d0>
  405bfd:	83 bc 24 90 00 00 00 	cmp    DWORD PTR [esp+0x90],0x1
  405c04:	01 
  405c05:	0f 8e 93 09 00 00    	jle    40659e <___gdtoa+0xfae>
  405c0b:	8b 44 24 18          	mov    eax,DWORD PTR [esp+0x18]
  405c0f:	83 e8 01             	sub    eax,0x1
  405c12:	39 44 24 30          	cmp    DWORD PTR [esp+0x30],eax
  405c16:	0f 8c 08 08 00 00    	jl     406424 <___gdtoa+0xe34>
  405c1c:	8b 7c 24 30          	mov    edi,DWORD PTR [esp+0x30]
  405c20:	29 c7                	sub    edi,eax
  405c22:	8b 44 24 18          	mov    eax,DWORD PTR [esp+0x18]
  405c26:	85 c0                	test   eax,eax
  405c28:	0f 88 15 0a 00 00    	js     406643 <___gdtoa+0x1053>
  405c2e:	8b 74 24 28          	mov    esi,DWORD PTR [esp+0x28]
  405c32:	89 44 24 5c          	mov    DWORD PTR [esp+0x5c],eax
  405c36:	c7 04 24 01 00 00 00 	mov    DWORD PTR [esp],0x1
  405c3d:	01 44 24 28          	add    DWORD PTR [esp+0x28],eax
  405c41:	01 44 24 1c          	add    DWORD PTR [esp+0x1c],eax
  405c45:	e8 b6 1a 00 00       	call   407700 <___i2b_D2A>
  405c4a:	89 44 24 20          	mov    DWORD PTR [esp+0x20],eax
  405c4e:	8b 44 24 1c          	mov    eax,DWORD PTR [esp+0x1c]
  405c52:	85 c0                	test   eax,eax
  405c54:	7e 1e                	jle    405c74 <___gdtoa+0x684>
  405c56:	85 f6                	test   esi,esi
  405c58:	7e 1a                	jle    405c74 <___gdtoa+0x684>
  405c5a:	8b 4c 24 1c          	mov    ecx,DWORD PTR [esp+0x1c]
  405c5e:	39 f1                	cmp    ecx,esi
  405c60:	89 c8                	mov    eax,ecx
  405c62:	7e 02                	jle    405c66 <___gdtoa+0x676>
  405c64:	89 f0                	mov    eax,esi
  405c66:	29 44 24 28          	sub    DWORD PTR [esp+0x28],eax
  405c6a:	29 c6                	sub    esi,eax
  405c6c:	29 44 24 1c          	sub    DWORD PTR [esp+0x1c],eax
  405c70:	89 44 24 5c          	mov    DWORD PTR [esp+0x5c],eax
  405c74:	8b 4c 24 30          	mov    ecx,DWORD PTR [esp+0x30]
  405c78:	85 c9                	test   ecx,ecx
  405c7a:	7e 4e                	jle    405cca <___gdtoa+0x6da>
  405c7c:	8b 54 24 40          	mov    edx,DWORD PTR [esp+0x40]
  405c80:	85 d2                	test   edx,edx
  405c82:	0f 84 dd 05 00 00    	je     406265 <___gdtoa+0xc75>
  405c88:	85 ff                	test   edi,edi
  405c8a:	7e 32                	jle    405cbe <___gdtoa+0x6ce>
  405c8c:	8b 44 24 20          	mov    eax,DWORD PTR [esp+0x20]
  405c90:	89 7c 24 04          	mov    DWORD PTR [esp+0x4],edi
  405c94:	89 04 24             	mov    DWORD PTR [esp],eax
  405c97:	e8 f4 1b 00 00       	call   407890 <___pow5mult_D2A>
  405c9c:	89 5c 24 04          	mov    DWORD PTR [esp+0x4],ebx
  405ca0:	89 04 24             	mov    DWORD PTR [esp],eax
  405ca3:	89 44 24 20          	mov    DWORD PTR [esp+0x20],eax
  405ca7:	e8 84 1a 00 00       	call   407730 <___mult_D2A>
  405cac:	89 1c 24             	mov    DWORD PTR [esp],ebx
  405caf:	89 44 24 10          	mov    DWORD PTR [esp+0x10],eax
  405cb3:	e8 f8 18 00 00       	call   4075b0 <___Bfree_D2A>
  405cb8:	8b 44 24 10          	mov    eax,DWORD PTR [esp+0x10]
  405cbc:	89 c3                	mov    ebx,eax
  405cbe:	8b 44 24 30          	mov    eax,DWORD PTR [esp+0x30]
  405cc2:	29 f8                	sub    eax,edi
  405cc4:	0f 85 9f 05 00 00    	jne    406269 <___gdtoa+0xc79>
  405cca:	c7 04 24 01 00 00 00 	mov    DWORD PTR [esp],0x1
  405cd1:	e8 2a 1a 00 00       	call   407700 <___i2b_D2A>
  405cd6:	89 c7                	mov    edi,eax
  405cd8:	8b 44 24 3c          	mov    eax,DWORD PTR [esp+0x3c]
  405cdc:	85 c0                	test   eax,eax
  405cde:	7e 0e                	jle    405cee <___gdtoa+0x6fe>
  405ce0:	89 3c 24             	mov    DWORD PTR [esp],edi
  405ce3:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
  405ce7:	e8 a4 1b 00 00       	call   407890 <___pow5mult_D2A>
  405cec:	89 c7                	mov    edi,eax
  405cee:	83 bc 24 90 00 00 00 	cmp    DWORD PTR [esp+0x90],0x1
  405cf5:	01 
  405cf6:	c7 44 24 10 00 00 00 	mov    DWORD PTR [esp+0x10],0x0
  405cfd:	00 
  405cfe:	0f 8e 8f 06 00 00    	jle    406393 <___gdtoa+0xda3>
  405d04:	8b 44 24 3c          	mov    eax,DWORD PTR [esp+0x3c]
  405d08:	bd 1f 00 00 00       	mov    ebp,0x1f
  405d0d:	85 c0                	test   eax,eax
  405d0f:	74 0b                	je     405d1c <___gdtoa+0x72c>
  405d11:	8b 47 10             	mov    eax,DWORD PTR [edi+0x10]
  405d14:	0f bd 6c 87 10       	bsr    ebp,DWORD PTR [edi+eax*4+0x10]
  405d19:	83 f5 1f             	xor    ebp,0x1f
  405d1c:	2b 6c 24 1c          	sub    ebp,DWORD PTR [esp+0x1c]
  405d20:	8b 54 24 28          	mov    edx,DWORD PTR [esp+0x28]
  405d24:	83 ed 04             	sub    ebp,0x4
  405d27:	83 e5 1f             	and    ebp,0x1f
  405d2a:	01 ea                	add    edx,ebp
  405d2c:	89 e8                	mov    eax,ebp
  405d2e:	85 d2                	test   edx,edx
  405d30:	89 6c 24 5c          	mov    DWORD PTR [esp+0x5c],ebp
  405d34:	7e 12                	jle    405d48 <___gdtoa+0x758>
  405d36:	89 1c 24             	mov    DWORD PTR [esp],ebx
  405d39:	89 54 24 04          	mov    DWORD PTR [esp+0x4],edx
  405d3d:	e8 de 1c 00 00       	call   407a20 <___lshift_D2A>
  405d42:	89 c3                	mov    ebx,eax
  405d44:	8b 44 24 5c          	mov    eax,DWORD PTR [esp+0x5c]
  405d48:	03 44 24 1c          	add    eax,DWORD PTR [esp+0x1c]
  405d4c:	85 c0                	test   eax,eax
  405d4e:	7e 0e                	jle    405d5e <___gdtoa+0x76e>
  405d50:	89 3c 24             	mov    DWORD PTR [esp],edi
  405d53:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
  405d57:	e8 c4 1c 00 00       	call   407a20 <___lshift_D2A>
  405d5c:	89 c7                	mov    edi,eax
  405d5e:	8b 44 24 34          	mov    eax,DWORD PTR [esp+0x34]
  405d62:	85 c0                	test   eax,eax
  405d64:	0f 85 12 05 00 00    	jne    40627c <___gdtoa+0xc8c>
  405d6a:	83 bc 24 90 00 00 00 	cmp    DWORD PTR [esp+0x90],0x2
  405d71:	02 
  405d72:	0f 8e 3b 03 00 00    	jle    4060b3 <___gdtoa+0xac3>
  405d78:	8b 44 24 18          	mov    eax,DWORD PTR [esp+0x18]
  405d7c:	85 c0                	test   eax,eax
  405d7e:	0f 8f 2f 03 00 00    	jg     4060b3 <___gdtoa+0xac3>
  405d84:	8b 44 24 18          	mov    eax,DWORD PTR [esp+0x18]
  405d88:	85 c0                	test   eax,eax
  405d8a:	0f 85 c7 01 00 00    	jne    405f57 <___gdtoa+0x967>
  405d90:	89 3c 24             	mov    DWORD PTR [esp],edi
  405d93:	c7 44 24 08 00 00 00 	mov    DWORD PTR [esp+0x8],0x0
  405d9a:	00 
  405d9b:	c7 44 24 04 05 00 00 	mov    DWORD PTR [esp+0x4],0x5
  405da2:	00 
  405da3:	e8 78 18 00 00       	call   407620 <___multadd_D2A>
  405da8:	89 1c 24             	mov    DWORD PTR [esp],ebx
  405dab:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
  405daf:	89 c7                	mov    edi,eax
  405db1:	e8 7a 1d 00 00       	call   407b30 <___cmp_D2A>
  405db6:	85 c0                	test   eax,eax
  405db8:	0f 8e 99 01 00 00    	jle    405f57 <___gdtoa+0x967>
  405dbe:	8b 44 24 0c          	mov    eax,DWORD PTR [esp+0xc]
  405dc2:	83 c0 02             	add    eax,0x2
  405dc5:	89 44 24 0c          	mov    DWORD PTR [esp+0xc],eax
  405dc9:	eb 72                	jmp    405e3d <___gdtoa+0x84d>
  405dcb:	90                   	nop
  405dcc:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  405dd0:	8b 44 24 20          	mov    eax,DWORD PTR [esp+0x20]
  405dd4:	85 c0                	test   eax,eax
  405dd6:	0f 88 15 fe ff ff    	js     405bf1 <___gdtoa+0x601>
  405ddc:	8b 44 24 0c          	mov    eax,DWORD PTR [esp+0xc]
  405de0:	dd 04 c5 80 a3 40 00 	fld    QWORD PTR [eax*8+0x40a380]
  405de7:	8b 44 24 18          	mov    eax,DWORD PTR [esp+0x18]
  405deb:	85 c0                	test   eax,eax
  405ded:	0f 8f e2 01 00 00    	jg     405fd5 <___gdtoa+0x9e5>
  405df3:	8b 84 24 94 00 00 00 	mov    eax,DWORD PTR [esp+0x94]
  405dfa:	c1 e8 1f             	shr    eax,0x1f
  405dfd:	84 c0                	test   al,al
  405dff:	0f 84 d0 01 00 00    	je     405fd5 <___gdtoa+0x9e5>
  405e05:	8b 44 24 18          	mov    eax,DWORD PTR [esp+0x18]
  405e09:	85 c0                	test   eax,eax
  405e0b:	0f 85 3a 01 00 00    	jne    405f4b <___gdtoa+0x95b>
  405e11:	d8 0d 50 a3 40 00    	fmul   DWORD PTR ds:0x40a350
  405e17:	dd 44 24 10          	fld    QWORD PTR [esp+0x10]
  405e1b:	d9 c9                	fxch   st(1)
  405e1d:	da e9                	fucompp 
  405e1f:	df e0                	fnstsw ax
  405e21:	9e                   	sahf   
  405e22:	0f 83 25 01 00 00    	jae    405f4d <___gdtoa+0x95d>
  405e28:	8b 44 24 0c          	mov    eax,DWORD PTR [esp+0xc]
  405e2c:	31 ff                	xor    edi,edi
  405e2e:	c7 44 24 20 00 00 00 	mov    DWORD PTR [esp+0x20],0x0
  405e35:	00 
  405e36:	83 c0 02             	add    eax,0x2
  405e39:	89 44 24 0c          	mov    DWORD PTR [esp+0xc],eax
  405e3d:	8b 44 24 24          	mov    eax,DWORD PTR [esp+0x24]
  405e41:	31 d2                	xor    edx,edx
  405e43:	c7 44 24 18 20 00 00 	mov    DWORD PTR [esp+0x18],0x20
  405e4a:	00 
  405e4b:	8d 70 01             	lea    esi,[eax+0x1]
  405e4e:	c6 00 31             	mov    BYTE PTR [eax],0x31
  405e51:	89 3c 24             	mov    DWORD PTR [esp],edi
  405e54:	89 54 24 10          	mov    DWORD PTR [esp+0x10],edx
  405e58:	e8 53 17 00 00       	call   4075b0 <___Bfree_D2A>
  405e5d:	8b 44 24 20          	mov    eax,DWORD PTR [esp+0x20]
  405e61:	85 c0                	test   eax,eax
  405e63:	74 18                	je     405e7d <___gdtoa+0x88d>
  405e65:	8b 54 24 10          	mov    edx,DWORD PTR [esp+0x10]
  405e69:	39 c2                	cmp    edx,eax
  405e6b:	0f 85 dd 03 00 00    	jne    40624e <___gdtoa+0xc5e>
  405e71:	8b 44 24 20          	mov    eax,DWORD PTR [esp+0x20]
  405e75:	89 04 24             	mov    DWORD PTR [esp],eax
  405e78:	e8 33 17 00 00       	call   4075b0 <___Bfree_D2A>
  405e7d:	89 1c 24             	mov    DWORD PTR [esp],ebx
  405e80:	e8 2b 17 00 00       	call   4075b0 <___Bfree_D2A>
  405e85:	8b 84 24 98 00 00 00 	mov    eax,DWORD PTR [esp+0x98]
  405e8c:	8b 7c 24 0c          	mov    edi,DWORD PTR [esp+0xc]
  405e90:	c6 06 00             	mov    BYTE PTR [esi],0x0
  405e93:	89 38                	mov    DWORD PTR [eax],edi
  405e95:	8b 84 24 9c 00 00 00 	mov    eax,DWORD PTR [esp+0x9c]
  405e9c:	85 c0                	test   eax,eax
  405e9e:	74 09                	je     405ea9 <___gdtoa+0x8b9>
  405ea0:	8b 84 24 9c 00 00 00 	mov    eax,DWORD PTR [esp+0x9c]
  405ea7:	89 30                	mov    DWORD PTR [eax],esi
  405ea9:	8b 84 24 8c 00 00 00 	mov    eax,DWORD PTR [esp+0x8c]
  405eb0:	8b 7c 24 18          	mov    edi,DWORD PTR [esp+0x18]
  405eb4:	09 38                	or     DWORD PTR [eax],edi
  405eb6:	8b 44 24 24          	mov    eax,DWORD PTR [esp+0x24]
  405eba:	83 c4 6c             	add    esp,0x6c
  405ebd:	5b                   	pop    ebx
  405ebe:	5e                   	pop    esi
  405ebf:	5f                   	pop    edi
  405ec0:	5d                   	pop    ebp
  405ec1:	c3                   	ret    
  405ec2:	b8 03 00 00 00       	mov    eax,0x3
  405ec7:	2b 44 24 2c          	sub    eax,DWORD PTR [esp+0x2c]
  405ecb:	89 44 24 2c          	mov    DWORD PTR [esp+0x2c],eax
  405ecf:	e9 95 fa ff ff       	jmp    405969 <___gdtoa+0x379>
  405ed4:	c7 44 24 34 00 00 00 	mov    DWORD PTR [esp+0x34],0x0
  405edb:	00 
  405edc:	e9 93 f9 ff ff       	jmp    405874 <___gdtoa+0x284>
  405ee1:	c7 44 24 2c 02 00 00 	mov    DWORD PTR [esp+0x2c],0x2
  405ee8:	00 
  405ee9:	e9 72 fa ff ff       	jmp    405960 <___gdtoa+0x370>
  405eee:	c7 44 24 40 00 00 00 	mov    DWORD PTR [esp+0x40],0x0
  405ef5:	00 
  405ef6:	e9 0c fa ff ff       	jmp    405907 <___gdtoa+0x317>
  405efb:	83 bc 24 90 00 00 00 	cmp    DWORD PTR [esp+0x90],0x2
  405f02:	02 
  405f03:	c7 44 24 40 00 00 00 	mov    DWORD PTR [esp+0x40],0x0
  405f0a:	00 
  405f0b:	0f 85 32 fc ff ff    	jne    405b43 <___gdtoa+0x553>
  405f11:	8b 94 24 94 00 00 00 	mov    edx,DWORD PTR [esp+0x94]
  405f18:	85 d2                	test   edx,edx
  405f1a:	0f 8e d3 04 00 00    	jle    4063f3 <___gdtoa+0xe03>
  405f20:	83 bc 24 94 00 00 00 	cmp    DWORD PTR [esp+0x94],0xe
  405f27:	0e 
  405f28:	0f 96 c2             	setbe  dl
  405f2b:	8b 8c 24 94 00 00 00 	mov    ecx,DWORD PTR [esp+0x94]
  405f32:	21 c2                	and    edx,eax
  405f34:	89 4c 24 5c          	mov    DWORD PTR [esp+0x5c],ecx
  405f38:	89 c8                	mov    eax,ecx
  405f3a:	89 4c 24 44          	mov    DWORD PTR [esp+0x44],ecx
  405f3e:	89 4c 24 18          	mov    DWORD PTR [esp+0x18],ecx
  405f42:	e9 ec f9 ff ff       	jmp    405933 <___gdtoa+0x343>
  405f47:	dd d8                	fstp   st(0)
  405f49:	eb 02                	jmp    405f4d <___gdtoa+0x95d>
  405f4b:	dd d8                	fstp   st(0)
  405f4d:	31 ff                	xor    edi,edi
  405f4f:	c7 44 24 20 00 00 00 	mov    DWORD PTR [esp+0x20],0x0
  405f56:	00 
  405f57:	8b 84 24 94 00 00 00 	mov    eax,DWORD PTR [esp+0x94]
  405f5e:	31 d2                	xor    edx,edx
  405f60:	8b 74 24 24          	mov    esi,DWORD PTR [esp+0x24]
  405f64:	c7 44 24 18 10 00 00 	mov    DWORD PTR [esp+0x18],0x10
  405f6b:	00 
  405f6c:	f7 d8                	neg    eax
  405f6e:	89 44 24 0c          	mov    DWORD PTR [esp+0xc],eax
  405f72:	e9 da fe ff ff       	jmp    405e51 <___gdtoa+0x861>
  405f77:	8b 44 24 0c          	mov    eax,DWORD PTR [esp+0xc]
  405f7b:	29 44 24 28          	sub    DWORD PTR [esp+0x28],eax
  405f7f:	c7 44 24 3c 00 00 00 	mov    DWORD PTR [esp+0x3c],0x0
  405f86:	00 
  405f87:	f7 d8                	neg    eax
  405f89:	89 44 24 30          	mov    DWORD PTR [esp+0x30],eax
  405f8d:	e9 17 f9 ff ff       	jmp    4058a9 <___gdtoa+0x2b9>
  405f92:	f7 d8                	neg    eax
  405f94:	89 44 24 28          	mov    DWORD PTR [esp+0x28],eax
  405f98:	c7 44 24 1c 00 00 00 	mov    DWORD PTR [esp+0x1c],0x0
  405f9f:	00 
  405fa0:	e9 e8 f8 ff ff       	jmp    40588d <___gdtoa+0x29d>
  405fa5:	db 44 24 0c          	fild   DWORD PTR [esp+0xc]
  405fa9:	da e9                	fucompp 
  405fab:	df e0                	fnstsw ax
  405fad:	9e                   	sahf   
  405fae:	7a 06                	jp     405fb6 <___gdtoa+0x9c6>
  405fb0:	0f 84 7b f8 ff ff    	je     405831 <___gdtoa+0x241>
  405fb6:	83 6c 24 0c 01       	sub    DWORD PTR [esp+0xc],0x1
  405fbb:	e9 71 f8 ff ff       	jmp    405831 <___gdtoa+0x241>
  405fc0:	8b 7c 24 30          	mov    edi,DWORD PTR [esp+0x30]
  405fc4:	8b 74 24 28          	mov    esi,DWORD PTR [esp+0x28]
  405fc8:	c7 44 24 20 00 00 00 	mov    DWORD PTR [esp+0x20],0x0
  405fcf:	00 
  405fd0:	e9 79 fc ff ff       	jmp    405c4e <___gdtoa+0x65e>
  405fd5:	dd 44 24 10          	fld    QWORD PTR [esp+0x10]
  405fd9:	d9 c0                	fld    st(0)
  405fdb:	8b 7c 24 24          	mov    edi,DWORD PTR [esp+0x24]
  405fdf:	d8 f2                	fdiv   st,st(2)
  405fe1:	d9 7c 24 4e          	fnstcw WORD PTR [esp+0x4e]
  405fe5:	c7 44 24 5c 01 00 00 	mov    DWORD PTR [esp+0x5c],0x1
  405fec:	00 
  405fed:	8d 77 01             	lea    esi,[edi+0x1]
  405ff0:	0f b7 44 24 4e       	movzx  eax,WORD PTR [esp+0x4e]
  405ff5:	b4 0c                	mov    ah,0xc
  405ff7:	66 89 44 24 4c       	mov    WORD PTR [esp+0x4c],ax
  405ffc:	d9 6c 24 4c          	fldcw  WORD PTR [esp+0x4c]
  406000:	db 5c 24 48          	fistp  DWORD PTR [esp+0x48]
  406004:	d9 6c 24 4e          	fldcw  WORD PTR [esp+0x4e]
  406008:	8b 4c 24 48          	mov    ecx,DWORD PTR [esp+0x48]
  40600c:	89 4c 24 48          	mov    DWORD PTR [esp+0x48],ecx
  406010:	8d 41 30             	lea    eax,[ecx+0x30]
  406013:	db 44 24 48          	fild   DWORD PTR [esp+0x48]
  406017:	d8 ca                	fmul   st,st(2)
  406019:	88 07                	mov    BYTE PTR [edi],al
  40601b:	de e9                	fsubrp st(1),st
  40601d:	d9 ee                	fldz   
  40601f:	d9 c9                	fxch   st(1)
  406021:	dd e1                	fucom  st(1)
  406023:	df e0                	fnstsw ax
  406025:	dd d9                	fstp   st(1)
  406027:	9e                   	sahf   
  406028:	0f 8b 52 09 00 00    	jnp    406980 <___gdtoa+0x1390>
  40602e:	8b 44 24 5c          	mov    eax,DWORD PTR [esp+0x5c]
  406032:	39 44 24 18          	cmp    DWORD PTR [esp+0x18],eax
  406036:	0f 84 93 03 00 00    	je     4063cf <___gdtoa+0xddf>
  40603c:	d9 05 44 a3 40 00    	fld    DWORD PTR ds:0x40a344
  406042:	8b 54 24 18          	mov    edx,DWORD PTR [esp+0x18]
  406046:	eb 0c                	jmp    406054 <___gdtoa+0xa64>
  406048:	8b 44 24 5c          	mov    eax,DWORD PTR [esp+0x5c]
  40604c:	39 c2                	cmp    edx,eax
  40604e:	0f 84 79 03 00 00    	je     4063cd <___gdtoa+0xddd>
  406054:	83 c0 01             	add    eax,0x1
  406057:	dc c9                	fmul   st(1),st
  406059:	83 c6 01             	add    esi,0x1
  40605c:	89 44 24 5c          	mov    DWORD PTR [esp+0x5c],eax
  406060:	d9 c1                	fld    st(1)
  406062:	d8 f3                	fdiv   st,st(3)
  406064:	d9 6c 24 4c          	fldcw  WORD PTR [esp+0x4c]
  406068:	db 5c 24 48          	fistp  DWORD PTR [esp+0x48]
  40606c:	d9 6c 24 4e          	fldcw  WORD PTR [esp+0x4e]
  406070:	8b 4c 24 48          	mov    ecx,DWORD PTR [esp+0x48]
  406074:	89 4c 24 48          	mov    DWORD PTR [esp+0x48],ecx
  406078:	8d 41 30             	lea    eax,[ecx+0x30]
  40607b:	db 44 24 48          	fild   DWORD PTR [esp+0x48]
  40607f:	d8 cb                	fmul   st,st(3)
  406081:	88 46 ff             	mov    BYTE PTR [esi-0x1],al
  406084:	de ea                	fsubrp st(2),st
  406086:	d9 ee                	fldz   
  406088:	d9 ca                	fxch   st(2)
  40608a:	dd e2                	fucom  st(2)
  40608c:	df e0                	fnstsw ax
  40608e:	dd da                	fstp   st(2)
  406090:	9e                   	sahf   
  406091:	7a b5                	jp     406048 <___gdtoa+0xa58>
  406093:	75 b3                	jne    406048 <___gdtoa+0xa58>
  406095:	dd d8                	fstp   st(0)
  406097:	dd d8                	fstp   st(0)
  406099:	dd d8                	fstp   st(0)
  40609b:	8b 44 24 0c          	mov    eax,DWORD PTR [esp+0xc]
  40609f:	83 c0 01             	add    eax,0x1
  4060a2:	89 44 24 0c          	mov    DWORD PTR [esp+0xc],eax
  4060a6:	c7 44 24 18 00 00 00 	mov    DWORD PTR [esp+0x18],0x0
  4060ad:	00 
  4060ae:	e9 ca fd ff ff       	jmp    405e7d <___gdtoa+0x88d>
  4060b3:	8b 44 24 40          	mov    eax,DWORD PTR [esp+0x40]
  4060b7:	85 c0                	test   eax,eax
  4060b9:	0f 84 19 02 00 00    	je     4062d8 <___gdtoa+0xce8>
  4060bf:	8d 04 2e             	lea    eax,[esi+ebp*1]
  4060c2:	85 c0                	test   eax,eax
  4060c4:	7e 14                	jle    4060da <___gdtoa+0xaea>
  4060c6:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
  4060ca:	8b 44 24 20          	mov    eax,DWORD PTR [esp+0x20]
  4060ce:	89 04 24             	mov    DWORD PTR [esp],eax
  4060d1:	e8 4a 19 00 00       	call   407a20 <___lshift_D2A>
  4060d6:	89 44 24 20          	mov    DWORD PTR [esp+0x20],eax
  4060da:	8b 74 24 10          	mov    esi,DWORD PTR [esp+0x10]
  4060de:	8b 6c 24 20          	mov    ebp,DWORD PTR [esp+0x20]
  4060e2:	85 f6                	test   esi,esi
  4060e4:	0f 85 e9 06 00 00    	jne    4067d3 <___gdtoa+0x11e3>
  4060ea:	8b 74 24 24          	mov    esi,DWORD PTR [esp+0x24]
  4060ee:	89 7c 24 1c          	mov    DWORD PTR [esp+0x1c],edi
  4060f2:	8b 7c 24 20          	mov    edi,DWORD PTR [esp+0x20]
  4060f6:	c7 44 24 5c 01 00 00 	mov    DWORD PTR [esp+0x5c],0x1
  4060fd:	00 
  4060fe:	89 74 24 28          	mov    DWORD PTR [esp+0x28],esi
  406102:	e9 d6 00 00 00       	jmp    4061dd <___gdtoa+0xbed>
  406107:	89 14 24             	mov    DWORD PTR [esp],edx
  40610a:	89 44 24 20          	mov    DWORD PTR [esp+0x20],eax
  40610e:	e8 9d 14 00 00       	call   4075b0 <___Bfree_D2A>
  406113:	8b 44 24 20          	mov    eax,DWORD PTR [esp+0x20]
  406117:	89 c1                	mov    ecx,eax
  406119:	0b 8c 24 90 00 00 00 	or     ecx,DWORD PTR [esp+0x90]
  406120:	75 18                	jne    40613a <___gdtoa+0xb4a>
  406122:	8b 8c 24 88 00 00 00 	mov    ecx,DWORD PTR [esp+0x88]
  406129:	f6 01 01             	test   BYTE PTR [ecx],0x1
  40612c:	75 0c                	jne    40613a <___gdtoa+0xb4a>
  40612e:	8b 54 24 2c          	mov    edx,DWORD PTR [esp+0x2c]
  406132:	85 d2                	test   edx,edx
  406134:	0f 84 55 08 00 00    	je     40698f <___gdtoa+0x139f>
  40613a:	85 f6                	test   esi,esi
  40613c:	0f 88 18 05 00 00    	js     40665a <___gdtoa+0x106a>
  406142:	0b b4 24 90 00 00 00 	or     esi,DWORD PTR [esp+0x90]
  406149:	75 10                	jne    40615b <___gdtoa+0xb6b>
  40614b:	8b b4 24 88 00 00 00 	mov    esi,DWORD PTR [esp+0x88]
  406152:	f6 06 01             	test   BYTE PTR [esi],0x1
  406155:	0f 84 ff 04 00 00    	je     40665a <___gdtoa+0x106a>
  40615b:	85 c0                	test   eax,eax
  40615d:	0f 8f c9 06 00 00    	jg     40682c <___gdtoa+0x123c>
  406163:	83 44 24 28 01       	add    DWORD PTR [esp+0x28],0x1
  406168:	0f b6 44 24 10       	movzx  eax,BYTE PTR [esp+0x10]
  40616d:	8b 74 24 28          	mov    esi,DWORD PTR [esp+0x28]
  406171:	88 46 ff             	mov    BYTE PTR [esi-0x1],al
  406174:	8b 44 24 18          	mov    eax,DWORD PTR [esp+0x18]
  406178:	39 44 24 5c          	cmp    DWORD PTR [esp+0x5c],eax
  40617c:	0f 84 97 06 00 00    	je     406819 <___gdtoa+0x1229>
  406182:	89 1c 24             	mov    DWORD PTR [esp],ebx
  406185:	c7 44 24 08 00 00 00 	mov    DWORD PTR [esp+0x8],0x0
  40618c:	00 
  40618d:	c7 44 24 04 0a 00 00 	mov    DWORD PTR [esp+0x4],0xa
  406194:	00 
  406195:	e8 86 14 00 00       	call   407620 <___multadd_D2A>
  40619a:	39 ef                	cmp    edi,ebp
  40619c:	c7 44 24 08 00 00 00 	mov    DWORD PTR [esp+0x8],0x0
  4061a3:	00 
  4061a4:	c7 44 24 04 0a 00 00 	mov    DWORD PTR [esp+0x4],0xa
  4061ab:	00 
  4061ac:	89 3c 24             	mov    DWORD PTR [esp],edi
  4061af:	89 c3                	mov    ebx,eax
  4061b1:	0f 84 8c 00 00 00    	je     406243 <___gdtoa+0xc53>
  4061b7:	e8 64 14 00 00       	call   407620 <___multadd_D2A>
  4061bc:	89 2c 24             	mov    DWORD PTR [esp],ebp
  4061bf:	c7 44 24 08 00 00 00 	mov    DWORD PTR [esp+0x8],0x0
  4061c6:	00 
  4061c7:	c7 44 24 04 0a 00 00 	mov    DWORD PTR [esp+0x4],0xa
  4061ce:	00 
  4061cf:	89 c7                	mov    edi,eax
  4061d1:	e8 4a 14 00 00       	call   407620 <___multadd_D2A>
  4061d6:	89 c5                	mov    ebp,eax
  4061d8:	83 44 24 5c 01       	add    DWORD PTR [esp+0x5c],0x1
  4061dd:	8b 44 24 1c          	mov    eax,DWORD PTR [esp+0x1c]
  4061e1:	89 1c 24             	mov    DWORD PTR [esp],ebx
  4061e4:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
  4061e8:	e8 d3 0f 00 00       	call   4071c0 <___quorem_D2A>
  4061ed:	89 7c 24 04          	mov    DWORD PTR [esp+0x4],edi
  4061f1:	89 1c 24             	mov    DWORD PTR [esp],ebx
  4061f4:	89 c6                	mov    esi,eax
  4061f6:	83 c6 30             	add    esi,0x30
  4061f9:	89 74 24 10          	mov    DWORD PTR [esp+0x10],esi
  4061fd:	89 44 24 30          	mov    DWORD PTR [esp+0x30],eax
  406201:	e8 2a 19 00 00       	call   407b30 <___cmp_D2A>
  406206:	89 6c 24 04          	mov    DWORD PTR [esp+0x4],ebp
  40620a:	89 c6                	mov    esi,eax
  40620c:	8b 44 24 1c          	mov    eax,DWORD PTR [esp+0x1c]
  406210:	89 04 24             	mov    DWORD PTR [esp],eax
  406213:	e8 68 19 00 00       	call   407b80 <___diff_D2A>
  406218:	89 c2                	mov    edx,eax
  40621a:	b8 01 00 00 00       	mov    eax,0x1
  40621f:	8b 4a 0c             	mov    ecx,DWORD PTR [edx+0xc]
  406222:	85 c9                	test   ecx,ecx
  406224:	0f 85 dd fe ff ff    	jne    406107 <___gdtoa+0xb17>
  40622a:	89 54 24 04          	mov    DWORD PTR [esp+0x4],edx
  40622e:	89 1c 24             	mov    DWORD PTR [esp],ebx
  406231:	89 54 24 20          	mov    DWORD PTR [esp+0x20],edx
  406235:	e8 f6 18 00 00       	call   407b30 <___cmp_D2A>
  40623a:	8b 54 24 20          	mov    edx,DWORD PTR [esp+0x20]
  40623e:	e9 c4 fe ff ff       	jmp    406107 <___gdtoa+0xb17>
  406243:	e8 d8 13 00 00       	call   407620 <___multadd_D2A>
  406248:	89 c7                	mov    edi,eax
  40624a:	89 c5                	mov    ebp,eax
  40624c:	eb 8a                	jmp    4061d8 <___gdtoa+0xbe8>
  40624e:	85 d2                	test   edx,edx
  406250:	0f 84 1b fc ff ff    	je     405e71 <___gdtoa+0x881>
  406256:	89 14 24             	mov    DWORD PTR [esp],edx
  406259:	e8 52 13 00 00       	call   4075b0 <___Bfree_D2A>
  40625e:	66 90                	xchg   ax,ax
  406260:	e9 0c fc ff ff       	jmp    405e71 <___gdtoa+0x881>
  406265:	8b 44 24 30          	mov    eax,DWORD PTR [esp+0x30]
  406269:	89 1c 24             	mov    DWORD PTR [esp],ebx
  40626c:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
  406270:	e8 1b 16 00 00       	call   407890 <___pow5mult_D2A>
  406275:	89 c3                	mov    ebx,eax
  406277:	e9 4e fa ff ff       	jmp    405cca <___gdtoa+0x6da>
  40627c:	89 7c 24 04          	mov    DWORD PTR [esp+0x4],edi
  406280:	89 1c 24             	mov    DWORD PTR [esp],ebx
  406283:	e8 a8 18 00 00       	call   407b30 <___cmp_D2A>
  406288:	85 c0                	test   eax,eax
  40628a:	0f 89 da fa ff ff    	jns    405d6a <___gdtoa+0x77a>
  406290:	89 1c 24             	mov    DWORD PTR [esp],ebx
  406293:	c7 44 24 08 00 00 00 	mov    DWORD PTR [esp+0x8],0x0
  40629a:	00 
  40629b:	c7 44 24 04 0a 00 00 	mov    DWORD PTR [esp+0x4],0xa
  4062a2:	00 
  4062a3:	83 6c 24 0c 01       	sub    DWORD PTR [esp+0xc],0x1
  4062a8:	e8 73 13 00 00       	call   407620 <___multadd_D2A>
  4062ad:	89 c3                	mov    ebx,eax
  4062af:	8b 44 24 40          	mov    eax,DWORD PTR [esp+0x40]
  4062b3:	85 c0                	test   eax,eax
  4062b5:	0f 85 24 07 00 00    	jne    4069df <___gdtoa+0x13ef>
  4062bb:	83 bc 24 90 00 00 00 	cmp    DWORD PTR [esp+0x90],0x2
  4062c2:	02 
  4062c3:	8b 44 24 44          	mov    eax,DWORD PTR [esp+0x44]
  4062c7:	7e 0b                	jle    4062d4 <___gdtoa+0xce4>
  4062c9:	83 7c 24 44 00       	cmp    DWORD PTR [esp+0x44],0x0
  4062ce:	0f 8e 86 07 00 00    	jle    406a5a <___gdtoa+0x146a>
  4062d4:	89 44 24 18          	mov    DWORD PTR [esp+0x18],eax
  4062d8:	c7 44 24 5c 01 00 00 	mov    DWORD PTR [esp+0x5c],0x1
  4062df:	00 
  4062e0:	8b 74 24 24          	mov    esi,DWORD PTR [esp+0x24]
  4062e4:	8b 6c 24 18          	mov    ebp,DWORD PTR [esp+0x18]
  4062e8:	eb 25                	jmp    40630f <___gdtoa+0xd1f>
  4062ea:	8d b6 00 00 00 00    	lea    esi,[esi+0x0]
  4062f0:	89 1c 24             	mov    DWORD PTR [esp],ebx
  4062f3:	c7 44 24 08 00 00 00 	mov    DWORD PTR [esp+0x8],0x0
  4062fa:	00 
  4062fb:	c7 44 24 04 0a 00 00 	mov    DWORD PTR [esp+0x4],0xa
  406302:	00 
  406303:	e8 18 13 00 00       	call   407620 <___multadd_D2A>
  406308:	83 44 24 5c 01       	add    DWORD PTR [esp+0x5c],0x1
  40630d:	89 c3                	mov    ebx,eax
  40630f:	89 7c 24 04          	mov    DWORD PTR [esp+0x4],edi
  406313:	83 c6 01             	add    esi,0x1
  406316:	89 1c 24             	mov    DWORD PTR [esp],ebx
  406319:	e8 a2 0e 00 00       	call   4071c0 <___quorem_D2A>
  40631e:	83 c0 30             	add    eax,0x30
  406321:	88 46 ff             	mov    BYTE PTR [esi-0x1],al
  406324:	3b 6c 24 5c          	cmp    ebp,DWORD PTR [esp+0x5c]
  406328:	7f c6                	jg     4062f0 <___gdtoa+0xd00>
  40632a:	89 44 24 10          	mov    DWORD PTR [esp+0x10],eax
  40632e:	31 d2                	xor    edx,edx
  406330:	8b 44 24 2c          	mov    eax,DWORD PTR [esp+0x2c]
  406334:	85 c0                	test   eax,eax
  406336:	0f 84 e5 03 00 00    	je     406721 <___gdtoa+0x1131>
  40633c:	83 f8 02             	cmp    eax,0x2
  40633f:	0f 84 18 04 00 00    	je     40675d <___gdtoa+0x116d>
  406345:	83 7b 10 01          	cmp    DWORD PTR [ebx+0x10],0x1
  406349:	0f 8e cb 05 00 00    	jle    40691a <___gdtoa+0x132a>
  40634f:	0f b6 4e ff          	movzx  ecx,BYTE PTR [esi-0x1]
  406353:	8b 6c 24 24          	mov    ebp,DWORD PTR [esp+0x24]
  406357:	eb 15                	jmp    40636e <___gdtoa+0xd7e>
  406359:	8d b4 26 00 00 00 00 	lea    esi,[esi+eiz*1+0x0]
  406360:	39 e8                	cmp    eax,ebp
  406362:	0f 84 a6 02 00 00    	je     40660e <___gdtoa+0x101e>
  406368:	0f b6 48 ff          	movzx  ecx,BYTE PTR [eax-0x1]
  40636c:	89 c6                	mov    esi,eax
  40636e:	80 f9 39             	cmp    cl,0x39
  406371:	8d 46 ff             	lea    eax,[esi-0x1]
  406374:	74 ea                	je     406360 <___gdtoa+0xd70>
  406376:	83 c1 01             	add    ecx,0x1
  406379:	88 08                	mov    BYTE PTR [eax],cl
  40637b:	8b 44 24 0c          	mov    eax,DWORD PTR [esp+0xc]
  40637f:	c7 44 24 18 20 00 00 	mov    DWORD PTR [esp+0x18],0x20
  406386:	00 
  406387:	83 c0 01             	add    eax,0x1
  40638a:	89 44 24 0c          	mov    DWORD PTR [esp+0xc],eax
  40638e:	e9 be fa ff ff       	jmp    405e51 <___gdtoa+0x861>
  406393:	83 fd 01             	cmp    ebp,0x1
  406396:	0f 85 68 f9 ff ff    	jne    405d04 <___gdtoa+0x714>
  40639c:	8b 84 24 80 00 00 00 	mov    eax,DWORD PTR [esp+0x80]
  4063a3:	8b 40 04             	mov    eax,DWORD PTR [eax+0x4]
  4063a6:	83 c0 01             	add    eax,0x1
  4063a9:	39 84 24 84 00 00 00 	cmp    DWORD PTR [esp+0x84],eax
  4063b0:	0f 8e 4e f9 ff ff    	jle    405d04 <___gdtoa+0x714>
  4063b6:	83 44 24 28 01       	add    DWORD PTR [esp+0x28],0x1
  4063bb:	83 44 24 1c 01       	add    DWORD PTR [esp+0x1c],0x1
  4063c0:	c7 44 24 10 01 00 00 	mov    DWORD PTR [esp+0x10],0x1
  4063c7:	00 
  4063c8:	e9 37 f9 ff ff       	jmp    405d04 <___gdtoa+0x714>
  4063cd:	dd d8                	fstp   st(0)
  4063cf:	8b 44 24 2c          	mov    eax,DWORD PTR [esp+0x2c]
  4063d3:	85 c0                	test   eax,eax
  4063d5:	0f 84 fe 01 00 00    	je     4065d9 <___gdtoa+0xfe9>
  4063db:	dd d8                	fstp   st(0)
  4063dd:	dd d8                	fstp   st(0)
  4063df:	83 7c 24 2c 01       	cmp    DWORD PTR [esp+0x2c],0x1
  4063e4:	0f 84 22 03 00 00    	je     40670c <___gdtoa+0x111c>
  4063ea:	8b 44 24 0c          	mov    eax,DWORD PTR [esp+0xc]
  4063ee:	e9 ff f6 ff ff       	jmp    405af2 <___gdtoa+0x502>
  4063f3:	ba 01 00 00 00       	mov    edx,0x1
  4063f8:	c7 84 24 94 00 00 00 	mov    DWORD PTR [esp+0x94],0x1
  4063ff:	01 00 00 00 
  406403:	e9 23 fb ff ff       	jmp    405f2b <___gdtoa+0x93b>
  406408:	83 7c 24 18 0e       	cmp    DWORD PTR [esp+0x18],0xe
  40640d:	c7 44 24 5c 01 00 00 	mov    DWORD PTR [esp+0x5c],0x1
  406414:	00 
  406415:	0f 96 c2             	setbe  dl
  406418:	21 c2                	and    edx,eax
  40641a:	b8 01 00 00 00       	mov    eax,0x1
  40641f:	e9 0f f5 ff ff       	jmp    405933 <___gdtoa+0x343>
  406424:	89 c2                	mov    edx,eax
  406426:	31 ff                	xor    edi,edi
  406428:	2b 54 24 30          	sub    edx,DWORD PTR [esp+0x30]
  40642c:	89 44 24 30          	mov    DWORD PTR [esp+0x30],eax
  406430:	01 54 24 3c          	add    DWORD PTR [esp+0x3c],edx
  406434:	e9 e9 f7 ff ff       	jmp    405c22 <___gdtoa+0x632>
  406439:	d9 7c 24 4e          	fnstcw WORD PTR [esp+0x4e]
  40643d:	dd 44 24 10          	fld    QWORD PTR [esp+0x10]
  406441:	dc 0c d5 78 a3 40 00 	fmul   QWORD PTR [edx*8+0x40a378]
  406448:	c7 44 24 5c 01 00 00 	mov    DWORD PTR [esp+0x5c],0x1
  40644f:	00 
  406450:	8b 74 24 24          	mov    esi,DWORD PTR [esp+0x24]
  406454:	0f b7 44 24 4e       	movzx  eax,WORD PTR [esp+0x4e]
  406459:	b4 0c                	mov    ah,0xc
  40645b:	d9 05 44 a3 40 00    	fld    DWORD PTR ds:0x40a344
  406461:	d9 ca                	fxch   st(2)
  406463:	66 89 44 24 4c       	mov    WORD PTR [esp+0x4c],ax
  406468:	eb 0f                	jmp    406479 <___gdtoa+0xe89>
  40646a:	8d b6 00 00 00 00    	lea    esi,[esi+0x0]
  406470:	d8 ca                	fmul   st,st(2)
  406472:	83 c0 01             	add    eax,0x1
  406475:	89 44 24 5c          	mov    DWORD PTR [esp+0x5c],eax
  406479:	d9 6c 24 4c          	fldcw  WORD PTR [esp+0x4c]
  40647d:	db 54 24 48          	fist   DWORD PTR [esp+0x48]
  406481:	d9 6c 24 4e          	fldcw  WORD PTR [esp+0x4e]
  406485:	8b 44 24 48          	mov    eax,DWORD PTR [esp+0x48]
  406489:	85 c0                	test   eax,eax
  40648b:	74 0a                	je     406497 <___gdtoa+0xea7>
  40648d:	89 44 24 48          	mov    DWORD PTR [esp+0x48],eax
  406491:	db 44 24 48          	fild   DWORD PTR [esp+0x48]
  406495:	de e9                	fsubrp st(1),st
  406497:	83 c6 01             	add    esi,0x1
  40649a:	8d 48 30             	lea    ecx,[eax+0x30]
  40649d:	88 4e ff             	mov    BYTE PTR [esi-0x1],cl
  4064a0:	8b 44 24 5c          	mov    eax,DWORD PTR [esp+0x5c]
  4064a4:	39 d0                	cmp    eax,edx
  4064a6:	75 c8                	jne    406470 <___gdtoa+0xe80>
  4064a8:	dd da                	fstp   st(2)
  4064aa:	d9 c9                	fxch   st(1)
  4064ac:	d9 05 54 a3 40 00    	fld    DWORD PTR ds:0x40a354
  4064b2:	d9 c2                	fld    st(2)
  4064b4:	d8 c1                	fadd   st,st(1)
  4064b6:	d9 ca                	fxch   st(2)
  4064b8:	dd e2                	fucom  st(2)
  4064ba:	df e0                	fnstsw ax
  4064bc:	dd da                	fstp   st(2)
  4064be:	9e                   	sahf   
  4064bf:	0f 87 94 00 00 00    	ja     406559 <___gdtoa+0xf69>
  4064c5:	de e2                	fsubp  st(2),st
  4064c7:	d9 c9                	fxch   st(1)
  4064c9:	dd e9                	fucomp st(1)
  4064cb:	df e0                	fnstsw ax
  4064cd:	9e                   	sahf   
  4064ce:	0f 86 0c f7 ff ff    	jbe    405be0 <___gdtoa+0x5f0>
  4064d4:	dd d9                	fstp   st(1)
  4064d6:	d9 ee                	fldz   
  4064d8:	d9 c9                	fxch   st(1)
  4064da:	da e9                	fucompp 
  4064dc:	df e0                	fnstsw ax
  4064de:	9e                   	sahf   
  4064df:	0f 8a 4d 04 00 00    	jp     406932 <___gdtoa+0x1342>
  4064e5:	0f 85 47 04 00 00    	jne    406932 <___gdtoa+0x1342>
  4064eb:	c7 44 24 18 00 00 00 	mov    DWORD PTR [esp+0x18],0x0
  4064f2:	00 
  4064f3:	eb 06                	jmp    4064fb <___gdtoa+0xf0b>
  4064f5:	0f b6 48 ff          	movzx  ecx,BYTE PTR [eax-0x1]
  4064f9:	89 c6                	mov    esi,eax
  4064fb:	80 f9 30             	cmp    cl,0x30
  4064fe:	8d 46 ff             	lea    eax,[esi-0x1]
  406501:	74 f2                	je     4064f5 <___gdtoa+0xf05>
  406503:	8b 44 24 38          	mov    eax,DWORD PTR [esp+0x38]
  406507:	83 c0 01             	add    eax,0x1
  40650a:	89 44 24 0c          	mov    DWORD PTR [esp+0xc],eax
  40650e:	e9 6a f9 ff ff       	jmp    405e7d <___gdtoa+0x88d>
  406513:	dd d8                	fstp   st(0)
  406515:	dd d8                	fstp   st(0)
  406517:	dd d8                	fstp   st(0)
  406519:	c7 44 24 0c 02 00 00 	mov    DWORD PTR [esp+0xc],0x2
  406520:	00 
  406521:	31 ff                	xor    edi,edi
  406523:	c7 44 24 20 00 00 00 	mov    DWORD PTR [esp+0x20],0x0
  40652a:	00 
  40652b:	e9 0d f9 ff ff       	jmp    405e3d <___gdtoa+0x84d>
  406530:	8b 44 24 0c          	mov    eax,DWORD PTR [esp+0xc]
  406534:	83 e1 01             	and    ecx,0x1
  406537:	0f b6 4e ff          	movzx  ecx,BYTE PTR [esi-0x1]
  40653b:	89 44 24 38          	mov    DWORD PTR [esp+0x38],eax
  40653f:	0f 84 ed 03 00 00    	je     406932 <___gdtoa+0x1342>
  406545:	eb 1a                	jmp    406561 <___gdtoa+0xf71>
  406547:	dd d8                	fstp   st(0)
  406549:	dd d8                	fstp   st(0)
  40654b:	dd d8                	fstp   st(0)
  40654d:	eb 12                	jmp    406561 <___gdtoa+0xf71>
  40654f:	dd d8                	fstp   st(0)
  406551:	dd d8                	fstp   st(0)
  406553:	dd d8                	fstp   st(0)
  406555:	dd d8                	fstp   st(0)
  406557:	eb 08                	jmp    406561 <___gdtoa+0xf71>
  406559:	dd d8                	fstp   st(0)
  40655b:	dd d8                	fstp   st(0)
  40655d:	dd d8                	fstp   st(0)
  40655f:	dd d8                	fstp   st(0)
  406561:	8b 54 24 24          	mov    edx,DWORD PTR [esp+0x24]
  406565:	eb 0e                	jmp    406575 <___gdtoa+0xf85>
  406567:	39 d0                	cmp    eax,edx
  406569:	0f 84 be 00 00 00    	je     40662d <___gdtoa+0x103d>
  40656f:	0f b6 48 ff          	movzx  ecx,BYTE PTR [eax-0x1]
  406573:	89 c6                	mov    esi,eax
  406575:	80 f9 39             	cmp    cl,0x39
  406578:	8d 46 ff             	lea    eax,[esi-0x1]
  40657b:	74 ea                	je     406567 <___gdtoa+0xf77>
  40657d:	89 54 24 24          	mov    DWORD PTR [esp+0x24],edx
  406581:	83 c1 01             	add    ecx,0x1
  406584:	88 08                	mov    BYTE PTR [eax],cl
  406586:	8b 44 24 38          	mov    eax,DWORD PTR [esp+0x38]
  40658a:	c7 44 24 18 20 00 00 	mov    DWORD PTR [esp+0x18],0x20
  406591:	00 
  406592:	83 c0 01             	add    eax,0x1
  406595:	89 44 24 0c          	mov    DWORD PTR [esp+0xc],eax
  406599:	e9 df f8 ff ff       	jmp    405e7d <___gdtoa+0x88d>
  40659e:	8b b4 24 80 00 00 00 	mov    esi,DWORD PTR [esp+0x80]
  4065a5:	29 ef                	sub    edi,ebp
  4065a7:	8b 54 24 20          	mov    edx,DWORD PTR [esp+0x20]
  4065ab:	8d 47 01             	lea    eax,[edi+0x1]
  4065ae:	89 44 24 5c          	mov    DWORD PTR [esp+0x5c],eax
  4065b2:	8b 4e 04             	mov    ecx,DWORD PTR [esi+0x4]
  4065b5:	29 fa                	sub    edx,edi
  4065b7:	39 ca                	cmp    edx,ecx
  4065b9:	0f 8d be 02 00 00    	jge    40687d <___gdtoa+0x128d>
  4065bf:	8b 44 24 20          	mov    eax,DWORD PTR [esp+0x20]
  4065c3:	8b 7c 24 30          	mov    edi,DWORD PTR [esp+0x30]
  4065c7:	8b 74 24 28          	mov    esi,DWORD PTR [esp+0x28]
  4065cb:	29 c8                	sub    eax,ecx
  4065cd:	83 c0 01             	add    eax,0x1
  4065d0:	89 44 24 5c          	mov    DWORD PTR [esp+0x5c],eax
  4065d4:	e9 5d f6 ff ff       	jmp    405c36 <___gdtoa+0x646>
  4065d9:	d8 c0                	fadd   st,st(0)
  4065db:	dd e1                	fucom  st(1)
  4065dd:	df e0                	fnstsw ax
  4065df:	9e                   	sahf   
  4065e0:	0f 87 22 01 00 00    	ja     406708 <___gdtoa+0x1118>
  4065e6:	d9 c9                	fxch   st(1)
  4065e8:	da e9                	fucompp 
  4065ea:	df e0                	fnstsw ax
  4065ec:	9e                   	sahf   
  4065ed:	7a 06                	jp     4065f5 <___gdtoa+0x1005>
  4065ef:	0f 84 3b ff ff ff    	je     406530 <___gdtoa+0xf40>
  4065f5:	8b 44 24 0c          	mov    eax,DWORD PTR [esp+0xc]
  4065f9:	0f b6 4e ff          	movzx  ecx,BYTE PTR [esi-0x1]
  4065fd:	c7 44 24 18 10 00 00 	mov    DWORD PTR [esp+0x18],0x10
  406604:	00 
  406605:	89 44 24 38          	mov    DWORD PTR [esp+0x38],eax
  406609:	e9 ed fe ff ff       	jmp    4064fb <___gdtoa+0xf0b>
  40660e:	8b 44 24 24          	mov    eax,DWORD PTR [esp+0x24]
  406612:	c7 44 24 18 20 00 00 	mov    DWORD PTR [esp+0x18],0x20
  406619:	00 
  40661a:	c6 00 31             	mov    BYTE PTR [eax],0x31
  40661d:	8b 44 24 0c          	mov    eax,DWORD PTR [esp+0xc]
  406621:	83 c0 02             	add    eax,0x2
  406624:	89 44 24 0c          	mov    DWORD PTR [esp+0xc],eax
  406628:	e9 24 f8 ff ff       	jmp    405e51 <___gdtoa+0x861>
  40662d:	89 54 24 24          	mov    DWORD PTR [esp+0x24],edx
  406631:	b9 31 00 00 00       	mov    ecx,0x31
  406636:	83 44 24 38 01       	add    DWORD PTR [esp+0x38],0x1
  40663b:	c6 02 30             	mov    BYTE PTR [edx],0x30
  40663e:	e9 41 ff ff ff       	jmp    406584 <___gdtoa+0xf94>
  406643:	8b 74 24 28          	mov    esi,DWORD PTR [esp+0x28]
  406647:	31 c0                	xor    eax,eax
  406649:	2b 74 24 18          	sub    esi,DWORD PTR [esp+0x18]
  40664d:	c7 44 24 5c 00 00 00 	mov    DWORD PTR [esp+0x5c],0x0
  406654:	00 
  406655:	e9 dc f5 ff ff       	jmp    405c36 <___gdtoa+0x646>
  40665a:	8b 4c 24 2c          	mov    ecx,DWORD PTR [esp+0x2c]
  40665e:	89 7c 24 20          	mov    DWORD PTR [esp+0x20],edi
  406662:	8b 74 24 28          	mov    esi,DWORD PTR [esp+0x28]
  406666:	8b 7c 24 1c          	mov    edi,DWORD PTR [esp+0x1c]
  40666a:	8b 54 24 10          	mov    edx,DWORD PTR [esp+0x10]
  40666e:	85 c9                	test   ecx,ecx
  406670:	0f 84 1e 02 00 00    	je     406894 <___gdtoa+0x12a4>
  406676:	83 7b 10 01          	cmp    DWORD PTR [ebx+0x10],0x1
  40667a:	0f 8e 0a 02 00 00    	jle    40688a <___gdtoa+0x129a>
  406680:	83 7c 24 2c 02       	cmp    DWORD PTR [esp+0x2c],0x2
  406685:	75 3a                	jne    4066c1 <___gdtoa+0x10d1>
  406687:	e9 63 02 00 00       	jmp    4068ef <___gdtoa+0x12ff>
  40668c:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  406690:	89 1c 24             	mov    DWORD PTR [esp],ebx
  406693:	c7 44 24 08 00 00 00 	mov    DWORD PTR [esp+0x8],0x0
  40669a:	00 
  40669b:	c7 44 24 04 0a 00 00 	mov    DWORD PTR [esp+0x4],0xa
  4066a2:	00 
  4066a3:	e8 78 0f 00 00       	call   407620 <___multadd_D2A>
  4066a8:	89 7c 24 04          	mov    DWORD PTR [esp+0x4],edi
  4066ac:	89 04 24             	mov    DWORD PTR [esp],eax
  4066af:	89 c3                	mov    ebx,eax
  4066b1:	e8 0a 0b 00 00       	call   4071c0 <___quorem_D2A>
  4066b6:	8b 6c 24 18          	mov    ebp,DWORD PTR [esp+0x18]
  4066ba:	83 c0 30             	add    eax,0x30
  4066bd:	89 44 24 10          	mov    DWORD PTR [esp+0x10],eax
  4066c1:	89 6c 24 04          	mov    DWORD PTR [esp+0x4],ebp
  4066c5:	89 3c 24             	mov    DWORD PTR [esp],edi
  4066c8:	e8 63 14 00 00       	call   407b30 <___cmp_D2A>
  4066cd:	85 c0                	test   eax,eax
  4066cf:	0f 8e 88 02 00 00    	jle    40695d <___gdtoa+0x136d>
  4066d5:	0f b6 44 24 10       	movzx  eax,BYTE PTR [esp+0x10]
  4066da:	83 c6 01             	add    esi,0x1
  4066dd:	88 46 ff             	mov    BYTE PTR [esi-0x1],al
  4066e0:	c7 44 24 08 00 00 00 	mov    DWORD PTR [esp+0x8],0x0
  4066e7:	00 
  4066e8:	c7 44 24 04 0a 00 00 	mov    DWORD PTR [esp+0x4],0xa
  4066ef:	00 
  4066f0:	89 2c 24             	mov    DWORD PTR [esp],ebp
  4066f3:	e8 28 0f 00 00       	call   407620 <___multadd_D2A>
  4066f8:	39 6c 24 20          	cmp    DWORD PTR [esp+0x20],ebp
  4066fc:	89 44 24 18          	mov    DWORD PTR [esp+0x18],eax
  406700:	75 8e                	jne    406690 <___gdtoa+0x10a0>
  406702:	89 44 24 20          	mov    DWORD PTR [esp+0x20],eax
  406706:	eb 88                	jmp    406690 <___gdtoa+0x10a0>
  406708:	dd d8                	fstp   st(0)
  40670a:	dd d8                	fstp   st(0)
  40670c:	8b 44 24 0c          	mov    eax,DWORD PTR [esp+0xc]
  406710:	0f b6 4e ff          	movzx  ecx,BYTE PTR [esi-0x1]
  406714:	8b 54 24 24          	mov    edx,DWORD PTR [esp+0x24]
  406718:	89 44 24 38          	mov    DWORD PTR [esp+0x38],eax
  40671c:	e9 54 fe ff ff       	jmp    406575 <___gdtoa+0xf85>
  406721:	89 1c 24             	mov    DWORD PTR [esp],ebx
  406724:	c7 44 24 04 01 00 00 	mov    DWORD PTR [esp+0x4],0x1
  40672b:	00 
  40672c:	89 54 24 18          	mov    DWORD PTR [esp+0x18],edx
  406730:	e8 eb 12 00 00       	call   407a20 <___lshift_D2A>
  406735:	89 7c 24 04          	mov    DWORD PTR [esp+0x4],edi
  406739:	89 04 24             	mov    DWORD PTR [esp],eax
  40673c:	89 c3                	mov    ebx,eax
  40673e:	e8 ed 13 00 00       	call   407b30 <___cmp_D2A>
  406743:	8b 54 24 18          	mov    edx,DWORD PTR [esp+0x18]
  406747:	83 f8 00             	cmp    eax,0x0
  40674a:	0f 8f ff fb ff ff    	jg     40634f <___gdtoa+0xd5f>
  406750:	75 0b                	jne    40675d <___gdtoa+0x116d>
  406752:	f6 44 24 10 01       	test   BYTE PTR [esp+0x10],0x1
  406757:	0f 85 f2 fb ff ff    	jne    40634f <___gdtoa+0xd5f>
  40675d:	83 7b 10 01          	cmp    DWORD PTR [ebx+0x10],0x1
  406761:	0f 8e dc 02 00 00    	jle    406a43 <___gdtoa+0x1453>
  406767:	c7 44 24 18 10 00 00 	mov    DWORD PTR [esp+0x18],0x10
  40676e:	00 
  40676f:	eb 02                	jmp    406773 <___gdtoa+0x1183>
  406771:	89 c6                	mov    esi,eax
  406773:	80 7e ff 30          	cmp    BYTE PTR [esi-0x1],0x30
  406777:	8d 46 ff             	lea    eax,[esi-0x1]
  40677a:	74 f5                	je     406771 <___gdtoa+0x1181>
  40677c:	8b 44 24 0c          	mov    eax,DWORD PTR [esp+0xc]
  406780:	83 c0 01             	add    eax,0x1
  406783:	89 44 24 0c          	mov    DWORD PTR [esp+0xc],eax
  406787:	e9 c5 f6 ff ff       	jmp    405e51 <___gdtoa+0x861>
  40678c:	8b 44 24 18          	mov    eax,DWORD PTR [esp+0x18]
  406790:	85 c0                	test   eax,eax
  406792:	0f 84 fa f3 ff ff    	je     405b92 <___gdtoa+0x5a2>
  406798:	8b 54 24 44          	mov    edx,DWORD PTR [esp+0x44]
  40679c:	85 d2                	test   edx,edx
  40679e:	0f 8e 3e f4 ff ff    	jle    405be2 <___gdtoa+0x5f2>
  4067a4:	d9 c0                	fld    st(0)
  4067a6:	d8 0d 44 a3 40 00    	fmul   DWORD PTR ds:0x40a344
  4067ac:	c7 44 24 38 ff ff ff 	mov    DWORD PTR [esp+0x38],0xffffffff
  4067b3:	ff 
  4067b4:	d9 c0                	fld    st(0)
  4067b6:	d8 0d 48 a3 40 00    	fmul   DWORD PTR ds:0x40a348
  4067bc:	d8 05 4c a3 40 00    	fadd   DWORD PTR ds:0x40a34c
  4067c2:	dd 5c 24 10          	fstp   QWORD PTR [esp+0x10]
  4067c6:	81 6c 24 14 00 00 40 	sub    DWORD PTR [esp+0x14],0x3400000
  4067cd:	03 
  4067ce:	e9 02 f2 ff ff       	jmp    4059d5 <___gdtoa+0x3e5>
  4067d3:	8b 45 04             	mov    eax,DWORD PTR [ebp+0x4]
  4067d6:	89 04 24             	mov    DWORD PTR [esp],eax
  4067d9:	e8 02 0d 00 00       	call   4074e0 <___Balloc_D2A>
  4067de:	8d 48 0c             	lea    ecx,[eax+0xc]
  4067e1:	89 c6                	mov    esi,eax
  4067e3:	8b 45 10             	mov    eax,DWORD PTR [ebp+0x10]
  4067e6:	89 0c 24             	mov    DWORD PTR [esp],ecx
  4067e9:	8d 14 85 08 00 00 00 	lea    edx,[eax*4+0x8]
  4067f0:	89 e8                	mov    eax,ebp
  4067f2:	83 c0 0c             	add    eax,0xc
  4067f5:	89 54 24 08          	mov    DWORD PTR [esp+0x8],edx
  4067f9:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
  4067fd:	e8 d6 18 00 00       	call   4080d8 <_memcpy>
  406802:	c7 44 24 04 01 00 00 	mov    DWORD PTR [esp+0x4],0x1
  406809:	00 
  40680a:	89 34 24             	mov    DWORD PTR [esp],esi
  40680d:	e8 0e 12 00 00       	call   407a20 <___lshift_D2A>
  406812:	89 c5                	mov    ebp,eax
  406814:	e9 d1 f8 ff ff       	jmp    4060ea <___gdtoa+0xafa>
  406819:	89 fa                	mov    edx,edi
  40681b:	8b 74 24 28          	mov    esi,DWORD PTR [esp+0x28]
  40681f:	8b 7c 24 1c          	mov    edi,DWORD PTR [esp+0x1c]
  406823:	89 6c 24 20          	mov    DWORD PTR [esp+0x20],ebp
  406827:	e9 04 fb ff ff       	jmp    406330 <___gdtoa+0xd40>
  40682c:	83 7c 24 2c 02       	cmp    DWORD PTR [esp+0x2c],0x2
  406831:	0f 84 2c f9 ff ff    	je     406163 <___gdtoa+0xb73>
  406837:	8b 74 24 28          	mov    esi,DWORD PTR [esp+0x28]
  40683b:	83 7c 24 10 39       	cmp    DWORD PTR [esp+0x10],0x39
  406840:	89 7c 24 20          	mov    DWORD PTR [esp+0x20],edi
  406844:	8b 7c 24 1c          	mov    edi,DWORD PTR [esp+0x1c]
  406848:	89 f0                	mov    eax,esi
  40684a:	0f 84 f1 00 00 00    	je     406941 <___gdtoa+0x1351>
  406850:	0f b6 4c 24 10       	movzx  ecx,BYTE PTR [esp+0x10]
  406855:	83 c6 01             	add    esi,0x1
  406858:	8b 54 24 20          	mov    edx,DWORD PTR [esp+0x20]
  40685c:	c7 44 24 18 20 00 00 	mov    DWORD PTR [esp+0x18],0x20
  406863:	00 
  406864:	89 6c 24 20          	mov    DWORD PTR [esp+0x20],ebp
  406868:	83 c1 01             	add    ecx,0x1
  40686b:	88 08                	mov    BYTE PTR [eax],cl
  40686d:	8b 44 24 0c          	mov    eax,DWORD PTR [esp+0xc]
  406871:	83 c0 01             	add    eax,0x1
  406874:	89 44 24 0c          	mov    DWORD PTR [esp+0xc],eax
  406878:	e9 d4 f5 ff ff       	jmp    405e51 <___gdtoa+0x861>
  40687d:	8b 7c 24 30          	mov    edi,DWORD PTR [esp+0x30]
  406881:	8b 74 24 28          	mov    esi,DWORD PTR [esp+0x28]
  406885:	e9 ac f3 ff ff       	jmp    405c36 <___gdtoa+0x646>
  40688a:	83 7b 14 00          	cmp    DWORD PTR [ebx+0x14],0x0
  40688e:	0f 85 ec fd ff ff    	jne    406680 <___gdtoa+0x1090>
  406894:	85 c0                	test   eax,eax
  406896:	89 54 24 18          	mov    DWORD PTR [esp+0x18],edx
  40689a:	0f 8e d3 00 00 00    	jle    406973 <___gdtoa+0x1383>
  4068a0:	89 1c 24             	mov    DWORD PTR [esp],ebx
  4068a3:	c7 44 24 04 01 00 00 	mov    DWORD PTR [esp+0x4],0x1
  4068aa:	00 
  4068ab:	e8 70 11 00 00       	call   407a20 <___lshift_D2A>
  4068b0:	89 7c 24 04          	mov    DWORD PTR [esp+0x4],edi
  4068b4:	89 04 24             	mov    DWORD PTR [esp],eax
  4068b7:	89 c3                	mov    ebx,eax
  4068b9:	e8 72 12 00 00       	call   407b30 <___cmp_D2A>
  4068be:	8b 54 24 18          	mov    edx,DWORD PTR [esp+0x18]
  4068c2:	83 f8 00             	cmp    eax,0x0
  4068c5:	0f 8e 98 01 00 00    	jle    406a63 <___gdtoa+0x1473>
  4068cb:	8b 44 24 30          	mov    eax,DWORD PTR [esp+0x30]
  4068cf:	83 c0 31             	add    eax,0x31
  4068d2:	83 fa 39             	cmp    edx,0x39
  4068d5:	89 44 24 10          	mov    DWORD PTR [esp+0x10],eax
  4068d9:	74 64                	je     40693f <___gdtoa+0x134f>
  4068db:	c7 44 24 18 20 00 00 	mov    DWORD PTR [esp+0x18],0x20
  4068e2:	00 
  4068e3:	83 7b 10 01          	cmp    DWORD PTR [ebx+0x10],0x1
  4068e7:	7f 06                	jg     4068ef <___gdtoa+0x12ff>
  4068e9:	83 7b 14 00          	cmp    DWORD PTR [ebx+0x14],0x0
  4068ed:	74 08                	je     4068f7 <___gdtoa+0x1307>
  4068ef:	c7 44 24 18 10 00 00 	mov    DWORD PTR [esp+0x18],0x10
  4068f6:	00 
  4068f7:	0f b6 44 24 10       	movzx  eax,BYTE PTR [esp+0x10]
  4068fc:	83 c6 01             	add    esi,0x1
  4068ff:	8b 54 24 20          	mov    edx,DWORD PTR [esp+0x20]
  406903:	89 6c 24 20          	mov    DWORD PTR [esp+0x20],ebp
  406907:	88 46 ff             	mov    BYTE PTR [esi-0x1],al
  40690a:	8b 44 24 0c          	mov    eax,DWORD PTR [esp+0xc]
  40690e:	83 c0 01             	add    eax,0x1
  406911:	89 44 24 0c          	mov    DWORD PTR [esp+0xc],eax
  406915:	e9 37 f5 ff ff       	jmp    405e51 <___gdtoa+0x861>
  40691a:	8b 4b 14             	mov    ecx,DWORD PTR [ebx+0x14]
  40691d:	85 c9                	test   ecx,ecx
  40691f:	0f 85 2a fa ff ff    	jne    40634f <___gdtoa+0xd5f>
  406925:	c7 44 24 18 00 00 00 	mov    DWORD PTR [esp+0x18],0x0
  40692c:	00 
  40692d:	e9 41 fe ff ff       	jmp    406773 <___gdtoa+0x1183>
  406932:	c7 44 24 18 10 00 00 	mov    DWORD PTR [esp+0x18],0x10
  406939:	00 
  40693a:	e9 bc fb ff ff       	jmp    4064fb <___gdtoa+0xf0b>
  40693f:	89 f0                	mov    eax,esi
  406941:	8b 54 24 20          	mov    edx,DWORD PTR [esp+0x20]
  406945:	83 c6 01             	add    esi,0x1
  406948:	b9 39 00 00 00       	mov    ecx,0x39
  40694d:	89 6c 24 20          	mov    DWORD PTR [esp+0x20],ebp
  406951:	8b 6c 24 24          	mov    ebp,DWORD PTR [esp+0x24]
  406955:	c6 00 39             	mov    BYTE PTR [eax],0x39
  406958:	e9 11 fa ff ff       	jmp    40636e <___gdtoa+0xd7e>
  40695d:	83 7c 24 10 39       	cmp    DWORD PTR [esp+0x10],0x39
  406962:	74 db                	je     40693f <___gdtoa+0x134f>
  406964:	83 44 24 10 01       	add    DWORD PTR [esp+0x10],0x1
  406969:	c7 44 24 18 20 00 00 	mov    DWORD PTR [esp+0x18],0x20
  406970:	00 
  406971:	eb 84                	jmp    4068f7 <___gdtoa+0x1307>
  406973:	c7 44 24 18 00 00 00 	mov    DWORD PTR [esp+0x18],0x0
  40697a:	00 
  40697b:	e9 63 ff ff ff       	jmp    4068e3 <___gdtoa+0x12f3>
  406980:	0f 85 a8 f6 ff ff    	jne    40602e <___gdtoa+0xa3e>
  406986:	dd d8                	fstp   st(0)
  406988:	dd d8                	fstp   st(0)
  40698a:	e9 0c f7 ff ff       	jmp    40609b <___gdtoa+0xaab>
  40698f:	89 f1                	mov    ecx,esi
  406991:	8b 74 24 28          	mov    esi,DWORD PTR [esp+0x28]
  406995:	83 7c 24 10 39       	cmp    DWORD PTR [esp+0x10],0x39
  40699a:	89 7c 24 20          	mov    DWORD PTR [esp+0x20],edi
  40699e:	8b 7c 24 1c          	mov    edi,DWORD PTR [esp+0x1c]
  4069a2:	89 f0                	mov    eax,esi
  4069a4:	74 99                	je     40693f <___gdtoa+0x134f>
  4069a6:	85 c9                	test   ecx,ecx
  4069a8:	7e 73                	jle    406a1d <___gdtoa+0x142d>
  4069aa:	8b 4c 24 30          	mov    ecx,DWORD PTR [esp+0x30]
  4069ae:	c7 44 24 18 20 00 00 	mov    DWORD PTR [esp+0x18],0x20
  4069b5:	00 
  4069b6:	83 c1 31             	add    ecx,0x31
  4069b9:	89 4c 24 10          	mov    DWORD PTR [esp+0x10],ecx
  4069bd:	0f b6 4c 24 10       	movzx  ecx,BYTE PTR [esp+0x10]
  4069c2:	83 c6 01             	add    esi,0x1
  4069c5:	8b 54 24 20          	mov    edx,DWORD PTR [esp+0x20]
  4069c9:	89 6c 24 20          	mov    DWORD PTR [esp+0x20],ebp
  4069cd:	88 08                	mov    BYTE PTR [eax],cl
  4069cf:	8b 44 24 0c          	mov    eax,DWORD PTR [esp+0xc]
  4069d3:	83 c0 01             	add    eax,0x1
  4069d6:	89 44 24 0c          	mov    DWORD PTR [esp+0xc],eax
  4069da:	e9 72 f4 ff ff       	jmp    405e51 <___gdtoa+0x861>
  4069df:	8b 44 24 20          	mov    eax,DWORD PTR [esp+0x20]
  4069e3:	c7 44 24 08 00 00 00 	mov    DWORD PTR [esp+0x8],0x0
  4069ea:	00 
  4069eb:	c7 44 24 04 0a 00 00 	mov    DWORD PTR [esp+0x4],0xa
  4069f2:	00 
  4069f3:	89 04 24             	mov    DWORD PTR [esp],eax
  4069f6:	e8 25 0c 00 00       	call   407620 <___multadd_D2A>
  4069fb:	83 7c 24 44 00       	cmp    DWORD PTR [esp+0x44],0x0
  406a00:	89 44 24 20          	mov    DWORD PTR [esp+0x20],eax
  406a04:	8b 44 24 44          	mov    eax,DWORD PTR [esp+0x44]
  406a08:	7f 0a                	jg     406a14 <___gdtoa+0x1424>
  406a0a:	83 bc 24 90 00 00 00 	cmp    DWORD PTR [esp+0x90],0x2
  406a11:	02 
  406a12:	7f 46                	jg     406a5a <___gdtoa+0x146a>
  406a14:	89 44 24 18          	mov    DWORD PTR [esp+0x18],eax
  406a18:	e9 a2 f6 ff ff       	jmp    4060bf <___gdtoa+0xacf>
  406a1d:	83 7b 10 01          	cmp    DWORD PTR [ebx+0x10],0x1
  406a21:	c7 44 24 18 10 00 00 	mov    DWORD PTR [esp+0x18],0x10
  406a28:	00 
  406a29:	7f 92                	jg     4069bd <___gdtoa+0x13cd>
  406a2b:	83 7b 14 01          	cmp    DWORD PTR [ebx+0x14],0x1
  406a2f:	19 c9                	sbb    ecx,ecx
  406a31:	89 4c 24 18          	mov    DWORD PTR [esp+0x18],ecx
  406a35:	f7 54 24 18          	not    DWORD PTR [esp+0x18]
  406a39:	83 64 24 18 10       	and    DWORD PTR [esp+0x18],0x10
  406a3e:	e9 7a ff ff ff       	jmp    4069bd <___gdtoa+0x13cd>
  406a43:	83 7b 14 00          	cmp    DWORD PTR [ebx+0x14],0x0
  406a47:	c7 44 24 18 00 00 00 	mov    DWORD PTR [esp+0x18],0x0
  406a4e:	00 
  406a4f:	0f 85 12 fd ff ff    	jne    406767 <___gdtoa+0x1177>
  406a55:	e9 19 fd ff ff       	jmp    406773 <___gdtoa+0x1183>
  406a5a:	89 44 24 18          	mov    DWORD PTR [esp+0x18],eax
  406a5e:	e9 21 f3 ff ff       	jmp    405d84 <___gdtoa+0x794>
  406a63:	0f 85 72 fe ff ff    	jne    4068db <___gdtoa+0x12eb>
  406a69:	f6 44 24 10 01       	test   BYTE PTR [esp+0x10],0x1
  406a6e:	66 90                	xchg   ax,ax
  406a70:	0f 84 65 fe ff ff    	je     4068db <___gdtoa+0x12eb>
  406a76:	e9 50 fe ff ff       	jmp    4068cb <___gdtoa+0x12db>
  406a7b:	31 c0                	xor    eax,eax
  406a7d:	8d 76 00             	lea    esi,[esi+0x0]
  406a80:	e9 8f ec ff ff       	jmp    405714 <___gdtoa+0x124>
  406a85:	b8 01 00 00 00       	mov    eax,0x1
  406a8a:	e9 40 ee ff ff       	jmp    4058cf <___gdtoa+0x2df>
  406a8f:	90                   	nop

00406a90 <___wcrtomb_cp>:
  406a90:	55                   	push   ebp
  406a91:	89 e5                	mov    ebp,esp
  406a93:	83 ec 48             	sub    esp,0x48
  406a96:	8b 55 10             	mov    edx,DWORD PTR [ebp+0x10]
  406a99:	8b 45 0c             	mov    eax,DWORD PTR [ebp+0xc]
  406a9c:	85 d2                	test   edx,edx
  406a9e:	66 89 45 e4          	mov    WORD PTR [ebp-0x1c],ax
  406aa2:	75 12                	jne    406ab6 <___wcrtomb_cp+0x26>
  406aa4:	66 3d ff 00          	cmp    ax,0xff
  406aa8:	77 5d                	ja     406b07 <___wcrtomb_cp+0x77>
  406aaa:	8b 4d 08             	mov    ecx,DWORD PTR [ebp+0x8]
  406aad:	88 01                	mov    BYTE PTR [ecx],al
  406aaf:	b8 01 00 00 00       	mov    eax,0x1
  406ab4:	c9                   	leave  
  406ab5:	c3                   	ret    
  406ab6:	8d 45 f4             	lea    eax,[ebp-0xc]
  406ab9:	89 44 24 1c          	mov    DWORD PTR [esp+0x1c],eax
  406abd:	8b 45 14             	mov    eax,DWORD PTR [ebp+0x14]
  406ac0:	c7 44 24 18 00 00 00 	mov    DWORD PTR [esp+0x18],0x0
  406ac7:	00 
  406ac8:	c7 44 24 0c 01 00 00 	mov    DWORD PTR [esp+0xc],0x1
  406acf:	00 
  406ad0:	c7 44 24 04 00 00 00 	mov    DWORD PTR [esp+0x4],0x0
  406ad7:	00 
  406ad8:	89 44 24 14          	mov    DWORD PTR [esp+0x14],eax
  406adc:	8b 45 08             	mov    eax,DWORD PTR [ebp+0x8]
  406adf:	89 14 24             	mov    DWORD PTR [esp],edx
  406ae2:	c7 45 f4 00 00 00 00 	mov    DWORD PTR [ebp-0xc],0x0
  406ae9:	89 44 24 10          	mov    DWORD PTR [esp+0x10],eax
  406aed:	8d 45 e4             	lea    eax,[ebp-0x1c]
  406af0:	89 44 24 08          	mov    DWORD PTR [esp+0x8],eax
  406af4:	e8 ef 16 00 00       	call   4081e8 <_WideCharToMultiByte@32>
  406af9:	83 ec 20             	sub    esp,0x20
  406afc:	85 c0                	test   eax,eax
  406afe:	74 07                	je     406b07 <___wcrtomb_cp+0x77>
  406b00:	8b 55 f4             	mov    edx,DWORD PTR [ebp-0xc]
  406b03:	85 d2                	test   edx,edx
  406b05:	74 ad                	je     406ab4 <___wcrtomb_cp+0x24>
  406b07:	e8 04 16 00 00       	call   408110 <__errno>
  406b0c:	c7 00 2a 00 00 00    	mov    DWORD PTR [eax],0x2a
  406b12:	b8 ff ff ff ff       	mov    eax,0xffffffff
  406b17:	c9                   	leave  
  406b18:	c3                   	ret    
  406b19:	8d b4 26 00 00 00 00 	lea    esi,[esi+eiz*1+0x0]

00406b20 <_wcrtomb>:
  406b20:	57                   	push   edi
  406b21:	56                   	push   esi
  406b22:	53                   	push   ebx
  406b23:	83 ec 20             	sub    esp,0x20
  406b26:	8b 5c 24 30          	mov    ebx,DWORD PTR [esp+0x30]
  406b2a:	8b 74 24 34          	mov    esi,DWORD PTR [esp+0x34]
  406b2e:	85 db                	test   ebx,ebx
  406b30:	74 5e                	je     406b90 <_wcrtomb+0x70>
  406b32:	a1 b0 e1 40 00       	mov    eax,ds:0x40e1b0
  406b37:	8b 38                	mov    edi,DWORD PTR [eax]
  406b39:	c7 44 24 04 00 00 00 	mov    DWORD PTR [esp+0x4],0x0
  406b40:	00 
  406b41:	c7 04 24 02 00 00 00 	mov    DWORD PTR [esp],0x2
  406b48:	e8 cb 15 00 00       	call   408118 <_setlocale>
  406b4d:	c7 44 24 04 2e 00 00 	mov    DWORD PTR [esp+0x4],0x2e
  406b54:	00 
  406b55:	89 04 24             	mov    DWORD PTR [esp],eax
  406b58:	e8 fb 15 00 00       	call   408158 <_strchr>
  406b5d:	31 d2                	xor    edx,edx
  406b5f:	85 c0                	test   eax,eax
  406b61:	74 0d                	je     406b70 <_wcrtomb+0x50>
  406b63:	83 c0 01             	add    eax,0x1
  406b66:	89 04 24             	mov    DWORD PTR [esp],eax
  406b69:	e8 f2 15 00 00       	call   408160 <_atoi>
  406b6e:	89 c2                	mov    edx,eax
  406b70:	0f b7 f6             	movzx  esi,si
  406b73:	89 7c 24 0c          	mov    DWORD PTR [esp+0xc],edi
  406b77:	89 74 24 04          	mov    DWORD PTR [esp+0x4],esi
  406b7b:	89 1c 24             	mov    DWORD PTR [esp],ebx
  406b7e:	89 54 24 08          	mov    DWORD PTR [esp+0x8],edx
  406b82:	e8 09 ff ff ff       	call   406a90 <___wcrtomb_cp>
  406b87:	83 c4 20             	add    esp,0x20
  406b8a:	5b                   	pop    ebx
  406b8b:	5e                   	pop    esi
  406b8c:	5f                   	pop    edi
  406b8d:	c3                   	ret    
  406b8e:	66 90                	xchg   ax,ax
  406b90:	8d 5c 24 1e          	lea    ebx,[esp+0x1e]
  406b94:	eb 9c                	jmp    406b32 <_wcrtomb+0x12>
  406b96:	8d 76 00             	lea    esi,[esi+0x0]
  406b99:	8d bc 27 00 00 00 00 	lea    edi,[edi+eiz*1+0x0]

00406ba0 <_wcsrtombs>:
  406ba0:	55                   	push   ebp
  406ba1:	57                   	push   edi
  406ba2:	56                   	push   esi
  406ba3:	31 f6                	xor    esi,esi
  406ba5:	53                   	push   ebx
  406ba6:	83 ec 3c             	sub    esp,0x3c
  406ba9:	c7 44 24 04 00 00 00 	mov    DWORD PTR [esp+0x4],0x0
  406bb0:	00 
  406bb1:	8b 5c 24 50          	mov    ebx,DWORD PTR [esp+0x50]
  406bb5:	c7 04 24 02 00 00 00 	mov    DWORD PTR [esp],0x2
  406bbc:	e8 57 15 00 00       	call   408118 <_setlocale>
  406bc1:	c7 44 24 04 2e 00 00 	mov    DWORD PTR [esp+0x4],0x2e
  406bc8:	00 
  406bc9:	89 04 24             	mov    DWORD PTR [esp],eax
  406bcc:	e8 87 15 00 00       	call   408158 <_strchr>
  406bd1:	85 c0                	test   eax,eax
  406bd3:	74 0d                	je     406be2 <_wcsrtombs+0x42>
  406bd5:	83 c0 01             	add    eax,0x1
  406bd8:	89 04 24             	mov    DWORD PTR [esp],eax
  406bdb:	e8 80 15 00 00       	call   408160 <_atoi>
  406be0:	89 c6                	mov    esi,eax
  406be2:	a1 b0 e1 40 00       	mov    eax,ds:0x40e1b0
  406be7:	8b 00                	mov    eax,DWORD PTR [eax]
  406be9:	89 44 24 1c          	mov    DWORD PTR [esp+0x1c],eax
  406bed:	8b 44 24 54          	mov    eax,DWORD PTR [esp+0x54]
  406bf1:	8b 38                	mov    edi,DWORD PTR [eax]
  406bf3:	85 ff                	test   edi,edi
  406bf5:	0f 84 cc 00 00 00    	je     406cc7 <_wcsrtombs+0x127>
  406bfb:	31 ed                	xor    ebp,ebp
  406bfd:	85 db                	test   ebx,ebx
  406bff:	74 76                	je     406c77 <_wcsrtombs+0xd7>
  406c01:	8b 4c 24 58          	mov    ecx,DWORD PTR [esp+0x58]
  406c05:	85 c9                	test   ecx,ecx
  406c07:	74 49                	je     406c52 <_wcsrtombs+0xb2>
  406c09:	89 f0                	mov    eax,esi
  406c0b:	89 fe                	mov    esi,edi
  406c0d:	89 c7                	mov    edi,eax
  406c0f:	eb 13                	jmp    406c24 <_wcsrtombs+0x84>
  406c11:	01 c3                	add    ebx,eax
  406c13:	01 c5                	add    ebp,eax
  406c15:	80 7b ff 00          	cmp    BYTE PTR [ebx-0x1],0x0
  406c19:	74 47                	je     406c62 <_wcsrtombs+0xc2>
  406c1b:	83 c6 02             	add    esi,0x2
  406c1e:	39 6c 24 58          	cmp    DWORD PTR [esp+0x58],ebp
  406c22:	76 2c                	jbe    406c50 <_wcsrtombs+0xb0>
  406c24:	8b 44 24 1c          	mov    eax,DWORD PTR [esp+0x1c]
  406c28:	89 7c 24 08          	mov    DWORD PTR [esp+0x8],edi
  406c2c:	89 44 24 0c          	mov    DWORD PTR [esp+0xc],eax
  406c30:	0f b7 06             	movzx  eax,WORD PTR [esi]
  406c33:	89 1c 24             	mov    DWORD PTR [esp],ebx
  406c36:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
  406c3a:	e8 51 fe ff ff       	call   406a90 <___wcrtomb_cp>
  406c3f:	85 c0                	test   eax,eax
  406c41:	7f ce                	jg     406c11 <_wcsrtombs+0x71>
  406c43:	b8 ff ff ff ff       	mov    eax,0xffffffff
  406c48:	83 c4 3c             	add    esp,0x3c
  406c4b:	5b                   	pop    ebx
  406c4c:	5e                   	pop    esi
  406c4d:	5f                   	pop    edi
  406c4e:	5d                   	pop    ebp
  406c4f:	c3                   	ret    
  406c50:	89 f7                	mov    edi,esi
  406c52:	8b 44 24 54          	mov    eax,DWORD PTR [esp+0x54]
  406c56:	89 38                	mov    DWORD PTR [eax],edi
  406c58:	83 c4 3c             	add    esp,0x3c
  406c5b:	89 e8                	mov    eax,ebp
  406c5d:	5b                   	pop    ebx
  406c5e:	5e                   	pop    esi
  406c5f:	5f                   	pop    edi
  406c60:	5d                   	pop    ebp
  406c61:	c3                   	ret    
  406c62:	8b 44 24 54          	mov    eax,DWORD PTR [esp+0x54]
  406c66:	c7 00 00 00 00 00    	mov    DWORD PTR [eax],0x0
  406c6c:	83 c4 3c             	add    esp,0x3c
  406c6f:	5b                   	pop    ebx
  406c70:	8d 45 ff             	lea    eax,[ebp-0x1]
  406c73:	5e                   	pop    esi
  406c74:	5f                   	pop    edi
  406c75:	5d                   	pop    ebp
  406c76:	c3                   	ret    
  406c77:	8b 44 24 58          	mov    eax,DWORD PTR [esp+0x58]
  406c7b:	85 c0                	test   eax,eax
  406c7d:	74 63                	je     406ce2 <_wcsrtombs+0x142>
  406c7f:	89 e8                	mov    eax,ebp
  406c81:	8b 5c 24 1c          	mov    ebx,DWORD PTR [esp+0x1c]
  406c85:	89 fd                	mov    ebp,edi
  406c87:	89 c7                	mov    edi,eax
  406c89:	eb 17                	jmp    406ca2 <_wcsrtombs+0x102>
  406c8b:	90                   	nop
  406c8c:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  406c90:	01 c7                	add    edi,eax
  406c92:	80 7c 04 2d 00       	cmp    BYTE PTR [esp+eax*1+0x2d],0x0
  406c97:	74 38                	je     406cd1 <_wcsrtombs+0x131>
  406c99:	83 c5 02             	add    ebp,0x2
  406c9c:	39 7c 24 58          	cmp    DWORD PTR [esp+0x58],edi
  406ca0:	76 37                	jbe    406cd9 <_wcsrtombs+0x139>
  406ca2:	89 5c 24 0c          	mov    DWORD PTR [esp+0xc],ebx
  406ca6:	89 74 24 08          	mov    DWORD PTR [esp+0x8],esi
  406caa:	0f b7 45 00          	movzx  eax,WORD PTR [ebp+0x0]
  406cae:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
  406cb2:	8d 44 24 2e          	lea    eax,[esp+0x2e]
  406cb6:	89 04 24             	mov    DWORD PTR [esp],eax
  406cb9:	e8 d2 fd ff ff       	call   406a90 <___wcrtomb_cp>
  406cbe:	85 c0                	test   eax,eax
  406cc0:	7f ce                	jg     406c90 <_wcsrtombs+0xf0>
  406cc2:	e9 7c ff ff ff       	jmp    406c43 <_wcsrtombs+0xa3>
  406cc7:	83 c4 3c             	add    esp,0x3c
  406cca:	31 c0                	xor    eax,eax
  406ccc:	5b                   	pop    ebx
  406ccd:	5e                   	pop    esi
  406cce:	5f                   	pop    edi
  406ccf:	5d                   	pop    ebp
  406cd0:	c3                   	ret    
  406cd1:	8d 47 ff             	lea    eax,[edi-0x1]
  406cd4:	e9 6f ff ff ff       	jmp    406c48 <_wcsrtombs+0xa8>
  406cd9:	89 fd                	mov    ebp,edi
  406cdb:	89 e8                	mov    eax,ebp
  406cdd:	e9 66 ff ff ff       	jmp    406c48 <_wcsrtombs+0xa8>
  406ce2:	89 dd                	mov    ebp,ebx
  406ce4:	89 e8                	mov    eax,ebp
  406ce6:	e9 5d ff ff ff       	jmp    406c48 <_wcsrtombs+0xa8>
  406ceb:	90                   	nop
  406cec:	90                   	nop
  406ced:	90                   	nop
  406cee:	90                   	nop
  406cef:	90                   	nop

00406cf0 <___mbrtowc_cp>:
  406cf0:	55                   	push   ebp
  406cf1:	89 e5                	mov    ebp,esp
  406cf3:	56                   	push   esi
  406cf4:	53                   	push   ebx
  406cf5:	83 ec 30             	sub    esp,0x30
  406cf8:	8b 5d 0c             	mov    ebx,DWORD PTR [ebp+0xc]
  406cfb:	8b 75 14             	mov    esi,DWORD PTR [ebp+0x14]
  406cfe:	85 db                	test   ebx,ebx
  406d00:	0f 84 2d 01 00 00    	je     406e33 <___mbrtowc_cp+0x143>
  406d06:	8b 4d 10             	mov    ecx,DWORD PTR [ebp+0x10]
  406d09:	85 c9                	test   ecx,ecx
  406d0b:	0f 84 2f 01 00 00    	je     406e40 <___mbrtowc_cp+0x150>
  406d11:	8b 06                	mov    eax,DWORD PTR [esi]
  406d13:	c7 06 00 00 00 00    	mov    DWORD PTR [esi],0x0
  406d19:	89 45 f4             	mov    DWORD PTR [ebp-0xc],eax
  406d1c:	0f b6 03             	movzx  eax,BYTE PTR [ebx]
  406d1f:	84 c0                	test   al,al
  406d21:	0f 84 99 00 00 00    	je     406dc0 <___mbrtowc_cp+0xd0>
  406d27:	83 7d 1c 01          	cmp    DWORD PTR [ebp+0x1c],0x1
  406d2b:	76 73                	jbe    406da0 <___mbrtowc_cp+0xb0>
  406d2d:	80 7d f4 00          	cmp    BYTE PTR [ebp-0xc],0x0
  406d31:	0f 85 9a 00 00 00    	jne    406dd1 <___mbrtowc_cp+0xe1>
  406d37:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
  406d3b:	8b 45 18             	mov    eax,DWORD PTR [ebp+0x18]
  406d3e:	89 04 24             	mov    DWORD PTR [esp],eax
  406d41:	e8 aa 14 00 00       	call   4081f0 <_IsDBCSLeadByteEx@8>
  406d46:	83 ec 08             	sub    esp,0x8
  406d49:	85 c0                	test   eax,eax
  406d4b:	74 53                	je     406da0 <___mbrtowc_cp+0xb0>
  406d4d:	83 7d 10 01          	cmp    DWORD PTR [ebp+0x10],0x1
  406d51:	0f 86 05 01 00 00    	jbe    406e5c <___mbrtowc_cp+0x16c>
  406d57:	8b 45 08             	mov    eax,DWORD PTR [ebp+0x8]
  406d5a:	c7 44 24 14 01 00 00 	mov    DWORD PTR [esp+0x14],0x1
  406d61:	00 
  406d62:	c7 44 24 0c 02 00 00 	mov    DWORD PTR [esp+0xc],0x2
  406d69:	00 
  406d6a:	89 5c 24 08          	mov    DWORD PTR [esp+0x8],ebx
  406d6e:	89 44 24 10          	mov    DWORD PTR [esp+0x10],eax
  406d72:	8b 45 18             	mov    eax,DWORD PTR [ebp+0x18]
  406d75:	c7 44 24 04 08 00 00 	mov    DWORD PTR [esp+0x4],0x8
  406d7c:	00 
  406d7d:	89 04 24             	mov    DWORD PTR [esp],eax
  406d80:	e8 73 14 00 00       	call   4081f8 <_MultiByteToWideChar@24>
  406d85:	83 ec 18             	sub    esp,0x18
  406d88:	85 c0                	test   eax,eax
  406d8a:	0f 84 b7 00 00 00    	je     406e47 <___mbrtowc_cp+0x157>
  406d90:	8d 65 f8             	lea    esp,[ebp-0x8]
  406d93:	b8 02 00 00 00       	mov    eax,0x2
  406d98:	5b                   	pop    ebx
  406d99:	5e                   	pop    esi
  406d9a:	5d                   	pop    ebp
  406d9b:	c3                   	ret    
  406d9c:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  406da0:	8b 45 18             	mov    eax,DWORD PTR [ebp+0x18]
  406da3:	85 c0                	test   eax,eax
  406da5:	75 50                	jne    406df7 <___mbrtowc_cp+0x107>
  406da7:	0f b6 03             	movzx  eax,BYTE PTR [ebx]
  406daa:	8b 55 08             	mov    edx,DWORD PTR [ebp+0x8]
  406dad:	66 89 02             	mov    WORD PTR [edx],ax
  406db0:	8d 65 f8             	lea    esp,[ebp-0x8]
  406db3:	b8 01 00 00 00       	mov    eax,0x1
  406db8:	5b                   	pop    ebx
  406db9:	5e                   	pop    esi
  406dba:	5d                   	pop    ebp
  406dbb:	c3                   	ret    
  406dbc:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  406dc0:	8b 45 08             	mov    eax,DWORD PTR [ebp+0x8]
  406dc3:	31 d2                	xor    edx,edx
  406dc5:	66 89 10             	mov    WORD PTR [eax],dx
  406dc8:	31 c0                	xor    eax,eax
  406dca:	8d 65 f8             	lea    esp,[ebp-0x8]
  406dcd:	5b                   	pop    ebx
  406dce:	5e                   	pop    esi
  406dcf:	5d                   	pop    ebp
  406dd0:	c3                   	ret    
  406dd1:	88 45 f5             	mov    BYTE PTR [ebp-0xb],al
  406dd4:	8b 45 08             	mov    eax,DWORD PTR [ebp+0x8]
  406dd7:	c7 44 24 14 01 00 00 	mov    DWORD PTR [esp+0x14],0x1
  406dde:	00 
  406ddf:	c7 44 24 0c 02 00 00 	mov    DWORD PTR [esp+0xc],0x2
  406de6:	00 
  406de7:	89 44 24 10          	mov    DWORD PTR [esp+0x10],eax
  406deb:	8d 45 f4             	lea    eax,[ebp-0xc]
  406dee:	89 44 24 08          	mov    DWORD PTR [esp+0x8],eax
  406df2:	e9 7b ff ff ff       	jmp    406d72 <___mbrtowc_cp+0x82>
  406df7:	8b 45 08             	mov    eax,DWORD PTR [ebp+0x8]
  406dfa:	c7 44 24 14 01 00 00 	mov    DWORD PTR [esp+0x14],0x1
  406e01:	00 
  406e02:	c7 44 24 0c 01 00 00 	mov    DWORD PTR [esp+0xc],0x1
  406e09:	00 
  406e0a:	89 5c 24 08          	mov    DWORD PTR [esp+0x8],ebx
  406e0e:	89 44 24 10          	mov    DWORD PTR [esp+0x10],eax
  406e12:	8b 45 18             	mov    eax,DWORD PTR [ebp+0x18]
  406e15:	c7 44 24 04 08 00 00 	mov    DWORD PTR [esp+0x4],0x8
  406e1c:	00 
  406e1d:	89 04 24             	mov    DWORD PTR [esp],eax
  406e20:	e8 d3 13 00 00       	call   4081f8 <_MultiByteToWideChar@24>
  406e25:	83 ec 18             	sub    esp,0x18
  406e28:	85 c0                	test   eax,eax
  406e2a:	74 1b                	je     406e47 <___mbrtowc_cp+0x157>
  406e2c:	b8 01 00 00 00       	mov    eax,0x1
  406e31:	eb 97                	jmp    406dca <___mbrtowc_cp+0xda>
  406e33:	8d 65 f8             	lea    esp,[ebp-0x8]
  406e36:	31 c0                	xor    eax,eax
  406e38:	5b                   	pop    ebx
  406e39:	5e                   	pop    esi
  406e3a:	5d                   	pop    ebp
  406e3b:	c3                   	ret    
  406e3c:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  406e40:	b8 fe ff ff ff       	mov    eax,0xfffffffe
  406e45:	eb 83                	jmp    406dca <___mbrtowc_cp+0xda>
  406e47:	e8 c4 12 00 00       	call   408110 <__errno>
  406e4c:	c7 00 2a 00 00 00    	mov    DWORD PTR [eax],0x2a
  406e52:	b8 ff ff ff ff       	mov    eax,0xffffffff
  406e57:	e9 6e ff ff ff       	jmp    406dca <___mbrtowc_cp+0xda>
  406e5c:	0f b6 03             	movzx  eax,BYTE PTR [ebx]
  406e5f:	88 06                	mov    BYTE PTR [esi],al
  406e61:	b8 fe ff ff ff       	mov    eax,0xfffffffe
  406e66:	e9 5f ff ff ff       	jmp    406dca <___mbrtowc_cp+0xda>
  406e6b:	90                   	nop
  406e6c:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]

00406e70 <_mbrtowc>:
  406e70:	56                   	push   esi
  406e71:	31 f6                	xor    esi,esi
  406e73:	53                   	push   ebx
  406e74:	83 ec 34             	sub    esp,0x34
  406e77:	8b 5c 24 40          	mov    ebx,DWORD PTR [esp+0x40]
  406e7b:	66 89 74 24 2e       	mov    WORD PTR [esp+0x2e],si
  406e80:	85 db                	test   ebx,ebx
  406e82:	74 70                	je     406ef4 <_mbrtowc+0x84>
  406e84:	a1 b0 e1 40 00       	mov    eax,ds:0x40e1b0
  406e89:	8b 30                	mov    esi,DWORD PTR [eax]
  406e8b:	c7 44 24 04 00 00 00 	mov    DWORD PTR [esp+0x4],0x0
  406e92:	00 
  406e93:	c7 04 24 02 00 00 00 	mov    DWORD PTR [esp],0x2
  406e9a:	e8 79 12 00 00       	call   408118 <_setlocale>
  406e9f:	c7 44 24 04 2e 00 00 	mov    DWORD PTR [esp+0x4],0x2e
  406ea6:	00 
  406ea7:	89 04 24             	mov    DWORD PTR [esp],eax
  406eaa:	e8 a9 12 00 00       	call   408158 <_strchr>
  406eaf:	31 c9                	xor    ecx,ecx
  406eb1:	85 c0                	test   eax,eax
  406eb3:	74 0d                	je     406ec2 <_mbrtowc+0x52>
  406eb5:	83 c0 01             	add    eax,0x1
  406eb8:	89 04 24             	mov    DWORD PTR [esp],eax
  406ebb:	e8 a0 12 00 00       	call   408160 <_atoi>
  406ec0:	89 c1                	mov    ecx,eax
  406ec2:	8b 54 24 4c          	mov    edx,DWORD PTR [esp+0x4c]
  406ec6:	85 d2                	test   edx,edx
  406ec8:	74 36                	je     406f00 <_mbrtowc+0x90>
  406eca:	8b 44 24 48          	mov    eax,DWORD PTR [esp+0x48]
  406ece:	89 74 24 14          	mov    DWORD PTR [esp+0x14],esi
  406ed2:	89 1c 24             	mov    DWORD PTR [esp],ebx
  406ed5:	89 4c 24 10          	mov    DWORD PTR [esp+0x10],ecx
  406ed9:	89 44 24 08          	mov    DWORD PTR [esp+0x8],eax
  406edd:	8b 44 24 44          	mov    eax,DWORD PTR [esp+0x44]
  406ee1:	89 54 24 0c          	mov    DWORD PTR [esp+0xc],edx
  406ee5:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
  406ee9:	e8 02 fe ff ff       	call   406cf0 <___mbrtowc_cp>
  406eee:	83 c4 34             	add    esp,0x34
  406ef1:	5b                   	pop    ebx
  406ef2:	5e                   	pop    esi
  406ef3:	c3                   	ret    
  406ef4:	8d 5c 24 2e          	lea    ebx,[esp+0x2e]
  406ef8:	eb 8a                	jmp    406e84 <_mbrtowc+0x14>
  406efa:	8d b6 00 00 00 00    	lea    esi,[esi+0x0]
  406f00:	ba 78 d0 40 00       	mov    edx,0x40d078
  406f05:	eb c3                	jmp    406eca <_mbrtowc+0x5a>
  406f07:	89 f6                	mov    esi,esi
  406f09:	8d bc 27 00 00 00 00 	lea    edi,[edi+eiz*1+0x0]

00406f10 <_mbsrtowcs>:
  406f10:	55                   	push   ebp
  406f11:	57                   	push   edi
  406f12:	56                   	push   esi
  406f13:	53                   	push   ebx
  406f14:	83 ec 3c             	sub    esp,0x3c
  406f17:	8b 44 24 5c          	mov    eax,DWORD PTR [esp+0x5c]
  406f1b:	8b 5c 24 50          	mov    ebx,DWORD PTR [esp+0x50]
  406f1f:	8b 74 24 54          	mov    esi,DWORD PTR [esp+0x54]
  406f23:	8b 7c 24 58          	mov    edi,DWORD PTR [esp+0x58]
  406f27:	85 c0                	test   eax,eax
  406f29:	0f 84 41 01 00 00    	je     407070 <_mbsrtowcs+0x160>
  406f2f:	c7 44 24 04 00 00 00 	mov    DWORD PTR [esp+0x4],0x0
  406f36:	00 
  406f37:	c7 04 24 02 00 00 00 	mov    DWORD PTR [esp],0x2
  406f3e:	e8 d5 11 00 00       	call   408118 <_setlocale>
  406f43:	c7 44 24 04 2e 00 00 	mov    DWORD PTR [esp+0x4],0x2e
  406f4a:	00 
  406f4b:	89 04 24             	mov    DWORD PTR [esp],eax
  406f4e:	e8 05 12 00 00       	call   408158 <_strchr>
  406f53:	c7 44 24 18 00 00 00 	mov    DWORD PTR [esp+0x18],0x0
  406f5a:	00 
  406f5b:	85 c0                	test   eax,eax
  406f5d:	74 0f                	je     406f6e <_mbsrtowcs+0x5e>
  406f5f:	83 c0 01             	add    eax,0x1
  406f62:	89 04 24             	mov    DWORD PTR [esp],eax
  406f65:	e8 f6 11 00 00       	call   408160 <_atoi>
  406f6a:	89 44 24 18          	mov    DWORD PTR [esp+0x18],eax
  406f6e:	a1 b0 e1 40 00       	mov    eax,ds:0x40e1b0
  406f73:	85 f6                	test   esi,esi
  406f75:	8b 00                	mov    eax,DWORD PTR [eax]
  406f77:	89 44 24 1c          	mov    DWORD PTR [esp+0x1c],eax
  406f7b:	0f 84 df 00 00 00    	je     407060 <_mbsrtowcs+0x150>
  406f81:	8b 0e                	mov    ecx,DWORD PTR [esi]
  406f83:	85 c9                	test   ecx,ecx
  406f85:	0f 84 d5 00 00 00    	je     407060 <_mbsrtowcs+0x150>
  406f8b:	85 db                	test   ebx,ebx
  406f8d:	74 71                	je     407000 <_mbsrtowcs+0xf0>
  406f8f:	85 ff                	test   edi,edi
  406f91:	0f 84 c9 00 00 00    	je     407060 <_mbsrtowcs+0x150>
  406f97:	89 74 24 54          	mov    DWORD PTR [esp+0x54],esi
  406f9b:	31 ed                	xor    ebp,ebp
  406f9d:	89 de                	mov    esi,ebx
  406f9f:	8b 5c 24 54          	mov    ebx,DWORD PTR [esp+0x54]
  406fa3:	eb 0f                	jmp    406fb4 <_mbsrtowcs+0xa4>
  406fa5:	8b 0b                	mov    ecx,DWORD PTR [ebx]
  406fa7:	01 c5                	add    ebp,eax
  406fa9:	83 c6 02             	add    esi,0x2
  406fac:	01 c1                	add    ecx,eax
  406fae:	39 ef                	cmp    edi,ebp
  406fb0:	89 0b                	mov    DWORD PTR [ebx],ecx
  406fb2:	76 30                	jbe    406fe4 <_mbsrtowcs+0xd4>
  406fb4:	8b 44 24 1c          	mov    eax,DWORD PTR [esp+0x1c]
  406fb8:	89 4c 24 04          	mov    DWORD PTR [esp+0x4],ecx
  406fbc:	89 34 24             	mov    DWORD PTR [esp],esi
  406fbf:	89 44 24 14          	mov    DWORD PTR [esp+0x14],eax
  406fc3:	8b 44 24 18          	mov    eax,DWORD PTR [esp+0x18]
  406fc7:	89 44 24 10          	mov    DWORD PTR [esp+0x10],eax
  406fcb:	8b 44 24 5c          	mov    eax,DWORD PTR [esp+0x5c]
  406fcf:	89 44 24 0c          	mov    DWORD PTR [esp+0xc],eax
  406fd3:	89 f8                	mov    eax,edi
  406fd5:	29 e8                	sub    eax,ebp
  406fd7:	89 44 24 08          	mov    DWORD PTR [esp+0x8],eax
  406fdb:	e8 10 fd ff ff       	call   406cf0 <___mbrtowc_cp>
  406fe0:	85 c0                	test   eax,eax
  406fe2:	7f c1                	jg     406fa5 <_mbsrtowcs+0x95>
  406fe4:	85 c0                	test   eax,eax
  406fe6:	75 6e                	jne    407056 <_mbsrtowcs+0x146>
  406fe8:	39 fd                	cmp    ebp,edi
  406fea:	73 6a                	jae    407056 <_mbsrtowcs+0x146>
  406fec:	c7 03 00 00 00 00    	mov    DWORD PTR [ebx],0x0
  406ff2:	83 c4 3c             	add    esp,0x3c
  406ff5:	89 e8                	mov    eax,ebp
  406ff7:	5b                   	pop    ebx
  406ff8:	5e                   	pop    esi
  406ff9:	5f                   	pop    edi
  406ffa:	5d                   	pop    ebp
  406ffb:	c3                   	ret    
  406ffc:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  407000:	31 ed                	xor    ebp,ebp
  407002:	66 89 6c 24 2e       	mov    WORD PTR [esp+0x2e],bp
  407007:	31 ed                	xor    ebp,ebp
  407009:	85 ff                	test   edi,edi
  40700b:	74 49                	je     407056 <_mbsrtowcs+0x146>
  40700d:	89 7c 24 58          	mov    DWORD PTR [esp+0x58],edi
  407011:	8d 5c 24 2e          	lea    ebx,[esp+0x2e]
  407015:	89 f7                	mov    edi,esi
  407017:	8b 74 24 1c          	mov    esi,DWORD PTR [esp+0x1c]
  40701b:	eb 11                	jmp    40702e <_mbsrtowcs+0x11e>
  40701d:	8d 76 00             	lea    esi,[esi+0x0]
  407020:	8b 0f                	mov    ecx,DWORD PTR [edi]
  407022:	01 c5                	add    ebp,eax
  407024:	01 c1                	add    ecx,eax
  407026:	39 6c 24 58          	cmp    DWORD PTR [esp+0x58],ebp
  40702a:	89 0f                	mov    DWORD PTR [edi],ecx
  40702c:	76 28                	jbe    407056 <_mbsrtowcs+0x146>
  40702e:	8b 44 24 18          	mov    eax,DWORD PTR [esp+0x18]
  407032:	89 74 24 14          	mov    DWORD PTR [esp+0x14],esi
  407036:	89 74 24 08          	mov    DWORD PTR [esp+0x8],esi
  40703a:	89 4c 24 04          	mov    DWORD PTR [esp+0x4],ecx
  40703e:	89 44 24 10          	mov    DWORD PTR [esp+0x10],eax
  407042:	8b 44 24 5c          	mov    eax,DWORD PTR [esp+0x5c]
  407046:	89 1c 24             	mov    DWORD PTR [esp],ebx
  407049:	89 44 24 0c          	mov    DWORD PTR [esp+0xc],eax
  40704d:	e8 9e fc ff ff       	call   406cf0 <___mbrtowc_cp>
  407052:	85 c0                	test   eax,eax
  407054:	7f ca                	jg     407020 <_mbsrtowcs+0x110>
  407056:	83 c4 3c             	add    esp,0x3c
  407059:	89 e8                	mov    eax,ebp
  40705b:	5b                   	pop    ebx
  40705c:	5e                   	pop    esi
  40705d:	5f                   	pop    edi
  40705e:	5d                   	pop    ebp
  40705f:	c3                   	ret    
  407060:	83 c4 3c             	add    esp,0x3c
  407063:	31 c0                	xor    eax,eax
  407065:	5b                   	pop    ebx
  407066:	5e                   	pop    esi
  407067:	5f                   	pop    edi
  407068:	5d                   	pop    ebp
  407069:	c3                   	ret    
  40706a:	8d b6 00 00 00 00    	lea    esi,[esi+0x0]
  407070:	c7 44 24 5c 74 d0 40 	mov    DWORD PTR [esp+0x5c],0x40d074
  407077:	00 
  407078:	e9 b2 fe ff ff       	jmp    406f2f <_mbsrtowcs+0x1f>
  40707d:	8d 76 00             	lea    esi,[esi+0x0]

00407080 <_mbrlen>:
  407080:	53                   	push   ebx
  407081:	31 c0                	xor    eax,eax
  407083:	83 ec 38             	sub    esp,0x38
  407086:	66 89 44 24 2e       	mov    WORD PTR [esp+0x2e],ax
  40708b:	a1 b0 e1 40 00       	mov    eax,ds:0x40e1b0
  407090:	8b 18                	mov    ebx,DWORD PTR [eax]
  407092:	c7 44 24 04 00 00 00 	mov    DWORD PTR [esp+0x4],0x0
  407099:	00 
  40709a:	c7 04 24 02 00 00 00 	mov    DWORD PTR [esp],0x2
  4070a1:	e8 72 10 00 00       	call   408118 <_setlocale>
  4070a6:	c7 44 24 04 2e 00 00 	mov    DWORD PTR [esp+0x4],0x2e
  4070ad:	00 
  4070ae:	89 04 24             	mov    DWORD PTR [esp],eax
  4070b1:	e8 a2 10 00 00       	call   408158 <_strchr>
  4070b6:	31 c9                	xor    ecx,ecx
  4070b8:	85 c0                	test   eax,eax
  4070ba:	74 0d                	je     4070c9 <_mbrlen+0x49>
  4070bc:	83 c0 01             	add    eax,0x1
  4070bf:	89 04 24             	mov    DWORD PTR [esp],eax
  4070c2:	e8 99 10 00 00       	call   408160 <_atoi>
  4070c7:	89 c1                	mov    ecx,eax
  4070c9:	8b 54 24 48          	mov    edx,DWORD PTR [esp+0x48]
  4070cd:	85 d2                	test   edx,edx
  4070cf:	74 2f                	je     407100 <_mbrlen+0x80>
  4070d1:	8b 44 24 44          	mov    eax,DWORD PTR [esp+0x44]
  4070d5:	89 5c 24 14          	mov    DWORD PTR [esp+0x14],ebx
  4070d9:	89 4c 24 10          	mov    DWORD PTR [esp+0x10],ecx
  4070dd:	89 54 24 0c          	mov    DWORD PTR [esp+0xc],edx
  4070e1:	89 44 24 08          	mov    DWORD PTR [esp+0x8],eax
  4070e5:	8b 44 24 40          	mov    eax,DWORD PTR [esp+0x40]
  4070e9:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
  4070ed:	8d 44 24 2e          	lea    eax,[esp+0x2e]
  4070f1:	89 04 24             	mov    DWORD PTR [esp],eax
  4070f4:	e8 f7 fb ff ff       	call   406cf0 <___mbrtowc_cp>
  4070f9:	83 c4 38             	add    esp,0x38
  4070fc:	5b                   	pop    ebx
  4070fd:	c3                   	ret    
  4070fe:	66 90                	xchg   ax,ax
  407100:	ba 70 d0 40 00       	mov    edx,0x40d070
  407105:	eb ca                	jmp    4070d1 <_mbrlen+0x51>
  407107:	90                   	nop
  407108:	90                   	nop
  407109:	90                   	nop
  40710a:	90                   	nop
  40710b:	90                   	nop
  40710c:	90                   	nop
  40710d:	90                   	nop
  40710e:	90                   	nop
  40710f:	90                   	nop

00407110 <___rv_alloc_D2A>:
  407110:	53                   	push   ebx
  407111:	31 db                	xor    ebx,ebx
  407113:	83 ec 18             	sub    esp,0x18
  407116:	8b 4c 24 20          	mov    ecx,DWORD PTR [esp+0x20]
  40711a:	83 f9 13             	cmp    ecx,0x13
  40711d:	76 11                	jbe    407130 <___rv_alloc_D2A+0x20>
  40711f:	b8 04 00 00 00       	mov    eax,0x4
  407124:	01 c0                	add    eax,eax
  407126:	83 c3 01             	add    ebx,0x1
  407129:	8d 50 10             	lea    edx,[eax+0x10]
  40712c:	39 ca                	cmp    edx,ecx
  40712e:	76 f4                	jbe    407124 <___rv_alloc_D2A+0x14>
  407130:	89 1c 24             	mov    DWORD PTR [esp],ebx
  407133:	e8 a8 03 00 00       	call   4074e0 <___Balloc_D2A>
  407138:	89 18                	mov    DWORD PTR [eax],ebx
  40713a:	83 c4 18             	add    esp,0x18
  40713d:	83 c0 04             	add    eax,0x4
  407140:	5b                   	pop    ebx
  407141:	c3                   	ret    
  407142:	8d b4 26 00 00 00 00 	lea    esi,[esi+eiz*1+0x0]
  407149:	8d bc 27 00 00 00 00 	lea    edi,[edi+eiz*1+0x0]

00407150 <___nrv_alloc_D2A>:
  407150:	56                   	push   esi
  407151:	53                   	push   ebx
  407152:	83 ec 14             	sub    esp,0x14
  407155:	8b 44 24 28          	mov    eax,DWORD PTR [esp+0x28]
  407159:	8b 5c 24 20          	mov    ebx,DWORD PTR [esp+0x20]
  40715d:	8b 74 24 24          	mov    esi,DWORD PTR [esp+0x24]
  407161:	89 04 24             	mov    DWORD PTR [esp],eax
  407164:	e8 a7 ff ff ff       	call   407110 <___rv_alloc_D2A>
  407169:	0f b6 13             	movzx  edx,BYTE PTR [ebx]
  40716c:	8d 4b 01             	lea    ecx,[ebx+0x1]
  40716f:	84 d2                	test   dl,dl
  407171:	88 10                	mov    BYTE PTR [eax],dl
  407173:	89 c2                	mov    edx,eax
  407175:	74 10                	je     407187 <___nrv_alloc_D2A+0x37>
  407177:	83 c1 01             	add    ecx,0x1
  40717a:	0f b6 59 ff          	movzx  ebx,BYTE PTR [ecx-0x1]
  40717e:	83 c2 01             	add    edx,0x1
  407181:	84 db                	test   bl,bl
  407183:	88 1a                	mov    BYTE PTR [edx],bl
  407185:	75 f0                	jne    407177 <___nrv_alloc_D2A+0x27>
  407187:	85 f6                	test   esi,esi
  407189:	74 02                	je     40718d <___nrv_alloc_D2A+0x3d>
  40718b:	89 16                	mov    DWORD PTR [esi],edx
  40718d:	83 c4 14             	add    esp,0x14
  407190:	5b                   	pop    ebx
  407191:	5e                   	pop    esi
  407192:	c3                   	ret    
  407193:	8d b6 00 00 00 00    	lea    esi,[esi+0x0]
  407199:	8d bc 27 00 00 00 00 	lea    edi,[edi+eiz*1+0x0]

004071a0 <___freedtoa>:
  4071a0:	8b 44 24 04          	mov    eax,DWORD PTR [esp+0x4]
  4071a4:	ba 01 00 00 00       	mov    edx,0x1
  4071a9:	8b 48 fc             	mov    ecx,DWORD PTR [eax-0x4]
  4071ac:	83 e8 04             	sub    eax,0x4
  4071af:	d3 e2                	shl    edx,cl
  4071b1:	89 48 04             	mov    DWORD PTR [eax+0x4],ecx
  4071b4:	89 50 08             	mov    DWORD PTR [eax+0x8],edx
  4071b7:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
  4071bb:	e9 f0 03 00 00       	jmp    4075b0 <___Bfree_D2A>

004071c0 <___quorem_D2A>:
  4071c0:	55                   	push   ebp
  4071c1:	57                   	push   edi
  4071c2:	56                   	push   esi
  4071c3:	53                   	push   ebx
  4071c4:	83 ec 4c             	sub    esp,0x4c
  4071c7:	8b 44 24 64          	mov    eax,DWORD PTR [esp+0x64]
  4071cb:	8b 7c 24 60          	mov    edi,DWORD PTR [esp+0x60]
  4071cf:	8b 50 10             	mov    edx,DWORD PTR [eax+0x10]
  4071d2:	31 c0                	xor    eax,eax
  4071d4:	3b 57 10             	cmp    edx,DWORD PTR [edi+0x10]
  4071d7:	0f 8f d6 01 00 00    	jg     4073b3 <___quorem_D2A+0x1f3>
  4071dd:	8b 44 24 64          	mov    eax,DWORD PTR [esp+0x64]
  4071e1:	8b 74 24 60          	mov    esi,DWORD PTR [esp+0x60]
  4071e5:	83 c0 14             	add    eax,0x14
  4071e8:	89 c7                	mov    edi,eax
  4071ea:	89 44 24 38          	mov    DWORD PTR [esp+0x38],eax
  4071ee:	8d 42 ff             	lea    eax,[edx-0x1]
  4071f1:	31 d2                	xor    edx,edx
  4071f3:	89 44 24 30          	mov    DWORD PTR [esp+0x30],eax
  4071f7:	c1 e0 02             	shl    eax,0x2
  4071fa:	01 c7                	add    edi,eax
  4071fc:	8d 5e 14             	lea    ebx,[esi+0x14]
  4071ff:	01 d8                	add    eax,ebx
  407201:	89 7c 24 28          	mov    DWORD PTR [esp+0x28],edi
  407205:	8b 3f                	mov    edi,DWORD PTR [edi]
  407207:	89 44 24 3c          	mov    DWORD PTR [esp+0x3c],eax
  40720b:	8b 00                	mov    eax,DWORD PTR [eax]
  40720d:	89 5c 24 2c          	mov    DWORD PTR [esp+0x2c],ebx
  407211:	8d 4f 01             	lea    ecx,[edi+0x1]
  407214:	f7 f1                	div    ecx
  407216:	89 7c 24 10          	mov    DWORD PTR [esp+0x10],edi
  40721a:	85 c0                	test   eax,eax
  40721c:	89 c5                	mov    ebp,eax
  40721e:	89 44 24 34          	mov    DWORD PTR [esp+0x34],eax
  407222:	0f 84 c7 00 00 00    	je     4072ef <___quorem_D2A+0x12f>
  407228:	8b 7c 24 38          	mov    edi,DWORD PTR [esp+0x38]
  40722c:	89 de                	mov    esi,ebx
  40722e:	c7 44 24 20 00 00 00 	mov    DWORD PTR [esp+0x20],0x0
  407235:	00 
  407236:	c7 44 24 24 00 00 00 	mov    DWORD PTR [esp+0x24],0x0
  40723d:	00 
  40723e:	c7 44 24 10 00 00 00 	mov    DWORD PTR [esp+0x10],0x0
  407245:	00 
  407246:	c7 44 24 14 00 00 00 	mov    DWORD PTR [esp+0x14],0x0
  40724d:	00 
  40724e:	66 90                	xchg   ax,ax
  407250:	83 c7 04             	add    edi,0x4
  407253:	89 e8                	mov    eax,ebp
  407255:	f7 67 fc             	mul    DWORD PTR [edi-0x4]
  407258:	03 44 24 20          	add    eax,DWORD PTR [esp+0x20]
  40725c:	13 54 24 24          	adc    edx,DWORD PTR [esp+0x24]
  407260:	c7 44 24 1c 00 00 00 	mov    DWORD PTR [esp+0x1c],0x0
  407267:	00 
  407268:	89 44 24 18          	mov    DWORD PTR [esp+0x18],eax
  40726c:	89 d3                	mov    ebx,edx
  40726e:	89 d9                	mov    ecx,ebx
  407270:	31 db                	xor    ebx,ebx
  407272:	89 4c 24 20          	mov    DWORD PTR [esp+0x20],ecx
  407276:	8b 0e                	mov    ecx,DWORD PTR [esi]
  407278:	89 5c 24 24          	mov    DWORD PTR [esp+0x24],ebx
  40727c:	31 db                	xor    ebx,ebx
  40727e:	2b 4c 24 18          	sub    ecx,DWORD PTR [esp+0x18]
  407282:	1b 5c 24 1c          	sbb    ebx,DWORD PTR [esp+0x1c]
  407286:	2b 4c 24 10          	sub    ecx,DWORD PTR [esp+0x10]
  40728a:	1b 5c 24 14          	sbb    ebx,DWORD PTR [esp+0x14]
  40728e:	83 c6 04             	add    esi,0x4
  407291:	c7 44 24 14 00 00 00 	mov    DWORD PTR [esp+0x14],0x0
  407298:	00 
  407299:	89 d8                	mov    eax,ebx
  40729b:	83 e0 01             	and    eax,0x1
  40729e:	39 7c 24 28          	cmp    DWORD PTR [esp+0x28],edi
  4072a2:	89 44 24 10          	mov    DWORD PTR [esp+0x10],eax
  4072a6:	89 4e fc             	mov    DWORD PTR [esi-0x4],ecx
  4072a9:	73 a5                	jae    407250 <___quorem_D2A+0x90>
  4072ab:	8b 44 24 3c          	mov    eax,DWORD PTR [esp+0x3c]
  4072af:	8b 38                	mov    edi,DWORD PTR [eax]
  4072b1:	85 ff                	test   edi,edi
  4072b3:	75 3a                	jne    4072ef <___quorem_D2A+0x12f>
  4072b5:	8b 4c 24 2c          	mov    ecx,DWORD PTR [esp+0x2c]
  4072b9:	89 c6                	mov    esi,eax
  4072bb:	83 e8 04             	sub    eax,0x4
  4072be:	39 c1                	cmp    ecx,eax
  4072c0:	73 22                	jae    4072e4 <___quorem_D2A+0x124>
  4072c2:	8b 76 fc             	mov    esi,DWORD PTR [esi-0x4]
  4072c5:	85 f6                	test   esi,esi
  4072c7:	75 1b                	jne    4072e4 <___quorem_D2A+0x124>
  4072c9:	8b 54 24 30          	mov    edx,DWORD PTR [esp+0x30]
  4072cd:	eb 07                	jmp    4072d6 <___quorem_D2A+0x116>
  4072cf:	90                   	nop
  4072d0:	8b 18                	mov    ebx,DWORD PTR [eax]
  4072d2:	85 db                	test   ebx,ebx
  4072d4:	75 0a                	jne    4072e0 <___quorem_D2A+0x120>
  4072d6:	83 e8 04             	sub    eax,0x4
  4072d9:	83 ea 01             	sub    edx,0x1
  4072dc:	39 c1                	cmp    ecx,eax
  4072de:	72 f0                	jb     4072d0 <___quorem_D2A+0x110>
  4072e0:	89 54 24 30          	mov    DWORD PTR [esp+0x30],edx
  4072e4:	8b 44 24 60          	mov    eax,DWORD PTR [esp+0x60]
  4072e8:	8b 7c 24 30          	mov    edi,DWORD PTR [esp+0x30]
  4072ec:	89 78 10             	mov    DWORD PTR [eax+0x10],edi
  4072ef:	8b 44 24 64          	mov    eax,DWORD PTR [esp+0x64]
  4072f3:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
  4072f7:	8b 44 24 60          	mov    eax,DWORD PTR [esp+0x60]
  4072fb:	89 04 24             	mov    DWORD PTR [esp],eax
  4072fe:	e8 2d 08 00 00       	call   407b30 <___cmp_D2A>
  407303:	85 c0                	test   eax,eax
  407305:	0f 88 a4 00 00 00    	js     4073af <___quorem_D2A+0x1ef>
  40730b:	31 f6                	xor    esi,esi
  40730d:	31 ff                	xor    edi,edi
  40730f:	8d 45 01             	lea    eax,[ebp+0x1]
  407312:	8b 6c 24 2c          	mov    ebp,DWORD PTR [esp+0x2c]
  407316:	89 74 24 10          	mov    DWORD PTR [esp+0x10],esi
  40731a:	8b 74 24 38          	mov    esi,DWORD PTR [esp+0x38]
  40731e:	89 7c 24 14          	mov    DWORD PTR [esp+0x14],edi
  407322:	8b 7c 24 28          	mov    edi,DWORD PTR [esp+0x28]
  407326:	89 44 24 34          	mov    DWORD PTR [esp+0x34],eax
  40732a:	8d b6 00 00 00 00    	lea    esi,[esi+0x0]
  407330:	83 c6 04             	add    esi,0x4
  407333:	8b 45 00             	mov    eax,DWORD PTR [ebp+0x0]
  407336:	31 db                	xor    ebx,ebx
  407338:	8b 4e fc             	mov    ecx,DWORD PTR [esi-0x4]
  40733b:	31 d2                	xor    edx,edx
  40733d:	29 c8                	sub    eax,ecx
  40733f:	19 da                	sbb    edx,ebx
  407341:	2b 44 24 10          	sub    eax,DWORD PTR [esp+0x10]
  407345:	1b 54 24 14          	sbb    edx,DWORD PTR [esp+0x14]
  407349:	83 c5 04             	add    ebp,0x4
  40734c:	c7 44 24 14 00 00 00 	mov    DWORD PTR [esp+0x14],0x0
  407353:	00 
  407354:	89 d3                	mov    ebx,edx
  407356:	83 e3 01             	and    ebx,0x1
  407359:	39 f7                	cmp    edi,esi
  40735b:	89 5c 24 10          	mov    DWORD PTR [esp+0x10],ebx
  40735f:	89 45 fc             	mov    DWORD PTR [ebp-0x4],eax
  407362:	73 cc                	jae    407330 <___quorem_D2A+0x170>
  407364:	8b 44 24 2c          	mov    eax,DWORD PTR [esp+0x2c]
  407368:	8b 5c 24 30          	mov    ebx,DWORD PTR [esp+0x30]
  40736c:	8d 14 98             	lea    edx,[eax+ebx*4]
  40736f:	8b 3a                	mov    edi,DWORD PTR [edx]
  407371:	85 ff                	test   edi,edi
  407373:	75 3a                	jne    4073af <___quorem_D2A+0x1ef>
  407375:	8b 4c 24 2c          	mov    ecx,DWORD PTR [esp+0x2c]
  407379:	8d 42 fc             	lea    eax,[edx-0x4]
  40737c:	39 c1                	cmp    ecx,eax
  40737e:	73 24                	jae    4073a4 <___quorem_D2A+0x1e4>
  407380:	8b 72 fc             	mov    esi,DWORD PTR [edx-0x4]
  407383:	85 f6                	test   esi,esi
  407385:	75 1d                	jne    4073a4 <___quorem_D2A+0x1e4>
  407387:	89 da                	mov    edx,ebx
  407389:	eb 0b                	jmp    407396 <___quorem_D2A+0x1d6>
  40738b:	90                   	nop
  40738c:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  407390:	8b 18                	mov    ebx,DWORD PTR [eax]
  407392:	85 db                	test   ebx,ebx
  407394:	75 0a                	jne    4073a0 <___quorem_D2A+0x1e0>
  407396:	83 e8 04             	sub    eax,0x4
  407399:	83 ea 01             	sub    edx,0x1
  40739c:	39 c1                	cmp    ecx,eax
  40739e:	72 f0                	jb     407390 <___quorem_D2A+0x1d0>
  4073a0:	89 54 24 30          	mov    DWORD PTR [esp+0x30],edx
  4073a4:	8b 44 24 60          	mov    eax,DWORD PTR [esp+0x60]
  4073a8:	8b 7c 24 30          	mov    edi,DWORD PTR [esp+0x30]
  4073ac:	89 78 10             	mov    DWORD PTR [eax+0x10],edi
  4073af:	8b 44 24 34          	mov    eax,DWORD PTR [esp+0x34]
  4073b3:	83 c4 4c             	add    esp,0x4c
  4073b6:	5b                   	pop    ebx
  4073b7:	5e                   	pop    esi
  4073b8:	5f                   	pop    edi
  4073b9:	5d                   	pop    ebp
  4073ba:	c3                   	ret    
  4073bb:	90                   	nop
  4073bc:	90                   	nop
  4073bd:	90                   	nop
  4073be:	90                   	nop
  4073bf:	90                   	nop

004073c0 <_dtoa_lock>:
  4073c0:	55                   	push   ebp
  4073c1:	89 e5                	mov    ebp,esp
  4073c3:	53                   	push   ebx
  4073c4:	89 c3                	mov    ebx,eax
  4073c6:	83 ec 14             	sub    esp,0x14
  4073c9:	8b 15 c8 d9 40 00    	mov    edx,DWORD PTR ds:0x40d9c8
  4073cf:	83 fa 02             	cmp    edx,0x2
  4073d2:	74 7f                	je     407453 <_dtoa_lock+0x93>
  4073d4:	85 d2                	test   edx,edx
  4073d6:	75 1d                	jne    4073f5 <_dtoa_lock+0x35>
  4073d8:	eb 2a                	jmp    407404 <_dtoa_lock+0x44>
  4073da:	8d b6 00 00 00 00    	lea    esi,[esi+0x0]
  4073e0:	c7 04 24 01 00 00 00 	mov    DWORD PTR [esp],0x1
  4073e7:	e8 14 0e 00 00       	call   408200 <_Sleep@4>
  4073ec:	83 ec 04             	sub    esp,0x4
  4073ef:	8b 15 c8 d9 40 00    	mov    edx,DWORD PTR ds:0x40d9c8
  4073f5:	83 fa 01             	cmp    edx,0x1
  4073f8:	74 e6                	je     4073e0 <_dtoa_lock+0x20>
  4073fa:	83 fa 02             	cmp    edx,0x2
  4073fd:	74 54                	je     407453 <_dtoa_lock+0x93>
  4073ff:	8b 5d fc             	mov    ebx,DWORD PTR [ebp-0x4]
  407402:	c9                   	leave  
  407403:	c3                   	ret    
  407404:	c7 44 24 04 01 00 00 	mov    DWORD PTR [esp+0x4],0x1
  40740b:	00 
  40740c:	c7 04 24 c8 d9 40 00 	mov    DWORD PTR [esp],0x40d9c8
  407413:	e8 f0 0d 00 00       	call   408208 <_InterlockedExchange@8>
  407418:	83 ec 08             	sub    esp,0x8
  40741b:	85 c0                	test   eax,eax
  40741d:	75 51                	jne    407470 <_dtoa_lock+0xb0>
  40741f:	c7 04 24 e0 d9 40 00 	mov    DWORD PTR [esp],0x40d9e0
  407426:	e8 9d 0d 00 00       	call   4081c8 <_InitializeCriticalSection@4>
  40742b:	83 ec 04             	sub    esp,0x4
  40742e:	c7 04 24 f8 d9 40 00 	mov    DWORD PTR [esp],0x40d9f8
  407435:	e8 8e 0d 00 00       	call   4081c8 <_InitializeCriticalSection@4>
  40743a:	83 ec 04             	sub    esp,0x4
  40743d:	c7 04 24 90 74 40 00 	mov    DWORD PTR [esp],0x407490
  407444:	e8 97 9e ff ff       	call   4012e0 <_atexit>
  407449:	c7 05 c8 d9 40 00 02 	mov    DWORD PTR ds:0x40d9c8,0x2
  407450:	00 00 00 
  407453:	8d 04 5b             	lea    eax,[ebx+ebx*2]
  407456:	8d 04 c5 e0 d9 40 00 	lea    eax,[eax*8+0x40d9e0]
  40745d:	89 04 24             	mov    DWORD PTR [esp],eax
  407460:	e8 3b 0d 00 00       	call   4081a0 <_EnterCriticalSection@4>
  407465:	8b 5d fc             	mov    ebx,DWORD PTR [ebp-0x4]
  407468:	83 ec 04             	sub    esp,0x4
  40746b:	c9                   	leave  
  40746c:	c3                   	ret    
  40746d:	8d 76 00             	lea    esi,[esi+0x0]
  407470:	83 f8 02             	cmp    eax,0x2
  407473:	0f 85 76 ff ff ff    	jne    4073ef <_dtoa_lock+0x2f>
  407479:	c7 05 c8 d9 40 00 02 	mov    DWORD PTR ds:0x40d9c8,0x2
  407480:	00 00 00 
  407483:	eb ce                	jmp    407453 <_dtoa_lock+0x93>
  407485:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  407489:	8d bc 27 00 00 00 00 	lea    edi,[edi+eiz*1+0x0]

00407490 <_dtoa_lock_cleanup>:
  407490:	55                   	push   ebp
  407491:	89 e5                	mov    ebp,esp
  407493:	83 ec 18             	sub    esp,0x18
  407496:	c7 44 24 04 03 00 00 	mov    DWORD PTR [esp+0x4],0x3
  40749d:	00 
  40749e:	c7 04 24 c8 d9 40 00 	mov    DWORD PTR [esp],0x40d9c8
  4074a5:	e8 5e 0d 00 00       	call   408208 <_InterlockedExchange@8>
  4074aa:	83 ec 08             	sub    esp,0x8
  4074ad:	83 f8 02             	cmp    eax,0x2
  4074b0:	74 02                	je     4074b4 <_dtoa_lock_cleanup+0x24>
  4074b2:	c9                   	leave  
  4074b3:	c3                   	ret    
  4074b4:	c7 04 24 e0 d9 40 00 	mov    DWORD PTR [esp],0x40d9e0
  4074bb:	e8 00 0d 00 00       	call   4081c0 <_DeleteCriticalSection@4>
  4074c0:	83 ec 04             	sub    esp,0x4
  4074c3:	c7 04 24 f8 d9 40 00 	mov    DWORD PTR [esp],0x40d9f8
  4074ca:	e8 f1 0c 00 00       	call   4081c0 <_DeleteCriticalSection@4>
  4074cf:	83 ec 04             	sub    esp,0x4
  4074d2:	c9                   	leave  
  4074d3:	c3                   	ret    
  4074d4:	8d b6 00 00 00 00    	lea    esi,[esi+0x0]
  4074da:	8d bf 00 00 00 00    	lea    edi,[edi+0x0]

004074e0 <___Balloc_D2A>:
  4074e0:	55                   	push   ebp
  4074e1:	31 c0                	xor    eax,eax
  4074e3:	89 e5                	mov    ebp,esp
  4074e5:	57                   	push   edi
  4074e6:	56                   	push   esi
  4074e7:	53                   	push   ebx
  4074e8:	83 ec 1c             	sub    esp,0x1c
  4074eb:	8b 75 08             	mov    esi,DWORD PTR [ebp+0x8]
  4074ee:	e8 cd fe ff ff       	call   4073c0 <_dtoa_lock>
  4074f3:	83 fe 09             	cmp    esi,0x9
  4074f6:	7f 2e                	jg     407526 <___Balloc_D2A+0x46>
  4074f8:	8b 1c b5 a0 d9 40 00 	mov    ebx,DWORD PTR [esi*4+0x40d9a0]
  4074ff:	85 db                	test   ebx,ebx
  407501:	74 6e                	je     407571 <___Balloc_D2A+0x91>
  407503:	8b 03                	mov    eax,DWORD PTR [ebx]
  407505:	83 3d c8 d9 40 00 02 	cmp    DWORD PTR ds:0x40d9c8,0x2
  40750c:	89 04 b5 a0 d9 40 00 	mov    DWORD PTR [esi*4+0x40d9a0],eax
  407513:	75 44                	jne    407559 <___Balloc_D2A+0x79>
  407515:	c7 04 24 e0 d9 40 00 	mov    DWORD PTR [esp],0x40d9e0
  40751c:	e8 97 0c 00 00       	call   4081b8 <_LeaveCriticalSection@4>
  407521:	83 ec 04             	sub    esp,0x4
  407524:	eb 33                	jmp    407559 <___Balloc_D2A+0x79>
  407526:	bf 01 00 00 00       	mov    edi,0x1
  40752b:	89 f1                	mov    ecx,esi
  40752d:	d3 e7                	shl    edi,cl
  40752f:	8d 04 bd 1b 00 00 00 	lea    eax,[edi*4+0x1b]
  407536:	c1 e8 03             	shr    eax,0x3
  407539:	c1 e0 03             	shl    eax,0x3
  40753c:	89 04 24             	mov    DWORD PTR [esp],eax
  40753f:	e8 ac 0b 00 00       	call   4080f0 <_malloc>
  407544:	85 c0                	test   eax,eax
  407546:	89 c3                	mov    ebx,eax
  407548:	74 5f                	je     4075a9 <___Balloc_D2A+0xc9>
  40754a:	83 3d c8 d9 40 00 02 	cmp    DWORD PTR ds:0x40d9c8,0x2
  407551:	89 73 04             	mov    DWORD PTR [ebx+0x4],esi
  407554:	89 7b 08             	mov    DWORD PTR [ebx+0x8],edi
  407557:	74 bc                	je     407515 <___Balloc_D2A+0x35>
  407559:	c7 43 10 00 00 00 00 	mov    DWORD PTR [ebx+0x10],0x0
  407560:	89 d8                	mov    eax,ebx
  407562:	c7 43 0c 00 00 00 00 	mov    DWORD PTR [ebx+0xc],0x0
  407569:	8d 65 f4             	lea    esp,[ebp-0xc]
  40756c:	5b                   	pop    ebx
  40756d:	5e                   	pop    esi
  40756e:	5f                   	pop    edi
  40756f:	5d                   	pop    ebp
  407570:	c3                   	ret    
  407571:	8b 1d 20 90 40 00    	mov    ebx,DWORD PTR ds:0x409020
  407577:	bf 01 00 00 00       	mov    edi,0x1
  40757c:	89 f1                	mov    ecx,esi
  40757e:	d3 e7                	shl    edi,cl
  407580:	8d 04 bd 1b 00 00 00 	lea    eax,[edi*4+0x1b]
  407587:	c1 e8 03             	shr    eax,0x3
  40758a:	89 da                	mov    edx,ebx
  40758c:	81 ea a0 d0 40 00    	sub    edx,0x40d0a0
  407592:	c1 fa 03             	sar    edx,0x3
  407595:	01 c2                	add    edx,eax
  407597:	81 fa 20 01 00 00    	cmp    edx,0x120
  40759d:	77 9a                	ja     407539 <___Balloc_D2A+0x59>
  40759f:	8d 04 c3             	lea    eax,[ebx+eax*8]
  4075a2:	a3 20 90 40 00       	mov    ds:0x409020,eax
  4075a7:	eb a1                	jmp    40754a <___Balloc_D2A+0x6a>
  4075a9:	31 c0                	xor    eax,eax
  4075ab:	eb bc                	jmp    407569 <___Balloc_D2A+0x89>
  4075ad:	8d 76 00             	lea    esi,[esi+0x0]

004075b0 <___Bfree_D2A>:
  4075b0:	55                   	push   ebp
  4075b1:	89 e5                	mov    ebp,esp
  4075b3:	53                   	push   ebx
  4075b4:	83 ec 14             	sub    esp,0x14
  4075b7:	8b 5d 08             	mov    ebx,DWORD PTR [ebp+0x8]
  4075ba:	85 db                	test   ebx,ebx
  4075bc:	74 29                	je     4075e7 <___Bfree_D2A+0x37>
  4075be:	83 7b 04 09          	cmp    DWORD PTR [ebx+0x4],0x9
  4075c2:	7f 2c                	jg     4075f0 <___Bfree_D2A+0x40>
  4075c4:	31 c0                	xor    eax,eax
  4075c6:	e8 f5 fd ff ff       	call   4073c0 <_dtoa_lock>
  4075cb:	8b 43 04             	mov    eax,DWORD PTR [ebx+0x4]
  4075ce:	83 3d c8 d9 40 00 02 	cmp    DWORD PTR ds:0x40d9c8,0x2
  4075d5:	8b 14 85 a0 d9 40 00 	mov    edx,DWORD PTR [eax*4+0x40d9a0]
  4075dc:	89 1c 85 a0 d9 40 00 	mov    DWORD PTR [eax*4+0x40d9a0],ebx
  4075e3:	89 13                	mov    DWORD PTR [ebx],edx
  4075e5:	74 19                	je     407600 <___Bfree_D2A+0x50>
  4075e7:	8b 5d fc             	mov    ebx,DWORD PTR [ebp-0x4]
  4075ea:	c9                   	leave  
  4075eb:	c3                   	ret    
  4075ec:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  4075f0:	8b 5d fc             	mov    ebx,DWORD PTR [ebp-0x4]
  4075f3:	c9                   	leave  
  4075f4:	e9 ef 0a 00 00       	jmp    4080e8 <_free>
  4075f9:	8d b4 26 00 00 00 00 	lea    esi,[esi+eiz*1+0x0]
  407600:	c7 04 24 e0 d9 40 00 	mov    DWORD PTR [esp],0x40d9e0
  407607:	e8 ac 0b 00 00       	call   4081b8 <_LeaveCriticalSection@4>
  40760c:	8b 5d fc             	mov    ebx,DWORD PTR [ebp-0x4]
  40760f:	83 ec 04             	sub    esp,0x4
  407612:	c9                   	leave  
  407613:	c3                   	ret    
  407614:	8d b6 00 00 00 00    	lea    esi,[esi+0x0]
  40761a:	8d bf 00 00 00 00    	lea    edi,[edi+0x0]

00407620 <___multadd_D2A>:
  407620:	55                   	push   ebp
  407621:	31 c9                	xor    ecx,ecx
  407623:	57                   	push   edi
  407624:	56                   	push   esi
  407625:	53                   	push   ebx
  407626:	83 ec 2c             	sub    esp,0x2c
  407629:	8b 44 24 40          	mov    eax,DWORD PTR [esp+0x40]
  40762d:	8b 7c 24 48          	mov    edi,DWORD PTR [esp+0x48]
  407631:	8b 40 10             	mov    eax,DWORD PTR [eax+0x10]
  407634:	89 fd                	mov    ebp,edi
  407636:	c1 fd 1f             	sar    ebp,0x1f
  407639:	89 44 24 1c          	mov    DWORD PTR [esp+0x1c],eax
  40763d:	8b 44 24 40          	mov    eax,DWORD PTR [esp+0x40]
  407641:	8d 58 14             	lea    ebx,[eax+0x14]
  407644:	8b 44 24 44          	mov    eax,DWORD PTR [esp+0x44]
  407648:	89 44 24 10          	mov    DWORD PTR [esp+0x10],eax
  40764c:	c1 f8 1f             	sar    eax,0x1f
  40764f:	89 44 24 14          	mov    DWORD PTR [esp+0x14],eax
  407653:	8b 04 8b             	mov    eax,DWORD PTR [ebx+ecx*4]
  407656:	8b 74 24 14          	mov    esi,DWORD PTR [esp+0x14]
  40765a:	0f af f0             	imul   esi,eax
  40765d:	f7 64 24 10          	mul    DWORD PTR [esp+0x10]
  407661:	01 f2                	add    edx,esi
  407663:	01 f8                	add    eax,edi
  407665:	11 ea                	adc    edx,ebp
  407667:	89 d5                	mov    ebp,edx
  407669:	89 ef                	mov    edi,ebp
  40766b:	31 ed                	xor    ebp,ebp
  40766d:	89 04 8b             	mov    DWORD PTR [ebx+ecx*4],eax
  407670:	83 c1 01             	add    ecx,0x1
  407673:	39 4c 24 1c          	cmp    DWORD PTR [esp+0x1c],ecx
  407677:	7f da                	jg     407653 <___multadd_D2A+0x33>
  407679:	89 ea                	mov    edx,ebp
  40767b:	8b 44 24 40          	mov    eax,DWORD PTR [esp+0x40]
  40767f:	09 fa                	or     edx,edi
  407681:	74 1d                	je     4076a0 <___multadd_D2A+0x80>
  407683:	8b 54 24 1c          	mov    edx,DWORD PTR [esp+0x1c]
  407687:	3b 50 08             	cmp    edx,DWORD PTR [eax+0x8]
  40768a:	7d 1c                	jge    4076a8 <___multadd_D2A+0x88>
  40768c:	8b 54 24 40          	mov    edx,DWORD PTR [esp+0x40]
  407690:	8b 44 24 1c          	mov    eax,DWORD PTR [esp+0x1c]
  407694:	89 7c 82 14          	mov    DWORD PTR [edx+eax*4+0x14],edi
  407698:	83 c0 01             	add    eax,0x1
  40769b:	89 42 10             	mov    DWORD PTR [edx+0x10],eax
  40769e:	89 d0                	mov    eax,edx
  4076a0:	83 c4 2c             	add    esp,0x2c
  4076a3:	5b                   	pop    ebx
  4076a4:	5e                   	pop    esi
  4076a5:	5f                   	pop    edi
  4076a6:	5d                   	pop    ebp
  4076a7:	c3                   	ret    
  4076a8:	8b 40 04             	mov    eax,DWORD PTR [eax+0x4]
  4076ab:	89 44 24 10          	mov    DWORD PTR [esp+0x10],eax
  4076af:	83 c0 01             	add    eax,0x1
  4076b2:	89 04 24             	mov    DWORD PTR [esp],eax
  4076b5:	e8 26 fe ff ff       	call   4074e0 <___Balloc_D2A>
  4076ba:	85 c0                	test   eax,eax
  4076bc:	89 c3                	mov    ebx,eax
  4076be:	74 3a                	je     4076fa <___multadd_D2A+0xda>
  4076c0:	8d 48 0c             	lea    ecx,[eax+0xc]
  4076c3:	8b 44 24 40          	mov    eax,DWORD PTR [esp+0x40]
  4076c7:	8b 40 10             	mov    eax,DWORD PTR [eax+0x10]
  4076ca:	89 0c 24             	mov    DWORD PTR [esp],ecx
  4076cd:	8d 14 85 08 00 00 00 	lea    edx,[eax*4+0x8]
  4076d4:	8b 44 24 40          	mov    eax,DWORD PTR [esp+0x40]
  4076d8:	89 54 24 08          	mov    DWORD PTR [esp+0x8],edx
  4076dc:	83 c0 0c             	add    eax,0xc
  4076df:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
  4076e3:	e8 f0 09 00 00       	call   4080d8 <_memcpy>
  4076e8:	8b 44 24 40          	mov    eax,DWORD PTR [esp+0x40]
  4076ec:	89 04 24             	mov    DWORD PTR [esp],eax
  4076ef:	e8 bc fe ff ff       	call   4075b0 <___Bfree_D2A>
  4076f4:	89 5c 24 40          	mov    DWORD PTR [esp+0x40],ebx
  4076f8:	eb 92                	jmp    40768c <___multadd_D2A+0x6c>
  4076fa:	31 c0                	xor    eax,eax
  4076fc:	eb a2                	jmp    4076a0 <___multadd_D2A+0x80>
  4076fe:	66 90                	xchg   ax,ax

00407700 <___i2b_D2A>:
  407700:	83 ec 1c             	sub    esp,0x1c
  407703:	c7 04 24 01 00 00 00 	mov    DWORD PTR [esp],0x1
  40770a:	e8 d1 fd ff ff       	call   4074e0 <___Balloc_D2A>
  40770f:	85 c0                	test   eax,eax
  407711:	74 0e                	je     407721 <___i2b_D2A+0x21>
  407713:	8b 54 24 20          	mov    edx,DWORD PTR [esp+0x20]
  407717:	c7 40 10 01 00 00 00 	mov    DWORD PTR [eax+0x10],0x1
  40771e:	89 50 14             	mov    DWORD PTR [eax+0x14],edx
  407721:	83 c4 1c             	add    esp,0x1c
  407724:	c3                   	ret    
  407725:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  407729:	8d bc 27 00 00 00 00 	lea    edi,[edi+eiz*1+0x0]

00407730 <___mult_D2A>:
  407730:	55                   	push   ebp
  407731:	57                   	push   edi
  407732:	56                   	push   esi
  407733:	53                   	push   ebx
  407734:	83 ec 3c             	sub    esp,0x3c
  407737:	8b 7c 24 50          	mov    edi,DWORD PTR [esp+0x50]
  40773b:	8b 6c 24 54          	mov    ebp,DWORD PTR [esp+0x54]
  40773f:	8b 77 10             	mov    esi,DWORD PTR [edi+0x10]
  407742:	8b 5d 10             	mov    ebx,DWORD PTR [ebp+0x10]
  407745:	39 de                	cmp    esi,ebx
  407747:	7d 0c                	jge    407755 <___mult_D2A+0x25>
  407749:	89 f0                	mov    eax,esi
  40774b:	89 de                	mov    esi,ebx
  40774d:	89 c3                	mov    ebx,eax
  40774f:	89 f8                	mov    eax,edi
  407751:	89 ef                	mov    edi,ebp
  407753:	89 c5                	mov    ebp,eax
  407755:	8d 04 1e             	lea    eax,[esi+ebx*1]
  407758:	3b 47 08             	cmp    eax,DWORD PTR [edi+0x8]
  40775b:	89 44 24 20          	mov    DWORD PTR [esp+0x20],eax
  40775f:	0f 9f c0             	setg   al
  407762:	0f b6 c0             	movzx  eax,al
  407765:	03 47 04             	add    eax,DWORD PTR [edi+0x4]
  407768:	89 04 24             	mov    DWORD PTR [esp],eax
  40776b:	e8 70 fd ff ff       	call   4074e0 <___Balloc_D2A>
  407770:	85 c0                	test   eax,eax
  407772:	89 44 24 2c          	mov    DWORD PTR [esp+0x2c],eax
  407776:	0f 84 08 01 00 00    	je     407884 <___mult_D2A+0x154>
  40777c:	8b 4c 24 20          	mov    ecx,DWORD PTR [esp+0x20]
  407780:	8d 40 14             	lea    eax,[eax+0x14]
  407783:	89 44 24 18          	mov    DWORD PTR [esp+0x18],eax
  407787:	8d 0c 88             	lea    ecx,[eax+ecx*4]
  40778a:	89 ca                	mov    edx,ecx
  40778c:	39 d0                	cmp    eax,edx
  40778e:	89 4c 24 28          	mov    DWORD PTR [esp+0x28],ecx
  407792:	73 11                	jae    4077a5 <___mult_D2A+0x75>
  407794:	8b 54 24 28          	mov    edx,DWORD PTR [esp+0x28]
  407798:	c7 00 00 00 00 00    	mov    DWORD PTR [eax],0x0
  40779e:	83 c0 04             	add    eax,0x4
  4077a1:	39 c2                	cmp    edx,eax
  4077a3:	77 f3                	ja     407798 <___mult_D2A+0x68>
  4077a5:	8d 47 14             	lea    eax,[edi+0x14]
  4077a8:	89 44 24 24          	mov    DWORD PTR [esp+0x24],eax
  4077ac:	8d 04 b0             	lea    eax,[eax+esi*4]
  4077af:	89 44 24 10          	mov    DWORD PTR [esp+0x10],eax
  4077b3:	8d 45 14             	lea    eax,[ebp+0x14]
  4077b6:	8d 1c 98             	lea    ebx,[eax+ebx*4]
  4077b9:	39 d8                	cmp    eax,ebx
  4077bb:	89 44 24 14          	mov    DWORD PTR [esp+0x14],eax
  4077bf:	89 5c 24 1c          	mov    DWORD PTR [esp+0x1c],ebx
  4077c3:	73 74                	jae    407839 <___mult_D2A+0x109>
  4077c5:	83 44 24 14 04       	add    DWORD PTR [esp+0x14],0x4
  4077ca:	8b 44 24 14          	mov    eax,DWORD PTR [esp+0x14]
  4077ce:	8b 68 fc             	mov    ebp,DWORD PTR [eax-0x4]
  4077d1:	85 ed                	test   ebp,ebp
  4077d3:	74 55                	je     40782a <___mult_D2A+0xfa>
  4077d5:	8b 7c 24 18          	mov    edi,DWORD PTR [esp+0x18]
  4077d9:	8b 74 24 24          	mov    esi,DWORD PTR [esp+0x24]
  4077dd:	c7 44 24 08 00 00 00 	mov    DWORD PTR [esp+0x8],0x0
  4077e4:	00 
  4077e5:	c7 44 24 0c 00 00 00 	mov    DWORD PTR [esp+0xc],0x0
  4077ec:	00 
  4077ed:	eb 03                	jmp    4077f2 <___mult_D2A+0xc2>
  4077ef:	90                   	nop
  4077f0:	89 c7                	mov    edi,eax
  4077f2:	83 c6 04             	add    esi,0x4
  4077f5:	8b 0f                	mov    ecx,DWORD PTR [edi]
  4077f7:	89 e8                	mov    eax,ebp
  4077f9:	f7 66 fc             	mul    DWORD PTR [esi-0x4]
  4077fc:	31 db                	xor    ebx,ebx
  4077fe:	01 c1                	add    ecx,eax
  407800:	11 d3                	adc    ebx,edx
  407802:	03 4c 24 08          	add    ecx,DWORD PTR [esp+0x8]
  407806:	13 5c 24 0c          	adc    ebx,DWORD PTR [esp+0xc]
  40780a:	89 0f                	mov    DWORD PTR [edi],ecx
  40780c:	89 da                	mov    edx,ebx
  40780e:	89 d0                	mov    eax,edx
  407810:	31 d2                	xor    edx,edx
  407812:	39 74 24 10          	cmp    DWORD PTR [esp+0x10],esi
  407816:	89 44 24 08          	mov    DWORD PTR [esp+0x8],eax
  40781a:	8d 47 04             	lea    eax,[edi+0x4]
  40781d:	89 54 24 0c          	mov    DWORD PTR [esp+0xc],edx
  407821:	77 cd                	ja     4077f0 <___mult_D2A+0xc0>
  407823:	8b 44 24 08          	mov    eax,DWORD PTR [esp+0x8]
  407827:	89 47 04             	mov    DWORD PTR [edi+0x4],eax
  40782a:	8b 44 24 14          	mov    eax,DWORD PTR [esp+0x14]
  40782e:	83 44 24 18 04       	add    DWORD PTR [esp+0x18],0x4
  407833:	39 44 24 1c          	cmp    DWORD PTR [esp+0x1c],eax
  407837:	77 8c                	ja     4077c5 <___mult_D2A+0x95>
  407839:	8b 7c 24 20          	mov    edi,DWORD PTR [esp+0x20]
  40783d:	85 ff                	test   edi,edi
  40783f:	7e 30                	jle    407871 <___mult_D2A+0x141>
  407841:	8b 5c 24 28          	mov    ebx,DWORD PTR [esp+0x28]
  407845:	8b 73 fc             	mov    esi,DWORD PTR [ebx-0x4]
  407848:	85 f6                	test   esi,esi
  40784a:	75 25                	jne    407871 <___mult_D2A+0x141>
  40784c:	8b 54 24 20          	mov    edx,DWORD PTR [esp+0x20]
  407850:	89 d0                	mov    eax,edx
  407852:	c1 e0 02             	shl    eax,0x2
  407855:	29 c3                	sub    ebx,eax
  407857:	89 d8                	mov    eax,ebx
  407859:	eb 0d                	jmp    407868 <___mult_D2A+0x138>
  40785b:	90                   	nop
  40785c:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  407860:	8b 4c 90 fc          	mov    ecx,DWORD PTR [eax+edx*4-0x4]
  407864:	85 c9                	test   ecx,ecx
  407866:	75 05                	jne    40786d <___mult_D2A+0x13d>
  407868:	83 ea 01             	sub    edx,0x1
  40786b:	75 f3                	jne    407860 <___mult_D2A+0x130>
  40786d:	89 54 24 20          	mov    DWORD PTR [esp+0x20],edx
  407871:	8b 44 24 2c          	mov    eax,DWORD PTR [esp+0x2c]
  407875:	8b 5c 24 20          	mov    ebx,DWORD PTR [esp+0x20]
  407879:	89 58 10             	mov    DWORD PTR [eax+0x10],ebx
  40787c:	83 c4 3c             	add    esp,0x3c
  40787f:	5b                   	pop    ebx
  407880:	5e                   	pop    esi
  407881:	5f                   	pop    edi
  407882:	5d                   	pop    ebp
  407883:	c3                   	ret    
  407884:	31 c0                	xor    eax,eax
  407886:	eb f4                	jmp    40787c <___mult_D2A+0x14c>
  407888:	90                   	nop
  407889:	8d b4 26 00 00 00 00 	lea    esi,[esi+eiz*1+0x0]

00407890 <___pow5mult_D2A>:
  407890:	55                   	push   ebp
  407891:	89 e5                	mov    ebp,esp
  407893:	57                   	push   edi
  407894:	56                   	push   esi
  407895:	53                   	push   ebx
  407896:	83 ec 1c             	sub    esp,0x1c
  407899:	8b 5d 0c             	mov    ebx,DWORD PTR [ebp+0xc]
  40789c:	8b 55 08             	mov    edx,DWORD PTR [ebp+0x8]
  40789f:	89 d8                	mov    eax,ebx
  4078a1:	83 e0 03             	and    eax,0x3
  4078a4:	0f 85 9e 00 00 00    	jne    407948 <___pow5mult_D2A+0xb8>
  4078aa:	c1 fb 02             	sar    ebx,0x2
  4078ad:	89 d0                	mov    eax,edx
  4078af:	85 db                	test   ebx,ebx
  4078b1:	74 4e                	je     407901 <___pow5mult_D2A+0x71>
  4078b3:	8b 3d 80 d0 40 00    	mov    edi,DWORD PTR ds:0x40d080
  4078b9:	85 ff                	test   edi,edi
  4078bb:	0f 84 d5 00 00 00    	je     407996 <___pow5mult_D2A+0x106>
  4078c1:	f6 c3 01             	test   bl,0x1
  4078c4:	75 13                	jne    4078d9 <___pow5mult_D2A+0x49>
  4078c6:	d1 fb                	sar    ebx,1
  4078c8:	74 35                	je     4078ff <___pow5mult_D2A+0x6f>
  4078ca:	8b 37                	mov    esi,DWORD PTR [edi]
  4078cc:	85 f6                	test   esi,esi
  4078ce:	66 90                	xchg   ax,ax
  4078d0:	74 3e                	je     407910 <___pow5mult_D2A+0x80>
  4078d2:	89 f7                	mov    edi,esi
  4078d4:	f6 c3 01             	test   bl,0x1
  4078d7:	74 ed                	je     4078c6 <___pow5mult_D2A+0x36>
  4078d9:	89 7c 24 04          	mov    DWORD PTR [esp+0x4],edi
  4078dd:	89 14 24             	mov    DWORD PTR [esp],edx
  4078e0:	89 55 e4             	mov    DWORD PTR [ebp-0x1c],edx
  4078e3:	e8 48 fe ff ff       	call   407730 <___mult_D2A>
  4078e8:	85 c0                	test   eax,eax
  4078ea:	89 c6                	mov    esi,eax
  4078ec:	74 7f                	je     40796d <___pow5mult_D2A+0xdd>
  4078ee:	8b 55 e4             	mov    edx,DWORD PTR [ebp-0x1c]
  4078f1:	89 14 24             	mov    DWORD PTR [esp],edx
  4078f4:	e8 b7 fc ff ff       	call   4075b0 <___Bfree_D2A>
  4078f9:	d1 fb                	sar    ebx,1
  4078fb:	89 f2                	mov    edx,esi
  4078fd:	75 cb                	jne    4078ca <___pow5mult_D2A+0x3a>
  4078ff:	89 d0                	mov    eax,edx
  407901:	8d 65 f4             	lea    esp,[ebp-0xc]
  407904:	5b                   	pop    ebx
  407905:	5e                   	pop    esi
  407906:	5f                   	pop    edi
  407907:	5d                   	pop    ebp
  407908:	c3                   	ret    
  407909:	8d b4 26 00 00 00 00 	lea    esi,[esi+eiz*1+0x0]
  407910:	b8 01 00 00 00       	mov    eax,0x1
  407915:	89 55 e4             	mov    DWORD PTR [ebp-0x1c],edx
  407918:	e8 a3 fa ff ff       	call   4073c0 <_dtoa_lock>
  40791d:	8b 37                	mov    esi,DWORD PTR [edi]
  40791f:	8b 55 e4             	mov    edx,DWORD PTR [ebp-0x1c]
  407922:	85 f6                	test   esi,esi
  407924:	74 51                	je     407977 <___pow5mult_D2A+0xe7>
  407926:	83 3d c8 d9 40 00 02 	cmp    DWORD PTR ds:0x40d9c8,0x2
  40792d:	75 a3                	jne    4078d2 <___pow5mult_D2A+0x42>
  40792f:	c7 04 24 f8 d9 40 00 	mov    DWORD PTR [esp],0x40d9f8
  407936:	89 f7                	mov    edi,esi
  407938:	89 55 e4             	mov    DWORD PTR [ebp-0x1c],edx
  40793b:	e8 78 08 00 00       	call   4081b8 <_LeaveCriticalSection@4>
  407940:	8b 55 e4             	mov    edx,DWORD PTR [ebp-0x1c]
  407943:	83 ec 04             	sub    esp,0x4
  407946:	eb 8c                	jmp    4078d4 <___pow5mult_D2A+0x44>
  407948:	8b 04 85 5c a3 40 00 	mov    eax,DWORD PTR [eax*4+0x40a35c]
  40794f:	89 14 24             	mov    DWORD PTR [esp],edx
  407952:	c7 44 24 08 00 00 00 	mov    DWORD PTR [esp+0x8],0x0
  407959:	00 
  40795a:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
  40795e:	e8 bd fc ff ff       	call   407620 <___multadd_D2A>
  407963:	85 c0                	test   eax,eax
  407965:	89 c2                	mov    edx,eax
  407967:	0f 85 3d ff ff ff    	jne    4078aa <___pow5mult_D2A+0x1a>
  40796d:	31 c0                	xor    eax,eax
  40796f:	8d 65 f4             	lea    esp,[ebp-0xc]
  407972:	5b                   	pop    ebx
  407973:	5e                   	pop    esi
  407974:	5f                   	pop    edi
  407975:	5d                   	pop    ebp
  407976:	c3                   	ret    
  407977:	89 7c 24 04          	mov    DWORD PTR [esp+0x4],edi
  40797b:	89 3c 24             	mov    DWORD PTR [esp],edi
  40797e:	e8 ad fd ff ff       	call   407730 <___mult_D2A>
  407983:	85 c0                	test   eax,eax
  407985:	89 c6                	mov    esi,eax
  407987:	89 07                	mov    DWORD PTR [edi],eax
  407989:	74 e2                	je     40796d <___pow5mult_D2A+0xdd>
  40798b:	c7 00 00 00 00 00    	mov    DWORD PTR [eax],0x0
  407991:	8b 55 e4             	mov    edx,DWORD PTR [ebp-0x1c]
  407994:	eb 90                	jmp    407926 <___pow5mult_D2A+0x96>
  407996:	b8 01 00 00 00       	mov    eax,0x1
  40799b:	89 55 e4             	mov    DWORD PTR [ebp-0x1c],edx
  40799e:	e8 1d fa ff ff       	call   4073c0 <_dtoa_lock>
  4079a3:	8b 3d 80 d0 40 00    	mov    edi,DWORD PTR ds:0x40d080
  4079a9:	8b 55 e4             	mov    edx,DWORD PTR [ebp-0x1c]
  4079ac:	85 ff                	test   edi,edi
  4079ae:	74 27                	je     4079d7 <___pow5mult_D2A+0x147>
  4079b0:	83 3d c8 d9 40 00 02 	cmp    DWORD PTR ds:0x40d9c8,0x2
  4079b7:	0f 85 04 ff ff ff    	jne    4078c1 <___pow5mult_D2A+0x31>
  4079bd:	c7 04 24 f8 d9 40 00 	mov    DWORD PTR [esp],0x40d9f8
  4079c4:	89 55 e4             	mov    DWORD PTR [ebp-0x1c],edx
  4079c7:	e8 ec 07 00 00       	call   4081b8 <_LeaveCriticalSection@4>
  4079cc:	8b 55 e4             	mov    edx,DWORD PTR [ebp-0x1c]
  4079cf:	83 ec 04             	sub    esp,0x4
  4079d2:	e9 ea fe ff ff       	jmp    4078c1 <___pow5mult_D2A+0x31>
  4079d7:	c7 04 24 01 00 00 00 	mov    DWORD PTR [esp],0x1
  4079de:	e8 fd fa ff ff       	call   4074e0 <___Balloc_D2A>
  4079e3:	85 c0                	test   eax,eax
  4079e5:	89 c7                	mov    edi,eax
  4079e7:	74 1e                	je     407a07 <___pow5mult_D2A+0x177>
  4079e9:	c7 40 14 71 02 00 00 	mov    DWORD PTR [eax+0x14],0x271
  4079f0:	8b 55 e4             	mov    edx,DWORD PTR [ebp-0x1c]
  4079f3:	c7 40 10 01 00 00 00 	mov    DWORD PTR [eax+0x10],0x1
  4079fa:	a3 80 d0 40 00       	mov    ds:0x40d080,eax
  4079ff:	c7 00 00 00 00 00    	mov    DWORD PTR [eax],0x0
  407a05:	eb a9                	jmp    4079b0 <___pow5mult_D2A+0x120>
  407a07:	c7 05 80 d0 40 00 00 	mov    DWORD PTR ds:0x40d080,0x0
  407a0e:	00 00 00 
  407a11:	31 c0                	xor    eax,eax
  407a13:	e9 57 ff ff ff       	jmp    40796f <___pow5mult_D2A+0xdf>
  407a18:	90                   	nop
  407a19:	8d b4 26 00 00 00 00 	lea    esi,[esi+eiz*1+0x0]

00407a20 <___lshift_D2A>:
  407a20:	55                   	push   ebp
  407a21:	57                   	push   edi
  407a22:	56                   	push   esi
  407a23:	53                   	push   ebx
  407a24:	83 ec 2c             	sub    esp,0x2c
  407a27:	8b 44 24 40          	mov    eax,DWORD PTR [esp+0x40]
  407a2b:	8b 74 24 44          	mov    esi,DWORD PTR [esp+0x44]
  407a2f:	89 c7                	mov    edi,eax
  407a31:	8b 50 04             	mov    edx,DWORD PTR [eax+0x4]
  407a34:	8b 40 10             	mov    eax,DWORD PTR [eax+0x10]
  407a37:	89 f3                	mov    ebx,esi
  407a39:	c1 fb 05             	sar    ebx,0x5
  407a3c:	01 d8                	add    eax,ebx
  407a3e:	8d 68 01             	lea    ebp,[eax+0x1]
  407a41:	89 44 24 18          	mov    DWORD PTR [esp+0x18],eax
  407a45:	8b 47 08             	mov    eax,DWORD PTR [edi+0x8]
  407a48:	39 c5                	cmp    ebp,eax
  407a4a:	7e 0d                	jle    407a59 <___lshift_D2A+0x39>
  407a4c:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  407a50:	01 c0                	add    eax,eax
  407a52:	83 c2 01             	add    edx,0x1
  407a55:	39 c5                	cmp    ebp,eax
  407a57:	7f f7                	jg     407a50 <___lshift_D2A+0x30>
  407a59:	89 14 24             	mov    DWORD PTR [esp],edx
  407a5c:	e8 7f fa ff ff       	call   4074e0 <___Balloc_D2A>
  407a61:	85 c0                	test   eax,eax
  407a63:	89 44 24 14          	mov    DWORD PTR [esp+0x14],eax
  407a67:	0f 84 bc 00 00 00    	je     407b29 <___lshift_D2A+0x109>
  407a6d:	85 db                	test   ebx,ebx
  407a6f:	8d 50 14             	lea    edx,[eax+0x14]
  407a72:	7e 13                	jle    407a87 <___lshift_D2A+0x67>
  407a74:	31 c0                	xor    eax,eax
  407a76:	c7 04 82 00 00 00 00 	mov    DWORD PTR [edx+eax*4],0x0
  407a7d:	83 c0 01             	add    eax,0x1
  407a80:	39 d8                	cmp    eax,ebx
  407a82:	75 f2                	jne    407a76 <___lshift_D2A+0x56>
  407a84:	8d 14 82             	lea    edx,[edx+eax*4]
  407a87:	8b 7c 24 40          	mov    edi,DWORD PTR [esp+0x40]
  407a8b:	8b 44 24 40          	mov    eax,DWORD PTR [esp+0x40]
  407a8f:	8b 4f 10             	mov    ecx,DWORD PTR [edi+0x10]
  407a92:	83 c0 14             	add    eax,0x14
  407a95:	83 e6 1f             	and    esi,0x1f
  407a98:	89 74 24 0c          	mov    DWORD PTR [esp+0xc],esi
  407a9c:	8d 3c 88             	lea    edi,[eax+ecx*4]
  407a9f:	89 f9                	mov    ecx,edi
  407aa1:	74 72                	je     407b15 <___lshift_D2A+0xf5>
  407aa3:	c7 44 24 10 20 00 00 	mov    DWORD PTR [esp+0x10],0x20
  407aaa:	00 
  407aab:	89 6c 24 1c          	mov    DWORD PTR [esp+0x1c],ebp
  407aaf:	89 cd                	mov    ebp,ecx
  407ab1:	29 74 24 10          	sub    DWORD PTR [esp+0x10],esi
  407ab5:	31 f6                	xor    esi,esi
  407ab7:	eb 09                	jmp    407ac2 <___lshift_D2A+0xa2>
  407ab9:	8d b4 26 00 00 00 00 	lea    esi,[esi+eiz*1+0x0]
  407ac0:	89 fa                	mov    edx,edi
  407ac2:	8b 18                	mov    ebx,DWORD PTR [eax]
  407ac4:	83 c0 04             	add    eax,0x4
  407ac7:	0f b6 4c 24 0c       	movzx  ecx,BYTE PTR [esp+0xc]
  407acc:	8d 7a 04             	lea    edi,[edx+0x4]
  407acf:	d3 e3                	shl    ebx,cl
  407ad1:	0f b6 4c 24 10       	movzx  ecx,BYTE PTR [esp+0x10]
  407ad6:	09 f3                	or     ebx,esi
  407ad8:	89 1a                	mov    DWORD PTR [edx],ebx
  407ada:	8b 70 fc             	mov    esi,DWORD PTR [eax-0x4]
  407add:	d3 ee                	shr    esi,cl
  407adf:	39 c5                	cmp    ebp,eax
  407ae1:	77 dd                	ja     407ac0 <___lshift_D2A+0xa0>
  407ae3:	85 f6                	test   esi,esi
  407ae5:	8b 6c 24 1c          	mov    ebp,DWORD PTR [esp+0x1c]
  407ae9:	89 72 04             	mov    DWORD PTR [edx+0x4],esi
  407aec:	74 07                	je     407af5 <___lshift_D2A+0xd5>
  407aee:	8b 6c 24 18          	mov    ebp,DWORD PTR [esp+0x18]
  407af2:	83 c5 02             	add    ebp,0x2
  407af5:	8b 7c 24 14          	mov    edi,DWORD PTR [esp+0x14]
  407af9:	8d 45 ff             	lea    eax,[ebp-0x1]
  407afc:	89 47 10             	mov    DWORD PTR [edi+0x10],eax
  407aff:	8b 44 24 40          	mov    eax,DWORD PTR [esp+0x40]
  407b03:	89 04 24             	mov    DWORD PTR [esp],eax
  407b06:	e8 a5 fa ff ff       	call   4075b0 <___Bfree_D2A>
  407b0b:	89 f8                	mov    eax,edi
  407b0d:	83 c4 2c             	add    esp,0x2c
  407b10:	5b                   	pop    ebx
  407b11:	5e                   	pop    esi
  407b12:	5f                   	pop    edi
  407b13:	5d                   	pop    ebp
  407b14:	c3                   	ret    
  407b15:	89 fb                	mov    ebx,edi
  407b17:	83 c0 04             	add    eax,0x4
  407b1a:	8b 48 fc             	mov    ecx,DWORD PTR [eax-0x4]
  407b1d:	83 c2 04             	add    edx,0x4
  407b20:	39 c3                	cmp    ebx,eax
  407b22:	89 4a fc             	mov    DWORD PTR [edx-0x4],ecx
  407b25:	77 f0                	ja     407b17 <___lshift_D2A+0xf7>
  407b27:	eb cc                	jmp    407af5 <___lshift_D2A+0xd5>
  407b29:	31 c0                	xor    eax,eax
  407b2b:	eb e0                	jmp    407b0d <___lshift_D2A+0xed>
  407b2d:	8d 76 00             	lea    esi,[esi+0x0]

00407b30 <___cmp_D2A>:
  407b30:	53                   	push   ebx
  407b31:	8b 4c 24 08          	mov    ecx,DWORD PTR [esp+0x8]
  407b35:	8b 54 24 0c          	mov    edx,DWORD PTR [esp+0xc]
  407b39:	8b 41 10             	mov    eax,DWORD PTR [ecx+0x10]
  407b3c:	8b 5a 10             	mov    ebx,DWORD PTR [edx+0x10]
  407b3f:	29 d8                	sub    eax,ebx
  407b41:	85 c0                	test   eax,eax
  407b43:	75 24                	jne    407b69 <___cmp_D2A+0x39>
  407b45:	c1 e3 02             	shl    ebx,0x2
  407b48:	83 c1 14             	add    ecx,0x14
  407b4b:	8d 04 19             	lea    eax,[ecx+ebx*1]
  407b4e:	8d 54 1a 14          	lea    edx,[edx+ebx*1+0x14]
  407b52:	eb 04                	jmp    407b58 <___cmp_D2A+0x28>
  407b54:	39 c1                	cmp    ecx,eax
  407b56:	73 18                	jae    407b70 <___cmp_D2A+0x40>
  407b58:	83 ea 04             	sub    edx,0x4
  407b5b:	83 e8 04             	sub    eax,0x4
  407b5e:	8b 1a                	mov    ebx,DWORD PTR [edx]
  407b60:	39 18                	cmp    DWORD PTR [eax],ebx
  407b62:	74 f0                	je     407b54 <___cmp_D2A+0x24>
  407b64:	19 c0                	sbb    eax,eax
  407b66:	83 c8 01             	or     eax,0x1
  407b69:	5b                   	pop    ebx
  407b6a:	c3                   	ret    
  407b6b:	90                   	nop
  407b6c:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  407b70:	31 c0                	xor    eax,eax
  407b72:	5b                   	pop    ebx
  407b73:	c3                   	ret    
  407b74:	8d b6 00 00 00 00    	lea    esi,[esi+0x0]
  407b7a:	8d bf 00 00 00 00    	lea    edi,[edi+0x0]

00407b80 <___diff_D2A>:
  407b80:	55                   	push   ebp
  407b81:	57                   	push   edi
  407b82:	56                   	push   esi
  407b83:	53                   	push   ebx
  407b84:	83 ec 2c             	sub    esp,0x2c
  407b87:	8b 74 24 40          	mov    esi,DWORD PTR [esp+0x40]
  407b8b:	8b 5c 24 44          	mov    ebx,DWORD PTR [esp+0x44]
  407b8f:	89 34 24             	mov    DWORD PTR [esp],esi
  407b92:	89 5c 24 04          	mov    DWORD PTR [esp+0x4],ebx
  407b96:	e8 95 ff ff ff       	call   407b30 <___cmp_D2A>
  407b9b:	85 c0                	test   eax,eax
  407b9d:	0f 84 1f 01 00 00    	je     407cc2 <___diff_D2A+0x142>
  407ba3:	0f 88 3f 01 00 00    	js     407ce8 <___diff_D2A+0x168>
  407ba9:	31 ff                	xor    edi,edi
  407bab:	8b 46 04             	mov    eax,DWORD PTR [esi+0x4]
  407bae:	89 04 24             	mov    DWORD PTR [esp],eax
  407bb1:	e8 2a f9 ff ff       	call   4074e0 <___Balloc_D2A>
  407bb6:	85 c0                	test   eax,eax
  407bb8:	89 c2                	mov    edx,eax
  407bba:	89 44 24 1c          	mov    DWORD PTR [esp+0x1c],eax
  407bbe:	0f 84 34 01 00 00    	je     407cf8 <___diff_D2A+0x178>
  407bc4:	89 78 0c             	mov    DWORD PTR [eax+0xc],edi
  407bc7:	8b 46 10             	mov    eax,DWORD PTR [esi+0x10]
  407bca:	83 c6 14             	add    esi,0x14
  407bcd:	8d 6b 14             	lea    ebp,[ebx+0x14]
  407bd0:	8d 7a 14             	lea    edi,[edx+0x14]
  407bd3:	c7 44 24 08 00 00 00 	mov    DWORD PTR [esp+0x8],0x0
  407bda:	00 
  407bdb:	89 44 24 18          	mov    DWORD PTR [esp+0x18],eax
  407bdf:	8d 04 86             	lea    eax,[esi+eax*4]
  407be2:	89 44 24 10          	mov    DWORD PTR [esp+0x10],eax
  407be6:	8b 43 10             	mov    eax,DWORD PTR [ebx+0x10]
  407be9:	c7 44 24 0c 00 00 00 	mov    DWORD PTR [esp+0xc],0x0
  407bf0:	00 
  407bf1:	8d 44 85 00          	lea    eax,[ebp+eax*4+0x0]
  407bf5:	89 44 24 14          	mov    DWORD PTR [esp+0x14],eax
  407bf9:	8d b4 26 00 00 00 00 	lea    esi,[esi+eiz*1+0x0]
  407c00:	83 c5 04             	add    ebp,0x4
  407c03:	83 c6 04             	add    esi,0x4
  407c06:	8b 4d fc             	mov    ecx,DWORD PTR [ebp-0x4]
  407c09:	8b 46 fc             	mov    eax,DWORD PTR [esi-0x4]
  407c0c:	31 d2                	xor    edx,edx
  407c0e:	31 db                	xor    ebx,ebx
  407c10:	29 c8                	sub    eax,ecx
  407c12:	19 da                	sbb    edx,ebx
  407c14:	2b 44 24 08          	sub    eax,DWORD PTR [esp+0x8]
  407c18:	1b 54 24 0c          	sbb    edx,DWORD PTR [esp+0xc]
  407c1c:	83 c7 04             	add    edi,0x4
  407c1f:	c7 44 24 0c 00 00 00 	mov    DWORD PTR [esp+0xc],0x0
  407c26:	00 
  407c27:	89 d1                	mov    ecx,edx
  407c29:	83 e1 01             	and    ecx,0x1
  407c2c:	39 6c 24 14          	cmp    DWORD PTR [esp+0x14],ebp
  407c30:	89 4c 24 08          	mov    DWORD PTR [esp+0x8],ecx
  407c34:	89 47 fc             	mov    DWORD PTR [edi-0x4],eax
  407c37:	77 c7                	ja     407c00 <___diff_D2A+0x80>
  407c39:	39 74 24 10          	cmp    DWORD PTR [esp+0x10],esi
  407c3d:	76 4b                	jbe    407c8a <___diff_D2A+0x10a>
  407c3f:	8b 5c 24 0c          	mov    ebx,DWORD PTR [esp+0xc]
  407c43:	8b 4c 24 08          	mov    ecx,DWORD PTR [esp+0x8]
  407c47:	89 7c 24 14          	mov    DWORD PTR [esp+0x14],edi
  407c4b:	89 74 24 08          	mov    DWORD PTR [esp+0x8],esi
  407c4f:	90                   	nop
  407c50:	83 c6 04             	add    esi,0x4
  407c53:	8b 46 fc             	mov    eax,DWORD PTR [esi-0x4]
  407c56:	31 d2                	xor    edx,edx
  407c58:	29 c8                	sub    eax,ecx
  407c5a:	19 da                	sbb    edx,ebx
  407c5c:	83 c7 04             	add    edi,0x4
  407c5f:	89 d5                	mov    ebp,edx
  407c61:	31 db                	xor    ebx,ebx
  407c63:	83 e5 01             	and    ebp,0x1
  407c66:	39 74 24 10          	cmp    DWORD PTR [esp+0x10],esi
  407c6a:	89 e9                	mov    ecx,ebp
  407c6c:	89 47 fc             	mov    DWORD PTR [edi-0x4],eax
  407c6f:	77 df                	ja     407c50 <___diff_D2A+0xd0>
  407c71:	8b 6c 24 08          	mov    ebp,DWORD PTR [esp+0x8]
  407c75:	8b 7c 24 10          	mov    edi,DWORD PTR [esp+0x10]
  407c79:	8b 5c 24 14          	mov    ebx,DWORD PTR [esp+0x14]
  407c7d:	f7 d5                	not    ebp
  407c7f:	8d 54 3d 00          	lea    edx,[ebp+edi*1+0x0]
  407c83:	c1 ea 02             	shr    edx,0x2
  407c86:	8d 7c 93 04          	lea    edi,[ebx+edx*4+0x4]
  407c8a:	85 c0                	test   eax,eax
  407c8c:	75 21                	jne    407caf <___diff_D2A+0x12f>
  407c8e:	8b 54 24 18          	mov    edx,DWORD PTR [esp+0x18]
  407c92:	89 d0                	mov    eax,edx
  407c94:	c1 e0 02             	shl    eax,0x2
  407c97:	29 c7                	sub    edi,eax
  407c99:	89 d0                	mov    eax,edx
  407c9b:	90                   	nop
  407c9c:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  407ca0:	83 e8 01             	sub    eax,0x1
  407ca3:	8b 6c 87 fc          	mov    ebp,DWORD PTR [edi+eax*4-0x4]
  407ca7:	85 ed                	test   ebp,ebp
  407ca9:	74 f5                	je     407ca0 <___diff_D2A+0x120>
  407cab:	89 44 24 18          	mov    DWORD PTR [esp+0x18],eax
  407caf:	8b 44 24 1c          	mov    eax,DWORD PTR [esp+0x1c]
  407cb3:	8b 54 24 18          	mov    edx,DWORD PTR [esp+0x18]
  407cb7:	89 50 10             	mov    DWORD PTR [eax+0x10],edx
  407cba:	83 c4 2c             	add    esp,0x2c
  407cbd:	5b                   	pop    ebx
  407cbe:	5e                   	pop    esi
  407cbf:	5f                   	pop    edi
  407cc0:	5d                   	pop    ebp
  407cc1:	c3                   	ret    
  407cc2:	c7 04 24 00 00 00 00 	mov    DWORD PTR [esp],0x0
  407cc9:	e8 12 f8 ff ff       	call   4074e0 <___Balloc_D2A>
  407cce:	85 c0                	test   eax,eax
  407cd0:	74 26                	je     407cf8 <___diff_D2A+0x178>
  407cd2:	c7 40 10 01 00 00 00 	mov    DWORD PTR [eax+0x10],0x1
  407cd9:	c7 40 14 00 00 00 00 	mov    DWORD PTR [eax+0x14],0x0
  407ce0:	83 c4 2c             	add    esp,0x2c
  407ce3:	5b                   	pop    ebx
  407ce4:	5e                   	pop    esi
  407ce5:	5f                   	pop    edi
  407ce6:	5d                   	pop    ebp
  407ce7:	c3                   	ret    
  407ce8:	89 f0                	mov    eax,esi
  407cea:	bf 01 00 00 00       	mov    edi,0x1
  407cef:	89 de                	mov    esi,ebx
  407cf1:	89 c3                	mov    ebx,eax
  407cf3:	e9 b3 fe ff ff       	jmp    407bab <___diff_D2A+0x2b>
  407cf8:	31 c0                	xor    eax,eax
  407cfa:	eb be                	jmp    407cba <___diff_D2A+0x13a>
  407cfc:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]

00407d00 <___b2d_D2A>:
  407d00:	55                   	push   ebp
  407d01:	b9 20 00 00 00       	mov    ecx,0x20
  407d06:	57                   	push   edi
  407d07:	56                   	push   esi
  407d08:	53                   	push   ebx
  407d09:	83 ec 14             	sub    esp,0x14
  407d0c:	8b 44 24 28          	mov    eax,DWORD PTR [esp+0x28]
  407d10:	8b 7c 24 2c          	mov    edi,DWORD PTR [esp+0x2c]
  407d14:	8d 58 14             	lea    ebx,[eax+0x14]
  407d17:	8b 40 10             	mov    eax,DWORD PTR [eax+0x10]
  407d1a:	8d 2c 83             	lea    ebp,[ebx+eax*4]
  407d1d:	8b 55 fc             	mov    edx,DWORD PTR [ebp-0x4]
  407d20:	8d 75 fc             	lea    esi,[ebp-0x4]
  407d23:	0f bd c2             	bsr    eax,edx
  407d26:	83 f0 1f             	xor    eax,0x1f
  407d29:	29 c1                	sub    ecx,eax
  407d2b:	83 f8 0a             	cmp    eax,0xa
  407d2e:	89 0f                	mov    DWORD PTR [edi],ecx
  407d30:	7f 3e                	jg     407d70 <___b2d_D2A+0x70>
  407d32:	b9 0b 00 00 00       	mov    ecx,0xb
  407d37:	89 d7                	mov    edi,edx
  407d39:	29 c1                	sub    ecx,eax
  407d3b:	d3 ef                	shr    edi,cl
  407d3d:	81 cf 00 00 f0 3f    	or     edi,0x3ff00000
  407d43:	89 7c 24 04          	mov    DWORD PTR [esp+0x4],edi
  407d47:	31 ff                	xor    edi,edi
  407d49:	39 f3                	cmp    ebx,esi
  407d4b:	c7 04 24 00 00 00 00 	mov    DWORD PTR [esp],0x0
  407d52:	73 05                	jae    407d59 <___b2d_D2A+0x59>
  407d54:	8b 7d f8             	mov    edi,DWORD PTR [ebp-0x8]
  407d57:	d3 ef                	shr    edi,cl
  407d59:	8d 48 15             	lea    ecx,[eax+0x15]
  407d5c:	d3 e2                	shl    edx,cl
  407d5e:	09 d7                	or     edi,edx
  407d60:	89 3c 24             	mov    DWORD PTR [esp],edi
  407d63:	dd 04 24             	fld    QWORD PTR [esp]
  407d66:	83 c4 14             	add    esp,0x14
  407d69:	5b                   	pop    ebx
  407d6a:	5e                   	pop    esi
  407d6b:	5f                   	pop    edi
  407d6c:	5d                   	pop    ebp
  407d6d:	c3                   	ret    
  407d6e:	66 90                	xchg   ax,ax
  407d70:	31 ff                	xor    edi,edi
  407d72:	39 f3                	cmp    ebx,esi
  407d74:	73 06                	jae    407d7c <___b2d_D2A+0x7c>
  407d76:	8b 7d f8             	mov    edi,DWORD PTR [ebp-0x8]
  407d79:	8d 75 f8             	lea    esi,[ebp-0x8]
  407d7c:	89 c1                	mov    ecx,eax
  407d7e:	83 e9 0b             	sub    ecx,0xb
  407d81:	89 4c 24 0c          	mov    DWORD PTR [esp+0xc],ecx
  407d85:	74 49                	je     407dd0 <___b2d_D2A+0xd0>
  407d87:	0f b6 4c 24 0c       	movzx  ecx,BYTE PTR [esp+0xc]
  407d8c:	bd 2b 00 00 00       	mov    ebp,0x2b
  407d91:	29 c5                	sub    ebp,eax
  407d93:	89 f8                	mov    eax,edi
  407d95:	c7 04 24 00 00 00 00 	mov    DWORD PTR [esp],0x0
  407d9c:	d3 e2                	shl    edx,cl
  407d9e:	89 e9                	mov    ecx,ebp
  407da0:	d3 e8                	shr    eax,cl
  407da2:	81 ca 00 00 f0 3f    	or     edx,0x3ff00000
  407da8:	09 c2                	or     edx,eax
  407daa:	31 c0                	xor    eax,eax
  407dac:	39 de                	cmp    esi,ebx
  407dae:	89 54 24 04          	mov    DWORD PTR [esp+0x4],edx
  407db2:	76 05                	jbe    407db9 <___b2d_D2A+0xb9>
  407db4:	8b 46 fc             	mov    eax,DWORD PTR [esi-0x4]
  407db7:	d3 e8                	shr    eax,cl
  407db9:	0f b6 4c 24 0c       	movzx  ecx,BYTE PTR [esp+0xc]
  407dbe:	d3 e7                	shl    edi,cl
  407dc0:	09 f8                	or     eax,edi
  407dc2:	89 04 24             	mov    DWORD PTR [esp],eax
  407dc5:	dd 04 24             	fld    QWORD PTR [esp]
  407dc8:	83 c4 14             	add    esp,0x14
  407dcb:	5b                   	pop    ebx
  407dcc:	5e                   	pop    esi
  407dcd:	5f                   	pop    edi
  407dce:	5d                   	pop    ebp
  407dcf:	c3                   	ret    
  407dd0:	81 ca 00 00 f0 3f    	or     edx,0x3ff00000
  407dd6:	89 3c 24             	mov    DWORD PTR [esp],edi
  407dd9:	89 54 24 04          	mov    DWORD PTR [esp+0x4],edx
  407ddd:	dd 04 24             	fld    QWORD PTR [esp]
  407de0:	83 c4 14             	add    esp,0x14
  407de3:	5b                   	pop    ebx
  407de4:	5e                   	pop    esi
  407de5:	5f                   	pop    edi
  407de6:	5d                   	pop    ebp
  407de7:	c3                   	ret    
  407de8:	90                   	nop
  407de9:	8d b4 26 00 00 00 00 	lea    esi,[esi+eiz*1+0x0]

00407df0 <___d2b_D2A>:
  407df0:	55                   	push   ebp
  407df1:	57                   	push   edi
  407df2:	56                   	push   esi
  407df3:	53                   	push   ebx
  407df4:	83 ec 1c             	sub    esp,0x1c
  407df7:	dd 44 24 30          	fld    QWORD PTR [esp+0x30]
  407dfb:	c7 04 24 01 00 00 00 	mov    DWORD PTR [esp],0x1
  407e02:	dd 5c 24 08          	fstp   QWORD PTR [esp+0x8]
  407e06:	e8 d5 f6 ff ff       	call   4074e0 <___Balloc_D2A>
  407e0b:	85 c0                	test   eax,eax
  407e0d:	0f 84 c5 00 00 00    	je     407ed8 <___d2b_D2A+0xe8>
  407e13:	8b 54 24 0c          	mov    edx,DWORD PTR [esp+0xc]
  407e17:	89 d3                	mov    ebx,edx
  407e19:	81 e2 ff ff ff 7f    	and    edx,0x7fffffff
  407e1f:	c1 ea 14             	shr    edx,0x14
  407e22:	81 e3 ff ff 0f 00    	and    ebx,0xfffff
  407e28:	85 d2                	test   edx,edx
  407e2a:	74 06                	je     407e32 <___d2b_D2A+0x42>
  407e2c:	81 cb 00 00 10 00    	or     ebx,0x100000
  407e32:	8b 7c 24 08          	mov    edi,DWORD PTR [esp+0x8]
  407e36:	85 ff                	test   edi,edi
  407e38:	75 3e                	jne    407e78 <___d2b_D2A+0x88>
  407e3a:	f3 0f bc cb          	tzcnt  ecx,ebx
  407e3e:	d3 eb                	shr    ebx,cl
  407e40:	85 d2                	test   edx,edx
  407e42:	8d 71 20             	lea    esi,[ecx+0x20]
  407e45:	b9 01 00 00 00       	mov    ecx,0x1
  407e4a:	89 58 14             	mov    DWORD PTR [eax+0x14],ebx
  407e4d:	c7 40 10 01 00 00 00 	mov    DWORD PTR [eax+0x10],0x1
  407e54:	74 56                	je     407eac <___d2b_D2A+0xbc>
  407e56:	8b 7c 24 38          	mov    edi,DWORD PTR [esp+0x38]
  407e5a:	8d 94 16 cd fb ff ff 	lea    edx,[esi+edx*1-0x433]
  407e61:	89 17                	mov    DWORD PTR [edi],edx
  407e63:	ba 35 00 00 00       	mov    edx,0x35
  407e68:	29 f2                	sub    edx,esi
  407e6a:	8b 74 24 3c          	mov    esi,DWORD PTR [esp+0x3c]
  407e6e:	89 16                	mov    DWORD PTR [esi],edx
  407e70:	83 c4 1c             	add    esp,0x1c
  407e73:	5b                   	pop    ebx
  407e74:	5e                   	pop    esi
  407e75:	5f                   	pop    edi
  407e76:	5d                   	pop    ebp
  407e77:	c3                   	ret    
  407e78:	f3 0f bc f7          	tzcnt  esi,edi
  407e7c:	89 f1                	mov    ecx,esi
  407e7e:	d3 ef                	shr    edi,cl
  407e80:	85 f6                	test   esi,esi
  407e82:	74 4f                	je     407ed3 <___d2b_D2A+0xe3>
  407e84:	b9 20 00 00 00       	mov    ecx,0x20
  407e89:	89 dd                	mov    ebp,ebx
  407e8b:	29 f1                	sub    ecx,esi
  407e8d:	d3 e5                	shl    ebp,cl
  407e8f:	89 e9                	mov    ecx,ebp
  407e91:	09 f9                	or     ecx,edi
  407e93:	89 48 14             	mov    DWORD PTR [eax+0x14],ecx
  407e96:	89 f1                	mov    ecx,esi
  407e98:	d3 eb                	shr    ebx,cl
  407e9a:	83 fb 01             	cmp    ebx,0x1
  407e9d:	19 c9                	sbb    ecx,ecx
  407e9f:	83 c1 02             	add    ecx,0x2
  407ea2:	85 d2                	test   edx,edx
  407ea4:	89 58 18             	mov    DWORD PTR [eax+0x18],ebx
  407ea7:	89 48 10             	mov    DWORD PTR [eax+0x10],ecx
  407eaa:	75 aa                	jne    407e56 <___d2b_D2A+0x66>
  407eac:	8b 7c 24 38          	mov    edi,DWORD PTR [esp+0x38]
  407eb0:	81 ee 32 04 00 00    	sub    esi,0x432
  407eb6:	0f bd 54 88 10       	bsr    edx,DWORD PTR [eax+ecx*4+0x10]
  407ebb:	c1 e1 05             	shl    ecx,0x5
  407ebe:	89 37                	mov    DWORD PTR [edi],esi
  407ec0:	8b 74 24 3c          	mov    esi,DWORD PTR [esp+0x3c]
  407ec4:	83 f2 1f             	xor    edx,0x1f
  407ec7:	29 d1                	sub    ecx,edx
  407ec9:	89 0e                	mov    DWORD PTR [esi],ecx
  407ecb:	83 c4 1c             	add    esp,0x1c
  407ece:	5b                   	pop    ebx
  407ecf:	5e                   	pop    esi
  407ed0:	5f                   	pop    edi
  407ed1:	5d                   	pop    ebp
  407ed2:	c3                   	ret    
  407ed3:	89 78 14             	mov    DWORD PTR [eax+0x14],edi
  407ed6:	eb c2                	jmp    407e9a <___d2b_D2A+0xaa>
  407ed8:	31 c0                	xor    eax,eax
  407eda:	eb 94                	jmp    407e70 <___d2b_D2A+0x80>
  407edc:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]

00407ee0 <___strcp_D2A>:
  407ee0:	8b 4c 24 08          	mov    ecx,DWORD PTR [esp+0x8]
  407ee4:	8b 44 24 04          	mov    eax,DWORD PTR [esp+0x4]
  407ee8:	8d 51 01             	lea    edx,[ecx+0x1]
  407eeb:	0f b6 09             	movzx  ecx,BYTE PTR [ecx]
  407eee:	84 c9                	test   cl,cl
  407ef0:	88 08                	mov    BYTE PTR [eax],cl
  407ef2:	74 10                	je     407f04 <___strcp_D2A+0x24>
  407ef4:	83 c2 01             	add    edx,0x1
  407ef7:	0f b6 4a ff          	movzx  ecx,BYTE PTR [edx-0x1]
  407efb:	83 c0 01             	add    eax,0x1
  407efe:	84 c9                	test   cl,cl
  407f00:	88 08                	mov    BYTE PTR [eax],cl
  407f02:	75 f0                	jne    407ef4 <___strcp_D2A+0x14>
  407f04:	f3 c3                	repz ret 
  407f06:	90                   	nop
  407f07:	90                   	nop
  407f08:	90                   	nop
  407f09:	90                   	nop
  407f0a:	90                   	nop
  407f0b:	90                   	nop
  407f0c:	90                   	nop
  407f0d:	90                   	nop
  407f0e:	90                   	nop
  407f0f:	90                   	nop

00407f10 <___rshift_D2A>:
  407f10:	55                   	push   ebp
  407f11:	57                   	push   edi
  407f12:	56                   	push   esi
  407f13:	53                   	push   ebx
  407f14:	83 ec 10             	sub    esp,0x10
  407f17:	8b 74 24 24          	mov    esi,DWORD PTR [esp+0x24]
  407f1b:	8b 44 24 24          	mov    eax,DWORD PTR [esp+0x24]
  407f1f:	8b 4c 24 28          	mov    ecx,DWORD PTR [esp+0x28]
  407f23:	8b 56 10             	mov    edx,DWORD PTR [esi+0x10]
  407f26:	8d 68 14             	lea    ebp,[eax+0x14]
  407f29:	89 c8                	mov    eax,ecx
  407f2b:	c1 f8 05             	sar    eax,0x5
  407f2e:	39 d0                	cmp    eax,edx
  407f30:	0f 8d 8a 00 00 00    	jge    407fc0 <___rshift_D2A+0xb0>
  407f36:	8d 44 85 00          	lea    eax,[ebp+eax*4+0x0]
  407f3a:	83 e1 1f             	and    ecx,0x1f
  407f3d:	8d 7c 95 00          	lea    edi,[ebp+edx*4+0x0]
  407f41:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
  407f45:	89 0c 24             	mov    DWORD PTR [esp],ecx
  407f48:	0f 84 92 00 00 00    	je     407fe0 <___rshift_D2A+0xd0>
  407f4e:	8b 74 24 04          	mov    esi,DWORD PTR [esp+0x4]
  407f52:	8b 04 24             	mov    eax,DWORD PTR [esp]
  407f55:	c7 44 24 08 20 00 00 	mov    DWORD PTR [esp+0x8],0x20
  407f5c:	00 
  407f5d:	29 44 24 08          	sub    DWORD PTR [esp+0x8],eax
  407f61:	8b 1e                	mov    ebx,DWORD PTR [esi]
  407f63:	8d 56 04             	lea    edx,[esi+0x4]
  407f66:	89 c1                	mov    ecx,eax
  407f68:	d3 eb                	shr    ebx,cl
  407f6a:	39 d7                	cmp    edi,edx
  407f6c:	0f 86 ac 00 00 00    	jbe    40801e <___rshift_D2A+0x10e>
  407f72:	89 ee                	mov    esi,ebp
  407f74:	89 6c 24 0c          	mov    DWORD PTR [esp+0xc],ebp
  407f78:	8b 6c 24 08          	mov    ebp,DWORD PTR [esp+0x8]
  407f7c:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  407f80:	8b 02                	mov    eax,DWORD PTR [edx]
  407f82:	89 e9                	mov    ecx,ebp
  407f84:	83 c6 04             	add    esi,0x4
  407f87:	83 c2 04             	add    edx,0x4
  407f8a:	d3 e0                	shl    eax,cl
  407f8c:	0f b6 0c 24          	movzx  ecx,BYTE PTR [esp]
  407f90:	09 d8                	or     eax,ebx
  407f92:	89 46 fc             	mov    DWORD PTR [esi-0x4],eax
  407f95:	8b 5a fc             	mov    ebx,DWORD PTR [edx-0x4]
  407f98:	d3 eb                	shr    ebx,cl
  407f9a:	39 d7                	cmp    edi,edx
  407f9c:	77 e2                	ja     407f80 <___rshift_D2A+0x70>
  407f9e:	2b 7c 24 04          	sub    edi,DWORD PTR [esp+0x4]
  407fa2:	8b 6c 24 0c          	mov    ebp,DWORD PTR [esp+0xc]
  407fa6:	8d 47 fb             	lea    eax,[edi-0x5]
  407fa9:	c1 e8 02             	shr    eax,0x2
  407fac:	8d 44 85 04          	lea    eax,[ebp+eax*4+0x4]
  407fb0:	85 db                	test   ebx,ebx
  407fb2:	89 18                	mov    DWORD PTR [eax],ebx
  407fb4:	74 03                	je     407fb9 <___rshift_D2A+0xa9>
  407fb6:	83 c0 04             	add    eax,0x4
  407fb9:	29 e8                	sub    eax,ebp
  407fbb:	c1 f8 02             	sar    eax,0x2
  407fbe:	eb 4b                	jmp    40800b <___rshift_D2A+0xfb>
  407fc0:	8b 44 24 24          	mov    eax,DWORD PTR [esp+0x24]
  407fc4:	c7 40 10 00 00 00 00 	mov    DWORD PTR [eax+0x10],0x0
  407fcb:	8b 44 24 24          	mov    eax,DWORD PTR [esp+0x24]
  407fcf:	c7 40 14 00 00 00 00 	mov    DWORD PTR [eax+0x14],0x0
  407fd6:	83 c4 10             	add    esp,0x10
  407fd9:	5b                   	pop    ebx
  407fda:	5e                   	pop    esi
  407fdb:	5f                   	pop    edi
  407fdc:	5d                   	pop    ebp
  407fdd:	c3                   	ret    
  407fde:	66 90                	xchg   ax,ax
  407fe0:	39 c7                	cmp    edi,eax
  407fe2:	89 ea                	mov    edx,ebp
  407fe4:	76 da                	jbe    407fc0 <___rshift_D2A+0xb0>
  407fe6:	83 c0 04             	add    eax,0x4
  407fe9:	8b 48 fc             	mov    ecx,DWORD PTR [eax-0x4]
  407fec:	83 c2 04             	add    edx,0x4
  407fef:	39 c7                	cmp    edi,eax
  407ff1:	89 4a fc             	mov    DWORD PTR [edx-0x4],ecx
  407ff4:	77 f0                	ja     407fe6 <___rshift_D2A+0xd6>
  407ff6:	8b 44 24 04          	mov    eax,DWORD PTR [esp+0x4]
  407ffa:	f7 d0                	not    eax
  407ffc:	01 f8                	add    eax,edi
  407ffe:	c1 e8 02             	shr    eax,0x2
  408001:	8d 04 85 04 00 00 00 	lea    eax,[eax*4+0x4]
  408008:	c1 f8 02             	sar    eax,0x2
  40800b:	8b 74 24 24          	mov    esi,DWORD PTR [esp+0x24]
  40800f:	85 c0                	test   eax,eax
  408011:	89 46 10             	mov    DWORD PTR [esi+0x10],eax
  408014:	74 b5                	je     407fcb <___rshift_D2A+0xbb>
  408016:	83 c4 10             	add    esp,0x10
  408019:	5b                   	pop    ebx
  40801a:	5e                   	pop    esi
  40801b:	5f                   	pop    edi
  40801c:	5d                   	pop    ebp
  40801d:	c3                   	ret    
  40801e:	89 e8                	mov    eax,ebp
  408020:	eb 8e                	jmp    407fb0 <___rshift_D2A+0xa0>
  408022:	8d b4 26 00 00 00 00 	lea    esi,[esi+eiz*1+0x0]
  408029:	8d bc 27 00 00 00 00 	lea    edi,[edi+eiz*1+0x0]

00408030 <___trailz_D2A>:
  408030:	53                   	push   ebx
  408031:	8b 44 24 08          	mov    eax,DWORD PTR [esp+0x8]
  408035:	8b 48 10             	mov    ecx,DWORD PTR [eax+0x10]
  408038:	8d 50 14             	lea    edx,[eax+0x14]
  40803b:	8d 1c 8a             	lea    ebx,[edx+ecx*4]
  40803e:	39 da                	cmp    edx,ebx
  408040:	73 28                	jae    40806a <___trailz_D2A+0x3a>
  408042:	8b 48 14             	mov    ecx,DWORD PTR [eax+0x14]
  408045:	31 c0                	xor    eax,eax
  408047:	85 c9                	test   ecx,ecx
  408049:	74 0b                	je     408056 <___trailz_D2A+0x26>
  40804b:	eb 15                	jmp    408062 <___trailz_D2A+0x32>
  40804d:	8d 76 00             	lea    esi,[esi+0x0]
  408050:	8b 0a                	mov    ecx,DWORD PTR [edx]
  408052:	85 c9                	test   ecx,ecx
  408054:	75 0c                	jne    408062 <___trailz_D2A+0x32>
  408056:	83 c2 04             	add    edx,0x4
  408059:	83 c0 20             	add    eax,0x20
  40805c:	39 d3                	cmp    ebx,edx
  40805e:	77 f0                	ja     408050 <___trailz_D2A+0x20>
  408060:	5b                   	pop    ebx
  408061:	c3                   	ret    
  408062:	f3 0f bc c9          	tzcnt  ecx,ecx
  408066:	01 c8                	add    eax,ecx
  408068:	5b                   	pop    ebx
  408069:	c3                   	ret    
  40806a:	31 c0                	xor    eax,eax
  40806c:	5b                   	pop    ebx
  40806d:	c3                   	ret    
  40806e:	90                   	nop
  40806f:	90                   	nop

00408070 <_signal>:
  408070:	ff 25 1c e2 40 00    	jmp    DWORD PTR ds:0x40e21c
  408076:	90                   	nop
  408077:	90                   	nop

00408078 <__setmode>:
  408078:	ff 25 d4 e1 40 00    	jmp    DWORD PTR ds:0x40e1d4
  40807e:	90                   	nop
  40807f:	90                   	nop

00408080 <___p__fmode>:
  408080:	ff 25 b8 e1 40 00    	jmp    DWORD PTR ds:0x40e1b8
  408086:	90                   	nop
  408087:	90                   	nop

00408088 <___p__environ>:
  408088:	ff 25 b4 e1 40 00    	jmp    DWORD PTR ds:0x40e1b4
  40808e:	90                   	nop
  40808f:	90                   	nop

00408090 <__cexit>:
  408090:	ff 25 c0 e1 40 00    	jmp    DWORD PTR ds:0x40e1c0
  408096:	90                   	nop
  408097:	90                   	nop

00408098 <___getmainargs>:
  408098:	ff 25 ac e1 40 00    	jmp    DWORD PTR ds:0x40e1ac
  40809e:	90                   	nop
  40809f:	90                   	nop

004080a0 <_clock>:
  4080a0:	ff 25 e8 e1 40 00    	jmp    DWORD PTR ds:0x40e1e8
  4080a6:	90                   	nop
  4080a7:	90                   	nop

004080a8 <_printf>:
  4080a8:	ff 25 10 e2 40 00    	jmp    DWORD PTR ds:0x40e210
  4080ae:	90                   	nop
  4080af:	90                   	nop

004080b0 <_strlen>:
  4080b0:	ff 25 28 e2 40 00    	jmp    DWORD PTR ds:0x40e228
  4080b6:	90                   	nop
  4080b7:	90                   	nop

004080b8 <_isspace>:
  4080b8:	ff 25 fc e1 40 00    	jmp    DWORD PTR ds:0x40e1fc
  4080be:	90                   	nop
  4080bf:	90                   	nop

004080c0 <_fwrite>:
  4080c0:	ff 25 f4 e1 40 00    	jmp    DWORD PTR ds:0x40e1f4
  4080c6:	90                   	nop
  4080c7:	90                   	nop

004080c8 <_vfprintf>:
  4080c8:	ff 25 30 e2 40 00    	jmp    DWORD PTR ds:0x40e230
  4080ce:	90                   	nop
  4080cf:	90                   	nop

004080d0 <_abort>:
  4080d0:	ff 25 d8 e1 40 00    	jmp    DWORD PTR ds:0x40e1d8
  4080d6:	90                   	nop
  4080d7:	90                   	nop

004080d8 <_memcpy>:
  4080d8:	ff 25 0c e2 40 00    	jmp    DWORD PTR ds:0x40e20c
  4080de:	90                   	nop
  4080df:	90                   	nop

004080e0 <_calloc>:
  4080e0:	ff 25 e4 e1 40 00    	jmp    DWORD PTR ds:0x40e1e4
  4080e6:	90                   	nop
  4080e7:	90                   	nop

004080e8 <_free>:
  4080e8:	ff 25 f0 e1 40 00    	jmp    DWORD PTR ds:0x40e1f0
  4080ee:	90                   	nop
  4080ef:	90                   	nop

004080f0 <_malloc>:
  4080f0:	ff 25 04 e2 40 00    	jmp    DWORD PTR ds:0x40e204
  4080f6:	90                   	nop
  4080f7:	90                   	nop

004080f8 <_tolower>:
  4080f8:	ff 25 2c e2 40 00    	jmp    DWORD PTR ds:0x40e22c
  4080fe:	90                   	nop
  4080ff:	90                   	nop

00408100 <_realloc>:
  408100:	ff 25 14 e2 40 00    	jmp    DWORD PTR ds:0x40e214
  408106:	90                   	nop
  408107:	90                   	nop

00408108 <_strcoll>:
  408108:	ff 25 24 e2 40 00    	jmp    DWORD PTR ds:0x40e224
  40810e:	90                   	nop
  40810f:	90                   	nop

00408110 <__errno>:
  408110:	ff 25 c4 e1 40 00    	jmp    DWORD PTR ds:0x40e1c4
  408116:	90                   	nop
  408117:	90                   	nop

00408118 <_setlocale>:
  408118:	ff 25 18 e2 40 00    	jmp    DWORD PTR ds:0x40e218
  40811e:	90                   	nop
  40811f:	90                   	nop

00408120 <_wcstombs>:
  408120:	ff 25 38 e2 40 00    	jmp    DWORD PTR ds:0x40e238
  408126:	90                   	nop
  408127:	90                   	nop

00408128 <_mbstowcs>:
  408128:	ff 25 08 e2 40 00    	jmp    DWORD PTR ds:0x40e208
  40812e:	90                   	nop
  40812f:	90                   	nop

00408130 <__fullpath>:
  408130:	ff 25 c8 e1 40 00    	jmp    DWORD PTR ds:0x40e1c8
  408136:	90                   	nop
  408137:	90                   	nop

00408138 <_fputc>:
  408138:	ff 25 ec e1 40 00    	jmp    DWORD PTR ds:0x40e1ec
  40813e:	90                   	nop
  40813f:	90                   	nop

00408140 <_localeconv>:
  408140:	ff 25 00 e2 40 00    	jmp    DWORD PTR ds:0x40e200
  408146:	90                   	nop
  408147:	90                   	nop

00408148 <_getenv>:
  408148:	ff 25 f8 e1 40 00    	jmp    DWORD PTR ds:0x40e1f8
  40814e:	90                   	nop
  40814f:	90                   	nop

00408150 <_wcslen>:
  408150:	ff 25 34 e2 40 00    	jmp    DWORD PTR ds:0x40e234
  408156:	90                   	nop
  408157:	90                   	nop

00408158 <_strchr>:
  408158:	ff 25 20 e2 40 00    	jmp    DWORD PTR ds:0x40e220
  40815e:	90                   	nop
  40815f:	90                   	nop

00408160 <_atoi>:
  408160:	ff 25 e0 e1 40 00    	jmp    DWORD PTR ds:0x40e1e0
  408166:	90                   	nop
  408167:	90                   	nop

00408168 <_SetUnhandledExceptionFilter@4>:
  408168:	ff 25 84 e1 40 00    	jmp    DWORD PTR ds:0x40e184
  40816e:	90                   	nop
  40816f:	90                   	nop

00408170 <_ExitProcess@4>:
  408170:	ff 25 50 e1 40 00    	jmp    DWORD PTR ds:0x40e150
  408176:	90                   	nop
  408177:	90                   	nop

00408178 <_GetModuleHandleA@4>:
  408178:	ff 25 68 e1 40 00    	jmp    DWORD PTR ds:0x40e168
  40817e:	90                   	nop
  40817f:	90                   	nop

00408180 <_GetProcAddress@8>:
  408180:	ff 25 6c e1 40 00    	jmp    DWORD PTR ds:0x40e16c
  408186:	90                   	nop
  408187:	90                   	nop

00408188 <_GetCommandLineA@0>:
  408188:	ff 25 60 e1 40 00    	jmp    DWORD PTR ds:0x40e160
  40818e:	90                   	nop
  40818f:	90                   	nop

00408190 <_VirtualQuery@12>:
  408190:	ff 25 94 e1 40 00    	jmp    DWORD PTR ds:0x40e194
  408196:	90                   	nop
  408197:	90                   	nop

00408198 <_VirtualProtect@16>:
  408198:	ff 25 90 e1 40 00    	jmp    DWORD PTR ds:0x40e190
  40819e:	90                   	nop
  40819f:	90                   	nop

004081a0 <_EnterCriticalSection@4>:
  4081a0:	ff 25 4c e1 40 00    	jmp    DWORD PTR ds:0x40e14c
  4081a6:	90                   	nop
  4081a7:	90                   	nop

004081a8 <_TlsGetValue@4>:
  4081a8:	ff 25 8c e1 40 00    	jmp    DWORD PTR ds:0x40e18c
  4081ae:	90                   	nop
  4081af:	90                   	nop

004081b0 <_GetLastError@0>:
  4081b0:	ff 25 64 e1 40 00    	jmp    DWORD PTR ds:0x40e164
  4081b6:	90                   	nop
  4081b7:	90                   	nop

004081b8 <_LeaveCriticalSection@4>:
  4081b8:	ff 25 7c e1 40 00    	jmp    DWORD PTR ds:0x40e17c
  4081be:	90                   	nop
  4081bf:	90                   	nop

004081c0 <_DeleteCriticalSection@4>:
  4081c0:	ff 25 48 e1 40 00    	jmp    DWORD PTR ds:0x40e148
  4081c6:	90                   	nop
  4081c7:	90                   	nop

004081c8 <_InitializeCriticalSection@4>:
  4081c8:	ff 25 70 e1 40 00    	jmp    DWORD PTR ds:0x40e170
  4081ce:	90                   	nop
  4081cf:	90                   	nop

004081d0 <_FindNextFileA@8>:
  4081d0:	ff 25 5c e1 40 00    	jmp    DWORD PTR ds:0x40e15c
  4081d6:	90                   	nop
  4081d7:	90                   	nop

004081d8 <_FindFirstFileA@8>:
  4081d8:	ff 25 58 e1 40 00    	jmp    DWORD PTR ds:0x40e158
  4081de:	90                   	nop
  4081df:	90                   	nop

004081e0 <_FindClose@4>:
  4081e0:	ff 25 54 e1 40 00    	jmp    DWORD PTR ds:0x40e154
  4081e6:	90                   	nop
  4081e7:	90                   	nop

004081e8 <_WideCharToMultiByte@32>:
  4081e8:	ff 25 98 e1 40 00    	jmp    DWORD PTR ds:0x40e198
  4081ee:	90                   	nop
  4081ef:	90                   	nop

004081f0 <_IsDBCSLeadByteEx@8>:
  4081f0:	ff 25 78 e1 40 00    	jmp    DWORD PTR ds:0x40e178
  4081f6:	90                   	nop
  4081f7:	90                   	nop

004081f8 <_MultiByteToWideChar@24>:
  4081f8:	ff 25 80 e1 40 00    	jmp    DWORD PTR ds:0x40e180
  4081fe:	90                   	nop
  4081ff:	90                   	nop

00408200 <_Sleep@4>:
  408200:	ff 25 88 e1 40 00    	jmp    DWORD PTR ds:0x40e188
  408206:	90                   	nop
  408207:	90                   	nop

00408208 <_InterlockedExchange@8>:
  408208:	ff 25 74 e1 40 00    	jmp    DWORD PTR ds:0x40e174
  40820e:	90                   	nop
  40820f:	90                   	nop

00408210 <___umoddi3>:
  408210:	55                   	push   ebp
  408211:	57                   	push   edi
  408212:	56                   	push   esi
  408213:	53                   	push   ebx
  408214:	83 ec 1c             	sub    esp,0x1c
  408217:	8b 44 24 3c          	mov    eax,DWORD PTR [esp+0x3c]
  40821b:	8b 4c 24 30          	mov    ecx,DWORD PTR [esp+0x30]
  40821f:	8b 6c 24 34          	mov    ebp,DWORD PTR [esp+0x34]
  408223:	8b 5c 24 38          	mov    ebx,DWORD PTR [esp+0x38]
  408227:	85 c0                	test   eax,eax
  408229:	89 c2                	mov    edx,eax
  40822b:	89 4c 24 0c          	mov    DWORD PTR [esp+0xc],ecx
  40822f:	89 ee                	mov    esi,ebp
  408231:	89 1c 24             	mov    DWORD PTR [esp],ebx
  408234:	89 4c 24 04          	mov    DWORD PTR [esp+0x4],ecx
  408238:	89 6c 24 08          	mov    DWORD PTR [esp+0x8],ebp
  40823c:	75 16                	jne    408254 <___umoddi3+0x44>
  40823e:	39 eb                	cmp    ebx,ebp
  408240:	76 4e                	jbe    408290 <___umoddi3+0x80>
  408242:	89 c8                	mov    eax,ecx
  408244:	89 ea                	mov    edx,ebp
  408246:	f7 f3                	div    ebx
  408248:	89 d0                	mov    eax,edx
  40824a:	31 d2                	xor    edx,edx
  40824c:	83 c4 1c             	add    esp,0x1c
  40824f:	5b                   	pop    ebx
  408250:	5e                   	pop    esi
  408251:	5f                   	pop    edi
  408252:	5d                   	pop    ebp
  408253:	c3                   	ret    
  408254:	39 e8                	cmp    eax,ebp
  408256:	77 58                	ja     4082b0 <___umoddi3+0xa0>
  408258:	0f bd f8             	bsr    edi,eax
  40825b:	83 f7 1f             	xor    edi,0x1f
  40825e:	75 60                	jne    4082c0 <___umoddi3+0xb0>
  408260:	8b 7c 24 04          	mov    edi,DWORD PTR [esp+0x4]
  408264:	39 3c 24             	cmp    DWORD PTR [esp],edi
  408267:	0f 87 e4 00 00 00    	ja     408351 <___umoddi3+0x141>
  40826d:	89 ef                	mov    edi,ebp
  40826f:	89 ce                	mov    esi,ecx
  408271:	29 de                	sub    esi,ebx
  408273:	19 c7                	sbb    edi,eax
  408275:	89 74 24 04          	mov    DWORD PTR [esp+0x4],esi
  408279:	89 7c 24 08          	mov    DWORD PTR [esp+0x8],edi
  40827d:	8b 44 24 04          	mov    eax,DWORD PTR [esp+0x4]
  408281:	8b 54 24 08          	mov    edx,DWORD PTR [esp+0x8]
  408285:	83 c4 1c             	add    esp,0x1c
  408288:	5b                   	pop    ebx
  408289:	5e                   	pop    esi
  40828a:	5f                   	pop    edi
  40828b:	5d                   	pop    ebp
  40828c:	c3                   	ret    
  40828d:	8d 76 00             	lea    esi,[esi+0x0]
  408290:	85 db                	test   ebx,ebx
  408292:	89 df                	mov    edi,ebx
  408294:	75 0b                	jne    4082a1 <___umoddi3+0x91>
  408296:	b8 01 00 00 00       	mov    eax,0x1
  40829b:	31 d2                	xor    edx,edx
  40829d:	f7 f3                	div    ebx
  40829f:	89 c7                	mov    edi,eax
  4082a1:	89 e8                	mov    eax,ebp
  4082a3:	31 d2                	xor    edx,edx
  4082a5:	f7 f7                	div    edi
  4082a7:	89 c8                	mov    eax,ecx
  4082a9:	f7 f7                	div    edi
  4082ab:	eb 9b                	jmp    408248 <___umoddi3+0x38>
  4082ad:	8d 76 00             	lea    esi,[esi+0x0]
  4082b0:	89 c8                	mov    eax,ecx
  4082b2:	89 ea                	mov    edx,ebp
  4082b4:	83 c4 1c             	add    esp,0x1c
  4082b7:	5b                   	pop    ebx
  4082b8:	5e                   	pop    esi
  4082b9:	5f                   	pop    edi
  4082ba:	5d                   	pop    ebp
  4082bb:	c3                   	ret    
  4082bc:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  4082c0:	8b 2c 24             	mov    ebp,DWORD PTR [esp]
  4082c3:	bb 20 00 00 00       	mov    ebx,0x20
  4082c8:	89 f9                	mov    ecx,edi
  4082ca:	29 fb                	sub    ebx,edi
  4082cc:	d3 e2                	shl    edx,cl
  4082ce:	89 d9                	mov    ecx,ebx
  4082d0:	89 e8                	mov    eax,ebp
  4082d2:	d3 e8                	shr    eax,cl
  4082d4:	89 f9                	mov    ecx,edi
  4082d6:	89 04 24             	mov    DWORD PTR [esp],eax
  4082d9:	89 e8                	mov    eax,ebp
  4082db:	d3 e0                	shl    eax,cl
  4082dd:	89 d9                	mov    ecx,ebx
  4082df:	89 c5                	mov    ebp,eax
  4082e1:	89 44 24 08          	mov    DWORD PTR [esp+0x8],eax
  4082e5:	8b 44 24 0c          	mov    eax,DWORD PTR [esp+0xc]
  4082e9:	09 14 24             	or     DWORD PTR [esp],edx
  4082ec:	89 f2                	mov    edx,esi
  4082ee:	d3 ea                	shr    edx,cl
  4082f0:	89 f9                	mov    ecx,edi
  4082f2:	d3 e6                	shl    esi,cl
  4082f4:	89 d9                	mov    ecx,ebx
  4082f6:	d3 e8                	shr    eax,cl
  4082f8:	89 f9                	mov    ecx,edi
  4082fa:	09 f0                	or     eax,esi
  4082fc:	8b 74 24 0c          	mov    esi,DWORD PTR [esp+0xc]
  408300:	f7 34 24             	div    DWORD PTR [esp]
  408303:	d3 e6                	shl    esi,cl
  408305:	89 74 24 04          	mov    DWORD PTR [esp+0x4],esi
  408309:	89 d6                	mov    esi,edx
  40830b:	f7 e5                	mul    ebp
  40830d:	39 d6                	cmp    esi,edx
  40830f:	89 c1                	mov    ecx,eax
  408311:	89 d5                	mov    ebp,edx
  408313:	72 2f                	jb     408344 <___umoddi3+0x134>
  408315:	39 44 24 04          	cmp    DWORD PTR [esp+0x4],eax
  408319:	72 25                	jb     408340 <___umoddi3+0x130>
  40831b:	8b 44 24 04          	mov    eax,DWORD PTR [esp+0x4]
  40831f:	29 c8                	sub    eax,ecx
  408321:	19 ee                	sbb    esi,ebp
  408323:	89 f9                	mov    ecx,edi
  408325:	89 f2                	mov    edx,esi
  408327:	d3 e8                	shr    eax,cl
  408329:	89 d9                	mov    ecx,ebx
  40832b:	d3 e2                	shl    edx,cl
  40832d:	89 f9                	mov    ecx,edi
  40832f:	d3 ee                	shr    esi,cl
  408331:	09 d0                	or     eax,edx
  408333:	89 f2                	mov    edx,esi
  408335:	83 c4 1c             	add    esp,0x1c
  408338:	5b                   	pop    ebx
  408339:	5e                   	pop    esi
  40833a:	5f                   	pop    edi
  40833b:	5d                   	pop    ebp
  40833c:	c3                   	ret    
  40833d:	8d 76 00             	lea    esi,[esi+0x0]
  408340:	39 d6                	cmp    esi,edx
  408342:	75 d7                	jne    40831b <___umoddi3+0x10b>
  408344:	89 d5                	mov    ebp,edx
  408346:	89 c1                	mov    ecx,eax
  408348:	2b 4c 24 08          	sub    ecx,DWORD PTR [esp+0x8]
  40834c:	1b 2c 24             	sbb    ebp,DWORD PTR [esp]
  40834f:	eb ca                	jmp    40831b <___umoddi3+0x10b>
  408351:	3b 44 24 08          	cmp    eax,DWORD PTR [esp+0x8]
  408355:	0f 82 12 ff ff ff    	jb     40826d <___umoddi3+0x5d>
  40835b:	e9 1d ff ff ff       	jmp    40827d <___umoddi3+0x6d>

00408360 <___udivdi3>:
  408360:	55                   	push   ebp
  408361:	57                   	push   edi
  408362:	56                   	push   esi
  408363:	53                   	push   ebx
  408364:	83 ec 14             	sub    esp,0x14
  408367:	8b 74 24 34          	mov    esi,DWORD PTR [esp+0x34]
  40836b:	8b 7c 24 28          	mov    edi,DWORD PTR [esp+0x28]
  40836f:	8b 6c 24 2c          	mov    ebp,DWORD PTR [esp+0x2c]
  408373:	8b 4c 24 30          	mov    ecx,DWORD PTR [esp+0x30]
  408377:	85 f6                	test   esi,esi
  408379:	89 3c 24             	mov    DWORD PTR [esp],edi
  40837c:	89 e8                	mov    eax,ebp
  40837e:	89 ca                	mov    edx,ecx
  408380:	75 2e                	jne    4083b0 <___udivdi3+0x50>
  408382:	39 e9                	cmp    ecx,ebp
  408384:	77 5c                	ja     4083e2 <___udivdi3+0x82>
  408386:	85 c9                	test   ecx,ecx
  408388:	89 cb                	mov    ebx,ecx
  40838a:	75 0b                	jne    408397 <___udivdi3+0x37>
  40838c:	b8 01 00 00 00       	mov    eax,0x1
  408391:	31 d2                	xor    edx,edx
  408393:	f7 f1                	div    ecx
  408395:	89 c3                	mov    ebx,eax
  408397:	89 e8                	mov    eax,ebp
  408399:	31 d2                	xor    edx,edx
  40839b:	f7 f3                	div    ebx
  40839d:	89 c5                	mov    ebp,eax
  40839f:	89 f8                	mov    eax,edi
  4083a1:	f7 f3                	div    ebx
  4083a3:	89 ea                	mov    edx,ebp
  4083a5:	83 c4 14             	add    esp,0x14
  4083a8:	5b                   	pop    ebx
  4083a9:	5e                   	pop    esi
  4083aa:	5f                   	pop    edi
  4083ab:	5d                   	pop    ebp
  4083ac:	c3                   	ret    
  4083ad:	8d 76 00             	lea    esi,[esi+0x0]
  4083b0:	39 ee                	cmp    esi,ebp
  4083b2:	77 22                	ja     4083d6 <___udivdi3+0x76>
  4083b4:	0f bd de             	bsr    ebx,esi
  4083b7:	83 f3 1f             	xor    ebx,0x1f
  4083ba:	75 36                	jne    4083f2 <___udivdi3+0x92>
  4083bc:	3b 0c 24             	cmp    ecx,DWORD PTR [esp]
  4083bf:	ba 00 00 00 00       	mov    edx,0x0
  4083c4:	0f 86 86 00 00 00    	jbe    408450 <___udivdi3+0xf0>
  4083ca:	39 ee                	cmp    esi,ebp
  4083cc:	0f 82 7e 00 00 00    	jb     408450 <___udivdi3+0xf0>
  4083d2:	31 c0                	xor    eax,eax
  4083d4:	eb cf                	jmp    4083a5 <___udivdi3+0x45>
  4083d6:	31 d2                	xor    edx,edx
  4083d8:	31 c0                	xor    eax,eax
  4083da:	83 c4 14             	add    esp,0x14
  4083dd:	5b                   	pop    ebx
  4083de:	5e                   	pop    esi
  4083df:	5f                   	pop    edi
  4083e0:	5d                   	pop    ebp
  4083e1:	c3                   	ret    
  4083e2:	89 f8                	mov    eax,edi
  4083e4:	89 ea                	mov    edx,ebp
  4083e6:	f7 f1                	div    ecx
  4083e8:	31 d2                	xor    edx,edx
  4083ea:	83 c4 14             	add    esp,0x14
  4083ed:	5b                   	pop    ebx
  4083ee:	5e                   	pop    esi
  4083ef:	5f                   	pop    edi
  4083f0:	5d                   	pop    ebp
  4083f1:	c3                   	ret    
  4083f2:	bf 20 00 00 00       	mov    edi,0x20
  4083f7:	89 d9                	mov    ecx,ebx
  4083f9:	29 df                	sub    edi,ebx
  4083fb:	89 d5                	mov    ebp,edx
  4083fd:	d3 e6                	shl    esi,cl
  4083ff:	89 f9                	mov    ecx,edi
  408401:	d3 ed                	shr    ebp,cl
  408403:	89 d9                	mov    ecx,ebx
  408405:	d3 e2                	shl    edx,cl
  408407:	09 f5                	or     ebp,esi
  408409:	89 54 24 04          	mov    DWORD PTR [esp+0x4],edx
  40840d:	8b 14 24             	mov    edx,DWORD PTR [esp]
  408410:	89 f9                	mov    ecx,edi
  408412:	89 c6                	mov    esi,eax
  408414:	d3 ee                	shr    esi,cl
  408416:	89 d9                	mov    ecx,ebx
  408418:	d3 e0                	shl    eax,cl
  40841a:	89 f9                	mov    ecx,edi
  40841c:	d3 ea                	shr    edx,cl
  40841e:	89 d7                	mov    edi,edx
  408420:	89 f2                	mov    edx,esi
  408422:	09 c7                	or     edi,eax
  408424:	89 f8                	mov    eax,edi
  408426:	f7 f5                	div    ebp
  408428:	89 d6                	mov    esi,edx
  40842a:	89 c7                	mov    edi,eax
  40842c:	f7 64 24 04          	mul    DWORD PTR [esp+0x4]
  408430:	39 d6                	cmp    esi,edx
  408432:	72 2c                	jb     408460 <___udivdi3+0x100>
  408434:	8b 2c 24             	mov    ebp,DWORD PTR [esp]
  408437:	89 d9                	mov    ecx,ebx
  408439:	d3 e5                	shl    ebp,cl
  40843b:	39 c5                	cmp    ebp,eax
  40843d:	73 04                	jae    408443 <___udivdi3+0xe3>
  40843f:	39 d6                	cmp    esi,edx
  408441:	74 1d                	je     408460 <___udivdi3+0x100>
  408443:	89 f8                	mov    eax,edi
  408445:	31 d2                	xor    edx,edx
  408447:	e9 59 ff ff ff       	jmp    4083a5 <___udivdi3+0x45>
  40844c:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  408450:	b8 01 00 00 00       	mov    eax,0x1
  408455:	e9 4b ff ff ff       	jmp    4083a5 <___udivdi3+0x45>
  40845a:	8d b6 00 00 00 00    	lea    esi,[esi+0x0]
  408460:	8d 47 ff             	lea    eax,[edi-0x1]
  408463:	31 d2                	xor    edx,edx
  408465:	83 c4 14             	add    esp,0x14
  408468:	5b                   	pop    ebx
  408469:	5e                   	pop    esi
  40846a:	5f                   	pop    edi
  40846b:	5d                   	pop    ebp
  40846c:	c3                   	ret    
  40846d:	90                   	nop
  40846e:	90                   	nop
  40846f:	90                   	nop

00408470 <_strdup>:
  408470:	ff 25 a0 e1 40 00    	jmp    DWORD PTR ds:0x40e1a0
  408476:	90                   	nop
  408477:	90                   	nop

00408478 <_stricoll>:
  408478:	ff 25 a4 e1 40 00    	jmp    DWORD PTR ds:0x40e1a4
  40847e:	90                   	nop
  40847f:	90                   	nop

00408480 <_main>:
  408480:	55                   	push   ebp
  408481:	89 e5                	mov    ebp,esp
  408483:	57                   	push   edi
  408484:	56                   	push   esi
  408485:	53                   	push   ebx
  408486:	bb a0 86 01 00       	mov    ebx,0x186a0
  40848b:	83 e4 f0             	and    esp,0xfffffff0
  40848e:	83 ec 60             	sub    esp,0x60
  408491:	e8 7a 99 ff ff       	call   401e10 <___main>
  408496:	8d 44 24 30          	lea    eax,[esp+0x30]
  40849a:	89 44 24 04          	mov    DWORD PTR [esp+0x4],eax
  40849e:	8d 44 24 20          	lea    eax,[esp+0x20]
  4084a2:	89 04 24             	mov    DWORD PTR [esp],eax
  4084a5:	8d 7c 24 50          	lea    edi,[esp+0x50]
  4084a9:	e8 f2 8f ff ff       	call   4014a0 <_encrypt>
  4084ae:	8d 74 24 40          	lea    esi,[esp+0x40]
  4084b2:	e8 e9 fb ff ff       	call   4080a0 <_clock>
  4084b7:	89 44 24 18          	mov    DWORD PTR [esp+0x18],eax
  4084bb:	90                   	nop
  4084bc:	8d 74 26 00          	lea    esi,[esi+eiz*1+0x0]
  4084c0:	89 7c 24 04          	mov    DWORD PTR [esp+0x4],edi
  4084c4:	89 34 24             	mov    DWORD PTR [esp],esi
  4084c7:	e8 d4 8f ff ff       	call   4014a0 <_encrypt>
  4084cc:	83 eb 01             	sub    ebx,0x1
  4084cf:	75 ef                	jne    4084c0 <_main+0x40>
  4084d1:	e8 ca fb ff ff       	call   4080a0 <_clock>
  4084d6:	c7 04 24 64 a0 40 00 	mov    DWORD PTR [esp],0x40a064
  4084dd:	2b 44 24 18          	sub    eax,DWORD PTR [esp+0x18]
  4084e1:	89 44 24 1c          	mov    DWORD PTR [esp+0x1c],eax
  4084e5:	db 44 24 1c          	fild   DWORD PTR [esp+0x1c]
  4084e9:	d8 35 7c a0 40 00    	fdiv   DWORD PTR ds:0x40a07c
  4084ef:	dd 5c 24 04          	fstp   QWORD PTR [esp+0x4]
  4084f3:	e8 b0 fb ff ff       	call   4080a8 <_printf>
  4084f8:	8d 65 f4             	lea    esp,[ebp-0xc]
  4084fb:	5b                   	pop    ebx
  4084fc:	5e                   	pop    esi
  4084fd:	5f                   	pop    edi
  4084fe:	5d                   	pop    ebp
  4084ff:	c3                   	ret    

00408500 <_register_frame_ctor>:
  408500:	55                   	push   ebp
  408501:	89 e5                	mov    ebp,esp
  408503:	83 ec 18             	sub    esp,0x18
  408506:	e8 f5 8d ff ff       	call   401300 <___gcc_register_frame>
  40850b:	c7 04 24 90 13 40 00 	mov    DWORD PTR [esp],0x401390
  408512:	e8 c9 8d ff ff       	call   4012e0 <_atexit>
  408517:	c9                   	leave  
  408518:	c3                   	ret    
  408519:	90                   	nop
  40851a:	90                   	nop
  40851b:	90                   	nop
  40851c:	90                   	nop
  40851d:	90                   	nop
  40851e:	90                   	nop
  40851f:	90                   	nop

00408520 <__CTOR_LIST__>:
  408520:	ff                   	(bad)  
  408521:	ff                   	(bad)  
  408522:	ff                   	(bad)  
  408523:	ff 00                	inc    DWORD PTR [eax]

00408524 <.ctors.65535>:
  408524:	00 85 40 00 00 00    	add    BYTE PTR [ebp+0x40],al
	...

0040852c <__DTOR_LIST__>:
  40852c:	ff                   	(bad)  
  40852d:	ff                   	(bad)  
  40852e:	ff                   	(bad)  
  40852f:	ff 00                	inc    DWORD PTR [eax]
  408531:	00 00                	add    BYTE PTR [eax],al
	...
