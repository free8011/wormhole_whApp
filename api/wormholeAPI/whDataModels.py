# coding: utf-8

from api.resourceIDs import WH_CASE_IDS
from api.resourceIDs import WH_PATH_MAP
from api.resourceIDs import WH_PROJECT_MODE
from urlModels import USE_URL_CUSTOM
from datetime import datetime
from types import *
import urllib
import os

class whData(object):
    TID = None
    projectId = None
    fileServePath = None
    versionInfo = None
    sequenceId = None
    sequenceNm = None

    assetList = None
    versionNumber = None
    taskTypeCd = None
    taskTypeNm = None
    publishDt = None
    file = None
    movie = None
    originalFilePath = None
    originalMoviePath = None
    publisherId = None
    publisherNm = None


    projectNm = None
    shotNm = None
    shotId = None
    snapShot = None
    startDt = None
    endDt = None
    comment = None
    coordinatorId = None
    publishHistory = None

    assetId = None
    assetNm = None

    fileHiRes = None
    fileAnimRes = None
    fileLowRes = None
    isLast = None
    publishInfo = None
    pubDate = None

    tag = None
    status = None
    ownerId = None
    leaserId = None
    coordinatorId = None



'''
class whTaskData(object):
    def __init__(self, dict_ = None):
        self.TID = WH_CASE_IDS.WH_TASK

    def setDict(self, dict_):
        if dict_:

            self.task_dict = dict_

    def getTaskDict(self):
        return self.task_dict

    def getTaskID(self, id_):
        self.task_dict.get(id_, None)
'''


class whMemberData(object):
    def __init__(self, dict_ = None):
        self.TID = WH_CASE_IDS.WH_MEMBER
        self.userId = None
        self.userName = None

        self._taskType = None
        self._userType = None
        self._userSkills = None
        self._userTeam = None
        self._userPhoto = None
        self._userEmail = None
        self._userOfficeTelNm = None
        self._userMobileNm = None
        self._userSkypeId = None
        self._userHistory = None

        self.setDict(dict_)

    def setDict(self, dict_):
        if dict_:
            if dict_.has_key('userId'): self.userId = dict_['userId']
            if dict_.has_key('userName'): self.userName = dict_['userName']

            if dict_.has_key('taskType'): self._taskType = dict_['taskType']
            if dict_.has_key('userType'): self._userType = dict_['userType']
            if dict_.has_key('userSkills'): self._userSkills = dict_['userSkills']
            if dict_.has_key('userTeam'): self._userTeam = dict_['userTeam']
            if dict_.has_key('userPhoto'): self._userPhoto = dict_['userPhoto']
            if dict_.has_key('userEmail'): self._userEmail = dict_['userEmail']
            if dict_.has_key('userOfficeTelNm'): self._userOfficeTelNm = dict_['userOfficeTelNm']
            if dict_.has_key('userMobileNm'): self._userMobileNm = dict_['userMobileNm']
            if dict_.has_key('userSkypeId'): self._userSkypeId = dict_['userSkypeId']


class whCompanyData(whData):
    def __init__(self):
        self.TID = WH_CASE_IDS.WH_COMPANY



class whProjectData(whData):
    def __init__(self, dict_ = None):
        self.TID = WH_CASE_IDS.WH_PROJECT
        self.setDict(dict_)

    def setDict(self, dict_):
        if dict_:
            self.projectId = dict_['projectId']
            self.fileServePath = dict_['fileServePath']
            if dict_['versionInfo']:
                self.versionInfo = float(dict_['versionInfo'])
            else:
                self.versionInfo = None

    def getDict(self):
        rnt_ = {}
        rnt_['projectId'] = self.projectId
        rnt_['fileServePath'] = self.fileServePath
        rnt_['versionInfo'] = self.versionInfo
        return rnt_

class whSequenceData(whData):
    def __init__(self, dict_ = None):
        self.TID = WH_CASE_IDS.WH_SEQUENCE
        self.setDict(dict_)

    def setDict(self, dict_):
        if dict_:
            self.sequenceId = dict_['sequenceId']
            self.sequenceNm = dict_['sequenceNm']

    def getDict(self):
        rnt_ = {}
        rnt_['sequenceId'] = self.sequenceId
        rnt_['sequenceNm'] = self.sequenceNm
        return rnt_

