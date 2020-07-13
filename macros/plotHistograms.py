import ROOT as r
from ROOT import gROOT
import optparse
import copy
import include.Canvas as Canvas


def plotSelection(histoList, name, log = False, xlabel = '', normed = False, legend = False, fill = True):

    plot = Canvas.Canvas(name, 'png', 0.15, 0.77, 0.9, 0.88, 1)

    sel = []
    ymax = 0.0
    for histo in histoList:
        _f = r.TFile(histo[0])
        aux_h = copy.deepcopy(_f.Get(histo[1]))
        if normed: aux_h.Scale(1/aux_h.Integral())
        if aux_h.GetMaximum() > ymax: ymax = aux_h.GetMaximum()


    for h,histo in enumerate(histoList):
        _f = r.TFile(histo[0])
        _h = copy.deepcopy(_f.Get(histo[1]))
        _f.Close()
        if xlabel != '':_h.GetXaxis().SetTitle(xlabel)

        if normed: 
            _h.Scale(1/_h.Integral())
            _h.GetYaxis().SetTitle('Event density')
        else:
            _h.GetYaxis().SetTitle('Events')

        if log: _h.SetMaximum(10.0*ymax)
        else: _h.SetMaximum(1.3*ymax)

        option = 'HIST'
        if h != 0: option = 'HIST, SAME'

        if fill:
            _h.SetLineColor(histo[2])
            _h.SetFillColorAlpha(histo[2], 0.5)
            plot.addHisto(_h, option, histo[3], 'f', '', 1, h)        
        else:
            plot.addHisto(_h, option, histo[3], 'f', histo[2], 1, h)        

    plot.save(legend, 0, log, '', '', outputDir = 'plots', maxYnumbers = 3)


