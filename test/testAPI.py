# coding: utf-8
__author__ = 'c2monster'
import os, time
from wormholeAPI.whAPIModels import whCompany
from wormholeAPI.whAPIModels import whSequence
from wormholeAPI.whDataModels import whEnvData
from wormholeAPI.whAPIControls import WhSequenceList

from wormholeAPI.whAPIControls import WhShotPubHis
from wormholeAPI.whAPIControls import WhAssetPubHis

from pprint import pprint
import copy
import sys

envFile = os.path.abspath('')+'/wormHole.env'
whcom = whCompany()
env = whEnvData(envFile)
whcom.setEnvFile(envFile)
whcom.setCompanyId(env.Company)

projindex = None

for i in range(whcom.project_count):
    if str(whcom.project_list[i].projectId) == env.Project:
        projindex = i

nowTime = time.strftime("%Y.%m.%d_%H:%M",time.localtime())
try:
    whcom.project_list[projindex].paths.customReplaceEnv('CATEGORY','cha')

except: pass
whcom.project_list[projindex].paths.customReplaceEnv('DATE',nowTime)
pprint (whcom.project_list[projindex].paths.__dict__)

asset_list = whcom.getProject(env.Project).asset_list
for i in asset_list:
    print i.tag
'''
#print whcom.project_id[env.Project].__dict__
#print whcom.project_list[projindex].paths.__dict__
for asset in whcom.getProject(whcom.env.Project).asset_list:
    print asset.__dict__

    print asset.assetId
    print asset.snapShot
    print asset.assetNm

    for assetpub in WhAssetPubHis(envFile,str(asset.assetId)).publishHis:
        print assetpub.__dict__

wh = whcom.project_list[projindex]
print dir(whcom.project_list[projindex])
print wh.seq_count
print wh.seq_list[0].__dict__

'''
'''
#get sequence List & count
whseqlist=  WhSequenceList(envFile)
seqList = []
for seq in whseqlist.list:

    seqList.append(str(seq.sequenceId))
#print seqList
#print whseqlist.count

print '/'*100
'''

'''
#get shot List
project = whcom.project_id[env.Project]
shotList = []
for seq in project.loadSeqs():
    try:

        for shot in project.seq_id[str(seq[1])].loadShots():
            #print shotList.append(str(shot[1]))
            print project.seq_id[str(seq[1])].shot_id[shot[1]].__dict__
        #print len(project.seq_id[str(seq[1])].loadShots())
    except:
        pass
print shotList
'''
'''
# getshot List
from wormholeAPI.whAPIControls import WhShotList
shotList2 = WhShotList(envFile,'all')

print shotList2.shot_list
'''



'''
whProjectPath = whcom.project_list[projindex]
nowTime = time.strftime("%Y.%m.%d_%H_%M",time.localtime())
whProjectPath.paths.customReplaceEnv('DATE',nowTime)
'''

'''
for i in  range(whcom.project_count):
    whcom
    whPpaths = projectInfo.paths
'''
import socket
