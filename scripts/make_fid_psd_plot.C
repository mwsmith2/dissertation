// Remake a spectral density FID plot.

// Set global style
gStyle->SetOptStat(0);

// Load data
TFile *pf = TFile("/Users/matthias/Workspace/gm2/studies/nmr-frequency/meas-vs-sim/root/ch2.root");
TH1F *ph = (TH1F *)pf->Get("h_fft");
TCanvas *c1 = TCanvas();

ph->SetTitle("FID Spectral Density");
ph->SetYTitle("amplitude [a.u.]");
ph->SetXTitle("freq [kHz]");

ph->GetXaxis()->SetRangeUser(10, 25)
ph->SetMarkerStyle(8);
ph->SetMarkerSize(0.7);
ph->Draw("pc");

//c1->Print("fig/fid-spectral-density.pdf");
c1->Print("test.pdf");
