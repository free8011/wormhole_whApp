# coding: utf-8

from api.wormholeAPI.whDataModels import whProjectData
from api.wormholeAPI.whDataModels import whSequenceData
from api.wormholeAPI.whDataModels import whShotData
from api.wormholeAPI.whDataModels import whAssetData
from api.wormholeAPI.whDataModels import whShotHistData
from api.wormholeAPI.whDataModels import whAssetHistData
from api.wormholeAPI.whDataModels import whMemberData
from api.wormholeAPI.whDataModels import whProjectPathData
from api.wormholeAPI.whDataModels import whEnvData
from api.wormholeAPI.whDataModels import whTaskListData
from api.wormholeAPI.whDataModels import whPAssetData
from api.wormholeAPI.whDataModels import whPShotData
from api.wormholeAPI.whDataModels import whAssetRData

from api.wormholeAPI.urlModels import PROJECT_LIST_QUERY
from api.wormholeAPI.urlModels import SEQ_LIST_QUERY
from api.wormholeAPI.urlModels import SHOT_NAME_LIST_QUERY
from api.wormholeAPI.urlModels import ASSET_ID_LIST_QUERY
from api.wormholeAPI.urlModels import SHOT_LIST_QUERY
from api.wormholeAPI.urlModels import ASSET_LIST_QUERY
from api.wormholeAPI.urlModels import PROJECT_USER_LIST_QUERY
from api.wormholeAPI.urlModels import USER_INFO_QUERY
from api.wormholeAPI.urlModels import GET_INFO_QUERY
from api.wormholeAPI.urlModels import SHOT_VERSION_LIST_QUERY
from api.wormholeAPI.urlModels import CallUrl
from api.wormholeAPI.urlModels import PROJECT_FILE_PATH_LIST_QUERY
from api.wormholeAPI.urlModels import GET_TASK_TYPE_LIST_QUERY
from api.wormholeAPI.urlModels import PUBLISH_ASSET_QUERY
from api.wormholeAPI.urlModels import PUBLISH_SHOT_QUERY
from api.wormholeAPI.urlModels import RECORD_IMPORT_ASSET_QUERY
from api.wormholeAPI.urlModels import FileUpload
from api.resourceIDs import WH_PRJ

##FLLLOW CLASS
'''
    whProjectLIst.project_list[0].asset_list[0].version_list[0]
                                 .seq_list[0].shot_list[0].version_list[0]

                                 .get_shot(<name string>)
                                 .get_asset(<name string>)
                 
                 .get_project(<name_string>)

'''

# API MOTHER CLASS
class whBase(object):
    def __init__(self):
        self._query = None
        self._result = None
        self.quety_call = None
        self.corpPrefix = None

    @property
    def query(self):
        return self._query
    
    @property
    def result(self):
        return self._result


class whAssetHist(whAssetHistData, whBase):
    def __init__(self, corpPrefix, projectId, dist_=None):
        self.corpPrefix = corpPrefix
        self.projectId = projectId
        whAssetHistData.__init__(self, dist_)



class whAsset(whAssetData, whBase):
    def __init__(self, corpPrefix, projectId, dict_ = None ):
        self.corpPrefix = corpPrefix
        self.projectId = projectId
        whAssetData.__init__(self, dict_)

        self._asset_hist = []

    def __getAssetHist(self):
        ahquery = ASSET_LIST_QUERY()
        ahquery.setMustQuery(self.corpPrefix, self.projectId, self.assetId)
        self._query = ahquery.getQuery()

        self.quety_call = CallUrl()
        self.quety_call.setURL(self._query)

        if self.quety_call.getIsSuccess():
            self._result = self.quety_call.getRes_dict()
            if self._result['AssetList'][0]['publishHistory']:
                for assetHist_ in self._result['AssetList'][0]['publishHistory']:
                    whassethist = whAssetHist(self.corpPrefix, self.projectId, assetHist_)
                    self._asset_hist.append(whassethist)

    @property
    def hist_count(self):
        if not self._asset_hist:
            self.__getAssetHist()
        return len(self._asset_hist)

    @property
    def hist_list(self):
        if not self._asset_hist:
            self.__getAssetHist()
        return  self._asset_hist


