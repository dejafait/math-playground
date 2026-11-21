# Bounded-profile Green resolvent: joint positivity proposal

TARGET: Review whether the bounded-profile Green resolvent yields positive joint angular Fourier data with zero mode H under C868a/C868b's necessary conditions, starting with the index set {0,(1,0),(0,1),(1,1)}.
CHECKED: 2026-11-06
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed the scoped L868/C868a/C868b and three named period-gap failure checks; searched scalar modified-Helmholtz Green functions, Bochner/Herglotz Fourier data, Schur products and positive resolvents, including frequency-dependent/profile queries listed below. No applicable joint-angular theorem located in the inspected sources; this bounded search does not certify novelty.
SOURCE_EVIDENCE: Engel-Nagel (2000), II.1.10 pp55-56, VI.1.7-1.8 pp353-354, VI.4.1/proof (4.2)-(4.3) pp384-386 https://www.math.uni-tuebingen.de/de/forschung/agfa/members/engel-nagel_one-parameter-semigroups.pdf ; Lebl, Notes on Diffy Qs, online 2026-11-06, Theorem2.2.1(1)/Example2.2.1 https://www.jirka.org/diffyqs/html/sec_ccsol.html ; Loomis (1953), 36A pp141-142 https://people.math.harvard.edu/~shlomo/212a/loomis.pdf ; Bhatia (2007), Sections1.1-1.2 pp1-2,4,7 https://assets.press.princeton.edu/chapters/s8445.pdf ; exact inspected passages and qualifications below. Reuse the saved compact Fejer assessment.
COMPARISON: Scalar resolvent and homogeneous-solution formulas are known. Bochner needs all joint finite quadratic forms; Schur preservation needs positive matrices of the same size; positive-semigroup resolvents need a common ordered function space and positive semigroup. None of the inspected statements supplies the frequency-dependent joint transform or licenses replacing the original mean by H. The four-index positivity question remains a mathematical test.
GAP: Establish or refute positivity of the prescribed four-index matrix from the explicit necessary-condition package below; no source import supplies that implication. Reconstruction, identification with B_n, removal of homogeneous freedom, zero-mode control and K>=-|M| remain separate gaps.
REASON: Essential scalar-kernel, homogeneous-freedom and finite-positivity source comparison is now complete for one bounded test. EXPLORE permits a separate mathematical attempt on that test, not derivation in this literature turn, certification of the proposed operator, or unrestricted reconstruction/period work.
SCOPE: L018/L847 and audited L868/C868a/C868b remain the origin; the first test is of their necessary profile/mean/positivity package, explicitly retaining a nonnegative C1 h as specified below. No growth, summability, bandwidth, feasible smoothing, global mean bound or graph-existence premise. Full admissibility is required for any conclusion about L868's feasible class.
COVERED_TARGET: Test whether the bounded-profile Green resolvent yields positive joint angular Fourier data with zero mode H under C868a/C868b's necessary conditions, starting with the index set {0,(1,0),(0,1),(1,1)}.

## Exact proposed operator test

For n!=0 write U_n(t)=B_n(t)-B_n''(t), using C868a's profile
notation and C868b's bound |U_n(t)|<=H on the entire real line.
The candidate data to assess, not a newly established decomposition,
are

\[
 b_0(x)=H,\qquad
 b_n(x)=\frac12\int_{\mathbb R}
       e^{-|n\cdot x-u|}U_n(u)\,du\quad(n\ne0).
\]

The proposed first discriminating test asks whether the finite
quadratic form with entries b_(j-l)(x) is nonnegative for all
coefficients when j,l range over
E={0,(1,0),(0,1),(1,1)}. This couples nonparallel angular
directions rather than just the opposite-index subgroup already
handled by C868b. Defining the proposed integral here approves
neither its role as a profile solution nor any reconstructed
positive function. The choice b_0=H is part of the question;
it is not the generally unknown original mean hhat_0(x).

