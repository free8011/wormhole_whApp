# coding: utf-8

import urllib, urllib2
import json
import httplib, mimetypes, mimetools, cookielib
import os

from api.resourceIDs import WH_CASE_IDS


#WH_COMPANY = 'demo'
URL_ROOT = '.wormholepipeline.co.kr/interface/'
# [ isUse Custom URL, CUSTOM URL ]
USE_URL_CUSTOM = [False, '']

class DEFAULT_QUERY:
    def __init__(self):
        self.COMPANY_NAME = 'corpPrefix'
        self.PROJECT_ID = 'projectId'
        self.SHOT_ID = 'shotId'
        self.USER_ID = 'userId'
        self.SEQ_ID = 'seqId'
        self.WORKING_SHOT_DIR = 'workingShotDir'
        self.TASK_TYPE = 'taskTypeCd'

        self.ASSET_ID = 'assetId'
        self.TAG = 'tag'
        self.FILE_TYPE = 'fileType'
        self.WORKING_ASSET_DIR = 'workingAssetDir'

        self.GET_TYPE = 'getType'
        self.VERSION_NUMBER = 'versionNumber'
        self.PUBLISHER_ID = 'publisherId'
        self.FILE_PUBLISH = 'filePublish'
        self.FILE_HI_RES = 'fileHiRes'
        self.FILE_ANIM_RES = 'fileAnimRes'
        self.FILE_LOW_RES = 'fileLowRes'
        self.MOVIE = 'movie'
        self.FILE = 'file'
        self.TAG = 'tag'
        self.ORIGINAL_SELECTED_FILE = 'originalSelectedFile'
        self.ORIGINAL_SELECTED_MOVIE = 'originalSelectedMovie'
        self.PUBLISH_INFO = 'publishInfo'
        self.PUBLISH_COMMENT = 'publishComment'
        self.PDATA_TYPE = 'PdataType'
        self.PUBLISH_ICON = 'publishIcon'
        self.ASSET_LIST = 'assetList'
        self.ASSET_LIST_VER = 'assetLIstVer'
        self.CACHE_FILE = 'cacheFile'
        self.PRE_COMP_FILE = 'preCompFile'
        self.USER_EXTRA_GEOM = 'userExtraGeom'

        self.ASSET_VERSION = 'assetVersion'
        self.WORK_TYPE = 'workType'
        self.SHOT_NM = 'shotNm'
        self.ASSET_NM = 'assetNm'

        self.must_query = ['COMPANY_NAME']
        self.option_query = []
        
        self.call_query = ''

        self.rnt_query = ''
        self.corpPrefix_value = ''


        self.projectId_value = ''
        self.shotId_value = ''
        self.userId_value = ''
        self.workingShotDir_value = ''
        self.taskTypeCd_value = ''

        self.assetId_value = ''
        self.tag_value = ''
        self.fileType_value = ''
        self.workingAssetDir_value = ''
        self.seqId_value = ''
        self.assetId_value = ''
        self.getType_value = ''

        self.versionNumber_value = ''
        self.publisherId_value = ''
        self.filePublish_value = ''
        self.fileHiRes_value = ''
        self.fileLowRes_value = ''
        self.fileAnimRes_value = ''
        self.movie_value = ''
        self.file_value = ''
        self.tag_value = ''
        self.originalSelectedFile_value = ''
        self.originalSelectedMovie_value = ''
        self.publishInfo_value = ''
        self.publishComment_value = ''
        self.PdataType_value = ''
        self.publishIcon_value = ''

        self.assetList_value = ''
        self.assetListVer_value = ''
        self.cacheFile_value = ''
        self.preCompFile_value = ''
        self.userExtraGeom_value = ''

        self.assetVersion_value = ''
        self.workType_value = ''
        self.shotNm_value = ''
        self.assetNm_value = ''

    def __runMustQuery(self):
        if USE_URL_CUSTOM[0]:
            self.rnt_query = 'http://%s/interface/%s?' % (
                                            USE_URL_CUSTOM[1],
                                            self.call_query
                                            )
        else:
            self.rnt_query = 'http://%s%s%s?' % (
                                            self.corpPrefix_value,
                                            URL_ROOT,
                                            self.call_query
                                            )


        for q in self.must_query:
            query = self.__dict__[q]
            query_value = self.__dict__[self.__dict__[q] + '_value']
            
            if self.must_query.index(q) > 0:
                self.rnt_query += '&'

            self.rnt_query += '%s=%s' % (query, query_value)

    def __runOptionQuery(self):
        if self.option_query:
            for q in self.option_query:
                query = self.__dict__[q]
                query_value = self.__dict__[self.__dict__[q] + '_value']
                if query_value:
                    self.rnt_query += '&%s=%s' % (query, query_value)

    def setProjectId(self, value):
        self.projectId_value = value

    def setCorpPrefix(self, value):
        self.corpPrefix_value = value

    def getQuery(self):
        self.__runMustQuery()
        self.__runOptionQuery()

        return self.rnt_query


