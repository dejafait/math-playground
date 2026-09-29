# Cubic RM Kahler eigenvector — literature assessment

TARGET: Test whether U extends to a rational cup-product-self-adjoint endomorphism U plus A of H^2(S,Q), with A on NS(S)_Q and a Kahler class omega in NS(S)_R satisfying A(omega)=lambda omega, where U(sigma)=lambda sigma.
CHECKED: 2026-09-27
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched the cubic RM twistor target, prescribed-form self-adjoint representations, scaled trace forms, odd-degree transfer and orthogonal approximation; queries and primary statements actually read are recorded below.
SOURCE_EVIDENCE: Hanselka (2015), Lemma 3.10 and Remark 3.12, https://d-nb.info/1112605010/34#page=68; Bayer-Fluckiger--Lenstra (1990), Proposition 1.2 proof, p. 362, https://pub.math.leidenuniv.nl/~lenstrahw/PUBLICATIONS/1990e/art.pdf#page=5; Peters--Sterk (June 2024 version), Proposition A.3.3, p. 424, https://www-fourier.univ-grenoble-alpes.fr/~peters/Books/QuadraticForms/QuadForms.pdf#page=431; further comparisons below.
COMPARISON: Known transfer constructions and cone tools supply a concrete method, but the inspected statements do not give the specified cubic operator and Kahler eigenvector on this divisor form; broad transfer existence results have different rank hypotheses.
GAP: Specialize the known construction to the actual rational form, check the sign at the specified holomorphic-form eigenvalue, and certify the Kahler chamber; no such certificate or obstruction is supplied by this review.
REASON: Import the general arithmetic and cone results and perform only the remaining compatibility test in a separate research turn. This bounded prerequisite could justify a bundle-existence search; it does not itself supply a bundle or transverse lift.

## Hypotheses

Retain the very general cubic S, the operator U of L006, and the
same product metric setup as the [completed bundle review](2026-09-27-hyperholomorphic-cubic-rm-representatives.md).
The minimal polynomial is f(z)=z^3+z^2-2z-1, and lambda is the
specified real eigenvalue in U(sigma)=lambda sigma. Write
N=NS(S)_Q. Its rank-four cup-product form is the one in L019,
equation (2), with basis (F,O,E,P) and determinant -7.
These are existing notebook inputs, not computations in this turn.

The requirement is A in End_Q(N), self-adjoint for that form,
with a Kahler eigenvector omega in N_R. Neither A nor the
conjugating maps used to construct it are required to preserve
the integral lattice. Omega need not be rational. No unital
action of the cubic field, or identity f(A)=0, is imposed on
all of N. Thus a dimension-divisibility argument for a field
action on the entire rank-four space would test a stronger target.
The adequate [rational Hodge target audit](../../foundations/01-target-and-scope.md)
and family audit are reused without changing their scope.

## Conclusion

The exact saved TARGET now has a completed SPECIALIZE assessment.
The selected method is a known transfer construction, followed by
a check of the actual rational form and the Kahler chamber.
This replaces an unspecified matrix search with a bounded test.
It establishes neither existence nor nonexistence for this S.

The main gap is still an algebraic representative extending the
cubic action in V_RM outside V_D. A compatible eigenvector would
provide cohomological data for the bundle route. Bundle existence,
stability, the other Chern-class requirements, and transport into
the missing NS-fixed direction would remain unresolved. A twistor
line alone does not reach that threshold. The achieved three RM
directions against four required, the 21-dimensional span on the
original family, and the universal fourfold and higher-dimensional
gaps are unchanged.

This is LITERATURE / NOVELTY_UNCHECKED / EXPLORATION. It is the
second exploration turn after L024, with no budget reset. No
mathematical result has been derived. The future specialization
should be reported as REPRODUCTION if it only applies the tools
below; absence of an exact source match does not establish novelty.

## Proof

The evidence is a comparison of source statements and hypotheses.
The pending assessment and an intermediate source checkpoint were
completed here without performing their proposed calculations.

### Closest geometric precedent

