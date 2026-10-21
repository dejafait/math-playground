# Coverage — arbitrary-branch sharp normalization defect

TARGET: Determine whether L128's r-branch local normalization defect is at most binom(r+1,3), sharply over all distinct quaternionic tangent-line arrangements.
CHECKED: 2026-10-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 388 searched arbitrary skew-line Hilbert functions, extremal Rao functions, normalization defects and arrangement regularity; reused the four-branch primary assessment and checked new primary arrangement and quadric sources, with queries and limits below.
SOURCE_EVIDENCE: Reused Derksen--Sidman (2002), Theorems 1.2/2.1 and inspected Section 2 proof; read Stacks Lemma 29.4.6 with its affine exactness proof; inspected Migliore--Nagel--Peterson--Turatti arXiv:2605.19434v1, Section 4.1, Propositions 4.2/4.4 with proofs; compared Derksen arXiv:math/0510584v1, Definition 4.5 and Theorem 4.6/Corollary 4.7 statements.
COMPARISON: Known results supply the all-degree regularity cutoff, binary scheme-union exact sequence and a skew-line-on-quadric comparison; none of the inspected statements is the proposed uniform completed normalization-length bound for all quaternionic arrangements.
GAP: Specialize union exactness and elementary linear-ideal restriction to bound the whole normalization quotient uniformly; separately verify an admissible quaternionic equality arrangement and the algebraic length comparison using L128. These remain mathematical tasks, not results of this review.
REASON: Essential source scope is now sufficient for one bounded specialization attempt on the unchanged target; reprove no general regularity or liaison theorem, and do not substitute generic Hilbert functions or product-ideal series for the required intersection-ideal ranks.
SCOPE: Conditional local normalization defect for an entire finite r-point fibre under L118/L120/L121/L128, all tangent-span dimensions allowed within quaternionic dimension 39; no generic-position assumption, actual collision existence or global bound.

## Proposed test and relevance

The main gap is universal primitive rational Hodge realization. The
intermediate target is one uniform sharp bound for the local normalization
quotient, using the actual formal model now verified in L128. Its possible
downstream use is to control contributions of arbitrary finite collisions
in a later global normalization/Euler calculation; neither that global
comparison nor a contradictory numerical threshold is available here.
This uniform target is intended to avoid a succession of separate
five-branch, six-branch and higher finite-jet lemmas.

Let g:B -> Z be the actual finite normalization and z the selected point
with its entire fibre of size r. The defect to bound is the algebraic
length of (g_*O_B/O_Z)_z. Test the proposed upper bound binom(r+1,3),
with sharpness only among distinct quaternionic tangent-line arrangements.
A tangent arrangement witnessing sharpness would not establish an actual
K3 collision or a common kernel. The expression is a proposed threshold,
not a result established or literature-approved in step 387.

Essential inputs are L118, L120, L121 and audited L128. Retain locally free
rank-two Omega-polystable F with integral c_1=0 and
ch_2=-14e_1-21e_2-tau_D on the identical marked K3 factors, common
quaternionic structures, pullback scale 2lambda and ambient quaternionic
dimension 39. F and collisions remain unproved. The lines are quaternionic
one-dimensional and complex two-dimensional; the complex projectivizations
are pairwise disjoint lines. Both ambient span and relative positions may
be special. Any primary theorem must retain that scope rather than assume
generic skew lines, a connected projective union or equidimensional
intersection hypotheses that fail here.

Continue only after a primary theorem or adequately screened specialization
controls the whole degree range and the actual finite-length quotient.
A larger-defect admissible arrangement refutes the proposed bound and
should be preserved as informative negative evidence. If a source only
bounds regularity, identify the remaining rank/Hilbert-function difference
before approval. Persistent essential source blockage should park the
dependent calculation and lead to an independently testable target.

ATTEMPTS/070 rules out the much smaller universal value r-1 and is not
reopened. ATTEMPTS/071--072 concern curvature restrictions, not this
extremal local-algebra test. The prior coordinate discovery and audit
remain ready for their own targets; they do not authorize this new one.
Check local duplicates and exact stronger known results in the separate
review. Mathlib coverage of the proposed full bound is not checked.

## Step 388 — primary comparison and approval (2026-10-18)

This is a literature-only approval of the exact TARGET above. The
REVIEW_REQUIRED text describing step 387 remains historical context.
No proposed inequality, equality example or new lemma is proved here.
LITERATURE_REASON: The invocation explicitly requires first coverage of
the all-r extremal target; the ready coordinate and four-branch reviews
leave its uniform low-degree length estimate outside their scope.

### Reused general arrangement input

