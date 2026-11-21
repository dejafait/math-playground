# Conditional phase-bound audit — working record, step468

Target: the unchanged SPECIALIZE assessment
`drafts/literature/2026-11-05-uniform-moment-phase-bounds-audit.md`.
Main gap is actual-Xi all-degree mixed positivity. This audit addresses
only L787's horizontal/local derivative antecedents, assuming the earlier
source tube majorant, saddle continuation and stated real-saddle data.

Read L786/L787 and the selected step466/467 records. Retrieved the full
relevant Section3 definitions and Lemmas3.4–3.5 proof cases from
Michałowski arXiv:2607.16795v1. No ancillary certificate was replayed.
The earlier coefficient stops have a different scope and remain intact.

Partial reasoning, saved before final arithmetic and proof assembly:

- Put L=log(1+R). Check q<1 explicitly in the general tube formula.
  Horizontal points admit radius 1/20 circles in the (0.3,0.1) tube.
  A rational exponential bound should give sup|L|<1.11e-11 there,
  hence |L''|<8.88e-9<1e-8.
- The complete local disk has |u-u_k|<=1/25. Radius 1/25 circles
  then stay at Re(u)>0.92, |Im(u)|<=0.08, inside the assumed
  (0.35,0.1) tube. Cauchy applied to L, not just R, bounds L''/L'''.
- For B=a+ib, Re(B/(B-3)^2) has numerator
  a(a-3)^2+(a-6)b^2, so a>6 certifies its positive real part
  on both domains directly. The z/u^2 sector must also be checked
  separately on the local disk.
- Elementary bounds B0>300, exp(4/25)<6/5,
  exp(-4/25)>=21/25 and cos(4/25)>=617/625 suffice.
  They give |B-3|>(83/100)B0, |u|>=(24/25)u_k.
  The prospective normalized lower bound is >6.633, and the
  second-derivative upper bound <13.709, hence below 14.185.
- Differentiating the resolvent yields the third derivative term
  192 B(B+3)/(B-3)^3. Its normalization is by 1/H0,
  just as for the second derivative. A bound below 100 has ample room.

Outstanding: verify every scalar inequality, complete both horizontal
regimes and the two disk sectors, and record the conditional proof only
if all required constants close. Do not audit saddle action, Lemmas3.1–3.3,
or a whole-wedge sign theorem in this step. No conclusion is yet imported.

Completion: all listed checks close in
`lemmas/L788-conditional-horizontal-and-local-phase-bounds.md`.
The exact rational certificate is
`scripts/complex-moment-audit/phase-bounds-468.json`; no comparisons
failed. The horizontal floor is (8/5)k/u_k^2; disk-wide normalized
curvature exceeds 6.633, the second derivative is below 13.709 and
the third-derivative ratio is below 51. Earlier tube and full-saddle
inputs remain explicit assumptions. L787's conditional inference and
the main PROOF assembly are unchanged; no whole-wedge sign follows.
