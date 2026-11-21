# Width Newton specialization1825

Approved target and unchanged SPECIALIZE assessment1823: rational inverse
roots on[1,2^30], error<=2^-60 and at most100 defined operations.
Main RH gap remains L030-L032/C032a; downstream use is possible C033z
slack for separately reviewed rounding, with conditioning/TV/realization open.

Working construction: normalize a=w,h=1 by at most15 divisions a/=4,h/=2,
testing a>1. Then a in(1/4,1],h<=1 and w=a/h^2. Eight Newton steps
x=x*(3-a*x*x)/2 from x=1, then q=h*x and the existing panel clamps.
Provisional full cost94, counting small-constant formation, input lower check,
16 normalization comparisons,30 divisions,40 Newton operations, rescaling
and two clamp comparisons. No bit-cost/runtime claim.

Use Brent-Zimmermann v0.5.9 Lemma3.14, p112, not its integer algorithm.
First-step relative error<=5/16 by monotonicity of(3*r-r^3)/2 for
r=sqrt(a) in[1/2,1]. For later steps the cited theorem bounds
e_next<=(24/11)e^2; hence e8<=(11/24)*(15/22)^128<2^-65.
Check induction, endpoints and complete ledger before accepting. The
input perturbation remains2^-123; total should preserve original(17).
This was the saved pre-verification specialization, not an approval record.

## Completion

The full proof, endpoint/interface justification and94-operation ledger
are canonical in C033z, extension1825. Exact checks pass in
`scripts/smoothed-law/width_newton_1825.json`; the continuum proof is the
written invariant/induction, not the finite samples. The first provisional
verbal count95 was conservative; the explicit ledger sums to94. No
full-evaluator cost or runtime theorem is inferred. Independent audit is
the next target, with a separate literature-gate approval still required.
