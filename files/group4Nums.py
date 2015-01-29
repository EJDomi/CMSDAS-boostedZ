from ROOT import*

print '\t| nominal | jecup | jecdown | jerup | jerdown | btagup | btagdown'
#for type in ('tt','zp2000','zp3000'):
type = 'zp3000'
nom1 = TFile('scaled_hist_' + type + '_nominal.root')
jecup1 = TFile('scaled_hist_' + type + '_jecup.root')
jecdown1 = TFile('scaled_hist_'  + type + '_jecdown.root')
jerup1 = TFile('scaled_hist_'  + type + '_jerup.root')
jerdown1 = TFile('scaled_hist_'  + type + '_jerdown.root')
btagup1 = TFile('scaled_hist_'  + type + '_btagup.root')
btagdown1 = TFile('scaled_hist_'  + type + '_btagdown.root')

nom2 = nom1.Get('h_mttbar')
jecup2 = jecup1.Get('h_mttbar') 
jecdown2 = jecdown1.Get('h_mttbar')
jerup2 = jerup1.Get('h_mttbar')
jerdown2 = jerdown1.Get('h_mttbar')
btagup2 = btagup1.Get('h_mttbar')
btagdown2 = btagdown1.Get('h_mttbar')

print type+'bin1','\t',nom2.Integral(1,84),jecup2.Integral(1,84),jecdown2.Integral(1,84),jerup2.Integral(1,84),jerdown2.Integral(1,84),btagup2.Integral(1,84),btagdown2.Integral(1,84)
print type+'bin2','\t',nom2.Integral(85,200),jecup2.Integral(85,200),jecdown2.Integral(85,200),jerup2.Integral(85,200),jerdown2.Integral(85,200),btagup2.Integral(85,200),btagdown2.Integral(85,200)

