# Lemma 593: no bounded coupled homogeneous completion of the fixed ellipse

## Hypotheses

Use real coordinates

    v=(x,y,z,X,Y,Z),     w=(x,y,X,Y),     dot_w=(y,z,Y,Z).

The prescribed raw second-moment matrix is exactly L473/L592's matrix,
in increasing lag r=0,1 and derivative order j=0,1,2:

    K_((r,j),(s,k))
      =integral_(-1/2)^(1/2) Re((iu)^j(-iu)^k exp(i(r-s)u)) du,
    K=[[K_0,D],[D^T,K_0]],
    K_0=[[1,0,-1/12],[0,1/12,0],[-1/12,0,1/80]].            (1)

Let mu be any bounded-support probability law on R^6 with
E_mu vv^T=K and the following exact first-triple marginal from L592:

    theta uniform on [0,2pi], independent of k,
    P(k=1/12)=1/6,    P(k=-7/60)=5/6,
    x=sqrt(2)cos(theta), y=sin(theta)/sqrt(6), z=kx.        (2)

The other triple may depend arbitrarily on theta and k and may use
additional randomness. No conditional independence, Schur-form law,
path realization or support bound common to all completions is imposed.
Centering of mu may be required in the application; the obstruction
below does not need it.

The permitted storage class consists of every globally C1 function
V:R^4 -> R such that V(a w)=a^2 V(w) for a>0. Write

    D V(v)=gradient V(w) dot dot_w.

## Conclusion

For every law mu satisfying the hypotheses, there is a member V of
the permitted class such that

    E_mu D V(v)>1/10000.                                   (3)

Consequently no bounded centered full-K completion of the fixed
marginal (2) can satisfy E_mu D V=0 for every permitted V. The law
would have to work for all V; the separating V may depend on its
finite support bound. Its coefficients below otherwise do not depend
on the completion.

This stops exactly the proposed fixed-marginal completion. L592's
bounded full-K W+U comparison law, its all-one-height cancellation and
its clipped mean 1/(36pi)>1/288 remain valid. There is no claim that
the enlarged coupled certificate class has a cheap certificate, that
another marginal cannot annihilate it, or that a periodic/lag law or
actual-Xi sign has been obtained. Unbounded completions are not covered.
The separate conceptual and exact-arithmetic audit in Section 5 passes
without changing the claim. This is a local specialization, with no
certified novelty claim beyond the assessed sources.

## Proof

### 1. Known inputs and the new test

The invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-31-coupled-four-state-flux-scope.md`
covers exactly testing bounded completions of (2). L592 supplies its
first-triple moments and clipping; those results are not reproved here.
L473 Sections 3--4 supply K>0 and its Schur complement positivity.
The ordinary Cauchy--Schwarz inequality and finite-dimensional spectral
theorem are the only additional general mathematical inputs.

The known sufficient weak-bound framework is A. Chernyavsky,
J. J. Bramburger, G. Fantuzzi and D. Goluskin,
[*Convex relaxations of integral variational problems*,
arXiv:2110.03079v1, Lemma 2.1 and (2.4)--(2.11), pp.8--10](https://arxiv.org/pdf/2110.03079v1),
with the C1 chain-rule formulation in G. Fantuzzi,
[*Verification of some functional inequalities via polynomial
optimization*, arXiv:2201.00362v1, Lemma 5 and (7)--(10), PDF p.3](https://arxiv.org/pdf/2201.00362v1).
The ready assessment compares their vector-state hypotheses. Neither
source supplies this marginal or separator. No sharpness, realization
converse, occupation-measure equivalence or reproof of those theorems
is used: this proof only tests the prescribed universal derivative
identity directly.

For (x,y) != (0,0), define

    r^2=x^2/2+6y^2,
    A=2x^3/r^2-3x,             B=3y-24y^3/r^2,
    F=A+2B,                   G=-A/2-5B/8,
    V_loc(w)=F(x,y)X+G(x,y)Y.                              (4)

A,B,F,G are smooth and positively homogeneous of degree one on
this domain. V_loc has degree two. It is not asserted to be globally
C1; Section 2 supplies the necessary extension. On (2), r=1.
With D F=F_x y+F_y z and D G=G_x y+G_y z, the ordinary product rule
there gives

    D V_loc=h dot b_1,
    b_0=(x,y,z)^T, b_1=(X,Y,Z)^T,
    h=(D F,F+D G,G)^T.                                    (5)

### 2. A valid global homogeneous storage for each bounded completion

Fix the law mu under consideration. Choose a finite b>=0 with
X^2+Y^2<=b^2 on a full-measure bounded support for mu. Let chi be a
C1 function on [0,infinity), equal to one for s<=b^2+1, zero for
s>=b^2+2, and between these points given by

    chi(s)=1-3t^2+2t^3,     t=s-(b^2+1),  0<=t<=1.

Both joining derivatives are zero. For r>0 put

    V(w)=chi((X^2+Y^2)/r^2) V_loc(w),                      (6)

and put V(w)=0 when r=0. This is positively homogeneous of degree
two, since the cutoff argument has degree zero. At every nonzero
w with r=0, X^2+Y^2>0. In a neighborhood of that point the ratio
exceeds b^2+2 wherever r>0, so V is identically zero there.
Thus V is C1 away from the full origin, including points with r=0
and the cutoff's joining surfaces.

Its restriction and gradient on the Euclidean unit sphere are
continuous and bounded. Differentiating the homogeneity identity
away from zero gives gradient V(a w)=a gradient V(w). Therefore
|V(w)|<=c_0 |w|^2 and |gradient V(w)|<=c_1 |w| for w != 0.
The first estimate proves differentiability at zero with derivative
zero, and the second proves continuity of that derivative. Hence V
is globally C1, with the permitted degree-two homogeneity.

On mu's support r=1 and (X^2+Y^2)/r^2<=b^2. The cutoff is
identically one on a neighborhood of each support point, so its
derivative contributes zero and D V=D V_loc=h dot b_1 there.
The growth bound also gives |D V(v)|<=c_1 |v|^2; all integrals
below are absolutely convergent. No inadmissible all-C1 or
nonhomogeneous test has replaced the stated storage class.

### 3. Remove the part determined exactly by covariance

All expectations in the next rational matrices use just (2). Set

    J=E h b_0^T,        L=J K_0^(-1),
    h_perp=h-L b_0,     C=E h_perp h_perp^T.

Direct integration, detailed in Section 4, yields

    K_0^(-1)=[[9/4,0,15],[0,12,0],[15,0,180]],
    J=[[0,0,1/90],[0,0,-1/288],[0,0,0]],
    L=[[1/6,0,2],[-5/96,0,-5/8],[0,0,0]],
    C=[[58/45,-1691/2880,3/32],
       [-1691/2880,65503/46080,-29/48],
       [3/32,-29/48,217/768]].                             (7)

In particular E h_perp b_0^T=J-L K_0=0 exactly. For any completion,
define the random vector and deterministic matrix

    R=b_1-D^T K_0^(-1)b_0,
    T=K_0-D^T K_0^(-1)D>0.                               (8)

The strict positivity follows from K>0 in L473. Expanding the
four terms using E b_0 b_0^T=E b_1 b_1^T=K_0 and
E b_0 b_1^T=D gives E RR^T=T. This is true for every completion,
not only the independent-noise completion used in L592.
The same exact covariance and orthogonality give

    E D V=E h dot b_1=m+E h_perp dot R,
    m=trace(L D).                                         (9)

The orientation of D matters: the determined term is
sum_(i,j) L_ij E (b_0)_j (b_1)_i=sum_(i,j) L_ij D_ji.
There is no centering or conditional-drift assumption in (8)--(9).

Apply Cauchy--Schwarz on the probability space to T^(1/2)h_perp
and T^(-1/2)R. Symmetric roots exist since T>0. The two squared
norm expectations are respectively trace(T C) and
trace(T^(-1) E RR^T)=3. Consequently

    |E h_perp dot R|<=sqrt(3 trace(T C)).                  (10)

This bounds the error uniformly over every possible dependence
structure of the second triple. No sampling of storage functions or
finite-basis completeness assertion enters.

### 4. Exact circular moments and the rational interval certificate

For nonnegative integers p,q,s the elementary circular integral gives

    E x^(2p)y^(2q)k^s
      =(2^p/6^q) ( (2p)!(2q)! / (4^(p+q)p!q!(p+q)!) )
        *[(1/6)(1/12)^s+(5/6)(-7/60)^s].                  (11)

A monomial with an odd exponent of x or y has zero expectation,
by reflection of theta; k is independent. Formula (11) also follows
by integrating the usual sine/cosine power identities over one period.
To compute (7), evaluate the following derivatives at r^2=1:

    A=2x^3-3x,                  B=3y-24y^3,
    A_x=6x^2-2x^4-3,           A_y=-24x^3y,
    B_x=24xy^3,                 B_y=3-72y^2+288y^4,
    D A=A_x y+A_y kx,           D B=B_x y+B_y kx,
    h=(D A+2D B, A+2B-D A/2-5D B/8, -A/2-5B/8)^T.       (12)

The derivatives are taken before setting r^2=1; differentiating
the restricted polynomials A,B instead would be wrong. Expand (12)
and use (11) in J and E hh^T. Then C=E hh^T-J K_0^(-1)J^T
gives exactly (7). This is a finite polynomial calculation; the full
coefficient lists and rational matrices are retained in the certificate.

It remains to bound m and 3 trace(T C) with the exact spectral D,
not a rounded matrix. In (1), D has entries

    D_jk=integral_(-1/2)^(1/2)
              Re((iu)^j(-iu)^k exp(-iu)) du,  0<=j,k<=2.

Expand exp(-iu) through n=N=20. The exact rational truncated value is

    d_jk=sum_(0<=n<=N, j+k+n even)
          (-1)^((j-k-n)/2) / [n! 2^(j+k+n)(j+k+n+1)].     (13)

The exponent in the sign is an integer on the displayed parity class,
including negative integers. The exponential Taylor remainder is at
most exp(|u|)|u|^(N+1)/(N+1)!. Since exp(1/2)<2 (compare its
series with the geometric series), integration gives

    |D_jk-d_jk|<=e_jk,
    e_jk=2/[(N+1)! 2^(j+k+N+1)(j+k+N+2)].                (14)

All matrix additions and multiplications in (8)--(10) can now use
the rational intervals [d_jk-e_jk,d_jk+e_jk]. Interval products
take the minimum and maximum of the four endpoint products;
dependent occurrences are enclosed without assuming independence.
The full exact interval calculation gives these outward coarsenings:

    421507201/200000000000 <= m
        <=1053768003/500000000000,
    3873179/10^12 <= 3 trace(T C) <= 193659/50000000000.    (15)

In particular, with strict margins,

    m>21/10000,          3 trace(T C)<1/250000=(1/500)^2. (16)

The reproducible exact-fraction script is
`scripts/coupled-flux/exact_completion_separator.py`;
run `python3 scripts/coupled-flux/exact_completion_separator.py`.
Its full certificate is
`scripts/coupled-flux/exact_completion_separator.json`.
It records (12), J,L,C, every spectral and Schur entry interval, the
uncoarsened scalar intervals, all thresholds and all failed checks
(none). It also checks K_0's inverse, the marginal matrix, projection
orthogonality, and C by direct residual integration. The selected
complete J,L,C and uncoarsened scalar intervals were inspected after
the run. The earlier floating-point probe
`scripts/coupled-flux/completion_probe.json` only selected the test;
it is not evidence for (15)--(16).

Finally (9), (10) and (16) give

    E D V>=m-sqrt(3 trace(T C))
          >21/10000-1/500=1/10000>0.

This proves (3) and contradicts the required all-storage cancellation.
The cutoff is allowed to depend on the candidate law's support bound:
for each candidate it gives one admissible V violating that candidate's
universal quantifier. It does not choose a different comparison law
for each test. The proof has used no full-C1 stationarity condition,
no actual lag relation, no fourth moments, and no Xi substitution.

### 5. Independent conceptual and exact-arithmetic audit, 31 October 2026

The invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-31-l593-independent-audit-scope.md`
approved this exact audit. Its primary sufficient-method comparison is
reused; none of the source sharpness or realization results is invoked.
The audit verifies this local obstruction, not the source manuscripts,
new mathematics beyond the inspected sources, or an RH candidate.

