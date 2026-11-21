# One-sided conjugate-pair tail budget — source coverage ready

TARGET: Derive a uniform one-sided bound E(lambda)>=-epsilon I with an explicit rational epsilon<B/100 on 0<=lambda<=1/20, using conjugate-pair real/imaginary decomposition and the de Bruijn strip theorem at L919's unchanged R=100, D=diag(1,200,40000), and B=5691/10^9; stop without refinement if this threshold fails.
CHECKED: 2026-11-21
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step2146 compared the specific H2 head/tail and endpoint stops with infinite Cauchy-Binet, weighted Hermite and real Vandermonde sources; bounded conjugate/strip/one-sided-tail searches found no inspected effective matching H2 budget. Detailed queries, inspected sources and unread leads are in 2026-11-21-h2-conjugate-triple-remainder-nomination-2145.md; no novelty inference.
SOURCE_EVIDENCE: Ding-Qi-Wei arXiv:1505.02528v4 Section3.2 p12 displayed elementary conjugate-block identity; Polymath arXiv:1904.12438v2 Theorem3.2 and the ordinary-critical-strip application in Proposition3.3's proof; L018,L019,L058,L063,L874 and audited L919(1),(8)-(10) and normalization. Exact primary statements were read in step2146; general theorems are imported, not reproved.
COMPARISON: Known conjugate-pair realification preserves positive and negative pieces; the standard strip theorem bounds zero heights without RH and L919 pays complete reciprocal-power tails. These cover the method, not its local scaling, a quantitative lower bound or the fixed hundredfold improvement test. This differs from bounding the absolute norm of the entire E.
GAP: Verify the local strip normalization, pair/multiplicity bookkeeping, full infinite real/imaginary decomposition and explicit effective epsilon. Head census/reality/separation and any strict head margin remain unpaid; no determinant sign is assumed.
REASON: Bounding only the opposing real-vector component may lower the sufficient head tolerance while retaining the positive tail contribution. This is a known-method specialization requiring effective constants, not a new positivity mechanism. The new assessment awaits separate next-turn approval; no estimate has been derived or evaluated.
SCOPE: Exact TARGET only; subsequent RESEARCH classification REPRODUCTION, task calculation. Fixed R,D,band and B/100 threshold; no new quadrature, zero census, direction search, cutoff change, grid refinement or stronger zero-free region. No creative claim or cross-notebook premise.

## Relevance and inputs

The main gap remains L030-L032/C032a actual-Xi all-degree mixed
positivity. This target pays only a one-sided tail cost for d=2.
If successful, a separately certified minimum eigenvalue of L919's
head above epsilon would be a sufficient positivity input. Neither
that head certificate nor other degrees, contacts, initialization or
global continuation follows. L917/L920/L922/L938 are stopped contrasts,
not positive premises. C874f concerns a different known slice only.

Use exactly L919's opposite-pair multiset, head including |zeta|=100,
strict complement E, coefficient convention and scaling. Its identity
and summation bounds hold for all zeros with full multiplicity and
do not require simple zeros or continuous indexing. L018 supplies
the ordinary critical strip at zero; L019/L058 identify the actual
family and its conjugation; L063 gives the product, with the uniform
tail application already paid in L919. Do not reread unrelated proofs.

The primary citations are
[Ding-Qi-Wei v4, Section3.2, p12](https://arxiv.org/pdf/1505.02528v4#page=12)
and [Polymath v2, Theorem3.2 and Proposition3.3 proof](https://arxiv.org/html/1904.12438v2#S3).
Use only the former's elementary pair identity, not the global
finite-rank decomposition's nonsingularity assumptions or PSD theorem.
Use the latter's standard strip theorem, not a conjecture that low-time
zeros are real. Its source t>t0 case must be distinguished from the
initial ordinary-strip bound; the closed interval includes lambda=0.
The normalization F(lambda,z)=8H_(4lambda)(2z) is already in L919.
The height conversion must be checked explicitly in the application;
no converted quantitative strip or epsilon was derived in this review.

## Bounded future calculation

Apply the cited block identity to the rank-one terms actually present
in E, absorbing their algebraic scalar in the reciprocal-power vector
when justified. Verify every factor of two for nonreal conjugate
classes, real classes and any conjugation-fixed opposite class.
Multiplicity copies must all be counted. Prove any exclusion of
imaginary-axis tail zeros from the imported strip, rather than
silently treating them as real or duplicating them.

Seek a full, explicit lower matrix bound by retaining the nonnegative
real-vector contribution and bounding the opposing imaginary-vector
contribution with the known strip and L919(10). Prove convergence of
both pieces and justify regrouping at each parameter uniformly as
needed for the bound. Cauchy-Binet or a determinant expansion is not
required for this changed test. Algebraic squares in H2 remain
algebraic squares; modulus bounds are permitted only for the error.
No all-real-zero or H3 assumption is allowed.

The pass threshold is precisely epsilon<B/100. A nonnegative explicit
rational epsilon meeting it must bound every real unit-vector
quadratic form of E from below on the entire closed band. Explain
why the bound is one-sided and compare it to L919's B in the same
matrix units. Do not claim ||E||<=epsilon unless independently proved.
If a finite estimate fails this fixed threshold, report the bound and
stop without optimization. Neither outcome licenses a head sweep.
The hundredfold threshold is a prospective discriminator for material
improvement, not a known fact or a condition equivalent to RH.

If arithmetic scripting is useful after approval, save the full
certificate inside scripts/heat/ and print actual/required bounds,
failures and paths only; independently inspect the load-bearing
values. A hand-checkable rational estimate needs no script. Write
a canonical lemma only if a relevant valid result is obtained;
include hypotheses, qualifications and Mathlib coverage. Full matching
Mathlib coverage is currently unchecked. Do not reprove the imported
strip theorem or Jensen; justify only this quantitative application.
