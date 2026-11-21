# Lemma 940: the symmetrized H2 polynomial is not Schur-concave

## Hypotheses

Take exactly the 34 pairs (c_alpha,alpha) in L938 equation (5), with
alpha=(alpha_0,...,alpha_6), sum alpha_k=12 and sum k alpha_k=12.
For each row let k_1,...,k_12 be its increasing exponent list. Use
L939 equation (4)'s labelled degree-twelve polynomial

    P(x)=sum_alpha (c_alpha/F_alpha) product_(i=1)^12 x_i^k_i,
    F_alpha=product_(k=0)^6 ((2k)!)^alpha_k.

Define the full arithmetic average, with every permutation counted,

    Pbar(x)=(1/12!) sum_(sigma in S_12) P(x_sigma(1),...,x_sigma(12)). (1)

The domain is the positive unit simplex
Delta={t in R^12: t_i>0, sum t_i=1}. Partial derivatives below are
ambient derivatives of the polynomial (1). No coordinate has first
been eliminated. All twelve factors, including the zero exponents
which represent L938's retained M_0^12 normalization, are kept.
There is no positive-kernel, real-zero, contact, RH or Decimal premise
in this finite algebraic statement.

## Conclusion

At the interior point

    t_*=(16/27,1/27,1/27,1/27,1/27,1/27,
                 1/27,1/27,1/27,1/27,1/27,1/27),

the exact Schur–Ostrowski discriminator is

    (t_1-t_2)(partial_1 Pbar(t_*)-partial_2 Pbar(t_*))
       =82068131/1395061649180208366873946214400 > 0.                (2)

Consequently Pbar is not Schur-concave on Delta. This disproves only
the proposed global Schur-concavity sufficient mechanism for this
fixed polynomial. It does not disprove a crossing bound for L938's
integrated density, a sign property of its Laplace transform, or RH.

Within the approved 48 tuples, fifteen discriminators are positive
and thirty-three negative; none is zero. One exact witness suffices
for (2); the other tests are a bounded record, not a global sign claim.

## Proof

### Arithmetic averaging and ambient derivatives

Fix m in {1,...,6} and put

    H_m(q)=Pbar(q,...,q,1,...,1),

with m entries q. For a row's labelled exponent slots, a given subset
I of size m is assigned to the q coordinates by exactly m!(12-m)!
permutations. Thus the *average*, not the permutation sum, is

    H_m(q)=sum_alpha c_alpha/(F_alpha binomial(12,m))
                      * sum_(I subset {1,...,12}, |I|=m) q^(sum_(i in I) k_i). (3)

Repeated exponent values do not change this count: their slots are
labelled. Equivalently, with beta_k slots of exponent k assigned to
the first block, their multiplicity is product_k binomial(alpha_k,beta_k),
where sum beta_k=m. The coefficients of the inner sum in (3) are

    [z^m y^s] product_(k=0)^6 (1+z y^k)^alpha_k.                    (4)

The total coefficient count is binomial(12,m). For a full monomial
orbit, its number of distinct exponent arrangements is
12!/product alpha_k!, with stabilizer size product alpha_k!; this
also confirms the denominator 12! in (1).