**Inputs and admissibility.** L592's exact marginal has r=1 almost
surely and all six distinct entries of K_0 as in (1). L473 Section 3
applies to precisely this spectral K: the quadratic form is the integral
of |P_0(iu)+exp(iu)P_1(iu)|^2. Continuity, the entire identity theorem,
and u=iv with v tending to positive infinity force both polynomials to
vanish if the form is zero. Therefore K>0. The quadratic-form test at
(-K_0^(-1)D a,a) gives T>0 for every nonzero a. No arithmetic moment
asymptotic, earlier finite marginal or uniform eigenvalue lower bound
enters this application.

For a candidate bounded-support law choose b as in Section 2. Its closed
support can be used: r=1 and the bound on X^2+Y^2 hold there by continuity.
At any nonzero point with r=0, the second pair is nonzero, so (6) vanishes
on an open neighborhood. On r>0 the ratio and V_loc are smooth; the two
zero joining derivatives of chi give a C1 product also at its joins.
Thus V is C1 on the punctured four-space. On the unit sphere both V and
its gradient are bounded, and positive homogeneity gives exactly the
quadratic and linear bounds used at the full origin. The first bound
proves Frechet differentiability there with derivative zero; the second
proves continuous differentiability. There is no C2 requirement.
The plateau has a strict margin of one above the support ratio, hence
V and its complete first derivative agree with V_loc near every support
point, regardless of the velocity (y,z,Y,Z). A support-dependent b changes
the test function only: for each fixed law required to cancel every V,
this one allowed V contradicts that requirement. No common b is needed.

