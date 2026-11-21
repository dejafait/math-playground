# Actual-Xi quadratic tail — source-approved quantitative continuation

TARGET: Establish an explicit uniform C/log T bound for the actual-Xi quadratic-tail C2 remainder on |v|<=1 and state the zero-safe first-Laguerre transfer with its full signed quadratic term retained.
CHECKED: 2026-11-03
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed exact-object search, primary comparison and local duplicate/failure review in 2026-11-03-actual-xi-quadratic-tail-scope.md; this nomination narrows that reviewed scope to one quantitative application, not a new source search or novelty claim.
SOURCE_EVIDENCE: Direct primary sources checked 2026-11-03: https://www.homepages.ucl.ac.uk/~ucahpet/IANTnotes2018.pdf Theorems 7.5/7.7, printed pp.56–59; https://arxiv.org/pdf/2412.15470v2 Theorem 1.1 p.1 and Section 5 pp.23–24; https://arxiv.org/html/1309.0055v2 Definition 1.1 and Proposition 2.2 proof (2.3), pp.3–4. Reuse L018/L024/L467/L471 and the completed scope comparison for the other leads; applicability and read limits below.
COMPARISON: The product and count inputs are covered. The changed physical disk, explicit Taylor-remainder constant and signed normalization are an elementary quantitative specialization. L464 already treats reciprocal-square shells, and L476 a shrinking clipped integral; neither is the exact C2 remainder. No reproof of Hadamard factorization, counting, or known sign identity is needed.
GAP: Prove analytic cancellation/nonvanishing and a normalized logarithm, bound the complete exterior-zero remainder with explicit constants/onset, and justify the denominator-free first-sign transfer. A favorable actual-local margin, central-value normalization, higher signs and global coverage are not supplied or approved.
REASON: Separate literature approval completed on 2026-11-03: direct source URLs and theorem/hypothesis checks repair the reported citation gate. SPECIALIZE remains appropriate for one bounded RESEARCH / REPRODUCTION application; no new mathematical result or novelty claim.
SCOPE: Exactly the TARGET; actual Xi, all actual zero locations and multiplicities, T sufficiently large with an explicit absolute onset, t in [T/log T,T], Xi(t)!=0, closed cutoff H=2*pi*log T; no RH, simplicity, separation, projected zeros, fixed-half-plane premise or central-value lower bound.

## Objects and proposed threshold

Let alpha denote distinct Xi zeros and m_alpha their full multiplicities.
Put L=log T and H=2*pi*L. Use

    P(v)=product_(|Re(alpha)-t|<=H) (1-v/(alpha-t))^m_alpha,
    R(v)=Xi(t+v)/(Xi(t)*P(v)),
    E(v)=log R(v), E(0)=0,
    Q(v)=E'(0)v+E''(0)v^2/2.

R is to be defined by analytic cancellation at local zeros; its
nonvanishing on a neighborhood of the full complex disk, the existence
of E and real Taylor coefficients must be proved, not assumed. Retain
both signs of ordinates and equality at the cutoff. Xi(t)!=0 is an
explicit normalization restriction, not a uniform lower bound.

The exact requested threshold is

    sup_(|v|<=1) |(E-Q)''(v)| <= C/log T

for a displayed absolute numerical C and displayed absolute onset,
uniformly in the specified t. This is unproved. A convergent full tail
estimate is required; a finite numerical screen is not evidence for it.
The allowed method is the local logarithmic product with its first two
Taylor terms removed, complete shell bounds from L467, and justified
local differentiation. No growing-radius substitution in A.1 is allowed.
Account explicitly for exterior zeros at arbitrarily large positive and
negative ordinates; summability for a fixed t is not uniformity in t,T.

Use the known gauge identity, compare Xi(t+v) with
Xi(t)*exp(Q(v))*P(v), and state the sufficient signed margin and its
error weight. Keep Q'' with its actual sign and value; if claiming a
sign for it, justify that from the actual conjugate pairs, without
assuming a sign for the local polynomial. Do not replace algebraic
squares by modulus squares on real v or divide by P at its zeros.
Handle real multiple zeros by the canceled entire identity/continuity.
Extending the normalization to Xi(t)=0 is outside this target and must
remain an explicit limitation. No unconditional first sign is promised.

