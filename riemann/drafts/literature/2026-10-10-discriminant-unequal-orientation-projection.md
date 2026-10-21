# Signed unequal-orientation projection — source comparison

TARGET: Determine whether the complete k=1 projection in L390 satisfies H^(-1) integral_[H,2H] 2 M(t)|Z(t)|^2 Re(K(t)E(t)Z(t)^2) dt = o((log H)^4), using signed unequal-orientation fourth moments.
CHECKED: 2026-10-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Bounded searches for unbalanced/nonabsolute/asymmetric fourth moments, conjugate-cube means and Gonek gamma-weighted Dirichlet-series lemmas; inspected readable primary modified-Gonek statements and Bourgain's unconditional subconvex theorem. Reused the balanced assessment and narrowly compared L390, its step-45 failure, and the older Gonek source-access qualification; no exact physical-moment match was found.
SOURCE_EVIDENCE: Laaksonen–Petridis arXiv:1505.00623v1 Lemma 1.2 and accepted manuscript dated 2017-02-26 p. 3; Sourmelidis–Steuding–Suriajaya arXiv:2007.14008v2 Section 3 between (35) and (36), both gamma phases and following application; Gonek (1984) Lemmas 2–5 endpoint-case prose, pp. 130–132, with garbled displays excluded; Bourgain arXiv:1408.5794v2 Theorem 5 (0.5), p. 2, Section 4 (4.1)–(4.3), p. 19. Precise links, hypotheses and limits below.
COMPARISON: Modified Gonek evaluates signed gamma-weighted absolutely convergent Dirichlet series with an explicit arithmetic sum and power-saving error on a right line; it is not a balanced moment theorem or the full physical k=1 estimate. Bourgain supplies a stronger pointwise input for a new connector test. L390 already handles the full-tail leading-scale transfer; its failed O(H^2) absolute budget is preserved.
GAP: The physical carrier/ordinary-jet conversion, fixed-rational-twist encoding, coefficient-sum bound at the required logarithmic scale, slowly varying weight transfer and sharp connectors remain to be proved in a later specialization. No small-complex-shift uniform moment theorem or k=1 cancellation has been established here.
REASON: Ready source coverage permits one bounded known-tool specialization of the unchanged TARGET; cite the signed mean-value theorem and subconvex bound rather than reprove them. The family-specific passage is necessary because neither source states the physical projection.
SCOPE: L390's exact actual M,K,E,Z and sharp dyadic interval; ordinary critical jets through order two, fixed response heads before height limits, then L390's full-tail transfer. No growing twists or RH.
LITERATURE_REASON: The saved target was REVIEW_REQUIRED for essential unequal-orientation source coverage; the changed input is a readable modified-Gonek statement with signed gamma phases, rather than further balanced-moment browsing.

## Startup proposal retained

The following proposal records the pre-review state; the source comparison
and decision below supersede its pending-coverage language.

The main gap is actual-theta global mixed positivity. This narrower
intermediate target could complete the previously unmatched k=1 part
of the discriminant square; the zero and k=2 harmonics and positive
coefficient noncancellation would remain independent obligations.
A negligible k=1 term alone would not prove the full moment target,
a positive sign proportion, eventual D sign or RH.

The new mechanism is a signed unequal-orientation moment calculation,
not another application of the same absolute rectangle estimate.
For fixed response heads, writing each Hardy jet using exact reflection
turns the k=1 carrier into products with one positive-height and three
negative-height zeta factors, with ordinary-jet conversion coefficients.
This description identifies the source scope; it does not evaluate
those products or authorize a balanced theorem for them.

A later literature turn should retrieve primary hypotheses and essential
proof cases for such shifted fixed-rational-twist (1,3) moments, including
whether complex-shift uniformity permits the required differentiation.
A direct matching result must be imported rather than reproved. If no
adequate source is found in a bounded comparison, document the remaining
specific estimate before considering an EXPLORE decision. Persistent
source failure should park this dependent target, not trigger repeated
access attempts. The prior sharp-Hardy source and discrete-grid routes
remain parked.

