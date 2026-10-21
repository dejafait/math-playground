# L033 — Enlarged paired quotient is residually irreducible

## Hypotheses

Let L=Q_3(zeta_20,pi), with zeta_20 of order 20 and pi^27=3.
Put J=log(O_L^times), V=ker(Tr_(L/Q_3)), and M=J intersect V.
Use exactly L032's admitted full presentation, integral logarithmic
basis and reciprocity-defined reference subgroup Gamma. Its audited
conclusions give

    M = Z_3 y_1 direct-sum direct-sum_(j=3)^108 Z_3 y_j.

Gamma fixes y_1 pointwise. On e_i=y_(2i+1), f_i=y_(2i+2),
1<=i<=53, its generators are u_i, v_i and w_i (1<=i<53 for w_i):

    u_i: f_i -> f_i+e_i,
    v_i: e_i -> e_i-f_i,
    w_i: e_i -> e_i-f_i+f_(i+1),
         e_(i+1) -> e_(i+1)+f_i-f_(i+1).

Every unlisted basis vector is fixed. These are the logarithmic actions
of the displayed paired and adjacent automorphisms in **Kaiji Kondo,
Anabelian aspects of the outer automorphism groups of the absolute
Galois groups of mixed-characteristic local fields**, **arXiv:2512.09231v2,
12 December 2025, section 1, Theorem 1.3 and its even-degree proof**,
printed pp. 9–11 ([versioned primary text](https://arxiv.org/html/2512.09231v2#S1)).
The hypotheses p odd and d>=2, and the adjacency case d>=5, hold with
p=3,d=108. L032 supplies the integral basis and common reference
transport, rather than assuming them from a rational theorem.

Let F=Z_3 y_1 and Q=M/F, with the induced Gamma action.
No separate x_2 shear or unit-exponent twist is included. No
O_U-linearity, field coordinates for the y_j or larger symplectic image
is assumed. L031's genuine field and lattice enter through L032.

## Conclusion

Q is free of rank 106 over Z_3. The specified subgroup Gamma acts
irreducibly on Q/3Q: its only invariant F_3-subspaces are zero and
Q/3Q, for every admitted presentation satisfying L032.

This is a **REPRODUCTION** of the inspected coefficient-propagation
method, with the integral even-degree quotient specialization written
out. L025 is a comparison of methods, not an input asserting this
field's result. No originality beyond the checked sources is claimed.
No stable-lattice/container conclusion, quotient valuation, orbit
radius, original input/action realization or finite B>=A follows here.

## Proof

### Integral quotient and reduction

Let E=sum_(j=3)^108 Z_3 y_j. L032's direct-sum equality says M=F
direct-sum E. Hence the map E -> M/F is an isomorphism of Z_3-modules:
it is surjective by the decomposition and injective because E intersect
F=0. In particular F is primitive, Q has no torsion, and the classes
of e_i,f_i form its full integral basis. This is a quotient of the
genuine J intersection, not a quotient of a sampled sublattice.

Since every generator and its inverse fixes F, the action descends to
an invertible Z_3-linear action on Q. The displayed matrices have no
y_1 term, so their induced formulas on these classes are exactly the
same. They also preserve E; this observation is not needed to identify
Q with a valued field or to give it a numerical norm. For u_i and v_i,
the inverse is obtained by reversing the added term. For w_i, its
difference from identity maps e vectors to f vectors and kills all f
vectors, so its square is zero and the inverse is identity minus that
difference. This confirms invertibility integrally in all cases.

The preimage of 3Q in M is F+3M, since a class [m] belongs to 3Q
exactly when m=3m'+f for some m' in M and f in F. Thus

    Q/3Q = M/(F+3M).

Using M=F direct-sum E identifies this with E/3E. It has dimension
106 over F_3, with basis bar(e_i),bar(f_i), 1<=i<=53. No residual
fixed y_1 line remains, and no other relation is introduced by the
quotient. Reduce the displayed integral formulas in this basis.

### Extraction and propagation for exactly Gamma

Let W be a nonzero Gamma-invariant F_3-subspace of Q/3Q. Choose

    z=sum_(i=1)^53 (A_i bar(e_i)+B_i bar(f_i)) in W, z nonzero.

If some B_i is nonzero, then (u_i-id)z=B_i bar(e_i) belongs to W.
Since B_i is invertible in F_3, bar(e_i) belongs to W, and
(v_i-id)bar(e_i)=-bar(f_i) puts bar(f_i) in W. If all B_i vanish,
some A_i is nonzero, so (v_i-id)z=-A_i bar(f_i) belongs to W.
Then bar(f_i) belongs to W and (u_i-id)bar(f_i)=bar(e_i) belongs
to W. In either case W contains both basis vectors for some pair i.
Each difference belongs to W because both the original and its image
belong to the invariant linear subspace.

For i<53, the formula

    (w_i-id)bar(e_i)=-bar(f_i)+bar(f_(i+1))

and the already available bar(f_i) give bar(f_(i+1)) in W.
Applying u_(i+1)-id gives bar(e_(i+1)). Thus an available pair
propagates one step right. For i>1 the second changed-vector formula
for the adjacent generator w_(i-1) gives

    (w_(i-1)-id)bar(e_i)=bar(f_(i-1))-bar(f_i).

This gives bar(f_(i-1)), then u_(i-1)-id gives bar(e_(i-1)).
Thus it also propagates one step left. Starting at the extracted pair,
finite iteration reaches the right endpoint 53 and left endpoint 1.
All 106 basis vectors belong to W, so W=Q/3Q. This covers every
nonzero W and proves irreducibility for the specified subgroup itself.
No group-generation or characteristic-at-least-five classification
theorem is used; every coefficient extracted here is a nonzero element
of F_3, and no division by 3 occurs.

### Scope and continuation test

The positive verdict passes the approved intermediate test. It repairs
only the residual-irreducibility premise after quotienting by the fixed
line. L032's whole-kernel reducibility and ATTEMPTS/024 remain valid.
Although the quotient admits this linear basis description, there is
no assertion that field valuation descends through F. A projected
container and its relation to an original numerical enclosure require
separate assessed work, as do fixed-line control, actual/native actions
and inputs, packet/global realization, pilot transport and essentiality.
The original finite B>=A gap remains open. The separate critical audit
below validates this result; it is not an IUT flaw candidate.

### Separate critical audit, 2026-10-08

The independent audit finds no error requiring a change in hypotheses
or conclusion. It verifies this existing known-method specialization;
it adds no homothety, valuation or numerical conclusion. The precise
Kondo citation and its inspected even-degree action coverage are reused
from the prior assessment. No new source inspection is claimed.

The only direct local input is audited L032. Its complete integral
basis, rather than just its rational trace-kernel statement, makes
E a complement to F inside the genuine M. In particular, if 3m is
in F, writing m=f+e forces 3e=0 and hence e=0. Thus no 3-torsion
is hidden in Q. The same direct sum proves Q is free of rank 106.
For reduction, [m]=3[m'] if and only if m-3m' belongs to F;
this gives precisely F+3M as the kernel of M -> Q/3Q. In the
direct-sum coordinates this is F direct-sum 3E. The quotient has
exactly the 106 displayed residual coordinates and no further relation.

To check the induced actions independently, abelianize L032's three
adjacent words. The exponent sum of the a_i word is
e_i-f_i+e_(i+1)+f_(i+1)-e_(i+1)=e_i-f_i+f_(i+1).
The exponent sum of the b_i word is
e_(i+1)-f_(i+1)-e_(i+1)+f_i+e_(i+1)+f_(i+1)-e_(i+1)=f_i.
The a_(i+1) word has sum
e_(i+1)-f_(i+1)-e_(i+1)+f_i+e_(i+1)
=e_(i+1)+f_i-f_(i+1). The unlisted b_(i+1) and y_1 are fixed.
Thus all matrices in the statement act on E with exactly the asserted
signs and no discarded y_1 component. The paired words similarly
give f_i+e_i and e_i-f_i. For each of the three matrix families,
N=h-id satisfies N^2=0, so (id-N)(id+N)=id integrally.
Consequently descent, reduction and the inclusion of inverses introduce
no extra action hypothesis. This verifies the selected reference action,
not arbitrary lifts with unit-exponent twists.

For nonzero invariant W, subtraction h(z)-z remains in W. If a
B_i is nonzero, u_i-id kills every other coordinate and extracts
B_i e_i; after scaling by B_i^(-1), v_i-id extracts -f_i.
If every B_i is zero, some A_i is nonzero, and v_i-id extracts
-A_i f_i; scaling and then u_i-id recover the pair. This covers
all nonzero vectors, including mixed coefficients and multiple
nonzero pairs. The only inverses of coefficients are those of nonzero
elements of F_3; the minus sign is nonzero in characteristic three.

Starting with e_i,f_i, applying w_i-id to e_i and adding f_i
gives f_(i+1), then u_(i+1)-id gives e_(i+1). This uses w_i
only when i<53. Applying w_(i-1)-id to e_i and adding f_i
gives f_(i-1), then u_(i-1)-id gives e_(i-1); this uses
w_(i-1) only when i>1. Iteration from any starting pair therefore
reaches all pairs 1 through 53, including both endpoints, without
an undefined w_0 or w_53. No division by 2 or 3, exceptional
characteristic assumption or larger symplectic-image assertion enters.
Hence the proof really establishes residual irreducibility for Gamma.

L031 enters only through L032's audited genuine-field/lattice input;
its determinant and explicit logarithm columns are not used by this
audit. L025 is still only a method comparison. Whole-kernel reducibility
persists, and no quotient field valuation, projected-container invariance,
fixed-line bound, actual/native input or essential IUT flaw is established.

## Mathlib

Full matching enlarged-field integral quotient and residual-action
theorem: **not checked**. Supporting free quotient, reduction and
invariant-subspace results: **not checked**. The complete elementary
specialization is supplied above using L032 and the precise primary
source; unknown Mathlib coverage is not evidence of absence. No formal
verification is claimed.
