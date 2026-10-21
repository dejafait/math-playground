# Full seven-torsion incidence maps — construction coverage

TARGET: Construct and independently verify the Schaefer--Stoll Section 7 incidence pullback and fiber-norm maps for L067's full seven-torsion algebra.
CHECKED: 2026-10-16
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Scoped incidence/affine-line/fiber-norm searches in L065--L068, the saved full-descent/scalar assessments, recent histories and seven-torsion implementation found only conditional interfaces and explicit exclusions; dedicated primary-source and implementation searches are recorded below, with no matching fixed incidence certificate located and no novelty inferred.
SOURCE_EVIDENCE: Schaefer--Stoll, author long version dated 2001-06-13, Section 7 Lemma 7.5, Lemmas 7.6--7.7, Proposition 7.8, Corollary 7.9 and Proposition 7.10, printed pp. 16--19, plus Section 10.1 pp. 24--25; Stacks tags 03QR, 03BE (39.23.5(3), 39.23.6 and Proposition 39.23.9) and 0BD2; Sutherland MIT 18.783 Fall 2023 Lecture 2 Section 2.2 pp. 2--4; Magma handbook V2.29 (2026-08-03) etale auxiliary functions and descent sections; exact statements and relevant proof cases inspected 2026-10-16.
COMPARISON: The general source already defines the full incidence Galois set and its pullback/determinant norm for every odd p; finite-etale quotient and norm theorems support a rational presentation. What remains is fixed-model construction, geometric identification and complete independent arithmetic replay. Section 10's p=3 chord-slope formulas and the inspected rational-torsion seven-isogeny routines do not supply that p=7 certificate.
GAP: No rational presentation of the dual/affine-line algebra B or incidence algebra D, inclusions, free B-basis, multiplication matrix or norm certificate has been built. Exact representation cost remains to be tested; complete global power classes, functions, embeddings/local identifications and local upper bounds remain independent.
REASON: This separate literature turn closes the essential construction/convention coverage for the unchanged saved target; known-algorithm reproduction may now attempt the bounded full-domain construction without another general scalar audit or source search.
SCOPE: Only L067's exact curve at p=7, full affine-line and incidence algebras, both projection pullbacks, determinant norm on the entire input algebra via a faithful multiplication representation, independent replay and bounded rejection/preservation checks; excludes global power-class enumeration, residual-image claims, local arithmetic and Selmer conclusions.

## Primary construction and hypotheses

Use Schaefer--Stoll, *How to do a p-descent on an elliptic curve*,
Trans. AMS 356 (2004), 1209--1231, DOI 10.1090/S0002-9947-03-03366-X,
with numbering exclusively from the
[author long version, 13 June 2001](https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf).
Section 2 assumes an odd prime p and a number field K. Section 7 uses
all of E[p] minus zero. Its description as the generic case does not
assume the actual Galois image is GL(2,F_p); the action factors through
a subgroup. The finite maps therefore require no L026 premise or
unproved residual surjectivity. Set K=Q and p=7, retaining audited
L067's nonsingular curve and both full coordinate presentations.

To avoid the local L067 notation B for a two-coordinate model, write
A=R for its degree-48 algebra and B_inc for the SOURCE's B below.
Lemma 7.5 identifies nonzero elements lambda of
Hom(E[p], Z/pZ) with affine lines ell={P:lambda(P)=1} missing zero.
B_inc is the equivariant function algebra of that Galois set, not an
assumed copy of A and not A_+, the algebra of directions through zero.
The dual is the ordinary F_p linear dual; the source separately keeps
its cyclotomic/Weil-pairing twist. No chosen root of unity or arbitrary
identification of the dual with E[p] may silently erase that twist.

Proposition 7.10, printed p. 19, defines
Y={(P,ell): P in E[p] minus zero, P in ell}, its algebra D, and the two
projections pi_1 and pi_2. They give inclusions i_A:A -> D and
j:B_inc -> D. The required map on units is
u=N_(D/B_inc) composed with i_A. On geometric functions it multiplies
all values on ell; it then induces the map on seventh-power classes.
The source explicitly computes it by choosing a B_inc-basis of D:
if M_T represents multiplication by i_A(T), then
u(h(T))=det(h(M_T)). This is an imported universal construction.
The norm is multiplicative and polynomial, not a Q-linear map A -> B_inc;
a 48-by-48 rational matrix cannot represent this norm as a linear map.

The required p=7 sizes from these source sets are dim_Q B_inc=48,
dim_Q D=336 and rank_(B_inc) D=7. These are construction thresholds,
not measured ranks of any newly produced algebra. No assertion that
B_inc or D is a single number field is approved; retain every factor.

## Essential proof cases and limits of the import