Reused Lemma 1.2.1.2 and reread Proposition 1.2.3.3 with its proof
in Ulrich Schlickewei, *Hodge classes on self-products of K3 surfaces*,
Bonn dissertation (2009), [printed pp. 29--30](https://d-nb.info/1000464202/34#page=31).
For a quadratic RM eigenvalue sqrt(d) and Picard rank at least
three, it constructs a self-adjoint divisor endomorphism with
a Kahler eigenvector. Its proof finds two rational Kahler classes
whose squares have ratio d, using rational points on an indefinite
quadric. The accompanying bundle application remains conditional.
The theorem addresses a quadratic eigenvalue, so it is a precedent
for the saved cubic test, not a full match. Reproducing its general
twistor criterion is unnecessary.

### Prescribed forms and a concrete transfer construction

Read Christoph Hanselka, *Characteristic Polynomials of Selfadjoint
Matrices*, Konstanz dissertation (defended 4 December 2015),
[Lemma 3.10, printed pp. 64--65, and Remark 3.12, p. 66](https://d-nb.info/1112605010/34#page=68).
For an irreducible separable polynomial and a specified regular
form, self-adjoint spectral representations correspond to scaled
trace forms isometric to that form. This treats the pairing as
part of the problem. It applies to a polynomial's field block;
it does not require putting that field structure on an unrelated
complement. Also inspected Theorems 3.13, 3.17 and 3.18,
pp. 67 and 70: the first permits powers of the polynomial, the
second concerns real function fields, and the number-field
statement uses the Euclidean form. None directly supplies the
required rank-four cup-product realization. The useful import
is the prescribed-form correspondence, not a Euclidean matrix.

Followed the odd-degree transfer lead and read
Bayer-Fluckiger--Lenstra, *Forms in Odd Degree Extensions and
Self-Dual Normal Bases*, American Journal of Mathematics 112
(1990), 359--373, [Proposition 1.2 proof, p. 362](https://pub.math.leidenuniv.nl/~lenstrahw/PUBLICATIONS/1990e/art.pdf#page=5).
For a simple odd-degree extension L=K(a), the proof uses the
K-linear functional s with s(1)=1 and s(a^i)=0 for
1<=i<[L:K], and records s_*(<1>)=<1> in W(K), together with
the transfer projection formula (1.3). This gives a specific
known transfer form to try. The functional is not the unscaled
field trace, and equality in a Witt group is not an explicit
isometry of the desired rank. Identifying the resulting form
with an appropriate part of N and assigning the positive line
to the specified lambda are still application obligations.
No cubic transfer matrix or signature is computed here.

### Stronger existence theorems and their rank limits

Read Bayer-Fluckiger--van Geemen--Schuett,
*K3 surfaces with real or complex multiplication*,
[arXiv:2401.04072v4, 31 July 2026](https://arxiv.org/pdf/2401.04072v4):
Theorem 2.1 and Lemma 2.3, pp. 5--6; Lemmas 5.1 and 6.1,
pp. 7--8; the signature discussion, p. 9; Theorem 8.1 and
Propositions 8.3 and 8.5, pp. 14--15; and Theorem 10.4
with its setup, pp. 17--18. Field actions correspond to transfers;
rank-one transfer signatures depend on real-embedding signs.
Rational isometry requires dimension, determinant, Hasse invariant
and signature, so determinant and signature alone are insufficient.

Theorem 8.1 requires a complement of dimension at least two;
a cubic block in N leaves one. Proposition 8.3 addresses the
full K3 form, while Proposition 8.5 concerns quadratic fields.
Theorem 10.4 requires field-rank m>=3 and K3-type signature,
unlike the rank-one block being considered. These scope limits
leave the specific compatibility argument open.

### The actual Kahler chamber

Read Huybrechts, *Lectures on K3 Surfaces*, author's book draft,
[chapter 8, section 5.1 and Theorem 5.2, printed p. 163](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=163).
The Kahler cone consists of classes in the distinguished positive
cone pairing positively with every smooth rational curve.
Its intersection with N_R is the ample cone, which is open.
Thus a positive-square eigenvector or finitely sampled curve
inequalities alone would leave a gap.

Read Peters--Sterk, *Symmetric and Quadratic Forms, with Applications
to Coding Theory, Algebraic Geometry and Topology*, author's
June 2024 version (title-page date 16 September 2024),
[Proposition A.3.3 and Corollary A.3.4, printed pp. 424--425](https://www-fourier.univ-grenoble-alpes.fr/~peters/Books/QuadraticForms/QuadForms.pdf#page=431).
For a nondegenerate rational quadratic space, its rational special
orthogonal group is dense in the product of its groups over any
finite set of completions, including the real completion.
The accompanying corollary concerns approximation of vectors
with a prescribed represented rational norm. Use the group
statement if the eigenvector's norm is irrational. This suggests
rational conjugation as a chamber tool once a positive eigenvector
is certified; that application and its effect on A remain to be
checked. No isometry preserving the integral lattice or induced
by an automorphism of S is required by the saved target.

### Search record, reuse and source limits

Queries on 2026-09-27 included:

- `"K3" "cubic" "Kähler" "eigenvector"`
- `"K3" "twistor" "cubic" "multiplication" Schlickewei`
- `quadratic forms self adjoint endomorphism prescribed characteristic polynomial trace form number field Bayer Fluckiger`
- `"self-adjoint" "scaled trace" quadratic`
- `"On the scaled trace forms and the transfer"`
- `K3 real multiplication transfer quadratic forms Bayer Fluckiger van Geemen Schutt 2024 2025`
- `"self-adjoint" "Lorentzian" "irreducible" polynomial`
- `"Scharlau transfer" "odd" "hyperbolic"`
- `"special orthogonal" "weak approximation" theorem pdf`

Title and author follow-ups led to the statements above. The
exact-geometry searches did not locate the saved cubic certificate.
This is a bounded comparison, not an exhaustive novelty search.
The PDF text of the cited statements was read. The screenshot
interface returned links without usable page images; no visual
inspection is claimed. A shell download failed because DNS access
was unavailable; the web PDF text supplied the necessary passages.

Krueskemper's 1992 paper and Bender's 1968 original remain unread
original sources. Their citations in the inspected works are not
counted as direct readings. Neither is essential to the selected
transfer construction and chamber test: the relevant transfer
identity is stated in the inspected Bayer-Fluckiger--Lenstra proof,
and the selected approximation theorem is stated in Peters--Sterk.
Scharlau's original transfer reference and the earlier proofs cited
there were not separately inspected. No source-access gap remains
for this assessment's selected inputs.

The existing lattice calculation in L019 is reused. The parent
bundle assessment already compared L004, L012, L017 and L024
with this route. Their exclusions concern isometries or specified
representatives, not the present arbitrary rational divisor
endomorphism. This review supplies no reason to reopen their
failed representatives or recompute their obstructions.

### Bounded specialization and stopping test

The same exact TARGET is retained for a separate research turn.
Use the cited transfer construction as the first concrete method:

1. Seek a rational self-adjoint operator on the recorded form,
   using the known transfer description. Supply an exact rational
   form identification or a rigorous incompatibility argument;
   matching determinant and signature alone will not suffice.
2. Check the eigenline for the specified lambda, then certify a
   Kahler vector by the cone criterion or a fully justified
   application of rational orthogonal approximation. A positive
   eigenline for a different conjugate is not the requested result.
3. Finish with a compatibility certificate, an obstruction for
   the stated realization, or an explicit inconclusive stop.
   An unsuccessful finite matrix search cannot prove nonexistence.

This is the final permitted test in the current three-turn
exploration window if it produces neither an advance nor an
informative negative result. A positive certificate would justify
a separate bundle-existence target, with its own literature gate.
A negative certificate would stop this selected common-metric
realization; an inconclusive test must not restart the budget
under a different name. No conclusion here excludes other
metrics, representatives, or mechanisms for the Hodge conjecture.

## Mathlib

Coverage: **not checked** for the full target or its transfer,
quadratic-form, approximation and Kahler-cone inputs. No full
matching declaration or absence from checked Mathlib sources is
asserted. The named results and direct links above are supporting
mathematical references; none is a cited full solution of the
saved cubic compatibility target.
