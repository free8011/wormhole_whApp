# -*- coding:utf-8 -*-
import requests
import json
import urllib
import os
import sys
import time

class Get:
    def __init__(self,corpPrefix="",url=""):
        self.corpPrefix = corpPrefix
        self.url = "http://%s"% url

    def __getdata(self, apiname="", data={}):
        __apiname = apiname
        __data = data
        __apiUrl = '%s/interface/%s.php?'%(self.url ,__apiname)
        __data["corpPrefix"] = self.corpPrefix
        __api = requests.post(__apiUrl,data=__data)

        # return dict(json.loads(api.text,encoding="utf-8"))
        return __api.json()
    def getToken(self,ID="",PW="",data = {}, dictype = False):
        apiname = "getToken"
        if dictype:
            pass
        else:
            data["ID"] = ID
            data["PW"] = PW
        return self.__getdata(apiname = apiname, data = data)

    def AssetList(self,projectId="",assetId="",tag="",PdataType="",userId="",workingAssetDir="",workingShotDir="",tastTypeCd="",data={},dictype=False):
        apiname = "getAssetList"
        if dictype:
            pass
        else:
            data["projectId"] = projectId
            data["assetId"] = assetId
            data["tag"] = tag
            data["PdataType"] = PdataType
            data["userId"] = userId
            data["workingAssetDir"] = workingAssetDir
            data["workingShotDir"] = workingShotDir
            data["tastTypeCd"] = tastTypeCd
        return self.__getdata(apiname=apiname, data=data)

    def ShotList(self, projectId="", shotId="", userId="", workingShotDir="", tastTypeCd="",PdataType="", data={}, dictype=False):
        apiname = "getShotList"
        if dictype:
            pass
        else:
            data["projectId"] = projectId
            data["shotId"] = shotId
            data["userId"] = userId
            data["workingShotDir"] = workingShotDir
            data["tastTypeCd"] = tastTypeCd
            data["PdataType"] = PdataType
        return self.__getdata(apiname=apiname, data=data)

    def MovAbsNumber(self,projectId="",type="",assetId="",shotId="",data={},dictype=False):
        '''

        :param projectId:
        :param type:-> 'Movie' or 'asset' or 'shot'
        :param assetId:
        :param shotId:
        :param data:
        :param dictype:
        :return:
        '''
        apiname = "getMovAbsNumber"
        if dictype:
            pass
        else:
            data["projectId"] = projectId
            data["type"] = type
            data["assetId"] = assetId
            data["shotId"] = shotId
        return self.__getdata(apiname=apiname, data=data)

    def ContactList(self, projectId="", assetId="",shotId="", data={}, dictype=False):
        apiname ="getContactList"
        if dictype:
            pass
        else:
            data["projectId"] = projectId
            data["assetId"] = assetId
            data["shotId"] = shotId
        return self.__getdata(apiname=apiname, data=data)

    def ProjectPath(self, projectId="",data={}, dictype=False):
        apiname = "getProjectPath"
        if dictype:
            pass
        else:
            data["projectId"] = projectId
        return self.__getdata(apiname=apiname, data=data)
    def getInfo(self, projectId="",getType="",seqId="",assetId="",shotId="",data={}, dictype=False):
        apiname = "getInfo"
        if dictype:
            pass
        else:
            data["corpPrefix"] = self.corpPrefix
            data["projectId"] = projectId
            data["getType"] = getType
            data["seqId"] = seqId
            data["assetId"] = assetId
            data["shotId"] = shotId
        return self.__getdata(apiname=apiname, data=data)
    def ThumbnailPath(self, projectId="",getType="",seqId="",assetId="",shotId="",data={}, dictype=False):
        apiname = "getInfo"
        if dictype:
            pass
        else:
            data["projectId"] = projectId
            data["getType"] = getType
            data["seqId"] = seqId
            data["assetId"] = assetId
            data["shotId"] = shotId
        return self.__getdata(apiname=apiname, data=data)

    def ShotMovies(self , projectId="",mode="Latest",taskTypeCD="",seqId="",data={}, dictype=False):
        apiname = "getShotMovies"
        if dictype:
            pass
        else:
            data["projectId"] = projectId
            data["mode"] = mode["seqId"] = seqId
            data["taskTypeCD"] = taskTypeCD
            data["seqId"] = seqId
        return self.__getdata(apiname=apiname, data=data)

    def TaskTypeList(self):
        apiname = "getTaskTypeList"
        data={}
        return self.__getdata(apiname=apiname, data=data)

    def ProjectList(self):
        apiname = "listOfProjects"
        data = {}
        return self.__getdata(apiname=apiname, data=data)

    def Seqnames(self, projectId="", data={}, dictype=False):
        apiname ="getSeqnameList"
        if dictype:
            pass
        else:
            data["projectId"] = projectId
        return self.__getdata(apiname=apiname, data=data)

    def ShotNames(self,projectId="",seqId="", data={}, dictype=False):
        apiname = "getShotnameList"
        if dictype:
            pass
        else:
            data["projectId"] = projectId
            data["seqId"] = seqId
        return self.__getdata(apiname=apiname, data=data)

    def AssetIds(self, projectId="", data={}, dictype=False):
        apiname = "getAssetIDList"
        if dictype:
            pass
        else:
            data["projectId"] = projectId
        return self.__getdata(apiname=apiname, data=data)

    def ProjectUsers(self, projectId="", data={}, dictype=False):
        apiname = "getProjectUser"
        if dictype:
            pass
        else:
            data["projectId"] = projectId
        return self.__getdata(apiname=apiname, data=data)


    def SeqShotMovie(self,projectId="",seqId="",taskTypeCD="Latest",data={}, dictype=False):
        apiname = "getSeqShotMovie"
        if dictype:
            pass
        else:
            data["projectId"] = projectId
            data["seqId"] = seqId
            data["taskTypeCD"] = taskTypeCD
        return self.__getdata(apiname=apiname, data=data)


    def SeqMovieList(self,projectId="",seqId="ALL",data={}, dictype=False):
        apiname = "getSeqMovieList"
        if dictype:
            pass
        else:
            data["projectId"] = projectId
            data["seqId"] = seqId
        return self.__getdata(apiname=apiname, data=data)

    def UserInfo(self, projectId="", data={}, dictype=False):
        apiname = "getUserInfo"
        if dictype:
            pass
        else:
            data["projectId"] = projectId
        return self.__getdata(apiname=apiname, data=data)

    def AssetTaskLastVersionList(self, projectId="", assetId="", tag="", PdataType="", userId="", workingAssetDir="",
                  workingShotDir="", tastTypeCd="", data={}, dictype=False):
        '''
        :param projectId:
        :param assetId:
        :param tag:
        :param PdataType:
        :param userId:
        :param workingAssetDir:
        :param workingShotDir:
        :param tastTypeCd:
        :param data:
        :param dictype:
        :return:
        '''
        apiname = "getAssetTaskLastVersionList"
        print "comments : Get asset task latest version with multi assets by using '|'. To separate assetId like 'assetId|assetId'"
        if dictype:
            pass
        else:
            data["projectId"] = projectId
            data["assetId"] = assetId
            data["tag"] = tag
            data["PdataType"] = PdataType
            data["userId"] = userId
            data["workingAssetDir"] = workingAssetDir
            data["workingShotDir"] = workingShotDir
            data["tastTypeCd"] = tastTypeCd
        return self.__getdata(apiname=apiname, data=data)

    def ProjectFilePath(self, projectId="", data={}, dictype=False):
        '''
        :param projectId:
        :param data:
        :param dictype:
        :return:
        '''
        apiname = "getProjectFilePaths"
        if dictype:
            pass
        else:
            data["projectId"] = projectId
        return self.__getdata(apiname=apiname, data=data)

    # def ProjPath(self, projectId="", type='all', name='all',data={}, dictype=False):
    #     '''
    #
    #     :param projectId:
    #     :param type:
    #     :param name:
    #     :param data:
    #     :param dictype:
    #     :return:
    #     '''
    #     apiname = "getProjectFilePaths"
    #     if dictype:
    #         pass
    #     else:
    #         data["projectId"] = projectId
    #     preresult = self.__getdata(apiname=apiname, data=data)
    #     n = len(preresult['fixedPath'].keys())
    #     projpaths = preresult['fixedPath'].keys()
    #     pathTypes = preresult['pathType'].values()
    #     result =[]
    #     for i in range(n):
    #         if type == 'all' or type.lower() == pathTypes[i].lower():
    #             if name == 'all' or name==projpaths[i]:
    #                 patharr = {}
    #                 patharr['name'] = projpaths[i]
    #                 patharr['type'] = pathTypes[i]
    #                 patharr['path'] = preresult['fixedPath'][projpaths[i]]
    #                 result.append(patharr)
    #     return result
    def ProjPath(self, projectId="", type='all', name='all',data={}, dictype=False):
        '''
        :param projectId:
        :param type:
        :param name:
        :param name default value : "all"
        :param data:
        :param dictype:
        :return:
        '''
        apiname = "getProjectFilePaths"
        if dictype:
            pass
        else:
            data["projectId"] = projectId
        preresult = self.__getdata(apiname=apiname, data=data)
        n = len(preresult['fixedPath'].keys())
        projpaths = preresult['fixedPath'].keys()
        pathTypes = preresult['pathType'].values()
        result =[]
        for i in range(n):
            if type == 'all' or type.lower() == pathTypes[i].lower():
                if name == 'all' or name==projpaths[i]:
                    patharr = {}
                    patharr['name'] = projpaths[i]
                    patharr['type'] = pathTypes[i]
                    patharr['path'] = preresult['fixedPath'][projpaths[i]]
                    result.append(patharr)
        return result
    def UserAssign(self, projectId="",userId="",data={}, dictype=False):
        apiname = "getUserAssign"
        if dictype:
            pass
        else:
            data["projectId"] = projectId
            data["userId"] = userId
        return self.__getdata(apiname=apiname, data=data)

    def FavList(self, userId="",data={}, dictype=False):
        apiname = "FavList"
        if dictype:
            pass
        else:
            data["userId"] = userId
        return self.__getdata(apiname=apiname, data=data)

    def AssetInfo(self, projectId="", file="", PdataType="", data={}, dictype=False):
        apiname = "getAssetInfo"
        if dictype:
            pass
        else:
            data["projectId"] = projectId
            data["file"] = file
            data["PdataType"] = PdataType
        return self.__getdata(apiname=apiname, data=data)

    def TaskInfo(self, projectId="", reckey="", userId="", data={}, dictype=False):
        apiname = "getTaskInfo"
        if dictype:
            pass
            # 1. 꼭 data 값이 전부 들어와야 하는 경우 check.. 없는게 편할듯..
            # mustkeys = ["corpPrefix","projectId","reckey","userId"]
            # parkey = data.keys()
            # for key in mustkeys:
            #     if parkey.count(key) == 0:
            #         return  {"isSuccess ": "0","message": "input error takes exactly 4 arguments (not found %s)"% key}
            # 1. - end
        else:
            data["projectId"] = projectId
            data["reckey"] = reckey
            data["userId"] = userId
        return self.__getdata(apiname=apiname, data=data)




