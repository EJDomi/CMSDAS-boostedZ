#! /usr/bin/env python
#Configuration

from optparse import OptionParser
parser = OptionParser()

parser.add_option('--infileNom', type='string', action='store',
		  dest='infile1',
		  help='Nominal input file')

parser.add_option('--infileUp', type='string', action='store',
		  dest='infile2',
		  help='Hist with up variation')

parser.add_option('--infileDown', type='string', action='store',
		  dest='infile3',
		  help='Hist with down variation')

parser.add_option('--infileBack', type='string', action='store',
		  dest='infile4',
		  help='Background')

parser.add_option('--outfile', type='string', action='store',
		  default='zp3000_plots.root',
		  dest='outfile',
		  help='Output file')


(options, args) = parser.parse_args()
argv = []

from ROOT import*
import CMS_lumi


####Change CMS_lumi variables
CMS_lumi.lumi_13TeV = '1.0 fb^{-1}'
CMS_lumi.writeExtraText = 1
CMS_lumi.extraText = ''
iPos = 11
if( iPos==0 ): CMS_lumi.relPosX = 0.12
outfile = TFile('my_plots.root', 'RECREATE')

####
for filename in ['scaled_hist_zp2000_','scaled_hist_zp3000_']:
	syst = [['jecup','jecdown','JEC'],
		['jerup','jerdown','JER'],
		['btagup','btagdown','Btag']]
	for iii in [0,1,2]:
		infile1 = TFile(filename+'nominal_opt.root')
		infile2 = TFile(filename+syst[iii][0]+'_opt.root')
		infile3 = TFile(filename+syst[iii][1]+'_opt.root')
		infile4 = TFile('scaled_hist_tt_nominal_opt.root')

		#infile1 = TFile(options.infile1)
		#infile2 = TFile(options.infile2)
		#infile3 = TFile(options.infile3)
		#infile4 = TFile(options.infile4)

		gStyle.SetOptStat(0)

		keyn = (('h_mttbar', 'M_{t#bar{t}} (GeV)'),
			('h_ptLep', 'Lepton p_{T} (GeV)'),
			('h_etaLep', 'Lepton #eta'),
			#('h_2DCut', '2D Cut'),
			('h_ptAK4', 'AK4 jet p_{T} (GeV)'),
			('h_etaAK4', 'AK4 jet #eta'),
			('h_mAK4', 'AK4 jet M (GeV)'),
			('h_bdiscAK4', 'AK4 jet b discriminator'),
			('h_ptAK8', 'AK8 jet p_{T} (GeV)'),
			('h_etaAK8', 'AK8 jet #eta'),
			('h_mAK8', 'AK8 jet M (GeV)'),
			('h_minmassAK8', 'AK8 jet M_{min} (GeV)'),
			('h_nsjAK8', 'AK8 n subjets'))

		j = 0
		for j in range(0, 11):   
		    hist1 = infile1.Get(keyn[j][0])
		    hist2 = infile2.Get(keyn[j][0])
		    hist3 = infile3.Get(keyn[j][0])
		    hist1.Rebin(2)
		    hist2.Rebin(2)
		    hist3.Rebin(2)
		    
		    if(keyn[j][0]=='h_mttbar'):
			    hist4 = infile4.Get(keyn[j][0])			
			    hist4.Rebin(4)
			    hist1.Rebin(2)
			    hist2.Rebin(2)
			    hist3.Rebin(2)
		    hist2.Divide(hist1)
		    hist3.Divide(hist1)
		    hist1.Divide(hist1)

		    #hist2.GetYaxis().SetRangeUser(0.001,3.5)

		    c1 = TCanvas()
		    c1.SetLeftMargin(0.2)
		    c1.SetBottomMargin(0.2)


		    hist1.GetXaxis().SetTitle(keyn[j][1])
		    hist1.GetXaxis().SetLabelSize(0.04)
		    hist1.GetXaxis().SetTitleSize(0.06)
		    hist1.GetXaxis().SetTitleOffset(1.0)
		    hist2.GetYaxis().SetTitle('Events')
		    hist2.GetYaxis().SetLabelSize(0.04)
		    hist2.GetYaxis().SetTitleSize(0.06) 
		    hist2.GetYaxis().SetTitleOffset(0.8)

		    if(keyn[j][0]=='h_mttbar'):
			    hist4.SetLineColor(3)
			    hist2.SetLineColor(kRed)
			    hist4.Draw()
			    hist2.Draw('SAME')
		    else:
			    hist2.SetLineColor(kRed)
			    hist2.Draw()
		    hist3.SetLineColor(kBlue)
		    hist3.Draw('SAME')
		    hist1.SetLineColor(kBlack)
		    hist1.Draw('SAME')
		    
		#############################################

		    leg = TLegend(0.6, 0.6, 0.89, 0.89)
		    leg.SetFillColor(kWhite)
		    leg.AddEntry(hist1,'Nominal','l')
		    leg.AddEntry(hist2,syst[iii][2]+'Up Variation', 'l')
		    leg.AddEntry(hist3,syst[iii][2]+'Down Variation', 'l')
		    if(keyn[j][0]=='h_mttbar'):leg.AddEntry(hist4,'Background','l')
		    leg.SetLineColor(kWhite)
		    if(filename=='scaled_hist_zp2000_'):
			    leg.SetHeader('Zprime#rightarrow ttbar (2TeV)')
		    else:
			    leg.SetHeader('Zprime#rightarrow ttbar (3TeV)')
		    leg.Draw()

		    CMS_lumi.CMS_lumi(c1, 4, iPos)

		    c1.cd()
		    c1.Update()
		    
		    c1.SaveAs(filename+syst[iii][2]+keyn[j][0]+'_dist.png')
		    c1.Write(filename+syst[iii][2]+keyn[j][0]+'_dist')
		############################################
outfile.Close()
