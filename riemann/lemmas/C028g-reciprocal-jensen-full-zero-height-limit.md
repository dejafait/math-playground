# Corollary C028g: reciprocal Jensen full-zero height limit

## Hypotheses

Use precisely C028b's actual family, with its positive coefficients:

    gamma_j=j! M_(2j)/(2j)!>0,  b_j=gamma_j/gamma_0,  b_0=1,
    F(u)=sum_(j>=0) b_j u^j/j!=Theta(u)/gamma_0,
    J_d(x)=sum_(j=0)^d binom(d,j) gamma_j x^j,
    R_d(x)=sum_(j=0)^d binom(d,j) gamma_j x^(d-j),
    U_d(u)=J_d(u/d)/gamma_0,
    H_d=sum_(R_d(z)=0) |Im z|.

Here Theta(u)=xi(1/2+sqrt(u)) denotes the even entire series, not a
choice of a square-root branch. Thus F is entire of order 1/2 and
F(0)=1. Integers d tend to infinity through d>=3. Count all polynomial
roots with algebraic multiplicity and all entire-function zeros with
analytic multiplicity. Retain C028f's uniform strict-tail bound with
one finite constant C=4K*3^(3/4)/log 2, where K>=1 depends only on F.
No RH, simple-zero hypothesis, Laguerre--Polya membership, effective K,
or vanishing compact nonreal-zero mass is assumed.

## Conclusion

The multiplicity-counted full zero sum is absolutely convergent, and

    lim_(d->infinity) H_d/d
      = S_F := sum_(F(w)=0) |Im(1/w)| < infinity.          (1)

In particular the normalized heights have a finite limit. This is a
specialization of the reviewed classical inputs, not a new general
zero-convergence theorem. No value zero for S_F, quantitative rate in d,
actual nonreal zero, or resolution of RH is established. This proof
passed the separate conceptual audit1522 below under the stated
C028b/C028f input contracts.

## Proof

### Imported inputs and their exact scope

