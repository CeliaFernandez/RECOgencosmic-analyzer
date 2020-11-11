import FWCore.ParameterSet.Config as cms


process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("MyAnalysis.RECOgencosmic-analyzer.RECOgencosmic_cff")
process.load('Configuration.Geometry.GeometryRecoDB_cff')
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = '80X_mcRun2_asymptotic_2016_TrancheIV_v8'  # or some other global tag depending on your CMSSW release and sample. 
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
       [
'/store/user/tomalin/Cosmic_MC/CMSSW_10_2_5_AOD_v1c/200901_001748/0000/cosmic_AOD_1.root',
'/store/user/tomalin/Cosmic_MC/CMSSW_10_2_5_AOD_v1c/200901_001748/0000/cosmic_AOD_2.root',
'/store/user/tomalin/Cosmic_MC/CMSSW_10_2_5_AOD_v1c/200901_001748/0000/cosmic_AOD_3.root',
'/store/user/tomalin/Cosmic_MC/CMSSW_10_2_5_AOD_v1c/200901_001748/0000/cosmic_AOD_4.root',
'/store/user/tomalin/Cosmic_MC/CMSSW_10_2_5_AOD_v1c/200901_001748/0000/cosmic_AOD_5.root',
'/store/user/tomalin/Cosmic_MC/CMSSW_10_2_5_AOD_v1c/200901_001748/0000/cosmic_AOD_6.root',
'/store/user/tomalin/Cosmic_MC/CMSSW_10_2_5_AOD_v1c/200901_001748/0000/cosmic_AOD_7.root',
'/store/user/tomalin/Cosmic_MC/CMSSW_10_2_5_AOD_v1c/200901_001748/0000/cosmic_AOD_8.root',
'/store/user/tomalin/Cosmic_MC/CMSSW_10_2_5_AOD_v1c/200901_001748/0000/cosmic_AOD_9.root',
'/store/user/tomalin/Cosmic_MC/CMSSW_10_2_5_AOD_v1c/200901_001748/0000/cosmic_AOD_10.root',
'/store/user/tomalin/Cosmic_MC/CMSSW_10_2_5_AOD_v1c/200901_001748/0000/cosmic_AOD_11.root',
'/store/user/tomalin/Cosmic_MC/CMSSW_10_2_5_AOD_v1c/200901_001748/0000/cosmic_AOD_12.root',
'/store/user/tomalin/Cosmic_MC/CMSSW_10_2_5_AOD_v1c/200901_001748/0000/cosmic_AOD_13.root',
'/store/user/tomalin/Cosmic_MC/CMSSW_10_2_5_AOD_v1c/200901_001748/0000/cosmic_AOD_14.root',
'/store/user/tomalin/Cosmic_MC/CMSSW_10_2_5_AOD_v1c/200901_001748/0000/cosmic_AOD_15.root'
       ]
    )
)

process.options = cms.untracked.PSet()
process.options.numberOfThreads=cms.untracked.uint32(8)
process.options.numberOfStreams=cms.untracked.uint32(0)

process.p = cms.Path(process.RECOgencosmicproducer)


