# Position-sensitive logarithmic gcd coercivity — source comparison

TARGET: Review source coverage for F_(log N)(c)>=-C Q(c) with one absolute C>=0 for all integers N>=2 and complex c, testing whether the d-dependent weighted rows and exact columns in L924 admit a quadratic-form bound at this smaller coefficient.
CHECKED: 2026-11-09
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step231 searched the signed linear-log gcd form, logarithmic gcd positivity, weighted Schur estimates and Gershgorin diagonal similarity; reused the November9 critical/row/audit comparisons and checked local logarithmic-gcd notes/history/stop for duplicates. Queries and inspected-versus-unread leads are recorded below; no novelty inference is made.
SOURCE_EVIDENCE: Leitner, CO-MAT2 Lecture Notes WS2013/14, Section1.1.1 Theorem1.1.3 printed p2, complete proof and preceding similarity statement; Bindel, CS6210 (2025-11-03), Symmetric eigenvalue basics and Variational approaches, Hermitian hypotheses and complete Rayleigh weighted-average argument. Reuse Tao Notes1 Section2 Theorem13 eq(22) through L924 (4)-(7); sources and qualifications below.
COMPARISON: The inspected named matrix theorems cover finite complex matrices, diagonal similarity and Hermitian quadratic-form bounds. They permit a later application to the Hermitian part of L924's finite matrix, retaining the index-dependent information lost by its global norm estimate. No inspected arithmetic theorem states F_(log N)>=-C Q; the scalar input and older gcd-spectrum comparisons remain adequate within their original scope.
GAP: The application must still establish the required all-N quadratic-form inequality, verify the weighted transpose orientation and factor of two, and retain empty rows, complex coefficients and kappa. This literature turn establishes no improved coefficient, margin, conditioning, moment or Xi-sign conclusion.
REASON: Essential source comparison for the changed coefficient is complete for the single COVERED_TARGET. Import the named matrix theorems and L924's proved scalar estimate; only their finite arithmetic application remains. The newly ready continuation receives separate approval next turn.
SCOPE: All N>=2, arbitrary complex vectors, natural logarithms, unchanged full F_A and Q, real cutoffs, kappa contribution and both cross terms. No new multiplier-length theorem, moment estimate, inverse-Gram bound, theta realization or Xi sign is proposed.
COVERED_TARGET: Specialize the cited Gershgorin and Hermitian Rayleigh bounds using L924's position-dependent rows and exact columns to prove F_(log N)(c)>=-C Q(c) for one absolute C>=0, all integers N>=2 and complex c, retaining kappa and all real cutoffs.

## Invocation-start nomination (preserved)

The following nomination described the uncovered target at invocation start.
Its review requirement is discharged by the source comparison below,
without proving the proposed arithmetic inequality.

The main gap remains L030-L032/C032a actual-Xi all-degree mixed
positivity. The nomination is an intermediate arithmetic question,
motivated by the d-dependent row information already displayed in
L924 (7), rather than another finite spectral grid. A stronger lower
bound at a smaller coefficient could give a logarithmic main-term
margin at the old coefficient. This could inform later observer norm
estimates; it does not justify longer multipliers without their moment
and conditioning estimates. No such strengthened bound or margin is
established in this nomination.

Review the exact assertion and stronger known logarithmic gcd-form
bounds, reusing the November9 source comparisons wherever their
hypotheses agree. Retrieve the hypotheses and relevant proof of a
standard weighted quadratic-form/Schur estimate if that is the needed
new interface. Compare it with the actual finite rows and columns,
without deriving a new arithmetic conclusion this literature turn.
If existing sources cover the assertion, import precisely; otherwise
identify only the required specialization and authorize a later
bounded proof attempt. Do not infer novelty from a failed search.

Continuation test: a separately assessed finite argument must cover
the same C for every N and complex vector, including all real and
empty cutoffs. A demonstrated failure of that interface or a rigorous
counterfamily changes the route; finite positive trial values do not
approve the inequality. The earlier dyadic-pilot stop is preserved.
The proposed use of the d-dependent information is distinct from
enlarging that grid or repeating L924's completed norm audit.

Essential local inputs are L737's finite identities and L924's scalar
row bound, exact column identity and step230 audit. No analytic part
of L737 is assumed. Source moment errors, conditioning, microscopic
realization and signed transfer remain independent open requirements.
No cross-notebook input is proposed. Full matching Mathlib coverage
is unchecked.

