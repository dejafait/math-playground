# Remaining local theta modes: nomination1635, reviewed1636

TARGET: Reproduce Kawano v1's remaining local theta-mode allowance T_modes(p)<=112 sqrt(L) exp(-5r/L^2) on C048c's full sector, with T_modes the normalized finite horizontal n>=2 integral specified in the assessment.
CHECKED: 2026-11-19
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step1636 searched exact manuscript/modes and B_modes terms, the exact title with theta/modes, and a fourth-power theta-tail query; the relevant primary match was Kawano. Scoped local Mellin literature/history/attempt searches found this nomination and prior exclusions, not a matching proved T_modes. Details in 2026-11-19-mellin-higher-local-modes-source-notes-1636.md; no novelty inference.
SOURCE_EVIDENCE: K. Kawano, Preprints.org202611.0383v1, posted4November2026, DOI10.20944/preprints202611.0383.v1, https://www.preprints.org/manuscript/202611.0383/v1 , Section5.2(28)/Lemma5.1(i), AppendixA.2(A3), AppendixB local definitions through B_modes and both real theta-series estimates with their proof sentence, AppendixC domain/local absorption through the other-mode allowance. Essential cases directly read19November2026; extraction in source-notes1636. DLMF7.7.6 coverage reused from source-notes1630/1633 and C048c.
COMPARISON: The source states the desired allowance and a real t>=1 series majorant, but leaves its uniform finite-integral specialization implicit. C048c supplies the matching sector, width, normalization and absorbed curvature. L799's strip holomorphy/normalized-series identity are reusable supporting results; its different rotated-saddle amplitude bound cannot be imported as T_modes.
GAP: Later verify the operational finite absolute contribution, convergence or justified reuse of L799's strip argument, real t>=1 prerequisite, complete series majorization, and uniform coefficient112/exponent5 with exact scalar bounds. No T_modes inequality or new series estimate was derived in this literature turn.
REASON: Essential coverage is available for separate REPRODUCTION. Independent verification is justified because the non-peer-reviewed source prints the allocation without its complete parameter-specific proof; citation alone does not discharge this verification target. The changed ready assessment needs separate next-turn approval before mathematics.
SCOPE: Only the exact finite horizontal n>=2 integral below, with C048c's unchanged parameters, width, full closed sector and branches; includes source-series verification and its absolute Gaussian specialization. No full-path assembly, zero count, inversion or sufficient mixed positivity.

## Operational integral retained unchanged after source comparison

Keep r=|p|, L=log r>=12, Re p>=-r/(4L), w=W_0(2p/pi),
u_0=w/2, d=1/(3L), and all branches and other definitions of C048c.
For real s in [-d,d], let u=u_0+s and propose

    R_modes(u)=sum_(n>=2) [n^4-3n^2/(2pi exp(2u))]
                                  exp(-pi(n^2-1)exp(2u)),
    T_modes(p)=|integral_(-d)^d K(s) R_modes(u_0+s)
                     exp(h_p(u_0+s)-h_p(u_0)) ds|
                                    / |sqrt(pi/A_0)|.

This definition comes from the A3 factor;
the source does not print the symbol T_modes. The local absolute-budget
reading is an applicability inference supported by B_modes and the
separate tail allocations, not an equality explicitly stated by the
author. A later proof must justify this finite contribution, the
series and any integral/sum exchange. Do not silently
replace it by a full-path expression, change width, add the finite-cell
perturbation factor, or assume a signed-integral bound controls a
restricted absolute contribution.

The source lead is exactly112sqrt(L)exp(-5r/L^2), not an allowance
derived in this turn. Source-notes1636 records the inspected primary
series bound, its t>=1 hypothesis, B_modes and the scope comparison.
Reuse C048c(3),(6)-(12),(19), L799's strip convergence and identity(4),
and covered real DLMF7.7.6. L799's final amplitude bound is outside scope.

After separate approval, the bounded mathematical test is to dominate
the absolute integrand on the full finite segment, retain the complex
Gaussian modulus normalization, and verify coefficient112/exponent5
analytically for L>=12. Check r=exp(12), unbounded L, real p, both
angular boundaries and reflection. Establish the real theta parameter
prerequisite before using the series bound; control the infinite sum,
not just its first term. Reuse or write out normal convergence on
compact subsets strictly inside the strip; termwise integration needs
uniform convergence or domination. Extend only a nonnegative real
Gaussian majorant. These are future obligations, not calculations.

Continue if these checks prove the exact allowance uniformly; otherwise
retain the failed inequality and distinguish sufficient-majorant failure
from a violation of T_modes. Neither is a disproof of RH. Matching
Mathlib coverage is unchecked.

The main gap remains L030-L032/C032a actual-Xi all-degree positivity.
This prospective component could contribute to an actual-theta Mellin
remainder. Horizontal tails, full assembly, zero counts, inversion and
a sufficient sign bridge remain independent. Preserve the global
automatic-import stop in ATTEMPTS/2026-11-05-mellin-global-remainder-import-unpaid.md.
No specific new central signed mechanism is justified by the completed
lower-power audit; the absence of a sufficient Mellin-to-sign bridge
blocks a responsible creative nomination from this component alone.

LITERATURE_REASON: At invocation the target had changed from the audited negative n=1 correction to the separate n>=2 sum; its essential series bound, scope and constant were unassessed. Step1636 supplies that coverage. Further discovery is unnecessary for this unchanged target; separate approval of this changed assessment precedes reproduction.
