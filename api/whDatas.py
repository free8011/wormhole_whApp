import os

import whAPI
from checkos import ClientOs


class WormholeData:
    def __init__(self, env):
        self.env = env
        self.projFilePath = {}
        self.wh = whAPI.Get(corpPrefix=self.env.Company, url=self.env.ServerName)

    def gettaskinfo(self):
        '''

        :return: set Task infomations.
        '''
        shotname = u''
        projName  = self.wh.getInfo(projectId=self.env.Project,getType='proj')['projectName']
        if self.env.DirType == 'shot':
            for seqs in self.wh.Seqnames(projectId=self.env.Project)['sequenceList']:
                if seqs['sequenceId'] == self.env.SeqName:
                    seqname = unicode(seqs['sequenceNm'])
            for shots in (self.wh.ShotNames(projectId=self.env.Project,seqId=self.env.SeqName)['shotList']):
                if shots['shotId'] == self.env.ShotName:
                    shotname = unicode(shots['shotNm'])
            self.env.__setattr__('category',None)
        elif self.env.DirType == 'asset':
            tag = self.wh.AssetList(projectId=self.env.Project,assetId=self.env.AssetPrefix)['AssetList'][0]['tag']
            if tag != '':
                category = tag.split(',')[0]
            elif tag == '':
                category = ''
            self.env.__setattr__('category',category)

        for users in self.wh.ProjectUsers(projectId=self.env.Project)['UserList']:
            if users['userId'] == self.env.UserID:
                username = unicode(users['userName'])

        self.env.__setattr__('SeqId','')
        self.env.__setattr__('ShotId','')
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
        version = float(self.wh.MovAbsNumber(projectId=self.env.Project, type=self.env.DirType,assetId=self.env.AssetPrefix,shotId=self.env.ShotId)['retNumber'])+1.0
        absnumber = int(self.wh.MovAbsNumber(projectId=self.env.Project, type='movie',assetId=self.env.AssetPrefix,shotId=self.env.ShotId)['retNumber'])
        self.env.__setattr__('VersionNumber',unicode(version))
        self.env.__setattr__('MovAbsNumber', unicode(absnumber))

        return self.env

    def ProjectFilePath(self,nametype = 'id',pdatatype=''):
        '''

        :param nametype:
        :param pdatatype:
        :return: publish paths(actual path)
        '''
        self.pathmap = {'[FILESERVERHOME]': self.env.ProjectHome, '[COMPANY]': self.env.Company,
                        '[PROJECTID]': self.env.Project, '[ASSETID]': self.env.AssetPrefix,
                        '[SEQUENCEID]': self.env.SeqId, '[SHOTID]': self.env.ShotId,
                        '[VERSIONNUMBER]':self.env.VersionNumber,'[PDATATYPE]':pdatatype,
                        '[TASKTYPEID]':self.env.TaskType,'[CATEGORY]':self.env.category,'[PUBLISHER]':self.env.UserID}

        if nametype == 'name':
            self.pathmap['[PROJECTID]']=self.env.ProjectName
            self.pathmap['[ASSETID]'] = self.env.AssetName
            self.pathmap['[SEQUENCEID]'] = self.env.SeqName
            self.pathmap['[SHOTID]'] = self.env.ShotName


        ProjectFilePath = self.wh.ProjectFilePath(projectId=self.env.Project)['fixedPath']
        # pathmap = ProjectFilePath

        # for k in  ProjectFilePath.keys():
        #     paths = ProjectFilePath[k]
        #     for ks in self.pathmap.keys():
        #         paths = paths.replace(str(ks), str(self.pathmap[ks]))

        for k ,paths in  ProjectFilePath.iteritems():
            for ks ,vs in self.pathmap.iteritems():
                paths = paths.replace(str(ks), str(vs))

            self.projFilePath[k] = os.path.normpath(paths)
        return self.projFilePath

    def ThumbnailPath(self):
        '''
        :return: Thumbnail url path
        '''

        taskinfodata = self.wh.ThumbnailPath(projectId=self.env.Project, getType=self.env.DirType,
                                             shotId=self.env.ShotId, assetId=self.env.AssetPrefix)
        if self.env.DirType == 'shot':
            taskthumbnailURL = taskinfodata['shotSnapShot']
        elif self.env.DirType == 'asset':
            taskthumbnailURL = taskinfodata['assetSnapShot']
        return taskthumbnailURL