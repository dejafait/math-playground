# Zero-conditioned pair mass: source notes

Working checkpoint saved during the literature-only step, 28 October
2026; the completed comparison below supersedes its pending-source
language. No bound or new
identity has been derived. The target remains the restricted L471
pair sum and an epsilon-uniform positive power at scale T(log T)^3.

Inspected primary statements:

- Carl de Boor, *Divided Differences*, Surveys in Approximation
  Theory 1 (2005), 46--69, Section 9, contour and Genocchi--Hermite
  representations: https://surveys-in-approximation-theory.com/papers/2/2.pdf.
  Complete relevant complex-node and coalescence cases still being read.
- S. J. Kirila, arXiv:1804.08826v1, Theorems 1--2 and Corollary 3:
  https://arxiv.org/html/1804.08826v1. These assume RH; they are
  unavailable as unconditional inputs to an off-line-pair estimate.
- Durkan--Hughes--Pearce-Crump, arXiv:2601.06292v1, (1.1) and
  Theorem 1/(2.1): https://arxiv.org/html/2601.06292v1.
  The unconditional result concerns the reflected bilinear product,
  not the off-line absolute-square sampling required by L471.
- Bettin, arXiv:1111.0925v1, Theorem 1:
  https://arxiv.org/html/1111.0925v1. Already covered locally in
  drafts/literature/2026-10-28-two-height-hardy-jet-moment-coverage.md;
  reuse its small-complex-shift qualifications, rather than reprove it.

The ordinary-moment and finite-law stops remain intact. A possible
continuation would combine zero-conditioned interpolation with local
finite Blaschke factorization to test cluster suppression before
summation. That is a proposed test, not a proved sampling theorem or
an approved new target. The primary factorization passage and its
scope must be checked before finalizing the assessment.

Final source comparison and the sole continuation will be recorded
in drafts/literature/2026-10-28-zero-conditioned-small-displacement-coverage.md
and PROGRESS.md, respectively. No lemma/script or proof assembly edit
is authorized in this turn.

## Completed primary-source comparison

### Interpolation

