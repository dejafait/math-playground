# Compressed Green-lift inference — audit assessment1264

TARGET: Audit Appendix C's compressed Green-lift contraction inference by proving it from its displayed norm and Euler–Lagrange premises or giving an exact rational model with V=R^2, lifted space R^3, one-dimensional trace/profile spaces, positive integration weights, nontrivial trace kernel and a strict contraction failure.
CHECKED: 2026-11-17
DECISION: EXPLORE
SEARCH_EVIDENCE: Discovery1264 searched compression/right-inverse norm terminology and inspected Douglas's primary factorization theorem; exact local2606.29555/Weyl/Volterra and word-bounded CKE/Green-lift checks found no matching source audit. The unrelated full-fiber Green stop was read and distinguished. No novelty or exhaustive absence claim.
SOURCE_EVIDENCE: Freedman2606.29555v1 Section3(1)-(7), Section15.7/Problems15.14-15.15 and full AppendixC multiplier/closure/primitive argument were inspected in discovery1264; Douglas1966 Theorem1 and complete proof pp413-414 supply the norm-sensitive comparison. Precise URLs and reading limitations are in the completed nomination1263 assessment; no source numerical or continuum certificate is imported.
COMPARISON: A contraction on lifted integrands and a right inverse after profile integration do not come with a source-provided norm estimate for that integration/lift. The audit must decide the exact sufficiency inference, with genuine trace-fiber stationarity and positive kernel energy retained; it may not infer actual-theta failure from an abstract model.
GAP: No countermodel, universal compression estimate or actual-theta contraction has been proved in this assessment. The source's full theta geometry, continuum domains, parameter uniformity and RH-facing bridge remain outside the finite test.
REASON: A bounded source-inference audit prevents importing an unverified signed inequality. Finite algebra is necessary here to test the claimed passage from pointwise multiplication and stationary fibers to profile norm domination; reproducing numerical grids or the source certificate is unnecessary.
SCOPE: One REPRODUCTION proof_audit of the displayed generic inference, with the fixed finite dimensions below, or a rigorous norm proof from the same premises. No actual-Xi counterexample, full Volterra closure audit, source-code reconstruction, larger dimension search or proof of M<=P for theta. Newly saved assessment requires separate next-turn approval before research.
LITERATURE_REASON: Discovery1264 encountered this previously unassessed primary argument; future work uses this coverage for the precise finite audit rather than browsing again.

The main gap remains L030-L032/C032a. The proposed signed intermediate
input from Freedman's AppendixC is M<=P on its Green-minimizer image.
It could help its original-Weyl lift, but its connection to the actual
notebook criterion and independent parameter/realization/bridge gaps
remain unproved. The immediate target is the sufficiency inference
supporting that input, not the input itself.

## Sources and exact applicability

Use [Freedman2606.29555v1](https://arxiv.org/html/2606.29555v1),
AppendixC, paragraphs beginning with the lifted multiplier and ending
with completed-domain Green-lift contraction and primitive compatibility.
Its multiplier is kappa=(1-s-u)/(1+s+u). Its integration C and
Green-minimizer lift E are distinct maps. The proposed audit isolates
the displayed general norm argument, not all specialized theta facts.
Use the completed discovery assessment
`2026-11-17-theta-specific-signing-discovery-nomination-1263.md`
for full source-scope notes and limitations.

[Douglas, Proc.AMS17(1966),413-415](https://home.agh.edu.pl/~rudol/Operat/DouglasFactorizationLemma.pdf),
Theorem1, including the reduced factor's norm and all proof cases,
is the comparison. Mere bounded factorization and factorization with
norm at most one require different hypotheses. Check finite matrix
norms directly; do not substitute a damaged OCR formula. The screenshot
and AMS access failures do not block this finite test.

## Fixed finite discriminator — proposed, not calculated

Use real Euclidean spaces V=R^2, H=R^3 and O=X=R. Seek rational
matrices L:V->H, C:H->O and an onto trace R:V->X. Require every
entry of the integration row C to be strictly positive. Choose rational
r_j>=0 and put K=diag((1-r_j)/(1+r_j)), j=1,2,3. Set

    G_plus=C L,   G_minus=C K L,
    Q(v,w)=<G_plus v,G_plus w>-<G_minus v,G_minus w>.

Impose strict positive definiteness of Q on the nonzero space ker R.
For the trace fiber Rv=1, require its unique constrained minimizer
f_1, and verify Q(f_1,h)=0 for every h in ker R. Require
G_plus f_1!=0. Define E:O->H from the lifted constrained minimizer
by

    E y = (y/(G_plus f_1)) L f_1.

The audit must check the multiplier bound, right-inverse and compressed
feature identities in these exact spaces; they are proposed conditions,
not established results in this file. Every map is finite dimensional,
so boundedness, density/closure and continuity are checked directly.
Do not let ker R be zero or drop stationarity/positive kernel energy.

The discriminating signed threshold is Q(f_1,f_1)>=0, equivalently
profile contraction on this one-dimensional minimizer image. A model
must give a strictly negative exact value and the corresponding
||CKE||>1, with all premises verified, to refute this general inference.
A floating approximation, a vanishing denominator or a model failing
one premise is insufficient. No model has been constructed here.

If the inference is proved, every norm and extra condition on C/E
must be explicit, and the actual source must be checked for that extra
condition before any specialization. If a countermodel succeeds,
abandon only the automatic inference and identify which additional
theta-specific identity would be needed. Do not call the actual theta
inequality false or the source wholly refuted. An unsuccessful search
within these dimensions is inconclusive; do not expand the bound in
this step. Record partial reasoning before longer work.

This is an ordinary source-reliability audit using known operator
principles, not a creative actual-theta construction. A justified
creative attempt still needs an independently signed actual-kernel
mechanism. No cross-notebook input is proposed. Full matching and
supporting Mathlib coverage is unchecked; no Lean verification is claimed.
