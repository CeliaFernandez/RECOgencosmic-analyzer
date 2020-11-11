import FWCore.ParameterSet.Config as cms

RECOgencosmicproducer = cms.EDAnalyzer('RECOgencosmicproducer',
    nameOfOutput = cms.string('output.root'),
    isData = cms.bool(True),
    EventInfo = cms.InputTag("generator"),
    bits = cms.InputTag("TriggerResults","","HLT"),
    RunInfo = cms.InputTag("generator"),
    BeamSpot = cms.InputTag("offlineBeamSpot"),
    GenParticleCollection = cms.InputTag("genParticles"),
    DGCollection = cms.InputTag("displacedGlobalMuons"),
    CosmicMuonCollection = cms.InputTag("muonsFromCosmics"),
    CosmicMuon1LegCollection = cms.InputTag("muonsFromCosmics1Leg"),
    theGenEventInfoProduct = cms.InputTag("generator"),
)