class PROJECT_LIST_QUERY(DEFAULT_QUERY):

    def __init__(self):
        DEFAULT_QUERY.__init__(self)

        self.call_query = 'listOfProjects.php'

    '''
    def getQuery(self):
        rnt_query = 'http://%s%s?%s=%s' % (URL_ROOT, 
                                           self.call_query, 
                                           self.COMPANY_NAME, 
                                           self.corpPrefix_value)
        return rnt_query
        '''


# SAMPLE RESULTS
# http://demo.wormholepipeline.com/interface/listOfProjects.php?corpPrefix=demo&
'''
{"isSuccess":"1","message":"","projectList":
    [
        {"projectId":"arrow","fileServePath":"Q:\\Core_wormhole_test\\demo\\arrow","versionInfo":null},
        {"projectId":"Wuhan_test","fileServePath":"Q:\\Core_wormhole_test\\demo\\Wuhan_test","versionInfo":null},
        {"projectId":"HWL","fileServePath":"Q:\\Core_wormhole_test\\demo\\HWL","versionInfo":"3"},
        {"projectId":"MtTam","fileServePath":"Q:\\Core_wormhole_test\\demo\\MtTam","versionInfo":"3"}
    ]
}

'''

class PROJECT_USER_LIST_QUERY(DEFAULT_QUERY):

    def __init__(self):
        DEFAULT_QUERY.__init__(self)
        self.call_query = 'getProjectUser.php'
        self.must_query = ['COMPANY_NAME', 'PROJECT_ID']
        self.option_query = []

    def setMustQuery(self, corpPrefix, project_id):
        self.corpPrefix_value = corpPrefix
        self.projectId_value = project_id

class USER_INFO_QUERY(DEFAULT_QUERY):

    def __init__(self):
        DEFAULT_QUERY.__init__(self)
        self.call_query = 'getUserInfo.php'
        self.must_query = ['COMPANY_NAME', 'USER_ID']
        self.option_query = []

    def setMustQuery(self, corpPrefix, user_id):
        self.corpPrefix_value = corpPrefix
        self.userId_value = user_id

class SEQ_LIST_QUERY(DEFAULT_QUERY):
    def __init__(self):
        DEFAULT_QUERY.__init__(self)
        self.call_query = 'getSeqnameList.php'
        self.must_query = ['COMPANY_NAME', 'PROJECT_ID']
        self.option_query = []

    def setMustQuery(self, corpPrefix, project_id):
        self.corpPrefix_value = corpPrefix
        self.projectId_value = project_id

class SHOT_VERSION_LIST_QUERY(DEFAULT_QUERY):

    def __init__(self):
        DEFAULT_QUERY.__init__(self)

        self.call_query = 'getShotList.php'
        self.must_query = ['COMPANY_NAME', 'PROJECT_ID', 'SHOT_ID']
        self.option_query = ['WORKING_SHOT_DIR', 'TASK_TYPE']

    def setMustQuery(self, corpPrefix, project_id, shotId):
        self.corpPrefix_value = corpPrefix
        self.projectId_value = project_id
        self.shotId_value = shotId

class SHOT_NAME_LIST_QUERY(DEFAULT_QUERY):

    def __init__(self):
        DEFAULT_QUERY.__init__(self)

        self.call_query = 'getShotnameList.php'
        self.must_query = ['COMPANY_NAME', 'PROJECT_ID', 'SEQ_ID']

    def setMustQuery(self, corpPrefix, project_id, seqId):
        self.corpPrefix_value = corpPrefix
        self.projectId_value = project_id
        self.seqId_value = seqId

