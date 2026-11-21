# Rectangular coupled differential interface — source review1288

Literature-only checkpoint: primary statements and the relevant kernel,
adjoint and boundary passages have been inspected. No rectangular kernel
identity has been derived, no theta substitution or coefficient elimination
has been made, and no existence or nonexistence verdict is claimed.

The main gap is L030-L032/C032a actual-Xi positivity in every degree.
The intermediate question is the fixed scalar-input/two-output interface
in nomination1287. Its possible use is organizing C032f(5)'s relative
output comparison; an interface alone would not prove that comparison.

## Primary sources actually inspected

W. Riley Casper, F. Alberto Grünbaum, Milen Yakimov and Ignacio Zurrián,
*Matrix valued discrete-continuous functions with the prolate spheroidal
property and bispectrality*,
[arXiv:2302.05750v2](https://arxiv.org/html/2302.05750v2),
14 February 2024. Inspected Definitions2.2-2.4/2.10, Section2.3
(2.4) and its formal-adjoint formula, Definition5.3/Proposition5.4,
Definition5.9, Theorem6.1 and its proof of(6.3), plus the statement
of6.2. Version1's first page was opened; numbering here is version2.
The right action is F.D=sum F^(j) B_j; the adjoint reverses products,
transposes matrices and replaces derivatives by their negatives.
Proposition5.4 is Green's identity for smooth square matrix functions
of compact support on a possibly infinite open interval. Its proof is
left to the reader. Definition5.3 specifies the boundary concomitant.
Theorem6.1 requires a square discrete-continuous bispectral function
and a bi-self-adjoint Fourier-algebra element; (6.1) is the finite-sum
Gram kernel sum_k Psi(k,x)^*Psi(k,y). Proof(6.3) transfers derivatives
and shifts using both boundary conditions and the bispectral relation.
It is not an arbitrary rectangular-intertwiner theorem. Statement(6.4)
has inconsistent notation; neither it nor an existence conclusion from6.2
is imported.

W. Riley Casper and Milen T. Yakimov, *Integral operators, bispectrality
and growth of Fourier algebras*,
[arXiv:1807.09314v2](https://arxiv.org/pdf/1807.09314v2),
24 October 2018; journal DOI
[10.1515/crelle-2019-0031](https://doi.org/10.1515/crelle-2019-0031).
Inspected Section3.4 p.20 and Section5.1/Theorem5.1 with its complete
proof p.25, including preceding(18)-(19). The theorem assumes a
bispectral meromorphic function, holomorphy near the two curves, all
polynomially weighted derivative integral bounds(19), and a bisymmetric
Fourier-algebra operator holomorphic near the first curve. Its conclusion
is core commutation for the product kernel integral psi(x,z)psi(y,z)dz.
The proof moves the Fourier partner across the inner integral, then
the original operator across the outer integral, using symmetry twice.
No such bispectral realization or partner is supplied for our kernels;
this is a scope comparison, not an application of that theorem.

Reuse Gordon Blower, *Hankel operators that commute with second-order
differential operators*, J.Math.Anal.Appl.342(2008),601-614,
[DOI](https://doi.org/10.1016/j.jmaa.2007.12.028),
[arXiv:0712.1013v1](https://arxiv.org/pdf/0712.1013v1),
Theorem2.1 proof(2.3)-(2.5), pp.3-4, and Proposition3.2(3.3),
pp.5-6, already inspected in source-notes1284. That exact scalar
compact-core identity is available; it does not assert a rectangular
matrix extension. Reuse1284's Yafaev domain comparison without browsing
the same scalar theorem again.

## Search and local duplicate/failure comparison

Queries included `"matrix valued" "Hankel" "differential operators"
intertwining`; `"rectangular" "integral" "bispectral" differential
operators`; `matrix valued integral operators intertwining differential
operators kernel Fourier algebra Casper Yakimov`; the exact titles above;
`"Hankel" "rectangular" "differential operator"`; `"matrix-valued"
"Hankel" "intertwining" differential`; `"integral transform"
"rectangular" "bispectral"`; `"matrix" "Hankel" "Sturm-Liouville"
commutation`; and `"Hankel operators" "intertwine" "differential"`.
No adequate theorem deciding this fixed four-kernel class was located.
This bounded search is not evidence of originality or a classification
of all relevant literature.

Targeted local searches covered the C032 files and 17November commutant,
theta-source and attempt paths, followed by exact source IDs, author pairs,
rectangular-intertwiner and matrix-bispectral terms in drafts/literature,
drafts/working and ATTEMPTS. The only extra rectangular-commutation hit,
`drafts/literature/2026-11-05-theta-additive-degree-compatibility.md`
(Campbell-Jalowy paragraph), concerns polynomial-degree Appell compatibility,
not this half-line integral interface. Existing675/677's Blower comparisons
are reused. No matching rectangular theta calculation was located in
these searches; no global absence claim is made.

C032h's full proof and audit1287 exclude the identical scalar expression
on both components, with one common p,q. The proposed independent matrix
P,Q is outside that statement, even if it were diagonal. Nondiagonal
coupling must therefore be retained in a future test. Nothing here proves
that it survives, or that it reduces to C032h. Preserve stop1283: separate
scalar symbol/inertia representations do not compare the squared paired
outputs. The older pointwise, compact-exact, corona and boundary-cloud
stops referenced there are not reopened.

## Exact applicability boundary and future necessary-condition test

Retain C032f(1)-(5), using only its accepted reduction for motivation;
the later witness calculation is unnecessary. C032e supplies the full
smooth positive Psi and bound(8). Keep H=L2(0,infinity;C),
Y=L2(0,infinity;C^2), both unweighted, and one common compact smooth
scalar input for both tilt components. Keep the same fixed c and all
four kernels. In particular do not substitute a square matrix kernel
with two independent inputs to invoke a source theorem.

Seek T_H f=-(p f')'+q f and T_Y g=-(P g')'+Q g, with real scalar
polynomials p,q and real symmetric matrix polynomials P,Q, each of
degree at most two, p(0)=0, P(0)=0, p(x)>0 and P(x) positive definite
for x>0. The proposed equalities T_Y A f=A T_H f and
T_Y B f=B T_H f are local smooth-function identities on the open
half-line. No closed realization or strong commutation is assumed.

The bounded future test is to establish the necessary rectangular
kernel identities by compact-core differentiation and integration by
parts, then compare their polynomial coefficients without deleting
off-diagonal entries. Cite the known Green identity, but justify its
use for the differently sized input and output rather than citing a
nonexistent rectangular theorem. Because this is precisely the local
dimension and action-convention difference not settled by the sources,
its proof belongs to a later research turn. If using a compact cutoff
to apply Proposition5.4 to a kernel slice, justify that the cutoff is
one on a neighborhood of the input support. Do not assume that the
kernel slice itself is compactly supported. Account for left versus
right action, transpose/conjugation and both endpoint brackets.

The discriminator is compatibility versus contradiction within this
fixed class. A contradiction from a necessary subset rejects the full
class; a surviving subset is only an unpaid necessary condition. Retain
linear p, possibly constant q, all matrix degeneracies allowed by the
stated positivity, and the unaltered b_sigma coefficients. No division
by a matrix or coefficient polynomial is allowed without checking its
domain of invertibility. No higher degree, rescaling, truncation, new
metric or full self-adjoint domain construction is included.

This is ready EXPLORE coverage for a bounded algebraic/core attempt,
not a new rectangular result proved here. The matrix concomitant is a
known input; the fixed-theta verdict remains uncomputed. Domain
realization, spectral multiplicity, the relative spectral bound,
actual-range inclusion, delta, source-norm transport, independently
signed Xi, initialization and all degrees remain open. Full matching
Mathlib coverage is unchecked. No RH candidate or cross-notebook input.

The missing independent signed-Xi interface blocks a justified central
creative nomination. This auxiliary fixed-class development is not
relabeled creative to satisfy scheduling. After a rejection, park this
class rather than automatically increasing degree. If the finite test
stalls, preserve its exact conditions and reassess its usefulness before
another attempt. Newly prepared continuations receive separate approval.
