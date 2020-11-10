#include <memory>
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "SimDataFormats/GeneratorProducts/interface/HepMCProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/GenRunInfoProduct.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h" 

#include "DataFormats/Common/interface/Handle.h"

#include "DataFormats/RecoCandidate/interface/RecoCandidate.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "DataFormats/MuonReco/interface/Muon.h"

#include <string>
#include <iostream>
#include <vector>
#include <algorithm>

#include "TLorentzVector.h"
#include "TTree.h"
#include "TFile.h"


//=======================================================================================================================================================================================================================//


///////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////// FUNCTIONS ///////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////



/////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////// DATA DEFINITION //////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////



class RECOgencosmicproducer : public edm::one::EDAnalyzer<edm::one::SharedResources>  {
   public:
      explicit RECOgencosmicproducer(const edm::ParameterSet&);
      ~RECOgencosmicproducer();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() override;
      virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
      virtual void endJob() override;

      edm::ParameterSet parameters;
      std::string output_filename;

      //// Get Tokens ////
      edm::EDGetTokenT<edm::View<reco::GenParticle> > theGenParticleCollection;
      edm::EDGetTokenT<edm::View<reco::Track> > theDGCollection;
      edm::EDGetTokenT<edm::View<reco::Muon> > theCosmicMuonCollection;
      edm::EDGetTokenT<edm::View<reco::Muon> > theCosmicMuon1LegCollection;

      //// General info /////
      Int_t Event_event;
      Int_t Event_run;
      Int_t Event_luminosityBlock;

      //// Generated cosmic muon
      Float_t genMu_pt;
      Float_t genMu_phi;
      Float_t genMu_eta;
      Float_t genMu_px;
      Float_t genMu_py;
      Float_t genMu_pz;
      Float_t genMu_vx;
      Float_t genMu_vy;
      Float_t genMu_vz;
      Float_t genMu_dxy;
      Int_t genMu_q;

      //// Reconstructed displaced global muons
      Int_t nDG;
      Float_t DG_pt[100];
      Float_t DG_px[100];
      Float_t DG_py[100];
      Float_t DG_pz[100];
      Float_t DG_phi[100];
      Float_t DG_eta[100];
      Int_t DG_q[100];
      Float_t DG_dxy[100];
      Float_t DG_dxyError[100];
      Float_t DG_Ixy[100];
      Int_t DG_numberOfValidHits[100];
      Float_t DG_chi2[100];
      Float_t DG_ndof[100];
      Float_t DG_vx[100];
      Float_t DG_vy[100];
      Float_t DG_vz[100];


      //// Reconstructed cosmic muons
      Int_t nCM;
      Float_t CM_pt[100];
      Float_t CM_px[100];
      Float_t CM_py[100];
      Float_t CM_pz[100];
      Float_t CM_phi[100];
      Float_t CM_eta[100];
      Int_t CM_q[100];
      Float_t CM_dxy[100];
      Float_t CM_dxyError[100];
      Float_t CM_Ixy[100];
      Int_t CM_numberOfValidHits[100];
      Float_t CM_chi2[100];
      Float_t CM_ndof[100];
      Float_t CM_vx[100];
      Float_t CM_vy[100];
      Float_t CM_vz[100];
      Float_t CM_timeAtIpInOut[100];
      Float_t CM_timeAtIpOutIn[100];

      //// Reconstructed cosmic muons 1 leg
      Int_t nCM1L;
      Float_t CM1L_pt[100];
      Float_t CM1L_px[100];
      Float_t CM1L_py[100];
      Float_t CM1L_pz[100];
      Float_t CM1L_phi[100];
      Float_t CM1L_eta[100];
      Int_t CM1L_q[100];
      Float_t CM1L_dxy[100];
      Float_t CM1L_dxyError[100];
      Float_t CM1L_Ixy[100];
      Int_t CM1L_numberOfValidHits[100];
      Float_t CM1L_chi2[100];
      Float_t CM1L_ndof[100];
      Float_t CM1L_vx[100];
      Float_t CM1L_vy[100];
      Float_t CM1L_vz[100];
      Float_t CM1L_timeAtIpInOut[100];
      Float_t CM1L_timeAtIpOutIn[100];

