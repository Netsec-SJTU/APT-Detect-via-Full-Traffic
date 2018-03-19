rule DarkHotel : APT
{
    meta:
        ref1 = "https://www.virustotal.com/hu/file/de4ff8901766e8fc89e8443f8732394618bf925ce29b6a8aafe1d60f496e7f0e/analysis/"
        ref2 = "http://securelist.com/blog/research/66779/the-darkhotel-apt/"
        ref3 = "https://blog.kaspersky.com/darkhotel-apt/6613/"
    strings:
        $service1 = "HP003044" nocase wide
        $service2 = "NetBIOS2010" nocase wide
        $file1 = "SYSTEMROOT\\winver32.exe" nocase wide
        $file2 = "SYSPATH\\actmove.exe" nocase wide
        $file3 = "SYSPATH\\appned.exe" nocase wide
        $file4 = "SYSPATH\\boof.exe" nocase wide
        $file5 = "SYSPATH\\gflash.exe" nocase wide
        $file6 = "SYSPATH\\lnetcpl.exe" nocase wide
        $file7 = "SYSPATH\\qernet.exe" nocase wide
        $file8 = "SYSPATH\\serves.exe" nocase wide
        $file9 = "SYSPATH\\secury.exe" nocase wide
        $file10 = "SYSPATH\\webhelp.exe" nocase wide
        $file11 = "SYSPATH\\autocheck.exe" nocase wide
        $file12 = "SYSPATH\\xflash.exe" nocase wide
        $file13 = "SYSPATH\\inetcpl.exe" nocase wide
        $file14 = "SYSPATH\\activemov.exe" nocase wide
        $file15 = "SYSPATH\\xmlhelp.exe" nocase wide
        $file16 = "SYSPATH\\winspooler.exe" nocase wide
        $file17 = "SYSPATH\\xsocket.exe" nocase wide
        $file18 = "SYSPATH\\actmove.exe" nocase wide
        $file19 = "SYSPATH\\appned.exe" nocase wide
        $file20 = "SYSPATH\\qernet.exe" nocase wide
        $file21 = "SYSPATH\\boof.exe" nocase wide
        $file22 = "SYSPATH\\gflash.exe" nocase wide
        $file23 = "SYSPATH\\lnetcpl.exe" nocase wide
        $file24 = "SYSPATH\\serves.exe" nocase wide
        $file25 = "SYSPATH\\secury.exe" nocase wide
        $file26 = "SYSPATH\\actmove.exe" nocase wide
        $file27 = "SYSPATH\\appned.exe" nocase wide
        $file28 = "SYSPATH\\boof.exe" nocase wide
        $file29 = "SYSPATH\\gflash.exe" nocase wide
        $file30 = "SYSPATH\\lnetcpl.exe" nocase wide
        $file31 = "SYSPATH\\qernet.exe" nocase wide
        $file32 = "SYSPATH\\serves.exe" nocase wide
        $file33 = "SYSPATH\\secury.exe" nocase wide
        $file34 = "SYSPATH\\actmove.sys" nocase wide
        $file35 = "SYSPATH\\appned.sys" nocase wide
        $file36 = "SYSPATH\\boof.sys" nocase wide
        $file37 = "SYSPATH\\gflash.sys" nocase wide
        $file38 = "SYSPATH\\lnetcpl.sys" nocase wide
        $file39 = "SYSPATH\\qernet.sys" nocase wide
        $file41 = "SYSPATH\\serves.sys" nocase wide
        $file42 = "SYSPATH\\secury.sys" nocase wide
        $file43 = "SYSPATH\\webhelp.sys" nocase wide
        $file44 = "SYSPATH\\autocheck.sys" nocase wide
        $file45 = "SYSPATH\\xflash.sys" nocase wide
        $file46 = "SYSPATH\\inetcpl.sys" nocase wide
        $file47 = "SYSPATH\\activemov.sys" nocase wide
        $file48 = "SYSPATH\\xmlhelp.sys" nocase wide
        $file49 = "SYSPATH\\winspooler.sys" nocase wide
        $file50 = "SYSPATH\\xsocket.sys file" nocase wide
        $file51 = "SYSPATH\\actmove.sys" nocase wide
        $file52 = "SYSPATH\\appned.sys" nocase wide
        $file53 = "SYSPATH\\qernet.sys" nocase wide
        $file54 = "SYSPATH\\boof.sys" nocase wide
        $file55 = "SYSPATH\\gflash.sys" nocase wide
        $file56 = "SYSPATH\\lnetcpl.sys" nocase wide
        $file57 = "SYSPATH\\serves.sys" nocase wide
        $file58 = "SYSPATH\\secury.sys" nocase wide
        $file59 = "SYSPATH\\actmove.sys" nocase wide
        $file60 = "SYSPATH\\appned.sys" nocase wide
        $file61 = "SYSPATH\\boof.sys" nocase wide
        $file62 = "SYSPATH\\gflash.sys" nocase wide
        $file63 = "SYSPATH\\lnetcpl.sys" nocase wide
        $file64 = "SYSPATH\\qernet.sys" nocase wide
        $file65 = "SYSPATH\\serves.sys" nocase wide
        $file66 = "SYSPATH\\secury.sys" nocase wide
        $file67 = "SYSPATH\\DivXfix.dll" nocase wide
        $file68 = "SYSPATH\\dbdebug.dll" nocase wide
        $file69 = "SYSPATH\\countryfix.dll" nocase wide
        $file70 = "SYSPATH\\cdboot.dll" nocase wide
        $file71 = "SYSPATH\\bitcheck.dll" nocase wide
        $file72 = "SYSPATH\\biosfix.dll" nocase wide
        $file73 = "SYSPATH\\actproxy.dll" nocase wide
        $file74 = "SYSPATH\\activems.dll" nocase wide
        $file75 = "SYSPATH\\dbdebug.dll" nocase wide
        $file76 = "SYSPATH\\countryfix.dll" nocase wide
        $file77 = "SYSPATH\\cdboot.dll" nocase wide
        $file78 = "SYSPATH\\bitcheck.dll" nocase wide
        $file79 = "SYSPATH\\DivXfix.dll" nocase wide
        $file80 = "SYSPATH\\biosfix.dll" nocase wide
        $file81 = "SYSPATH\\actproxy.dll" nocase wide
        $file82 = "SYSPATH\\dsound4d.dll" nocase wide
        $file83 = "SYSPATH\\actmove.dll" nocase wide
        $file84 = "SYSPATH\\appned.dll" nocase wide
        $file85 = "SYSPATH\\qernet.dll" nocase wide
        $file86 = "SYSPATH\\boof.dll" nocase wide
        $file87 = "SYSPATH\\gflash.dll" nocase wide
        $file88 = "SYSPATH\\lnetcpl.dll" nocase wide
        $file89 = "SYSPATH\\serves.dll" nocase wide
        $file90 = "SYSPATH\\secury.dll" nocase wide
        $file91 = "SYSPATH\\actmove.dll" nocase wide
        $file92 = "SYSPATH\\appned.dll" nocase wide
        $file93 = "SYSPATH\\boof.dll" nocase wide
        $file94 = "SYSPATH\\gflash.dll" nocase wide
        $file95 = "SYSPATH\\lnetcpl.dll" nocase wide
        $file96 = "SYSPATH\\qernet.dll" nocase wide
        $file97 = "SYSPATH\\serves.dll" nocase wide
        $file98 = "SYSPATH\\secury.dll" nocase wide
        $driver1 = "activemov.sys" nocase wide
        $driver2 = "activems.sys" nocase wide
        $driver3 = "actmove.sys" nocase wide
        $driver4 = "actproxy.sys" nocase wide
        $driver5 = "appned.sys" nocase wide
        $driver6 = "autocheck.sys" nocase wide
        $driver7 = "biosfix.sys" nocase wide
        $driver8 = "bitcheck.sys" nocase wide
        $driver9 = "boof.sys" nocase wide
        $driver10 = "cdboot.sys" nocase wide
        $driver11 = "countryfix.sys" nocase wide
        $driver12 = "dbdebug.sys" nocase wide
        $driver13 = "divxfix.sys" nocase wide
        $driver14 = "dsound4d.sys" nocase wide
        $driver15 = "gflash.sys" nocase wide
        $driver16 = "lnetcpl.sys" nocase wide
        $driver17 = "qernet.sys" nocase wide
        $driver18 = "secury.sys" nocase wide
        $driver19 = "serves.sys" nocase wide
        $driver20 = "webhelp.sys" nocase wide
        $driver21 = "winspooler.sys" nocase wide
        $driver22 = "xflash.sys" nocase wide
        $driver23 = "xmlhelp.sys" nocase wide
        $driver24 = "xsocket.sys" nocase wide
    condition:
        any of them
        //5 of them
}