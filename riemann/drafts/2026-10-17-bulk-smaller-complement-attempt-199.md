# Step 199 — smaller full-complement core/tail attempt (completed)

The ready target is exactly the step-195 SPECIALIZE target. The main RH
gap is unchanged. The intermediate target is a negative lower core and
a smaller certified upper bound on its entire complement, sufficient for
`-delta*(1-pbar)+M*pbar<0`. A nonzero I could obstruct L423's specified
occupation law; realization, clipping and L413's regulator margin remain
independent gaps.

Reuse audited C426a/C426b, the fixed full-response range, all eight
step-196 moment bounds and literal selectors. First evaluate a conditional
anchor at g=1 using complete branchwise angular quadrature. Then use
response-derivative transport on a finite partition, counting fallback
and failed evaluations as well as strict-state evaluations. Stop on a
strict comparison or the original caps. Preserve all unsuccessful bounds.
The corrected inherited callback total through step 198 is 166413,
leaving 95731 below the combined 262144 cap. No sampling, joint-prime
subdivision, signed polynomial expectation, altered response law or
M_* retry is authorized.

Initial checkpoint: no new numerical bound or sign had been claimed.

Completed result: [C426c](../lemmas/C426c-smaller-complement-bounded-test.md)
contains the full proof and certificate qualifications. A(1) is negative,
but no saved cutoff has a successful complete comparison. Fourteen
response slabs, including every strict and fallback derivative, give a
smaller full-complement bound without a useful certified core. Including
all auxiliary value-bound calls and the consistency check, combined work
is 261020/262144. Park this implementation; retain I in [-.194,.114].
