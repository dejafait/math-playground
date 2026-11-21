# Fixed-panel S7 contact: midpoint construction misses the saved box

9 November 2026, step38. The invocation-start EXPLORE assessment was
`drafts/literature/2026-11-09-contact-conditioned-seventh-moment-test-37.md`.
Only its finite class on panel0 was tested. Canonical finite-log and
flux identities remain [L874](../lemmas/L874-actual-theta-finite-contact-flux-reduction.md)
and [L923](../lemmas/L923-fixed-weighted-cubic-floor-and-unpaid-flux-deficit.md);
the complete input intervals and strict H1 bounds remain
[L917](../lemmas/L917-low-time-twelfth-moment-enclosures-and-h2-budget-stop.md).
No new lemma is claimed.

One rational construction rounded the exact interval midpoints for
m0,...,m5 to the nearest multiple of 10^-12. It retained the common
m0. The positive leading logarithmic block determined (p,q,1) from
the first two null rows; the third row determined S6 and m6. For this
tuple only, all principal minors of W=(y_(i+j+1))_(0<=i,j<=2) were
strictly positive, justifying the candidate choice y7=v^T W^(-1)v,
v=(y4,y5,y6). This specializes the Schur theorem already inspected in
the assessment; no inverse for arbitrary members was assumed. The
coefficient vector is defined exactly as (p,q,1)/sqrt(1+p^2+q^2).

**WHY IT FAILS.** The forced m6 is exactly

    15398474721871902606918368525740454695290982837825130603
    /751907982071339259336119494269016164667569895509900000000000.

It lies in [0.0000204792010,0.0000204792011], whereas the complete saved
upper endpoint is
`0.00002047688138780858510145627382688526320382798415118205041055084465952868866993271164255933509926153165`.
Exact endpoint subtraction is negative for upper-minus-m6. The relative
box position is in [2.30548132,2.30548133], requiring membership in
[0,1]. Therefore the tuple is inadmissible even though its computed
flux is in [5.34990779e-15,5.34990780e-15]. A positive flux outside the
class proves neither failure of the required implication nor existence
of a class member. No universal sign or infeasibility proof was found.

Reproduce with `python3 scripts/heat/contact-s7-fixed-panel-38.py`.
Exit status 1 deliberately reports the failed candidate. Full exact
endpoints, common-mass values, matrices, all principal minors, null-row
and finite-log residuals, normalized coefficient products, flux, checks
and failures are in `scripts/heat/contact-s7-fixed-panel-38.json`.
Of 94 exact checks, the sole failure is `m6_in_complete_interval`.
The complete failure, m6 membership record, check list and residuals
were inspected with the shared JSON inspector. Other checks are useful
diagnostics; they do not repair the failed interval membership or
constitute an independent later audit.

The attempt stops at this first unpaid comparison, without a second
candidate, box widening, new moments, quadrature or sweep. The standard
Schur/logarithm algebra is reproduced, not a new general theorem. Outcome
EXPLORATION/REPRODUCTION, with no progress beyond the checked sources and
no mathematical budget reset. L921/L922/L923 retain their original scopes.
Actual realization/tilt relations, contact sign, initialization/tangency,
other panels/degrees and global continuation remain unresolved.
