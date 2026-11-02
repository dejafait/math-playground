# Approved weighted-annulus attempt — working checkpoint

Target: the exact covered W_T=o(N^2) target in the saved
2026-11-01-vertical-pick-density-weighted-annulus assessment (SPECIALIZE).
Only that target is being attempted. L641/L642 and both recorded
boundary-transfer/constrained-trace failures have been read. Existing
unfinished files are preserved. No source refresh or new mechanism is
being approved here.

Main gap: actual-Xi initial signs/all-degree mixed positivity; locally,
the constrained signed near-annulus trace. Intermediate use: a small
nonnegative E_N mean may support subsequent simultaneous count/trace
height selection, still separate from eigenvalue signs and RH.

Candidate estimates, still undergoing proof checks:

* Write L_N(x,y)=log|B_N(x-iy)| for y>=0, |x|>=1. Differentiate
  the exact distinct-pole logarithm in y before taking its grid mean.
  The continuum integral is at most 2 arctan(4/7)<21/20;
  monotone Riemann-sum error should be at most 2y. Thus
  L_N<=(21/20)Ny+2y. Spatial decay is separately needed.
* The half-plane conjugation Cf=B_N overline(f(bar z)) preserves
  H_N and commutes with real-symbol concentration. If justified,
  E_N is invariant and F_N=exp(L_N) k_E(x+iy,x+iy).
* Poisson contraction and the boundary leakage suggest the exterior
  upper diagonal integral is O(sqrt(N)+Ny log(e/y)). The interval
  edge loss must be retained, including y=0 separately.
* Try delta=(log N)/(4N), theta=11/20. The core would cost
  O(N^(141/80)); larger displacements, banded in widths 1/N using
  the strict primary density theorem with a lower threshold, would
  cost O(N^(2-1/80)). Constants and endpoint multiplicities are
  not yet certified. No W_T result is claimed in this checkpoint.

Continue only after the conjugation, product discretization, Poisson
edge integral, padded finite zero sum and band endpoints are proved.
Otherwise retain the exact failed inequality and park this certificate.
The primary density statement is imported from Baluyot's 2017 thesis,
Theorem 1.2.1 p.16, with its saved assessed qualifications. No weighted
Maples--Rodgers theorem or new density theorem is being used.

Completed: the estimates above are proved locally in canonical L643,
including conjugation invariance, spatial integrability, Poisson edges,
the y=0 atom, positive-height padding, strict density cutoffs and all
multiplicities. W_T=O(N^(159/80)) follows. The earlier checkpoint
is preserved; its tentative status is superseded by that canonical
proof, which remains independently unaudited. The next nomination is
a conceptual audit with unchanged source coverage, for separate
supervisor approval. Simultaneous count/trace selection and signs
remain open. No additional mathematical target was attempted.
