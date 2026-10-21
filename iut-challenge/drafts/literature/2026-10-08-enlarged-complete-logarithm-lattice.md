# Genuine enlarged logarithm lattice — completed source comparison

TARGET: Compute an exact Z_3-basis of log(O_L^times) for L=Q_3(zeta_20,pi), pi^27=3, with complete unit coverage and controlled infinite tails.
CHECKED: 2026-10-08
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the parent field/unit-filtration assessment and its cyclotomic-image exclusions; searched exact logarithm-image basis, local unit-group algorithm, pi^27, zeta_20 and exact unramified coefficient arithmetic; inspected HPP's basis cases, Clark's integral models, and official Magma/SymPy arithmetic documentation.
SOURCE_EVIDENCE: Clark, undated 161-page author notes, Propositions 2.5/2.9/2.30, Corollaries 2.6/2.10/2.33, printed pp. 63–65, 76–77; Hess–Pauli–Pohst, undated 18-page author manuscript, Theorems 3.1/3.3 and case-I proof pp. 3–5, Proposition 3.4/Algorithm 3.5 pp. 5–6, Proposition 5.1(i,iii–iv) pp. 9–10; official Magma Exact p-Adic Rings constructors and SymPy 1.14.0 Matrix Normal Forms documentation; accessed 2026-10-08.
COMPARISON: Known finite-unit basis and exact integral-model methods cover the specified e=27, f=4 field; no inspected source prints its genuine rank-108 additive logarithm matrix or licenses O_U-stability. Computing that matrix is a certified specialization/reproduction, not a new general basis theorem.
GAP: Produce complete genuine-image generators, certified finite representatives and an exact rank-108 Z_3-basis with both span inclusions; justify the coefficient-field identification and every omitted infinite term.
REASON: Essential sources are accessible and cover the changed coefficient arithmetic and complete-generation obligations; approve one bounded exact calculation while preserving the false scalar-transport stop.
LITERATURE_REASON: The saved target was REVIEW_REQUIRED for the full enlarged image, rather than one separating logarithm; exact coefficient representation and complete-basis certification were outside the parent audit's scope.
SCOPE: Only the ordinary continuous unit-logarithm image for the specified field and its exact Z_3-lattice certificate; no O_U-module assumption, action/radius transfer, packet realization or original-IUT implication.

## Relevance and local comparison

The main gap remains finite B>=A in the original comparison, with actual
input/action/pilot compatibility. The single intermediate target above
could supply a correct local shell for a later separately reviewed action
or radius test in a field containing the required prime-to-3 roots.
It establishes neither division-field admissibility nor global realization.
Actual/native inputs, pilot transport, essentiality and the numerical
comparison remain independent gaps.

Essential input is L030's audited field model and scalar-transport failure.
L016 supplies only an old-field comparison and a reusable certificate
method. Read L030's field hypotheses and complete-tail argument, L016's
all-unit reduction/tail and lattice-verification passages, ATTEMPTS/023,
history/083, and the parent identity and audit assessments. No matching
new-field basis occurs in those inspected records. Preserve L029 and
ATTEMPTS/022's unchanged-packet exclusion; they motivate the new field
but are not mathematical inputs of its basis calculation. No sibling
notebook or supervisor state was read.

