# coding: utf-8

from wormholeAPI.whAPIModels import whCompany

class WhComAssetEnv:
    def __init__(self, envFile):
        if not envFile:
            raise RuntimeError("Must Set envfile value!")
        self.whcompany = whCompany()
        self.whcompany.setEnvFile(envFile)
        self.whproject = self.whcompany.getProject(self.whcompany.env.Project)
        self.whasset = self.whproject.getAsset(self.whcompany.env.AssetPrefix)




class WhComShotEnv:
    def __init__(self, envFile):
        if not envFile:
            raise RuntimeError("Must Set envfile value!")
        self.whcompany = whCompany()
        self.whcompany.setEnvFile(envFile)
        self.whproject = self.whcompany.getProject(self.whcompany.env.Project)
        self.whsequence = self.whproject.getSequence(self.whcompany.env.SeqName)
        self.whshot = self.whsequence.getShot(self.whcompany.env.ShotName)



class WhAssetList:
    def __init__(self, envFile):
        if not envFile:
            raise RuntimeError("Must Set envfile value!")
        self.whcompany = whCompany()
        self.whcompany.setEnvFile(envFile)
        self.whproject = self.whcompany.getProject(self.whcompany.env.Project)
        self.asset_list = self.whproject.asset_list
        self.asset_count = self.whproject.asset_count
        self.whassetlist = []
        for i in range(self.whproject.asset_count):
            self.whassetlist.append(self.asset_list[i].assetId)


class WhAssetPubHis:
    def __init__(self, envFile, assetId):
        self.whcompany = whCompany()
        self.whcompany.setEnvFile(envFile)
        self.whproject = self.whcompany.getProject(self.whcompany.env.Project)
        self.publishHis = self.whproject.getAsset(assetId).hist_list
        self.publishHis_count = self.whproject.getAsset(assetId).hist_count

class WhSequenceList:
    def __init__(self, envFile):
        self.whcompany = whCompany()
        self.whcompany.setEnvFile(envFile)
        self.whproject = self.whcompany.getProject(self.whcompany.env.Project)
        self.list = self.whproject.seq_list
        self.count = self.whproject.seq_count


class WhShotList:
    def __init__(self,envFile, sequenceId):
        self.whcompany = whCompany()
        self.whcompany.setEnvFile(envFile)
        self.whproject = self.whcompany.getProject(self.whcompany.env.Project)
        self.shot_list = []
        for seqid in self.whproject.seq_list:
            if sequenceId == 'all':
                try:
                    for shot in self.whproject.seq_id[seqid.sequenceId].loadShots():
                        self.shot_list.append(shot[1])
                except:
                    pass
            else:
                if seqId.sequenceId == sequenceId:
                    try:
                        for shot in self.whproject.seq_id[sequenceId].loadShots():
                            self.shot_list.append(shot[1])
                    except:
                        pass
class WhShotPubHis:
    def __init__(self,envFile,sequenceId, shotId):
        self.whcompany = whCompany()
        self.whcompany.setEnvFile(envFile)
        self.whproject = self.whcompany.getProject(self.whcompany.env.Project)
        self.whseq = self.whproject.__dict__
        print self.whseq

