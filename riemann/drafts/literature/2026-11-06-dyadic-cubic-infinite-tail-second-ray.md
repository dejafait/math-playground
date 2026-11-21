# Dyadic cubic infinite tail — second-ray source comparison

TARGET: Test whether F(z)=product_(j>=0)P(2^(-j)z), P(w)=1+2w+2w^2+w^3, has det([z^(2+j-i)]F)_(0<=i,j<r)>=0 for every integer r>=1, with negative-index coefficients zero.
CHECKED: 2026-11-06
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Bounded exact-polynomial/dyadic-product and stronger-result searches under rectangular Schur positivity, reciprocal q-products, coefficient log-concavity and convolution found no inspected exact-family all-rank sign theorem. Checked L840/L841, the first-ray and all-fixed-shifts assessments, and the finite-class and generic-log-concavity stops; details below. Search failure is not a novelty claim.
SOURCE_EVIDENCE: Reuse Macdonald (1995), I.2 (2.4)–(2.6)/(2.9), pp.20–23, I.3 (3.4)/(3.5)/(3.9), pp.41–42; McMullen (2025-12-02), compact-product criterion/Theorem3.1 p.80 and Cauchy formula/bound pp.12–13; DLMF 17.2.4, 17.5.1/.2/.4 as inspected in the first-ray assessment. Newly inspected Johnson–Goldschmidt author preprint (2005-10-12), Theorems1.4/1.5 and Condition1 pp.2,4–5, Lemma4.3 and proof pp.12–13; Gross–Mansour–Tucker–Wang author draft (2015-01-20), Section1.2 p.3 and Section2 p.5, explicit no-internal-zeros convolution statement.
COMPARISON: Universal rectangular Jacobi–Trudi identities and compact coefficient transfer are covered; the family-specific second-ray sign is not. Scalar coefficient nonnegativity from L841 does not supply a higher minor. Standard log-concavity convolution with no internal zeros is not automatic transfer for L841's gapped factor reciprocals. Finite L840 palindromicity and finite PF order do not state the infinite all-rank conclusion.
GAP: In a later mathematical step check the exact rectangular index/ordinary-coefficient correspondence, obtain certified coefficients from the defining product using finite coefficient operations and the covered analytic passage, and decide the second-ray signs including zeros. No second-ray determinant, recurrence, sign certificate, negative minor or asymptotic has been derived in this review. Actual-Xi signs and realization remain independent.
REASON: Known algebraic and analytic methods cover the necessary operations; only the exact-family sign specialization remains. One bounded coefficient/determinant test is justified without an essential unread source, reproof of universal identities or reopening general meromorphic asymptotics. This assessment does not assert that the specialization succeeds.
LITERATURE_REASON: Shift two is outside the prior first-ray assessment; essential higher-rectangle/convolution comparison was missing. That comparison is now completed and the next turn defaults to mathematics.
SCOPE: Exactly TARGET, ordinary coefficients, q=1/2, weak inequalities, all integer ranks r>=1. Approves known-identity specialization, exact coefficient computation with justified analytic passage, and an all-rank argument only within this coefficient method. Excludes automatic higher-ray/PF closure, strict signs, higher shifts, new pole asymptotics and Xi transfer.

## Purpose, overlap and retained stops

The main gap remains L030–L032/C032a actual-Xi all-degree mixed
positivity. This intermediate test discriminates whether the infinite-tail
weak-ray model survives its next necessary shift. One rigorously negative
determinant rejects this family's all-shift ansatz; a positive answer only
preserves that possibility. Every k>=3, strict signs, useful Xi growth,
realization and actual-Xi signs remain independent.

L840 at m=1 is the audited finite input. Its first and second rays agree
by finite cubic palindromicity; this is not a statement about the infinite
product. L841 proves entire convergence, F(0)=1, a reciprocal disk |t|<1,
fixed-coefficient limits and the infinite first ray. Its independent audit
is pending. L841 (3) records periodic zero classes 4 and 5 modulo6 in
individual reciprocal coefficients. Retain these cases without inferring
any second-ray sign. No second-ray calculation was performed here.

The first-ray assessment inspected the general algebraic and analytic
sources, not just a single-row statement. Reuse its coverage. The
all-fixed-shifts assessment and
`ATTEMPTS/2026-11-06-all-fixed-shift-weak-detector-stop.md` retain the
finite tied-modulus obstruction. Bultheel's persistent source blocker
belongs to the parked general meromorphic-asymptotics approach; it was
not retried. The independent coefficient test needs no such theorem.
The generic infinite-log-concavity stop in
`ATTEMPTS/2026-11-04-generic-infinite-log-concavity-edge-sign-stop.md`
concerns other sequences and higher minors; it neither proves nor
refutes TARGET. No cross-notebook theorem is proposed.

## Primary theorem scope