At nomination this was not ready coverage or a mathematical result.
The nominated task was literature_comparison/standard/high. A central
creative attempt is not yet justified: this audit supplies no new
actual-theta or signed-realization premise. Do not label this routine
arithmetic refinement creative to satisfy a scheduling target.

## Completed comparison — 9 November 2026, step231

### Relevance, reuse and recorded failures

The main gap is L030-L032/C032a actual-Xi all-degree mixed positivity.
The intermediate target remains precisely the smaller-coefficient,
all-N complex quadratic-form bound in TARGET. It could improve an
arithmetic main-term margin for future observer estimates. Moment
errors, coefficient conditioning, realization and signed transfer
are independent open steps; no multiplier length or RH conclusion
follows from this comparison.

Read L924 in full, including step230, and L737's finite (5)-(11).
Reused the November9 critical-coercivity and row-sum assessments:
their primary Mertens inspection and the checked gcd-spectrum
comparisons are unchanged. A targeted search of the November9
logarithmic-gcd assessments, working notes, histories and ATTEMPTS
found the nomination but no all-N proof at log N. The step226 pilot
already used a symmetric numerator to select trials; symmetrization
itself is therefore not a new local device. Its positive trial values
do not bound spectra. Read its pertinent coordinate description and
the preserved failure in
ATTEMPTS/2026-11-09-logarithmic-gcd-dyadic-pilot-inconclusive-226.md.
The proposed analytic use of index-dependent rows differs from
enlarging that parked grid. No certificates were needed or replayed.

The older assessment's comparison with bramble_trace paper41v3,
Section5 Lemmas4/5/5a, remains a scope comparison: fixed positive
shift or N^epsilon/inverse losses do not supply the proposed absolute
additive derivative bound. No unreviewed manuscript theorem is
imported. Yang, arXiv:2201.12968v3 Theorems1.1/1.2 and Sections4.2-4.3,
and Mathematika68(2022) Proposition2 concern product-log extrema or
different-exponent upper estimates. Their already inspected statements
do not cover this signed linear-log bound relative to Q. Reuse those
exact comparisons rather than rereading unchanged primary passages.

### Primary matrix input and precise import boundary

