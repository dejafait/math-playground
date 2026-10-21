# Changed-H t=0 full-system test — saved reasoning

Approved target: determine whether the redistributed-H t=0 affine cyclic
root satisfies every constraint of L051 (1)–(4). Prior SPECIALIZE coverage:
`drafts/literature/2026-10-18-redistributed-h-t0-real-feasibility.md`.
Main gap remains universal eventual descent. This tests one full-real-system
survivor; a strict failed necessary guard suffices and gives no wider verdict.

Use L055's literal table with only H_0=39 and H_24=32670622 changed,
a_i=2 for i<24 and a_24=166504412. Essential inputs are L051, L055's
factored-root/analytic method, and L079's changed table/positive Lambda.
L078 matches the normalized unshifted root; L080/C080b provide arithmetic
and actual-word context only. The ready source review records known-result,
duplicate and Attempts 026–031 comparisons; none supplies this verdict.

Planned discriminating check: freshly show c_0>10^8 and c_i>2 for
1<=i<24. With kappa=23/11, C_i=product_(j<i)c_j and
R=sum eta_i/C_i, deduce R<kappa(1+2/10^8)=R_+. For the exact cyclic
root n_0=R/(exp(Lambda)-1), every i<=24 has
s_i/C_i=n_0+sum_(j<i)eta_j/C_j+kappa/C_i
<R_+/lambda_-+R_++kappa<20*10^9<exp(24).
Therefore h_18<24+log C_18. Certify the resulting upper bound on
h_18+J_18 log(27/16)-H_18 log2 using changed prefix exponents.
A negative bound rejects the root; an interval touching zero gives no
verdict. No other allocation or t=1 calculation is authorized here.

Completed verdict: the root fails the own-input H guard at row18.
The full proof is canonical in L081; the exact upper margin is
-457745289/50000000000<0, against the requirement >0. The script
`scripts/postspell-word-count/certify_redistributed_h_t0_real_feasibility.py`
wrote the complete same-stem certificate and passed all 150 certification
checks. No other guard verdict, t=1 test or wider search is asserted.
The proposed critical-audit continuation has REVIEW_REQUIRED coverage;
independent audit remains unresolved.