class whShotHist(whShotHistData, whBase):
    def __init__(self, corpPrefix, projectId, dict_ = None):
        self.corpPrefix = corpPrefix
        self.projectId = projectId
        whShotHistData.__init__(self, dict_)
        self._shot_hist = []


class whUser(whMemberData, whBase):
    def __init__(self, corpPrefix, projectId, dict_ = None):
        self.corpPrefix = corpPrefix
        self.projectId = projectId
        whMemberData.__init__(self, dict_)


    def __getUserInfo(self):
        hlquery = USER_INFO_QUERY()
        hlquery.setMustQuery(self.corpPrefix, self.shotId)
        self._query = hlquery.getQuery()

        self.quety_call = CallUrl()
        self.quety_call.setURL(self._query)

        if self.quety_call.getIsSuccess():
            self._result = self.quety_call.getRes_dict()

    @property
    def taskType(self):
        if not self._taskType:
            self.__getUserInfo()
        return self._taskType

    @property
    def userType(self):
        if not self._userType:
            self.__getUserInfo()
        return self._userType

    @property
    def userSkills(self):
        if not self._userSkills:
            self.__getUserInfo()
        return self._userSkills

    @property
    def userTeam(self):
        if not self._userTeam:
            self.__getUserInfo()
        return self._userTeam

    @property
    def userPhoto(self):
        if not self._userPhoto:
            self.__getUserInfo()
        return self._userPhoto

    @property
    def userEmail(self):
        if not self._userEmail:
            self.__getUserInfo()
        return  self._userEmail

    @property
    def userOfficeTelNm(self):
        if not self._userOfficeTelNm:
            self.__getUserInfo()
        return  self._userOfficeTelNm

    @property
    def userMobileNm(self):
        if not self._userMobileNm:
            self.__getUserInfo()
        return  self._userMobileNm

    @property
    def userSkypeId(self):
        if not self._userSkypeId:
            self.__getUserInfo()
        return  self._userSkypeId

    @property
    def userHistory(self):
        if not self._userHistory:
            self.__getUserInfo()
        return  self._userHistory
    '''
    @property
    def userId(self):
        if not self.userId:
            self.__getUserInfo()
        return self.userId
    '''


class whShot(whShotData, whBase):
    def __init__(self, corpPrefix, projectId, dict_ = None ):
        self.corpPrefix = corpPrefix
        self.projectId = projectId
        whShotData.__init__(self, dict_)

        self._shot_hist = []

    def __getShotHist(self):
        hlquery = SHOT_LIST_QUERY()
        hlquery.setMustQuery(self.corpPrefix, self.projectId, self.shotId)
        self._query = hlquery.getQuery()

        self.quety_call = CallUrl()
        self.quety_call.setURL(self._query)

        if self.quety_call.getIsSuccess():
            self._result = self.quety_call.getRes_dict()
            if self._result['publishHistory']:
                for shotHist_ in self._result['publishHistory']:
                    whshothist = whShotHist(self.corpPrefix, self.projectId, shotHist_)
                    self._shot_hist.append(whshothist)

    @property
    def hist_count(self):
        if not self._shot_hist:
            self.__getShotHist()
        return len(self._shot_hist)

    @property
    def hist_list(self):
        if not self._shot_hist:
            self.__getShotHist()
        return  self._shot_hist


class whProjectPath(whProjectPathData, whBase):
    def __init__(self, corpPrefix, projectId, dict_ = None):
        self.corpPrefix = corpPrefix
        self.projectId = projectId
        whProjectPathData.__init__(self, dict_)


