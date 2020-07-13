import ROOT as r
from ROOT import gROOT
import math
import include.Canvas as Canvas

_file = r.TFile("/afs/cern.ch/work/f/fernance/private/CosmicStudy/SmallVolume/CMSSW_8_0_21/src/MyAnalysis/RECOgencosmic-analyzer/output.root")
_tree = _file.Get("Events")

gROOT.ProcessLine('.L include/tdrstyle.C')
gROOT.SetBatch(1)
r.setTDRStyle()

upperLegs = r.TH2F("upperLegs", "", 60, -30, 30, 60, -30, 30)
lowerLegs = r.TH2F("lowerLegs", "", 60, -30, 30, 60, -30, 30)


for _e,ev in enumerate(_tree):

    for i in range(0, ev.nDG):
        if ev.DG_phi[i] > 0:
            upperLegs.Fill(ev.DG_vx[i], ev.DG_vy[i])
        if ev.DG_phi[i] < 0:
            lowerLegs.Fill(ev.DG_vx[i], ev.DG_vy[i])
        
"""
PLOT = Canvas.Canvas('2Dplot', 'png', 0.6, 0.6, 0.89, 0.89, 1)
PLOT.addHisto(upperLegs, 'BOX', 'Upper legs', 'f', r.kRed, 1, 0)
PLOT.addHisto(lowerLegs, 'BOX, SAME', 'Lower legs', 'f', r.kBlue, 1, 2)
PLOT.save(1, 0, 0, '', '')
"""
lowerLegs.SetFillColor(r.kRed)
upperLegs.SetFillColor(r.kBlue)

c1 = r.TCanvas("c1", "", 600, 600)
lowerLegs.Draw("BOX")
upperLegs.Draw("BOX, SAME")
c1.SaveAs("2Dlegs.png")

allvolume = lowerLegs.Clone()
allvolume.Add(upperLegs)
allvolume.GetYaxis().SetTitle('DG muon v_{y} (cm)')
allvolume.GetXaxis().SetTitle('DG muon v_{x} (cm)')

PLOT = Canvas.Canvas('vxvyDGpop', 'png', 0.6, 0.6, 0.89, 0.89, 1)
PLOT.addHisto(allvolume, 'COLZ', '', 'f', r.kRed, 1, 0)
PLOT.save(0, 0, 0, '', '')