class Post():
    def __init__(self,corpPrefix="",url=""):
        self.corpPrefix = corpPrefix
        self.url = "http://%s"% url

    def __getdata(self, apiname="", data={}):
        __apiUrl = '%s/interface/%s.php?'%(self.url ,apiname)
        __data = data
        __data["corpPrefix"] = self.corpPrefix
        api = requests.post(__apiUrl,data=__data)
        # return dict(json.loads(api.text,encoding="utf-8"))
        return api.json()

    def recImportedAsset(self,projectId="",userId="",taskTypeCd="",assetId="",assetVersion="",workType="",shotNm="",assetNm="",workingAssetDir="",workingShotDir="",data={},dictype=False):
        apiname = "recordImportAsset"
        if dictype:
            pass
        else:
            data["projectId"] = projectId
            data["userId"] = userId
            data["taskTypeCd"] = taskTypeCd
            data["assetId"] = assetId
            data["assetVersion"] = assetVersion
            if workType == "":
                return "argument error : workType is 'a' or 's'. a = asset, s = shot."
            data["workType"] = workType
            data["shotNm"] = shotNm
            data["assetNm"] = assetNm
            data["workingAssetDir"] = workingAssetDir
            data["workingShotDir"] = workingShotDir
        return self.__getdata(apiname=apiname, data=data)

    def publishAsset(self,projectId="",assetId="",versionNumber="",publisherId="",taskTypeCd="",filePublish="",fileHiRes="",fileAnimRes="",fileLowRes="",movie="",tag="",originalSelectedFile="",originalSelectedMovie="",publishInfo="",publishComment="",PdataType="",publishIcon="",data={},dictype=False):
        apiname = "publishAsset"
        if dictype:
            data["publishComment"] = "<BR>".join(data["publishComment"].split("\n")).replace(' ', '%20')
        else:
            data["projectId"] = projectId
            data["assetId"] = assetId
            data["versionNumber"] = versionNumber
            data["publisherId"] = publisherId
            data["taskTypeCd"] = taskTypeCd
            data["filePublish"] = filePublish.replace('\\','/')
            data["fileHiRes"] = fileHiRes.replace('\\','/')
            data["fileAnimRes"] = fileAnimRes.replace('\\','/')
            data["fileLowRes"] = fileLowRes.replace('\\','/')
            data["movie"] = movie.replace('\\','/')
            data["tag"] = tag
            data["originalSelectedFile"] = originalSelectedFile.replace('\\','/')
            data["originalSelectedMovie"] = originalSelectedMovie.replace('\\','/')
            data["publishInfo"] = publishInfo
            data["publishComment"] = "<BR>".join(publishComment.split("\n")).replace(' ', '%20')
            data["PdataType"] = PdataType
            data["publishIcon"] = publishIcon.replace('\\','/')
        return self.__getdata(apiname=apiname, data=data)



    def recordImportShot(self, projectId="", shotId="", userId="", taskTypeCd="", workingShotDir="", versionNumber="", PdataType="",
                         file="", cacheFile="", preCompFile="",userExtraGeom="", data={}, dictype=False):
        apiname = "recordImportShot"
        if dictype:
            pass
        else:
            data["projectId"] = projectId
            data["shotId"] = shotId
            data["userId"] = userId
            data["taskTypeCd"] = taskTypeCd
            data["workingShotDir"] = workingShotDir
            data["versionNumber"] = versionNumber
            data["PdataType"] = PdataType
            data["file"] = file.replace('\\','/')
            data["cacheFile"] = cacheFile.replace('\\','/')
            data["preCompFile"] = preCompFile.replace('\\','/')
            data["userExtraGeom"] = userExtraGeom
        return self.__getdata(apiname=apiname, data=data)

    def publishShot(self, projectId="",shotId="",versionNumber="",publisherId="",taskTypeCd="",assetList="",assetListVer="",PdataType="",file="",cacheFile="",preCompFile="",userExtraGeom="",movie="",originalSelectedFile="",originalSelectedMovie="",publishInfo="",publishComment="",publishIcon="", data={}, dictype=False):
        apiname = "publishShot"
        if dictype:
            data["publishComment"] = "<BR>".join(data["publishComment"].split("\n"))
        else:
            data["projectId"] = projectId
            data["shotId"] = shotId
            data["versionNumber"] = versionNumber
            data["publisherId"] = publisherId
            data["taskTypeCd"] = taskTypeCd
            data["assetList"] = assetList
            data["assetListVer"] = assetListVer
            data["PdataType"] = PdataType
            data["file"] = file.replace('\\','/')
            data["cacheFile"] = cacheFile.replace('\\','/')
            data["preCompFile"] = preCompFile.replace('\\','/')
            data["userExtraGeom"] = userExtraGeom
            data["movie"] = movie.replace('\\','/')
            data["originalSelectedFile"] = originalSelectedFile.replace('\\','/')
            data["originalSelectedMovie"] = originalSelectedMovie.replace('\\','/')
            data["publishInfo"] = publishInfo
            data["publishComment"] = "<BR>".join(publishComment.split("\n")).replace(' ', '%20')
            data["publishIcon"] = publishIcon.replace('\\','/')
        return self.__getdata(apiname=apiname, data=data)


    def uploadMediafile(self, projectId="",imgFileName="",orgFilePath="",tag="",data={}, dictype=False):
        apiname = "uploadMediafile"
        if dictype:
            pass
        else:
            data["projectId"] = projectId
            if imgFileName != "":
                print "imgFileName is wormhole server path"
            data["imgFileName"] = imgFileName
            data["orgFilePath"] = orgFilePath.replace('\\','/')
            if tag !="":
                print "comments : Set tag with multi tag by using ','. Category is '/'. To separate tag or Category like 'tag1,Category1/tag2,tag3'"
            data["tag"] = tag
        return self.__getdata(apiname=apiname, data=data)

    def publishSequence(self, projectId="",sequenceId="",versionNumber="",publisherId="",taskTypeCd="",movie="",publishComment="",data={}, dictype=False):
        apiname = "publishSequence"
        if dictype:
            pass
        else:
            data["projectId"] = projectId
            data["sequenceId"] = sequenceId
            data["versionNumber"] = versionNumber
            data["publisherId"] = publisherId
            data["taskTypeCd"] = taskTypeCd
            data["movie"] = movie.replace('\\','/')
            data["publishComment"] = publishComment
        return self.__getdata(apiname=apiname, data=data)

    def reqReview(self, projectId="",nodeType="",nodeId="",taskTypeCd="",movie="",uploadFile="",reviewComment="",userId="",reviewerApr="",reviewerCC="",data={}, dictype=False):
        apiname = "reqReview"
        if dictype:
            pass
        else:
            data["projectId"] = projectId
            data["nodeType"] = nodeType
            data["nodeId"] = nodeId
            data["taskTypeCd"] = taskTypeCd
            data["movie"] = movie.replace('\\','/')
            data["uploadFile"] = uploadFile.replace('\\','/')
            data["reviewComment"] = reviewComment
            data["userId"] = userId
            data["reviewerApr"] = reviewerApr
            data["reviewerCC"] = reviewerCC
        return self.__getdata(apiname=apiname, data=data)

    def rvwReview(self, projectId="",rvwKey="",rvwUID="",rvwCMT="",status="",movFile="",data={}, dictype=False):
        apiname = "rvwReview"
        if dictype:
            pass
        else:
            data["projectId"] = projectId
            data["rvwKey"] = rvwKey
            data["rvwUID"] = rvwUID
            data["rvwCMT"] = rvwCMT
            data["status"] = status
            data["movFile"] = movFile.replace('\\','/')
        return self.__getdata(apiname=apiname, data=data)

    def thumbnail(self, projectId="",imgFileName="",workType="",data={}, dictype=False):
        apiname = "Upload_Thumbnail"
        if dictype:
            pass
        else:
            data["projectId"] = projectId
            data["imgFileName"] = imgFileName
            data["workType"] = workType
        return self.__getdata(apiname=apiname, data=data)

    def uploadedReviewFile(self, projectId="",fileName="",data={}, dictype=False):
        apiname = "UploadReviewFile"
        if dictype:
            pass
        else:
            data["projectId"] = projectId
            data["fileName"] = fileName.replace('\\','/')
        return self.__getdata(apiname=apiname, data=data)
