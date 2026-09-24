# Dyadic mass variation checkpoint — 2026-09-13

Existing L165 step is complete and preserved. Current audit concerns replacing
W by its dyadic average against χ''(Q/M), with fixed M.

Write v=log(t/T), x_j=n_j/N. Every six-amplitude product equals its
value at T times exp(v L−3v²/2), where L=sum_j log x_j lies in
[0,6 log 2]. Thus W(Te^v)/W(T) is exp(−3v²/2) times the
moment generating function of a probability measure on that fixed compact
interval. Candidate rigorous obstruction: these profiles have a uniform
positive L1 distance from constants on u∈[1,2]. Otherwise compactness of
probability measures gives a limiting profile constant on an interval;
analytic continuation would force a compactly supported moment generating
function to equal exp(3v²/2), impossible by its growth at positive infinity.

Resume by proving this compactness argument and converting it to the
absolute covariance bound. This does NOT show the actual χ'' correlation
fails to vanish; it shows amplitude flattening cannot justify it.

Completed as L166. The compactness argument is proved using bounded
moments and locally uniform entire-series convergence. It gives a uniform
positive L1 distance from constants and rules out amplitude flattening.
The actual cutoff covariance remains unproved; its required normalized
rate is o((log T)^(-4)).
