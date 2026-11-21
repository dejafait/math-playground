# Real-axis polynomial-exponent closure: source comparison1329

TARGET: Assess known closure obstructions to approximating K(u)/K(0) uniformly on [-1/10,1/10] by exp(P(iu)), where P is an even real polynomial, P(0)=0, P' has only real zeros, and P(iu) tends to minus infinity as real |u| tends to infinity, without assuming convergence of complex jets.
CHECKED: 2026-11-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1329 searched the precise exponent family, real-rooted derivative approximation, absolute-monotonicity closure and pointwise-limit terminology; scoped local duplicate/failure checks found only the nomination and the explicit weaker-topology exclusions in assessment1325/stop1326. No exact actual-theta closure theorem was located; this is not a novelty claim.
SOURCE_EVIDENCE: Konheim--Weiss, Functions which operate on characteristic functions, Pacific J.Math.15(4)(1965),1279-1293, Section2 definition and Lemma3/proof pp1283-1284 read in the publisher PDF. The one-variable closure is explicitly included. Reuse discovery1325 for Branden--Chasse v2 Theorem5.4; its statement was also checked in the primary PDF p26. Widder ChapterIV content was inaccessible and is not an input.
COMPARISON: A primary real-variable closure theorem is now available, so absence of complex-jet convergence is not itself a source blocker. Its hypotheses must still be established for transformed negative-log polynomial profiles and their finite limit; the source does not identify the actual K or assert the requested approximation is impossible.
GAP: The unperformed specialization must establish the polynomial-profile hypothesis, transfer the stated real-axis convergence through the logarithm, and compare the resulting necessary condition with the already audited C019a coefficient data. No family-specific closure claim or incompatibility has been derived in this literature turn.
REASON: The source gap has been repaired by a precise named result stronger than uniform-limit closure in its own class. Only the actual-family applicability argument remains; re-proving the general closure theorem or repeating the Jensen calculation is unnecessary.
SCOPE: Completed literature-only review of the exact saved family and interval. The separate continuation1329 is a bounded known-theorem specialization, prepared for next-invocation approval. No new lemma, finite-difference computation, mathematical script, closure contradiction or actual-Xi sign is established here.

Essential local inputs are L016/L019 for the normalized positive actual
kernel and C019a for the exact-jet exclusion and its limits. L020 is
potential downstream transform motivation, not an input to a closure
claim. No cross-notebook input. The general sufficient transform theorem
is recorded at https://arxiv.org/abs/1402.2795v2, Theorem5.4; its
hypotheses and applicability must remain distinct from the still unproved
family-specific closure application. The prior Jensen source is
https://msp.org/pjm/1989/136-2/pjm-v136-n2-p03-s.pdf.

The admission test was recovery of a precise real-variable closure
result with a bounded applicability test. Lemma 3 supplies that source
input; the remaining specialization is nominated separately. If its
hypotheses fail for this family, stop that application rather than return
to degree sweeps or assert a general approximation obstruction.
Uniform real-axis convergence here is a local necessary
test for a proposed approximation route; transform convergence at all
complex arguments, global tail control, actual construction, all-degree
positivity, initialization, singular blocks and identification remain
independent unresolved requirements. No completeness or novelty claim.

A creative central construction is not yet specified outside the
excluded exact-jet class. This bounded source target is not labeled
creative. Full matching Mathlib coverage for the changed closure target
is unchecked. The research outcome of audit1328 stands independently
of today's source comparison or the next specialization's success.

## Primary source recovered1329

A. G. Konheim and B. Weiss, *Functions which operate on characteristic
functions*, Pacific J. Math. 15(4) (1965), 1279--1293, Section2,
Lemma3, pp1283--1284,
[publisher PDF](https://msp.org/pjm/1965/15-4/pjm-v15-n4-p15-s.pdf).
The definition requires every mixed derivative, including order zero,
to be nonnegative on 0<=x_i<a. Lemma3 asserts pointwise-limit closure.
Use n=1 on [0,1/100), with finite limit and no right-endpoint claim.
The inspected proof takes n=1 as known, then uses power-series coefficients
and induction; it does not prove the base case. Cite the lemma. Its
statement and proof do not require the assumptions on operator F used
elsewhere in the paper.

The prospective application uses the definitions x=u^2,
F_P(x)=-P(i sqrt(x)), and F_K(x)=-log(K(sqrt(x))/K(0)).
They designate the objects to check, not established class membership.
The polynomial factorization, multiplicities at zero, decay-determined
sign, logarithm continuity, endpoint regularity and coefficient comparison
are all deferred to the next mathematical step. C019a already contains
the required even analytic germ and certified data through order six;
there is no reason to compute another Jensen polynomial. No derivatives
of an arbitrary uniformly convergent sequence are interchanged here.

## Search, overlap and access record

Queries included `"absolutely monotonic" "uniform limits" polynomials`,
`"absolutely monotonic" "pointwise limit" theorem`,
`Bernstein theorem absolutely monotonic functions power series positive
coefficients proof pdf`, `"uniform approximation" "polynomial"
"exponential" "real zeros" derivative Fourier`, and
`"even polynomial" "derivative" "real zeros" "coefficients" Fourier
transform`. Additional negative-log/closure terminology found no exact
actual-theta theorem. Search results are discovery aids, not evidence
for an impossibility result. The original Bernstein papers, Katsnelson's
exposition and the Dimitrov--Rusev survey are unread leads, not inputs.

The Widder publisher page identifies *The Laplace Transform* (1941),
ChapterIV pp144--179, but denies content access:
https://www.degruyterbrill.com/document/doi/10.1515/9781400876457-005/html.
No theorem number or proof from it is asserted. PDF screenshot retrieval
timed out, and a shell download failed DNS; the publisher's web-extracted
definition, statement and full proof passage remained readable. These
access failures do not block citation of the inspected Lemma3.

Local checks covered L016/L019, C019a, discovery1325, assessment1325,
stop1326 and history1328; a terminology search was confined to this
notebook's drafts/literature and ATTEMPTS. The earlier exact-jet stop
does not prove this changed-topology exclusion. The Branden--Chasse
source still supplies downstream motivation only. No relevant matching
Mathlib coverage was checked, and no absence claim is made.
