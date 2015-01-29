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
CMS_lumi.extraText = 'Preliminary'

iPos = 11
if( iPos==0 ): CMS_lumi.relPosX = 0.12

H_ref = 600; 
W_ref = 800; 
W = W_ref
H  = H_ref


####

infile1 = TFile(options.infile1)
infile2 = TFile(options.infile2)
#infile3 = TFile(options.infile3)
#outfile = TFile(options.outfile, 'RECREATE')

gStyle.SetOptStat(0)

# references for T, B, L, R
T = 0.08*H_ref
B = 0.12*H_ref 
L = 0.12*W_ref
R = 0.04*W_ref

#for key in infile1.GetListOfKeys():
#	keyn = key.GetName()

keyn = (('h_mttbar', 'M_{t#bar{t}} (GeV)'),( 'h_ptLep', 'Lepton p_{T} (GeV)'),('h_etaLep', 'Lepton #eta'),('h_2DCut', '2D Cut'),('h_ptAK4', 'AK4 jet p_{T} (GeV)'),('h_etaAK4', 'AK4 jet #eta'),('h_mAK4', 'AK4 jet M (GeV)'),('h_bdiscAK4', 'AK4 jet b discriminator'),('h_ptAK8', 'AK8 jet p_{T} (GeV)'),('h_etaAK8', 'AK8 jet #eta'),('h_mAK8', 'AK8 jet M (GeV)'),('h_minmassAK8', 'AK8 jet M_{min} (GeV)'),('h_nsjAK8', 'AK8 n subjets'))

j = 3
#for j in range(0, 12):   

hist1 = infile1.Get(keyn[j][0])
hist2 = infile2.Get(keyn[j][0])
#hist3 = infile3.Get(keyn[j][0])
#hist1.Rebin(4)
#hist2.Rebin(4)
#hist3.Rebin(4)

#hist2.Divide(hist1)
#hist3.Divide(hist1)
#hist1.Divide(hist1)

hist1.GetXaxis().SetRangeUser(0,1.0)
hist2.GetXaxis().SetRangeUser(0,1.0)
c1 = TCanvas()
c1.SetLeftMargin(0.2)
c1.SetBottomMargin(0.2)


hist2.GetXaxis().SetTitle('#Delta R')
hist2.GetXaxis().SetLabelSize(0.04)
hist2.GetXaxis().SetTitleSize(0.06)
hist2.GetXaxis().SetTitleOffset(1.0)
hist2.GetYaxis().SetTitle('p_{T}^{rel} (GeV)')
hist2.GetYaxis().SetLabelSize(0.04)
hist2.GetYaxis().SetTitleSize(0.06) 
hist2.GetYaxis().SetTitleOffset(0.8)

hist1.SetMarkerStyle(24)
hist2.SetMarkerStyle(24)
hist2.SetMarkerColor(kRed)
hist2.Draw()
#hist3.SetLineColor(kBlue)
#hist3.Draw('SAME')
hist1.SetMarkerColor(kBlue)
hist1.Draw('SAME')

#############################################

leg = TLegend(0.7, 0.7, 0.89, 0.89)
leg.SetFillColor(kWhite)
leg.AddEntry(hist1,'Z prime 2 TeV','P')
leg.AddEntry(hist2,'Z prime 3 TeV ', 'P')
#leg.AddEntry(hist3,'Down Variation', 'l')
#leg.SetLineColor(kWhite)
#leg.SetHeader('Legend')
leg.Draw()

CMS_lumi.CMS_lumi(c1, 4, iPos)

c1.cd()
c1.Update()

#c1.SaveAs(keyn[0][0]+'.png')
#c1.Write()
############################################