Daniel Leitner, *CO-MAT2 Lecture Notes*, Wintersemester2013/14,
Universitaet Wien, Section1.1.1,
[Theorem1.1.3 (Gershgorin circle theorem)](https://www.csc.univie.ac.at/files/Numerik_WS13-14/Lecture_Notes2.pdf),
printed p2 (PDF p6). Read the preceding similarity statement and the
complete theorem/proof. For every finite complex square matrix A,
each eigenvalue lies in some closed disk with center a_ii and radius
sum_(j!=i)|a_ij|. No symmetry, irreducibility or positivity is required.
The proof chooses a nonzero eigenvector component of maximal modulus;
its division is legitimate, and no strict disk or simple-eigenvalue
condition occurs. The preceding statement preserves eigenvalues under
any nonsingular similarity. Import these standard facts without
reproving them. No assertion from the later Bendixson discussion is
needed.

David Bindel, *CS6210: Matrix Computations — Theory for SEP and SVD*,
3 November2025,
[Symmetric eigenvalue basics / Variational approaches](https://www.cs.cornell.edu/courses/cs6210/2025fa/lec/2025-11-03.html).
Read the Hermitian hypothesis A=A*, unitary eigendecomposition, and
complete weighted-average argument for the Rayleigh quotient. For
finite Hermitian A and complex v!=0, v*Av/(v*v) lies between its
least and greatest eigenvalues. Repeated eigenvalues are allowed.
The ordinary Hermitian statement suffices; no generalized-denominator
conditioning or eigenvector-stability conclusion is imported.

These inputs cover the linear-algebra techniques for the requested
application. Gershgorin alone would bound eigenvalues of a nonnormal
matrix, not its numerical range. A later proof must apply it through
the actual Hermitian matrix and use the Hermitian Rayleigh statement.
Diagonal similarity preserves spectra, not Euclidean quadratic forms;
the similarity-transformed matrix must not simply be treated as
Hermitian. This distinction is an essential application check.

L737 already contains a full finite weighted Schur proof for complex
vectors. It may be reused within its hypotheses; no new general
Schur lemma is needed. The newly inspected Gershgorin statement
provides an alternative named theorem for the position-dependent
application, not an independent arithmetic estimate.

### Exact finite interface still to be specialized

The following information is quoted from existing canonical proofs;
it is not a new quadratic-form calculation. In L924 (5)-(7),

    y_d=sqrt(phi(d)) B_d,   Q=||y||_2^2,
    K_(d,n)=Lambda(n/d)sqrt(phi(d)/phi(n)) for d|n, n>d,
    K_(d,n)=0 otherwise,   h_d=1/sqrt(phi(d)),
    sum_n K_(d,n)h_n/h_d <= log(N/d)+C_*,
    sum_d K_(d,n)h_d/h_n = log n,
    F_A=sum_d (A+2*kappa(d))|y_d|^2-2 Re sum_d (Ky)_d conjugate(y_d).

Here C_*=M+3 log2+2 is already an absolute nonnegative constant,
valid at every real cutoff, and every h_d is strictly positive.
The scalar Mertens source is Tao, *254A Notes1*, 23 November2014,
[Section2 Theorem13, eq(22)](https://terrytao.wordpress.com/2014/11/23/254a-notes-1-elementary-multiplicative-number-theory/).
Reuse its complete inspection in the row-sum assessment and its
denominator specialization proved in L924; no new Mertens proof,
constant optimization or Goldfeld extraction is required.

The later application should examine the Hermitian part of K with
the same positive weights before replacing individual indices by
global maxima. It must establish, rather than assume, that the
resulting bound pays the cross term at coefficient log N with only
an absolute additive remainder. Verify the transpose weights, the
factor of two in the real part, the diagonal contribution, and the
return from y to arbitrary complex c. Retain kappa until a justified
lower bound; treat c=0 without division. L737 inversion and L924
already ensure Q>0 for nonzero c, without a uniform condition number.
Empty rows and the zero column must remain included.

This is the precise unproved specialization in COVERED_TARGET.
No row/column combination, new bound for the Hermitian part, final
constant at log N or arithmetic conclusion is derived in this turn.
Source coverage supports a finite theorem-application attempt,
classified REPRODUCTION; it does not certify success or originality.

### Search scope, other leads and coverage qualifications

Queries included `"logarithmic" "gcd" "quadratic" lower bound`,
`"gcd" "log" "log N" positive definite logarithmic matrix`,
`"logarithmic gcd" quadratic forms`,
`"gcd" "log(m" "log(n" quadratic`,
`"gcd" "log" "lcm" "quadratic form" lower`,
`"logarithmic gcd" "positive" kernel`,
`Schur test symmetric kernel quadratic form proof lecture notes pdf weighted`,
and `Gershgorin theorem weighted row sums diagonal similarity proof lecture notes`.
Exact searches did not locate a matching all-N signed arithmetic theorem.
This is a bounded comparison, not an exhaustive literature or priority claim.

One newly inspected near-name match is Grand Challenge Labs,
[*The logarithmic GCD kernel*](https://grandchallenge.github.io/MATH-PROGRAMME/LOG_GCD_PUBLICATION/),
publication record dated23 July2026, sections The claim and Why the
quadratic form is nonnegative. It states positivity for log(gcd(m,n))
on positive integers with real coefficients, with a von Mangoldt
divisor Gram representation. That is a different kernel, without our
gcd/sqrt(mn) factor and signed log m/log n terms. It does not state
the present bound. Its formal-certification claims were not replayed
or adopted as Mathlib coverage; no theorem from this page is imported.
The separate LOG_GCD_KERNEL URL failed to open, but the publication
page supplies the compared claim; this is not an essential blocker.

Other search results, including Berezhnoi-Maligranda on Schur-test
limits and diagonal-scaling refinements, remain unread leads and are
not premises. A guessed Vienna functional-analysis PDF URL returned
404; it is unused. The two fully inspected matrix sources and the
existing finite Schur proof suffice for the scoped continuation.
No relevant source change invalidated the reused scalar assessment.

Full matching Mathlib coverage remains unchecked, not absent.
This turn changes no lemma, mathematical script, DAG edge or argument
in PROOF.md. No cross-notebook input was used.

Continuation test: a later proof must give one C independent of N and
c for the full form, including all prime powers and real/empty cutoffs.
If the actual weighted Hermitian interface cannot meet the coefficient,
record its exact failure; an obstruction to this interface alone does
not refute the inequality. A rigorous unbounded negative family would
abandon the inequality; finite trials decide neither alternative.
Do not repeat the pilot or continue with an uncovered replacement.

Outcome: LITERATURE / EXPLORATION / NOVELTY_UNCHECKED. Essential
comparison is complete for one bounded specialization, with the
arithmetic assertion still open. The next task is calculation/standard/high
for a routine finite application. A justified central creative target
is still blocked by missing actual-theta/signed-realization input;
this arithmetic refinement is not relabeled creative for scheduling.
