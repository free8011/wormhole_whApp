from wormholeAPI.whDataModels import whEnvData
from wormholeAPI.whAPIModels import whCompany
import whAPI
from checkos import ClientOs
from pprint import pprint

def gettaskinfo(env):
    shotname = u''
    pprint(env.__dict__)
    wh = whAPI.Get(corpPrefix=env.Company, url=env.ServerName)
    # pprint(wh.ContactList(projectId=env.Project,shotId=env.ShotId))

    for shots in (wh.ShotNames(projectId=env.Project,seqId=env.SeqName)['shotList']):
        if shots['shotId'] == env.ShotName:
            shotname = unicode(shots['shotNm'])
    for seqs in wh.Seqnames(projectId=env.Project)['sequenceList']:
        if seqs['sequenceId'] == env.SeqName:
            seqname = unicode(seqs['sequenceNm'])
            print seqname , env.SeqName
    if env.DirType == 'shot':
        env.__setattr__('SeqId',env.SeqName)
        env.__setattr__('SeqName',seqname)
        env.__setattr__('ShotId',env.ShotName)
        env.__setattr__('ShotName',shotname)
    env.__setattr__('ProjectName','projectname')
    # env.__setattr__('UserName',username)
    # pprint(env.__dict__)
    oscheck = ClientOs()
    env.__setattr__('SysUserHome',oscheck.userPath)
    env.__setattr__('OS',oscheck.getOSType)
    env.__setattr__('WhAppPath',oscheck.whAppPath)

    return env