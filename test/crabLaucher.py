from WMCore.Configuration import Configuration
config = Configuration()

config.section_('General')
config.General.transferLogs = True
config.General.requestName = 'cosmicRECOTuples_rsb2'

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'runRECOgencosmicproducer_cfg.py'
config.JobType.disableAutomaticOutputCollection = True
config.JobType.outputFiles = ['output.root']
config.section_('Data')
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.inputDataset = '/CosmicMuonsMCPrivate2016_smallVolume/fernance-step2_RAW2DIGI-L1Reco-RECO-EI-0f111def6b9b94823916592fdafc5ec9/USER'
config.Data.publication = False
config.Data.outLFNDirBase = '/store/user/fernance/' 

config.section_('Site')
config.Site.storageSite = 'T2_ES_IFCA'
