# L017 — Exact certificate for the disjoint triple's nonprime isolated branch

## Hypotheses

Let F=F_(97^20), H be the order-sixteen subgroup of F_97^*, and
C=RS[F,H,8]. Use the pinned event on 1/4<=delta<5/16 and L010's
moment map sigma. Suppose a,b have four-error representatives e0,e1,e2
at parameters 0,1,2 with respective supports

    A0={1,8,12,18}, A1={22,27,33,47}, A2={50,64,70,75}.

All twelve weights are nonzero and may range over the full field F.
The eight-by-twelve matrix of -sigma(e0)+2sigma(e1)-sigma(e2)=0
has rank eight. Choose any F_97 basis z1,...,z4 of its kernel. Write
u_r=sigma(e0_r), v_r=sigma(e1_r)-sigma(e0_r) for the errors of
the r-th basis vector.

For a four-set K in H put f_K(X)=product_(x in K)(X-x)=sum_j f_j X^j
and define the four-by-four matrix

    M_K(T)_(i,r)=sum_(j=0)^4 f_j*(u_(r,i+j)+T*v_(r,i+j)),
    i=1,...,4, r=1,...,4.

Assume there is a parameter t in F minus F_97 with a four-error
representative on K such that det M_K(T) is not the zero polynomial.
This last condition is on the fourth-support recurrence determinant,
not L010's Hankel determinant D.

## Conclusion

The exact finite certificate below gives

    B(a,b)={0,1,2,t}, hence |B(a,b)|=4.

The normalized moments are defined over F_(97^2), up to a common
nonzero scalar; t has degree two over F_97. No further sparse point
exists even on the projective syndrome line over the algebraic closure.
The numeric exclusion explicitly depends on the complete exact
certificate, rather than an analytic classification of the determinant
factors. In particular this is a restriction on the stated isolated
branch, not on every pencil with this triple or on arbitrary triples.

For this fixed triple the certificate finds 201 irreducible quadratic
factor occurrences, accounting for all 402 nonprime target-field root
occurrences. There are no irreducible quartic factors with such roots
and no larger kernels at those roots. Each factor gives an actual pencil
with exactly four bad parameters. Conjugate occurrences are retained
without assuming that they are distinct projective lines.

The four zero-determinant supports are

    {1,12,22,64}, {8,27,50,75}, {8,47,64,75}, {12,33,47,50}.

Their families are outside the conclusion. Thus a sixteen-count equality
pencil with this triple, if any, can have a nonprime bad parameter only
on one of these four supports. A pencil with all bad parameters in the
prime field is also outside this branch exclusion.

## Proof

L010 proves ker(sigma)=C, minimum codeword weight nine, uniqueness of
weight-at-most-four representatives and the converse locator test.
The triple relation follows by applying sigma to the three affine
parameters. Its twelve columns are nonzero scalar multiples of twelve
distinct Vandermonde columns; any eight are independent. Hence its
kernel has dimension four over F_97 and every extension. Write the
actual weight vector as sum_r z_r*zr, with z_r in F.

A syndrome m lies in the moment space on K exactly when
sum_j f_j*m_(i+j)=0 for i=1,...,4. Necessity is evaluation of f_K
at its four roots. For sufficiency solve the first four moments by
Vandermonde inversion on K; the monic recurrence successively recovers
moments five through eight. Thus the fourth error is equivalent to
M_K(t)z=0, retaining nonzero actual weights separately. This does not
assume that a fabricated locator comes from a valid error word.