Carl de Boor, *Divided Differences*, Surveys in Approximation Theory
1 (2005), 46--69, [Section 9, (50)--(52), pp. 62--64](https://surveys-in-approximation-theory.com/papers/2/2.pdf#page=17).
Read the full contour and Genocchi--Hermite passages, including complex
sites and repeated interpolation. The contour representation requires
holomorphy on a larger disk and a smaller enclosing circle with no
nodes in the intervening annulus. The simplex formula integrates the
nth derivative over convex combinations of its nodes. These are
classical formulas, including confluent data. Xi is entire, but its
zero-conditioned specialization and uniform summed estimates remain
research work. A real mean-value theorem for complex nodes is not
licensed. No sampling bound or epsilon exponent is supplied.

### Finite zero factorization

Kevin Broughan, *Equivalents of the Riemann Hypothesis*, Volume Two:
*Analytic Equivalents*, Cambridge (2017), [Theorem 3.3, proof (1),(4),
pp. 26--27](https://api.pageplace.de/preview/DT0400.9781108195430_A31720577/preview-9781108195430_A31720577.pdf#page=48).
Read the complete finite-factor and central-zero cases. Dividing a
bounded holomorphic function on the unit disk by a finite Blaschke
product of its zeros leaves a holomorphic quotient with the same
supremum bound. Multiplicity repeats the factors; central zeros use
powers of z and Schwarz's lemma. Only that finite statement is
proposed as an input, not the entire infinite-factorization proof.
No separation is required, but no summed quotient estimate follows
as a quoted theorem. Apply on compact local disks, never by assuming
Xi globally bounded. The new question is whether keeping the other
nearby zero factors offsets cluster occupancy before covering the
height interval. That compensation is unproved here.

### Positive discrete moments

Kirila v1, [Theorems 1--2 and Corollary 3](https://arxiv.org/html/1804.08826v1),
read together with J_k's definition: Theorem 1 has exponent k(k+2)
for k>0; Theorem 2 permits complex shifts of modulus <=1/log T;
Corollary 3 has exponent k(k+2nu) for nu>=1 and k>1/2.
All assume RH. None can be an unconditional input for hypothetical
off-line pairs, and none states the pair-divided short-window bound.
The full arithmetic proofs were not audited: the stated hypothesis
already prevents the proposed import.

### Unconditional reflected moments

Benjamin Durkan, Christopher Hughes and Andrew Pearce-Crump,
*The discrete second moment of mixed derivatives of the Riemann zeta
function*, [arXiv:2601.06292v1, 9 January 2026, (1.1), (1.3),
Theorem 1/(2.1), pp. 1--3](https://arxiv.org/pdf/2601.06292v1#page=2).
Read the defining sum, its stated RH specialization and all theorem
hypotheses/error alternatives. For positive integers mu,nu the
unconditional summand is zeta^(mu)(rho) zeta^(nu)(1-rho), with a
degree mu+nu+2 polynomial main term and O(T exp(-C sqrt(log T)))
error; RH permits O(T^(1/2+delta)). The source restricts its
absolute-square interpretation to RH. Off the line 1-rho is not
conjugate(rho). Thus no positive quotient-square bound is imported.
No full proof audit is needed to identify this statement mismatch.

### Continuous microscopic moments and gamma factors

Reuse [the paired-height assessment](literature/2026-10-28-two-height-hardy-jet-moment-coverage.md),
whose Bettin source scope is unchanged. Sandro Bettin,
*The second moment of the Riemann zeta function with unbounded shifts*,
[arXiv:1111.0925v1, Theorem 1, p. 2, small-shift completion pp. 9--10](https://arxiv.org/pdf/1111.0925v1#page=2),
allows Re a,Re b=O(1/log T), with error
O((sqrt(T)+sqrt(|Im a|)+sqrt(|Im b|))log^2 T).
The two main terms have a combined limiting interpretation at a=b;
do not split the poles. Deterministic bounded microscopic complex
shifts are covered, not shifts chosen at zeros. Any area/contour
integration, endpoint control and gamma-normalized specialization
still need justification in research. Use L465 Sections 1--2 and 5
for analytic prefactors and sector estimates. A(t) from L471 is a
real-height normalization, not a holomorphic modulus of Gamma.
No new moment application has been performed here.

## Bounded search and duplicate/failure comparison

Queries included `Carl de Boor divided differences Genocchi Hermite
formula complex nodes pdf`, `unconditional upper bounds discrete
moments zeta derivatives zeros multiplicity fourth moment`, `zeta
function divided difference conjugate zeros moments derivative off
critical line`, `zeta Blaschke local zeros mean square`, `zeta pair
quotient Blaschke moments`, and `holomorphic zeros divided differences
sampling inequality`. Quoted divided-difference/zero-conditioned,
stronger-result and 2024--2026 discrete-moment variants were screened.
No inspected theorem matches B_epsilon; no novelty is inferred.

Local searches in drafts/literature, ATTEMPTS and foundations found
no previous de Boor/Genocchi/Blaschke or named discrete-source assessment.
Bettin already has adequate local coverage and is reused. L471's
complete relevant argument and both nominated ATTEMPTS records were
read: ordinary fourth moments lose d^(-3/2), while L473's specified
finite moment constraints lack actual zero conditions. Retain both
stops. The proposed cluster-aware aggregation is not another copy of
the ordinary-moment substitution or finite-law test.

Unread/unimported adjacent leads: Christ--Kalpokas, *Upper bounds for
discrete moments of the derivatives ... on the critical line* (2012);
Garunkstis--Steuding, *Simple zeros and discrete moments ...* (2005),
[DOI 10.1016/j.jnt.2004.12.006](https://doi.org/10.1016/j.jnt.2004.12.006),
including a real-gap theta^3 estimate exposed by search. Publisher
full text returned 403; the indexed mirror returned a bot challenge.
Its full theorem/proof was not read. Do not import snippet constants
or infer a complex-quotient extension. Neither is essential to the
independent finite-disk test. Other 2026 search-result claims were not
treated as primary theorems. These limited access failures do not
establish a persistent blocker for the independent test.

No cross-notebook input was used. Full matching Mathlib coverage was
not checked; unknown availability is not absence.

## Decision and limits

The review supports one EXPLORE continuation using accessible classical
interpolation/factorization and the already assessed continuous moment
input. It does not supply a bound or alpha>0. Research must test
cluster/multiplicity aggregation without an extra logarithm and with
uniform constants for every 0<epsilon<=1. Begin with the cubic power
suggested by L471's existing weight only as an unproved test; any
rigorous fixed positive exponent at the required scale would count.
An epsilon-dependent constant, fixed-epsilon asymptotic, assumed sparse
microscopic count or bound at T(log T)^(3+delta) does not meet it.
Success still leaves the complementary sector, full N(T) saving,
individual-height signs and global mixed positivity open. The proposed
research assessment requires separate approval next invocation.
