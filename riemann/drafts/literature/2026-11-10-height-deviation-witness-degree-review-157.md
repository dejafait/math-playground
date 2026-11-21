# Height and deviation versus mixed-witness degree — completed comparison

TARGET: Assess whether an actual off-line zeta zero with |Im rho|<=T and |Re rho-1/2|>=delta forces a negative L030 mixed form of degree at most an explicit D(T,delta), without supplied node separations, comparing L032/L895 and effective finite Li-criterion bounds.
CHECKED: 2026-11-10
DECISION: EXPLORE
SEARCH_EVIDENCE: Step158 searched effective/finite Li criteria, negative-index bounds, reciprocal-zero Hankel/Grommer criteria and quantitative Li-to-polynomial-square conversion; inspected Palojarvi's primary statements and relevant proof cases. Scoped local comparison read L018/L024-L026/L030-L032/C032a/L057/L895 and relevant witness/Hardy assessments. No matching height/deviation-only L030 degree theorem was located; search failure proves neither novelty nor impossibility.
SOURCE_EVIDENCE: Neea Palojarvi, Explicit zero-free regions and a tau-Li-type criterion, arXiv:1807.01506v2 (20 January 2020), Introduction and count assumptions (PDF page indices0-2), Theorem2.1/proof (indices3-5), Lemma2.2/Theorem2.3/proof (indices5-7), Theorem3.1/proof (indices8-11); indices are zero-based, versioned PDF and HTML inspected. Theorem3.1 states separation-free finite Li detection, with printed-constant qualifications below. Brown's original full theorem was not retrieved and is not imported.
COMPARISON: L032/L895 still depend on a finite head and interpolation conditioning. Palojarvi controls a different, Mobius-transformed Li zero sum, not L030's beta-squared algebraic-square form; its finite index window cannot be called a mixed-witness degree bound. The source explicitly reports a gap in Brown's opposite-direction Theorem2. No direct import closes the requested gap.
GAP: An explicit separation-free conversion to L030, a justified height/deviation specialization, complete tail/error control and any source-constant repair remain unproved. No off-line zero or actual sign is supplied.
REASON: Complete this literature-only comparison with an informative scope limit. Park automatic Li-to-mixed import and nominate an independently testable conversion from a supplied certified negative Li margin; that changed target requires its own review before research.
SCOPE: T>=1, 0<delta<1/2, actual nontrivial zero rho with the displayed bounds, multiplicities retained, and L030's actual reciprocal-node form with real polynomial coefficients. The desired D may depend on T and delta but not on unspecified other zero locations or minimal separations. No off-line zero is asserted to exist.

The main gap remains L030-L032/C032a all-degree mixed positivity.
A quantitative negative-witness bound could connect a hypothesized
off-line zero in a specified region to a finite mixed test. It would
not prove the signs of those tests, exclude unbounded heights or resolve
RH. A weaker conditional bound must be recorded with its extra inputs.

## Original nomination instructions — retained as history

Start from L032 and L895's complete proofs only as needed, then search
specific local assessments/failures concerning effective witness degree,
Li detection and node clustering before primary comparison. Required
actual-Xi normalization inputs are L018/L024/L025/L026 and L030/C032a;
none of their hypotheses is replaced by a freely chosen node model.
No cross-notebook input is proposed. Mathlib matching coverage unchecked.

Continue only if coverage identifies an explicit applicable bound or a
bounded intermediate target with all extra assumptions stated. Retire
this nomination if the only available bounds require unavailable node
separations, reproduce the supplied-head certificate, or transfer Li
signs to mixed forms without justification. A failed search is neither
a nonexistence proof nor a reason to invent a degree bound. Any newly
ready mathematical continuation needs its separate approval next turn.

## Completed source comparison — step158

### Primary result, hypotheses and exact observable

