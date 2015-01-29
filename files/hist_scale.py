#! /usr/bin/env python

#Configuration

from optparse import OptionParser
parser = OptionParser()

parser.add_option('--infile', type='string', action='store',
		  dest='infile',
		  help='Input root histograms')

parser.add_option('--outfile', type='string', action='store',
		  default='scaled_hist_',
		  dest='outfile',
		  help='Name of output file')

parser.add_option('--verbose', action='store_true',
		  default=False,
		  dest='verbose',
		  help='Print debugging info')

parser.add_option('--totalevents', type='float', action='store',
		  default=20000.0,
		  dest='N_tot',
		  help='Initial number of MC events')

parser.add_option('--sigma', type='float', action='store',
		  default=1,
		  dest='sigma',
		  help='Cross section')

parser.add_option('--lumi', type='float', action='store',
		  default=1000,
		  dest='lumi',
		  help='Luminosity')

parser.add_option('--sf', type='float', action='store',
		  default=1.0,
		  dest='SF',
		  help='Scale Factor')

(options, args) = parser.parse_args()
argv = []

from ROOT import*

infile = TFile(options.infile)
#outfile = TFile(options.outfile + options.infile, 'recreate')
outfile = TFile(options.outfile, 'RECREATE')                              
outfile.cd()

scale = options.lumi * options.sigma * options.SF / options.N_tot


for key in infile.GetListOfKeys():
    hist = key.ReadObj()
    hist.Scale(scale)
    if ( hist.GetName() == 'h_mttbar'):
	print infile.GetName(), 'bin1', hist.Integral(1,84)
	print infile.GetName(), 'bin2', hist.Integral(85,200)
    outfile.cd()
    hist.Write()
outfile.cd()
outfile.Write()
outfile.Close()
