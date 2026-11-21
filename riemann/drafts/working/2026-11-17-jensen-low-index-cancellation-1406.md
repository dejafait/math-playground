# Signed low-index budget — working save1406

Approved target remains assessment1402's exact fixed actual-Jensen
squared pair. This is the refined low-index test saved in step1405,
not a new target or a literature approval. Main gap remains actual-Xi
all-degree positivity L030-L032/C032a. An O(1) bound for
sum_(k<=L) B_k^2/k would pay only part of C019u's diagonal; its
high indices and off-diagonal budget, then sign density and ordered
root separation, would remain open.

Inputs read: C019u in full; C019p's definitions and alpha coefficient
proof; C019r's definitions and eventual scales; C019t's transfer
statement. Retain C019m/p/s/t contracts, C019r's mean, exact alpha,
linear taper, L=floor(X^(1/1000)), own heat times and source floors.
Prior stops1403/1405 concern absolute estimates, not this signed test.
No ordinary-to-heat theorem or unread source is an input.

Working mechanism, not yet a result: for k<=L all six factor indices
are below every source cutoff. The untapered unshifted coefficient
product has local exponents -1,-1,1/2,1/2,1/2,1/2 and cancels.
Introduce six normalized complex shifts in the finite coefficient
polynomial K_k(z). Subtract r=max|z_j| from every shift, factor out
k^(r/log L), and use prime-coefficient cancellation. Higher prime
powers have the summable d_4(p^e)^2/p^e bound. The elementary factorial
identity bounds sum_(p<=L) (log p)^2/p by 2(log L)^2. Candidate norm:
||K(z)||_(k<=L,1/k) <= C exp(r+64r^2).

The four linear tapers are four distinct first derivatives in the
normalized shifts. Cauchy's formula on unit circles should pay these.
The two quadratic heat weights admit exact scalar Gaussian integrals
inside each finite coefficient. This must be proved and dominated;
it is not an imported Gaussian averaging theorem. Normalized heat
widths are at most sqrt(5)/1000 eventually, leaving a strict Gaussian
integrability margin against the above quadratic norm growth.

Required finish: verify the exact shifts and heat identity, uniform
norm and Y-derivative bounds, and convert those to the coefficientwise
supremum-plus-total-variation budget. Stop if these bounds lose a
growing logarithm; failure would concern the sufficient grouped
method, not refute the exact real-pair moment. No calculation script
or numerical experiment is needed. Canonical proof will hold the
complete argument if the test succeeds; this save is not a proof.

## Completion on 18 November 2026

The test succeeds locally: canonical
`lemmas/C019v-low-index-signed-heat-coefficient-budget.md` proves
sum_(k<=L) B_k^2/k=O(1), including coefficientwise supremum and
variation, and the complete low-index grouped norm is O(X).
Its proof records the finite signed Euler coefficient estimate, exact
four taper derivatives, two individually proved Gaussian identities,
and the strict domination margin 4743/10000. There is no numerical
certificate or effective onset. This is local reproduction, with an
independent conceptual audit still outstanding, not a source-level
novelty claim or a full M2 result.

The first unpaid part is now the norm of the exact high-index block
L<k<=Z_*=N_*^2L^4. An O(X) bound for that block, combined with
C019v by the L2 triangle inequality, would pay the full sufficient
grouped norm and then C019u/t would transfer to the fixed actual
pair. Its truncated convolutions, true entries and variation remain
unproved; (6) of C019v cannot simply replace them. This is the next
refined test within unchanged ready1402. Stops1403/1405 remain valid.