The nomination required inspection, before a mathematical test, of primary statements and relevant
proof cases for the one-dimensional Green resolvent, its homogeneous
freedom, positive definite Fourier data and positivity-preserving
multiplier/integral operators. Compare precisely with the radial
argument n dot x that changes with n. Reuse existing Fejer and
finite trigonometric positivity coverage wherever its hypotheses
are unchanged. Do not infer joint positivity from positivity of
each separate scalar kernel, or import an extra growth condition
on B_n. At nomination, no primary source for these additional uses had
been inspected. The separate source review below completes this
coverage for the bounded test only. Matching Mathlib coverage is unchecked.

## Relevance and decision test

The main gap remains L030-L032/C032a actual-Xi all-degree mixed
positivity. A positive reconstructed correction, if justified, could
help separate correction cost from the remaining homogeneous modes
in L868's period problem. This is a proposed use, not a conclusion:
global reconstruction, the original pointwise domination by |F|,
the zero mode and the threshold K>=-|M| would still require proof.
Graph realization and higher Xi signs are independent gaps.

For a later covered attempt, a primary theorem with applicable
hypotheses or a proved joint positivity mechanism would justify
continuation. A negative finite test satisfying the stated necessary
conditions would stop the claim that those conditions alone make
this operator positive. Such data would not be a counterexample
to L868's full feasible class, the sharp period inequality or RH
without separately proving all original constraints. Passing just
the selected finite test would not establish full positivity or
justify indefinitely enlarging matrices without a new mechanism.

The proposed operator supplies a different test from repeating
trace cancellation or manipulating the unchanged free mean. Keep
the stops in ATTEMPTS/2026-11-06-one-sided-dual-reduction-period-gap.md,
ATTEMPTS/2026-11-06-fourier-diagonal-period-uncontrolled.md and
ATTEMPTS/2026-11-06-g-zero-fiber-period-gap.md. No cross-notebook
input is proposed. Creative discovery remains a priority, but this
nomination is a source comparison, not an approved creative proof
attempt or a claimed new central sign mechanism.

## Separate literature review, 6 November 2026

LITERATURE_REASON: The saved target was REVIEW_REQUIRED: the Green
operator, homogeneous freedom and joint finite positivity were outside
the reused compact Fourier assessment. This review supplies that missing
comparison once; the prior Hardy/Fejer inputs are reused unchanged.

This completes the source gate for the COVERED_TARGET, without performing
its mathematical test. The original TARGET records the completed review;
the COVERED_TARGET is the exact proposed mathematical continuation. A
supervisor-required separate approval of this changed assessment remains
separate from the completed literature work.

### Inspected primary statements and relevant proof cases