class whShotHistData(whData):
    def __init__(self, dict_ = None):
        self.TID = WH_CASE_IDS.WH_SHOT_HIST
        self.setDict(dict_)

    def setDict(self, dict_):
        if dict_:
            if dict_.has_key('assetList') : self.assetList = dict_['assetList']
            if dict_.has_key('versionNumber') : self.versionNumber = dict_['versionNumber']
            if dict_.has_key('taskTypeCd') : self.taskTypeCd = dict_['taskTypeCd']
            if dict_.has_key('taskTypeNm') : self.taskTypeNm = dict_['taskTypeNm']
            if dict_.has_key('publishDt') : self.publishDt = dict_['publishDt']
            if dict_.has_key('file') : self.file = dict_['file']
            if dict_.has_key('movie') : self.movie = dict_['movie']
            if dict_.has_key('originalFilePath') : self.originalFilePath = dict_['originalFilePath']
            if dict_.has_key('originalMoviePath') : self.originalMoviePath = dict_['originalMoviePath']
            if dict_.has_key('publisherId') : self.publisherId = dict_['publisherId']
            if dict_.has_key('publisherNm') : self.publisherNm = dict_['publisherNm']



class whShotData(whData):
    def __init__(self, dict_ = None):
        self.TID = WH_CASE_IDS.WH_SHOT
        self.setDict(dict_)

    def setDict(self, dict_):
        if dict_:
            if dict_.has_key('shotNm') : self.shotNm = dict_['shotNm']
            if dict_.has_key('snapShot') : self.snapShot = dict_['snapShot']
            if dict_.has_key('startDt') : self.startDt = dict_['startDt']
            if dict_.has_key('endDt') : self.endDt = dict_['endDt']
            if dict_.has_key('comment') : self.comment = dict_['comment']
            if dict_.has_key('coordinatorId') : self.coordinatorId = dict_['coordinatorId']
            if dict_.has_key('shotId') : self.shotId = dict_['shotId']


class whAssetHistData(whData):
    def __init__(self, dict_ = None):
        self.TID = WH_CASE_IDS.WH_ASSET_HIST
        self.setDict(dict_)

    def setDict(self, dict_):
        if dict_:
            if dict_.has_key('versionNumber') : self.versionNumber = dict_['versionNumber']
            if dict_.has_key('taskTypeCd') : self.taskTypeCd = dict_['taskTypeCd']
            if dict_.has_key('taskTypeNm') : self.taskTypeNm = dict_['taskTypeNm']
            if dict_.has_key('file') : self.file = dict_['file']
            if dict_.has_key('fileHiRes') : self.fileHiRes = dict_['fileHiRes']
            if dict_.has_key('fileAnimRes') : self.fileAnimRes = dict_['fileAnimRes']
            if dict_.has_key('fileLowRes') : self.fileLowRes = dict_['fileLowRes']
            if dict_.has_key('movie') : self.movie = dict_['movie']
            if dict_.has_key('isLast') : self.isLast = dict_['isLast']
            if dict_.has_key('publishInfo') : self.publishInfo = dict_['publishInfo']
            if dict_.has_key('publisherId') : self.publisherId = dict_['publisherId']
            if dict_.has_key('pubDate') : self.pubDate = dict_['pubDate']




class whAssetData(whData):
    def __init__(self, dict_ = None):
        self.TID = WH_CASE_IDS.WH_ASSET
        self.setDict(dict_)

    def setDict(self, dict_):
        if dict_:
            if dict_.has_key('assetId') : self.assetId = dict_['assetId']
            if dict_.has_key('assetNm') : self.assetNm = dict_['assetNm']
            if dict_.has_key('snapShot') : self.snapShot = dict_['snapShot']

            if dict_.has_key('tag') : self.tag = dict_['tag']
            if dict_.has_key('startDt') : self.startDt = dict_['startDt']
            if dict_.has_key('endDt') : self.endDt = dict_['endDt']
            if dict_.has_key('status') : self.status = dict_['status']
            if dict_.has_key('comment') : self.comment = dict_['comment']
            if dict_.has_key('ownerId') : self.ownerId = dict_['ownerId']
            if dict_.has_key('leaserId') : self.leaserId = dict_['leaserId']
            if dict_.has_key('coordinatorId') : self.coordinatorId = dict_['coordinatorId']