Lemma 7.6 gives the homogeneous incidence-product sequence. Its proof
counts all affine lines through a point, treats other scalar multiples
separately, and reduces its kernel claim to Lemma 7.7. The latter uses
polynomials of degree at most p-1 in each variable; its line-sum proof
retains both b nonzero and b=0 and the exceptional top monomial
j=k=p-1. Proposition 7.8 applies Lemma 7.4's Sylow conditions and
Corollary 7.1 to pass to H^1. Its last invariant-surjectivity check is
stated briefly in the source; no new reproof of that step is offered.
Corollary 7.9 identifies the cohomology image using BOTH the scalar
kernel and the incidence kernel, and intersects with A(S,p) for the
unramified restriction. Reuse the ready L065/L066 source assessments
for the unchanged global/local descent hypotheses. The present target
constructs the maps only and does not claim a cohomology or Selmer
calculation by building them.

Proposition 7.10's proof is precisely pullback followed by multiplication
over pi_2-fibers. Its matrix paragraph gives a full-element rule, rather
than a test on selected global classes. Section 10.1 supplies an explicit
slope polynomial and a 3-by-3 matrix only for p=3 (and initially a!=0).
Its lines in the plane cubic are not a formula for seven-element affine
lines in the F_7 torsion vector space. Do not extrapolate that slope
polynomial, its separation assertion or its matrix to this target.

## Finite rational presentation coverage and permitted attempt