Continue only with adequate coverage for a signed contribution at
H log^4 H scale and its complete-tail/sharp-endpoint transfer. A nonzero
leading term would change the reduction and must be retained, not called
a failed search. Stop a proposed negligibility proof if it only reproduces
the O(H^2) certificate. This is an uncovered proposed target, not approval
of previously uncovered mathematics in the turn that derived L390.

Essential continuation inputs: L390 (partial reduction, separate critical
audit pending), L366/L368 complete actual response, L370 physical identity,
L389 fourth norm budgets and the inspected Hughes–Young balanced theorem
for comparison only. All unequal-orientation signed estimates, endpoint
transfers, total beta>0, global positivity, pencil margins and actual
common-zero upper counts remain unresolved. No RH, simplicity,
noncoincidence, independent phases or eventual D sign is assumed.
Full matching Mathlib coverage has not been checked.

## Separate source comparison — 2026-10-10, step 46

### Readable signed mean-value input

N. Laaksonen and Y. N. Petridis, *On the Value Distribution of Two
Dirichlet L-functions*, [arXiv:1505.00623v1, Lemma 1.2](https://arxiv.org/html/1505.00623v1),
also [accepted manuscript, dated 26 February 2017, p. 3](https://discovery.ucl.ac.uk/1544001/1/lvalues_accepted.pdf#page=3),
states the modified Gonek lemma for a Dirichlet series
F(s)=sum a(n)n^(-s) convergent for Re s>1, with a(n)=O(n^epsilon).
Writing a=1+1/log T, its gamma-weighted integral is

    (2 pi i)^(-1) integral_[a+i,a+iT]
      (m/(2 pi))^s Gamma(s) exp(delta pi i s/2) F(s) ds.

For delta=-1 it equals
sum_(n<=Tm/(2 pi)) a(n) exp(-2 pi i n/m)
+O(m^a T^(1/2+epsilon)); for delta=+1 it is O(m^a).
Read both cases in the primary HTML and independently in the accepted
PDF. The statement leaves m's range implicit; do not infer a growing
or complex m theorem from this display. Only fixed positive integer
gamma scales are needed in the proposed integer-frequency encoding.
No RH assumption is imposed on Lemma 1.2; the RH-dependent zero-value
theorems elsewhere in the paper are not inputs here.

A second readable primary restatement is A. Sourmelidis, J. Steuding
and A. I. Suriajaya, *Dirichlet Series with Periodic Coefficients and
their Value-Distribution Near the Critical Line*,
[arXiv:2007.14008v2, Section 3, immediately after (35)](https://arxiv.org/html/2007.14008v2#S3).
It explicitly uses a fixed positive integer q, a fixed epsilon>0,
the line Re s=1+epsilon, a convergent Dirichlet series on Re s>1,
and a(n)<<n^eta for every eta>0. For omega=-1 its integral with
(q/(2 pi))^s Gamma(s) exp(omega pi i s/2) has main term
sum_(n<=tau q/(2 pi)) a(n) exp(-2 pi i n/q) and error
O_epsilon(tau^(1/2+epsilon)); for omega=+1 it is O_epsilon(1).
Constants may depend on the fixed q and coefficient sequence.
Read the two branches, the reference to Steuding (2002), Lemma 3,
and the exact two-exponential decomposition of Delta(1-s) and its
use through (36). Generic coefficients are allowed in the lemma;
periodicity is used in the subsequent application, not in its premise.
That subsequent periodic simplification is not licensed for d_4.

Gonek, *Mean values of the Riemann zeta-function and its derivatives*,
Invent. Math. 75 (1984), 123–141, DOI 10.1007/BF01403094,
[author PDF, Lemmas 2–5, pp. 130–132](https://sas.rochester.edu/mth/people/faculty/gonek-steve/assets/pdf/5-mvzdrvs.pdf#page=8),
provides the originating stationary-phase proof. Read its interior
stationary case, distances within sqrt(A) of either endpoint, exterior
indices, coefficient-error summation and dyadic completion. The OCR
still corrupts displays and screenshot calls returned no inspectable
images; local retrieval failed DNS. No uncertain formula is imported
from that OCR. The readable modern statements above supply the exact
usable formulas; the older access failure remains recorded, rather than
being described as resolved for the original scan. The unread Steuding
(2002) proof and the garbled Conrey–Ghosh (1985), Lemma 1, are additional
leads only, not essential assumed theorems or sources of error constants.

### Endpoint input and specialization limits

J. Bourgain, *Decoupling, exponential sums and the Riemann zeta
function*, J. Amer. Math. Soc. 30 (2017), 205–224,
[arXiv:1408.5794v2, Theorem 5 (0.5), p. 2](https://arxiv.org/pdf/1408.5794v2#page=2),
gives |zeta(1/2+it)|<<_epsilon |t|^(13/84+epsilon), unconditionally,
for every epsilon>0 at large |t|. Read Section 4 (4.1)–(4.3), p. 19:
its missing short-sum ranges are covered by the additional exponent
pair estimates, whose hypotheses are checked there for F(x)=log x;
the approximate functional equation and partial summation complete
the zeta bound. Cite the theorem; no reproof of decoupling or the
exponential-sum estimates is justified. The v1 abstract's 53/342 is
not the exponent of the inspected v2 statement.

This is a critical-line value bound, not a bound for all physical jets
on the whole connector. A later application must give the fixed-strip
Phragmen–Lindelof interpolation, Cauchy derivative-circle control and
gamma-factor estimates before comparing the complete connector with
H log^4 H. It must retain powers of i, every derivative of R, and
the slowly varying logarithmic normalizations. These are elementary
known-tool specializations proposed for testing, not established bounds
in this literature turn.

The signed mean-value sources apply on an absolutely convergent right
line. They do not directly accept the critical line, MK, E, arbitrary
height-dependent coefficients, or a fast gamma phase as a slow weight.
For fixed response heads the proposed route encodes each fixed rational
twist using integer numerator support and an integer gamma scale.
Its normalization and sign must be checked explicitly later. Ordinary
zeta derivatives can instead be treated as fixed logarithm-weighted
Dirichlet coefficients; this offers a route that does not assume an
unread uniform complex-shift theorem. Verify absolute convergence,
coefficient majorants, and the classical generalized-divisor summatory
bound (Dirichlet's hyperbola method) needed at the retained logarithmic
scale. Do not differentiate a nonuniform asymptotic. Partial summation
for the gamma/jet coefficients and every sharp endpoint also remain
application obligations. No physical integral is evaluated here.

### Decision, failures and continuation test

No inspected source states TARGET itself. SPECIALIZE covers one
later proof attempt using the readable signed mean-value input and
Bourgain's bound, with the precise differences above. A fixed-head
O_N(H log^3 H) bound, or another proved o(H log^4 H) bound, would
be a useful threshold; it is sought, not asserted. Any surviving
H log^4 H coefficient must be retained and would change the proposed
negligibility conclusion. Stop if the complete signed calculation
still has an uncontrolled connector or only reproduces the old H^2
budget. No theorem establishes that such a connector is harmless here.

Queries included `zeta unbalanced fourth moment three one chi`,
`zeta unbalanced moments`, `zeta non-absolute fourth`, `Riemann zeta
mixed moment conjugate cube integral`, `Gonek lemma chi Dirichlet
series mean values zeta derivatives 1984 lemma 2`, `generalized Gonek
lemma`, and `Modified Gonek Lemma`. Followed the primary references
identified above. Search snippets, MathOverflow, repository surveys
and publication lists were locators only. Searches did not establish
novelty. Reused the prior Hughes–Young/Bui–Hall/Pliego comparison;
no repeated extraction was needed for unchanged balanced coverage.

The older assessment's Gonek stop concerned unread displays and a
different signed two-factor target; it is not a global ban. The new
readable fixed-integer-scale theorem and subconvex connector input
give a distinct, independently testable implementation. The absolute
four-factor rectangle failure in step 45 remains intact. The narrow
local search found no completed exact k=1 result, and neither L381's
two-factor estimate nor L383's harmonic estimates may be silently
extended to four factors.

Essential local inputs remain L390, L366/L368, L370 and L389;
L381/L383 supply exact carrier conventions only where already proved.
L390 itself awaits critical audit. Even success leaves k=0 coefficient
application, k=2 sharp endpoints, total beta>0, eventual physical sign,
common-zero upper counts, total pencil margins and global positivity
unresolved. Full matching Mathlib coverage was not checked; no library
absence, formal verification, new lemma or RH progress is claimed.
