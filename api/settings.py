# coding: utf-8

import platform
import os
import sys
from pprint import pprint
import _winreg

from resourceIDs import MAX_VERSION_IDS
from resourceIDs import NUKE_VERSION_IDS
from resourceIDs import XSI_VERSION_IDS
from resourceIDs import MAYA_VERSION_IDS
from resourceIDs import SYSTEM_TYPE
from resourceIDs import SW_TYPE_IDS

MAYA_VERSION_LIST = []
MAX_VERSION_LIST = []
NUKE_VERSION_LIST = []
XSI_VERSION_LIST = []


class SwModel:
    SWID = None
    VERSION = None
    sw_path_1 = None
    sw_path_2 = None



regedit = "C:/Windows/regedit.exe"

class VersionCheck(object):

    @staticmethod
    def Maya():

        MayaVersion = []

        version_list = (
            ( MAYA_VERSION_IDS.IDS_MAYA_2012, 'Software\\Autodesk\\Maya\\2012\\Setup\\InstallPath'),
            ( MAYA_VERSION_IDS.IDS_MAYA_2013, 'Software\\Autodesk\\Maya\\2013\\Setup\\InstallPath'),
            ( MAYA_VERSION_IDS.IDS_MAYA_2014, 'Software\\Autodesk\\Maya\\2014\\Setup\\InstallPath'),
            ( MAYA_VERSION_IDS.IDS_MAYA_2015, 'Software\\Autodesk\\Maya\\2015\\Setup\\InstallPath'),
            ( MAYA_VERSION_IDS.IDS_MAYA_2016, 'Software\\Autodesk\\Maya\\2016\\Setup\\InstallPath')
        )

        for v in version_list:
            try:
                key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, v[1])
                value =  _winreg.QueryValueEx(key, "MAYA_INSTALL_LOCATION")[0]+'bin'

                smodel = SwModel()
                smodel.SWID = SW_TYPE_IDS.IDS_SW_MAYA
                smodel.sw_path_1 = value
                smodel.VERSION = v[0]

                MayaVersion.append( smodel)
            except:
                pass
        #print MayaVersion
        return MayaVersion

    @staticmethod
    def Nuke():

        NukeVersion = []
        version_list = ( NUKE_VERSION_IDS.IDS_NUKE_7, "NukeScript\\shell\\open\\command\\")

        try:

            key = _winreg.OpenKey(_winreg.HKEY_CLASSES_ROOT, version_list[1])
            value = _winreg.QueryValueEx(key,'')[0]
            cut = ' '+value.split(' ')[-1]

            smodel = SwModel()
            smodel.SWID = SW_TYPE_IDS.IDS_SW_NUKE
            smodel.VERSION = version_list[0]
            smodel.sw_path_1 = value.rstrip(cut)
            smodel.sw_path_2 = value.rstrip(cut)+' --nukex'

            #NukeVersion.append(value.rstrip(cut))
            #NukeVersion.append(value.rstrip(cut)+' --nukex')
            NukeVersion.append(smodel)

        except:
            pass

        return NukeVersion

    @staticmethod
    def Xsi():
        XsiVersion = []
        version_list = (
            ( XSI_VERSION_IDS.IDS_XSI_2012 ,'2012'),
            ( XSI_VERSION_IDS.IDS_XSI_2013, '2013'),
            ( XSI_VERSION_IDS.IDS_XSI_2014, '2014'),
            ( XSI_VERSION_IDS.IDS_XSI_2015, '2015')
        )
        for v in version_list:
            try:
                VersionPath = "Software\\Autodesk\\Softimage\\InstallPaths\\"
                key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, VersionPath)
                value = _winreg.QueryValueEx(key,v[1])[0]

                smodel = SwModel()
                smodel.SWID = SW_TYPE_IDS.IDS_SW_XSI
                smodel.VERSION = v[0]
                smodel.sw_path_1 = value
                XsiVersion.append(smodel)

            except:
                pass
        return XsiVersion


    @staticmethod
    def Max():
        MaxVersion = []
        #2012
        version_list = (
            ( MAX_VERSION_IDS.IDS_MAX_2012, 'Software\\Autodesk\\3dsMax\\14.0\\MAX-1:409\\'),
            ( MAX_VERSION_IDS.IDS_MAX_2015, 'Software\\Autodesk\\3dsMax\\17.0\\' )
        )

        for v in version_list:
            try:
                key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, v[1])
                value = _winreg.QueryValueEx(key,'Installdir')[0]

                smodel = SwModel()
                smodel.SWID = SW_TYPE_IDS.IDS_SW_MAX
                smodel.VERSION = v[0]
                smodel.sw_path_1 = value

                MaxVersion.append(smodel)

            except:
                pass

        return MaxVersion

    @staticmethod
    def Python():
        PythonInstallPath = []
        VersionPath = "Software\\Python\\PythonCore\\2.6\\InstallPath"
        key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, VersionPath)
        value = _winreg.QueryValueEx(key,'')[0]
        PythonInstallPath.append(value)
        return PythonInstallPath

# MAC OSX
def set_sys_osx():
    pass

# WINDOWS
def set_sys_window():

    global MAYA_VERSION_LIST
    global MAX_VERSION_LIST
    global XSI_VERSION_LIST
    global NUKE_VERSION_LIST

    MAYA_VERSION_LIST = VersionCheck.Maya()
    '''
    if (MAYA_VERSION_LIST):
        for mv in MAYA_VERSION_LIST:
            print mv.VERSION
            print mv.sw_path_1
            '''

    XSI_VERSION_LIST = VersionCheck.Xsi()
    NUKE_VERSION_LIST = VersionCheck.Nuke()
    #print VersionCheck.Python()

    MAX_VERSION_LIST = VersionCheck.Max()
    '''
    if (MAX_VERSION_LIST):
        for mx in MAX_VERSION_LIST:
            print mx.VERSION
            print mx.sw_path_1
            '''

#------------------------------------------#

sys = {'Windows':SYSTEM_TYPE.SYS_WINDOWS,
       'Darwin':SYSTEM_TYPE.SYS_OSX}

SYSTEM_INFO = sys.get(platform.system())

switch = {
          SYSTEM_TYPE.SYS_WINDOWS:set_sys_window,
          SYSTEM_TYPE.SYS_OSX:set_sys_osx
          }


f = switch.get(SYSTEM_INFO)
f()
