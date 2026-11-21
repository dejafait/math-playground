# Nomination: coefficient conditioning for the unweighted gcd form

TARGET: Review and assess source coverage for Q(c)>=a_epsilon N^(-epsilon)||c||_2^2 for every epsilon>0, one a_epsilon>0 uniform in N>=2 and complex c, starting with paper41v3 Section5 Lemma5 and its cited inputs.
CHECKED: 2026-11-09
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step235 checked the exact endpoint inverse lead, general smallest-eigenvalue comparisons and primary divisor/totient/Schur inputs; detailed reads and limits below. The improvement is already claimed explicitly in the inspected manuscript, so a new-result route is unnecessary.
SOURCE_EVIDENCE: paper41v3 (5),(19),(20),(26),(27), entire Lemma5 proof; Aistleitner-Berkes-Seip arXiv:1210.0741v5 Section4 Theorems5/6 and (23); Tao 2008 divisor bound (3) and both prime cases; Rosser-Schoenfeld 1962 Theorem15 (3.41)-(3.42), pp71-72 and Section9; Grafakos-Torres 2000 Section2 classical Schur theorem p2.
COMPARISON: The endpoint inverse claim covers the desired coefficient loss in the correct finite normalization, including complex vectors; generic positive-shift and arbitrary-index bounds alone are insufficient. Reproduce only the finite endpoint specialization using precise standard inputs because the immediate manuscript is unreviewed.
GAP: No essential source is blocked. The finite proof, exponent allocation and all-small-N constants still need canonical mathematical verification; no new coefficient inequality is established in this literature turn. Moment errors, realization and Xi signs remain independent.
REASON: Exact overlap changes the continuation from developing an uncovered conditioning estimate to a bounded reproduction. The separate continuation assessment names that verification; no longer-multiplier or analytic application is approved.

## Invocation-start nomination (historical)

The main gap is L030-L032/C032a actual-Xi all-degree mixed positivity.
The intermediate question is whether known endpoint gcd-matrix bounds
replace L737's crude conditioning loss by the stated subpower loss.
The exact Q is sum_(d<=N)phi(d)|sum_(k<=N/d)c_(dk)/sqrt(dk)|^2,
with arbitrary complex c and natural-number indices. This is the
unchanged Q in L737, L924 and audited L925; no new form is proposed.

A reliable coefficient lower bound could later help compare L925's
arithmetic margin with a moment error measured in ||c||_2^2. It alone
would not supply a longer-multiplier projection result, local numerator,
realization, signed transfer or positivity. Those separate inputs and
their ranges would need their own coverage before an application.
No improved conditioning inequality is derived in this nomination.

Start with the exact previously inspected lead: bramble_trace,
*Generalized Laguerre positivity at growing orders*, paper41 v3,
23 October2026, Section5 Lemma5,
https://rstation.ai/problems/riemann_hypothesis/papers/41/v3 .
The prior comparison read its definitions and proof, but treated it
as an unreviewed manuscript comparison rather than an established
input. Retrieve its exact theorem and load-bearing cited hypotheses
before reading larger passages. Check whether a standard primary
gcd-matrix theorem already supplies the requested bound. Distinguish
the unweighted endpoint from a fixed positive shift, an inverse norm
bound from individual-entry estimates, and constants uniform in N,c
from constants allowed to depend on epsilon. An epsilon loss is
explicitly permitted here; no absolute constant loss is sought.

Continue by recording IMPORT, SPECIALIZE or EXPLORE only if exact
hypotheses and supporting sources justify the corresponding next
target. If the lead needs an inaccessible essential result, record
SOURCE_BLOCKED and park its dependent application; do not repeat the
old signed-derivative search or enlarge the parked dyadic pilot.
An unrelated kernel or insufficient vector uniformity is evidence to
change the target, not an imported bound.

Essential inputs for later mathematics would include L737's finite
factorization/inversion and audited L925; the quantitative inverse
estimate is presently an unresolved assumption. No cross-notebook
input is proposed. Full matching Mathlib coverage is unchecked.

This is a literature_comparison/standard/high nomination, not a
creative central mechanism. The completed audit supplies no new
actual-theta or signed-realization premise to justify one; that
blocker stays explicit rather than relabeling this task.

## Completed source comparison — 9 November 2026, step235

This section supersedes the nomination's source-readiness statements.
No lemmas or mathematical scripts were written. The review preserves
the exact coefficient target and changes only its source coverage.

### Local comparison and failures

Read L737's hypotheses and finite (5)-(11), L925's hypotheses, the
critical-coercivity review's shifted-form comparison, and the November4
projection assessment's spectral comparison. L737 (11) is deliberately
crude. Neither it nor L925 duplicates a canonical subpower bound.
The parked step226 dyadic pilot concerns the different signed form;
its stop is preserved and gives no reason to enlarge that pilot.
No sibling notebook or cross-notebook result was used.

### Exact manuscript overlap and reliability

