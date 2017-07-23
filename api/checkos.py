# -*- coding: utf-8 -*-
import sys
import os
import platform

class ClientOs():
    def __init__(self):
        self.whAppPath = ''
        self.getOSType = ''
        self.userPath = os.path.join(os.path.expanduser("~"), 'wormhole','presets')
        if platform.system() == 'Windows':
            import _winreg
            key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,'SOFTWARE\\Classes\\WHPlugin\\shell\\open\\command',0,_winreg.KEY_READ)
            (value, valuetype) = _winreg.QueryValueEx(key, 'Path')
            # path =  value.replace('\\','/').replace('//','/')
            self.syspath = os.path.join(value,'bin','wormhole_api','whpy')

            self.whAppPath = os.path.join(value,'bin','whApp')
            self.getOSType = 'WINDOWS'

        elif platform.system() == 'Linux':
            import getpass
            import subprocess
            sys.path.append('/usr/local/bin/WHPlugin/bin/wormhole_api/whpy')
            self.whAppPath = '/usr/local/bin/WHPlugin/bin/whApp'
            self.getOSType = 'LINUX'
            systemuser = getpass.getuser()


        elif platform.system() == 'Darwin':
            pass