**Scalar resolvent and positivity.** Klaus-Jochen Engel and Rainer Nagel,
*One-Parameter Semigroups for Linear Evolution Equations*, GTM194,
Springer (2000), [II.1.10, pp55-56; VI.1.7-1.8, pp353-354;
VI.4.1 and (4.2)-(4.3), pp384-386](https://www.math.uni-tuebingen.de/de/forschung/agfa/members/engel-nagel_one-parameter-semigroups.pdf#page=400).
II.1.10 assumes a strongly continuous semigroup with norm at most
M exp(wt); for Re(lambda)>w its Laplace integral is the resolvent.
Inspected its inverse proof and norm estimate. VI.1.8 assumes a
semigroup on a Banach lattice, and its forward proof obtains positive
resolvents from the integral. VI.4.1 works on C([-infinity,infinity]),
with finite endpoint limits, and second-derivative domain C2 of that
compactification. Its proof gives the convolution kernel
exp(-mu|t|)/(2mu), Re(mu)>0, lambda=mu^2. Read the injectivity,
split-integral differentiation, endpoint-limit and norm arguments.
The candidate uses mu=1. The theorem's endpoint-limit hypothesis is
not known for general U_n. Import the kernel formula, not its full
function-space conclusion for arbitrary bounded profiles. Any extension
needed by the later attempt must explicitly justify that difference.
Neither result asserts the joint-frequency claim here.

**Homogeneous freedom.** Jiri Lebl, *Notes on Diffy Qs*, author-hosted
online version inspected 2026-11-06, [Theorem2.2.1(1), its characteristic
equation discussion and Example2.2.1](https://www.jirka.org/diffyqs/html/sec_ccsol.html#thm:ccsol),
also [Theorem2.1.2](https://www.jirka.org/diffyqs/html/solinear_section.html).
The hypotheses are a second-order linear equation with constant
coefficients, nonzero leading coefficient, and distinct real
characteristic roots. Example2.2.1 explicitly treats y''-k^2 y=0;
at k=1 its general solution is c1 exp(t)+c2 exp(-t). The existence
and uniqueness statement assumes continuous coefficients/forcing on
an interval and two initial data. Read the distinct-root construction
and complete example; no claim to have read a proof of the general
existence theorem, which is only cited. Real and imaginary parts
handle complex profiles. This known formula records the freedom
that a particular Green solution does not remove. No boundedness
of B_n, or vanishing of its homogeneous constants, is imported.

**Fourier positive definiteness.** Lynn H. Loomis, *An Introduction to
Abstract Harmonic Analysis*, Van Nostrand (1953), [36A, pp141-142](https://people.math.harvard.edu/~shlomo/212a/loomis.pdf#page=149).
Read the Bochner theorem statement, its positive-functional setup and
the displayed measure-to-positivity argument; the converse refers
back to 26I and is imported by citation, not reproved or independently
audited here. For a locally compact abelian group, bounded positive
definite functions correspond to finite positive measures on its
dual. The theorem applies to the discrete group Z2, whose dual is
the two-dimensional torus; discreteness removes a continuity issue.
Choose the negative-exponential character convention used locally.
The relevant positive-definiteness requirement is every finite joint
quadratic form, and the zero coefficient is the total mass. Thus
the desired mass H is part of the claim to test; the source cannot
be invoked before that positivity hypothesis has been verified.
It supplies a measure, not automatically a C1 density.

**Finite matrix criteria and multipliers.** Rajendra Bhatia,
*Positive Definite Matrices*, Princeton (2007), [Sections1.1-1.2,
pp1-2,4,7](https://assets.press.princeton.edu/chapters/s8445.pdf#page=7).
Inspected the quadratic-form/eigenvalue/principal-minor criteria,
the Fourier-Stieltjes example, and the Schur-product paragraph and
its tensor-product/principal-submatrix proof. A Hermitian finite
matrix is positive semidefinite exactly when its quadratic forms,
equivalently all principal minors, are nonnegative. Schur's theorem
requires both matrices positive semidefinite and of the same size.
These criteria directly cover the proposed finite E test, with no
infinite summation. They do not reduce joint positivity to bounds
on individual entries or to an opposite-index Toeplitz subfamily.
No positive matrix multiplier/common positive integral representation
for the candidate has been supplied by this source.

### Applicability boundary and exact necessary-condition test

Retain finite H>=0 and the fixed real ell of C868b. For the first
abstract test, require a real, nonnegative C1 function h on R2 times
T2, with normalized Fourier coefficients
hhat_n(x)=U_n(n dot x) for n!=0 and C1 profiles on R. Require
|U_n(t)|<=H globally, and require its actual mean m(x)=hhat_0(x)
to obey m(s,s)=m(ell,s)=H for every real s. Retain C868b's full
finite opposite-index positivity with a0=H at every radial x, not
just a few selected minors. Reality/conjugacy and simultaneous
compatibility with this one h must be respected. Where B_n are
used, retain the C3 profile relation U_n=B_n-B_n''; do not replace
it with an assumed boundedness of B_n. These are the already
stated necessary restrictions being tested, not newly proved
consequences or a sufficient characterization of admissibility.

For this package the candidate b_n and finite E are exactly those
displayed above, including b0=H. Establish joint positivity by a
valid common positive representation, or find a rigorously checked
negative quadratic form with data satisfying the entire package.
A collection of independently assigned bounded U_n without a
compatible nonnegative h is not such a witness. A numerical negative
eigenvalue alone is not a certificate. Finite-mode examples are allowed
as test data, not assumed representative of the full class.

This abstraction deliberately does not assert existence of real q,r
obeying the original modulus bound and both closure equations for
actual F. Any failed test is consequently a failure of sufficiency
of this necessary-condition package only. Full L868 counterexamples
or a period conclusion require checking all those extra conditions,
all actual zeros and the fixed orientation separately. H=0 must
retain C868b's angular independence, not radial independence.

The source comparison leaves two distinct applicability problems:
the candidate kernel is evaluated at n dot x with a different
profile for each n, and the prescribed zero coefficient need not
equal m(x). Scalar positivity alone does not supply the hypotheses
of a joint positive-matrix integral or Schur theorem. This is an
absence of an applicable import in the sources checked, not a proof
that no such representation exists. Do not discard homogeneous
terms or reconstruct an infinite positive C1 correction in this
first test. No general growth/regularity theorem for the full
feasible class is necessary to perform the finite test as defined.

### Search record, duplicates, qualifications and disposition

Searches performed included: `Green function one dimensional modified
Helmholtz operator 1-d2 dx2 exponential kernel bounded solution pdf`;
`Herglotz theorem positive definite sequence torus Z^d Schur product
positive Fourier multiplier lecture notes`; `positive semigroup resolvent
integral positivity preserving Engel Nagel theorem pdf`; `Engel Nagel
one parameter semigroups II.1.10 pdf`; `positive definite frequency
dependent Green kernel Fourier`; `bounded profiles Green positive
definite Fourier`; `Fourier resolvent positivity preserving multiplier`;
and author/MIT constant-coefficient ODE searches. Searches were bounded
by the named scalar, finite positivity and operator hypotheses, not
by a claim that the proposed conclusion must be original.

Additional inspected but unused sources: Masatsugu Sei Suzuki,
*One dimensional Green's function*, 2 December2010, [Section17.3,
PDF pp6-9](https://bingweb.binghamton.edu/~suzuki/Math-Physics/LN-17_1D_Greens_function.pdf),
including both signs of x and the decay boundary condition. Its
x>0 contour text says lower half-plane while specifying the pole
ik and an upper contour; use the clean Engel-Nagel proof instead.
Peter L. Falb, [*On a theorem of Bochner*, Publ.Math.IHES36 (1969),
pp59-60](https://www.numdam.org/item/10.1007/BF02684597.pdf#page=2),
was read for the scalar introduction, finite-form definition and
Lemma2.3 proof; no operator-valued theorem is imported. Teschl's
author ODE PDF timed out twice; use Lebl's accessible exact homogeneous
example rather than make that access issue a dependent blocker.
Uninspected leads include Arendt's *Resolvent Positive Operators*
and other search hits on positive semigroups; none is evidence of
an applicable theorem here. Mathlib matching coverage remains unchecked.

The scoped duplicate check read the relevant C868a/C868b proofs,
L868's system/period interface, the ready diagonal and fixed-fiber
audit assessments, and the three named ATTEMPTS above. They preserve
the free A+H threshold, reconstruction limitations and subclass stops;
none contains this completed Green test. No sibling notebook or
cross-notebook input was read. The October zero-free-region input is
not invoked by this angular operator question.

Disposition: EXPLORE, source coverage ready for exactly one separate
finite joint-positivity attempt. This is literature EXPLORATION, no
new mathematical advance or informative counterexample. The result
does not move the RH gap. A rigorous negative finite witness stops
this necessary-condition implication; a positive test alone does
not establish all joint forms or authorize a chain of larger tests.
A common positive mechanism would justify reconsidering decomposition,
then the still-open period comparison. Reconstruction, original
domination, global zero-mode control, graph realization and Xi signs
remain unresolved. Any changed target needs REVIEW_REQUIRED coverage.
