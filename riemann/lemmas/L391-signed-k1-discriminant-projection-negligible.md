# Lemma 391: the complete signed k=1 projection is lower order

## Hypotheses

Use the fixed actual functions and ordinary height jets of L390:
f=F_0/A, L=log(2+t), x=f, y=f'/L, z=f''/L^2,

    M=(z^2+3xz/2+x^2/16-y^2)/2,
    K=((z-x/4)-iy)^2/2,
    E=R^2=pi^(-it) Gamma(1/4+it/2)/Gamma(1/4-it/2),
    Z=zeta(5/2+it).

H tends to infinity through real values. No RH, simplicity,
noncoincidence, phase independence or physical discriminant sign is
assumed. The source inputs below are unconditional and fixed-order;
twists and response heads are fixed before taking the height limit.

## Conclusion

Writing ell=log H, the complete sharp-interval projection satisfies

    (1/H) integral_[H,2H] 2 M |Z|^2 Re(K E Z^2) dt
        = o(ell^4).                                      (1)

For each fixed N, replacing Z by Z_N=sum_(n<=N)n^(-5/2-it)
gives the stronger bound O_N(ell^3). Constants in this fixed-head
bound need not be uniform in N. This settles only the k=1 harmonic
of L390. It supplies no k=0 or k=2 evaluation, positive total square
coefficient, improved sign proportion, eventual sign, common-zero
upper count, mixed positivity or RH consequence. The separate critical
audit below validates this specialization with unchanged conclusions.

## Proof

This is a REPRODUCTION under the prior SPECIALIZE assessment
`drafts/literature/2026-10-10-discriminant-unequal-orientation-projection.md`.
The signed mean-value theorem and subconvex bound are imported, not
reproved. The physical jet conversion, slow weights and sharp
connectors are the application obligations addressed here.

### Imported inputs and their exact scope

