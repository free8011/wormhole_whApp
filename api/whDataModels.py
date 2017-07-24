from wormholeAPI.whDataModels import whEnvData
from wormholeAPI.whAPIModels import whCompany
import os
import whAPI
from checkos import ClientOs
from pprint import pprint
class WormholeData:
    def __init__(self, env):
        self.env = env
        self.projFilePath = {}

        self.wh = whAPI.Get(corpPrefix=self.env.Company, url=self.env.ServerName)


    def gettaskinfo(self):
        shotname = u''
        projName  =self.wh.getInfo(projectId=self.env.Project,getType='proj')['projectName']

        for seqs in self.wh.Seqnames(projectId=self.env.Project)['sequenceList']:
            if seqs['sequenceId'] == self.env.SeqName:
                seqname = unicode(seqs['sequenceNm'])
        for shots in (self.wh.ShotNames(projectId=self.env.Project,seqId=self.env.SeqName)['shotList']):
            if shots['shotId'] == self.env.ShotName:
                shotname = unicode(shots['shotNm'])
        for users in self.wh.ProjectUsers(projectId=self.env.Project)['UserList']:
            if users['userId'] == self.env.UserID:
                username = unicode(users['userName'])

        if self.env.DirType == 'shot':
            self.env.__setattr__('SeqId',self.env.SeqName)
            self.env.__setattr__('SeqName',seqname)
            self.env.__setattr__('ShotId',self.env.ShotName)
            self.env.__setattr__('ShotName',shotname)
        self.env.__setattr__('ProjectName',projName)
        oscheck = ClientOs()
        self.env.__setattr__('SysUserHome',oscheck.userPath)
        self.env.__setattr__('OS',oscheck.getOSType)
        self.env.__setattr__('WhAppPath',oscheck.whAppPath)
        self.env.__setattr__('UserName',username)

        return self.env

    def ProjectFilePath(self, nametype='id'):
        # pprint(self.wh.MovAbsNumber(projectId=self.env.Project, type=self.env.DirType,assetId=self.env.AssetPrefix,shotId=self.env.ShotId)['retNumber'])
        version = float(self.wh.MovAbsNumber(projectId=self.env.Project, type=self.env.DirType,assetId=self.env.AssetPrefix,shotId=self.env.ShotId)['retNumber'])+1.0
        self.pathmap = {'[FILESERVERHOME]': self.env.ProjectHome, '[COMPANY]': self.env.Company,
                        '[PROJECTID]': self.env.ProjectName, '[ASSETID]': self.env.AssetPrefix,
                        '[SEQUENCEID]': self.env.SeqId, '[SHOTID]': self.env.ShotId, '[VERSIONNUMBER]':str(version),'[PDATATYPE]':'IMAGE'}
        if nametype == 'name':
            self.pathmap['[PROJECTID]']=self.env.ProjectName
            self.pathmap['[ASSETID]'] = self.env.AssetName
            self.pathmap['[SEQUENCEID]'] = self.env.SeqName
            self.pathmap['[SHOTID]'] = self.env.ShotName



        ProjectFilePath = self.wh.ProjectFilePath(projectId=self.env.Project)['fixedPath']
        # pathmap = ProjectFilePath

        for k in  ProjectFilePath.keys():
            paths = ProjectFilePath[k]
            for ks in self.pathmap.keys():
                paths = paths.replace(str(ks), str(self.pathmap[ks]))

            self.projFilePath[k] = os.path.normpath(paths)

        return self.projFilePath








        # if self.env.DirType == 'shot':

    def ThumbnailPath(self):

        taskinfodata = self.wh.ThumbnailPath(projectId=self.env.Project, getType=self.env.DirType,
                                             shotId=self.env.ShotId, assetId=self.env.AssetPrefix)
        if self.env.DirType == 'shot':
            taskthumbnailURL = taskinfodata['shotSnapShot']
        elif self.env.DirType == 'asset':
            taskthumbnailURL = taskinfodata['assetSnapShot']
        return taskthumbnailURL