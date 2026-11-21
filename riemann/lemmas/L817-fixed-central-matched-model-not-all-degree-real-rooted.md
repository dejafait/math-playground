# Lemma 817: the fixed central matched model is not real-rooted in every degree

## Hypotheses

Use L791's exact positive solution A,B,C, fixed D=B_J/2 and original
radius10^(-15) box. These four parameters are fixed as d varies. Retain
L791's inherited actual-completion, analytic-error, certified-data and
software contracts; this statement does not independently verify them.
For j>=0 and integers d>=1 define

    c=D/(AC),
    alpha_j=c^j (A)_j(C)_j/[(B)_j(D)_j],
    p_d(y)=sum_(j=0)^d (-1)^j binom(d,j) alpha_j y^j.

Here (u)_0=1 and (u)_j=u(u+1)...(u+j-1). There is no actual-Xi
root-location or simplicity assumption.

## Conclusion

There is an integer d>=1 for which p_d has a nonreal root. In
particular this unchanged fixed family cannot have d simple positive
roots for every degree d. This conclusion holds throughout the original
L791 box and its D enclosure, not merely at rounded parameter centers.

No effective failure degree is supplied. L791's five simple positive
model roots and L792's separate actual degree-five result are preserved.
Degree-dependent parameters, other reference families, actual signed
residual estimates, all-degree mixed positivity and RH remain unresolved.
This is a known-theorem application, not a new classification theorem.

## Proof

**Imported results and scope.** Use the infinite Pólya–Schur theorem
as stated in O. Katkova, B. Shapiro and A. Vishnyakova,
*Multiplier sequences and logarithmic mesh*,
[arXiv:1010.6052v1](https://arxiv.org/pdf/1010.6052v1),
28 October 2010, printed p.2, Theorem3, equivalences (iii) and (iv).
Its binomial symbols use alpha_j, whereas its entire symbol uses
alpha_j/j!; real zeros may have multiplicities.

Use A. D. Sokal, *When does a hypergeometric function pFq belong to
the Laguerre–Pólya class LP+?*, J. Math. Anal. Appl.515 (2022),126432,
[published primary text](https://discovery.ucl.ac.uk/10150527/1/Sokal_1-s2.0-S0022247X22004462-main.pdf),
pp.2–3, Theorems3 and5, specifically Theorem5 with p=q=2. Real
numerator parameters outside the nonpositive integers and positive
denominator parameters are required. LP+ membership requires a pairing
with each numerator minus its denominator a nonnegative integer.
For p=q there are no extra denominator parameters to quantify over.
This case imports H. Ki and Y.-O. Kim, *On the Zeros of Some Generalized
Hypergeometric Functions*, JMAA243 (2000),249–260,
Theorem3, [DOI10.1006/jmaa.1999.6662](https://doi.org/10.1006/jmaa.1999.6662).
Sokal's theorem and proof were inspected; Ki–Kim's original proof was
not retrieved or independently audited. These are theorem imports.

The prior IMPORT assessment is
`drafts/literature/2026-11-05-fixed-model-classification-application.md`;
its underlying source comparison is
`drafts/literature/2026-11-05-fixed-matched-model-all-degree-scope.md`.
Only normalization and exact-box applicability are established below.
No multiplier characterization or hypergeometric necessity is reproved.

**Whole-box arithmetic.** L791 gives exact finite-decimal centers

    A_0=35.6309307137600661975195539113178411836878763333606566614993963425894747837,
    B_0=11.5396899408362113695275954198992597350375534869564808109911297157568358833,
    C_0=4.05445979673638286096848518914467946155196456913726344707711370176031147267,

with |A-A_0|,|B-B_0|,|C-C_0|<=10^(-15), and

    3.73557374335529<D<3.73557374335530.

Comparing these rational endpoints gives strict, deliberately wider bounds

    35.630<A<35.632,   11.539<B<11.541,
     4.054<C<4.055,     3.735<D<3.736.

For example A_0-10^(-15)>35.630 and
A_0+10^(-15)<35.632; the other coordinates are checked in the
same way from the displayed exact centers. Subtraction yields

    24.089<A-B<24.093,     .318<C-D<.320,
    31.894<A-D<31.897,   -7.487<C-B<-7.484.

All intervals have rational endpoints. For the pairing (A,B),(C,D),
the differences lie strictly between consecutive integers 24,25 and
0,1, respectively. For the only other pairing (A,D),(C,B), A-D lies
between 31,32 and C-B is negative. Thus neither pairing has both
differences in {0,1,2,...}. This exhausts the two reindexings; no
numerator equals a denominator, and all four parameters are positive.

**Exponential normalization.** Since c>0 and all parameters are positive,
alpha_j>0 for every j, including alpha_0=1. The entire symbol is exactly

    Phi(z)=sum_(j>=0) alpha_j z^j/j!
          = 2F2(A,C;B,D;c z).

Indeed the coefficient ratio in this exponential series is

    [alpha_(j+1)/(j+1)!]/[alpha_j/j!]
       = c (A+j)(C+j)/[(j+1)(B+j)(D+j)] -> 0.

The ratio test proves convergence at every complex z; the factorial
is essential. L791's model is precisely the binomial symbol with the
reflection y -> -y. Its actual matching convention was
F_j=S^j alpha_j, S=B R_1>0, for j<=4. Thus removing or restoring
that scale only rescales the variable by a positive number; no raw
moment or ordinary-coefficient sequence is substituted for alpha_j.

**Contradiction from the weaker all-degree real-root premise.** Suppose
every p_d has only real roots, allowing multiplicities. Put
q_d(x)=p_d(-x)=sum binom(d,j)alpha_j x^j. This polynomial has degree
exactly d, constant term1, and every coefficient positive. It is strictly
positive for x>=0, so its real roots, under the supposition, are all
strictly negative. The degree-zero symbol is1. Therefore the all-degree
binomial-symbol hypothesis (iv) of infinite Pólya–Schur is satisfied.

Its conclusion (iii) gives a type-I product for either Phi(z) or
Phi(-z). The reflected option is impossible: Phi(0)=1 forces the
product's zero-at-origin exponent to be0 and its constant to be1;
its derivative at0 is then a+sum gamma_n>=0, whereas
(Phi(-z))'|_(z=0)=-alpha_1<0. Here a,gamma_n>=0 and
sum gamma_n<infinity are exactly the imported product conditions.
Consequently Phi itself belongs to LP+.

Positive rescaling preserves LP+: in its defining compact-limit
description, substitute z/c in each negative-real-rooted polynomial.
Hence Phi(z/c)=2F2(A,C;B,D;z) belongs to LP+. The hypotheses of
Sokal Theorem5 at p=q=2 hold because A,C,B,D>0. Its necessary
integer-pairing condition contradicts the whole-box exclusions above.
Thus the supposition that every p_d is real-rooted is false. Degree
exactly d and the fundamental theorem of algebra give a nonreal root
at some finite degree. Failure of this weaker premise also rejects the
stronger all-degree simple-positive-root premise. No simplicity
conclusion is inferred from Pólya–Schur or from a surviving pairing.

Only the fixed model is excluded. The actual sequence agrees with its
scaled coefficients through index4, not all indices. Nothing in this
argument identifies a nonreal root of an actual Jensen polynomial or
an off-line zeta zero. No numerical root scan or mathematical script
was needed for the exact interval comparisons.

## Mathlib

Full matching coverage of Pólya–Schur, the cited hypergeometric
classification and this specialization is unchecked. No absence claim
or formal verification is made. The analytic/data/software premises
from L791 retain their original qualifications.