**Raw moments, orientation and error.** With B=D^T K_0^(-1), expand
E(b_1-Bb_0)(b_1-Bb_0)^T=K_0-BD-D^T B^T+B K_0 B^T=T.
These are raw second matrices, so possible nonzero means cause no extra
terms. Direct projection gives E h_perp b_0^T=0. Consequently the mean
is sum_(i,j)L_ij D_ji+E h_perp dot R, exactly trace(LD), not trace(LD^T).
For the random vectors T^(1/2)h_perp and T^(-1/2)R their inner product
is h_perp dot R and their mean squared norms are trace(TC) and 3.
Cauchy--Schwarz on the probability space proves (10) with no assumption
of centering, conditional independence or a special completion law.

**An independent circular calculation.** The audit script does not
import the construction script. Write

    x=sqrt(2) rho cos(theta), y=rho sin(theta)/sqrt(6).

On the support rho=1 and z=kx. Along the direction (y,z), differentiation
of these two coordinate identities gives

    dot_rho=(1+12k)cos(theta)sin(theta)/sqrt(12),
    dot_theta=(12k cos^2(theta)-sin^2(theta))/sqrt(12).

Since A=sqrt(2)rho cos(3theta) and B=rho sin(3theta)/sqrt(6),
these identities calculate DA and DB without differentiating the
restricted Cartesian polynomials. For an exact Fourier implementation
put t=exp(i theta), c_n=(t^n+t^(-n))/2 and s_n=(t^n-t^(-n))/2.
Here s_n=i sin(n theta). With c=c_1, s=s_1 set

    a=(1+12k)c s, b=12k c^2+s^2,
    q_A=-a c_3/6+b s_3/2, p_B=-a s_3/12+b c_3/4.

Then DA=i sqrt(6)q_A, DB=sqrt(2)p_B, and each h_i has form
sqrt(2)p_i+i sqrt(6)q_i with

    (p_0,q_0)=(2p_B,q_A),
    (p_1,q_1)=(c_3-5p_B/8,-s_3/3-q_A/2),
    (p_2,q_2)=(-c_3/2,5s_3/48).

The corresponding pairs for b_0 are (c,0),(0,-s/6),(kc,0).
Every p is reciprocal under t -> 1/t and every q is anti-reciprocal.
Thus mixed p q terms have constant coefficient zero. Write CT for the
constant Laurent coefficient. The exact circular mean of a product is
2 CT(p_i p_j)-6 CT(q_i q_j). Average over the
two k values with weights 1/6 and 5/6. All entries of J,L,C are (7),
and the independently obtained unprojected second matrix is

    E hh^T=[[59/45,-1711/2880,3/32],
            [-1711/2880,65603/46080,-29/48],
            [3/32,-29/48,217/768]].                        (17)

