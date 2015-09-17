# Dissertation

My disseration will be on the g-2 Field Shimming and initial Field Measurement.

## Tentative Outline

* Physics Introduction [~10 pages]
  - historical background (3-5 pages)
  - motivation from theoretical standpoint (2-3 pages)
  - g-2 working principles (2-3 pages)
* Field Measurement [~10 pages
  - nmr probes (3-5 pages)
  - shimming field (3-5 pages)
  - coupling of field to muons (2-3 pages)
* FID Analysis [~10 pages]
  - Bloch equations (1-2 pages)
  - frequency extraction (3-5 pages)
  - gradients (3-5 pages)
* Field Perturbation Measurements [~5 pages]
  - design principle (2-3 pages)
  - results (1-2 pages)
* Muon Tracking Simulation [~10 pages]
  - interpolating the field (1-2 pages)
  - polar multipoles (2-4 pages)
  - azimuthal closed orbit distortions (2-4 pages)
  - constraints on field (3-5 pages)
* Field Shimming [~12 pages]
  - raw results (2-4 pages)
  - analysis chain (3-5 pages)
  - final results (2-4 pages)
  - resulting errors (1-2 pages)
* Appendices
  - fid-analysis code design
  - gm2-nmr-daq


## Work Roadmap

* Field shimming[3-4 months]
  - collect data
  - analyze
  - iterate shim positions
  - repeat
* NMR-DAQ [ongoing]
  - polish and maintenance
  - add midas-to-art layer for data
  - flesh out online displays
* Full tracking study [4-6 weeks]
  - choose a framework
  - think about validating with simple model (julia, whatever)
  - investigate effects of
    * different field interpolations
    * individual multi-poles
    * realistic muon distributions
    * realistic data from e821/shimming runs
    * closed orbit distortions
* Errors from 2d multi-pole approximation [2-4 weeks]
  - piggyback on the work Martin started
  - figure out worst cases
* Continue study of the effect of field gradients[1-2 weeks]
  - effect on frequency extraction
  - extract information about gradient

## Potential Studies

* Simulation of trolley perturbations
  - map field induced on trolley
  - apply gradients to simulated FIDs
  - extract error
* Time dependent field changes
  - model small changes present at beginning of fill
  - extract error, muon losses
* Simulate other field perturbations
  - SiPMs, other hardware in proper position
  - extract effect on field