class ASSET_ID_LIST_QUERY(DEFAULT_QUERY):
    def __init__(self):
        DEFAULT_QUERY.__init__(self)

        self.call_query = 'getAssetIDList.php'
        self.must_query = ['COMPANY_NAME', 'PROJECT_ID', 'ASSET_ID']

        self.option_query = ['FILE_TYPE']

    def setMustQuery(self, corpPrefix, project_id, asset_id):
        self.corpPrefix_value = corpPrefix
        self.projectId_value = project_id
        self.assetId_value = asset_id


class SHOT_LIST_QUERY(DEFAULT_QUERY):
    '''
    GET SHOT LIST is not pallowed.... with GET ASEET LIST
    '''

    def __init__(self):
        DEFAULT_QUERY.__init__(self)

        self.call_query = 'getShotList.php'

        self.must_query = ['COMPANY_NAME', 'PROJECT_ID', 'SHOT_ID']
        #self.option_query = ['WORKING_SHOT_DIR', 'TASK_TYPE']

    def setMustQuery(self, corpPrefix, project_id, shot_id):
        self.corpPrefix_value = corpPrefix
        self.projectId_value = project_id
        self.shotId_value = shot_id

    #def setShotId(self, value):
    #    self.shotId_value = value

class ASSET_LIST_QUERY(DEFAULT_QUERY):

    def __init__(self):
        DEFAULT_QUERY.__init__(self)

        self.call_query = 'getAssetList.php'
        self.must_query = ['COMPANY_NAME', 'PROJECT_ID']
        self.option_query = ['ASSET_ID', 'TAG', 'FILE_TYPE', 
                             'USER_ID', 'WORKING_ASSET_DIR', 'WORKING_SHOT_DIR']

    def setMustQuery(self, corpPrefix, project_id, asset_id):
        self.corpPrefix_value = corpPrefix
        self.projectId_value = project_id
        self.assetId_value = asset_id

    def setOptionQuery(self, asset_id, tag, file_type, user_id, working_asset_dir, working_shot_dir):

        if asset_id:
            self.assetId_value = asset_id
        if tag:
            self.tag_value = tag
        if file_type:
            self.fileType_value = file_type
        if user_id:
            self.userId_value = user_id
        if working_asset_dir:
            self.workingAssetDir_value = working_asset_dir
        if working_shot_dir:
            self.workingShotDir_value = working_shot_dir

class GET_INFO_QUERY(DEFAULT_QUERY):

    def __init__(self):
        DEFAULT_QUERY.__init__(self)
        self.call_query = 'getInfo.php'
        self.must_query = ['COMPANY_NAME', 'PROJECT_ID', 'GET_TYPE']
        self.option_query = ['SEQ_ID', 'ASSET_ID', 'SHOT_ID']

    def setMustQuery(self, corpPrefix, project_id, get_type):
        self.corpPrefix_value = corpPrefix
        self.projectId_value = project_id
        self.getType_value = get_type

    def setOptionQuery(self, seqId, assetId, shotId):
        if seqId:
            self.seqId_value = seqId
        if assetId:
            self.assetId_value = assetId
        if shotId:
            self.shotId_value = shotId



class TASK_TYPE_LIST_QUERY(DEFAULT_QUERY):

    def __init__(self):
        DEFAULT_QUERY.__init__(self)
        self.call_query = 'getTaskTypeList.php'
        self.must_query = ['COMPANY_NAME']

    def setMustQuery(self, corpPrefix):
        self.corpPrefix_value = corpPrefix


class PROJECT_FILE_PATH_LIST_QUERY(DEFAULT_QUERY):

    def __init__(self):
        DEFAULT_QUERY.__init__(self)
        self.call_query = 'getProjectFilePaths.php'
        self.must_query = ['COMPANY_NAME', 'PROJECT_ID']

    def setMustQuery(self, corpPrefix, project_id):
        self.corpPrefix_value = corpPrefix
        self.projectId_value = project_id

class GET_TASK_TYPE_LIST_QUERY(DEFAULT_QUERY):
    def __init__(self):
        DEFAULT_QUERY.__init__(self)
        self.call_query = 'getTaskTypeList.php'
        self.must_query = ['COMPANY_NAME']

    def setMustQuery(self, corpPrefix):
        self.corpPrefix_value = corpPrefix

