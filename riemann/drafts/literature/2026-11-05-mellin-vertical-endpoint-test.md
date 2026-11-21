# Standalone vertical theta-Mellin endpoint: research nomination

TARGET: Attempt the standalone vertical theta-Mellin endpoint bound |V(s,y_L)|/|4pi^2 exp(S_s(x))C|<=exp(-Q/2) on all D, using fixed-height meromorphic continuation and treating h=0.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse step534's completed exact-target, Taylor-subtraction and Cauchy/endpoint searches and narrow duplicate/failure comparison in 2026-11-05-mellin-vertical-endpoint-scope.md; no novelty inference.
SOURCE_EVIDENCE: Zagier, Mellin appendix to Zeidler (Springer 2006), Section1, author PDF pp1–2, subtraction case after (2), https://people.mpim-bonn.mpg.de/zagier/files/tex/MellinTransform/fulltext.pdf; DLMF v1.2.8, https://dlmf.nist.gov/2.5#ii (2.5.17–25), https://dlmf.nist.gov/1.9#iii (1.9.30–31), https://dlmf.nist.gov/1.9#vi (1.9.48), https://dlmf.nist.gov/1.10#viii (1.10.18–19/M-test); paper23 v1 Section3 Lemma2 (10)–(14), https://rstation.ai/problems/riemann_hypothesis/papers/23; post20 endpoint paragraphs/07:10:31 UTC revision, https://rstation.ai/r/riemann_hypothesis/posts/20. Detailed inspected hypotheses and general Gaussian-sum coverage remain in the completed scope assessment.
COMPARISON: Standard continuation and holomorphic-kernel methods cover part of the target. The exact uniform bound is an author source claim whose u>3 longer-diameter specialization is unverified. Independent verification is needed for changed height, full kernel, phase payment, poles and h=0; neither the source circle constant nor global contour estimate is a premise.
GAP: Establish fixed-height continuation with correct orientation, pole qualifications and compatibility, then the normalized bound for the actual y_L on all D; alternatively give a rigorous obstruction to the sufficient method without claiming a counterexample to RH.
REASON: The sources are accessible and methods are adequately covered for a bounded component attempt independent of unread supplements. A citation alone does not settle its parameter-specific hypotheses or exact allowance.
SCOPE: Separate literature approval completed in step535 with direct primary URLs repaired; target and hypotheses unchanged. No mathematical specialization or endpoint estimate was derived in steps534–535. A future attempt is REPRODUCTION and established-route development, not creative sign work.

## Separate source-gate repair — step535

LITERATURE_REASON: Supervisor recovery reports that the ready assessment lacks a direct source URL; repair that citation defect for the unchanged target, reusing step534 rather than reopening its search or deriving mathematics.

Reopened the linked author PDF, Section1 pp1–2, and DLMF2.5(ii),
1.9(iii), 1.10(viii). The subtraction identity after Zagier's (2)
assumes a power asymptotic expansion at zero and rapid decay at infinity;
its finite-interval component is the relevant method, not an assertion
of imaginary-ray decay. DLMF2.5.17 requires increasing real exponent
parts tending to infinity; 2.5.25 identifies the truncated transform's
principal parts. DLMF1.9.30–31 requires continuity within and on a
simple closed contour and analyticity inside it. DLMF1.10.18–19 and
the integral M-test require joint continuity, parameter analyticity
and, for singular endpoints, uniform convergence on compact parameter
sets. These conditions still need verification in the proposed application.

The paper23 and post20 landing pages were accessible again; their
previously inspected endpoint cases and comparison are reused from
`2026-11-05-mellin-vertical-endpoint-scope.md`, not re-proved here.
Derivation87 remains unread and is not a premise. No source supplies
the exact actual-height allowance by automatic import. The existing
duplicate/failure comparison and global-import stop remain applicable.
The SPECIALIZE decision approves a bounded method specialization only.
This is a process repair with no new mathematical evidence (STALLED),
not a new source discovery or renewed mathematical exploration budget.

Use L797's saddle/domain, L798's phase and principal branches, L799's
complete normally convergent series P, and L802's left-endpoint height:

    D={s: |s|>=6000, Re(s)>=-|s|/(8 log|s|)},
    F(x)=x(pi exp(2x)-9/4)=s, x=u+ih,
    Q=pi exp(2u), d=3/(16u), A=2F'(x)/x,
    a=exp(-i Arg A/2), z_L=x-da=v_L+i y_L,
    S_s(z)=2s Log z+(9/2)z-pi exp(2z), C=sqrt(2pi/A).

For each independent fixed real y with 0<|y|<pi/4, start with

    V(s,y)=integral_[0,i y] exp(2s Log z)P(z) dz,
    Re(s)>-1/2,

on the oriented straight segment. Outside that half-plane V means
meromorphic continuation in s at fixed y, whose legitimacy is part of
the attempt. Only then evaluate at y=y_L(s). Define V(s,0)=0 for
the actual h=0 case. Do not assert analyticity of the moving-height
composite or an ordinary improper integral outside its convergence
half-plane. Retain the exact denominator |4pi^2 exp(S_s(x))C| and
target exp(-Q/2), without an upper cutoff on u.

The single bounded attempt must discharge these connected obligations:

1. Apply the standard subtraction theorem to the fixed oriented ray,
   including the exponent change and principal-power factor. State
   possible versus actual poles and compatibility of subtraction
   orders; show evaluations needed on D are legitimate. Do not use
   evenness to cancel terms without a justified input. A compact-circle
   identity may be independently verified as in post20, but its
   denominator's apparent singularities require separate treatment.
2. Supply effective complete-series control on every chosen circle
   strictly inside the theta strip. Use the inspected Cauchy/compact
   integral and Gaussian-sum methods with their hypotheses. Do not
   assume the source's 400 cos(2H)^(-5/2) bound, L799's local eta on
   other circles, or the endpoint allowance itself.
3. Pay the normalized phase and all prefactors at the actual y_L,
   addressing convergent small-height and continued-height regimes.
   The old u>=6/h=.7 argument and u>=3/d=1/(8u) assertion are method
   guides, not proofs for d=3/(16u). Cover both signs of h, both closed
   boundaries of D and the actual h=0 regime, including compatibility
   as h tends to zero along D. No all-s compatibility at y=0 is assumed.

The continuation test is a full uniform proof of this endpoint bound
or an informative rigorous obstruction to the chosen sufficient
method. A failed absolute majorant does not refute the bound or RH;
preserve it and require materially new input before retrying. Save
unfinished reasoning before lengthy work. No numerical script is
required and finite samples are not proof.

Essential local IDs: L797, L798, L799, L802. L803 and L800/L801 are
downstream assembly context only. The global-import stop remains in
force; no unread derivation or cross-notebook input is a premise.
Success could supply one component of separately assessed Mellin
assembly. Global contour equality/budget, quotient/inversion,
certificates and a sufficient actual-Xi sign implication remain open.
Full matching Mathlib coverage is unchecked; no RH candidate is claimed.