      // Output definition:
      TFile *file_out;
      TTree *tree_out;

};
//=======================================================================================================================================================================================================================//




//=======================================================================================================================================================================================================================//
RECOgencosmicproducer::RECOgencosmicproducer(const edm::ParameterSet& iConfig)
{
   usesResource("TFileService");
   
   parameters = iConfig;

   theGenParticleCollection = consumes<edm::View<reco::GenParticle> >  (parameters.getParameter<edm::InputTag>("GenParticleCollection"));
   theDGCollection = consumes<edm::View<reco::Track> >  (parameters.getParameter<edm::InputTag>("DGCollection"));
   theCosmicMuonCollection = consumes<edm::View<reco::Muon> >  (parameters.getParameter<edm::InputTag>("CosmicMuonCollection"));
   theCosmicMuon1LegCollection = consumes<edm::View<reco::Muon> >  (parameters.getParameter<edm::InputTag>("CosmicMuon1LegCollection"));

}
//=======================================================================================================================================================================================================================//




//=======================================================================================================================================================================================================================//
RECOgencosmicproducer::~RECOgencosmicproducer()
{

}
//=======================================================================================================================================================================================================================//



//=======================================================================================================================================================================================================================//
void RECOgencosmicproducer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{

   /////////////////////////////////////////////////////////////////////////////////////
   ///////////////////////////////////// MAIN CODE /////////////////////////////////////
   /////////////////////////////////////////////////////////////////////////////////////



   //////////////////////////////// GET THE COLLECTIONS ////////////////////////////////
   
   edm::Handle<edm::View<reco::GenParticle> > genParticles;
   iEvent.getByToken(theGenParticleCollection, genParticles);

   edm::Handle<edm::View<reco::Track> > DGs;
   iEvent.getByToken(theDGCollection, DGs);
  
   edm::Handle<edm::View<reco::Muon> > CMs;
   iEvent.getByToken(theCosmicMuonCollection, CMs);

   edm::Handle<edm::View<reco::Muon> > CM1Ls;
   iEvent.getByToken(theCosmicMuon1LegCollection, CM1Ls);

   //////////////////////////////// EVENT INFO  ////////////////////////////////
   Event_event = iEvent.id().event();
   Event_run = iEvent.id().run();
   Event_luminosityBlock = iEvent.id().luminosityBlock();


   //////////////////////////////// GENERATED MUON  ////////////////////////////////

   // Loop to identify the generated muons
   for(size_t i = 0; i < genParticles->size(); i++) {

      const reco::GenParticle &particle = (*genParticles)[i];

      if ( abs( particle.pdgId() ) == 13 ){

         if ( particle.status() == 1 ) {

            genMu_pt = particle.pt();
            genMu_eta = particle.eta();
            genMu_phi = particle.phi();
            genMu_px = particle.px();
            genMu_py = particle.py();
            genMu_pz = particle.pz();
            genMu_vx = particle.vx();
            genMu_vy = particle.vy();
            genMu_vz = particle.vz();
            genMu_dxy = (-particle.vx()*particle.py() + particle.vy()*particle.px())/(particle.pt());
            genMu_q = particle.charge();


         }

      }

   }



   //////////////////////////////// DISPLACED GLOBAL MUONS  ////////////////////////////////
   nDG = 0;
   for(size_t i = 0; i < DGs->size(); i++) {

      const reco::Track &muon = (*DGs)[i];

      DG_pt[nDG] = muon.pt();
      DG_eta[nDG] = muon.eta();
      DG_phi[nDG] = muon.phi();
      DG_q[nDG] = muon.charge();
      DG_px[nDG] = muon.px();
      DG_py[nDG] = muon.py();
      DG_pz[nDG] = muon.pz();
      DG_dxy[nDG] = muon.dxy();
      DG_dxyError[nDG] = muon.dxyError();
      DG_Ixy[nDG] = fabs(muon.dxy())/muon.dxyError();
      DG_q[nDG] = muon.charge();
      DG_numberOfValidHits[nDG] = muon.numberOfValidHits();
      DG_chi2[nDG] = muon.chi2();
      DG_ndof[nDG] = muon.ndof();
      DG_vx[nDG] = muon.vx();
      DG_vy[nDG] = muon.vy();
      DG_vz[nDG] = muon.vz();

      nDG++;

   }

   nCM = 0;
   for(size_t i = 0; i < CMs->size(); i++) {

      const reco::Muon &muon = (*CMs)[i];
      
      CM_pt[nCM] = muon.pt();
      CM_eta[nCM] = muon.eta();
      CM_phi[nCM] = muon.phi();
      CM_q[nCM] = muon.charge();
      CM_px[nCM] = muon.px();
      CM_py[nCM] = muon.py();
      CM_pz[nCM] = muon.pz();
      CM_dxy[nCM] = muon.bestTrack()->dxy();
      CM_dxyError[nCM] = muon.bestTrack()->dxyError();
      CM_Ixy[nCM] = fabs(muon.bestTrack()->dxy())/muon.bestTrack()->dxyError();
      CM_q[nCM] = muon.charge();
      CM_numberOfValidHits[nCM] = muon.bestTrack()->numberOfValidHits();
      CM_chi2[nCM] = muon.bestTrack()->chi2();
      CM_ndof[nCM] = muon.bestTrack()->ndof();
      CM_vx[nCM] = muon.vx();
      CM_vy[nCM] = muon.vy();
      CM_vz[nCM] = muon.vz();
      CM_timeAtIpInOut[nCM] = muon.time().timeAtIpInOut;
      CM_timeAtIpOutIn[nCM] = muon.time().timeAtIpOutIn;
      
      nCM++;

   }


   nCM1L = 0;
   for(size_t i = 0; i < CM1Ls->size(); i++) {

      const reco::Muon &muon = (*CM1Ls)[i];
      
      CM1L_pt[nCM1L] = muon.pt();
      CM1L_eta[nCM1L] = muon.eta();
      CM1L_phi[nCM1L] = muon.phi();
      CM1L_q[nCM1L] = muon.charge();
      CM1L_px[nCM1L] = muon.px();
      CM1L_py[nCM1L] = muon.py();
      CM1L_pz[nCM1L] = muon.pz();
      CM1L_dxy[nCM1L] = muon.bestTrack()->dxy();
      CM1L_dxyError[nCM1L] = muon.bestTrack()->dxyError();
      CM1L_Ixy[nCM1L] = fabs(muon.bestTrack()->dxy())/muon.bestTrack()->dxyError();
      CM1L_q[nCM1L] = muon.charge();
      CM1L_numberOfValidHits[nCM1L] = muon.bestTrack()->numberOfValidHits();
      CM1L_chi2[nCM1L] = muon.bestTrack()->chi2();
      CM1L_ndof[nCM1L] = muon.bestTrack()->ndof();
      CM1L_vx[nCM1L] = muon.vx();
      CM1L_vy[nCM1L] = muon.vy();
      CM1L_vz[nCM1L] = muon.vz();
      CM1L_timeAtIpInOut[nCM] = muon.time().timeAtIpInOut;
      CM1L_timeAtIpOutIn[nCM] = muon.time().timeAtIpOutIn;
      
      nCM1L++;

   }


   // Fill the tree
   tree_out->Fill();

}











