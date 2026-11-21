# Quadratic Grunsky nonlinear branch nomination1316 — source review1317

TARGET: Determine whether C031a's six full equations have a local positive-tau branch with b(0)=(1,0,0,0,0), u=400 and v(0)=160000-A/C for the fixed1307 actual constants, by a divided-residual implicit-function construction; require verified extension and rank hypotheses and keep full-disk univalence separate.
CHECKED: 2026-11-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1317 reused1315 and C031a/C031b, searched Grunsky-specific local assessments/stops/history for divided residuals, implicit functions, desingularization, Hadamard and Crandall-Rabinowitz, and performed the exact external queries recorded below. Standard division/IFT sources cover the method; no inspected source decides this actual finite system. No novelty claim.
SOURCE_EVIDENCE: Kunzinger, Lie Transformation Groups, Summer2015 notes with Dec2024 correction preface, Theorem3.2.15 and full proof p44, https://www.mat.univie.ac.at/~mike/teaching/ss15/ltg.pdf ; de Oliveira1212.2066v1 Section3 Theorem2/proof, https://arxiv.org/html/1212.2066v1 ; Crandall-Rabinowitz JFA8(1971)321-340, Theorem1.7/proof(1.9)-(1.11) pp325-326, https://jxshix.people.wm.edu/2013-taiwan/crandall-rabinowitz-1971-JFA.pdf .
COMPARISON: Hadamard division and the ordinary C1 implicit-function theorem cover a smooth extended divided system with a verified base zero and invertible dependent derivative. They do not verify these instance-specific hypotheses. The simple-bifurcation theorem additionally requires a trivial solution curve, one-dimensional kernel/cokernel and transversality; C031b's rank alone is insufficient. Linear-prescription stops do not settle this quadratic system.
GAP: Verify the divided extension, its exact base zero and its six-variable dependent derivative for a1,...,a5,v with tau free and u fixed at400, then apply the cited theorem only if all hypotheses pass. Neither that derivative nor a branch is established in this literature turn. Full-disk analytic realization remains independent.
REASON: New essential source coverage removes the method-level literature gap left by1315, permitting only the stated finite specialization after separate approval. An ordinary theorem application with explicit hypothesis checks is needed; reproof of division, bifurcation or IFT is unnecessary.
SCOPE: Exactly C031a's six full polynomial equations and fixed1307 actual constants, b=b*+tau*a, b*=(1,0,0,0,0), u identically400 and v(0)=160000-A/C. One division by tau, a base-zero check, one dependent-derivative test and conditional local C1 existence application. No higher-order branch expansion, repeated blow-up, increased degree, quadrature, weight sweep, singular-branch theorem or univalence construction. This changed ready assessment requires separate approval before research.

## Original nomination1316 (historical scope)

At nomination1316 this was uncovered, not a ready continuation or an
existence claim. No divided-residual expansion, rank computation, higher-order
calculation or implicit-function application was made in1316. C031b's
canonical proof and full first-order certificate retain the completed
result independently of the new target's approval.

LITERATURE_REASON: New hypothesis/conclusion scope: a compatible tangent does not imply an actual nonlinear branch. The proposed division by the vanishing parameter changes the function and theorem hypotheses from the unscaled finite necessary test covered in1315.

Reuse the primary implicit-function extraction if adequate; do not repeat
searches merely for scheduling. Search specifically for polynomial
parameter desingularization, divided residuals, simple bifurcation/local
branch criteria, and local Grunsky duplicate/failure records relevant to
this exact finite system. A known theorem should be imported with only
its applicability calculation later. No originality inference follows
from the first-order result or an unsuccessful search.

Continuation inputs: C031a,C031b and C030z fixed1307 actual boxes, with
L025,L027 actual definitions/signs and L019,L021,L036,L037,L917 inherited
contracts. L030-L032/C032a give intended finite-block use. Nonlinear
existence is unresolved; even success would leave pole exclusion,
whole-disk univalence, actual identification, larger blocks, singular
cases and initialization open. No RH or cross-notebook premise.

The nominated source review was to decide IMPORT, SPECIALIZE, EXPLORE or an honest
source blocker for this exact target. Stop this method if its required
extension/rank cannot be justified, retaining the first-order result;
do not infer branch nonexistence merely from a failed sufficient method.
Full matching Mathlib coverage remains unchecked. The nomination routed
the next turn to standard/high literature comparison, not creative proof work. A
central creative analytic construction is not yet specified well enough
to test, and the finite branch prerequisite remains unestablished.