if __name__=='__main__':


    #########################
    ###   Parser object   ###   
    #########################
    """
    parser = optparse.OptionParser(usage='usage: %prog [opts] FilenameWithSamples', version='%prog 1.0')
    parser.add_option('-i', '--input', action='store', type=str, dest='inputFile', default='launchWithGridui/merged.root', help='the input file. default \'merged.root\'')
    parser.add_option('-t', '--tag', action='store', type=str, dest='tag', default='launchWithGridui/merged.root', help='the input file. default \'merged.root\'')
    (opts, args) = parser.parse_args()
    """

    ############# Set the TDR plot style
    gROOT.ProcessLine('.L ' +'include/tdrstyle.C')
    gROOT.SetBatch(1)
    r.setTDRStyle()


    ###########################
    ###   Drawing objects   ###   
    ###########################
    
    """ format: [file, name, color, label] """
    h_genMu_pt = []
    h_genMu_pt.append( ['outHist_45k.root', '45k_h_genMu_pt', r.kAzure-7, ''] )
    plotSelection(h_genMu_pt, name = 'h_genMu_pt', log = True, xlabel = '', normed = False)

    h_genMu_eta = []
    h_genMu_eta.append( ['outHist_45k.root', '45k_h_genMu_eta', r.kAzure-7, ''] )
    plotSelection(h_genMu_eta, name = 'h_genMu_eta', log = False, xlabel = '', normed = False)

    h_genMu_phi = []
    h_genMu_phi.append( ['outHist_45k.root', '45k_h_genMu_phi', r.kAzure-7, ''] )
    plotSelection(h_genMu_phi, name = 'h_genMu_phi', log = False, xlabel = '', normed = False)

    h_genMu_dxy = []
    h_genMu_dxy.append( ['outHist_45k.root', '45k_h_genMu_dxy', r.kAzure-7, ''] )
    plotSelection(h_genMu_dxy, name = 'h_genMu_dxy', log = False, xlabel = '', normed = False)

    h_genMu_vx = []
    h_genMu_vx.append( ['outHist_45k.root', '45k_h_genMu_vx', r.kAzure-7, ''] )
    plotSelection(h_genMu_vx, name = 'h_genMu_vx', log = False, xlabel = '', normed = False)
    h_genMu_vy = []
    h_genMu_vy.append( ['outHist_45k.root', '45k_h_genMu_vy', r.kAzure-7, ''] )
    plotSelection(h_genMu_vy, name = 'h_genMu_vy', log = False, xlabel = '', normed = False)
    h_genMu_vz = []
    h_genMu_vz.append( ['outHist_45k.root', '45k_h_genMu_vz', r.kAzure-7, ''] )
    plotSelection(h_genMu_vz, name = 'h_genMu_vz', log = False, xlabel = '', normed = False)

    h_genMu_px = []
    h_genMu_px.append( ['outHist_45k.root', '45k_h_genMu_px', r.kAzure-7, ''] )
    plotSelection(h_genMu_px, name = 'h_genMu_px', log = True, xlabel = '', normed = False)
    h_genMu_py = []
    h_genMu_py.append( ['outHist_45k.root', '45k_h_genMu_py', r.kAzure-7, ''] )
    plotSelection(h_genMu_py, name = 'h_genMu_py', log = True, xlabel = '', normed = False)
    h_genMu_pz = []
    h_genMu_pz.append( ['outHist_45k.root', '45k_h_genMu_pz', r.kAzure-7, ''] )
    plotSelection(h_genMu_pz, name = 'h_genMu_pz', log = True, xlabel = '', normed = False)

    h_genMu_q = []
    h_genMu_q.append( ['outHist_45k.root', '45k_h_genMu_q', r.kAzure-7, ''] )
    plotSelection(h_genMu_q, name = 'h_genMu_q', log = False, xlabel = '', normed = False)

    h_nDG = []
    h_nDG.append( ['outHist_45k.root', '45k_h_nDG', r.kAzure-7, ''] )
    plotSelection(h_nDG, name = 'h_nDG', log = False, xlabel = '', normed = False)

    h_DG_pt = []
    h_DG_pt.append( ['outHist_45k.root', '45k_h_DG_pt', r.kAzure-7, ''] )
    plotSelection(h_DG_pt, name = 'h_DG_pt', log = True, xlabel = '', normed = False)

    h_DG_eta = []
    h_DG_eta.append( ['outHist_45k.root', '45k_h_DG_eta', r.kAzure-7, ''] )
    plotSelection(h_DG_eta, name = 'h_DG_eta', log = False, xlabel = '', normed = False)

    h_DG_phi = []
    h_DG_phi.append( ['outHist_45k.root', '45k_h_DG_phi', r.kAzure-7, ''] )
    plotSelection(h_DG_phi, name = 'h_DG_phi', log = False, xlabel = '', normed = False)

    h_DG_dxy = []
    h_DG_dxy.append( ['outHist_45k.root', '45k_h_DG_dxy', r.kAzure-7, ''] )
    plotSelection(h_DG_dxy, name = 'h_DG_dxy', log = False, xlabel = '', normed = False)

    h_DG_dxyError = []
    h_DG_dxyError.append( ['outHist_45k.root', '45k_h_DG_dxyError', r.kAzure-7, ''] )
    plotSelection(h_DG_dxyError, name = 'h_DG_dxyError', log = True, xlabel = '', normed = False)

    h_DG_Ixy = []
    h_DG_Ixy.append( ['outHist_45k.root', '45k_h_DG_Ixy', r.kAzure-7, ''] )
    plotSelection(h_DG_Ixy, name = 'h_DG_Ixy', log = False, xlabel = '', normed = False)

    h_DG_vx = []
    h_DG_vx.append( ['outHist_45k.root', '45k_h_DG_vx', r.kAzure-7, ''] )
    plotSelection(h_DG_vx, name = 'h_DG_vx', log = False, xlabel = '', normed = False)
    h_DG_vy = []
    h_DG_vy.append( ['outHist_45k.root', '45k_h_DG_vy', r.kAzure-7, ''] )
    plotSelection(h_DG_vy, name = 'h_DG_vy', log = False, xlabel = '', normed = False)
    h_DG_vz = []
    h_DG_vz.append( ['outHist_45k.root', '45k_h_DG_vz', r.kAzure-7, ''] )
    plotSelection(h_DG_vz, name = 'h_DG_vz', log = False, xlabel = '', normed = False)

    h_DG_q = []
    h_DG_q.append( ['outHist_45k.root', '45k_h_DG_q', r.kAzure-7, ''] )
    plotSelection(h_DG_q, name = 'h_DG_q', log = False, xlabel = '', normed = False)

    h_DG_normChi2 = []
    h_DG_normChi2.append( ['outHist_45k.root', '45k_h_DG_normChi2', r.kAzure-7, ''] )
    plotSelection(h_DG_normChi2, name = 'h_DG_normChi2', log = False, xlabel = '', normed = False)

    h_DG_numberOfValidHits = []
    h_DG_numberOfValidHits.append( ['outHist_45k.root', '45k_h_DG_numberOfValidHits', r.kAzure-7, ''] )
    plotSelection(h_DG_numberOfValidHits, name = 'h_DG_numberOfValidHits', log = False, xlabel = '', normed = False)

    """
    LxyPlot = []
    LxyPlot.append( ['outHist_400_150_400.root', '400_150_400_h_LLP_Lxy', r.kBlue+-4, 'm_{H} = 400 GeV, m_{X} = 150 GeV, c#tau = 40 cm'] )
    LxyPlot.append( ['outHist_400_150_40.root', '400_150_40_h_LLP_Lxy', r.kBlue-9, 'm_{H} = 400 GeV, m_{X} = 150 GeV, c#tau = 4 cm'] )
    LxyPlot.append( ['outHist_1000_150_100.root', '1000_150_100_h_LLP_Lxy', r.kRed+1, 'm_{H} = 1000 GeV, m_{X} = 150 GeV, c#tau = 10 cm'] )
    LxyPlot.append( ['outHist_1000_150_10.root', '1000_150_10_h_LLP_Lxy', r.kRed-7, 'm_{H} = 1000 GeV, m_{X} = 150 GeV, c#tau = 1 cm'] )
    plotSelection(LxyPlot, name = 'X_decayLength', log = True, xlabel = 'Gen X decay length (cm)', normed = True)
    """
