# Partial-matrix completion — source comparison

## Hypotheses

Let G be a finite undirected specified-entry graph with every diagonal
specified. A partial Hermitian matrix specifies conjugate entries on G;
each fully specified clique principal matrix is positive semidefinite.
Unspecified entries are otherwise free.

## Conclusion

Every such partial matrix has a positive semidefinite completion if and
only if G is chordal. This universal statement does not assert failure
for every matrix on a nonchordal graph. It imposes no Boolean equal-union
equations between unspecified entries. The notebook has established
neither chordality nor all-clique positivity for its proposed matrix.

## Proof

Precise citation: Robert Grone, Charles R. Johnson, Eduardo M. Sá and
Henry Wolkowicz, *Positive definite completions of partial Hermitian
matrices*, Linear Algebra and its Applications 58 (1984), 109–124,
DOI 10.1016/0024-3795(84)90207-6,
[author-hosted published paper](https://www.math.uwaterloo.ca/~hwolkowi/henry/reports/pdcomplGJSW84.pdf).
Read Section 5 definitions, pp. 118–119; Proposition 2 and its complete
proof, p. 119; Theorem 7, p. 120, and both proof directions, pp. 121–122.
Proposition 2 supplies the semidefinite qualification, including singular
clique matrices. The proof uses perturbation and a bounded subsequence;
the chordal direction completes entries successively, while the converse
uses an induced cycle. No reproof or notebook application is made.

The paper's word “nonnegative” denotes positive semidefinite, not
entrywise nonnegative. Browser text was readable but some scanned
symbols were garbled; the abstract corroborates the chordal statement.
No garbled cycle inequality or entry formula is imported. Screenshot
calls returned textual references without image data; a shell download
failed at DNS. The citation and relevant proof cases remain accessible
through the browser. No local PDF was obtained or claimed inspected.

## Singular block criterion — source coverage added 2026-10-13

Import Takashi Sano, *Moore-Penrose inverse, generalized Schur complement
and inertia*, Acta Scientiarum Mathematicarum (published 27 February 2026),
DOI 10.1007/s44146-026-00231-y,
[publisher full text](https://link.springer.com/article/10.1007/s44146-026-00231-y).
Inspected Section 2, Theorem 2.1 and its complete proof, Corollary 2.2,
and Theorem 2.6 and its complete proof. For a finite Hermitian block
matrix M=[A,B;B*,C], Theorem 2.6 states that M is PSD exactly when
C is PSD, ker(C) is contained in ker(B), and A-B C^dagger B* is PSD.
No nonsingularity or maximal-rank assumption is required. Corollary 2.2
identifies the kernel condition with range(B*) contained in range(C).
The proof obtains kernel necessity using the PSD square root, then uses
an invertible triangular congruence for both directions. Real symmetric
matrices and scalar A are covered special cases; no theorem is reproved.
The source attributes the criterion to Albert (1969), Theorem 1;
Albert's original proof was not accessible and is not claimed inspected.

Independent comparison: Olaf Dreyer, *Matrix completion and semidefinite
matrices*, [arXiv:2112.03758v1](https://arxiv.org/pdf/2112.03758v1),
submitted 3 December 2021, manuscript dated 8 December 2021. Inspected
Section 2 (7)–(13), printed p. 4; Theorem 5.1, p. 10; Theorem 5.2
and its complete proof, pp. 10–11. Its kernel argument is explicit,
but Theorem 5.1 refers to Albert for its proof. Theorem 5.2 allows
an entire free cross block; it supplies no verdict when entries of that
block must retain prescribed moments. Its later maximal-rank uniqueness
results are not used. The source criterion is known; none of these source
theorems supplies a verdict for the notebook's partially prescribed column.

## Inverse action and scalar minimization — source coverage added 2026-10-13

For the one-column energy application, additionally inspected Sano's
Lemma 2.7 and its complete proof, Section 2, at the same publisher URL.
With closed range, the Moore–Penrose inverse is the inverse of the
restriction to the kernel's orthogonal complement on the range, and zero
on its orthogonal complement. Finite-dimensional ranges are closed.
This supports inverse action on the already established orthogonal
product modes; it does not evaluate any prescribed column. The notebook
must verify its weighted coordinate realization and normalization.

For minimization import Stephen Boyd and Lieven Vandenberghe,
*Convex Optimization*, revised author-hosted slides by Boyd,
Vandenberghe and Parth Nobel,
[402-page PDF](https://web.stanford.edu/~boyd/cvxbook/bv_cvxslides.pdf),
retrieved 13 October 2026; no publication date for this revised PDF is
asserted. Read PDF pages 53–55 (first/second-order conditions and the
quadratic example), 97–99 (complete local/global proof, differentiable
optimality criterion and examples), and 105–106 (QP and least squares).
A real quadratic with PSD Hessian is convex. For a differentiable convex
objective on a convex feasible set, feasibility together with
gradient dot (y-x)>=0 for every feasible y characterizes optimality.
The QP formulation allows linear inequalities and a singular PSD Hessian.
These statements cover scalar interval minimization once the actual
quadratic and its curvature are verified; no coefficient or minimizer
is supplied. No general optimization algorithm is needed or imported.

The author-hosted book PDF returned browser errors/timeouts on its
web.stanford.edu, www.stanford.edu and stanford.edu URLs. Its indexed
Section 4.4 snippet is not theorem evidence. The inspected author slides
provide sufficient coverage independently; the book remains an unread
lead, not an essential source blocker. Screenshot calls returned no
image data; the complete relevant PDF text passages were readable.

## Multivariable optimality certificates — source coverage added 2026-10-15

The same 402-page author slides were retrieved again on 15 October 2026.
Additionally read PDF pp. 174–175, slides 5.19–5.20, including the complete
KKT sufficiency argument; rechecked PDF pp. 53–54, 97–98 and 105 for
curvature, differentiable optimality and general polyhedral QP scope.
For differentiable convex objectives and inequalities with affine
equalities, primal feasibility, nonnegative inequality multipliers,
complementary slackness and Lagrangian stationarity certify global
optimality. The proof identifies equal primal and dual values using
convexity. This sufficiency direction requires no Slater condition;
the source states its converse under Slater. The QP statement permits
any finite dimension and a singular PSD Hessian. It does not assert
existence, boundedness, attainment or strict curvature for a particular
prescribed family. These are known optimization inputs only; no family
objective or certificate is evaluated here.

## Complementary slackness and equality consistency — coverage added 2026-10-15

Yinyu Ye, *Conic Linear Programming*, December 2004, revised October
2017, [Stanford course monograph](https://web.stanford.edu/class/msande310/sdpmain.pdf):
read Section 2.3's opening scalar complementarity argument, printed
p. 42 (PDF p. 55). For nonnegative vectors, zero inner product forces
each coordinate product to vanish. This algebraic implication assumes
neither strict feasibility nor an optimization theorem. The matrix-product
extension cites Exercise 1.4; that exercise and Proposition 2.4's rank
conclusions are not imported. Also read Section 1.3.1, Theorem 1.11,
p. 13 (PDF p. 26): Ax=b is solvable exactly when no y satisfies
A^T y=0, b^T y=1. This is stated without proof there. Read the complete
pivot/back-substitution description in Section 1.5.1, pp. 23–24
(PDF pp. 36–37). Exact rational elimination is the intended application;
no rank or consistency verdict for the notebook is supplied by this source.

Coding comparison: Brouwer–Polak, *Uniqueness of codes using semidefinite
programming*, [arXiv:1709.02195v1](https://arxiv.org/pdf/1709.02195v1),
7 September 2017, Section 2.1, equations (2)–(3) and the full ensuing
scalar-block argument, printed pp. 2–3, freshly read. Feasible primal
and dual optima with equal objective have zero PSD inner product;
positive scalar dual blocks force their primal partners to vanish.
The final displayed implication interchanges the primal/dual program
labels; use the preceding correctly identified product argument only.
No uniqueness theorem, numerical certificate, attainment or equality
of the notebook's full SDP optimum is imported. The local application
must supply its own exact cancellation, weighted zero and nonnegative
slacks, rather than assume those optimization hypotheses.

The Boyd slides and book URLs returned browser errors in this turn.
Their previously assessed QP coverage remains intact; neither is an
essential source for the scalar complementarity implication above.
No prescribed completion system was formed or evaluated in this addition.

## Mathlib

Full matching chordal-completion theorem and Boolean-constrained
completion: not checked. Supporting PSD results: not checked.
Full matching singular-block range/Schur criterion: not checked.
Full matching weighted invariant energy application and supporting
pseudoinverse/convex quadratic minimization results: not checked.
Unknown availability is not evidence of absence.
Full matching scalar complementarity and linear-system alternative:
not checked; supporting rational elimination coverage is not checked.


## Polyhedral feasibility certificates — coverage added 2026-10-15

**Hypotheses and conclusion.** For a finite real matrix A and vector b,
Farkas’ lemma gives exactly one of Ax=b,x>=0 or A^T y>=0,b^T y<0.
The inequality variant allows free x: Ax<=b or y>=0,A^T y=0,b^T y<0.
No strict feasibility is required.

**Precise citation and proof inspected.** Michel X. Goemans, *Advanced
Algorithms*, Lecture 3, 19 September 2001, scribes Abhinav Kumar and
Nodari Sitchinava, distributed in MIT OCW Fall 2008,
[primary notes](https://ocw.mit.edu/courses/6-854j-advanced-algorithms-fall-2008/b23096080e3d2142c3c8337bdcd9d3c7_lect9_19.pdf),
Theorems 1 and 3, printed pp. 1–2 (PDF pp. 2–3). Read Theorem 1’s
projection proof through its strict-sign conclusion and Theorem 3’s
statement; the latter has no separate converse proof here. OCR garbles
some signs; the surrounding nonnegative-variable proof resolves Theorem 1’s
signs. Screenshot calls returned references without image data.

**Rational certificates.** MIT 6.854, 2020 collection,
[Linear Programming notes](https://courses.csail.mit.edu/6.854/20/Notes/n11-lp.html),
sections “Introduction”, “Linear Equalities” and “Basic Feasible Solutions”,
read standard-form conversion, Cramer’s-rule bit representation, the
complete movement-to-a-basic-feasible-solution argument and tight-system
reconstruction. Standard form uses nonnegative variables and slack
variables; free variables can be split. Basic solutions are recovered
from nonsingular tight systems. These provide known rational LP coverage;
no notebook witness or separator has been constructed or certified here.
The HTML is a mixed-year course compilation; no single lecture date or
new theorem number is asserted. Unrelated informal geometry claims in
that page are not imported.

**Applicability and qualifications.** The intended application is the
finite affine seven/seven system with fixed rational column data, not a
general semidefinite alternative. Reconstruct all original rows and retain
nonnegativity and equality conditions; a certificate must be checked
there, even if discovered in reduced coordinates. Neither a solver status
nor small floating residuals suffice. No general theorem is reproved.
Full matching Mathlib Farkas/rational-certificate coverage: not checked.

**Access record.** Ye’s October 2017 monograph and Stanford’s lecture04
and Cottle reference notes opened initially but bounded page requests
and screenshot retrieval timed out; shell download failed DNS. Search
extracts from those sources were not imported as theorem evidence.
The readable MIT passages above resolve the essential coverage without
requiring those inaccessible continuations. Existing Ye equality and
complementarity coverage remains unchanged.

## Joint affine-LMI feasibility — coverage added 2026-10-17

### Hypotheses and conclusion

Finite real symmetric affine matrix inequalities, including diagonal
scalar inequalities, are within standard SDP scope. A checked feasible
point or a contradictory trace certificate is sufficient; no universal
rational reconstruction or strict-separation guarantee is imported.

### Proof and precise citations

Lieven Vandenberghe and Stephen Boyd, *Semidefinite Programming*,
SIAM Review 38(1) (March 1996), 49–95, DOI 10.1137/1038003,
[author-hosted published PDF](https://web.stanford.edu/~boyd/papers/pdf/semidef_prog.pdf):
read Section 1.1 (1)–(6), pp.49–51; Section 3.1 (27)–(32), pp.63–64,
including the complete weak-duality trace argument; Theorem 3.1 and its
following counterexample, pp.64–65. Its strong-duality proof references
are unread and unnecessary here. The notebook must check the original
affine formulation and every certificate coefficient; no new finite
feasibility result is asserted by this source note.

Comparison only: Vladimir Kolmogorov, Simone Naldi and Jeferson Zapata,
*Certifying solutions of degenerate semidefinite programs*,
[arXiv:2405.13625v3](https://arxiv.org/pdf/2405.13625v3), 25 April 2025,
Sections 3–4, pp.6–9: inspected the nonempty-set/rank hypotheses,
Algorithm 4.1, Lemma 4.1/proof, Definition 4.2 and Theorem 4.3 with its
complete proof. Its maximum-rank proximity and valid-column premises
are not established locally; this algorithm is not imported for use.
The v3 numbering supersedes the initial v2 HTML lead for this review.

The exact target comparison, nonessential access failures, stronger
unimported leads and bounded certificate contract are recorded in
`drafts/literature/2026-10-17-zero-plane-remaining-mode-feasibility.md`.
No general theorem is reproved and no mathematical calculation is made
in this coverage addition.

### Mathlib

Full matching joint SDP certification and supporting exact conic-duality
coverage: not checked. Unknown availability is not evidence of absence.

## Fixed-face certificates — coverage added 2026-10-18

### Hypotheses

Work in finite real symmetric matrices with trace inner product. Let
M(x)=M_0+sum_j x_j M_j be an affine pencil. A proposed reducing matrix
S must be fixed, PSD, and orthogonal to every coefficient, including M_0.
For a proper reduction it must act nontrivially on the current cone,
after any previously justified fixed-kernel removal. These are conditions
to verify, not consequences of a numerical dual iterate.

### Conclusion

Import the following known face description: if F=U S_+^d U^T and
U^T S U is PSD, and B spans ker(U^T S U), then

    F intersect S^perp = U B S_+^r B^T U^T.

For the full cone use U=I. A checked reducing matrix orthogonal to the
affine pencil permits restriction to this face. In constraint form retain
the compressed PSD condition AND the mixed and removed-coordinate zero
equations. No minimal-face or strict-feasibility conclusion is included.

### Proof and precise citation

Frank Permenter and Pablo Parrilo, *Partial facial reduction: simplified,
equivalent SDPs via approximations of the PSD cone*,
[arXiv:1408.4685v3](https://arxiv.org/pdf/1408.4685v3), version submitted
17 May 2017, manuscript dated 19 May 2017. Read Section 2.2, Lemma 1,
equations (1)–(4), printed pp.4–5; Section 2.3, Lemma 2 and its complete
two-direction proof and ensuing restriction argument, pp.5–6;
Section 2.4, Algorithm 2 and Lemma 3 with its complete proof, pp.7–8;
and Section 4.1's complete constraint reformulation, pp.18–19.
Numbering here refers to this arXiv version, not a different edition.

Lemma 3 proves both containments using PSD trace orthogonality and
range containment. Section 4.1 explicitly retains U^T M V=0 and
V^T M V=0 alongside U^T M U PSD, with V spanning ker(U^T).
Deleting these equations is not the imported equivalence. The formula
also permits a zero-dimensional remaining kernel; retain its zero
matrix requirement rather than silently dropping the constraint.

Lemma 2's existence equivalence assumes the original feasible set is
nonempty. That hypothesis is not established here, so its existence
direction and Algorithm 2's terminal strict-feasibility conclusion are
not invoked. Remark 1, p.7, explicitly preserves infeasibility under
certified face restrictions. The application is only the checked-certificate
restriction and Lemma 3; it does not presume nonemptiness. Section 3.1,
pp.9–10, also warns that a partial reduction may miss a minimal face.
No general theorem is reproved.

### Notebook applicability and limitations

The saved step-298 model is finite and rational affine in three plane
parameters and 45 moments. Its 81 blocks and scalar inequalities can be
handled blockwise, retaining all original equations and scales. The
certificate conditions above remain to be checked on that model.
L082's scalar Schur weights alone do not supply a fixed matrix S;
L083's negative-square pairing and L084's equality consistency do not
prove fixed-face containment. The canonical weights must be transported
through the actual block normalization, with the full anchor retained.
No such transport or exposing matrix was calculated in this source review.
Rational data do not guarantee a rational feasible point or a rational
reducing matrix. Slater, maximum-rank proximity, strong separation,
convergence of a new solve and feasibility of the reduced problem remain
unasserted. Prior certification and completion comparisons remain intact.

### Mathlib

Full matching fixed-face reduction and supporting PSD trace/range
results: not checked. Unknown availability is not evidence of absence.