class PUBLISH_ASSET_QUERY(DEFAULT_QUERY):
    def __init__(self):
        DEFAULT_QUERY.__init__(self)
        self.call_query = 'publishAsset.php'
        self.must_query = ['COMPANY_NAME', 'PROJECT_ID', 'ASSET_ID',
                           'VERSION_NUMBER', 'PUBLISHER_ID', 'TASK_TYPE',
                           'FILE_PUBLISH', 'MOVIE']
        self.option_query = ['FILE_HI_RES', 'FILE_ANIM_RES', 'FILE_LOW_RES',
                             'TAG', 'ORIGINAL_SELECTED_FILE', 'ORIGINAL_SELECTED_MOVIE',
                             'PUBLISH_INFO', 'PUBLISH_COMMENT', 'PDATA_TYPE', 'PUBLISH_ICON']
    def setMustQuery(self, corpPrefix, projectId, assetId, versionNumber,
                     publisherId, taskTypeCd, filePublish, movie):
        self.corpPrefix_value = corpPrefix
        self.projectId_value = projectId
        self.assetId_value = assetId
        self.versionNumber_value = versionNumber
        self.publisherId_value = publisherId
        self.taskTypeCd_value = taskTypeCd
        self.filePublish_value = filePublish
        self.movie_value = movie

    def setOptionQuery(self, fileHiRes, fileAnimRes, fileLowRes, tag,
                       originalSelectedFile, originalSelectedMovie, publishInfo,
                       publishComment, PdataType, publishIcon):
        if fileHiRes:
            self.fileHiRes_value = fileHiRes
        if fileAnimRes:
            self.fileAnimRes_value = fileAnimRes
        if fileLowRes:
            self.fileLowRes_value = fileLowRes
        if tag:
            self.tag_value = tag;
        if originalSelectedFile:
            self.originalSelectedFile_value = originalSelectedFile
        if originalSelectedMovie:
            self.originalSelectedMovie_value = originalSelectedMovie
        if publishInfo:
            self.publishInfo_value = publishInfo
        if publishComment:
            self.publishComment_value = publishComment
        if PdataType:
            self.PdataType_value = PdataType
        if publishIcon:
            self.publishIcon_value = publishIcon

class RECORD_IMPORT_ASSET_QUERY(DEFAULT_QUERY):
    def __init__(self):
        DEFAULT_QUERY.__init__(self)
        self.call_query = 'recordImportAsset.php'
        self.must_query = ['COMPANY_NAME', 'PROJECT_ID', 'USER_ID', 'TASK_TYPE', 'ASSET_ID', 'ASSET_VERSION']
        self.option_query = ['WORK_TYPE', 'SHOT_NM', 'ASSET_NM', 'WORKING_ASSET_DIR', 'WORKING_SHOT_DIR']

    def setMustQuery(self, corpPrefix, projectId, userId, taskTypeCd, assetId, assetVersion):
        self.corpPrefix_value = corpPrefix
        self.projectId_value = projectId
        self.userId_value = userId
        self.taskTypeCd_value = taskTypeCd
        self.assetId_value = assetId
        self.assetVersion_value = assetVersion

    def setOptionQuery(self, workType, shotNm, assetNm, workingAssetDir, workinmgShotDir):
        if workType:
            self.workType_value = workType
        if shotNm:
            self.shotNm_value = shotNm
        if assetNm:
            self.assetNm_value = assetNm
        if workingAssetDir:
            self.workingAssetDir_value = workingAssetDir
        if workinmgShotDir:
            self.workingShotDir_value = workinmgShotDir

class PUBLISH_SHOT_QUERY(DEFAULT_QUERY):
    def __init__(self):
        DEFAULT_QUERY.__init__(self)
        self.call_query = 'publishShot.php'
        self.must_query = ['COMPANY_NAME', 'PROJECT_ID', 'SHOT_ID',
                           'ASSET_LIST', 'VERSION_NUMBER', 'PUBLISHER_ID', 'TASK_TYPE',
                           'FILE', 'MOVIE']
        self.option_query = ['ORIGINAL_SELECTED_FILE', 'ORIGINAL_SELECTED_MOVIE',
                             'PRE_COMP_FILE', 'USER_EXTRA_GEOM',
                             'PUBLISH_INFO', 'PUBLISH_COMMENT', 'PDATA_TYPE', 'PUBLISH_ICON', 'CACHE_FILE']

    def setMustQuery(self, corpPrefix, projectId, shotId, assetList, versionNumber,
                         publisherId, taskTypeCd, file, movie):
        self.corpPrefix_value = corpPrefix
        self.projectId_value = projectId
        self.shotId_value = shotId
        self.assetList_value = assetList
        self.versionNumber_value = versionNumber
        self.publisherId_value = publisherId
        self.taskTypeCd_value = taskTypeCd
        self.file_value = file
        self.movie_value = movie


    def setOptionQuery(self, originalSelectedFile, originalSelectedMovie,
                        preCompFile, userExtraGeom, publishInfo, publishComment, PdataType, publishIcon, cacheFile):
        if originalSelectedFile:
            self.originalSelectedFile_value = originalSelectedFile
        if originalSelectedMovie:
            self.originalSelectedMovie_value = originalSelectedMovie

        if preCompFile:
            self.preCompFile_value = preCompFile
        if userExtraGeom:
            self.userExtraGeom_value = userExtraGeom
        if publishInfo:
            self.publishInfo_value = publishInfo
        if publishComment:
            self.publishComment_value = publishComment
        if PdataType:
            self.PdataType_value = PdataType
        if publishIcon:
            self.publishIcon_value = publishIcon
        if cacheFile:
            self.cacheFile_value = cacheFile