bramble_trace, *Generalized Laguerre positivity at growing orders*,
v3, 23 October2026, [Section5 Lemma5](https://rstation.ai/problems/riemann_hypothesis/papers/41/v3).
Read (5),(19),(20),(26),(27) and its complete proof. At shift zero,
its real matrix has entries B_0(d,n)=1_(d|n)sqrt(phi(d)/n), so its
F_a(0)=||B_0 a||_2^2 is exactly the local Q(a). The source explicitly
uses arbitrary complex vectors. Its shift variable c is unrelated to
the local coefficient vector c. Lemma5 states ||B_c^(-1)||^2
<<_epsilon N^epsilon uniformly for real shifts c>=0. The endpoint
therefore requires no limiting shift argument. Its proof uses finite
Möbius inversion, weights n^(-1/2), and divisor/totient bounds.
These standard inputs were not precisely cited there. The claim is
an exact known manuscript overlap, not a certified new estimate.
Only the endpoint will be reproduced; no analytic theorem, uniform
positive constant at epsilon=0, or shifted extension is imported.

### Primary scalar inputs

Terence Tao, [*The divisor bound*](https://terrytao.wordpress.com/2008/09/23/the-divisor-bound/),
23 September2008, equation(3), states tau(n)<=C_eta n^eta for
every eta>0, with C_eta independent of n. Read the whole proof of
(3), including the large-prime case and the finite-small-prime case.
This is a named standard input; its proof need not be repeated.

J.B. Rosser and L. Schoenfeld, *Approximate formulas for some functions
of prime numbers*, Illinois J. Math.6(1962),64-94,
[DOI10.1215/ijm/1255631807](https://doi.org/10.1215/ijm/1255631807),
[primary-paper scan](https://denisevellachemla.eu/Rosser-Schoenfeld-1962.pdf),
Theorem15, pp71-72, equations(3.41)-(3.42). Read the statement and
Section9 pp88-89, including the finite-range and large-n proof cases.
For n>=3, n/phi(n)<exp(gamma)loglog n+5/(2loglog n), except
n=223092870, where (3.42) uses 2.50637 in place of 5/2.
The exception must be retained; indices1,2 need separate treatment.
Only a non-effective subpower corollary is needed later, with constants
depending on the requested exponent. No explicit best constant or
uniformity as the exponent tends to zero is requested. This bound is
unconditional; its numerical constants need not be recomputed here.

### Primary matrix input and comparisons

L. Grafakos and R.H. Torres, *A multilinear Schur test and multiplier
operators*, author manuscript dated 9 February2000,
[Section2, classical Schur theorem, p2](https://grafakos.missouri.edu/preprints/multilinear_schur.pdf).
Read the complete classical statement (a)-(c) and its measure-space
hypotheses. It covers nonnegative kernels on sigma-finite spaces for
1<p<infinity. Finite counting measure and p=2 cover absolute inverse
entries. Positive weights and both weighted sums must be checked;
complex inputs are controlled by absolute values. This is an operator
norm test, not an entrywise eigenvalue inference. L737 already contains
the finite weighted Cauchy-Schwarz proof, which may be reused.

C. Aistleitner, I. Berkes and K. Seip, *GCD sums from Poisson integrals
and systems of dilated functions*, JEMS17(2015),1517-1546,
[arXiv:1210.0741v5](https://arxiv.org/pdf/1210.0741v5), Section4,
Theorems5/6, printed pp15-17. Read their definitions, (23), both
statements and Theorem6's complete proof. Theorem5 is an upper spectral
bound; Theorem6 gives a lower product over the first N-1 coordinates
for arbitrary distinct multi-indices and a decreasing positive sequence
in the infinite unit polydisk. It does not itself state the requested
natural-prefix subpower lower bound. No inference from an upper norm
to a lower eigenvalue is used. Reuse the earlier Lindqvist-Seip
s>1 comparison unchanged; it neither covers nor refutes this weaker
finite endpoint target. The 2009 Hilberdink and inverse-GCD papers
remain background leads, not imported theorem statements.

Queries included `gcd matrix gcd(m,n) sqrt mn smallest eigenvalue
Lindqvist Seip inverse lower bound`, `Hilberdink arithmetical mapping
smallest eigenvalue gcd matrix inverse 2009`, `divisor bound d(n)
O epsilon n epsilon totient n phi(n) log log theorem primary notes`,
`Rosser Schoenfeld 1962 theorem 15 n phi n pdf`, and `weighted Schur
test positive weights matrix operator norm lecture notes theorem`.
A guessed Tao operator-notes URL was inaccessible; the inspected
Grafakos-Torres statement removes that nonessential access issue.
DLMF27.2 was inspected only for notation, not as a spectral theorem.
Search results and abstracts alone were not accepted as theorem evidence.

### Decision and bounded continuation

SPECIALIZE authorizes a later finite reproduction of the endpoint claim,
with hypotheses N>=2 and arbitrary complex vectors. The extra work is
justified by the unreviewed immediate source and its compressed standard
input citations. It must track the squared inverse norm, positive
weights, all exponent losses, cutoff1, and constants independent of N
and the vector. It must not reprove the general scalar or Schur theorems.
If any unavoidable fixed power of N remains, report the mismatch and
stop this claimed specialization. Otherwise record it as reproduction,
then assess any analytic use separately. No mathematical derivation or
numerical test was made here. Full matching Mathlib coverage is unchecked.

The continuation is saved separately in
drafts/literature/2026-11-09-gcd-coefficient-conditioning-reproduction.md
for the supervisor's separate approval. No concrete actual-theta or
signed-realization premise has emerged to justify a creative central
attempt; that blocker remains explicit. No exploration counter is reset.
