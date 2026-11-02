# Unit-length Hardy closure: calculation checkpoint

Approved target: Test the appended unit-length quintic Hermite closure of f_H against all L473 second/fourth tolerances, including wrap-around phases.

Inputs read: L473 hypotheses and (1)--(2),(6),(9)--(10), plus L581's fixed-divisor endpoint interface. The supplied SPECIALIZE assessment covers the exact target. No further source review is needed. Preserve the exact-law stop in L581; this is a changed marginal.

Set ell=log H, L=H ell, P=L+1. Retain f(s)=Z(H+s/ell) on [0,L] and append the unique quintic matching the value and first two s derivatives at L to those at 0. Fixed-order bounds through order two give endpoint/neighborhood jet size O(H^(1/6)); the fixed polynomial bridge has the same bound for all three coordinates.

Pending full write-up: verify the six basis endpoint conditions, C2 periodic joining and uniform-phase stationarity. For any degree d=2 or 4 paired monomial, the periodic and reference integrands agree on [0,L-1]. Only the final Hardy strip and the unit bridge differ, with wrap-around into [0,1]. The generic comparison should be bounded by (3 A^d H^(d/6)+|M_ref|)/P. L473 bounds |M_ref| by O(ell) for degree two and O(ell^4) for degree four. Tight same-height (0,1) and (1,2) entries must instead be evaluated exactly by periodic total derivatives. No lemma or success claim is made at this checkpoint.

Independent gaps: hard ell^2 paired support, positive clipped mass, rare/bulk replacement and actual-Xi transfer. A successful comparison supplies none of these automatically. Full evidence will be canonical in L582 if all checks pass.

Completed: all checks pass in the written specialization; the full proof and precise imported-source qualifications are canonical in `lemmas/L582-unit-hermite-hardy-periodic-moment-closure.md`. No mathematical script was needed. This preserves the pre-completion reasoning; L582 still awaits its separate critical application audit.
