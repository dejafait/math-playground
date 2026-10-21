# L022 — Complete sixteen-count exclusion for the saved disjoint triple

## Hypotheses

Let F=F_(97^20), H be the order-sixteen subgroup of F_97^*, and
C=RS[F,H,8]. Use the pinned event on 1/4<=delta<5/16 and L010's
moment map sigma. Suppose a,b have full weight-four error representatives
e0,e1,e2 at parameters 0,1,2, with respective supports

    A0={1,8,12,18}, A1={22,27,33,47}, A2={50,64,70,75}.

Their twelve nonzero weights may be arbitrary elements of F. No
prime-subfield restriction on a,b or any other bad parameter is imposed.

## Conclusion

The bad set satisfies |B(a,b)|<=15. This completes the restricted-triple
exclusion, including rational roots, nonprime roots and identically zero
fourth-support determinants. It depends on the complete finite
certificates stated here and in L017–L021. It does not give a global
fifteen-count bound, classify arbitrary disjoint triples, or resolve the
challenge. In particular domain automorphisms are not assumed to carry
an arbitrary disjoint triple to these three sets.

## Proof

### Moment space and separation of the remaining branch

L010 gives ker(sigma)=C and minimum nonzero codeword weight nine.
Weight-at-most-four representatives are unique. A full error at zero
gives D(0)!=0. A persistent coordinate locator would vanish at both
zero and one, placing that coordinate in both A0 and A1 by L010's
pointwise locator identity. Those sets are disjoint, so no coordinate
locator is identically zero. L010 applies: the sparse parameters are
exactly B(a,b), its size is at most sixteen, and sixteen forces full
weight-four errors with distinct supports at all sixteen parameters.

The triple weights satisfy -sigma(e0)+2sigma(e1)-sigma(e2)=0.
Its eight-by-twelve matrix has columns -x^j,2x^j,-x^j on A0,A1,A2,
for 1<=j<=8. The twelve coordinates are distinct; any eight columns
are Vandermonde columns with nonzero diagonal factors. Thus the matrix
has rank eight over F_97 and every extension. Let z1,...,z4 be the
F_97 kernel basis with identity in the final four coordinates. Write
u_r=sigma(e0_r), v_r=sigma(e1_r)-sigma(e0_r).

For a four-set K, put f_K(X)=sum_(j=0)^4 f_j X^j, the monic polynomial
with roots K, and define

    M_K(T)_(i,r)=sum_(j=0)^4 f_j*(u_(r,i+j)+T*v_(r,i+j)),
    i=1,...,4, r=1,...,4.

A syndrome on K satisfies these four recurrence equations. Conversely,
inverting its first-four-moment Vandermonde matrix gives weights on K,
and the monic recurrence recovers moments five through eight. Thus a
fourth error at t is equivalent to M_K(t)z=0 for the actual triple
kernel coordinates z, with full weights checked separately. This is
an applicability argument for the existing moment framework; determinant
vanishing alone is not treated as a sparse-error witness.

### Complete rational-root certificate

The command

    python3 scripts/coefficient-feasibility/rational_branch_audit.py

saves `scripts/coefficient-feasibility/rational-branch-audit-result.json`.
It assembles a per-root certificate missing from the earlier six-layout
aggregate report. This is an exact audit of a finite branch, not renewed
random sampling. Each of the 1817 sets K different from A0,A1,A2 is
retained with its matrix and determinant. Each determinant has degree
at most four and is independently checked by scalar elimination at five
distinct points, which checks all its coefficients.

