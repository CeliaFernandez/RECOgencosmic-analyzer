import ROOT as r


_f = r.TFile("outHist_30k.root")
_h = _f.Get('30k_h_nDG')

for n in range(1, _h.GetNbinsX() + 1):

    print('Bin ' + str(n) + ': ' + str(_h.GetBinContent(n)))
    print('nDG = ' + str(n - 1) + ': ' + str(_h.GetBinContent(n)/_h.GetEntries()))


_t = r.TChain("Events")
_t.Add('/afs/cern.ch/work/f/fernance/private/CosmicStudy/SmallVolume/CMSSW_8_0_21/src/MyAnalysis/RECOgencosmic-analyzer/output_1.root')
_t.Add('/afs/cern.ch/work/f/fernance/private/CosmicStudy/SmallVolume/CMSSW_8_0_21/src/MyAnalysis/RECOgencosmic-analyzer/output_2.root')
_t.Add('/afs/cern.ch/work/f/fernance/private/CosmicStudy/SmallVolume/CMSSW_8_0_21/src/MyAnalysis/RECOgencosmic-analyzer/output_3.root')

DG1_p = 0.0
DG1_m = 0.0
DG2_p = 0.0
DG2_m = 0.0

for ev in _t:

    phi_p = 0.0
    phi_m = 0.0

    for n in range(0, ev.nDG):
        if ev.DG_phi[n] > 0: phi_p+=1   
        if ev.DG_phi[n] < 0: phi_m+=1 

    if ev.nDG == 1:
        DG1_p = DG1_p + phi_p
        DG1_m = DG1_m + phi_m
    if ev.nDG == 2:
        DG2_p = DG2_p + phi_p
        DG2_m = DG2_m + phi_m

print("> DG = 1:")
print("DG_p", DG1_p / (DG1_p+DG1_m))
print("DG_m", DG1_m / (DG1_p+DG1_m))
print("> DG = 2:")
print("DG_p", DG2_p / (DG2_p+DG2_m))
print("DG_m", DG2_m / (DG2_p+DG2_m))

  