[Stacks Lemma 58.2.2, tag 03QR](https://stacks.math.columbia.edu/tag/03QR)
identifies etale schemes over a field with continuous Galois sets; its
proof constructs each orbit from an open stabilizer and a finite
separable fixed field. This justifies retaining the Galois action, not
substituting a bare abstract incidence table for a rational algebra.
[Stacks Section 39.23, tag 03BE](https://stacks.math.columbia.edu/tag/03BE)
defines the invariant algebra as the equalizer of the two pullbacks.
Lemma 39.23.5(3) proves flat-base-change compatibility by taking the
kernel of their difference. Lemma 39.23.6 identifies geometric quotient
points with orbits. Proposition 39.23.9 requires affine schemes, finite
locally free source/target, and a genuine equivalence relation; under
these hypotheses the invariant spectrum represents the quotient and
the covering is finite locally free. The inspected proof checks the
closed equivalence relation, faithful-flat descent and local freeness.
These hypotheses must be justified for any implemented quotient.

A permitted finite presentation route is the standard quotient of the
scheme of ordered independent torsion pairs (P,Q): identify direction
representatives by Q -> bQ (b in F_7^*) for incident pairs, and identify
line representatives also by P -> P+aQ (a in F_7). This describes the
intended quotient specification, not a new certified instance or a
proved identification of implementation output. The next research
step must establish that these equivalence classes give exactly the
source Y and affine-line Galois sets, verify freeness and the group-law
maps, and check all resulting rational invariant kernels. The general
quotient result above is imported; only this elementary applicability
argument and its fixed arithmetic certificates need to be supplied.
There is no need to determine a full residual Galois group or assume
its maximality to use this presentation.

The ambient product A tensor_Q A has dimension 2304; the ordered-basis
open-and-closed part has the required 2016 points, using the source's
formula #GL(2,F_p)=(p-1)^2 p(p+1), printed p. 15. This bounds the finite
ambient problem; it is not a runtime or coefficient-height bound.
A compressed equivalent presentation is allowed only with complete
mutually inverse transports and geometric justification. Do not take
one selected factor or require a splitting-field computation as an
unrecorded extra input. If a smaller presentation is not established,
the full finite quotient remains the specified fallback.

For any addition formulas import
[Sutherland, MIT 18.783 Fall 2023 Lecture 2, Section 2.2](https://math.mit.edu/classes/18.783/2023/LectureNotes2.pdf),
printed pp. 2--4: unequal x-coordinates use the secant formula, equal
coordinates require inverse/doubling cases, and O is treated separately.
The source establishes the geometric group law and its regular maps.
Reuse audited L068 for scalar multiplication and its forward convention.
Exact denominator inverses on the chosen finite domain, or certified
separate exceptional components, remain mandatory in a new instance.
Do not discard an exceptional component merely to make a division work.

[Stacks Lemma 31.18.6, tag 0BD2](https://stacks.math.columbia.edu/tag/0BD2)
assumes a finite locally free map of fixed positive degree and constructs
its norm by a multiplication determinant, independent of basis and
compatible with arbitrary base change. Its proof passes to a free
basis, takes the determinant and checks basis independence; over a
split finite algebra this is the product on the complete fiber. It
therefore supports full-domain verification after the actual rank-seven
B_inc-module and its incidence interpretation are certified. No general
norm theorem or incidence exact-sequence reproof is needed.

## Required complete finite evidence and stopping test

The one approved attempt is at the fixed curve and p=7, with no cap
extension, new curve or global unit/class computation. Preserve all
upstream bytes and the degree-47 invalid draft. Before costly arithmetic,
save the chosen presentation, conventions and unfinished reasoning.

1. Construct faithful rational presentations of B_inc and D with their
   entire bases/relations, exact inclusion images and geometric Galois-set
   identification. Check the required dimensions 48 and 336 and all
   quotient/freeness claims. Verify every denominator used by any
   ordered-pair/addition presentation on its entire stated domain.
2. Certify both pullbacks on complete algebra generators and both L067
   coordinate transports. Supply a B_inc-basis of D of size seven and
   full inverse Q-basis transports for the associated 336 coordinates.
   A candidate power basis must pass the entire invertibility test;
   numerical root matching or a defining-polynomial check is insufficient.
3. Supply M_T and independently reconstruct multiplication by every
   element of A's full 48-element basis. Check the faithful module
   representation, its algebra relations and the complete transports.
   This establishes the rule det(h(M_T)) for every h, rather than
   asserting that norms of basis elements determine all other norms.
   Include the seventh-power and constant conventions; restrict to units
   when passing to power classes. No global power-class basis is supplied.
4. A verifier independent of producer arithmetic must replay the full
   presentation, both inclusions, every rank/inverse identity and the
   multiplication representation. Compare determinant norms with an
   independently justified complete-fiber or characteristic-polynomial
   computation; finitely sampled values alone do not prove a universal
   polynomial map. Include bounded missing-fiber, wrong-incidence,
   corrupt-inclusion and wrong-norm-convention rejection cases, preserving
   originals. Save full certificates under scripts/seven-torsion/ and
   print only actual/required sizes, failures and artifact paths.

Continue to a canonical known-method result only if the full-domain
identification, ranks, norm rule and independent replay all pass.
If the one fixed presentation is computationally infeasible, or an
exceptional component or geometric identification cannot be certified,
save the failed representation and exact failing obligation and stop
this attempt. Do not claim a source impossibility or change the target
mid-calculation; a materially different follow-up needs its own review.

## Implementation, duplicate and failure comparison

Inspected the [Magma handbook auxiliary etale functions](https://magma.maths.usyd.edu.au/magma/handbook/text/1568)
and [Mordell--Weil/descent documentation](https://magma.maths.usyd.edu.au/magma/handbook/text/1570),
V2.29 dated 3 August 2026. AbsoluteAlgebra supplies product-field
representations and isomorphisms; pSelmerGroup supplies number-field
power classes under its stated base-field restriction. Neither is an
explicit fixed incidence certificate. The full three/five descent
section does not provide this seven-map certificate. The documented
pIsogenyDescent(E,P) at p=7 requires a Q-rational point of order seven;
the fake second-isogeny routine has the same kernel hypothesis and
produces a different object. No such input is supplied here, so these
routines cannot simply replace the full-torsion construction. This is
an inspected documentation comparison, not a claim about every version
or private implementation. No software was run or installed.

Queries included `Schaefer Stoll p descent incidence algebra norm lines
implementation`, `"p-descent" "incidence" algebra Schaefer Stoll`,
`"7-descent" "norm" algebra elliptic`, the exact Proposition 7.10,
and the Magma full-descent/etale terminology. Stacks finite-etale Galois
sets, finite affine quotients and finite-free norms were searched and
read as above. Search leads to Fisher's rational-torsion examples and
Cremona--Fisher--O'Neil--Simon--Stoll's explicit n-descent series were
located but their papers were not read; no theorem from them is used.
No failed search establishes novelty or absence of a matching package.
The detailed source inspection checkpoint is
`drafts/2026-10-16-conductor389-seven-incidence-source-review.md`.

Local searches were restricted to L065--L068, relevant full-descent and
scalar assessments, histories 234--245 and scripts/seven-torsion/.
L067/L068 explicitly exclude incidence; L065/L066 specify conditional
uses only. ATTEMPTS/021 retains the finite quotient obstruction, 032 the
capped zero residue, 033 the missing ordinary evaluation and 034 the
stop on repeating interfaces. Those records remain intact. This target
is a different finite input, not a reopening of a stopped scalar test.

## Relevance, remaining gaps and classification

The main gap is rank E(Q)=m(E) for arbitrary E/Q with m(E)>=2. The
intermediate target is exactly the saved incidence-map construction.
Its plausible downstream use is an additional necessary cohomology-image
constraint in L066 when complete global power classes are independently
available. This does not supply those classes or activate L066 by itself.
The analytic-rank-zero/one inputs and official rank/refined-formula scope
are unchanged from foundations/01-target-and-scope.md.

Essential local inputs are audited L067 (the complete algebra and both
basis transports) and L068 (all six geometric scalar maps). No
cross-notebook theorem or L026 premise is used in map construction.
Functions, global units/classes, embeddings/local identifications,
local upper bounds and all Selmer containment evidence stay missing.
L026 residual premises, successful localization, rational membership,
divisible Sha and arbitrary-curve comparison stay unresolved.

Mathlib full matching incidence/finite-certificate coverage: not checked;
no absence claim. The approved future work is REPRODUCTION under
SPECIALIZE. This literature step imports and compares known sources,
constructs no new lemma or mathematical script and spends no
mathematical exploration turn. No incidence polynomial, map, rank
certificate, Selmer bound or new mathematical discovery is claimed.