class CallUrl:

    isSuccess = False
    message = None

    def __init__(self):
        self.url = None
        self.data = None
        self.info = None
        self.result = None
        self.res_dict = {}

    def _applyResponse(self):
        #print self.url
        response = urllib2.urlopen(self.url)
        self.info = response.info()
        self.result = response.read()
        self.res_dict = json.loads(self.result)
        self.isSuccess = self.res_dict['isSuccess']
        self.message = self.res_dict['message']

    def setURL(self, url_path):
        #print url_path.encode('utf-8')
        self.url = url_path
        self._applyResponse()

    def getInfo(self):
        return self.info

    def getResult(self):
        return self.result

    def getRes_dict(self):
        return self.res_dict

    def getIsSuccess(self):
        return self.isSuccess

    def getMessage(self):
        return self.message

class FileUpload:
    def __init__(self,  corpPrefix = None):
        self.filename = ''
        self.corpPrefix_value = corpPrefix
        if USE_URL_CUSTOM[0]:
            self.rnt_query = 'http://%s/interface/upload.php' % (
                                            USE_URL_CUSTOM[1]
                                            )
            self.file_query = 'http://%s' % USE_URL_CUSTOM[1]
        else:
            self.rnt_query = 'http://%s%supload.php' % (
                                            self.corpPrefix_value,
                                            URL_ROOT
                                            )
            self.file_query = 'http://%s.wormholepipeline.co.kr' % self.corpPrefix_value

    def Upload(self, fullfilepath):
        self.filename = os.path.basename(fullfilepath)
        #rnt_path = '%s/tmp/%s' % (self.file_query, self.filename)
        rnt = self.__post_multipart([], [['uploadedfile', './tmp/%s' % self.filename, open(fullfilepath, 'rb').read()]])
        return self.filename, rnt

    def __post_multipart(self, fields, files):

        content_type, body = self.__encode_multipart_formdata(fields, files)
        headers = {'Content-Type': content_type,
                   'Content-Length': str(len(body))}
        r = urllib2.Request(self.rnt_query, body, headers)
        return urllib2.urlopen(r).read()

    def __encode_multipart_formdata(self, fields, files):
        BOUNDARY = '----------bound@ry_$'
        CRLF = '\r\n'
        L = []
        for (key, value) in fields:
            L.append('--' + BOUNDARY)
            L.append('Content-Disposition: form-data; name="%s"' % key)
            L.append('')
            L.append(value)
        for (key, filename, value) in files:
            L.append('--' + BOUNDARY)
            L.append('Content-Disposition: form-data; name="%s"; filename="%s"' % (key, filename))
            L.append('Content-Type: %s' % self.__get_content_type(filename))
            L.append('')
            L.append(value)
        L.append('--' + BOUNDARY + '--')
        L.append('')
        body = CRLF.join(L)
        content_type = 'multipart/form-data; boundary=%s' % BOUNDARY
        return content_type, body

    def __get_content_type(self, filename):
        return mimetypes.guess_type(filename)[0] or 'application/octet-stream'

    '''
        upload_file_url = 'http://demo.wormholepipeline.com/interface/upload.php'
        res = post_multipart(upload_file_url,[],
               [['uploadedfile', './tmp/cappng.png', open('C:\\temp\\cappng.png', 'rb').read()]]
               )
        print res
    '''