N. Laaksonen and Y. N. Petridis, *On the Value Distribution of Two
Dirichlet L-functions*, [arXiv:1505.00623v1, Lemma 1.2](https://arxiv.org/html/1505.00623v1),
and the [accepted manuscript dated 26 February 2017, p. 3](https://discovery.ucl.ac.uk/1544001/1/lvalues_accepted.pdf#page=3),
state a modified Gonek lemma. We use the fixed-right-line formulation
in A. Sourmelidis, J. Steuding and A. I. Suriajaya, *Dirichlet Series
with Periodic Coefficients and their Value-Distribution Near the
Critical Line*, [arXiv:2007.14008v2, Section 3 between (35) and (36)](https://arxiv.org/html/2007.14008v2#S3):
for fixed q in the positive integers, fixed delta>0, a=1+delta,
and F(s)=sum c(n)n^(-s) convergent on Re s>1 with
c(n)<<_eta n^eta for every eta>0,

    (1/(2 pi i)) integral_[a+i,a+iV]
        (q/(2 pi))^s Gamma(s) exp(-pi i s/2) F(s) ds
      = sum_(n<=Vq/(2 pi)) c(n) exp(-2 pi i n/q)
          +O_delta(V^(1/2+delta));                    (2)

the analogous +pi i s/2 integral is O_delta(1). Constants can depend
on the fixed series and q. Periodicity belongs to the subsequent
application, not this theorem's coefficient hypothesis. We use no
growing q, complex q, complex-shift differentiation or periodic
simplification. The originating Gonek (1984) Lemmas 2--5 are not
needed as additional inputs from their unreadable displays.

J. Bourgain, *Decoupling, exponential sums and the Riemann zeta
function*, [arXiv:1408.5794v2, Theorem 5 (0.5), p. 2](https://arxiv.org/pdf/1408.5794v2#page=2),
gives |zeta(1/2+it)|<<_epsilon t^(13/84+epsilon).
Choose epsilon=1/168; in particular this gives the weaker convenient
bound O(t^(1/6)). We also use the standard Phragmen--Lindelof
convexity principle in a fixed vertical strip, Cauchy's derivative
estimate, the zeta functional equation, and sector-qualified Stirling
and polygamma expansions already used in L381/L383. All derivative
orders below are at most two per critical factor, not growing orders.

### Exact ordinary jets and conjugation

Let tau be complex height, s=1/2+i tau, and write h_p(s)=zeta^(p)(s),
where these superscripts mean s derivatives. On the rectangle
H<=Re tau<=2H, -11/20<=Im tau<=0, the holomorphic extensions of
L381/L383 give f=-R h_0 and R'/R=i Omega, where

    Omega(tau)=[Psi(1/4+i tau/2)+Psi(1/4-i tau/2)-2 log pi]/4.

Ordinary tau differentiation, including the phase derivative, gives

    D_0=h_0,
    D_1=i(h_1+Omega h_0)/L,
    D_2=(-h_2-2 Omega h_1-Omega^2 h_0+i Omega' h_0)/L^2,
    (x,y,z)=-R(D_0,D_1,D_2).                         (3)

Here L=Log(2+tau); primes on Omega mean tau derivatives. These are
values of ordinary derivatives divided by L^j, not derivatives of
those divisors. In particular neither the i factors nor Omega'
has been omitted. All branches and factors are holomorphic on a
neighborhood of the rectangle: their possible poles have Re tau=0,
R is the nonzero square root of E, and Re(2+tau)>0.

M is real on the original line. Consequently the complex conjugate
of M K E Z_N^3 conjugate(Z_N) on that line is

    M conjugate(K) E^(-1) conjugate(Z_N)^3 Z_N.

Define the explicit homogeneous degree-four polynomial

    P(D)=[(D_2^2+3D_0D_2/2+D_0^2/16-D_1^2)/2]
           [(D_2-D_0/4+iD_1)^2/2].

Equation (3) gives M conjugate(K)=R^4 P(D)=E^2 P(D),
so the remaining carrier is E. At s=1/2+i tau it is exactly

    E=chi(1-s),
    chi(1-s)=(2 pi)^(-s) Gamma(s)
                  [exp(-pi i s/2)+exp(pi i s/2)].     (4)

This is the usual zeta functional-equation factor, using gamma
reflection and duplication. Thus the physical k=1 term is twice
the real part of the integral of (4) times P(D) and the fixed head.
No modulus-square replacement of the signed polynomial is made.

Expanding only the finite polynomial P(D) writes it as a finite sum
of terms

    w(tau) F_p(s),  F_p(s)=product_(j=1)^4 h_(p_j)(s),
    0<=p_j<=2, d=sum p_j<=8.                         (5)

Each scalar w is a constant multiple of Omega^b (Omega')^c/L^m
with m=d+b+2c, or a finite sum of such monomials. The individually
controlled polygamma bounds give, uniformly on this rectangle,

    Omega=O(ell), Omega'=O(1/H), Omega''=O(1/H^2),
    |w|=O(ell^(-d)), |d w/d tau|=O(ell^(-d)/H).      (6)

These follow by differentiating the displayed monomials, with
L'=1/(2+tau); no O term is differentiated. This also proves that
the total variation of w on a right horizontal edge is O(ell^(-d)).

### Fixed rational twists and signed right-line primitives

Each term in conjugate(Z_N)^3 Z_N is a fixed scalar times r^(it),
where r=u/v is a positive rational with positive integer u,v.
At complex height it is r^(s-1/2). Its constant r^(-1/2) can be
absorbed into the fixed scalar. On Re s>1, the complete series for
F_p has coefficients

    c_p(n)=(-1)^d sum_(n_1 n_2 n_3 n_4=n)
                         product_j (log n_j)^(p_j). (7)

For p_j=0 the logarithm factor means 1, also at n_j=1. In particular
|c_p(n)|<=d_4(n)(log n)^d for n>=2, with the evident n=1 case.
The product series is absolutely convergent and locally uniformly
convergent on Re s>1; d_4(n)<<_eta n^eta and logarithms preserve
this bound after reducing eta. These are the elementary fixed-divisor
bounds, not moment assumptions.

Encode the rational twist exactly as

    r^s F_p(s)=u^s sum_(n>=1) c_p(n)(v n)^(-s).

The series on the right has coefficient c_p(n) at index v n and
zero elsewhere. It meets (2)'s hypotheses, with fixed integer gamma
scale q=u. Its negative-exponential main sum is therefore

    sum_(v n<=Vu/(2 pi)) c_p(n) exp(-2 pi i v n/u).  (8)

We require only an absolute bound for this *signed theorem output*.
For X>=2 the elementary generalized-divisor summatory bound is

    sum_(n<=X) d_4(n) <= X(1+log X)^3.

Indeed sum the first three divisor variables with weight
1/(n_1 n_2 n_3), bound the count of the fourth by X/(n_1 n_2 n_3),
and enlarge the first three ranges to [1,X]. Hence (8) is
O_(r,p)(V(log V)^(d+3)); no asymptotic or cancellation in d_4
is assumed. The elementary summation is included to justify the
specific logarithmic threshold absent from the cited theorem.

Move to the fixed line a=21/20, so delta=1/20 in (2).
Subtract the theorem at V and H. Both branches of (4) together give
for every H<=V<=2H the primitive bound

    |integral_[H,V] chi(1-a-it) r^(a+it)
                         F_p(a+it) dt|
       <= C_(r,p)[H ell^(d+3)+H^(11/20)].            (9)

The factor converting ds/(2 pi i) into dt is the constant 1/(2 pi),
and is harmless for this bound. Constants are uniform in V here:
the fixed-parameter theorem holds for every sufficiently large V,
and H<=V<=2H. The nonstationary gamma branch is retained, not dropped.
Partial summation against w(t-i 11/20), using (6) and (9), gives
O_(r,p)(H ell^3) for each term on this right line. This uses the
complete primitive, with both sharp endpoints, and does not insert
the fast carrier into a theorem for slowly varying weights.

### Sharp connectors with a strict sublinear budget

The right-line step still requires both connectors; the old H^2
estimate in L390 does not suffice. On the fixed strip
1/2<=sigma<=11/10, interpolate Bourgain's above consequence with
the absolutely bounded line sigma=11/10. The standard strip
Phragmen--Lindelof principle gives

    |zeta(sigma+it)| <= C H^((5/18)(11/10-sigma)),
                      H<=t<=2H.                   (10)

The function has no pole at these heights. Equivalently apply the
principle to (s-1)zeta(s), of polynomial growth on this strip, and
divide by |s-1| comparable to H; this yields precisely the same
interpolated exponent. For the Cauchy disks just to the left of 1/2,
the functional equation and Stirling extend (10) with an O(1/ell)
change in its exponent. Heights on these disks remain comparable
to H. Disks of radius 1/ell about points with
1/2<=sigma<=21/20 remain below 11/10 for large H. Cauchy's estimate
therefore gives, for p<=2,

    |h_p(s)| <= C_p ell^p
             H^((5/18)(11/10-sigma))                (11)

on both connectors. The factor H^(O(1/ell)) has been absorbed into
the constant. Sector-qualified Stirling gives
|chi(1-s)|<=C H^(sigma-1/2). Combining (6) and (11), all ell^d
derivative factors cancel their coefficient normalizations. The
absolute integrand for each fixed twist is bounded by

    C_(r,p) H^(sigma-1/2+(10/9)(11/10-sigma)).

The exponent is linear and decreasing on [1/2,21/20], with maximum
2/3 at sigma=1/2. Each connector has fixed length 11/20 and hence
absolute integral O_(r,p)(H^(2/3)). In particular it is o(H ell^4).
The exact carrier (4), not either unbounded exponential alone, is
used for this connector estimate. All other coefficients and fixed
twists are bounded as already checked. There are no residues, poles
or branch cuts in the rectangle. Cauchy's theorem, (9), (6) and the
connectors now prove the fixed-head O_N(H ell^3) bound on the original
sharp interval. Conjugation and taking twice the real part recover
exactly its physical projection.

### Complete response tails

Let eta_N=sum_(n>N)n^(-5/2). On the real line Z and every Z_N are
uniformly bounded, and |Z-Z_N|<=eta_N. For U=x^2+y^2+z^2,
L390 gives |M|+|K|<=C U. Consequently, separately for this harmonic,

    |2M Re(K E [Z^3 conjugate(Z)-Z_N^3 conjugate(Z_N)])|
         <= C eta_N U^2.                            (12)

L390's fourth-jet budgets, imported there from Bui--Hall and also
used in L389, give (1/H) integral U^2=O(ell^4). Thus the normalized
full-minus-head projection is bounded by C eta_N ell^4 uniformly
in N and large H. Divide by ell^4, take the height limsup at each
fixed N using its O_N(ell^3) bound, and then let N tend to infinity.
The absolute limsup is zero, proving (1). No growing-head theorem,
uniform subconvex constant in N or discarded derivative tail is
required. The response derivative tails were already absorbed in
L390's lower-order physical reduction.

### Separate critical audit — 2026-10-11

This REPRODUCTION audit uses the prior SPECIALIZE assessment
`drafts/literature/2026-10-10-signed-k1-projection-audit.md`.
The primary modified-Gonek statements, Bourgain v2 Theorem 5 and
Bui--Hall v1 Theorem 3 were already inspected in its reused source
assessments. They are imported in their stated fixed-parameter scopes.
The present check also validates the physical reduction and full-tail
budgets in L390's separate audit. No new source theorem is claimed.

**Carrier, ordinary jets and all polynomial terms.** The positive p
in Q has no phase, so R^2 is exactly the displayed E. The continuous
root agreeing with Q/A on the real interval exists throughout the
rectangle: gamma has no zeros, its poles here would have real height
zero, and the rectangle is simply connected. L390 (6), with its fixed
real completion convention, gives f=-R h_0, also at zeta zeros. Its extension
then gives f'=-R i(h_1+Omega h_0) and
f''=-R[-h_2-2Omega h_1-Omega^2h_0+iOmega'h_0].
These verify every term in (3), including both factors i and Omega'.
Only after taking these ordinary derivatives is division by L^j made.

Since x,y,z and M are real on the original interval,
conjugate(K)=((z-x/4)+iy)^2/2 there. Substitution gives
M conjugate(K)=R^4 P(D); four minus signs cancel. Also
conjugate(E)=E^(-1) and |Z_N|^2 Z_N^2=Z_N^3 conjugate(Z_N).
Hence conjugating the complex integrand leaves exactly E P(D)
conjugate(Z_N)^3 Z_N, not E^(-1) or an absolute square.
Gamma duplication and reflection yield
chi(1-s)=2(2pi)^(-s) Gamma(s) cos(pi s/2), proving (4)
with both exponential branches and their coefficients intact.

To check the complete finite expansion without discarding any monomial,
assign to each term of D_j the tuple (p,b,c,m) recording h_p,
Omega^b, (Omega')^c and L^(-m). The possible tuples are

    D_0: (0,0,0,0);
    D_1: (1,0,0,1), (0,1,0,1);
    D_2: (2,0,0,2), (1,1,0,2), (0,2,0,2), (0,0,1,2).

Each satisfies m=p+b+2c. Every monomial of P is a product of
exactly four such terms, so (5)--(6) cover every resulting term,
with d<=8. For the paired digamma expression the sector estimates
give Omega=O(ell), Omega'=O(H^(-1)), Omega''=O(H^(-2)).
For the last estimate one may apply Cauchy to the separately bounded
Omega' on a circle of radius H/10: both gamma arguments stay of
size comparable to H in fixed sectors away from the negative real
axis, giving the same O(H^(-1)) bound on that circle. This does not
differentiate a bare asymptotic error.
Termwise differentiation of Omega^b (Omega')^c L^(-m), with
nonnegative fixed b,c,m and L'=1/(2+tau), proves |w'|<=C ell^(-d)/H.
This remains valid when Omega or Omega' vanishes, since no division
by either is needed. Over length H the total variation is O(ell^(-d)).

**Signed right line and twists.** For a fixed response head every
twist is r^(it) with positive rational r=u/v. Since s=1/2+i tau,
the extension is r^(s-1/2), with an entire single-valued real-log
exponential. The series supported at indices vn has coefficients
c_p(n); because v is fixed, its subpolynomial bounds hold also as
bounds in the new index. Its absolute convergence on Re s>1 is
unchanged. Applying the cited fixed-right-line theorem with q=u
gives the cutoff vn<=Vu/(2pi) and phase exp(-2pi i vn/u),
exactly (8). No coprimality or periodic coefficient hypothesis is
used, and no growing integer is substituted into a fixed-q theorem.

The count of factorizations n_1 n_2 n_3 n_4<=X is at most
X(sum_(n<=X)1/n)^3<=X(1+log X)^3. Each logarithmic weight
is at most (log X)^d; the n=1 term is handled separately.
This proves the required main-sum bound even if the additive phase
has no cancellation. Subtracting the theorem at H and V is uniform
for H<=V<=2H, including its positive-exponential O(1) branch.
If B(V) denotes this signed primitive, partial summation gives
w(V-i11/20)B(V)-integral_H^V w'(t-i11/20)B(t)dt.
Its size is at most
C ell^(-d)[H ell^(d+3)+H^(11/20)]=O(H ell^3).
Thus the fast gamma factor stays inside the controlled primitive;
it is never treated as a slow coefficient.

**Sharp connectors.** Bourgain's 13/84+1/168=9/56 is strictly
less than 1/6, so the weaker critical-line exponent used here is
valid. On the fixed strip [1/2,11/10], remove the pole by multiplying
by s-1 and apply strip Phragmen--Lindelof with boundary exponents
7/6 and 1. Dividing by |s-1| comparable to H gives the linear
exponent B(sigma)=(5/18)(11/10-sigma), without a pole premise
on the full strip. The known polynomial growth of zeta meets the
strip growth condition. All bounds hold on slightly extended height
intervals as well, so Cauchy disks at H and 2H are included.

For sigma'=1/2-u, 0<=u<=1/ell, the functional equation gives
|zeta(sigma'+it)|<=C H^[u+B(1/2+u)]
=C H^[1/6+(13/18)u]. This differs from B(sigma') by at most
4/(9ell). On the rest of a disk of radius 1/ell, B varies by
at most 5/(18ell). Heights remain comparable to H, and the disks
stay below 11/10 for large H. Cauchy's estimate therefore gives
exactly (11), with the factors H^(O(1/ell)) absorbed into constants.
The four derivative powers ell^d cancel |w|<=C ell^(-d).
Stirling gives |chi(1-s)|<=C H^(sigma-1/2), uniformly in this
fixed strip, so the remaining exponent is

    sigma-1/2+4B(sigma)=13/18-sigma/9 <= 2/3.

Both fixed-length connectors thus cost O_(r,p)(H^(2/3)), strictly
below H ell^4. The entire integrand is holomorphic on the rectangle;
in particular zeta's pole and the gamma/polygamma poles have real
height zero, and Log(2+tau) is nonzero with no cut crossing here.
No residue, sharp endpoint or branch change has been omitted.
The finitely many fixed-head terms give O_N(H ell^3) on the
original line after this contour shift.

**Uniform full-tail limit.** Since |Z|,|Z_N|<=M_0 and
|Z-Z_N|<=eta_N, a four-factor telescoping expansion gives
|Z^3 conjugate(Z)-Z_N^3 conjugate(Z_N)|<=4M_0^3 eta_N.
With |M K|<=C U^2, (12) follows uniformly in N. The audited
L390 Hardy fourth-moment budget gives integral U^2/H<=C ell^4.
If I(H) is the mean in (1), then for every fixed N,

    limsup_(H->infinity) |I(H)|/ell^4 <= C eta_N.

The constant on the right is independent of N; the fixed-head
O_N(ell^3) term has vanished before this inequality is taken.
Letting N tend to infinity proves zero limsup. No growing-head
constant or interchange of two uncontrolled limits is involved.

The complete k=1 estimate passes unchanged, as do L390's physical
input and full-tail budgets. This audit adds no moment coefficient or
new dependency. The k=0, k=2 and positive complete beta questions
remain separate; all actual-theta positivity and count gaps remain open.

## Mathlib

Full matching signed gamma-weighted moment, Bourgain subconvexity
and physical k=1 specialization coverage has not been checked.
Supporting contour, finite polynomial and summation facts alone
would not formalize the imported analytic inputs. No Lean
verification, library absence or novelty beyond the checked sources
is claimed. This is a partial local reproduction, not an RH candidate.
