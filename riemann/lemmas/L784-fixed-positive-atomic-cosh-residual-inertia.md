# Lemma 784: one fixed positive atomic cosh mixture passes the residual-index test

## Hypotheses

This is a model calculation, not a statement about actual Xi. Define

    mu=(delta_1+delta_3)/2+2 delta_2,
    G_*(w)=integral cosh(t sqrt(w)) dmu(t), r=3, R=8, k=2,
    t_0=pi^2/128, alpha_1=-t_0, alpha_2=-9t_0, sigma=9/8,
    g(z)=G_*(8z), P(z)=(z-alpha_1)(z-alpha_2), F=g/P,
    p=z^-2 P, b=p/F=P^2/(z^2 g), c=F/p=z^2 g/P^2.

The square-root notation denotes the even entire cosh series; removable
values are understood. Let beta_m be the Laurent coefficients of b on
its annulus containing the unit circle. All sequences start at coordinate1,
the inner product is conjugate-linear in its first argument, and Q_3
deletes coordinates1,2,3. Define

    d_i=alpha_i^2 F(alpha_i)/P'(alpha_i), C=diag(d_1,d_2),
    V_(l,i)=alpha_i^(l-1), H(b)_(l,h)=beta_(l+h-1),
    U=Q_3 H(b)V, Y=Q_3 V, S=Y*U, A=U C Y*,
    h_3(z)=sum_(n>=0) beta_(4+n) z^(n+1),
    K_ij=(h_3(alpha_i)-h_3(alpha_j))/(alpha_i-alpha_j) for i!=j,
    K_ii=h_3'(alpha_i), E_ii=sqrt(|d_i| |alpha_i|^3),
    J=diag(sign(d_i)), Q=-E K E.

The finite matrix Q is distinct from the infinite projection Q_3.
All convergence, grouping and nonzero denominators are proved below.
Write inertia as (n_+,n_0,n_-), including multiplicities.

## Conclusion

The prescribed positive measure has every exponential moment, and G_*
is entire with strictly positive Taylor coefficients,
G_*(0)=3, G_*(8)>0 and |G_*(w)|<=3 exp(3 sqrt(|w|)). In particular its
entire-function order is at most1/2. There are exactly two distinct,
simple nonzero negative roots of g in |z|<1, namely alpha_1,alpha_2,
no root on |z|=1, and F is entire and zero-free on a neighborhood of
|z|<=9/8. Quantitative contour bounds are

    min_(|z|=9/8) |F(z)|>1/125, max_(|z|=9/8) |b(z)|<337.

The complete residues are

    d_1=(2+sqrt(2)/2)/(2pi)>0,
    d_2=-27(2-sqrt(2)/2)/(2pi)<0.

The projected pairing and normalization satisfy

    S=diag(alpha_i^3) K,
    E^-1 (I-CS) E=I-JQ, J=diag(1,-1),
    det(I-A)=det(I-CS)=det(I-JQ)>0.

For the entire Laurent tail, not a finite approximation to it,

    inertia(J-Q)=(1,0,1)=inertia(J).

Thus both n_0(J-Q)=0 and n_-(J-Q)=n_-(J) hold for this one model.
This does not establish their implication from positive cosh mixtures
in general, actual-Xi signs, other radii/groupings, any other mixed minor
or RH. It does not contradict L783, which has different model premises.
The independent conceptual and arithmetic audit in step455 passes for
this fixed known-method specialization, with the same limited scope.

## Proof