class whSequence(whSequenceData, whBase):
    def __init__(self, corpPrefix, projectId, dict_ = None):
        self.corpPrefix = corpPrefix
        self.projectId = projectId
        whSequenceData.__init__(self, dict_)

        self._shot_list = []
        self._shot_id = {}

    def __getShotList(self):
        slquery = SHOT_NAME_LIST_QUERY()
        slquery.setMustQuery(self.corpPrefix, self.projectId, self.sequenceId)
        self._query = slquery.getQuery()

        self.quety_call  = CallUrl()
        self.quety_call.setURL(self._query)

        if self.quety_call.getIsSuccess():
            self._result = self.quety_call.getRes_dict()
            if self._result['shotList']:
                self._shot_list = []
                for shot_ in self._result['shotList']:
                    whshot = whShot(self.corpPrefix, self.projectId,  shot_)
                    self._shot_list.append(whshot)
                    self._shot_id[whshot.shotId] = whshot

    def getShot(self, ID):
        slquery = SHOT_VERSION_LIST_QUERY()
        slquery.setMustQuery(self.corpPrefix, self.projectId, ID)
        self._query = slquery.getQuery()

        self.quety_call  = CallUrl()
        self.quety_call.setURL(self._query)

        if self.quety_call.getIsSuccess():
            self._result = self.quety_call.getRes_dict()
            #if self._result['shotList']:
            self._shot_list = []
            self._result['shotId'] = ID
            whshot = whShot(self.corpPrefix, self.projectId, self._result)
            self._shot_list.append(whshot)
            self._shot_id[whshot.shotId] = whshot
            return whshot

    def loadShots(self):
        self.__getShotList()
        return [(x[0], x[1].shotId) for x in enumerate(self._shot_list)]

    @property
    def shot_count(self):
        if not self._shot_list:
            self.__getShotList()
        return len(self._shot_list)

    @property
    def shot_list(self):
        if not self._shot_list:
            self.__getShotList()
        return self._shot_list

    @property
    def shot_id(self):
        if not self._shot_id:
            self.__getShotList()
        return self._shot_id


