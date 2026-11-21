# Reciprocal-power production matrix: completed source comparison

TARGET: Assess whether the normalized reciprocal-power-sum exponential Riordan production matrix provides an independently checkable sufficient condition for actual-Xi mixed Hankel positivity, and identify one finite obstruction test.
CHECKED: 2026-11-13
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step773 searched production-matrix/Hankel total positivity, exponential Riordan/Appell production matrices and bounded-moment obstructions; read Sokal 2105.05583v2 Sections2.1-2.3/2.6 and Zhu 2006.14485v2 Proposition3.2/Lemma3.4. Narrow local searches found the older connected-partition comparison as related coverage, not an assessment of this array; queries and limits below.
SOURCE_EVIDENCE: Sokal, DOI10.1007/s00605-022-01687-0, Theorems2.9/2.14/2.19, Proposition2.8, Lemma2.12, Corollary2.13 and complete relevant proofs; published PDF pp17-19/21-23. Theorem2.19 gives the exact formal production formula; Theorem2.14 covers all zeroth-column Hankel minors. L027 already proves S_2>0. No actual production entry was calculated.
COMPARISON: Production total positivity is a sufficient stronger hypothesis, not supplied by defining R or by its entry signs. The general theorem covers F=M,G=t; the associated-subgroup row-polynomial Theorem2.20 does not apply automatically. L057 and L825 retain their distinct scopes. A single entry P_(2,0) is an independent theta-coefficient obstruction test, not another Hankel degree sweep.
GAP: No actual-Xi sign of P_(2,0), other production minor or uniform factorization is proved. The finite test needs S_2,S_3,S_4,S_5 from actual theta coefficients and complete inherited error inclusion. Shifted Hankel coverage is available conditionally on full production total positivity; proving that hypothesis remains open.
REASON: Essential source coverage is now available for one later known-method specialization. Import the cited general criteria without reproof; test only P_(2,0) against zero. A strict negative abandons this Appell construction, not RH; a passing test does not justify a sweep or propagation claim.
SCOPE: Completed literature-only comparison of the unchanged proposed array; separate finite-test continuation is drafts/literature/2026-11-13-appell-production-entry-test-773.md. No mathematical invocation, new lemma, evaluator or script in this turn.
LITERATURE_REASON: The invocation-start assessment was REVIEW_REQUIRED and lacked primary production/Hankel theorem hypotheses and indexing; existing coefficient-evaluator coverage is reused rather than refreshed.

## Original nomination (source status superseded by step773 below)

Main gap: L030-L032/C032a require actual-Xi mixed quadratic-form
positivity for every real polynomial. The potential downstream use is a
known production-matrix theorem implying the required Hankel positivity
from independently established total positivity of a different matrix.
That implication and its exact shifted coverage must be imported only
after primary hypotheses and relevant proof cases have been read.

Proposed objects, not established positive objects: use the actual
reciprocal power sums S_k of L024/L025 as in L030. Subject to separately
justifying S_2>0, put m_n=S_(n+2)/S_2 and define the lower triangular
array R_(n,k)=binom(n,k)m_(n-k), for 0<=k<=n. Its proposed exponential
Riordan notation is [M(t),t], M(t)=sum_(n>=0)m_n t^n/n!. Define the formal
production matrix P=R^(-1) Rbar, where Rbar deletes R's first row; check
that each entry is well-defined with the exact index conventions. These
are definitions for source comparison, not claims of total positivity,
convergence, a new identity or a lemma. Formal versus analytic hypotheses
must be distinguished. No zero locations or RH premise is permitted.

The literature turn should search exact/stronger production-matrix,
exponential Riordan, Hankel total positivity and planar-network results;
retrieve primary theorem statements, hypotheses and relevant proof cases
before proposing an entry calculation. Determine whether this particular
choice f(t)=t is too restrictive. Do not substitute a different array
silently. If an exact theorem covers the formal array, identify at most
one finite obstruction test confined to the leading 4-by-4 block of P,
including every required input S_k and the exact sign/minor threshold.
A theorem citation alone supplies no actual-Xi entry signs.

Continue only if the criterion is a true sufficient condition with an
independent theta-coefficient interface, and a concrete finite minor can
falsify that proposed sufficient construction without requiring unknown
zeros. A negative minor would abandon this chosen array, not RH. Passing
all selected finite minors retires that diagnostic unless a distinct
uniform production-sign mechanism is identified and separately assessed.
If the criterion assumes the desired Hankel positivity, or the literature
already rules out this Appell choice except in a demonstrably inapplicable
class, record that source obstruction and park it without a calculation.
Do not replace the old degree sweep by a production-block sweep.