## Relevance and stop decision

The main gap is actual-Xi all-degree mixed positivity, including initial
signs at unbounded heights. This intermediate bound could turn a future
independent local-polynomial margin into a controlled actual-Xi first-sign
test; it distinguishes an approximation error from the retained signed
curvature. It does not pay that margin, higher signs or global coverage.

Success requires the complete bound and the zero-safe signed interface
with exact hypotheses. If uniformity, constants or a term's sign fails,
record the precise obstruction and narrow/park that claim. Even a successful
calculation does not justify another normalization iteration: subsequent
sign work needs a materially new independently testable actual-local
margin/witness and its own source assessment. No such margin is currently
known from the checked inputs. This explains why a creative central-gap
attempt is not nominated by this review.

L018/L024/L467/L471 are the essential local input IDs. L464 Section 3
is an implementation/duplicate comparison, not a new premise; L476 and
the Gaussian/heat stops are contrasts only. No cross-notebook input is
used. Full matching Mathlib coverage is unchecked. Full proof and precise
citations belong in a canonical lemma only after a later research turn.

## Separate source approval — 3 November 2026, step 223

This is a citation/process repair, outcome STALLED: the prior source
comparison already approved the same mathematical scope. The target,
hypotheses and proposed threshold are unchanged. No calculation was
performed, and no lemma or mathematical script was changed.

Primary retrievals used the three exact URLs in SOURCE_EVIDENCE, then
within-source searches for Proposition 2.2, Theorems 7.5/7.7 and the proof
of Theorem 1.1. No additional general discovery search was needed; reuse
the exact-object searches and duplicate/failure comparison in the scope
assessment. These are inspected sources, not unread leads.

[Petrow, *Introduction to Analytic Number Theory*](https://www.homepages.ucl.ac.uk/~ucahpet/IANTnotes2018.pdf),
Theorem 7.7, printed p.58, requires order at most one and a nonzero
value at zero. Its genus-one factorization converges on compact sets;
the proof opening p.59 uses square summability and a nonvanishing
quotient. Theorem 7.5 supplies the preceding zero/summability input.
L024 already justifies Xi's application and pairing, so import that
canonical result. The source does not assert the requested uniform
moving-center remainder or sign margin. This check read the statement
and relevant proof opening, not a new independent audit of the entire
factorization proof. The PDF is unversioned; the exact URL above is
the copy inspected today.

[Bellotti–Wong, arXiv:2412.15470v2](https://arxiv.org/pdf/2412.15470v2),
7 July 2025, Theorem 1.1 p.1, counts positive ordinates through T and
states its error estimate for every T>=e. Section 5, pp.23–24,
separates heights at 30610046000 and uses a previously computed
argument bound below that height. Both cases were checked. No source
computation was rerun. L467's existing audit handles multiplicities,
closed endpoints and low-height shells; its conclusion is reused
unchanged. The source alone does not state the requested C2 estimate.

[Csordas, arXiv:1309.0055v2](https://arxiv.org/html/1309.0055v2),
21 February 2014, Definition 1.1 and Proposition 2.2 proof (2.3),
were checked through the proof's sign inference. The identity comes
from its product; the proposition's positivity additionally excludes
nonreal real-parts from a prescribed interval. That exclusion is not
available here. L471 already verifies the actual-Xi identity and
convergence; its gauge formula remains the canonical application.
No positivity theorem is imported. Preserve the actual quadratic
curvature in the future transfer and the stated central nonzero
normalization restriction. Mathlib coverage remains unchecked.

The separate approval is complete for exactly TARGET and SCOPE above.
Continue with one bounded quantitative reproduction, certifying the
complete exterior tail, explicit constants/onset and zero-safe signed
interface, or documenting the precise failed hypothesis/bound. A
favorable local margin, central-zero normalization, higher signs and
global coverage remain independent and unapproved. Success cannot
justify another normalization iteration without a materially new,
separately assessed signed mechanism.
