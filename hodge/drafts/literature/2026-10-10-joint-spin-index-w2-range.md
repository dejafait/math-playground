# Joint mod-two spin-index range — primary-source assessment

TARGET: Determine the joint (w_2(R_G), w_2(R_H)) values attainable by spin pushforwards of quaternionic line classes on S x S with L079's fixed c_2.
CHECKED: 2026-10-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Bounded discovery searched quaternionic-line classification on eight-manifolds, real K-theory of K3 products, simultaneous spin indices, and suspension splittings; exact queries, duplicates and inspected versus unread leads are distinguished below.
SOURCE_EVIDENCE: Read So--Theriault 1909.11129v3 Theorem 1.1, Theorem 5.9 and its spin specialization, Proposition 6.1 and proof; Hatcher Algebraic Topology Proposition 4I.1 and proof; Husemoller Fibre Bundles third edition Chapter 9 Section 1 Propositions 1.1/1.4 and Theorems 1.2/1.5; Cadek--Crabb--Vanzura corrected manuscript Section 8 stable sequence, Proposition 8.2 and Corollary 8.4 with splitting proof; ABS Table 2 and Theorems (6.9),(11.5),(12.1); Eschenburg--Hanke v2 Theorem 10.7(b). Direct URLs and qualifications are below; the audited L084 index convention is reused.
COMPARISON: Known suspension and stable-range results supply a finite calculation framework retaining real torsion and finite-rank lifts; no inspected theorem states this fixed-c_2 joint range. L050/L071 settle nonemptiness, while L079 and ATTEMPTS/043,/045,/053 leave separate-image constraints compatible. Neither the group splitting nor existence with c_2 determines the simultaneous pushforwards.
GAP: Compute the fixed-character KSp fibre, establish which stable classes lift to quaternionic lines using the cited rank-two/Euler framework, and evaluate both spin Gysin maps with their actual orientation before extracting virtual w_2. No joint range, torsion dimension, branch restriction or sufficiency for a holomorphic kernel has been calculated.
REASON: Essential source coverage now supports a separate bounded REPRODUCTION calculation using stable suspension splittings and spin Thom excision, with the finite-rank condition checked explicitly. Import the general theorems; no reproof of them or originality claim is justified.
LITERATURE_REASON: The new joint coefficient target requires torsion and finite-rank coverage absent from the ready real-structure audit; the fresh suspension/stable-range sources address precisely that missing scope.
SCOPE: Identical marked S and complex-oriented spin fibres of L079/L084; c_2=9e_1+10e_2+tau_D integrally, rank one over H, all possible lifts with these data. The images mean the negatives of the two virtual real indices for the topology test; realizability as actual images is a separate condition.

## Main gap and bounded test

The main gap remains algebraic realization of every primitive rational
Hodge class. The local gap is existence of one holomorphic F realizing
the fixed negative mixed tensor. L084's audited identification permits
a topological necessary test that retains information lost under
complexification. This literature-only step completes coverage for the
unchanged calculation target. It derives no new range or lemma; after
approval, the next work is the separate mathematical specialization.

Retain L071 for the geometric setup and finite-rank existence input,
L079 for the exact full character and all actual-image alternatives,
and L084 for the two signed real indices. A calculation must range
over every quaternionic line lift of the fixed integral c_2. Rational
GRR alone, one arbitrarily chosen stable KSp lift, or a classification
of arbitrary-rank coefficients does not meet the threshold. Define
Stiefel--Whitney classes of the virtual negatives consistently before
comparing them to the actual positive-rank images. No equality of
complexifications may be promoted to equality in KO.

Continue this mechanism if inspected primary results permit a complete
joint mod-two range, or a rigorous necessary restriction with a concrete
branch test. Abandon it as an exclusion mechanism if the complete range
adds no constraint beyond the existing independent tests. Park any
source-blocked dependent calculation and choose an independent target;
do not repeat the parked Itoh source retrieval. Passing a topological
test does not imply an actual image pair, a holomorphic F or transport.

## Recovery comparison of distinct mechanisms

1. Joint mod-two spin indices of one coefficient: selected. The
   discriminant is the simultaneous range as the full kernel lift
   varies, rather than a separate characteristic identity on each
   image. The independent-index stops do not test this coupling.