Compare the exact L057 finite-extrapolation obstruction and L825
common-symbol obstruction before any mathematical invocation. Essential
local inputs for future work are L018's actual completion, L024/L025
reciprocal power sums and L030/L032's mixed criterion; canonical proof
ranges for any additionally used identity must be read then. No
cross-notebook input is authorized or needed. S_2 positivity and all
normalization/index/analytic assumptions remain unresolved in this
nomination. Full matching Mathlib coverage is unchecked.

The next task is literature_comparison/standard/high. Source coverage and
an independent all-degree sign mechanism are missing, so this nomination
is not yet a justified proof_attempt/creative. It is a bounded discovery
lead, not a new lemma or a novelty claim. Its assessment requires a
separate turn; the completed C825a audit stands independently.

## Completed source review — 13 November 2026, step773

The main gap remains L030-L032/C032a's actual-Xi algebraic-square
positivity in every degree. The intermediate target was a source-backed
sufficient production criterion and one falsifiable leading-block test.
The source criterion is available; its actual entry signs are not.
This is local source-coverage progress using known results, with no
advance beyond those sources and no actual-Xi mathematical calculation.

### Search and reuse

External queries included `Sokal exponential Riordan production matrix
Hankel total positivity Appell theorem`, `exponential Riordan Appell
production matrix total positive Gaussian Poisson cumulants`, `Alan
Sokal 2021 forests rooted labeled trees arxiv 2105 total positivity`,
`"Appell" "production matrix" "totally positive"`, `"Appell"
"production" "total positivity" moments`, `"Riordan" "Appell"
"Hankel" "production"`, and `"production matrix" "bounded" "moments"
Appell`. These found general criteria and examples, not an actual-Xi
application or an inspected theorem excluding every nontrivial Appell
choice. This bounded search establishes neither novelty nor absence.

Local exact-term searches of drafts/literature and ATTEMPTS found
`2026-11-06-theta-connected-partition-interface.md`. Reuse its inspected
Lehner path/cumulant and universal-lifting comparisons: crossing and
permutation signs persist; a cumulant moment assumption is not an
independent sign input. The production criterion here asks for a
different explicit sufficient hypothesis. No new partition theorem or
positive moment law is assumed. L057 and its finite-extrapolation
ATTEMPTS entry were read, as were L825's common-symbol statement and
necessary-condition proof. L825 concerns centered additive factors,
not this reciprocal-power array. The finite-residue sequence's step772
stop remains closed; no adjacent-degree continuation is proposed.

### Primary theorem hypotheses and proof cases actually read

