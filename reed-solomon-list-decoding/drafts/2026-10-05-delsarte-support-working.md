# Basic Delsarte LP — bounded mathematical working record

Approved target: test the basic LP for A(1024,10,68) against
65537^28/2^128, uniformly in m. Reuse the prior SPECIALIZE assessment
`literature/2026-10-05-delsarte-support-certificate.md`.

Main gap: arbitrary-center safety at 68 agreements. Intermediate target:
an exact rational dual certificate below threshold or a feasible rational
primal witness above threshold. The former could certify index 956; the
latter stops this basic LP as a sufficient certificate, without proving
unsafety or the existence of an actual code of the witness size.

Essential inputs are L001, C001a and C001b (C001a retains C012a/L019).
L001's common-column uniqueness gives pairwise support intersection <=63;
choosing 68 columns permits extra agreements. No scalar projection or
exponent m is used. The primary LP statement and normalization have already
been inspected in the prior assessment; no enhanced inequalities are used.
The nested-floor stop and triple-support degeneracies remain in force.

Bounded test: compute the 68 by 64 rational Hahn coefficients; use a
high-precision simplex tableau only to identify a basis, then reconstruct
and verify a rational primal or dual witness. A numerical optimum alone
is not evidence of feasibility or a theorem. Continue if an exact upper
certificate reaches threshold; abandon this LP for that purpose only if
an exact feasible primal witness exceeds it. Failure to solve or reconstruct
is unresolved calculation, not exhaustion. Safety at 67 agreements, exact
maxima, determinant density transfer and ABF equivalence remain open.

Initial checkpoint was saved before computation. Exact reconstruction
yielded positive coefficients at every distance 5,...,68, tight Hahn rows
1,...,64 and four positive remaining primal slacks. The matching dual is
positive at rows 1,...,64, zero thereafter, and tight at every distance.
Equal objectives give the exact optimum U-1, where U is L001's support
ratio, exceeding threshold by more than 2.766 times. The complete result
and arithmetic qualifications are canonical in L021; the independent
audit recomputes all 4352 coefficients and every inequality. Basic LP
optimization is now stopped for this threshold, without claiming unsafety.

The overview was condensed to repair the reported 100-line documentation
limit; canonical proofs and existing unfinished work were preserved.
Only a joint-distance SDP source comparison is proposed for the next turn,
with REVIEW_REQUIRED coverage; no new SDP bound was derived or assumed.
