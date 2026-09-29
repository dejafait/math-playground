# Minimal cubic resolution: integral-twist test

Date: 2026-09-27. Working record for the exact target assessed in
[the saved review](literature/2026-09-27-cubic-subspace-mixed-resolution.md).

The target is an actual three-presentation resolution of I_C with
factor divisor classes in L025's final W, whose terminal twist is
stable at the specified metric and has invariant c_1 and c_2.
The gap is a representative supporting the missing fourth RM direction;
the known family supplies three directions and a 21-dimensional span.
Even a successful bundle would leave transverse transport and the
universal Hodge target unresolved.

L027 forces the mixed correction R=(A-2 id) pi_W and the projections
of an integral twisting class. The first test is whether this correction
can be an integral sum of original divisor tensors minus the single
rank-one tensor coming from the twist. If this already fails, actual
section maps cannot repair it. If it passes, it supplies no maps,
exactness or stability certificate. The adequate prior EXPLORE review
is reused; no source gap in that review is being cleared this turn.

Initial checkpoint before further work: in L025's explicit pre-chamber
model, W_0 is spanned by F,O,E and its orthogonal complement is generated
by P-O-2F+E/2. The projection of the integral divisor lattice to W_0
can have half-integral E coefficient. The fixed correction tensor has
to be compared with those projected integral twists, rather than with
arbitrary rational rank-one tensors. L025's final rational conjugation
need not preserve this lattice. An obstruction in W_0 alone would not
yet exclude the exact final target. No conclusion is claimed here.

## Arithmetic calculation and provisional obstruction

The initial symbolic command could not run because SymPy is unavailable.
A standard-library Fraction calculation instead gave the correction
tensor in the basis (F,O,E,P):

\[
B_0=\begin{pmatrix}
0&-1&1&0\\
-1&1/2&1/2&0\\
1&1/2&2&0\\
0&0&0&0
\end{pmatrix}.
\]

Its O tensor O coefficient is half-integral, while that coefficient
of r pi_W(t_1) tensor pi_W(t_2) is integral for integral twists in
this initial model. This excludes that model but does not by itself
survive an arbitrary rational chamber conjugation.

A basis-independent replacement is available. For any actual vector
bundle F on S x S, the mixed component of ch_2(F) is integral:
it is alpha tensor beta minus the integral mixed component of c_2(F),
where c_1(F)=p_1^*alpha+p_2^*beta. Hence its correspondence operator
preserves the integral divisor lattice. For the saved W target, L027
forces alpha,beta to lie in K=ker(A), and its normalized character
has divisor operator A+2 pi_K. Thus ch_2(F) has divisor operator
A+gamma pi_K, gamma=2+q(alpha,beta)/rank(F). This is self-adjoint
and has characteristic polynomial f(z)(z-gamma); integrality forces
gamma to be an integer.

The divisor Gram determinant is -7, and the displayed basis is the
full lattice because an overlattice index squared would divide 7.
Modulo 2 its pairing is therefore nondegenerate and alternating.
But f mod 2 is the irreducible cubic z^3+z^2+1. The cubic and linear
primary spaces of the proposed integral self-adjoint operator would
be orthogonal nondegenerate spaces of dimensions three and one.
A one-dimensional alternating space is degenerate, a contradiction.

This is a provisional scoped obstruction to the exact saved target,
not a candidate resolution of the Hodge conjecture. Remaining checks
before promotion to a lemma: the integral Kunneth statement for ch_2,
preservation of the saturated divisor lattice, the twist coefficient,
the self-adjointness assertion, and the characteristic-two primary
decomposition. None requires section-space or stability calculations
if the contradiction stands. No arbitrary rational conjugation is
being assumed integral.

## Completed decision

All listed checks have been resolved in the full proof
[L028](../lemmas/L028-cubic-subspace-resolution-parity-obstruction.md).
The integral-basis fact is reused from L020; the forced rational
operator is reused from L027. Integral Kunneth and Lefschetz (1,1)
make the mixed ch_2 operator integral on NS(S), and its two rational
blocks make it self-adjoint. Only that integral operator is reduced
modulo 2. Its primary decomposition is obtained there by coprime
polynomials, not by reducing the rational W/K splitting.

The independent standard-library certificate
`python3 scripts/cubic-kahler/check_cubic_parity_obstruction.py`
passed, including exhaustive checking of all 1024 self-adjoint
operators on the four-dimensional alternating space. The proof
uses the general orthogonality argument, not that enumeration.

The exact saved target is excluded before actual section maps,
rank conditions or stability need testing. This is an informative
NEGATIVE / RESEARCH / REPRODUCTION result, applying known integral
Chern and alternating-form facts; no claim of originality follows
from the prior search's lack of a full match. No complete candidate
proof or disproof of the Hodge conjecture appeared. The known span
and deformation directions are unchanged. The earlier calculation
and its provisional qualifications above are preserved as the
working record, superseded by the basis-independent proof.