class whAssetRData(object):
    def __init__(self):
        self.TID = WH_CASE_IDS.WH_RECORD_ASSET

        self._corpPrefix = None
        self._projectId = None
        self._userId = None
        self._taskTypeCd = None
        self._assetId = None
        self._assetVersion = None
        self._workType = None
        self._shotNm = None
        self._assetNm = None
        self._workingAssetDir = None
        self._workingShotDir = None

    @property
    def corpPrefix(self):
        return self._corpPrefix

    @corpPrefix.setter
    def corpPrefix(self, value):
        self._corpPrefix = value

    @property
    def projectId(self):
        return self._projectId

    @projectId.setter
    def projectId(self, value):
        self._projectId = value

    @property
    def userId(self):
        return self._userId

    @userId.setter
    def userId(self, value):
        self._userId = value

    @property
    def taskTypeCd(self):
        return self._taskTypeCd

    @taskTypeCd.setter
    def taskTypeCd(self, value):
        self._taskTypeCd = value

    @property
    def assetId(self):
        return self._assetId

    @assetId.setter
    def assetId(self, value):
        self._assetId = value

    @property
    def assetVersion(self):
        return self._assetVersion

    @assetVersion.setter
    def assetVersion(self, value):
        self._assetVersion = value

    @property
    def workType(self):
        return self._workType

    @workType.setter
    def workType(self, value):
        self._workType = value

    @property
    def shotNm(self):
        return self._shotNm

    @shotNm.setter
    def shotNm(self, value):
        self._shotNm = value

    @property
    def assetNm(self):
        return self._assetNm

    @shotNm.setter
    def assetNm(self, value):
        self._assetNm = value

    @property
    def workingAssetDir(self):
        return self._workingAssetDir

    @workingAssetDir.setter
    def workingAssetDir(self, value):
        self._workingAssetDir = value

    @property
    def workingShotDir(self):
        return self._workingShotDir

    @workingShotDir.setter
    def workingShotDir(self, value):
        self._workingShotDir = value