The nonzero polynomial det M_K(T) has degree at most four, so the
minimal polynomial of t over F_97 divides it. A degree-d irreducible
factor has roots in F_(97^20) exactly when d divides twenty, by the
finite-field root description in Milne, *Fields and Galois Theory*,
v5.10 (September 2022), [printed p. 53](https://www.jmilne.org/math/CourseNotes/FT.pdf#page=53). Since t is nonprime, d is two
or four. Cubic roots do not belong to the specified field. The fixed
triple's disjointness also shows that D and every coordinate locator
are nonzero polynomials: D(0) is nonzero by the full error at zero;
a persistent coordinate locator would place its coordinate in both
disjoint supports A0 and A1 by L010's pointwise identity.

The command

    python3 scripts/coefficient-feasibility/extension_roots.py

records `scripts/coefficient-feasibility/extension-root-result.json`.
It exhausts all binom(16,4)-3=1817 other supports K. Each determinant
is computed by signed permutation expansion, and independently evaluated
by scalar elimination at five distinct prime-field points, checking
every coefficient. Its squarefree radical is factored exactly over
F_97, with product reconstruction and irreducibility checks. The degree
sum of the selected quadratic and quartic factors is independently
compared with

    deg gcd(radical,T^(97^20)-T) - deg gcd(radical,T^97-T).

This accounts for all target-field nonprime roots, not a sample of them.
The exhaustive factor and kernel conclusions are:

| Exact certificate quantity | Value |
| --- | ---: |
| Fourth supports tested | 1817 |
| Zero determinants retained outside this branch | 4 |
| Selected irreducible quadratic factor occurrences | 201 |
| Selected irreducible quartic factor occurrences | 0 |
| Nonprime target-field root occurrences | 402 |
| Rank-three full-weight factor representatives | 201 |
| Larger kernels or rejected full weights | 0 |
| Representatives with any lower-weight parameter | 0 |
| Representatives with regular four-error count other than four | 0 |
| Full L010 sixteen-count equality representatives | 0 |

For every selected irreducible f, the script works in the exact field
K_f=F_97[alpha]/(f), checks alpha^(97^20)=alpha, and computes the
kernel of M_K(alpha) by elimination. Its dimension is one in all
201 cases. The kernel remains one-dimensional over F, so every
permitted actual z is a scalar multiple of this vector, after one
of the two embeddings of K_f into F. The reconstructed twelve error
weights and four fourth-error weights are nonzero. All eight moments
are compared to the independently solved fourth Vandermonde system.
The certificate retains these factors, matrices' ranks and weight
vectors, not merely the final counts. Finite field multiplication is
checked against independent prime-polynomial reduction; inverses are
checked by multiplication and Fermat powers on control elements.

It remains to justify what the exact count computation proves for
each recovered pencil. Reconstruct its five actual signed-minor locator
coefficients from its affine moments, check all four recurrence identities,
and check those minors independently by scalar elimination at five
points. Select tau in F_97 where D(tau) and all sixteen coordinate
locators are nonzero. Such a tau exists: their total degree is at
most 68, below 97. Replace the direction v by u+tau*v. Homogeneity
gives the polynomial transformation

    L_new(T,X)=(1+T)^4*L_old(tau*T/(1+T),X).

Every new coordinate locator has degree four. The point at new infinity
is the selected nonsparse old tau, so this chart loses no sparse point
of the projective line. This change is used only to audit its sparse
points; the conclusion refers to the original parameters.

For each coordinate locator ell_x take its monic squarefree radical
and multiply these sixteen radicals to obtain J(T). A root's
multiplicity in J is the number of distinct vanishing coordinate
locators, even when an individual locator has a repeated root. By
L010, after removing roots of D, the multiplicity-four factor of J
is exactly the regular four-error parameter polynomial W(T).
The certificate proves that the common gcd of all coordinate locators
is one. L010's lower-weight multiplicity identity then excludes every
weight-zero, -one, -two or -three parameter over the algebraic closure.

In all 201 cases W has degree four and equals, coefficient by
coefficient,

    product_(gamma in {0,1,2,alpha})
      (T-gamma/(tau-gamma)).

This is an independent comparison with the four known errors, beyond
the degree count. The factor has four distinct roots in K_f, and
gcd(W,T^(97^20)-T)=W. Thus no additional four-error or lower-weight
parameter exists over F or the algebraic closure, including old infinity.
Frobenius conjugation preserves every polynomial identity, kernel rank,
full-weight gate and exact-field count, so the same conclusion holds
for the other root of f. Arbitrary scalar multiples preserve the sparse
parameters and the original event. Adding codewords to a or b also
preserves agreement and failure on every restriction. This covers the
actual input pair, rather than just the chosen representatives.

L010's same-support failure argument therefore identifies these four
sparse parameters with B(a,b). At each of 0,1,2,t its error has weight
four, and there are no further parameters. This proves the conclusion
with the stated finite-certificate dependence. For the excluded three
supports K=A0,A1,A2 there can be no new four-error parameter: two
errors on a fixed four-set would represent the whole pencil there
and force persistent locators, contrary to the disjointness argument.

For a concrete representative, take alpha^2+55alpha+74=0,
K={1,8,79,85}, and the weights, in the displayed support orders,

    e0=(33+25alpha,30+79alpha,16+44alpha,29+29alpha),
    e1=(11+69alpha,26+14alpha,82+87alpha,95+76alpha),
    e2=(22+45alpha,67+13alpha,15+77alpha,1),
    e_alpha=(33+33alpha,30+7alpha,3+83alpha,61+23alpha).

The script independently interpolates the original event on all 2517
admissible supports for a=e0, b=e1-e0 in its transformed chart. It
finds exactly the corresponding four parameters, which map back to
{0,1,2,alpha}; it checks that old infinity is not bad. This is an
auxiliary check of the finite-certificate example, not a general bound.

The audit also forms the actual resultant product, imports Milne
Proposition 4.35(b), [printed p. 58](https://www.jmilne.org/math/CourseNotes/FT.pdf#page=58),
and compares all 48 residuals of the covered triangular fourth-root
test with exact squarefree multiplicity decomposition. Every candidate
fails the fourth-power identity. It keeps coordinate simplicity,
candidate squarefreeness, D-coprimality and specified-field splitting
as separate gates. These checks reproduce the local equality test;
they do not prove a global fifteen bound. The existing eleven-count
witness remains stronger than every pencil in this tested branch.

## Mathlib

The full nonprime isolated-branch restriction and its finite certificate:
**not checked** in Mathlib. Supporting finite-field quotient arithmetic,
kernel descent, Vandermonde and locator incidence coverage elsewhere:
**not checked**. No Lean verification or full matching theorem is claimed.

Supporting resultant product and specialization coverage is **present**
in the previously inspected
[Resultant.Basic at commit 300d0e535721bc098547106fc297d8ba2a63f6bb](https://github.com/leanprover-community/mathlib4/blob/300d0e535721bc098547106fc297d8ba2a63f6bb/Mathlib/RingTheory/Polynomial/Resultant/Basic.lean),
including
[`Polynomial.resultant_prod_left`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Polynomial/Resultant/Basic.html#Polynomial.resultant_prod_left)
and
[`Polynomial.resultant_map_map`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Polynomial/Resultant/Basic.html#Polynomial.resultant_map_map).
The full branch exclusion is **absent from that source checked**;
coverage elsewhere is **not checked**. These are supporting audit tools.

The standard squarefree/perfect-power ingredients are imported from
Volkovich, *On Some Computations on Sparse Polynomials*, Lemmas 23–24,
[p. 48:8](https://drops.dagstuhl.de/storage/00lipics/lipics-vol081-approx-random2017/LIPIcs.APPROX-RANDOM.2017.48/LIPIcs.APPROX-RANDOM.2017.48.pdf#page=8),
and the finite-field/resultant ingredients from the named Milne statements.
They were read in the saved SPECIALIZE assessment and are reused. The
step specializes and implements the covered moment/recurrence framework;
no certified originality or advance beyond the checked literature is claimed.