## Completed literature-only review1317 — 17 November2026

**Gap, target and use.** L030-L032/C032a still require actual-Xi
all-degree positivity. This target concerns only nonlinear existence
for C031a's finite three-index match. A branch could make a later,
independent whole-disk realization test concrete. Neither a tangent nor
a local formal match supplies the actual mixed-form sign. Pole exclusion,
whole-disk univalence, identification, larger blocks and initialization
remain unpaid. No new mathematics is derived in this review.

### Inspected theorem statements and essential proof cases

M. Kunzinger, *Lie Transformation Groups: An Introduction to Symmetry
Group Analysis of Differential Equations*, Summer Term2015, current
author-hosted notes with December2024 correction preface,
[Theorem3.2.15, printed p44, PDF page50](https://www.mat.univie.ac.at/~mike/teaching/ss15/ltg.pdf).
For a smooth map P:M^m->R^l, l<=m, of maximal rank on P^(-1)(0),
a smooth scalar f vanishes there iff f=sum_i Q_i P_i with smooth Q_i.
The full proof uses submersion coordinates near the zero set, integrates
the derivative along the normal coordinates, divides by a nonzero
component away from the zero set, and patches by a partition of unity.
The coordinate case P=tau on a Euclidean product neighborhood covers
division by tau with the other coordinates retained as parameters.
The required vanishing is on the whole local tau=0 slice, not merely
at one point. Use the local coordinate case; no global manifold
patching is needed for the proposed calculation. Import the named
Hadamard lemma without reproof. It supplies no base zero of the quotient
and no invertible derivative.

O. R. B. de Oliveira, *The Implicit and the Inverse Function Theorems:
Easy Proofs*, Real Anal. Exchange39(1)(2013/2014),207-218,
[arXiv1212.2066v1,10 December2012, Section3 Theorem2](https://arxiv.org/html/1212.2066v1).
Reused1315's extraction and checked the full theorem/proof: a C1 map
on an open subset of R^n x R^m, a zero (x0,y0), and invertible
D_y F(x0,y0) give a unique local C1 graph y=y(x), with the stated
implicit derivative formula. The proof secures local injectivity,
normalizes the partial derivative, solves one scalar equation and the
remaining system inductively, then uses the chain rule and injectivity.
Import it without reproof. It gives local qualitative existence,
not an effective interval radius, analytic regularity or a global
classification at singular points. An open neighborhood of tau=0
is required before restricting the conclusion to positive tau.

M. G. Crandall and P. H. Rabinowitz, *Bifurcation from Simple
Eigenvalues*, J. Funct. Anal.8(1971),321-340,
[Theorem1.7 and proof, pp325-326, (1.9)-(1.11)](https://jxshix.people.wm.edu/2013-taiwan/crandall-rabinowitz-1971-JFA.pdf).
For F:(-1,1)xV->Y between Banach spaces, F(t,0)=0; continuous
F_t,F_x,F_tx; one-dimensional kernel and cokernel of F_x(0,0);
and F_tx(0,0)x0 outside its range for a kernel generator x0, the
local zero set is a trivial curve plus a nontrivial curve. Continuous
F_xx gives C1 parameter functions. The proof defines
f(alpha,t,z)=F(t,alpha*x0+alpha*z)/alpha for alpha!=0, with
value F_x(t,0)(x0+z) at zero. It checks a base zero and proves the
derivative in (t,z) is an isomorphism using kernel/cokernel and
transversality, then invokes IFT. Lemma1.12 is needed for exhaustion
of the local zero set. This confirms the classical division method;
it is not a direct branch theorem for our unverified variable split.
Use ordinary IFT for the proposed sufficient construction; no claim
to CR hypotheses or exhaustive branch classification is needed.

### Exact scope of the next applicability check

Reuse C031a's full finite polynomial residuals F and C031b's already
proved base/tangent formulas. Hold u=400 exactly. For tau!=0 the
proposed function is G(tau,a,v)=F(b*+tau*a,tau,400,v)/tau.
The future research must verify vanishing of the numerator on the
whole zero slice, construct its extension on a real open neighborhood,
and identify the value at zero. Merely declaring G(0)=0 would not
verify an extension. Polynomial division is an acceptable explicit
check in this fixed polynomial instance of Hadamard's lemma; no
infinite series, summability or limiting interchange is involved.
This paragraph specifies a proposed function, not a computed quotient.

Take the six dependent variables to be (a1,...,a5,v), with tau free.
Use C031b(3)'s tangent at u0=400,v0=160000-A/C as the proposed
base a0. Verify G(0,a0,v0)=0 and compute the exact dependent
derivative there. Exhibit a nonzero determinant or an equivalent
complete linear invertibility argument. C031b's unscaled rank-five
matrix is not the derivative required here, and its row relation
does not by itself decide this six-variable test. No transformed
derivative, determinant or branch result was calculated in1317.

If all hypotheses hold, apply the cited ordinary theorem and state
the resulting local C1 solution precisely; show equivalence with the
original equations for nonzero tau. Strict positivity of the limiting
weights must be combined with continuity and restriction to sufficiently
small positive tau. Use the actual constants, not an arbitrary point
or midpoint from the boxes. Reuse the inherited strict v0 bound from
C031b; no new quadrature or arithmetic-library certification is approved.
Do not promise a computable radius, analyticity, uniqueness of all
original branches or a uniform radius for every parameter in the boxes
without a separate proof. Local uniqueness in the extended variables
is only the conclusion of the cited theorem in its neighborhood.

**Continuation/abandonment test.** A verified extension, exact base zero
and invertible dependent derivative justify this sufficient local
existence application. If any check fails or remains undecided, save
the exact failed/undecided condition and stop this fixed divided-system
test. Do not continue to repeated division, higher-order equations or
a weight sweep. Failure of this sufficient method does not prove
nonexistence of a nonlinear branch. Singular, non-C1/fractional-power,
zero/diverging-weight and other regular branches remain open.

### Duplicate checks, search record and source limits

Read C031a/C031b and assessment1315, with completed review1315 in
nomination1314. Searched Grunsky-named local literature, attempts and
history for `divid|implicit|bifur|desingular|branch`, then specifically
`C031a|C031b|divided.residual|Hadamard|Crandall|Rabinowitz`.
Read stop1253, four-point stop1307 and audited unit-disk stop1311.
They concern different linear prescriptions; they supply no nonlinear
quadratic-defect solution or obstruction. The proposed division is
outside1315's necessary-first-order scope. No earlier completed local
division/existence result for this fixed system was found in that search.
This is a bounded overlap check, not evidence of originality.

External queries included: `"polynomial equations" "implicit function
theorem" "blow-up" parameter`; `"Grunsky" "implicit function" defect`;
`"divided" "Hadamard lemma" implicit function theorem parameter`;
`Crandall Rabinowitz bifurcation simple eigenvalues 1971 pdf theorem1.7`;
`"Hadamard lemma" "parameter" site:edu filetype:pdf`;
`"Grunsky" "quadratic defect" "branch"`;
`"Grunsky" "divided residual"`; `"Hadamard's Lemma" "smooth"
filetype:pdf`; and `"Grunsky" "quadratic" "local branch"`.
Search snippets and unrelated results were not theorem inputs. The
AMS crmm24 preview returned403; it is an unused lead, with accessible
author-hosted Hadamard and primary bifurcation texts supplying the
essential coverage. No persistent source blocker remains for this
finite target. No direct actual-Xi inverse-Grunsky branch theorem was
identified; an unsuccessful search establishes no novelty.

Mathlib: reuse1315's inspected official Implicit/ImplicitContDiff
coverage, including `HasStrictFDerivAt.implicitFunction` and
`ContDiffAt.implicitFunction`, as supporting tools only. Full matching
Grunsky/actual-Xi/nonlinear-branch and Hadamard-specialization coverage
is not checked here; no absence claim or Lean verification. A future
canonical proof must retain these qualifications and precise citations.

Essential inputs remain C031a,C031b,C030z's fixed1307 boxes, L025,L027
and inherited L019,L021,L036,L037,L917 contracts. L030-L032/C032a
explain the intended use. No RH or cross-notebook premise. This review
is SPECIALIZE coverage, ready only for separate approval; the proposed
construction is routine finite algebra plus a classical theorem, not
a creative central analytic mechanism. The latter remains blocked by
the absence of an independently specified whole-disk construction.