class whProject(whProjectData, whBase):
    def __init__(self, corpPrefix, dict_ = None):
        whBase.__init__(self)

        self.corpPrefix = corpPrefix

        self._seq_list = []
        self._seq_id = {}
        self._asset_list = []
        self._asset_id = {}
        self._user_list = []
        self._user_id = {}
        ## 2015-05-25 addtion project path
        self._paths = []

        self._env = None

        if dict_:
            whProjectData.__init__(self, dict_)
        else:
            whProjectData.__init__(self)


    def getAsset(self, ID = None):
        if not ID:
            return None

        aquery = ASSET_LIST_QUERY()
        aquery.setMustQuery(self.corpPrefix, self.projectId, ID)
        self._query = aquery.getQuery()
        self.quety_call = CallUrl()
        self.quety_call.setURL(self._query)

        if self.quety_call.getIsSuccess():
            self._result = self.quety_call.getRes_dict()
            if self._result['AssetList']:
                self._asset_list = []

                asset_ = self._result['AssetList'][0]
                whasset = whAsset(self.corpPrefix, self.projectId, asset_)

                self._asset_list.append(whasset)
                self._asset_id['whasset.assetId'] = whasset
                #code = compile('self.asset_%s = whasset' % whasset.assetId.replace(' ', '_') , '<string>', 'exec')
                #exec code

                return whasset
        return None


    def getSequence(self, ID=None):
        if not ID:
            return None
        plquery = SEQ_LIST_QUERY()
        plquery.setMustQuery(self.corpPrefix, self.projectId)
        self._query = plquery.getQuery()
        self.quety_call  = CallUrl()
        self.quety_call.setURL(self._query)

        if self.quety_call.getIsSuccess():
            self._result = self.quety_call.getRes_dict()
            if self._result['sequenceList']:
                self._seq_list = []
                for seq_ in self._result['sequenceList']:
                    #print seq_
                    if seq_['sequenceId'] == ID:
                        whsequence = whSequence(self.corpPrefix, self.projectId, seq_)
                        self._seq_list.append(whsequence)
                        self._seq_id[whsequence.sequenceId] = whsequence
                        return whsequence


    def __getAssetListPrjID(self):

        alquery = ASSET_ID_LIST_QUERY()
        alquery.setMustQuery(self.corpPrefix, self.projectId, 'ALL')
        self._query = alquery.getQuery()
        self.quety_call = CallUrl()
        self.quety_call.setURL(self._query)

        if self.quety_call.getIsSuccess():
            self._result = self.quety_call.getRes_dict()
            if self._result['assetList']:
                self._asset_list = []
                for asset_ in self._result['assetList']:
                    whasset = whAsset(self.corpPrefix, self.projectId, asset_)
                    self._asset_list.append(whasset)
                    self._asset_id[whasset.assetId] = whasset
                    #code = compile('self.asset_%s = whasset' % whasset.assetId.replace(' ', '_') , '<string>', 'exec')
                    #exec code



    def __getSeqListPrjID(self):
        plquery = SEQ_LIST_QUERY()
        plquery.setMustQuery(self.corpPrefix, self.projectId)
        self._query = plquery.getQuery()
        self.quety_call  = CallUrl()
        self.quety_call.setURL(self._query)

        if self.quety_call.getIsSuccess():
            self._result = self.quety_call.getRes_dict()
            if self._result['sequenceList']:
                self._seq_list = []
                for seq_ in self._result['sequenceList']:
                    #print seq_
                    whsequence = whSequence(self.corpPrefix, self.projectId, seq_)
                    self._seq_list.append(whsequence)
                    self._seq_id[whsequence.sequenceId] = whsequence

    def __getUserListPrjID(self):
        plquery = PROJECT_USER_LIST_QUERY()
        plquery.setMustQuery(self.corpPrefix, self.projectId)
        self._query = plquery.getQuery()
        self.quety_call  = CallUrl()
        self.quety_call.setURL(self._query)

        if self.quety_call.getIsSuccess():
            self._result = self.quety_call.getRes_dict()
            if self._result['UserList']:
                for user_ in self._result['UserList']:
                    #print seq_
                    whuser = whUser(self.corpPrefix, self.projectId, user_)
                    self._user_list.append(whuser)

                    self._user_id[whuser.userId] = whuser



    def __getProjectPathID(self):
        plquery = PROJECT_FILE_PATH_LIST_QUERY()
        plquery.setMustQuery(self.corpPrefix, self.projectId)
        self._query = plquery.getQuery()
        self.quety_call = CallUrl()
        self.quety_call.setURL(self._query)

        if self.quety_call.getIsSuccess():
            self._result = self.quety_call.getRes_dict()
            if self._result['fixedPath']:
                #for path_ in self._result['fixedPath']:
                whpath = whProjectPathData(self._result['fixedPath'])
                if self._env:
                    whpath.replaceEnv(self._env)
                self._paths = whpath

    def assetPublish(self, whpasset, iconFile=None):
        if not self.env:
            return

        whpasset.corpPrefix = self.env.Company
        whpasset.projectId = self.env.Project
        whpasset.assetId = self.env.AssetPrefix
        whpasset.taskTypeCd = self.env.TaskTypeCode
        whpasset.publisherId = self.env.UserID

        outurl = None
        plquery = PUBLISH_ASSET_QUERY()
        if iconFile:
            file_ = FileUpload(self.corpPrefix)
            outurl, msg = file_.Upload(iconFile)
            whPAssetData.publishIcon = outurl


        plquery.setMustQuery(whpasset.corpPrefix, whpasset.projectId, whpasset.assetId, whpasset.versionNumber,
                             whpasset.publisherId, whpasset.taskTypeCd, whpasset.filePublish, whpasset.movie)
        plquery.setOptionQuery(whpasset.fileHiRes, whpasset.fileAnimRes, whpasset.fileLowRes, whpasset.tag,
                               whpasset.originalSelectedFile, whpasset.originalSelectedMovie, whpasset.publishInfo,
                               whpasset.publishComment, whpasset.PdataType, whpasset.publishIcon)

        self._query = plquery.getQuery()
        self.quety_call  = CallUrl()
        self.quety_call.setURL(self._query)

        if self.quety_call.getIsSuccess():
            self._result = self.quety_call.getRes_dict()
    '''
    def recordImportAsset(self, whAssetRData):
        plquery = RECORD_IMPORT_ASSET_QUERY()

        whAssetRData.corpPrefix = self.env.Company
        whAssetRData.projectId = self.env.Project
        whAssetRData.userId = self.env.UserID
        whAssetRData.taskTypeCd = self.env.TaskTypeCode
        whAssetRData.assetId = self.env.AssetName
        #whAssetRData.assetVersion =
        whAssetRData.workType = 'a'
        whAssetRData.assetNm = self.env.AssetName
        whAssetRData.workingAssetDir = self.env.AssetWorkingDir

        plquery.setMustQuery(whAssetRData.corpPrefix, whAssetRData.projectId, whAssetRData.userId, whAssetRData.taskTypeCd,
                             whAssetRData.assetId, whAssetRData.assetVersion)

        plquery.setOptionQuery(whAssetRData.workType, whAssetRData.shotNm, whAssetRData.assetNm, whAssetRData.workingAssetDir, whAssetRData.workingShotDir)
        self._query = plquery.getQuery()
        self.quety_call  = CallUrl()
        self.quety_call.setURL(self._query)

        if self.quety_call.getIsSuccess():
            self._result = self.quety_call.getRes_dict()

    '''
    def shotPublish(self, whPShotData, iconFile=None):

        if not self.env:
            return

        whPShotData.corpPrefix = self.env.Company
        whPShotData.projectId = self.env.Project
        whPShotData.shotId = self.env.ShotName
        whPShotData.taskTypeCd = self.env.TaskTypeCode
        whPShotData.publisherId = self.env.UserID

        outurl = None
        plquery = PUBLISH_SHOT_QUERY()
        if iconFile:
            file_ = FileUpload(self.corpPrefix)
            outurl, msg = file_.Upload(iconFile)
            whPShotData.publishIcon = outurl
        plquery.setMustQuery(whPShotData.corpPrefix, whPShotData.projectId, whPShotData.shotId, whPShotData.assetList, whPShotData.versionNumber,
                         whPShotData.publisherId, whPShotData.taskTypeCd, whPShotData.file, whPShotData.movie)

        plquery.setOptionQuery(whPShotData.originalSelectedFile, whPShotData.originalSelectedMovie,
                        whPShotData.preCompFile, whPShotData.userExtraGeom, whPShotData.publishInfo, whPShotData.publishComment, whPShotData.PdataType, whPShotData.publishIcon,
                               whPShotData.cacheFile)

        self._query = plquery.getQuery()
        self.quety_call  = CallUrl()
        self.quety_call.setURL(self._query)

        if self.quety_call.getIsSuccess():
            self._result = self.quety_call.getRes_dict()


    def loadAssets(self):
        #if not self._asset_list:
        self.__getAssetListPrjID()
        return [(x[0], x[1].assetId) for x in enumerate(self._asset_list)]

    def loadSeqs(self):
        self.__getSeqListPrjID()
        return [(x[0], x[1].sequenceId) for x in enumerate(self._seq_list)]

    def loadUsers(self):
        self.__getUserListPrjID()
        return [(x[0], x[1].userId) for x in enumerate(self._user_list)]

    @property
    def seq_list(self):
        if not self._seq_list:
            self.__getSeqListPrjID()
        return self._seq_list

    @property
    def seq_id(self):
        if not self._seq_id:
            self.__getSeqListPrjID()
        return self._seq_id

    @property
    def seq_count(self):
        if not self._seq_list:
            self.__getSeqListPrjID()
        return len(self._seq_list)

    @property
    def asset_count(self):
        if not self._asset_list:
            self.__getAssetListPrjID()
        return len(self._asset_list)

    @property
    def asset_list(self):
        if not self._asset_list:
            self.__getAssetListPrjID()
        return self._asset_list

    @property
    def asset_id(self):
        if not self._asset_id:
            self.__getAssetListPrjID()
        return self._asset_id

    @property
    def user_list(self):
        if not self._user_list:
            self.__getUserListPrjID()
        return self._user_list

    @property
    def user_id(self):
        if not self._user_id:
            self.__getUserListPrjID()
        return self._user_id

    @property
    def user_count(self):
        if not self._user_list:
            self.__getUserListPrjID()
        return len(self._user_list)

    @property
    def paths(self):
        if not self._paths:
            self.__getProjectPathID()
        return self._paths

    @property
    def env(self):
        return self._env

    @env.setter
    def env(self, value):
        self._env = value


