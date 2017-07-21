from wormholeAPI.whDataModels import whEnvData
from wormholeAPI.whAPIModels import whCompany


def gettaskinfo(env):
    shotname = u''
    wh = whAPI.Get(corpPrefix=env.Company, url=env.ServerName)
    pprint(wh.ContactList(projectId=env.Project,shotId=env.ShotId))

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
    return env