//=======================================================================================================================================================================================================================//




//=======================================================================================================================================================================================================================//
void RECOgencosmicproducer::beginJob()
{
  std::cout << "Begin Job" << std::endl;

  output_filename = parameters.getParameter<std::string>("nameOfOutput");
  file_out = new TFile(output_filename.c_str(), "RECREATE");


  // -> Output tree definition

  tree_out = new TTree("Events", "Events"); // declaration

  // Branches:

  tree_out->Branch("Event_event", &Event_event, "Event_event/I");

  tree_out->Branch("genMu_pt", &genMu_pt, "genMu_pt/F");
  tree_out->Branch("genMu_px", &genMu_px, "genMu_px/F");
  tree_out->Branch("genMu_py", &genMu_py, "genMu_py/F");
  tree_out->Branch("genMu_pz", &genMu_pz, "genMu_pz/F");
  tree_out->Branch("genMu_eta", &genMu_eta, "genMu_eta/F");
  tree_out->Branch("genMu_phi", &genMu_phi, "genMu_phi/F");
  tree_out->Branch("genMu_vx", &genMu_vx, "genMu_vx/F");
  tree_out->Branch("genMu_vy", &genMu_vy, "genMu_vy/F");
  tree_out->Branch("genMu_vz", &genMu_vz, "genMu_vz/F");
  tree_out->Branch("genMu_dxy", &genMu_dxy, "genMu_dxy/F");
  tree_out->Branch("genMu_q", &genMu_q, "genMu_q/I");

  tree_out->Branch("nDG", &nDG, "nDG/I");
  tree_out->Branch("DG_pt", DG_pt, "DG_pt[nDG]/F");
  tree_out->Branch("DG_px", DG_px, "DG_px[nDG]/F");
  tree_out->Branch("DG_py", DG_py, "DG_py[nDG]/F");
  tree_out->Branch("DG_pz", DG_pz, "DG_pz[nDG]/F");
  tree_out->Branch("DG_eta", DG_eta, "DG_eta[nDG]/F");
  tree_out->Branch("DG_phi", DG_phi, "DG_phi[nDG]/F");
  tree_out->Branch("DG_q", DG_q, "DG_q[nDG]/I");
  tree_out->Branch("DG_vx", DG_vx, "DG_vx[nDG]/F");
  tree_out->Branch("DG_vy", DG_vy, "DG_vy[nDG]/F");
  tree_out->Branch("DG_vz", DG_vz, "DG_vz[nDG]/F");
  tree_out->Branch("DG_dxy", DG_dxy, "DG_dxy[nDG]/F");
  tree_out->Branch("DG_dxyError", DG_dxyError, "DG_dxyError[nDG]/F");
  tree_out->Branch("DG_Ixy", DG_Ixy, "DG_Ixy[nDG]/F");
  tree_out->Branch("DG_numberOfValidHits", DG_numberOfValidHits, "DG_numberOfValidHits[nDG]/I");
  tree_out->Branch("DG_chi2", DG_chi2, "DG_chi2[nDG]/F");
  tree_out->Branch("DG_ndof", DG_ndof, "DG_ndof[nDG]/F");

  tree_out->Branch("nCM", &nCM, "nCM/I");
  tree_out->Branch("CM_pt", CM_pt, "CM_pt[nCM]/F");
  tree_out->Branch("CM_px", CM_px, "CM_px[nCM]/F");
  tree_out->Branch("CM_py", CM_py, "CM_py[nCM]/F");
  tree_out->Branch("CM_pz", CM_pz, "CM_pz[nCM]/F");
  tree_out->Branch("CM_eta", CM_eta, "CM_eta[nCM]/F");
  tree_out->Branch("CM_phi", CM_phi, "CM_phi[nCM]/F");
  tree_out->Branch("CM_q", CM_q, "CM_q[nCM]/I");
  tree_out->Branch("CM_vx", CM_vx, "CM_vx[nCM]/F");
  tree_out->Branch("CM_vy", CM_vy, "CM_vy[nCM]/F");
  tree_out->Branch("CM_vz", CM_vz, "CM_vz[nCM]/F");
  tree_out->Branch("CM_dxy", CM_dxy, "CM_dxy[nCM]/F");
  tree_out->Branch("CM_dxyError", CM_dxyError, "CM_dxyError[nCM]/F");
  tree_out->Branch("CM_Ixy", CM_Ixy, "CM_Ixy[nCM]/F");
  tree_out->Branch("CM_numberOfValidHits", CM_numberOfValidHits, "CM_numberOfValidHits[nCM]/I");
  tree_out->Branch("CM_chi2", CM_chi2, "CM_chi2[nCM]/F");
  tree_out->Branch("CM_ndof", CM_ndof, "CM_ndof[nCM]/F");
  tree_out->Branch("CM_timeAtIpInOut", CM_timeAtIpInOut, "CM_timeAtIpInOut[nCM]/F");
  tree_out->Branch("CM_timeAtIpOutIn", CM_timeAtIpOutIn, "CM_timeAtIpOutIn[nCM]/F");


  tree_out->Branch("nCM1L", &nCM1L, "nCM1L/I");
  tree_out->Branch("CM1L_pt", CM1L_pt, "CM1L_pt[nCM1L]/F");
  tree_out->Branch("CM1L_px", CM1L_px, "CM1L_px[nCM1L]/F");
  tree_out->Branch("CM1L_py", CM1L_py, "CM1L_py[nCM1L]/F");
  tree_out->Branch("CM1L_pz", CM1L_pz, "CM1L_pz[nCM1L]/F");
  tree_out->Branch("CM1L_eta", CM1L_eta, "CM1L_eta[nCM1L]/F");
  tree_out->Branch("CM1L_phi", CM1L_phi, "CM1L_phi[nCM1L]/F");
  tree_out->Branch("CM1L_q", CM1L_q, "CM1L_q[nCM1L]/I");
  tree_out->Branch("CM1L_vx", CM1L_vx, "CM1L_vx[nCM1L]/F");
  tree_out->Branch("CM1L_vy", CM1L_vy, "CM1L_vy[nCM1L]/F");
  tree_out->Branch("CM1L_vz", CM1L_vz, "CM1L_vz[nCM1L]/F");
  tree_out->Branch("CM1L_dxy", CM1L_dxy, "CM1L_dxy[nCM1L]/F");
  tree_out->Branch("CM1L_dxyError", CM1L_dxyError, "CM1L_dxyError[nCM1L]/F");
  tree_out->Branch("CM1L_Ixy", CM1L_Ixy, "CM1L_Ixy[nCM1L]/F");
  tree_out->Branch("CM1L_numberOfValidHits", CM1L_numberOfValidHits, "CM1L_numberOfValidHits[nCM1L]/I");
  tree_out->Branch("CM1L_chi2", CM1L_chi2, "CM1L_chi2[nCM1L]/F");
  tree_out->Branch("CM1L_ndof", CM1L_ndof, "CM1L_ndof[nCM1L]/F");
  tree_out->Branch("CM1L_timeAtIpInOut", CM1L_timeAtIpInOut, "CM1L_timeAtIpInOut[nCM1L]/F");
  tree_out->Branch("CM1L_timeAtIpOutIn", CM1L_timeAtIpOutIn, "CM1L_timeAtIpOutIn[nCM1L]/F");

}
//=======================================================================================================================================================================================================================//
void RECOgencosmicproducer::endJob()
{
  std::cout << "End Job" << std::endl;

  file_out->cd();
  tree_out->Write();
  file_out->Close();

}




//=======================================================================================================================================================================================================================//
void RECOgencosmicproducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}
//=======================================================================================================================================================================================================================//
/*
void RECOgencosmicproducer::getCorrectDaughter(const reco::Candidate *c)
{

   for (size_t q = 0; q < c->numberOfDaughters(); q++){

      if (c->pdgId() == c->daughter(q)->pdgId()) { return q; }

   }

   return -1;

}
*/


DEFINE_FWK_MODULE(RECOgencosmicproducer);