class whCompany(whBase):

    def __init__(self, corpPrefix = None):
        whBase.__init__(self)

        self._project_list = []
        self._project_id = {}
        self._member_list = []
        self._query = None

        self._env = None

        if corpPrefix:
            self.setProjectListId(corpPrefix)

    def setCompanyId(self, corpPrefix):
        if corpPrefix:
            self.corpPrefix = corpPrefix
        else:
            raise RuntimeError("Must Set corpPrefix value!")

    def __getProjectListPrjID(self):
        plquery = PROJECT_LIST_QUERY()
        plquery.setCorpPrefix(self.corpPrefix)
        self._query = plquery.getQuery()

        self.quety_call = CallUrl()
        self.quety_call.setURL(self._query)

        if self.quety_call.getIsSuccess():
            self._result = self.quety_call.getRes_dict()
            if self._result['projectList']:
                self._project_list = []
                for i, project_ in enumerate(self._result['projectList']):
                    whproject = whProject(self.corpPrefix, project_)
                    if self._env:
                        whproject.env = self._env
                    #print project_
                    self._project_list.append(whproject)

                    ##dict type
                    self._project_id[whproject.projectId] = whproject

                    ##IDS SET
                    #code = compile('self.project_%s = whproject' % whproject.projectId, '<string>', 'exec')
                    #exec code

    def __getMemberListPrjID(self):
        pass
        #mlquery

    def loadProjects(self):
        #if not self._project_list:
        self.__getProjectListPrjID()
        return [(x[0], x[1].projectId) for x in enumerate(self._project_list)]

    def getProject(self, ID):
        if not self._project_list:
            self.__getProjectListPrjID()
        if self._project_id:
            if self._project_id.has_key(ID):
                return self._project_id[ID]
        return None




    @property
    def project_count(self):
        if not self._project_list:
            self.__getProjectListPrjID()
        return len(self._project_list)

    @property
    def project_list(self):
        if not self._project_list:
            self.__getProjectListPrjID()
        return self._project_list


    @property
    def project_id(self):
        if not self._project_id:
            self.__getProjectListPrjID()
        return self._project_id

    @property
    def env(self):
        return self._env

    def setEnvFile(self, filepath):
        self._env = whEnvData(filepath)

        if self._env and self._env.Company:
            self.setCompanyId(self._env.Company)
            #self.__getProjectListPrjID()



class whTaskList(whTaskListData, whBase):
    def __init__(self, corpPrefix = None):
        whBase.__init__(self)
        self.corpPrefix = corpPrefix
        self._env = None
        whTaskListData.__init__(self)


    def __getTaskListURL(self):
        plquery = GET_TASK_TYPE_LIST_QUERY()
        plquery.setCorpPrefix(self.corpPrefix)
        self._query = plquery.getQuery()

        self.quety_call = CallUrl()
        self.quety_call.setURL(self._query)

        if self.quety_call.getIsSuccess():
            self._result = self.quety_call.getRes_dict()
            if self._result['taskTypeList']:
                self.setDict(self._result['taskTypeList'])

    @property
    def taskList(self):
        if not self._taskList:
            self.__getTaskListURL()
        return self._taskList

    def taskCount(self):
        if not self._taskCount:
            self.__getTaskListURL()
        return self._taskCount

    def setEnvFile(self, filepath):
        self._env = whEnvData(filepath)
        if self._env and self._env.Company:
            self.corpPrefix = self._env.Company