2. Direct analytic gluing of the separately constructed E_4 and J_5:
   not selected. Individual bundles give no common kernel or inverse
   transform; an essential reconstruction theorem and a concrete
   parameter problem would first need coverage.
3. Repeating standalone image parity or adjoint RR: not selected.
   ATTEMPTS/043,/045,/053 already retain compatible branches. No new
   hypothesis or discriminating test reopens those calculations.

L082's constructed J_5 and L083's E_4 are not assumed to be actual
images. Any subsequent comparison with a particular constructed branch
must justify its real topology and retain every allowable J_5, as well
as all L079 alternatives, before claiming an exclusion of F. That
comparison is not performed here. There is no cross-notebook input.

Mathlib coverage of this full joint range is not checked. No novelty
or availability claim is made. No mathematical lemma or script for this
new target has been written.

## Primary source comparison

**Suspension framework.** Tseleung So and Stephen Theriault, *The
suspension of a 4-manifold and its applications*,
[arXiv:1909.11129v3, 3 November 2022](https://arxiv.org/pdf/1909.11129v3),
Theorem 1.1, p. 1; Theorem 5.9 and the proof of Theorem 1.1, p. 19;
Proposition 6.1 and proof, pp. 19--20. The manifold must be smooth,
closed, connected and orientable, with no 2-torsion in H_1. The spin
case gives a suspension decomposition into spheres and odd-primary
Moore spaces; Proposition 6.1 explicitly covers arbitrary reduced
generalized cohomology, including KO. S meets the hypotheses by
L050's retained K3 inputs. The proof's spin case uses trivial Sq^2;
its cohomology application uses suspension and finite-wedge axioms.
The result is an additive splitting, not a ring or Gysin identification.

Allen Hatcher, *Algebraic Topology* (2002),
[Proposition 4I.1 and proof, p. 467](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf#page=476),
splits the suspension of a product of CW complexes into the two factor
suspensions and the suspended smash product. The join/cone proof was
read. Both factors here have finite CW structures. This supplies the
product framework without an unjustified torsion-free KO Kunneth
formula. Example 4.55, pp. 383--384, also records the classical
symplectic sphere fibrations. No product group is evaluated here.

**Finite rank, not just stable existence.** Dale Husemoller,
*Fibre Bundles*, third edition, Springer GTM 20 (1994),
[Chapter 9 Section 1, pp. 111--112](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/husemoller.pdf#page=132),
Proposition 1.1, Theorem 1.2, Proposition 1.4 and Theorem 1.5.
For an n-dimensional CW base and F=R,C,H with c=dim_R(F), the
section and cancellation thresholds are respectively n<=ck-1 and
n<=ck-2. Repeated splitting reduces bundles to rank
ceil((n+1)/c)-1; cancellation applies at rank at least
ceil((n+2)/c)-1. The section and homotopy-of-sections proofs were read.
This covers reduction and cancellation at quaternionic rank two on
an eight-dimensional base. Rank one needs an additional section
test; it does not follow from this stable range. Virtual ranks must
first be represented by adding trivial quaternionic summands.

Cadek--Crabb--Vanzura, *Obstruction theory on 8-manifolds*,
author manuscript dated 5 December 2007, corrected 8 July 2008,
[Section 8, pp. 11--13](https://www.math.muni.cz/~cadek/papers/8_manifolds.pdf#page=11),
especially the split top-cell KSp sequence, Proposition 8.2 and
Corollary 8.4 with its proof. The base is a connected closed smooth
eight-manifold, and lambda has c_1 reducing to w_2 of its tangent
bundle. Lambda is trivial here. Corollary 8.4 is the existence input
already used in L050/L071, not a classification of all lifts. Its
converse proof splits a quaternionic rank-two bundle with zero Euler
class into a quaternionic line and a trivial summand. This is the
finite-rank step to retain when varying a stable coefficient; arbitrary
rank and one selected lift cannot establish the required range.

**Real coefficients and Gysin maps.** Atiyah--Bott--Shapiro,
*Clifford modules*, Topology 3 Supplement 1 (1964),
[Table 2, p. 12; Theorems (6.9), p. 15; (11.5), p. 28;
(12.1), p. 30](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/abs.pdf).
The coefficient table, periodic ring identification and module form
of the Thom theorem were read. The general orientation theorem
requires a class restricting to the suspension generator on each
fibre. Its multiplicative construction supports local spin Thom
excision and the projection formula, retaining real torsion.
Eschenburg--Hanke,
[arXiv:2011.14368v2, Theorem 10.7(b), p. 35](https://arxiv.org/pdf/2011.14368v2#page=35),
gives the quaternionic-to-real Thom map for a spin bundle of rank
4m with m odd over a finite CW base. Here m=1. The inspected formula
uses the balanced quaternionic tensor with the spinor Hopf bundle.
L084's audited analytic convention and the parent assessment's
Atiyah--Singer V input fix the two index signs; they are reused.
The additive suspension isomorphism alone does not identify either
pushforward. The next proof must check the oriented local top-cell
map and its compatibility with the chosen splitting, in both factors.

**Characteristic-class convention.** Milnor--Stasheff,
*Characteristic Classes* (1974),
[Section 4, Whitney axiom and Lemma 4.1; Property 9.5;
Theorem 12.5; Problem 14-B](https://aareyanmanzoor.github.io/assets/books/characteristic-classes.pdf),
read in the TeX transcription, PDF pp. 45--48, 109, 152--153 and 176.
The primary book statements give the product/inverse convention for
total w, the mod-two Euler relation and the Euler section obstruction.
Problem 14-B records the usual realification/Chern compatibility;
it is a supporting exercise, not a computed joint index theorem.
Use these conventions on virtual negatives. A genuine actual image
is a further geometric condition. No Stiefel--Whitney value is
assigned to a kernel or image in this review.

## Bounded discovery and comparison record

Queries included: "quaternionic line bundles eight dimensional
manifolds classification KSp Cadek Crabb Vanzura"; "real K theory
K3 surface product KO torsion symplectic families index Stiefel
Whitney"; "KO K3 K-theory torsion"; "quaternionic stable c4
8-manifolds"; "quaternionic line index Stiefel"; "suspension
simply connected 4-manifold wedge"; "So Theriault suspension
4 manifold applications theorem spin arxiv"; and "quaternionic
vector bundle stable range dimension base Sp(n) rank theorem".
Primary statements were followed before larger passages. The local
duplicate search used L050/L071/L079/L084, the parent real-family
assessment, and precisely ATTEMPTS/043,/045,/053. Their earlier
existence and separate-index conclusions are retained.

Unimported leads: Blumenhagen--Cribiori--Kneissl--Makridou,
*Dimensional Reduction of Cobordism and K-theory*, 2208.01656,
Section 3.3.7, appeared as a K3 KO computation lead; its full proof
and extensions were not inspected, so no table is imported. The
original Atiyah--Hirzebruch complex spectral-sequence paper is not
used for KO differential formulas. Searches also returned Real
involution-equivariant "Quaternionic" Bloch-bundle classification;
that is a different bundle problem. No inaccessible lead is essential
to the selected suspension mechanism. Shell downloads failed DNS;
the needed primary passages were accessible through the web reader.
No PDF download or full source extract was saved as a certificate.

## Separate calculation scope and test

Import the cited general results without reproof. The remaining work
is their specialization to the exact fixed-c_2 fibre and both Gysin
maps. Establish, rather than assume, completeness of the stable-class
variation, preservation of all integral Chern data, finite-rank
representability and the relation of torsion to w_2. Track any
noncanonical splitting; a group isomorphism is not a natural
pushforward formula. No integral NS/T splitting is available.

One coherent calculation may give the complete attainable-pair set
or a rigorous necessary restriction with a concrete L079 branch
test. If the full range adds no restriction, stop this topological
exclusion route. If a branch is excluded, retain every other L079
alternative and every allowable J_5 topology. This source review
does not derive or approve a newly discovered mathematical claim;
it approves a later attempt using the listed known frameworks.
Completed kind/classification: LITERATURE / NOVELTY_UNCHECKED;
the contemplated mathematical specialization is REPRODUCTION.
