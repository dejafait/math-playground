# Two-sided quotient cancellation: source nomination1965

TARGET: Assess source coverage for a two-sided fractional-moment cancellation diagnostic for C028d's actual quotient, testing whether its antisymmetric logarithmic-moment error vanishes after the degree limit and then the cutoff limit.
CHECKED: 2026-11-20
DECISION: EXPLORE
SEARCH_EVIDENCE: Review1966 searched paired log-moments, negative polynomial moments/Remez and uniform cumulant remainders; reused1962's positive coverage and scoped local stops. Queries, inspected passages and access limits: drafts/literature/2026-11-20-two-sided-quotient-source-notes-1966.md. No matching theorem or novelty finding.
SOURCE_EVIDENCE: Fradelizi arXiv:0807.0080v1 Sections2.3,3.1-3.2 (8), Corollaries8-9 and complete proofs, PDF pp11-15, https://arxiv.org/html/0807.0080v1 ; Wainwright--Jordan author draft Section3.5.1 Proposition2/(3.40)-(3.41) and proof pp61-62, https://people.eecs.berkeley.edu/~jordan/sail/readings/wainwright-jordan-fnt.pdf ; reuse positive-moment sources1962. Carbery--Wright remains unread, not imported.
COMPARISON: Fradelizi supplies polynomial small-value and negative-moment estimates allowing all multiplicities, with median scale and strict exponent range; it does not give the rational quotient's signed cancellation. Log-partition smoothness has no uniform-in-degree remainder rate. C029f still decides only the one-sided comparison.
GAP: Actual inverse-quotient applicability and the degree-uniform full-window signed remainder are unproved; no vanishing or nonzero value of E is established. Separate moment bounds do not meet the nominated continuation test.
REASON: Completed essential source comparison; park the full paired diagnostic pending a materially new signed-complement input. Use accessible Fradelizi coverage instead of retrying the persistent Carbery--Wright source blocker; isolate a fixed negative-interval prerequisite for separate review.
SCOPE: Literature only; unchanged actual C028d/e/f/g coefficients, all algebraic multiplicities, d>=3, q=1/2, fixed A>=max(1,2sqrt(M)), nu uniform on [-Ad,Ad], degree first. No new lemma, calculation, source theorem application or RH claim is authorized by this nomination.

## Exact proposed diagnostic, not a result

Keep the original Q_d(y)=P_d(y-b_1), f_d(y)=log|Q_d(y)|-d log|y|
and M=exp(b_1)F(1). Consider the proposed quantities

    Z^+_(d,A)=integral exp(f_d/(2d)) dnu,
    Z^-_(d,A)=integral exp(-f_d/(2d)) dnu,
    E_(d,A)=2Ad[log Z^+_(d,A)-log Z^-_(d,A)]
              -(1/d)integral_(-Ad)^(Ad) f_d(y)dy.

These expressions specify what the source review must assess. In
particular this nomination does not prove that Z^- is finite or that
any sign, expansion or asymptotic estimate for E holds. The candidate
threshold to test, not an available premise, is

    limsup_(A->infinity) limsup_(d->infinity) |E_(d,A)|=0.

The motivation is a signed pairing of the positive and negative
powers, rather than an upper payment through one positive moment.
Whether it removes the comparison cost in this actual family is
unresolved. C029f bounds only the positive-exponent centered loss;
subtracting an unbounded or unknown second loss would be invalid.
Its nonnegative-complement argument must not be transferred to this
signed difference. The new singularities include poles at every real
zero of Q_d, with full multiplicity, as well as the common-origin case.

A vanishing error would still leave an independent upper estimate for
the paired expression unpaid. It would be an intermediate comparison
input for C028d/e's signed-height route, not H_d=o(d) or RH. A proved
nonzero error, or a specific obstruction to controlling it, could
instead reject this signed comparison before attempting that upper
estimate. No such conclusion is asserted now.

## Bounded review and continuation test

Search the exact signed log-moment difference, symmetric cumulant
remainders and positive/negative polynomial moments. Read primary
hypotheses and the essential singular and uniformity cases before any
large source extract. Reuse the adequate positive-moment coverage1962;
seek only the newly essential inverse/paired-moment coverage. Compare
theorems with this singular actual quotient and moving interval measure,
including whether their constants depend on degree or a zero-separation
assumption. Neither a formal Taylor series at exponent zero nor fixed-d
convergence establishes the fixed-q ordered threshold here.

Continue only if this comparison identifies a concrete bounded test
for the signed error, with a source-supported treatment of all root
multiplicities and of the entire complement of any retained interval.
The test may establish vanishing error or an informative nonzero floor;
it must not merely rename the unpaid height bound. If the sources only
bound each nonnegative Jensen loss separately, assume a symmetric law
for f_d, or leave a degree-uniform remainder uncontrolled, record that
specific gap and park the paired diagnostic pending a materially new
input. Do not substitute another q sweep or an identity-only audit.

The limited local comparison reused stops1959/1961/1963 and source
notes1603/1747. Degree-increment assessment1514/source-notes1515 already
park the derivative/primitive comparison; it is not a fresh candidate.
Filename screening in drafts/literature and ATTEMPTS, followed by term
searches in source-notes1959/1962/1603/1747, found no exact paired target.
This is not an exhaustive duplicate or literature search. Further
comparison, not new mathematics, is the next task.

Essential existing inputs are C028d/e/f/g and C029f. The definitions
of Z^- and E carry no established finiteness, signed-remainder bound,
limiting-value or upper-payment assumption. Full matching Mathlib
coverage is unknown. A creative proof route is not ready: only if the
source review identifies an actual-theta cancellation mechanism and
a discriminating bounded test should one be nominated for separate
approval. No creative label is assigned to ordinary cumulant algebra.

## Completed source review1966

The original nomination is retained above. Review1966 inspected the
primary negative-moment theorem, its singular exponent cases, and a
primary log-partition smoothness statement/proof; see source-notes1966.
No theorem supplies the actual-family signed complement or required
ordered vanishing rate. Park this full-window diagnostic under its
stated test; it is not proved false. EXPLORE records the unsuccessful
bounded coverage search, not approval of another unchanged cumulant
calculation. No lemma or mathematical script changed. A separate fixed
negative-interval log-potential nomination1966 is REVIEW_REQUIRED.