class whEnvData(object):
    def __init__(self, filepath):
        self.UserHome = None
        self.ProjectHome = None
        self.ServerName = None
        self.Company = None
        self.OS = None
        self.Project = None
        self.WormholeBin = None
        self.DirType = None
        self.TaskType = None
        self.TaskTypeCode = None
        self.UserID = None
        self.Uemail = None
        self.Ucontact = None
        self.AssetName = None
        self.AssetPrefix = None
        self.AssetWorkingDir = None
        self.PreviewRenderDir = None
        self.LogDir = None
        self.EditDB = None
        self.xsiAssetModelDir = None
        self.xsiAssetWorkingDir = None
        self.xsiAssetMovieDir = None
        self.xsiModelServerDir = None
        self.xsiModelMovieServerDir = None
        self.WormholePythonModule = None

        self.SeqName = None
        self.ShotName = None
        self.ShotWorkingDir = None
        self.FirstFrame = None
        self.LastFrame = None
        self.RenderSize = None
        self.LoRenderSize = None
        self.xsiShotWorkingDir = None
        self.xsiShotMovieDir = None
        self.xsiShotServerDir = None
        self.xsiShotMovieServerDir = None

        self.WindowsFileServerHome = None
        self.LinuxFileServerHome = None

        if os.path.exists(filepath):
            self.readFile(filepath)

    def readFile(self, filename):
        self.ENV_PROJECT_MODE = None
        search_list = [x for x in self.__dict__.keys() if '__' not in x]
        f = open(filename, 'r')
        text = f.read()
        f.close()
        for line_ in text.splitlines():
            if line_ and line_[0] != '#':
                for v in search_list:
                    if line_.split('=')[0].strip() == v:
                        rnt_ = line_.split('=')
                        code = compile('self.%s = "%s"' % (v, rnt_[1].strip()), '<string>', 'exec')
                        exec code

        self.WormholeBin = self.WormholeBin % {
            'ProjectHome':self.ProjectHome,
            'Company':self.Company,
            'Project':self.Project
        }
        self.EditDB = self.EditDB % {
            'ProjectHome':self.ProjectHome,
            'Company':self.Company,
            'Project':self.Project
        }
        self.WormholePythonModule = self.WormholePythonModule % {
            'ProjectHome':self.ProjectHome,
            'Company':self.Company,
            'Project':self.Project
        }
        if self.DirType == 'asset':
            self.ENV_PROJECT_MODE = WH_PROJECT_MODE.IDS_ASSET_MODE

            self.AssetWorkingDir = self.AssetWorkingDir % {
                'UserHome': self.UserHome,
                'Project':self.Project,
                'AssetPrefix':self.AssetPrefix,
                'TaskType':self.TaskType,
                'UserID':self.UserID
            }
            self.PreviewRenderDir = self.PreviewRenderDir % {
                'AssetWorkingDir':self.AssetWorkingDir
            }

            self.LogDir = self.LogDir % {
                'AssetWorkingDir':self.AssetWorkingDir
            }

            self.xsiAssetModelDir = self.xsiAssetModelDir % {
                'AssetWorkingDir':self.AssetWorkingDir
            }
            self.xsiAssetWorkingDir = self.xsiAssetWorkingDir % {
                'AssetWorkingDir':self.AssetWorkingDir
            }
            self.xsiModelServerDir = self.xsiModelServerDir % {
                'ProjectHome':self.ProjectHome,
                'Company':self.Company,
                'AssetPrefix':self.AssetPrefix
            }
            self.xsiModelMovieServerDir = self.xsiModelMovieServerDir % {
                'ProjectHome':self.ProjectHome,
                'Company':self.Company,
                'AssetPrefix':self.AssetPrefix
            }
        elif self.DirType =='shot':
            self.ENV_PROJECT_MODE = WH_PROJECT_MODE.IDS_SHOT_MODE

            self.ShotWorkingDir = self.ShotWorkingDir % {
                'UserHome': self.UserHome,
                'Project':self.Project,
                'SeqName':self.SeqName,
                'ShotName':self.ShotName,
                'TaskType':self.TaskType,
                'UserID':self.UserID
            }
            self.xsiShotWorkingDir = self.xsiShotWorkingDir % {
                'UserHome': self.UserHome,
                'Project':self.Project,
                'SeqName':self.SeqName,
                'ShotName':self.ShotName,
                'TaskType':self.TaskType,
                'UserID':self.UserID,
            }
            self.xsiShotMovieDir = self.xsiShotMovieDir % {
                'xsiShotWorkingDir': self.xsiShotWorkingDir
            }
            self.xsiShotServerDir = self.xsiShotServerDir % {
                'ProjectHome':self.ProjectHome,
                'Company':self.Company,
                'Project':self.Project,
                'SeqName':self.SeqName,
                'ShotName':self.ShotName,
            }
            self.xsiShotMovieServerDir = self.xsiShotMovieServerDir %{
                'ProjectHome':self.ProjectHome,
                'Company':self.Company,
                'Project':self.Project,
                'SeqName':self.SeqName,
                'ShotName':self.ShotName,
            }
            self.PreviewRenderDir = self.PreviewRenderDir % {
                'ShotWorkingDir':self.ShotWorkingDir
            }
        self.useCustomUrl(True)

    def useCustomUrl(self, rnt=True, custom_url = None):
        USE_URL_CUSTOM[0] = True
        if (custom_url):
            USE_URL_CUSTOM[1] = custom_url
        else:
            USE_URL_CUSTOM[1] = self.ServerName
        #print '##%s##' % USE_URL_CUSTOM[1]