For a nonzero determinant Delta, form its monic squarefree radical R_K
and compute G_K=gcd(R_K,T^97-T) by modular Frobenius. This is the
complete prime-field root factor, by Milne's finite-field root description
(*Fields and Galois Theory*, v5.10, September 2022,
[printed p. 53](https://www.jmilne.org/math/CourseNotes/FT.pdf#page=53)).
The script reconstructs G_K from its distinct linear factors and
records roots 0,1,2 separately. The relevant finite conclusions are:

| Certificate quantity | Value |
| --- | ---: |
| Fourth supports checked | 1817 |
| Identically zero determinants | 4 |
| Rational root occurrences outside {0,1,2} | 1329 |
| Rank-three one-dimensional kernels at those roots | 1329 |
| Occurrences rejected for a zero actual weight | 197 |
| Full-weight occurrences | 1132 |
| Audited projective moment lines | 1105 |
| Lines passing the normalized fourth-power identity | 0 |
| Lines passing full L010 sixteen-count equality | 0 |

The roots are occurrences across supports, not distinct parameters or
pencils. Every specialized kernel and its twelve weights is retained;
for full triple weights, the fourth weights are independently obtained
by Vandermonde inversion and all eight moments compared. A zero weight
is an exclusion, not an unsearched branch.

At a rational t, Gaussian elimination uses only F_97 operations.
The rank is exactly three in all 1329 cases, and remains three over F:
a nonzero three-by-three minor stays nonzero and the determinant remains
zero. Its kernel over F is therefore F times the saved prime-field
kernel vector. Every actual full-weight moment pair in this branch is
lambda*(u,v) for one saved pair and a single lambda in F^times. A saved
zero weight remains zero under every scalar multiple. This descent
covers extension weights, rather than only prime-field examples.

### Projective deduplication, charts and extension scalars

For each full-weight pair u,v the script forms all 28 minors
u_i*v_j-u_j*v_i and normalizes their first nonzero entry. The pair is
independent: if sigma(e1)=c*sigma(e0), then e1-c*e0 is a codeword
supported on at most eight coordinates, forcing it to be zero; the
disjoint full supports make this impossible. Thus those minors are
not all zero.

Every occurrence is assigned to an audited representative U,V. The
script solves, on a nonzero two-coordinate minor, for alpha,beta,gamma,
eta in F_97 and explicitly checks all eight coordinates of

    u=alpha*U+beta*V, v=gamma*U+eta*V,
    alpha*eta-beta*gamma != 0.

These equations, not the normalized key alone, certify every duplicate.
They hold over F as well. The actual pair's homogeneous moments are
lambda*((alpha*p+gamma*q)*U+(beta*p+eta*q)*V) at [p:q].
The displayed invertible matrix bijects the projective parameter line.
Multiplication of a nonzero syndrome by a nonzero scalar preserves its
unique sparse representative's support and weight. Therefore the
projective sparse-point set is preserved, including parameters at
infinity. Changes of a,b by codewords preserve the original agreement
and failure conditions on every restriction. No affine parameter count
is assumed invariant under an arbitrary projective change of chart.

Here is why the particular audited chart loses no sparse point.
For each representative's old chart, D and every coordinate locator
are nonzero and have degree at most four. Their union of prime-field
root sets has size at most 4+16*4=68<97. Choose tau in F_97 with
D(tau) and all coordinate locators nonzero; necessarily tau!=0, since
zero is a full weight-four point. Replace the word pair a,b by

    a_new=a, b_new=a+tau*b.

The actual signed minors obey the homogeneous identity

    L_new(T,X)=(1+T)^4*L_old(tau*T/(1+T),X).

This follows because each minor is homogeneous of degree four in the
moments. It is a polynomial identity, including T=-1. The script
checks it for every locator and recomputes every signed minor from the
new actual words. All coordinate leading coefficients and that of D
are nonzero. New infinity is old tau and is nonsparse: D(tau)!=0 and
no coordinate locator vanishes there. Thus every sparse point on the
projective syndrome line, including old infinity if it was sparse,
has a finite parameter in this new chart. The transformed pencil is
still nonpersistent, so L010 identifies all these finite sparse points
with its bad set and bounds their total by sixteen.

For each of the 1105 representative charts, the actual product

    R(T)=product_(x in H) ell_x(T)

has degree 64. This equals the resultant with X^16-1 by Milne
Proposition 4.35(b),
[printed p. 58](https://www.jmilne.org/math/CourseNotes/FT.pdf#page=58).
The saved triangular monic fourth-root test fixes the sixteen lower
coefficients successively using division by four. In every chart at
least one of the remaining 48 coefficient identities fails. Therefore
R cannot equal c*P^4 for any monic degree-sixteen P, even after
extension: its leading coefficient fixes c, and the triangular recursion
forces the same prime-field candidate coefficients in every extension.
An independent exact squarefree decomposition also has a multiplicity
other than four in every case. The standard recognition ingredients are
imported from Volkovich, *On Some Computations on Sparse Polynomials*,
Lemmas 23–24,
[p. 48:8](https://drops.dagstuhl.de/storage/00lipics/lipics-vol081-approx-random2017/LIPIcs.APPROX-RANDOM.2017.48/LIPIcs.APPROX-RANDOM.2017.48.pdf#page=8).
These tools do not themselves decide constrained moment feasibility.

A common extension scalar multiplies every locator by lambda^4 and
R by lambda^64, leaving its monic normalization unchanged. The failure
therefore applies to every descended input, not only the representative.
L010's equality requires c*P^4 with P split squarefree of degree sixteen,
so the failed necessary identity excludes sixteen projective sparse
points. Every original finite bad set embeds in this projective sparse
set and consequently has size at most fifteen. This handles the entire
rational-root branch, including all duplicate lines and extension scalars.

The audit additionally records coordinate simplicity, gcd(R,D), and
exact coordinate-radical parts gcd(radical(ell_x),T^(97^20)-T).
The full equality predicate includes the specified-field splitting gate;
a failed power gate is already decisive, and no hypothetical P is
claimed to split. The exact regular four-error root polynomial is also
computed using coordinate radicals and removing D-roots. Thirteen
representatives retain unclassified lower-weight roots for exact total
counting, but these do not weaken the sixteen exclusion: L010 includes
such roots, and any lower-weight bad point itself excludes equality.
No exact count is asserted for those thirteen representatives.

### Exhaustion for the saved triple

Suppose, for contradiction, that the original pair had sixteen bad
parameters. L010 then supplies a fourth finite parameter t outside
{0,1,2}, with a full four-error support K distinct from A0,A1,A2.
The certificate lists exactly four identically zero determinants:

    {1,12,22,64}, {8,27,50,75}, {8,47,64,75}, {12,33,47,50}.

If det M_K is zero, L018, L019, L020 or L021, respectively, excludes
sixteen at every full-weight specialization over F, including its
rank-exceptional locus. If the determinant is nonzero and t is not in
F_97, L017 excludes sixteen (indeed that branch has exactly four bad
parameters). If the determinant is nonzero and t is in F_97, the
rational-root audit above excludes sixteen. These are exhaustive cases.
Together with L010's upper count sixteen, they prove |B(a,b)|<=15.

The new input is this restricted-triple certificate and its assembly,
not a new resultant or perfect-power theorem. Its full exclusion is
potentially beyond the literature checked in the saved assessment;
that qualification does not certify originality. The main error interval
remains 11/q–16/q for arbitrary input pairs, against the required 15/q.

## Mathlib

Full restricted-triple exclusion, kernel-descent and finite-certificate
coverage: **not checked**. Supporting Vandermonde, rank and projective
basis-change coverage elsewhere: **not checked**. No Lean verification
or full matching theorem is claimed.

Supporting resultant product and specialization coverage: **present** in
the previously inspected
[Resultant.Basic at commit 300d0e535721bc098547106fc297d8ba2a63f6bb](https://github.com/leanprover-community/mathlib4/blob/300d0e535721bc098547106fc297d8ba2a63f6bb/Mathlib/RingTheory/Polynomial/Resultant/Basic.lean),
including
[`Polynomial.resultant_prod_left`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Polynomial/Resultant/Basic.html#Polynomial.resultant_prod_left)
and
[`Polynomial.resultant_map_map`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Polynomial/Resultant/Basic.html#Polynomial.resultant_map_map).
The full restricted-triple exclusion is **absent from that source checked**;
coverage elsewhere is **not checked**. These declarations support the
algebraic audit, not the complete constrained statement.
