# -*- coding: utf-8 -*-
import os
import sys
import time
# import platform
# import checkos
# oscheck = checkos.ClientOs()
# sys.path.append(oscheck.syspath)




from wormholeAPI.whDataModels import whEnvData
from wormholeAPI.whAPIModels import whCompany

class GetInfo:
    def __init__(self, envfile):
        self.envfile = envfile
        self.pathrools = {}

        self.whcom = whCompany()
        # self.envs()
        # self.pathrool()
        # self.paths()

        # print oscheck.userPath
        # print oscheck.getOSType
        # print oscheck.whAppPath


        self.env = whEnvData(self.envfile)

    def pathrool(self):

        # self.whcom.setCompanyId(self.env.Company)

        self.whcom.setCompanyId(self.env.Company)
        for project in self.whcom.project_list:
            if project.projectId == self.env.Project:
                self.pathrools = project.paths.__dict__
        return self.pathrools

    def paths(self):
        self.whcom.setEnvFile(self.envfile)
        self.whProjectPath = self.whcom.project_id[self.env.Project]

        nowTime = time.strftime("%Y.%m.%d_%H_%M", time.localtime())

        # self.whProjectPath.paths.customReplaceEnv('DATE',nowTime)
        # self.whProjectPath.paths.customReplaceEnv('VERSIONNUMBER',datatype)
        # self.whProjectPath.paths.customReplaceEnv('PDATATYPE',version)
        # self.whProjectPath.paths.customReplaceEnv('[PUBLISHER]','TEST')

        return self.whProjectPath.paths.__dict__



from pprint import pprint
whenv = GetInfo('./wormHole.env')
pprint(whenv.pathrool())
pprint(whenv.paths())


#
#
# from wormholeAPI.whAPIModels import whCompany
# from wormholeAPI.whDataModels import whEnvData
# from wormholeAPI.whDataModels import whProjectData
# envFile = u'z:/192.168.0.11/local/161207/A_C/实拍/c3m//wormHole.env'
# whcom = whCompany()
# projindex = None
#
#
# whcom.setEnvFile(envFile)
# env = whEnvData(envFile)
# print type(env.TaskType)
# whcom.setCompanyId(env.Company)
# whProjectPath = whcom.project_id[env.Project]
# print whProjectPath.paths.fixShotMovPath

#
# envFile = os.path.abspath('')+'/wormHole.env'
# whcom = whCompany()
# projindex = None
#
#
# whcom.setEnvFile(envFile)
# env = whEnvData(envFile)
# whcom.setCompanyId(env.Company)
# whProjectPath = whcom.project_id[env.Project]
# nowTime = time.strftime("%Y.%m.%d_%H_%M",time.localtime())
# whProjectPath.paths.customReplaceEnv('DATE',nowTime)
# PATH = whProjectPath.paths
# #print whcom.project_id[env.Project].paths.__dict__
#
# # define the wormhole.env setting values
# serverAddress = env.ServerName # demo.wormholepipeline.com
# corpPrefix = env.Company    # demo
# projectId = env.Project    # MtTam
# DirTypeId = env.DirType    # shot / asset
# GetUserID  = env.UserID    # user ID
# GetTaskType  = env.TaskType     # tasktype name
# GetFileServerPath = env.ProjectHome     # file server path
# OS = env.OS
# GetTaskTypeCode = env.TaskTypeCode
# if (DirTypeId == 'shot'):
#     GetSeqName  = env.SeqName    # Sequence name
#     GetShotName  = env.ShotName     # Shot name
#     GetFirstFrame  =env.FirstFrame     # first frame
#     GetLastFrame  = env.LastFrame     # last frame
#
#
# if (DirTypeId == 'asset'):
#     getFirstFrame = ''
#     getLastFrame = ''
#     GetAssetName  = env.AssetName
#     GetAssetPrefix  = env.AssetPrefix
#