class whProjectPathData(object):
    def __init__(self, dict_ = None):
        #print dict_
        self.TID = WH_CASE_IDS.WH_PRJ_PATH

        self.fixShotPubPath = None
        self.fixShotMovPath = None
        self.fixShotTextPath = None
        self.fixShotCachePath = None
        self.fixShotEtc1Path = None
        self.fixShotEtc2Path = None
        self.fixShotEtc3Path = None
        self.fixShotEtc4Path = None
        self.fixShotEtc5Path = None

        self.fixAssetPubPath = None
        self.fixAssetMovPath = None
        self.fixAssetTextPath = None
        self.fixAssetCachePath = None
        self.fixAssetEtc1Path = None
        self.fixAssetEtc2Path = None
        self.fixAssetEtc3Path = None
        self.fixAssetEtc4Path = None
        self.fixAssetEtc5Path = None

        self.setDict(dict_)

    def setDict(self, dict_):
        if dict_:

            if dict_.has_key('fixShotPubPath'):self.fixShotPubPath = dict_['fixShotPubPath']
            if dict_.has_key('fixShotMovPath'):self.fixShotMovPath = dict_['fixShotMovPath']
            if dict_.has_key('fixShotTextPath'):self.fixShotTextPath = dict_['fixShotTextPath']
            if dict_.has_key('fixShotCachePath'):self.fixShotCachePath = dict_['fixShotCachePath']
            if dict_.has_key('fixShotEtc1Path'):self.fixShotEtc1Path = dict_['fixShotEtc1Path']
            if dict_.has_key('fixShotEtc2Path'):self.fixShotEtc2Path = dict_['fixShotEtc2Path']
            if dict_.has_key('fixShotEtc3Path'):self.fixShotEtc3Path = dict_['fixShotEtc3Path']

            if dict_.has_key('fixShotEtc4Path'):self.fixShotEtc4Path = dict_['fixShotEtc4Path']
            if dict_.has_key('fixShotEtc5Path'):self.fixShotEtc5Path = dict_['fixShotEtc5Path']

            if dict_.has_key('fixAssetPubPath'):self.fixAssetPubPath = dict_['fixAssetPubPath']
            if dict_.has_key('fixAssetMovPath'):self.fixAssetMovPath = dict_['fixAssetMovPath']
            if dict_.has_key('fixAssetTextPath'):self.fixAssetTextPath = dict_['fixAssetTextPath']
            if dict_.has_key('fixAssetCachePath'):self.fixAssetCachePath = dict_['fixAssetCachePath']
            if dict_.has_key('fixAssetEtc1Path'):self.fixAssetEtc1Path = dict_['fixAssetEtc1Path']
            if dict_.has_key('fixAssetEtc2Path'):self.fixAssetEtc2Path = dict_['fixAssetEtc2Path']
            if dict_.has_key('fixAssetEtc3Path'):self.fixAssetEtc3Path = dict_['fixAssetEtc3Path']

            if dict_.has_key('fixAssetEtc4Path'):self.fixAssetEtc4Path = dict_['fixAssetEtc4Path']
            if dict_.has_key('fixAssetEtc5Path'):self.fixAssetEtc5Path = dict_['fixAssetEtc5Path']




    def replaceEnvFile(self, filename):
        replaceData = whEnvData(filename)
        path_map = WH_PATH_MAP()
        path_map.FILESERVERHOME = replaceData.ProjectHome
        path_map.COMPANY = replaceData.Company
        path_map.PROJECTID = replaceData.Project
        path_map.ASSETID = replaceData.AssetPrefix
        path_map.PUBLISHER = replaceData.UserID
        path_map.SEQUENCEID = replaceData.SeqName
        path_map.SHOTID = replaceData.ShotName
        path_map.TASKTYPEID = replaceData.TaskType

        replaceList = [x for x in self.__dict__.keys() if '__' not in x and 'TID' not in x]
        for r in replaceList:
             for v, w in  [x for x in path_map.__dict__.items() if '__' not in x[0] or 'TID' not in x[0]]:
                if str(w).endswith('/') == True:
                    w = w.rstrip('/')
                if str(w) != 'None':
                    code = compile('self.%s = self.%s.replace("[%s]", "%s")' % (r, r, v, w), '<string>', 'exec')
                exec code

    def replaceEnv(self, envData):
        replaceData = envData
        path_map = WH_PATH_MAP()
        path_map.FILESERVERHOME = replaceData.ProjectHome
        path_map.COMPANY = replaceData.Company
        path_map.PROJECTID = replaceData.Project
        path_map.ASSETID = replaceData.AssetPrefix
        path_map.PUBLISHER = replaceData.UserID
        path_map.SEQUENCEID = replaceData.SeqName
        path_map.SHOTID = replaceData.ShotName
        path_map.TASKTYPEID = replaceData.TaskType

        replaceList = [x for x in self.__dict__.keys() if '__' not in x and 'TID' not in x]
        for r in replaceList:
            for v, w in  [x for x in path_map.__dict__.items() if '__' not in x[0] or 'TID' not in x[0]]:
                if str(w).endswith('/') == True:
                    w = w.rstrip('/')
                try:
                    if str(w) != 'None':
                        code = compile('self.%s = self.%s.replace("[%s]", "%s")' % (r, r, v, w), '<string>', 'exec')
                    exec code
                except:
                    if str(w) != 'None':
                        code = compile('self.%s = self.%s' % (r, r),'<string>', 'exec')
                    exec code


    def customReplaceEnv(self, capital, path):
        replaceList = [x for x in self.__dict__.keys() if '__' not in x and 'TID' not in x]
        for x in replaceList:
            if str(path).endswith('/') == True:
                path = path.rstrip('/')
            try:
                code = compile('self.%s = self.%s.replace("[%s]", "%s")' % (x, x, capital, path), '<string>', 'exec')
                exec code
            except:
                code = compile('self.%s = self.%s' % (x, x),'<string>', 'exec')
                exec code