The [official challenge announcement](https://zen.ac.jp/news/0ul6zqed9-0),
dated 2023/07/07, was rechecked on 2026-10-08: its Challenger paragraph
still asks for a paper showing an inherent flaw. This is the accessible
current primary version, not a correctness or prize-adjudication certificate.

## Primary theorem coverage

[Clark, Algebraic Number Theory II: Valuations, Local Fields and Adeles](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf),
undated author-hosted 161-page version: Proposition 2.5 assumes a complete
DVR and a monic polynomial with irreducible residue polynomial; separable
reduction gives the unramified integral model. The following classification
and Corollary 2.6 identify unramified extensions and allow base change.
Proposition 2.9/Corollary 2.10 give the Eisenstein integral model.
Proposition 2.30 requires a Henselian valued field and preserves
prime-to-residue-characteristic roots under reduction; Corollary 2.33
states the finite-field torsion count and excludes p-primary roots when
(p-1) does not divide e. Inspected the integral-DVR and classification
passages; reused the parent's inspected Eisenstein and lifting proofs.
L030 already checks U unramified of degree four and L/U Eisenstein of
degree 27. These general results are inputs to cite, not reprove.

A permitted exact coefficient-model choice for the calculation is
 theta=zeta_20^4 with polynomial Phi_5(X)=X^4+X^3+X^2+X+1.
Verify its separable irreducible reduction over F_3 and its identification
with the specified U using the cited unramified classification and root
order, before using 1,theta,theta^2,theta^3 as coefficients. This is a
standard integral-model specialization covered by Clark, not a theorem
asserting stability of the logarithm image. It avoids treating a truncated
3-adic factor of Phi_20 as an exact polynomial. This turn produces no
factorization certificate or new field-model proof.

[Hess–Pauli–Pohst, Computing the Multiplicative Group of Residue Class Rings](https://page.math.tu-berlin.de/~kant/publications/papers/hepapo.pdf),
undated author-hosted 18-page manuscript: section 3 identifies successive
principal-unit quotients with the additive residue field. Theorem 3.3
uses lifts of an F_p-basis and fundamental levels
0<nu<pe/(p-1), p not dividing nu. It gives finite-quotient basis
representations if (p-1) does not divide e, the critical map is invertible,
or the truncation is below e/(p-1). Here the first alternative applies.
Read Theorem 3.1's shallow/deep power cases, both order ranges and the
complete case-I induction in Theorem 3.3; Proposition 3.4 and Algorithm
3.5 supply effective basis/coordinate procedures. Proposition 5.1(i)
covers positive-depth logarithms; (iii–iv) give inverse log/exp strictly
above e/(p-1), including finite deep quotients. Depth 14 exceeds 27/2.
Remark 5.2 assumes deep inputs and does not certify shallow tails.
Reused the warning about corrupted extraction of part (ii); use the
standard continuous logarithm homomorphism. These methods cover f=4,
not just f=1; they give no O_U-linear action on shallow logarithms.

The manuscript's number-field formulation applies through the completion
of Q(pi,zeta_20) at the selected place, as justified in the parent
assessment. No additional global IUT initial-data hypothesis is supplied
by this ordinary field-of-definition observation.

## Exact arithmetic and stronger-result comparison

[Official Magma handbook, Exact p-Adic Rings](https://docs.magma-maths.org/LocalFields/PAdicRingsAndTheirExtensions/xpadic.html),
page accessed 2026-10-08, documents Exact=true for the base field/ring
and extension constructors requiring an inertial or Eisenstein polynomial,
or specifying unramified degree. Read the constructors and the example
of a ramified extension over an unramified one. This covers a supported
representation architecture, not a theorem computing the logarithm image.
Magma execution, licensing and availability are not required or verified;
exact rational polynomial reduction with a mathematical certificate is
sufficient. No software, key or credit purchase is proposed.

[SymPy 1.14.0, Matrix Normal Forms](https://docs.sympy.org/latest/modules/matrices/normalforms.html),
page last updated 2025-04-27, accessed 2026-10-08: smith_normal_form
requires a PID; hermite_normal_form accepts integer matrices. Its optional
modular D must be a positive multiple of the HNF determinant, with a
full-row-rank assumption. Read these requirements and examples. The
referenced Cohen Algorithms 2.4.5/2.4.8 were not independently read and
are not imported through a secondary reference. The standard named
Smith/Hermite normal-form theorem can be cited, but a software matrix
alone is not a verified Z_3-span certificate. L016 already documents
exact local diagonalization and full row/column transformation checks;
reuse the method, not its old numerical basis.

New queries: `p adic logarithm units lattice basis algorithm Hess Pauli
Pohst principal units`; `exact image p adic logarithm local field units
Zp basis computation`; `unramified extension cyclotomic fifth roots Q3
integral basis Phi5`; `"logarithm" "pi^27" units`; `"logarithm"
"zeta_20" lattice`; `site.docs.magma-maths.org unramified extension
exact p adic polynomial integral`. No inspected theorem computes the
specified additive matrix. Failure to find one does not certify novelty.
Reused the parent's inspected Sarkar–Shaikh arXiv:1904.09850v6 Theorem
1.4 and Sarkar arXiv:2601.18187v1 Theorem 2.1 exclusions: their
Q_p(zeta_p) hypothesis differs, and the recorded withdrawal/numbering
warning persists. The newly returned quadratic 2-adic basis paper
arXiv:1907.06437 is an unread lead with different field scope. Discussion
threads, group-ring integral logarithms and software search snippets are
not imported mathematical evidence.

## Bounded mathematical continuation and discriminating test

The exact TARGET is unchanged. Next, specialize the known unit-filtration
construction in a verified 108-dimensional common Q_3-coordinate model.
One economical route is four residue-basis lifts at each shallow depth
1,...,13, together with the complete deep ideal H=pi^14 O_L. This is
an alternative to the fundamental-level multiplicative basis; do not
mistake an overcomplete generator family for an additive basis. Establish
all-unit coverage, including residue torsion with zero logarithm, and
both containments in the resulting Z_3-span. The convergence and deep
inverse theorems are imported; only field-specific representatives and
certificates need computation.

For every shallow generator, prove the infinite error lies in H before
replacing its logarithm by a finite coordinate representative. L030 and
L016 contain a block-tail method for unit coefficients at this ramification;
check its hypotheses for every new coefficient/depth, rather than using
Remark 5.2 or extrapolating old table entries. Arithmetic in Phi_5 and
pi^27=3 must be exact. Include every deep-ideal basis column. Certify
rank 108 and both span inclusions using complete generator coordinates
and basis expressions, or full invertible local row/column transforms.
A determinant/index, sample, numerical precision label or O_U-basis
assumption cannot substitute for these checks. A convergent-logarithm
basis is acceptable only with rigorous generation and independence;
a usable finite rational-coordinate basis requires certified tail replacements.

Continue if the complete certificate and infinite proof establish an exact
basis. If a proposed basis fails, record the failed column or unproved
tail and preserve the attempted computation; this does not refute existence
of a genuine basis or IUT. Persistent essential representation/source
blockers require parking dependent calculations and a different test.
Do not repeat L030's separator as a substitute for the full image.

SPECIALIZE approves one calculation using known methods; a successful
basis computation is REPRODUCTION, not a new general theorem or
certified originality. This completed literature step is EXPLORATION /
LITERATURE / NOVELTY_UNCHECKED: new target-specific source comparison,
no new basis, lemma or mathematical script. No mathematical exploration
attempt is spent. Full matching and supporting Mathlib coverage remain
**not checked**, not absent. PROOF.md and DAG.md need no change because
the argument and its mathematical inputs have not changed.