Cormac O'Sullivan, *Zeros of Jensen polynomials and asymptotics for the
Riemann xi function*, arXiv:2007.13582v2, 9 December 2020,
[Introduction (1.2), Section 3.1, Theorem 3.1 proof sketch and
Corollary 3.2](https://arxiv.org/html/2007.13582v2#S3.SS1), supplies the
ordinary scaled Jensen limit for an entire function and the actual
Theta convention and order. C028b checks this normalization and gives

    U_d -> F uniformly on every compact subset of C,
    H_d/d = sum_(U_d(u)=0) h(u),  h(u)=|Im(1/u)|.          (2)

The second identity includes every root and preserves multiplicity
under z=d/u. Positivity of gamma_0 and gamma_d makes both polynomial
degrees exactly d and excludes zero roots. We use only the compact
limit and actual order from the cited source, not its conditional
hyperbolicity conclusion. These statements are not reproved here.

Terence Tao, *Math 246A, Notes 4: singularities of holomorphic functions*,
11 October 2016,
[Theorem 37 (Rouche's theorem)](https://terrytao.wordpress.com/2016/10/11/math-246a-notes-4-singularities-of-holomorphic-functions/),
preserves the interior zero count with multiplicity for f and f+g
holomorphic near a simple closed contour and its interior when
|g|<|f| on the contour. All uses below are for fixed circles and
entire functions, with the strict comparison verified explicitly.

Terence Tao, *246B, Notes 1: Zeroes, poles, and factorisation of
meromorphic functions*, 23 December 2020,
[Theorem 22, proof equation (20) and its dyadic summability argument;
Proposition 8](https://terrytao.wordpress.com/2020/12/23/246b-notes-1-zeroes-poles-and-factorisation-of-meromorphic-functions/),
gives the following summability input: for a nonzero entire function
of order at most rho>=0, its nonzero zeros w, repeated with multiplicity,
satisfy sum |w|^(-floor(rho)-1)<infinity. The proof treats finite zero
sets separately and proves the infinite case with an exponent strictly
between rho and floor(rho)+1. Origin zeros are removed first. We import
only this summability conclusion, not the rest of the factorization.
Taking rho=1/2 is legitimate for the actual F; F(0)=1 makes it nonzero
and leaves no origin factor to remove. Hence

    sum_(F(w)=0) 1/|w| < infinity.                       (3)

This import needs neither finite type at order 1/2 nor real zeros.
Since 0<=h(w)<=1/|w|, (3) proves the asserted absolute convergence of
S_F, for a finite or infinite zero set. In either case its strict tail

    T_F(R)=sum_(F(w)=0, |w|>R) h(w)

tends to zero as R tends to infinity: a convergent nonnegative series
has arbitrarily small mass outside a finite set, and one disk contains
that set. This argument also covers an empty zero set, with sum zero.

The separate polynomial input is the already audited C028f:

    T_d(R):=sum_(U_d(u)=0, |u|>R) h(u)
        <= C R^(-1/4)      (d>=3, R>=1).                 (4)

It controls the complete strict tail, with C independent of d and R.
Its positive-coefficient and actual-order hypotheses are precisely
those above. A fixed-polynomial bound with a degree-dependent constant
would not suffice. No summability or counting theorem is reproved here.

### A common zero-free neighborhood of the origin

By continuity and F(0)=1 choose 0<r_*<1/2 such that
|F(u)-1|<=1/4 for |u|<=2r_*. Compact convergence in (2) gives d_0>=3
such that, for every d>=d_0, |U_d(u)-F(u)|<1/4 throughout that disk.
Thus |F(u)|>=3/4 and |U_d(u)|>1/2 there. All these functions have no
zeros in this same closed disk. This excludes roots approaching the
singularity of h as d tends to infinity; individual identities U_d(0)=1
alone would not establish that fact. The finitely many earlier degrees
do not affect the limit and have no zero at zero by (2)'s contract.

### Complete compact weighted sums with multiplicities

Fix R>=1 such that F has no zero on |u|=R. As F is nonzero entire,
its zeros are isolated and there are only finitely many in the closed
disk. List the distinct ones as w_1,...,w_s, with multiplicities m_i,
and put N=sum_i m_i. Define

    A_d(R)=sum_(U_d(u)=0, |u|<=R) h(u),
    A_F(R)=sum_(F(w)=0, |w|<=R) h(w).

We prove A_d(R)->A_F(R), including the case N=0.

Suppose first N>0. For an arbitrary epsilon>0, choose pairwise disjoint
closed disks D_i centered at w_i, contained in |u|<R and outside
|u|<=r_*, containing no other zero of F, and sufficiently small that

    |h(u)-h(w_i)| < epsilon/(N+1)   for every u in D_i.   (5)

Such disks exist by isolation, finiteness of the distinct centers and
continuity of h away from zero. Their boundaries contain no zero of F.
The compact set

    E={u:|u|<=R} minus the union of the interiors of D_i

contains no zero of F, including on all the small boundaries and the
outer circle. Consequently eta=min_E |F|>0. Compact convergence yields
d_1>=d_0 such that for every d>=d_1,

    sup_(|u|<=R) |U_d(u)-F(u)| < eta/2.

On E this makes |U_d|>=|F|-|U_d-F|>eta/2, so there are no extra roots
on the complement or its boundaries. On each boundary D_i it also
gives |U_d-F|<|F|. Rouche's theorem applies to the entire functions
F and U_d and gives exactly m_i roots of U_d in the interior of D_i,
counting multiplicity. These are all its roots in |u|<=R. Therefore

    |A_d(R)-A_F(R)|
      <=sum_i sum_(U_d(u)=0, u in D_i) |h(u)-h(w_i)|
      < N epsilon/(N+1) < epsilon.                     (6)

No labeling or simplicity of the individual roots is needed. In
particular (5) remains valid when w_i is real and h(w_i)=0, even if
nearby polynomial roots are nonreal. The disks and d_1 may depend on
epsilon and the fixed R; they do not move during the degree limit.

If N=0, F is nonvanishing on the whole closed radius-R disk. Its
positive minimum and compact convergence make U_d nonvanishing there
for all sufficiently large d. Then A_d(R)=A_F(R)=0 exactly. This
completes compact weighted convergence in every case. It also verifies
that no roots on the chosen outer circle escape the compact accounting.

### The two tails and the order of limits

Let epsilon>0. Choose R>=1 sufficiently large that

    C R^(-1/4)<epsilon/3,    T_F(R)<epsilon/3,

and so that |u|=R is F-zero-free. Such a choice is possible: both
inequalities persist upon increasing R, and only finitely many zero
moduli occur in each bounded interval. Thus every sufficiently far
interval of positive length contains a permitted radius.

Keep this R fixed. By compact convergence just proved, there is an
integer d_2>=3 such that for every integer d>=d_2,
|A_d(R)-A_F(R)|<epsilon/3. The complete sums split exactly into the
closed-disk terms and strict tails, with every multiplicity retained.
By (2), absolute convergence of S_F, and (4),

    |H_d/d-S_F|
      <= |A_d(R)-A_F(R)| + T_d(R) + T_F(R)
      < epsilon/3 + epsilon/3 + epsilon/3 = epsilon.

This proves (1). The radius is selected before the degree onset;
neither a moving-cutoff limit nor an interchange of an unbounded
singular weight with infinite zero measures has been assumed.

### Relevance and remaining gap

C028b already proves that H_d=o(d) is equivalent to RH for this actual
family. Equation (1) identifies its remaining limiting functional,
but supplies no inequality forcing S_F=0. In particular the earlier
conditional one-zero lower bound is consistent with (1): a nonreal
zero of multiplicity m contributes m|Im(1/w)|>0 to S_F. No such zero
is exhibited. The fixed coefficient-budget and inverse-direction
obstructions are contrasts, not inputs to this proof. C028f pays the
escaping roots only; compact actual nonreal-zero mass remains unpaid.

### Separate conceptual audit1522 (2026-11-18)

The complete limit passes under the unchanged SPECIALIZE assessment1520.
The audit read the full C028b/C028f contracts and proofs and reused the
primary statements and essential proof cases recorded in source-notes1519
and recovery1521. No correction, stronger theorem, additional source
import or new mathematical dependency was required. In particular this
audit does not reprove the entire earlier Xi input chain. The following
checks account for the potentially singular weight and both limits.

**Normalization and eventual exclusion of the singularity.** In C028b,
U_d(u)=(u/d)^d R_d(d/u)/gamma_0 for u!=0. The change of variable has
nonzero derivative, and gamma_0,gamma_d>0 exclude zero roots and lost
degree. Thus dividing the complete R_d height by the positive real d
gives exactly the finite sum in (2), with every multiplicity. The actual
Theta convention supplies order 1/2 for this F, not for a differently
scaled or shifted input. For the selected closed disk of radius 2r_*,
F(0)=1 and continuity give |F|>=3/4. Uniform convergence on that disk
gives |U_d|>1/2 for every d beyond one onset. This is a common zero-free
disk, rather than an assertion inferred merely from U_d(0)=1. The finite
number of earlier degrees have defined weights and do not affect the
limit. Neither the disk nor this onset requires RH.

**Full compact counting.** With R fixed and F nonzero on its boundary,
isolation of zeros gives a finite multiset inside. Each chosen D_i lies
strictly inside the outer disk and outside |u|<=r_*;
the finitely many radii can be chosen positive with disjoint closures.
Continuity of h away from zero gives (5) for any prescribed epsilon.
It applies even at a multiple real zero, where h is continuous although
no differentiability of h is asserted. Removing the open small disks
leaves a compact set E with no F-zero anywhere, including both types
of boundary. Therefore eta=min_E|F| is strictly positive. The same
uniform bound eta/2 both excludes all U_d zeros in E and establishes
strict Rouche domination on every small circle. Entirety verifies the
holomorphy hypotheses on neighborhoods of those circles and interiors.
Rouche gives exactly m_i roots inside each circle, not merely at least
one or a selected conjugate pair. Hence there are exactly N compact
roots in total for large d, and their weighted error is less than
N epsilon/(N+1). No simple-root labels, continuous root branches, or
unproved absence of other compact roots are used. If N=0, the positive
minimum on the whole closed disk excludes all compact polynomial roots
eventually, as claimed. These arguments also exclude polynomial roots
on the chosen outer circle for all sufficiently large degrees.

**Entire summability and the distinct polynomial tail.** The cited
Tao246B Theorem22 summability step applies to a nonzero entire function
of order at most rho, after removing origin zeros. Here rho=1/2 and
F(0)=1 meet those hypotheses. Its required strict exponent gap can be
chosen as rho+1/4=3/4<floor(rho)+1=1; there is no assumption of finite
type at order 1/2. The source treats a finite zero list directly and
the infinite list with multiplicity by its dyadic estimate. Thus (3)
is justified in all cases, and domination by 1/|w| makes the entire
height tail tend to zero. For an empty zero list the sum is zero.
C028f is a separate, degree-uniform estimate for the complete strict
polynomial tail. Its constant is exactly 4K*3^(3/4)/log 2, with one K
depending only on this fixed F. A finite limit for the entire sum alone
would not justify this polynomial control.

**Cutoffs and quantifiers.** Given epsilon>0, absolute convergence of
the entire sum and the decreasing bound C R^(-1/4) first give a lower
radius beyond which both tails are <epsilon/3. Each bounded annulus
contains only finitely many F-zero moduli, so R can be increased to
avoid them while retaining both inequalities. Compact convergence is
then used with this single R to select one degree onset for all later
degrees. Dependence of the small disks and that onset on epsilon and R
is permitted; no effective or uniform rate in R is asserted. The compact
sums use |u|<=R and the tails use |u|>R, so their partition includes
every boundary multiplicity exactly once, even before invoking eventual
boundary exclusion. The three errors are respectively <epsilon/3,
<epsilon/3 and <epsilon/3. This proves the stated full limit without
interchanging an infinite sum with the degree limit or ignoring an
unbounded weight at the origin.

The only direct local mathematical inputs remain C028b and C028f; the
classical imports are cited above. The audit validates the existing
specialization, not progress beyond those checked methods. In particular
S_F<infinity does not imply S_F=0: every hypothetical nonreal zero still
has a strictly positive contribution with its multiplicity. No such
zero is constructed, no effective K or degree rate is supplied, and the
RH-equivalent compact-mass payment remains open.

## Mathlib

Not checked. Availability of a full matching theorem for this reciprocal
height limit, or formalized supporting Jensen, Rouche and entire-order
summability results, is unknown. No absence or formal verification is
claimed. The precise classical imports are given above; the common
origin exclusion, full compact multiset accounting and two-tail passage
are the local specialization proved here and checked in audit1522.