class whTaskData(object):
    code = -1
    name = None
    color = None
    def __init__(self, code, name, color):
        self.TID = WH_CASE_IDS.WH_TASK
        self.code = code
        self.name = name
        self.color = color


class whTaskListData(object):
    def __init__(self, list_ = None):
        #print dict_
        self.TID = WH_CASE_IDS.WH_TASK_LIST
        self._taskList = []
        self._taskCount = 0
        self.setDict(list_)
    def setDict(self, list_):
        if list_:
            self._taskList = []
            for task_ in list_:
                whtask = whTaskData(task_['code'], task_['name'], task_['color'])
                self._taskList.append(whtask)
            self._taskCount = len(self._taskList)

class whPShotData(object):
    def __init__(self, whprojectdata=None):
        self.TID = WH_CASE_IDS.WH_PUBLISH_SHOT
        self._corpPrefix = None
        self._projectId = None
        self._shotId = None
        self._assetList = None
        self._versionNumber = None
        self._publisherId = None
        self._taskTypeCd = None
        self._file = None
        self._movie = None
        self._cacheFile = None
        self._PdataType = None

        self._assetListVer = None
        self._preCompFile = None
        self._userExtraGeom = None
        self._originalSelectedFile = None
        self._originalSelectedMovie = None
        self._publishInfo = None
        self._publishComment = None
        self._publishIcon = None

        if whprojectdata:
            self._corpPrefix = whprojectdata.corpPrefix
            self._projectId = whprojectdata.projectId

    @property
    def shotId(self):
        return self._shotId

    @shotId.setter
    def shotId(self, value):
        self._shotId = value

    @property
    def assetList(self):
        return self._assetList

    @assetList.setter
    def assetList(self, value):
        self._assetList = value

    @property
    def assetLIstVer(self):
        return self._assetListVer

    @assetLIstVer.setter
    def assetListVer(self, value):
        self._assetListVer = value

    @property
    def cacheFile(self):
        return self._cacheFile

    @cacheFile.setter
    def cacheFile(self, value):
        self._cacheFile = value

    @property
    def preCompFile(self):
        return self._preCompFile

    @preCompFile.setter
    def preCompFile(self, value):
        self._preCompFile = value

    @property
    def userExtraGeom(self):
        return self._userExtraGeom

    @userExtraGeom.setter
    def userExtraGeom(self, value):
        self._userExtraGeom = value

    @property
    def corpPrefix(self):
        return  self._corpPrefix

    @corpPrefix.setter
    def corpPrefix(self, value):
        #if type(value) not in StringTypes:
        #    raise RuntimeError("Must input String value!")
        self._corpPrefix = value

    @property
    def projectId(self):
        return  self._projectId

    @projectId.setter
    def projectId(self, value):
        # if type(value) not in StringType:
        #   raise RuntimeError("Must input String value!")
        self._projectId = value

    @property
    def versionNumber(self):
        return self._versionNumber

    @versionNumber.setter
    def versionNumber(self, value):
        self._versionNumber = value

    @property
    def publisherId(self):
        return self._publisherId

    @publisherId.setter
    def publisherId(self, value):
        self._publisherId = value

    @property
    def taskTypeCd(self):
        return self._taskTypeCd

    @taskTypeCd.setter
    def taskTypeCd(self, value):
        self._taskTypeCd = value

    @property
    def originalSelectedFile(self):
        return self._originalSelectedFile

    @originalSelectedFile.setter
    def originalSelectedFile(self, value):
        self._originalSelectedFile = value

    @property
    def originalSelectedMovie(self):
        return self._originalSelectedMovie

    @originalSelectedMovie.setter
    def originalSelectedMovie(self, value):
        self._originalSelectedMovie = value

    @property
    def publishInfo(self):
        return self._publishInfo

    @publishInfo.setter
    def publishInfo(self, value):
        self._publishInfo = value

    @property
    def publishComment(self):
        return self._publishComment

    @publishComment.setter
    def publishComment(self, value):
        self._publishComment = urllib.quote(value)

    @property
    def PdataType(self):
        return self._PdataType

    @PdataType.setter
    def PdataType(self, value):
        self._PdataType = value

    @property
    def publishIcon(self):
        return self._publishIcon

    @publishIcon.setter
    def publishIcon(self, value):
        self._publishIcon = value