Alan D. Sokal, *Total positivity of some polynomial matrices that
enumerate labeled trees and forests I: forests of rooted labeled trees*,
Monatshefte fuer Mathematik (2022),
[DOI10.1007/s00605-022-01687-0](https://doi.org/10.1007/s00605-022-01687-0),
[published primary PDF](https://discovery.ucl.ac.uk/id/eprint/10144793/1/Sokal2022_Article_TotalPositivityOfSomePolynomia.pdf),
[arXiv:2105.05583v2, 8 March2022](https://arxiv.org/html/2105.05583v2).
Read Section2.1's conventions; Section2.2 (2.5)-(2.11) and uniqueness
paragraph; Section2.3 Proposition2.8 and its induction, Theorem2.9,
Lemma2.12/(2.20)-(2.22), Corollary2.13, Theorem2.14 and Example2.15;
Section2.6 (2.30)-(2.39), Lemma2.18 and Theorem2.19 including its forward
column-generating-function argument and reverse formal-ODE argument.
Section2.1 is on PDFpp10-11; the propagation and production statements
and proofs cited above are on PDFpp17-19 and21-23, respectively.
Also inspected Theorem2.20's hypotheses to exclude its automatic use.

The paper uses TP to mean every minor is **nonnegative**, permitting
zeros. Theorem2.9 requires an infinite row-finite or column-finite
matrix over a partially ordered commutative ring; TP of order r passes
to its output O(P), with O(P)_(n,k)=(P^n)_(0,k). Proposition2.8 proves
the minor statement by induction and Cauchy-Binet on finite row
truncations. This is not an assertion that nonnegative entries suffice.

Theorem2.14, under the same finiteness/order hypotheses, passes TP of
order r to the entire zeroth-column Hankel matrix. Its proof uses
Lemma2.12's identity H=O(P)O(P^T)^T and Cauchy-Binet. The proof explicitly
handles both finiteness alternatives: the sum over the intermediate
index is finite on the first factor for row-finite P, and on the second
factor for column-finite P. Thus no analytic infinite-sum exchange is
being imported. The conclusion concerns every minor, not just leading
principal determinants; shifted Hankel matrices are included as
submatrices. For real symmetric finite restrictions, the standard
principal-minor criterion for positive semidefiniteness gives the
required mixed-form implication when the positive S_2 normalization
is restored. This is the applicability of a known sufficient theorem,
not an unconditional positivity result.

Theorem2.19 works over a commutative ring containing the rationals,
for lower-triangular L with invertible diagonal and L_(0,0)=1. It
identifies P=L^(-1)Delta L, where Delta removes row zero, by

    p_(n,k) = (n!/k!)(z_(n-k) + k a_(n-k+1)),
    A(s) = G'(Gbar(s)),   Z(s) = F'(Gbar(s))/F(Gbar(s)).

These are the source's formulas (2.33)/(2.35); the a sequence here
belongs to the production theorem, not L776's coefficients. Coefficients
with negative indices vanish. F and G are formal series with F(0)=1,
G(0)=0 and invertible G'(0); no positive measure, zero-location premise,
analytic continuation or convergence radius is required.

The nominated pair is exactly F=M,G=t over the real numbers, provided
S_2 is nonzero. Its defining Riordan columns are the proposed binomial
columns, and its diagonal is one; the source's lower-Hessenberg
production matrix is consequently row-finite. This identifies the
correct class and conventions without computing a production entry.
Full TP of P is an additional, unpaid assumption, not a consequence of
calling R an exponential Riordan array. No converse is imported.

Theorem2.20 is stronger for row-generating polynomials but explicitly
assumes F=1 (the associated subgroup). It cannot be invoked for general
M. Example2.15 already shows why general output-row polynomial TP is
false. Zeroth-column Theorem2.14 is precisely the needed conclusion
here, so that extra theorem is unnecessary. No planar-network
realization is supplied by these source definitions; one would need
independent nonnegative weights and the correct minor signs.

Bao-Xuan Zhu, [arXiv:2006.14485v2](https://arxiv.org/html/2006.14485v2),
*Total positivity from a generalized cycle index polynomial*,
Section3 Proposition3.2, production display and Lemma3.4, was inspected
as a matching formula/criterion comparison. It uses ordinary A,Z
coefficients inside the factorial-scaled production formula and cites
the general propagation results. Its special PF-function sufficient
families do not establish the actual M'/M sign conditions here. Sokal's
self-contained theorem/proofs suffice; there is no reason to reprove
them or to import an unread stronger family. The search also found
Zhu's 2202.03793 row-polynomial paper and the original branched-fraction
paper 1807.03271; their full proofs were not read and are not inputs.

### Local normalization, independent interface and the single test

Read L018/L024/L025/L030/L032, L033/L040 and L027. L027 already proves
S_k>0 for 1<=k<=6 using the established zero-free central disk and strip;
it does not assume RH. Thus S_2>0 is available, contrary to the
nomination's unresolved-normalization note. This is reuse of a proved
local result, not a new sign theorem or an independent audit of L027.
L040 supplies the justified finite Newton recurrence from actual theta
coefficients; hence the test need not use any zero list.

The one proposed discriminator is the **1-by-1 minor P_(2,0)**, inside
the leading 4-by-4 block. Apply the cited production formula in a later
research turn and enclose it against the required threshold zero.
It needs m_0=1,m_1,m_2,m_3, equivalently S_2,S_3,S_4,S_5. This is only
a proposed specialization: no cumulant expansion, coefficient identity
for this entry, numerical sign or general obstruction is derived now.
Its exact computation and normalization must be checked next turn.

The available evaluator interface is L776's actual G coefficients,
L778's audited uniform complex error on |w|<=1600, and L791's
Cauchy-error/normalization procedure audited in step478. Read those
specific statements and audit ranges, and reuse
`2026-11-04-actual-fixed-pair-certificate-audit.md` for the established
integration/arithmetic contracts. Future use requires coefficients
through index5: L791's saved five gamma intervals alone cover only
indices0-4 and are insufficient. The complete L778 polynomial evaluator
has the needed coefficient data; its current record/hash, failure fields
and each used interval must be inspected then, with E_G/1600^j added
to every coefficient enclosure. No evaluator data was verified today.
Numerical conclusions retain L778's trusted Decimal/transcendental
software contracts; there is no new evaluator or backend attestation.

A strict negative upper endpoint rejects TP of this chosen production
matrix and closes this Appell sufficient construction. It refutes
neither Hankel positivity nor RH. If the entry is nonnegative, this
single diagnostic ends without certifying production TP; do not sweep
degrees or minors. An interval crossing zero is inconclusive and may
not be reported as either sign. A uniform production-sign mechanism
still has to be specified and separately assessed before propagation.
This limited test is meaningful even though other main-goal gaps stay
open. It is routine specialization/calculation, not a protected creative
attempt; no independent all-degree theta sign mechanism is yet ready.

Mathlib: targeted public documentation searches for Riordan and
production/Hankel combinations returned no matching documentation
result. This is not evidence of absence. Full matching coverage remains
unchecked; no Lean theorem is an input. No cross-notebook input was used.