**Universal identities and analytic passage — reused.** I. G. Macdonald,
*Symmetric Functions and Hall Polynomials*, second edition, Oxford (1995),
[primary book PDF](https://math.berkeley.edu/~corteel/MATH249/macdonald.pdf),
I.2 (2.4)–(2.6), (2.9)/(2.9'), pp.20–23; I.3 (3.4)/(3.5), pp.41–42.
The two Jacobi–Trudi formulas hold for arbitrary partitions in elementary
and complete homogeneous functions, with h_0=e_0=1, negative subscripts
zero and H(t)E(-t)=1. They are polynomial identities allowing complex
numerical specialization. They need neither positive real variables nor
nonzero solid minors. They give no positivity conclusion for the complex
alphabet here. A later application must check the rectangle, conjugate
partition, matrix orientation and rank explicitly. No universal reproof
is needed.

C. McMullen, *Advanced Complex Analysis*, notes of 2 December 2025,
[primary PDF](https://people.math.harvard.edu/~ctm/home/text/class/harvard/213a/25/html/home/course/course.pdf),
compact-product criterion/Theorem3.1 p.80 and Cauchy formula/bound
pp.12–13. Reuse the first-ray assessment and L841's explicit hypothesis
verification. Compact convergence and a nonvanishing reciprocal disk
permit fixed Taylor-coefficient passage, and a fixed finite determinant
is a polynomial in finitely many coefficients. This gives no uniform
rank limit. A numerical truncation later needs a complete error bound.
The already inspected [DLMF product definition](https://dlmf.nist.gov/17.2.E4)
and [Euler/q-binomial identities](https://dlmf.nist.gov/17.5) provide
optional coefficient descriptions for |q|<1, with the reciprocal Taylor
series restricted to |z|<1. They supply no rectangular sign theorem.
No family-specific factorization or recurrence was derived in this turn.

**Convolution and support qualifications — newly inspected.** Oliver
Johnson and Christina Goldschmidt, *Preservation of log-concavity on
summation*, author preprint dated 12 October 2005,
[primary PDF](https://www.stats.ox.ac.uk/~goldschm/logconcavity.pdf);
published ESAIM Probability and Statistics10 (2006), 206–215,
DOI10.1051/ps:2006008. Preprint Theorem1.4 p.2 states convolution
preservation for independent log-concave variables. Theorem1.5 requires
a log-concave input and Condition1's two families of partial-sum
inequalities (pp.4–5), not just nonnegative coefficients. Lemma4.3 and
its complete proof pp.12–13 give a sufficient adjacent-ratio bound for
geometric smoothing and an obstruction for an isolated support gap,
using equations(10)–(12). The ratio hypothesis must be defined and
verified. Do not extend its stated isolated-gap condition to L841's
two-zero blocks without an argument. Theorem4.4's monotonicity statement
and proof were also read; no required geometric decomposition has been
established here. These statements provide comparison, not target signs.

Jonathan L. Gross, Toufik Mansour, Thomas W. Tucker and David G. L.
Wang, *Log-concavity of combinations of sequences and applications to
genus distributions*, author draft dated 20 January 2015,
[primary PDF](https://www.cs.columbia.edu/~gross/research/LCGD-GMTW-SIDMA20jan15.pdf),
Section1.2 p.3 and Section2 p.5. The latter explicitly states convolution
closure for log-concave sequences **without internal zeros**, citing
Cauchy–Binet and Stanley Proposition2. It distinguishes ordinary
convolution from the Hadamard product. This qualified statement supplies
no automatic closure for L841's gapped reciprocal factors. It does not
assert that smoothing is impossible. Graph-specific results and
synchronization criteria are not imported. Stanley's original proof
is an unread reference, not an essential input to this coefficient test.

## Search and comparison limits

Exact-family queries included “1+2x+2x^2+x^3 infinite product determinant”,
“1+2z+2z^2+z^3 infinite” and “dyadic cubic Toeplitz product”. Stronger-result
queries included “q-products coefficients log-concavity”, “Toeplitz
determinants rectangular Schur two column log concavity convolution q
products”, “q-product rectangular Schur positivity complex variables”
and “log concave sequences convolution no internal zeros theorem”. They
led to the primary sources above, general q-products, finite-band
identities and unrelated q-Turan inequalities. No inspected result
states TARGET. Snippets, secondary summaries and unrelated preprint
leads were not theorem evidence. There is no novelty inference.

Reuse the all-fixed-shifts assessment's inspected comparisons with
PF-infinity and strict solid-minor criteria. Those require stronger
premises. Weak zeros cannot be removed, and finite PF order does not
supply unbounded-rank signs. No essential unread source blocks the
proposed coefficient test. Full matching Mathlib coverage is unchecked;
no absence claim is made.

## Approved bounded continuation

Keep exactly TARGET for the next mathematical step. Apply the cited
universal identities, verify the higher rectangle and obtain exact or
rigorously bounded coefficients from the defining product. Reuse
L840/L841's analytic scope with L841's audit qualification explicit.
Prefer this coefficient construction to general determinant asymptotics.
Do not create a lemma merely to restate a universal identity.

One rigorously negative minor decides the test negatively. A positive
answer needs every r>=1, equality cases and the necessary limit
justification. Finite positive samples, decimal signs without error
bounds, division by zero minors and multiplication of weak solid-ray
signs are insufficient. If this coefficient method leaves a sign or
remainder uncontrolled in the bounded step, save the precise obstruction
and stop it. No new pole mechanism is approved under this assessment.

SPECIALIZE approves a known-method applicability test, with REPRODUCTION
classification for those standard operations. It neither imports the
unproved sign nor certifies originality. The original nomination is
preserved verbatim in
`drafts/2026-11-06-dyadic-second-ray-source-nomination.md`; the working
record is `drafts/2026-11-06-dyadic-second-ray-source-working.md`.
This is source coverage only, with no mathematical advance claimed.
No justified creative central-Xi mechanism is ready: an independent
signed Xi input remains missing. Do not relabel this model specialization
as creative to meet a routing target.
