# -*- coding:utf-8 -*-
import os
from api import whAPI
from pprint import pprint
import bcopy
path = "D:\\tmp\\wormholeTest"
num_files = sum([len(files) for r, d, files in os.walk(path)])
print num_files

url = "simo.wormholepipeline.co.kr"
corpPrefix = "simo"
projectId = "test"
reckey = "24"
userId ="c2m"

# wh = whAPI.Get(corpPrefix=corpPrefix,url=url)
















#
# apiname = "TaskInfo"
# getTaskinfoDic = { "projectId":projectId, "reckey":reckey, "userId":userId}
# getTaskinfoDic2 = {"reckey":reckey}
#
# TaskinfData = wh.TaskInfo(data=getTaskinfoDic)
# pprint(TaskinfData)
#
# # getTaskInfo2 = wh.TaskInfo2(data=getTaskinfoDic,dictype=True)
# getTaskInfo2 = wh.TaskInfo(projectId=projectId,reckey=reckey,userId=userId)
# # pprint(getTaskInfo2)
#
#
# getTokenDic = {"corpPrefix":corpPrefix, "ID":userId, "PW":"c2m"}
#
# # Tocken = wh.getTocken(corpPrefix=corpPrefix,ID=userId,PW="c2m")
# Token = wh.getToken(data=getTokenDic,dictype=True)
# # pprint(Token)
#
# getAssetListDic = {"projectId":"TA","assetId":"A_A","tag":"","PdataType":"","userId":userId,"workingAssetDir":"","workingShotDir":"","tastTypeCd":"5"}
# AssetList = wh.AssetList(data=getAssetListDic,dictype=True)
# # pprint(AssetList)
#
#
# getShotList = wh.ShotList(projectId="TA",shotId="S_A",userId=userId,tastTypeCd='1')
# pprint(getShotList)
#
# pprint(wh.TaskTypeList())

# projPath = wh.ProjectFilePath(projectId=projectId)
# pprint(projPath)
# print help(wh.ProjPath)
# pprint(wh.ProjPath(projectId=projectId,type='A'))







