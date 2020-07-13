import ROOT as r
from ROOT import gROOT
import optparse
import math

class Histo:

    def __init__(self, variables, key, xlabel, bins, color):

        self.variables = variables
        self.key = key

        self.histo = r.TH1F(key, '', bins[0], bins[1], bins[2])
        self.histo.GetXaxis().SetTitle(xlabel)
        self.histo.SetLineColor(color)
        self.histo.SetLineWidth(2)
        


if __name__=='__main__':


    #########################
    ###   Parser object   ###   
    #########################
    parser = optparse.OptionParser(usage='usage: %prog [opts] FilenameWithSamples', version='%prog 1.0')
    parser.add_option('-i', '--input', action='store', type=str, dest='inputFile', default='launchWithGridui/merged.root', help='the input file. default \'merged.root\'')
    parser.add_option('-t', '--tag', action='store', type=str, dest='tag', default='launchWithGridui/merged.root', help='the input file. default \'merged.root\'')
    (opts, args) = parser.parse_args()

    ############# Set the TDR plot style
    gROOT.ProcessLine('.L ' +'include/tdrstyle.C')
    gROOT.SetBatch(1)
    r.setTDRStyle()


    #################################
    ###   Get the file and tree   ###   
    #################################
    inputFiles = opts.inputFile.split(',')

    _tree = r.TChain("Events")
    for _f in inputFiles:
        _tree.Add(_f)

    #_input = r.TFile(opts.inputFile)
    #_tree = _input.Get('Events')


    #################################
    ###   Initialize histograms   ###   
    #################################
    Lxy_bins = [40, 0, 200]
    dxy_bins = [100, -280, 280]
    pt_bins = [100, 0, 500]
    phi_bins = [100, -math.pi, math.pi]
    eta_bins = [100, -3, 3]
    vx_bins = [100, -900, 900]
    vy_bins = [100, 0, 900]
    vz_bins = [100, -2000, 2000]
    py_bins = [100, -500, 0]
    pxz_bins = [100, -300, 300]
    q_bins = [5, -2.5, 2.5]

    histos = {}
    histos['h_genMu_pt'] = Histo(['genMu_pt'], opts.tag + '_h_genMu_pt', 'Generated muon p_{T} (GeV)', pt_bins, r.kBlack) 
    histos['h_genMu_phi'] = Histo(['genMu_phi'], opts.tag + '_h_genMu_phi', 'Generated muon #phi', phi_bins, r.kBlack) 
    histos['h_genMu_eta'] = Histo(['genMu_eta'], opts.tag + '_h_genMu_eta', 'Generated muon #eta', eta_bins, r.kBlack) 
    histos['h_genMu_dxy'] = Histo(['genMu_dxy'], opts.tag + '_h_genMu_dxy', 'Generated muon d_{xy} (cm)', dxy_bins, r.kBlack) 
    histos['h_genMu_vx'] = Histo(['genMu_vx'], opts.tag + '_h_genMu_vx', 'Status 1 muon v_{x} (cm)', vx_bins, r.kBlack) 
    histos['h_genMu_vy'] = Histo(['genMu_vy'], opts.tag + '_h_genMu_vy', 'Status 1 muon v_{y} (cm)', vy_bins, r.kBlack) 
    histos['h_genMu_vz'] = Histo(['genMu_vz'], opts.tag + '_h_genMu_vz', 'Status 1 muon v_{z} (cm)', vz_bins, r.kBlack) 
    histos['h_genMu_px'] = Histo(['genMu_px'], opts.tag + '_h_genMu_px', 'Generated muon p_{x} (GeV)', pxz_bins, r.kBlack) 
    histos['h_genMu_pz'] = Histo(['genMu_pz'], opts.tag + '_h_genMu_pz', 'Generated muon p_{z} (GeV)', pxz_bins, r.kBlack) 
    histos['h_genMu_py'] = Histo(['genMu_py'], opts.tag + '_h_genMu_py', 'Generated muon p_{y} (GeV)', py_bins, r.kBlack) 
    histos['h_genMu_q'] = Histo(['genMu_q'], opts.tag + '_h_genMu_q', 'Generated muon q', q_bins, r.kBlack) 


    histos['h_nDG'] = Histo(['nDG'], opts.tag + '_h_nDG', 'Number of DG muons', [4, 0, 4], r.kBlack) 
    histos['h_DG_pt'] = Histo(['DG_pt'], opts.tag + '_h_DG_pt', 'DG muon p_{T} (GeV)', pt_bins, r.kBlack) 
    histos['h_DG_phi'] = Histo(['DG_phi'], opts.tag + '_h_DG_phi', 'DG muon #phi', phi_bins, r.kBlack) 
    histos['h_DG_eta'] = Histo(['DG_eta'], opts.tag + '_h_DG_eta', 'DG muon #eta', eta_bins, r.kBlack) 
    histos['h_DG_dxy'] = Histo(['DG_dxy'], opts.tag + '_h_DG_dxy', 'DG muon d_{xy} (cm)', [100, -100, 100], r.kBlack) 
    histos['h_DG_dxyError'] = Histo(['DG_dxyError'], opts.tag + '_h_DG_dxyError', 'DG muon #sigma_{d} (cm)', [80, 0, 0.2], r.kBlack) 
    histos['h_DG_Ixy'] = Histo(['DG_Ixy'], opts.tag + '_h_DG_Ixy', 'DG muon |d_{xy}|/#sigma_{d}', [80, 0, 15000], r.kBlack) 
    histos['h_DG_normChi2'] = Histo(['DG_chi2/DG_ndof'], opts.tag + '_h_DG_normChi2', 'DG muon #chi^{2}/ndof', [45, 0, 15], r.kBlack) 
    histos['h_DG_numberOfValidHits'] = Histo(['DG_numberOfValidHits'], opts.tag + '_h_DG_numberOfValidHits', 'DG muon N_{hits}', [40, 0, 80], r.kBlack) 
    histos['h_DG_q'] = Histo(['DG_q'], opts.tag + '_h_DG_q', 'DG muon q', q_bins, r.kBlack) 
    histos['h_DG_vx'] = Histo(['DG_vx'], opts.tag + '_h_DG_vx', 'DG muon v_{x} (cm)', [100, -40,40], r.kBlack) 
    histos['h_DG_vy'] = Histo(['DG_vy'], opts.tag + '_h_DG_vy', 'DG muon v_{y} (cm)', [100, -40, 40], r.kBlack) 
    histos['h_DG_vz'] = Histo(['DG_vz'], opts.tag + '_h_DG_vz', 'DG muon v_{z} (cm)', [100, -200, 200], r.kBlack) 
 
    ################################
    ###   Loop over the events   ###   
    ################################
    """
    for _e, event in enumerate(_tree):

       for hname in histos.keys():
           for var in histos[hname].variables:
               value = eval('event.'+var)
               histos[hname].histo.Fill(value)
    """

    for hname in histos.keys():
        _tree.Project(histos[hname].key, histos[hname].variables[0], '', '')


    ###########################
    ###   Save histograms   ###   
    ###########################
    _out = r.TFile('outHist_'+opts.tag + '.root', 'RECREATE')
    _out.cd()

    for hname in histos.keys():
        histos[hname].histo.Write()

    _out.Close()
    #_input.Close()