class whPAssetData(object):
    def __init__(self, whprojectdata=None):
        self.TID = WH_CASE_IDS.WH_PUBLISH_ASSET

        self._corpPrefix = None
        self._projectId = None
        self._assetId = None
        self._versionNumber = None
        self._publisherId = None
        self._taskTypeCd = None
        self._filePublish = None
        self._movie = None

        self._fileHiRes = None
        self._fileAnimRes = None
        self._fileLowRes = None
        self._tag = None
        self._originalSelectedFile = None
        self._originalSelectedMovie = None
        self._publishInfo = None
        self._publishComment = None
        self._PdataType = None
        self._publishIcon = None

        if whprojectdata:
            self._corpPrefix = whprojectdata.corpPrefix
            self._projectId = whprojectdata.projectId

    @property
    def corpPrefix(self):
        return  self._corpPrefix

    @corpPrefix.setter
    def corpPrefix(self, value):
        if type(value) not in StringTypes:
            raise RuntimeError("Must input String value!")
        self._corpPrefix = value

    @property
    def projectId(self):
        return  self._projectId

    @projectId.setter
    def projectId(self, value):
        #if type(value) not in StringType:
        #    raise RuntimeError("Must input String value!")
        self._projectId = value

    @property
    def assetId(self):
        return self._assetId

    @assetId.setter
    def assetId(self, value):
        #if type(value) not in StringType:
        #    raise RuntimeError("Must input String value!")
        self._assetId = value

    @property
    def versionNumber(self):
        return self._versionNumber

    @versionNumber.setter
    def versionNumber(self, value):
        self._versionNumber = value

    @property
    def publisherId(self):
        return self._publisherId

    @publisherId.setter
    def publisherId(self, value):
        self._publisherId = value

    @property
    def taskTypeCd(self):
        return self._taskTypeCd

    @taskTypeCd.setter
    def taskTypeCd(self, value):
        self._taskTypeCd = value

    @property
    def filePublish(self):
        return self._filePublish

    @filePublish.setter
    def filePublish(self, value):
        if not os.path.exists(value):
            raise RuntimeError("file %s not exist!" % value)
        self._filePublish = value

    @property
    def movie(self):
        return self._movie

    @movie.setter
    def movie(self, value):
        if not os.path.exists(value):
            raise RuntimeError("file %s not exist!" % value)
        self._movie = value

    @property
    def fileHiRes(self):
        return self._fileHiRes

    @fileHiRes.setter
    def fileHiRes(self, value):
        self._fileHiRes = value

    @property
    def fileAnimRes(self):
        return self._fileAnimRes

    @fileAnimRes.setter
    def fileAnimRes(self, value):
        self._fileAnimRes = value

    @property
    def fileLowRes(self):
        return self._fileLowRes

    @fileLowRes.setter
    def fileLowRes(self, value):
        self._fileLowRes = value

    @property
    def tag(self):
        return self._tag

    @tag.setter
    def tag(self, value):
        self._tag = value

    @property
    def originalSelectedFile(self):
        return self._originalSelectedFile

    @originalSelectedFile.setter
    def originalSelectedFile(self, value):
        self._originalSelectedFile = value

    @property
    def originalSelectedMovie(self):
        return self._originalSelectedMovie

    @originalSelectedMovie.setter
    def originalSelectedMovie(self, value):
        self._originalSelectedMovie = value

    @property
    def publishInfo(self):
        return self._publishInfo

    @publishInfo.setter
    def publishInfo(self, value):
        self._publishInfo = value

    @property
    def publishComment(self):
        return self._publishComment

    @publishComment.setter
    def publishComment(self, value):
        self._publishComment = urllib.quote(value)

    @property
    def PdataType(self):
        return self._PdataType

    @PdataType.setter
    def PdataType(self, value):
        self._PdataType = value

    @property
    def publishIcon(self):
        return self._publishIcon

    @publishIcon.setter
    def publishIcon(self, value):
        self._publishIcon = value