Exact Gauss--Jordan inversion yields the displayed K_0 inverse. Direct
Fourier integration of the projected residual checks all nine zero
orthogonality entries and all nine entries of C, not just its diagonal.
This also checks the original derivative formulas: the derivatives in
(12) follow from the quotient rule before restriction, including the
r^2 derivatives x and 12y. The original circular moment formula is the
usual even sine/cosine integral; both coordinate reflections preserve
the independent k law and annihilate odd exponents.

**Independent spectral enclosures.** Put S=sin(1/2), C_*=cos(1/2).
Integration by parts on [-1/2,1/2] gives

    C_0=integral cos u du=2S,
    S_1=integral u sin u du=2S-C_*,
    C_2=integral u^2 cos u du=2C_*-7S/2,
    S_3=integral u^3 sin u du=23C_*/4-21S/2,
    C_4=integral u^4 cos u du=337S/8-23C_*,
    D=[[C_0,-S_1,-C_2],[S_1,C_2,-S_3],[-C_2,S_3,C_4]].   (18)

The phases i^(j-k)exp(-iu) fix all signs in this full matrix. For S
use the alternating terms (-1)^n/[2^(2n+1)(2n+1)!]; for C_* use
(-1)^n/[2^(2n)(2n)!]. The partial sums n=0,...,16 and the same sums
including n=17 enclose the exact values, because the term magnitudes
strictly decrease to zero. Rational interval propagation through (18)
and (8)--(10) therefore gives a separate certificate of the actual
spectral calculation, independent of the original exponential expansion.

For comparison, the original expansion's phase is i^(j-k-n), and
integration of |u|^(j+k+21) times 2/21! gives exactly (14) at N=20.
The geometric-series comparison proves exp(1/2)<2 strictly. Thus its
remainder and interval arithmetic are also valid. The new enclosures
are contained in every original D and T entry interval, both original
uncoarsened scalar intervals, and both displayed coarsenings (15).
Dependence between repeated entries need not be removed for interval
containment. Independently obtained outward bounds are

    2107536005367/10^15 <= m <= 2107536005368/10^15,
    3873179520/10^15 <= 3 trace(TC) <= 3873179521/10^15.    (19)

Their rational comparison with 21/10000 and 1/250000 is strict. Since
T>0 and C=E h_perp h_perp^T is positive semidefinite, the square root
in (10) is the nonnegative real one. Equations (9)--(10) again give
E D V>1/10000 for every candidate completion. No correction is needed.

Reproduce the independent check with
`python3 scripts/coupled-flux/audit_completion_separator.py`.
The full certificate is
`scripts/coupled-flux/audit_completion_separator.json`; it retains both
curvature cases' complete Fourier coefficients, complete rational
matrices, all spectral/Schur intervals and every check/failure. All 18
checks pass. The complete Fourier coefficients of h in both cases,
J,L,C,E hh^T, exact scalar endpoints and checks were inspected; all nine
D/T entries were compared using exact arithmetic. This is arithmetic
evidence coupled with the analytic proof above, not a numerical preview.
The construction's earlier evidence and its floating probe are preserved.

The verified result stops bounded completions of the exact marginal (2).
It does not decide another marginal, unbounded support, a cheap coupled
certificate, periodic/lag realization, or controlled nonlinear Xi
transfer. In particular L592's independent W+U obstruction survives.

## Mathlib

Full matching Mathlib coverage for this fixed-marginal completion
obstruction has not been checked. Cauchy--Schwarz, finite-dimensional
positive square roots, the C1 product/chain rules, circular integrals
and Taylor remainder bounds are supporting standard mathematics, not
a claimed formalization of the argument. The exact Python certificate
does not certify the analytic cutoff proof; that proof and the universal
quantifiers are checked in Section 5. This informal audit is not a
formalization. Unknown Mathlib coverage is not evidence of absence.