Reuse `2026-10-18-actual-four-branch-normalization-jets.md`, primary-source
section, for [Derksen--Sidman, *A sharp bound for the
Castelnuovo--Mumford regularity of subspace arrangements*, Adv. Math.
172 (2002), 151--157](https://sites.lsa.umich.edu/hderksen/wp-content/uploads/sites/614/2018/05/A.I.a.10.pdf),
Theorems 1.2 and 2.1, pp. 153--154, and its inspected complete Section 2
proof. The intersection ideal of r linear spaces is r-regular without
genericity; the stated sheaf vanishing includes H^1(I(d))=0 for d>=r-1.
The sharpness example uses an auxiliary secant line. That example alone
is not a normalization-length theorem. L121's complex projectivizations
are disjoint lines, the applicable scope; checking the restriction
sequence and the finite low degrees remains part of the specialization.
No need to reproduce the general theorem's induction or saturation proof.

### Binary union, rather than pairwise replacement

[Stacks, Lemma 29.4.6](https://stacks.math.columbia.edu/tag/01QX),
read with its entire affine exactness argument, gives
0 -> A/(I intersect J) -> A/I direct sum A/J -> A/(I+J) -> 0
for ideals in any ring. The last map is the difference of restrictions.
This permits an inductive union calculation without replacing simultaneous
intersections by pairwise gluing. The next attempt may test product-ideal
containment after restriction to the added plane. Its exact colength
estimate and summation have not been supplied by this review. No separate
citation or reproof of a target-equivalent bound is being hidden here.

### Primary sharpness comparison, with limited import

[Migliore--Nagel--Peterson--Turatti, *Weak and strong Lefschetz
properties for Hartshorne--Rao modules of curves in P^3*,
arXiv:2605.19434v1, 19 May 2026](https://arxiv.org/pdf/2605.19434v1),
Section 4.1, printed pp. 21--23, was read through the complete proofs of
Propositions 4.2 and 4.4. Over an algebraically closed characteristic-zero
field, these treat r skew lines on a smooth quadric. Proposition 4.2's
proof identifies the Rao module with the cokernel of the restriction
from the homogeneous coordinate ring to the direct sum of the line
coordinate rings. Its linkage argument gives degree support 0 through
r-2; its displayed resolution and the WLP conclusion are not needed for
our proposed upper bound. Their low-r cancellation conventions need not
be imported. This is a comparison source, not a theorem bounding all
arrangements. A future equality test must check an actual quaternionic
configuration, its whole restriction image, and small r separately.
No statement that every quaternionic arrangement lies on a quadric is
made, and WLP does not give the required total length automatically.

### Stronger-result and scope screen

[Derksen, *Hilbert series of subspace arrangements*,
arXiv:math/0510584v1](https://arxiv.org/pdf/math/0510584),
Definition 4.5, Theorem 4.6 and Corollary 4.7, printed p. 5, were
inspected at statement level. Transversality requires each subset's
intersection codimension to equal the minimum of the ambient dimension
and the sum of its codimensions. The conclusion compares series modulo
a polynomial and identifies sufficiently high degrees; it does not
identify the low-degree intersection-ideal Hilbert function. Theorem
4.1 is advertised for the product ideal, which must not be exchanged
with the intersection. Its proof was not read or imported. Thus this
lead does not remove the finite-degree difference addressed here.

Generic maximal-rank results remain outside the special-configuration
scope, as already checked in the four-branch review. No full matching
bound was established by this bounded search; this is not evidence of
novelty. Search snippets were used only for discovery. An inaccessible
IJPAM PDF lead was not used, and supplies no essential missing input.
A shell download of the quadric preprint failed DNS; the web PDF text
provided the complete relevant proofs, so there is no source blocker.

Queries included `disjoint lines Hilbert function lower bound r regularity
subspace arrangement Derksen Sidman`, `skew lines Hilbert function quadric
lower bound`, `disjoint lines minimal Hilbert`, `skew lines maximal Rao
function`, `disjoint lines upper bound cohomology`, `normalization subspace
arrangements delta invariant`, and `Hilbert series of subspace arrangements
Derksen transversal theorem`. Searches for stronger extremal results did
not yield an inspected theorem deciding the full target. Curve delta
results and categorical uses of normalization were irrelevant leads.

### Local comparison and exact approved work

The supplied DAG and L128 hypotheses/conclusion identify the actual
completed restriction map. L126's coverage/import paragraph and the
four-branch assessment already retain all-degree regularity. L122's
statement and ATTEMPTS/070 preserve the counterexample to defect r-1;
ATTEMPTS/071--072, as recorded in the startup, test curvature and do not
exclude this algebraic extremal mechanism. No existing all-r sharp bound
was located in these relevant local paths. Existing changes are preserved.

Approval covers the unchanged TARGET for all finite r>=1, every tangent
span in quaternionic dimension 39, and all distinct quaternionic lines.
The next proof attempt should use the binary union sequence to test a
uniform upper bound and a quaternionic real-slope/quadric model for
sharpness. These are proposed tests, not newly established intermediate
results. A complete relevant degree calculation is required; sample
arrangements cannot verify the upper bound. Canonical proofs belong in a
future lemma file, with full assumptions and the existing completion
inputs, only after that mathematical attempt succeeds.

Retain L118/L120/L121 and audited L128, the hypothetical F with
ch_2=-14e_1-21e_2-tau_D and integral c_1=0, the common structures,
scale 2lambda and ambient quaternionic dimension 39. A larger admissible
defect abandons the numerical bound. A successful sharp tangent bound
would supply a local term for a later global normalization/Euler
comparison; that global comparison, F existence, collision occurrence,
transport and universal primitive Hodge realization remain unresolved.
Mathlib: the full extremal bound was not checked; no absence claim.