Symmetry makes each ambient partial in the first block equal to
H_m'(q)/m. Euler's identity for a degree-twelve polynomial, obtained
by differentiating each monomial, gives the partial in the second
block as (12H_m(q)-qH_m'(q))/(12-m). Put s=mq+12-m. Homogeneity of
the partials, of degree eleven, therefore gives at
t=(q^m,1^(12-m))/s

    D_ij=(t_i-t_j)(partial_i Pbar-partial_j Pbar)
        =(q-1)/(m(12-m)s^12) * (s H_m'(q)-12m H_m(q)),             (5)

for i in the first block and j in the second. The power s^12 includes
the coordinate difference as well as the derivative scaling.

### A short exact witness

For m=1, (3) specializes without a large permutation enumeration:

    H_1(q)=(1/12) sum_alpha (c_alpha/F_alpha)
                                      sum_(k=0)^6 alpha_k q^k
          =N(q)/1140694410240000,                                 (6)
    N(q)=1485-2562q+9415q^2-9996q^3+6795q^4-2002q^5-63q^6.

For complete arithmetic specification, the seven integer coefficients
in (6) are exactly

    (1140694410240000/12)
           * (sum_alpha c_alpha alpha_k/F_alpha)_(k=0,...,6)
        =(1485,-2562,9415,-9996,6795,-2002,-63).

This identity uses all 34 rows in their original order and their
factorials. The row terms, exponent lists, factorial products and
coefficient checks are retained in the certificate described below.
It can also be verified directly by these seven finite rational sums
from L938's table; no transcendental values are involved.

At q=16 direct Horner evaluation yields

    N(16)=-2749469523,
    N'(16)=-948426018,
    27 N'(16)-12 N(16)=7386131790>0.                               (7)

Equation (5), with m=1, s=27, now gives

    D_12=15*7386131790/(11*27^12*1140694410240000),

which reduces to (2). Both denominators and every simplex coordinate
are strictly positive. Notice that

    Pbar(t_*)=-916489841/57070703830099433190297799680000<0.         (8)

This last value is recorded to distinguish global value ordering from
possible properties of the zero superlevel set; no conclusion about
invariance of that set is drawn here.

### Why the witness obstructs Schur-concavity on this domain

The standard input is Alexandre Ostrowski, *Sur quelques applications
des fonctions convexes et concaves au sens de I. Schur*, J. Math.
Pures Appl. (9) 31 (1952), 253–292, section II no.12, pp262–263,
and section III Theorem VII, no.17 and proof nos.18–21, pp268–272
([original article](https://www.numdam.org/item/JMPA_1952_9_31__253_0.pdf)).
It assumes a symmetric function with continuous first partials on the
product of an open interval and characterizes Schur-convexity by the
pairwise derivative sign. Applying it to the negative function reverses
the sign. The exact readable Schur-concavity formula is also recorded
in Ivo Klemes, *Symmetric polynomials and l^p inequalities for certain
intervals of p*, arXiv:1002.3938v2 (9 January 2011), section3, pp13–15,
equation (9):

    (partial_i Phi-partial_j Phi)/(x_j-x_i)>=0, x_i!=x_j

([primary author manuscript](https://arxiv.org/pdf/1002.3938v2)). The
prior assessment records that Ostrowski's extracted formula was not
readable, while its hypotheses and proof and this corroborating formula
were inspected. No uninspected book theorem number is asserted.

Pbar is a symmetric polynomial on (0,infinity)^12, so all smoothness
and symmetry hypotheses hold without a coefficient-sign assumption.
Only necessity on the fixed-sum simplex is needed. Its applicability
can be seen directly from the source's binary mixing argument: write
a=16/27, b=1/27, and for 0<h<(a-b)/2 replace the first two coordinates
by a-h,b+h. This equals the doubly stochastic mixture of t_* and its
first-two-coordinate transposition with weights 1-h/(a-b),h/(a-b).
It stays in Delta and is majorized by t_*. Schur-concavity would
require its Pbar value to be at least Pbar(t_*). Its right derivative
at h=0, however, is -partial_1 Pbar+partial_2 Pbar<0 by (2) and a>b.
Differentiability therefore gives a strictly smaller value for all
sufficiently small positive h, a contradiction. This verifies the
relative-domain specialization, without importing an orthant
sufficiency theorem into an unproved simplex assertion.

### Exact finite verification and scope

Reproduction command:

    python3 scripts/heat/l938-schur-obstruction-56.py

The complete record is `scripts/heat/l938-schur-obstruction-56.json`.
It uses only Python integers and fractions.Fraction, and records input
hashes, every check, failures, every row's two-block coefficients,
both derivative constructions and all 48 exact values. Its 1278 checks
pass with no failures. The finite checks have the following scope.

The six Newton polynomials of L938 (3) and the six Leibniz terms of its
3-by-3 determinant reconstruct all 34 table coefficients exactly,
including the ordinary-degree cancellation and the retained A_0 powers.
This is verification of the existing input, not a reproof of a new
logarithm theorem. For each row, (4)'s binomial coefficients agree with
explicit enumeration of all subsets of the twelve labelled slots.

The derivative is independently assembled by conditioning on the
ordered exponents k,ell at the two differentiated coordinates. There
are alpha_k(alpha_ell-1_(k=ell)) choices of those slots. Choose m-1
of the remaining ten slots for the other q coordinates; if their
exponent sum is u, their contribution to the ambient partial difference
at (q^m,1^(12-m)) is

    k q^(k-1+u) - ell q^(k+u),

with the first term omitted for k=0. Average over
12*11*binomial(10,m-1) equally likely assignments, then multiply by
c_alpha/F_alpha. Every coefficient agrees with
H_m'/m-(12H_m-qH_m')/(12-m), row by row. Thus the test does not
mistake a derivative along the unit simplex for an ambient partial.
The proof of the averaging counts above justifies both algorithms;
their agreement alone would not establish the mathematics.

For q in the prescribed order (1/16,1/8,1/4,1/2,2,4,8,16), all signs are:

| m | Exact signs of D_ij |
|---:|---|
| 1 | + + + - - - - + |
| 2 | + + + - + - - - |
| 3 | + + - - + - - - |
| 4 | + + - - - - + - |
| 5 | - - - - - - + - |
| 6 | - - - - - - - - |

The script checks the simplex coordinates, Euler identity, row sums
and all derivative evaluations exactly. The complete witness,
including every row contribution, and the complete sign summary and
empty failure list were inspected. The additional compact integer
identity (7) was saved and checked without adding test points. There
has been no separate later audit of this result.

The pre-existing EXPLORE assessment is
`drafts/literature/2026-11-09-l938-simplex-majorization-scope-54.md`.
The criterion and permutation algebra are standard; the source search
did not settle this particular signed polynomial. This is a local
negative result about the proposed mechanism, with no certified
originality claim beyond that search. L915/L916/L937 and the fixed-cell
stop remain unchanged.

No equality between a symmetrized integral and L938's density is used
in this algebraic obstruction. Integral preservation with its singular
face weights, ordering of the actual-theta energy-simplex laws, and
any variation-transfer implication are not supplied here. The main
L030–L032/C032a gap also retains endpoint signs, contacts, other degrees,
initialization, realization and global continuation.

## Mathlib

Full Mathlib coverage for the Schur–Ostrowski criterion and this exact
specialization is not established. The prior targeted search did not
identify a full match, which is not evidence of absence. Supporting
finite-group averaging, polynomial differentiation and rational
arithmetic coverage has not been checked for this proof. The certificate
is not a Lean verification.
