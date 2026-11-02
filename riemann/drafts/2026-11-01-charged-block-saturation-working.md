# Charged-block saturation calculation — saved working state

Approved target: the exact TARGET in drafts/literature/2026-11-01-charged-block-density-saturation-test.md. No new literature scope.

Candidate construction for T>=2H0, H0=3.0610046*10^10: L=log T, d=1/L, h=4/L, n=floor(T/h), gamma_j=T+jh (0<=j<=n). Include gamma_j+-id and negatives, common multiplicity one. Not an actual-Xi zero set.

Counting argument to finish canonically: nonempty (H,2H] intersection implies T/2<=H<2T. Then log T<=2 log H and log H<=2 log T. N_mod <=H L/4+1<=H log H. For delta=sigma-1/2<d, H^(-delta/4)>=exp(-1/2)>1/2; for delta>=d the strict count is zero. Thus the exact density leading term alone dominates. Closed unit counts of both members <=L/2+2<=L<=log(v+2) when nonempty; otherwise zero.

Clipped strict intervals are disjoint (h=4d). With r=T-nh in [0,4d), exact measure is (2n+1)d+min(d,r). First interval contributes d, last contributes d+min(d,r), interiors 2d each. Hence >=T/2-d>=T/3 for all stipulated T, and =T/2+O(1/log T). Check all boundary cases and save full proof in L612 before claiming the obstruction. Next action should independently audit this quantitative nonimplication, with a new REVIEW_REQUIRED assessment; no unsupported central creative mechanism is nominated.

Completion: the finite counting and all boundary cases are now written canonically in lemmas/L612-charged-block-density-saturation.md. This scratch state is preserved; use that full proof for subsequent review. Outcome NEGATIVE concerns only the specified count-only implication. Independent audit coverage is nominated as REVIEW_REQUIRED in drafts/literature/2026-11-01-l612-saturation-audit.md.

Audit correction (2026-11-01): the historical exact formula above overcounts by d. The canonical L612 formula is now 2nd+min(d,r), with T=4nd+r and correction min(d,r)-r/2 to T/2. The lower bound T/2-d>=T/3 survives by a two-case argument in r, not by the historical floor-only calculation. Both uniform count constraints passed independent replay. Preserve the preceding scratch statements as superseded evidence, not as a usable exact formula.
