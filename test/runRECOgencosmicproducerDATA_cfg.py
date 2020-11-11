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
'/store/data/Run2018A/NoBPTX/AOD/17Sep2018-v1/100000/00F53C8B-15FF-1543-AB21-F15B1DBF1A6A.root',
       ]
    )
)

process.options = cms.untracked.PSet()
process.RECOgencosmicproducer.isData = True
process.RECOgencosmicproducer.nameOfOutput = "outputDATA.root"
#process.options.numberOfThreads=cms.untracked.uint32(8)
process.options.numberOfStreams=cms.untracked.uint32(0)

process.p = cms.Path(process.RECOgencosmicproducer)