[Palojarvi v2](https://arxiv.org/pdf/1807.01506v2), also inspected in
[versioned HTML](https://arxiv.org/html/1807.01506v2), assumes tau in [1,2),
zeros in 0<=Re rho<=tau, no zero rho=tau, and explicit two-sided counts
for both signs of the ordinate and for dyadic shells (Introduction,
assumptions (1)-(2), zero-based PDF pages1-2):

    |N_F(u)-A_F u log u-B_F u| < C_1 log u+C_2+C_3/u,
    |N_F(u,2u)-A_F u log u-(A_F log 4+B_F)u|
        < c_1 log u+c_2+c_3/u,                    u>=T_0.

Here A_F>0, B_F is real and the error constants are nonnegative.
Her coefficients are symmetric-height limits of
sum_[|Im rho|<=u] [1-(rho/(rho-tau))^n]. Theorem3.1 (PDF indices8-11)
states that, for R>1 and its explicit piecewise N (using W_{-1},
T_0, M_F and K_{F,2}(tau)), nonnegativity at all multiples of N in
[N,5N^2(A_F log N+M_F)] excludes |rho/(rho-tau)|>=R.
This is a cited statement, not a verified numerical specialization here.
At tau=1 the source identifies it with the usual zeta Li coefficients.
The constant factor in local xi does not affect logarithmic derivatives
of positive order. No L030 polynomial or degree occurs in this theorem.

### Essential proof cases read and qualifications

Theorem2.1 bounds the complete high-ordinate real tail at ne*tau
by K_{F,1}(tau)n log n; its proof sums all dyadic shells.
Theorem2.3 normalizes the head by its maximal Mobius modulus and applies
Lemma2.2 to N-th powers: max_[1<=k<=5M] Re sum_j z_j^k>=1/20
when max_j|z_j|=1. It allows repeated nodes, not merely separated ones.
Its cited original is P. Turan, *On a New Method of Analysis and its
Applications*, Chapter5, Theorem11; the book proof was not read.
Theorem3.1 combines low, intermediate and high ordinates, then checks
its two R regimes. The intermediate zeros are not discarded.
The head proof uses no simplicity or distinctness; counts and sums
must retain multiplicity. This is source interpretation, not a new
detector proof or a transfer between observables.

The v2 PDF and HTML both print M_F with C_2/e+C_2/3+C_3/9,
whereas the displayed count it is used to bound contains C_1 log N.
The later K_{F,2} comparison also changes a logarithmic constant to
an expression containing A_F log(5e*tau). These are unresolved
printed-constant/proof comparisons, not proved errors or repairs.
No zeta count constants were substituted and no corrected theorem is
asserted. The publisher PDF linked from the author's institutional
record was inaccessible at both host variants; shell curl lacked DNS.
Readable v2 suffices for this scope comparison. Retrying publisher access
or fixing constants is not the next task.

The introduction (PDF index1) reports that Brown's Theorem2, the opposite
zero-free-region to finite-Li-positivity direction, remains unproved
after errors in its supporting Lemma5. This is the author's report,
not an independent Brown audit. It does not invalidate every finite
Li detector. Brown's abstract and garbled author-copy PDF of
Bombieri-Lagarias are not theorem evidence imported here.

### Local duplicates, other leads and source limits

Canonical L032 has degree N+|E|-1 and tail error C^2 T 4^(-N),
with C depending on its head. Canonical audited L895 explicitly retains
the head, conditioning factors, full tail and multiplicities. Neither
is a T,delta-only bound. L057 lets off-line heights vary with the number
of tests; it is not an obstruction to a height-dependent cutoff.
The 31 October disk-Hardy witness assessment concerns a centered D_1
and supplied boundary norm; the 26 October product-tail assessment only
mentions Li as a different observable. Neither supplies this conversion.

A further primary lead, bramble_trace,
[*Quantitative negative tests for the Weil form near the height
horizon*](https://rstation.ai/problems/riemann_hypothesis/papers/28),
v1 (19 October 2026), Theorems1.1-1.4 and Section2, was inspected at
statement/normalization level only. Its compact smooth tests, complete
geometric Weil form and extra height/slack hypotheses do not give an
L030 polynomial degree. Its proof is unread and no result is imported.
The contour-Hankel scope was already compared in step157; no new source
read or global-tail conversion is claimed. Grommer references and
asymptotic Li papers remain leads, not quantitative substitutes.

Queries included effective/quantitative Li criterion with finite indices,
negative Li coefficient polynomial/Hankel, reciprocal-zero Hankel
effective degree, Grommer quantitative nonreal zeros, and Li criterion
polynomial approximation. Secondary summaries located sources only.
No exact matching theorem was found in this bounded search; this says
nothing about novelty or nonexistence. Mathlib full match is unchecked.
No cross-notebook theorem was read.

### Decision

This is an informative failure of direct source import, not a negative
mathematical answer to D(T,delta). Do not relabel a Li index as a mixed
degree. The next review isolates the transfer by supplying n, a certified
negative margin epsilon and A>=sum_j|beta_j|. Those are additional
hypotheses, not proved inputs. It asks for explicit degree and complete
error control with L026 geometry, including accumulation at beta=0.
The effective Li window/constants, supply of these data from T,delta
and actual-Xi mixed signs remain independent obligations. No kernel
identity, witness, estimate, lemma or mathematical script was derived.