**Imported methods and scope.** Reuse the invocation-start SPECIALIZE
assessment `drafts/literature/2026-11-05-fixed-atomic-cosh-residual-index-test.md`.
The elementary primary inputs are NIST DLMF v1.2.8 (2026-09-15),
[4.28.2](https://dlmf.nist.gov/4.28.E2) (complex exponential definition),
[4.33.2](https://dlmf.nist.gov/4.33.E2) (even cosh series),
[4.35.7](https://dlmf.nist.gov/4.35.E7),
[4.35.27](https://dlmf.nist.gov/4.35.E27) and
[4.35.30](https://dlmf.nist.gov/4.35.E30) (sum/double/triple arguments),
and [4.2.3/5/6](https://dlmf.nist.gov/4.2.i) (all logarithm branches).
DLMF [1.10(i), equation1.10.1 and Zeros](https://dlmf.nist.gov/1.10.i)
supplies the disk Taylor expansion and local multiplicity interface;
its removable-singularity case in 1.10(iii) applies after cancellation.
DLMF [1.10(iii), equations1.10.6–7](https://dlmf.nist.gov/1.10.iii)
give Laurent coefficients and absolute locally uniform convergence on
an annulus. The two-point divided-difference and repeated-argument
interface is Carl de Boor, *Divided Differences*, Surveys in Approximation
Theory1 (2005),46–69, Example2/(10), p.49, Proposition25/(26) and proof,
pp.53–54 ([author PDF](https://pages.cs.wisc.edu/~deboor/sat/papers/2/2.pdf)).
The finite-rank determinant interface is M. Duits, *Determinantal point
processes*, AppendixA, Lemmas66/69, pp.51–52
([author PDF](https://people.kth.se/~duits/static/media/DPP2.44e051d148b79af222fa.pdf)).
Use Sylvester's law of inertia; compare the invertible-congruence step
of G. Berkolaiko and P. Kuchment, *Spectral shift via “lateral” perturbation*,
J. Spectr. Theory12 (2022),83–104, Theorem2.7/proof pp.88–91,
[DOI10.4171/JST/395](https://ems.press/content/serial-article-files/33861).
No residual-index bound is imported from that theorem.

These inputs provide known methods, not the specified roots or matrix.
The specializations below evaluate the exact prescribed diagnostic.
L777/L782 supply conventions and a comparison method; their actual-Xi
statements are not applied to this different function. No computed entry
of L783 is used. No general source theorem is reproved. No genus-zero
product is asserted or needed, and no quadrature is used.

**Entire function and exhaustive complex roots.** The measure has finite
support and positive masses with total mass3, so all exponential moments
are finite. Termwise summation of the three globally convergent even
series gives

    G_*(w)=sum_(n>=0) [(1+3^(2n))/2+2*2^(2n)] w^n/(2n)!,
    G_*(w)=cosh(2y)(cosh(y)+2), y^2=w.                  (1)

The latter follows from the sum-of-coshes identity, or the double/triple
identities. It is independent of the sign of y. All coefficients are
strictly positive. Also |cosh(ty)|<=exp(t|y|), so the stated growth bound
and order-at-most1/2 follow, with no conclusion that roots are all real.

The first factor in (1) vanishes exactly at
y=i*pi*(2n+1)/4, n in Z, by its exponential definition. Identifying y
and -y gives the distinct w roots

    w=-pi^2(2n+1)^2/16, n>=0.                          (2)

For the other factor, e^y solves u^2+4u+1=0. With
a=log(2+sqrt(3))>0 its exhaustive logarithm preimages are

    y=+/-a+(2n+1)i*pi, n in Z.                         (3)

Their w squares are nonreal; their moduli are
a^2+(2n+1)^2*pi^2>pi^2>9. Thus no principal-branch or real-axis-only
root search is being substituted for exhaustion.

Every root is simple in w. At (2), sinh(2y)!=0 and
cosh(y)+2 is nonzero since cosh(y) is +/-sqrt(2)/2. At (3), sinh(y)!=0
and cosh(2y)=2 cosh(y)^2-1=7. Finally y!=0 in both families, so the
local map y -> w=y^2 has nonzero derivative and preserves simplicity.
No factors share a root, and w=0 is not a root.

The rational pi bounds certified below imply 0<t_0<2/25,
9t_0<18/25<1, and 25*pi^2/16>9. Consequently exactly the first two
roots of (2) lie in |w|<8, and all remaining roots of either family
lie strictly outside |w|<=9. Dividing g(z) by its two simple factors
therefore makes F entire and zero-free on a neighborhood of the closed
sigma disk. A neighborhood exists by isolation of zeros and compactness;
strict nonvanishing at the removed roots follows from simplicity.
This also proves contour nonvanishing, the exact grouping and G_*(8)>0.

**Quantitative contour bound.** On |z|=9/8 choose either y with y^2=8z
and write y=x+iv, so x^2+v^2=9. The identity

    |cosh(x+iv)|^2=sinh(x)^2+cos(v)^2

follows directly from the exponential definition. If |x|>=1/10 then
|cosh(2y)|>=|sinh(2x)|>=1/5. Otherwise |v|>299/100 and |v|<=3,
so 0<2pi-2|v|<1/3, using 157/50<pi<22/7. Thus
|cosh(2y)|>=cos(2v)>1-(1/3)^2/2=17/18>1/5.

For the other factor, if |x|<=1 then
Re(cosh(y)+2)>=2-cosh(1)>1/3. Here the even series gives

    cosh(1) <= sum_(j=0)^3 1/(2j)! + (1/8!)/(1-1/90) <5/3,

since ratios of successive terms from 1/8! onward are at most1/90.
If |x|>1, then |v|<sqrt(8)<3. For |v|<=pi/2 the same real part
is at least2. For pi/2<|v|<3, its imaginary part has modulus
|sinh(x) sin(v)|>sin(3)>1/10. Indeed u=pi-3 is between.14 and1/7,
and sin(3)=sin(u)>=u-u^3/6>1/10. Hence uniformly on this circle

    |g(z)|>=1/50,
    |P(z)|< (9/8+2/25)(9/8+18/25)<5/2,
    |F(z)|>1/125,
    |b(z)|<125(1+(18/25)/(9/8))^2<337.                (4)

The ratio |g/P| is legitimate on the circle, where P is nonzero.
All comparison inequalities in (4), the cosh-series bound and the
angle bounds are included as exact rational checks in the certificate.

**Normalization, residues and convergence.** The factors p,F are real,
F(1)>0, p tends to1 at infinity and has the logarithm
-sum_i sum_(n>=1) alpha_i^n/(n z^n) outside the roots. F has a
holomorphic logarithm on its zero-free disk with real value log F(1).
Their sum is the normalized logarithm of z^-2 g(z) on the common
annulus, so b=p/F, c=F/p have the stipulated normalization, including
the scalar in F. In particular bc=1 wherever defined.

At a root, F(alpha_i)=g'(alpha_i)/P'(alpha_i), whence
d_i=alpha_i^2 g'(alpha_i)/P'(alpha_i)^2. With
theta_1=pi/4, theta_2=3pi/4, direct differentiation of (1) gives

    g'(alpha_i)=8 sin(2theta_i)(cos(theta_i)+2)/theta_i,
    P'(alpha_1)=8t_0, P'(alpha_2)=-8t_0.

Substitution gives exactly the two residues in the conclusion.
They include the R=8 derivative factor; d_2 includes the alpha_2^2
factor81. The simple principal parts of c are
sum_i d_i/(z-alpha_i); subtracting these leaves a holomorphic function
on |z|<sigma. Thus for |z|>max|alpha_i| its complete negative
Laurent coefficients are c_(-n)=sum_i d_i alpha_i^(n-1), n>=1.
Consequently H(tilde c)=VCV^T. The columns of V are in l2.

By the Laurent Cauchy estimate and (4), |beta_n|<=337 sigma^-n
for n>=1. This estimate uses a Laurent contour, not analyticity of b
across its pole at0. It gives sum n|beta_n|^2<infinity, so H(b) is
Hilbert–Schmidt. The operator A is bounded and finite rank. For any
0<s<sigma the complete double series

    sum_(u,v>=0) beta_(4+u+v) x^u y^v

converges absolutely and uniformly on |x|,|y|<=s, with absolute sum
at most337 sigma^-4/(1-s/sigma)^2. Regrouping by u+v gives the
divided difference of h_3 off the diagonal and h_3' on it, with all
derivatives locally uniformly convergent. Therefore

    S_ij=sum_(l>=4,h>=1) alpha_i^(l-1) beta_(l+h-1) alpha_j^(h-1)
        =alpha_i^3 K_ij.                              (5)

The substitutions are l=4+u and h=1+v. The first term is
alpha_i^3 beta_4. Absolute convergence justifies this reindexing and
the diagonal limit. Because d_i alpha_i^3=-J_ii E_ii^2, equation(5)
gives CS=-J E^2 K and E^-1 CS E=-J E K E=JQ. The cited finite-rank
determinant identity applies to A=UCY*, including dependent columns,
and gives det(I-A)=det(I-CS). This uses a similarity, without assuming
that CS or A is selfadjoint.

**Exact evaluation of the complete tail.** Let

    B(z)=P(z)^2/g(z)=P(z)/F(z),
    T(z)=sum_(m=-2)^3 beta_m z^m.

B is holomorphic on |z|<sigma. Its Taylor coefficients can be computed
near0 by multiplying P^2 by the local inverse series of g. Only six
jets are needed, not evaluation of that local inverse beyond its first
pole. The first six g coefficients are exactly

    g_0,...,g_5=3,52,584/3,15776/45,121376/315,4041344/14175.

Write u_n for the coefficient of z^n in 1/g locally at0. The exact recurrence and values are

    u_0=1/3, u_n=-(1/3) sum_(j=1)^n g_j u_(n-j),
    u_0,...,u_5=1/3,-52/9,2120/27,-415136/405,
                22631008/1701,-2446097536/14175.

With P=z^2+10t_0 z+9t_0^2 and p_j=[z^j]P^2, this specifies
the exact six beta values by

    beta_m=sum_(j=0)^min(4,m+2) p_j u_(m+2-j), -2<=m<=3.   (6)

Uniqueness of the Taylor series of B identifies these with the actual
Laurent coefficients of b=z^-2 B. Its entire positive tail obeys

    h_3(z)=z^-3(b(z)-T(z)), 0<|z|<sigma,                (7)

with the removable value at0. This is an identity of analytic functions,
not a six-coefficient approximation or an analytic continuation of the
uncancelled inverse series. No tail is set to zero. At a removed root

    b(alpha_i)=0, b'(alpha_i)=P'(alpha_i)/(alpha_i^2 F(alpha_i))=1/d_i,
    h_3(alpha_i)=-T(alpha_i)/alpha_i^3,
    K_ii=1/(d_i alpha_i^3)+3T(alpha_i)/alpha_i^4-T'(alpha_i)/alpha_i^3.

The exact positive-diagonal congruence

    M=E^-1 (J-Q) E^-1=diag(J_ii/E_ii^2)+K

has J_ii/E_ii^2=-1/(d_i alpha_i^3). Hence its entries reduce to

    M_ii=3T(alpha_i)/alpha_i^4-T'(alpha_i)/alpha_i^3,
    M_12=(-T(alpha_1)/alpha_1^3+T(alpha_2)/alpha_2^3)/(alpha_1-alpha_2). (8)

The residue term cancels in M, and is retained in K. All denominators
are strictly nonzero. Equations(6)–(8) are exact expressions for the
full nonrational Laurent-series matrix, sufficient to replace a
truncation estimate. The quantitative bound(4) independently supplies
the convergence and operator justification.

**Rigorous arithmetic and full inertia.** Reproduce with

    python3 scripts/fixed-atomic-cosh/exact-inertia-453.py

The full certificate is `scripts/fixed-atomic-cosh/exact-inertia-453.json`.
Arithmetic uses Fraction throughout, with outward rounding after each
interval operation to denominator2^192. For a rational x its lower
endpoint is floor(2^192 x)/2^192 and upper endpoint is its ceiling
analogue, so rounding preserves inclusion even for negative numbers.
Products take extrema of all four endpoint products; division is used
only when the divisor interval excludes0. All exponent operations are
integer powers. The square-root enclosure uses exact integer squares
bounding sqrt(2) at denominator10^50; no floating-point root is used.

For pi, Machin's identity pi=16 atan(1/5)-4 atan(1/239) is enclosed
by adjacent alternating Taylor sums, with32 and8 terms respectively.
The remainder is bounded by the next term. For completeness its branch
is checked algebraically: tan(4 atan(1/5))=120/119, so
tan(4 atan(1/5)-atan(1/239))=1. The angle is positive and below.8,
in (0,pi/2), from the same elementary arctangent bounds; therefore it
is pi/4. The coarse comparison .8<pi/2 does not use the Machin
enclosure: atan(1)=integral_0^1 (1+x^2)^-1 dx>1/2 gives pi/2>1.
This tiny elementary check certifies the numerical enclosure,
rather than assuming displayed decimal digits of pi. The resulting
interval is contained in (157/50,22/7).

The certificate retains all six coefficients, residues, weights, complete
h_3 node values, K, M, determinants and LDL pivots. Full selected
load-bearing intervals and all22 check results were inspected; none
fails. The initial serialization attempt exceeded Python's integer-string
limit; outward dyadic rounding replaced unbounded fraction growth before
the successful run, without weakening any required strict comparison.
It is not a mathematical counterexample or a failed sign test.
The certified deliberately rounded bounds from(8) are

    5063 < M_11 < 5064,
    .062 < M_12 < .063,
    -.454 < M_22 < -.453,
    -2294 < det(M) < -2293.                            (9)

In particular the first LDL pivot M_11 is positive and the second
det(M)/M_11 is strictly negative. Completing the square, or Sylvester's
law of inertia under the invertible triangular LDL congruence, gives
inertia(M)=(1,0,1). The positive invertible E gives the same inertia
for J-Q. This determines both negative index and nullity, rather than
using determinant parity alone. Separately,

    det(I-CS)=det(J)det(J-Q)=-E_11^2 E_22^2 det(M)>0,

consistent with the signed similarity and determinant orientation.
No Toeplitz/Fredholm prefactor is invoked to infer an actual-Xi sign.

**Independent audit, step455 (2026-11-05).** The prior SPECIALIZE
assessment `drafts/literature/2026-11-05-fixed-atomic-cosh-inertia-audit.md`
covers this audit. Both complete root families and their local
multiplicities were checked, including all logarithm branches and the
nonzero derivative of the square map. Both contour-lower-bound cases
in (4), the scale8 residues, the Laurent annulus and coefficient contour,
and convergence before the diagonal limit in (5) pass. In (6) the local
inverse series is used only for derivatives at0. The larger analytic
disk is obtained from B=P/F after removable zeros, not from 1/g.
Consequently (7) evaluates the complete tail. The identity b'(alpha)=1/d
and the algebraic cancellation in (8) pass independently of arithmetic.
The original `diagonal_cancellation_consistent` interval-overlap check
is only a consistency check; overlap alone would not prove an identity.

The original implementation was read in full and replayed: 22/22 checks
pass. Floor/ceiling dyadic rounding encloses exact operations for either
sign; reciprocal intervals are formed only away from0. Negative powers
are reciprocals of positive integer powers, with all required intervals
excluding0. Original complete pi, root, coefficient, residue, weight,
h_3, K, M, determinant and pivot evidence was inspected. No model
hypothesis, cancellation, denominator or strict-sign defect was found.

A separate implementation does not import the original interval class:

    python3 scripts/fixed-atomic-cosh/audit-replay-455.py

Its full certificate is `scripts/fixed-atomic-cosh/audit-replay-455.json`.
It recomputes pi with36 and10 alternating-series terms and sqrt(2) by
integer squares at denominator10^60. All intermediate interval endpoints
are exact fractions with no rounding; only serialization rounds outward
to denominator2^224. For an interval avoiding0, negative powers use the
monotone reciprocal map followed by the usual real integer power; even
positive powers additionally test0 when it belongs to the interval.

The alternate algebra expands P^2 first. Let a_j, j=0..4, be
(81,180,118,20,1), so p_j=a_j t_0^(4-j). For -2<=m<=3 and
0<=j<=min(4,m+2), put c_(m,j)=a_j u_(m+2-j). Equation(8), with
alpha=-q t_0, then gives the finite exact expressions

    M_ii=sum_(m,j) (3-m)c_(m,j)(-q_i)^(m-4)t_0^(m-j), q_1=1,q_2=9,
    M_12=sum_(m,j) c_(m,j)[(-9)^(m-3)-(-1)^(m-3)]t_0^(m-j)/8.

These follow by differentiating each finite term of T, and by
alpha_1-alpha_2=8t_0, respectively. Thus this arithmetic replay is
algebraically equivalent to (8), with no further analytic assumption.
Collecting the exact rational coefficients reduces the entries to

    M_11=2120/27-(830272/45)t_0+(22631008/21)t_0^2,
    M_12=2120/27-(830272/81)t_0+(22631008/189)t_0^2,
    M_22=2120/27-(830272/405)t_0+(22631008/1701)t_0^2.

The independent implementation proves all inequalities(9) and strict
LDL signs directly; its29 checks pass. Its separate enclosures for every
beta from-2 through3, both h_3 node values, residues, weights, K, M,
determinants and pivots lie inside the original enclosures. Containment
is a consistency test, not the basis of the sign conclusion: the strict
bounds are also checked on the independent intervals. The complete
selected M, determinant, weights and pivot fields were inspected, not
only a certificate preview. The second pivot is in particular negative,
so the verified congruences establish both the negative index and zero
nullity. No formal verification or generic extension is asserted.

The single fixed diagnostic and its independent audit are now closed.
Its matching index does not supply a theorem for positive mixtures. An
additional independently controlled signed inequality is still missing,
and the actual-Xi/global gaps remain unchanged.

## Mathlib

Full matching coverage has not been checked; neither presence nor absence
is claimed. The informal inputs are the precisely cited elementary
hyperbolic/Laurent identities, divided-difference and finite-rank
interfaces, Sylvester's law, the elementary alternating-series remainder
and exact rational interval arithmetic. No formal verification or new
general theorem beyond the inspected sources is asserted.
