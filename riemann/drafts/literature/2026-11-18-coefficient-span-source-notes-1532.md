# Coefficient-span source ledger1532

18 November 2026. Literature only. Assessment1531's exact target is
uniform approximation of 1 by the odd coefficient functions of C032m's
kernel on [1,2]. No approximant, annihilator or evolution equation for
that nonlinear kernel is derived here.

## Primary theorem coverage

1. Theo Bühler and Dietmar A. Salamon, *Functional Analysis*, lecture
   notes dated 11 May 2016,
   [PDF](https://math.jhu.edu/~js/Math637/eth.functionalanalysis.pdf).
   Read Section2.3.4, Theorem2.3.22 and Corollary2.3.24, printed pp70-71,
   with complete proofs. In a real normed space, membership of x in the
   closure of a linear subspace Y is equivalent to every bounded linear
   functional annihilating Y also annihilating x. Outside that closure,
   the separation proof constructs a norm-one functional whose value
   is the positive distance. The PDF text extraction loses overbars;
   use the closure formulation, consistent with both proof directions.
   Screenshots did not yield inspectable image content here.
   Also inspected Theorem5.4.5, pp200-203, statement and essential
   algebra/constant/lattice steps: complex Stone-Weierstrass requires a
   unital, point-separating, conjugation-invariant subalgebra. Its proof
   uses polynomial compositions, not just linear combinations.
   Example1.3.7, p28, records signed-measure duality; its separate
   measure-book reference was inaccessible and is replaced by item2.

2. Terence Tao, *245B, Notes 12: Continuous functions on locally compact
   Hausdorff spaces*, 2 March 2009,
   [author text](https://terrytao.wordpress.com/2009/03/02/245b-notes-12-continuous-functions-on-locally-compact-hausdorff-spaces/).
   Inspected Theorem24 and its compact-space proof, Lemma29 and proof,
   Exercise31 and Remark33. Signed Riesz representation identifies the
   continuous real dual of C(X), for compact Hausdorff X, with finite
   signed Radon measures. The positive theorem constructs a regular
   measure; the signed passage decomposes a bounded functional into
   positive parts. Exercise31 states the signed conclusion explicitly
   rather than supplying a separate full proof. The displayed inequality
   0<=I(f) in Lemma29's proof is a typo for arbitrary signed I; neither
   that inequality nor positivity of I is a hypothesis of the lemma.
   We cite the standard signed Riesz theorem, not that erroneous line.
   Our [1,2] is compact metric; C_c=C and finite Borel measures are
   regular. No density or absolute continuity of a mixing measure is
   required. This is the relevant measure dual, not Hilbert-space Riesz.

3. Peter Borwein and Tamás Erdélyi, *The full Müntz theorem in C[0,1]
   and L1[0,1]*, J. London Math. Soc. (2)54 (1996), 102-110,
   [author manuscript](https://people.tamu.edu/~terdelyi/papers-online/Fullmuntz.pdf).
   Inspected Theorem2.1, manuscript p3, and its bounded-analytic/Mellin
   proof case inf(lambda_i)>0, pp7-8. For distinct positive real
   exponents, span{1,x^(lambda_i)} is uniformly dense exactly when
   sum lambda_i/(1+lambda_i^2) diverges. The proof uses the actual
   powers to construct a bounded Mellin transform and invoke Blaschke
   uniqueness. Other exponent-limit proof cases were not audited;
   no Müntz theorem is imported for our family. No representation of
   phi_n as powers in a common width coordinate has been established.
   Adding 1 to our span would assume precisely the membership at issue.
   The manuscript's separate away-from-zero Lp statement is not a
   uniform approximation theorem for these nonlinear coefficients.

4. James Nolen, *Partial Differential Equations and Diffusion Processes*,
   Stanford Math227 notes, accessed 18 November 2026,
   [course PDF](https://math.stanford.edu/~ryzhik/STANFORD/STANF227-10/notes227-09.pdf),
   Section2.3, (3.17), P0-P1, printed pp14-15; Theorem2.3.1 and its
   differentiation argument pp16-17. The Gaussian heat kernel is smooth
   for positive time and satisfies partial_t Phi=Delta Phi, with
   variance 2t. The convolution theorem assumes continuous initial data
   of at most exponential growth. Its proof uses dominated difference
   quotients; the displayed global sup(g) bound only covers bounded g
   literally, so it is not reused for our unbounded divisor.
   Only the single-Gaussian identity is an input to the proposed test.
   Complex translations, the infinite zero sum, the R integral and
   nonlinear exponentials need their own uniform justifications.
   This source does not assert their evolution or coefficient closure.

## Comparison and applicability limits

For a real continuous coefficient family, items1-2 are the standard
source tools for the proposed constant-versus-mass-one-annihilator
duality. A functional nonzero on 1 can be normalized there; mere
nonzero annihilators of mass zero do not answer that question.
The canonical application, including this normalization, is deferred
to mathematical work. No new local duality lemma is claimed here.

C032m supplies joint continuity of all fixed complex derivatives in
width, so coefficient continuity has an existing analytic interface.
C032k records real-even profiles; an application of real duality must
explicitly retain their conjugation symmetry and the normalized
primitives. No arbitrary complex coefficient family is silently
substituted. The source results do not need heat positivity, while
the probability-law interpretations retain C032j's extra inputs.

Missing structural hypotheses are concrete: the *linear* coefficient
span has no proved multiplication closure or inclusion of constants;
no Mellin power representation or bounded-transform zero set is known.
Pairwise distinct widths, finite-family independence and entire
dependence on w give none of these hypotheses. This is a comparison of
theorem scope, not a counterexample to coefficient completeness.

Reused without re-browsing: source ledger1528's Haslinger2.39 analytic
integration coverage and Powers-Xu Definition1/Theorem1 comparison;
C032j's fixed-v1 Sra qualifications; C032l's Narasimhan finite theorem
and stop1302. The latter is not extended from finite sums to integrals.
No sibling notebook, other preprint version or finite-zero data was read.

## Bounded search and access record

Queries included `Hahn Banach Riesz representation theorem density
linear span continuous functions signed measures lecture notes`;
`Müntz analytic kernels completeness`; `Müntz away from the origin
Borwein Erdelyi pdf`; `exp(-E sinh Riemann smoothing`; `Sra smoothing
mixtures Xi`; `annihilator coefficient analytic kernel complete`;
`Gaussian signed mixtures identifiability compact`; `analytic kernel
complete Stone-Weierstrass`; `Riemann smoothing width differential
equation`; `Gaussian odd coefficient span heat`; and `smoothed Xi
uniform approximation`. Punctuation variants were used.

The exact-family queries produced no inspected matching completeness
or closed-width-recurrence theorem. Gaussian-mixture identifiability,
Hermite completeness and other kernel results surfaced only as leads;
their hypotheses have not been matched and they are not imported.
Do not infer novelty from these search results.

Local searches were confined to compact-width/smoothed-law assessments,
working notes and the named stop1302. No prior width-evolution closure
proof was located in those paths. Salamon's old measure.pdf URL
returned403 and the alternate salamond URL404. Item2 supplied accessible
independent coverage; there is no remaining access dependency for the
scalar test. The older probability-kernel blocker stays parked.

## Bounded continuation

Compare up to three mechanisms: direct algebra closure (unpaid and
including 1 would be circular), a Müntz representation (unverified
power structure), and exact Gaussian-width evolution (explicit starting
identity with a concrete closure test). Select the third for one
attempt, as scoped in width-evolution1532. Do not run grid fitting.

Seek an exact, uniformly justified width-evolution formula and determine
whether it yields a closed *linear* recurrence among the odd coefficient
functions. Every boundary/normalization and nonlinear term must remain.
If unclosed terms remain, record them and stop the proposed direct
linear-recursion argument; their presence alone does not prove that
no other recurrence, approximation or annihilator exists. If closure
is obtained, specify the further approximation estimate it would need.

The main gap remains L030-L032/C032a actual-Xi all-degree positivity.
This test could organize or exclude one continuum smoothing repair;
positive mixtures, moments and unsmoothed realization remain independent.
Full matching Mathlib coverage is unchecked. No new lemma, mathematical
script, DAG edge or main-proof change belongs to this literature step.
