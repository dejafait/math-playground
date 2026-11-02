# Lemma 656: one polynomial controls two dense narrow pole clouds

## Hypotheses

Let n>=5, x=-d=-5/4, R=11/8, U=R^2, eta=1/100 and t_j=j/n
for 0<=j<n. The finite set Z consists of distinct points a satisfying
Re(a)=x and |a|<=R-eta, and contains x. Its original simple-pole
residues r_a are positive integers, M=sum_a r_a<=n/3, and N=|Z|.
The family is independent of |u|=1. There is no separation, symmetry
or coefficient-integrality assumption. Define

    B_u(z)=product_(j<n) R(z-t_j*u)/(U-t_j*z/u),
    b_u(zeta)=B_u(R*zeta),  W_a(u)=B_u(x)/B_u(a),
    L(z)=sum_a r_a/(z-a),  q_u(zeta)=sum_a r_a W_a(u)/(R*zeta-a).

The full analytic component F_u is determined by
b_u q_u=B_u(x)L(R*zeta)-F_u. All grid factors and the conjugated
denominator angle are retained. Use normalized spatial and angular
circle means and <f,g>=mean f conjugate(g), linear in its first entry.
Put

    D_u=sum_a r_a^2 |W_a(u)|^2/(U-|a|^2),
    D_single,n=mean_u D_u,
    D_(u,M)={P_+(b_u J s): deg s<M},
    J s=zeta^(-1)conjugate(s),
    J_n=mean_u ||Proj_(D_(u,M)) F_u||_2^2,
    sigma=sqrt(137/5000),
    delta=log(26/19)-(log 2)/3,  tau_n=(M/sigma)exp(-delta*n),
    f_u(z)=conjugate(B_u(x))/B_(conjugate(u))(2x-z).

For the auxiliary construction choose c1,c2 in Z, allowing c1=c2,
and an integer m>=1 with 2m<=M. Suppose every a in Z satisfies
min(|a-c1|,|a-c2|)<=h, where 0<=h<r=m/(8n). Set

    Q(z)=(z-c1)^m(z-c2)^m,  q=2m,
    B=max(|W_c1(u)|,|W_c2(u)|),
    S=sum_a r_a |W_a(u)|^2,  A=S/R,
    K=4m exp(m)(22n/m)^(2m-1),
    E=[2r/(r-h)] exp(m)(3h/r^2)^m.

Let H_u be the degree-<2m polynomial with f_u-H_u divisible locally
by Q at its zeros. For c1!=c2 this matches m Taylor coefficients at
each center; for c1=c2 it matches 2m coefficients there. Existence
without an inverse center separation is proved below. These are
artificial approximation conditions, independent of original residues.
Put s_u(zeta)=H_u(R*zeta).

## Conclusion

Uniformly in u, all center separations and the permitted family,

    ||s_u||_2<=B K,
    |H_u(a)-conjugate(W_a(u))|<=B E  for every a in Z,       (1)
    |R^(-1)sum_a r_a W_a(u)H_u(a)-A|<=E sqrt(M) A.          (2)

If E sqrt(M)<=1, the full joint certificate is

    ||Proj_D F_u||_2
      >=max(0,(1-E sqrt(M))*sigma/[R sqrt(M) K]*sqrt(D_u)
                    -tau_n).                              (3)

In particular, suppose

    n>=32768,
    c1,c2 in Z,  min(|a-c1|,|a-c2|)<=2^(-34) for every a.   (4)

There is no further restriction on N or M, and

    ||Proj_D F_u||_2^2 >= (1/4)exp(-n/16)D_u,
    J_n >= (1/4)exp(-n/16)D_single,n.                       (5)

The centers may be anywhere on the admissible vertical segment,
including far apart or coincident. Thus two spatially separated dense
clouds are covered, with all cross-cloud values paid by one polynomial.
The radius 2^(-34) is stringent; this does not subsume L655's larger
single-cloud radius or establish the unrestricted spread-family bound.
More than two such clouds and general dense support remain open.
Xi realization, matching upper bounds, all-degree signs and inherited
audits remain independent. This result is separately unaudited and
is neither certified originality nor an RH candidate.

## Proof

### 1. Scope, named inputs and complete response

Reuse the unchanged invocation-start EXPLORE assessment
drafts/literature/2026-11-02-joint-full-grid-polynomial-dual.md.
Its finite polynomial/residue scope covers this same joint target.
The scoped local comparison read L654's full adaptive-contour proof,
L655's single-center proof, L651's Gram/correction proof, and the
relevant C645y/L649/L650 definitions and response. L652's repeated-jet
stop and L647's constant grouping stop remain valid contrasts. The
construction uses a chosen low degree, not all original multiplicity
jets or a sum of independently optimized cloud energies. No novelty
is inferred from this comparison.

Import the residue theorem from R. W. Howell and J. H. Mathews,
Complex Analysis, online edition, front matter updated 22 August
2025, [Section 8.1, Theorem 8.1.5](https://complexanalysis.org/web/sec_residue-thm.html).
Its simple-pole case also gives the Cauchy formula used below.
Supporting Hardy projections are L. Baratchart, S. Chevillard and
T. Qian, Minimax principle and lower bounds in H2-rational
approximation, J. Approx. Theory 206 (2016), 17--47, preprint v2,
24 March 2015, [Section 4, (17)--(19)](https://arxiv.org/pdf/1501.01161v2),
[DOI](https://doi.org/10.1016/j.jat.2015.03.004).
Fourier orthogonality and Parseval are A. Levitt, Analyse de Fourier
et applications, version retrieved 2 November 2026,
[Theorem 1.3/Exercise 1.2 and Theorem 1.11/Corollary 1.12,
printed pp.6,8](https://www.imo.universite-paris-saclay.fr/~antoine.levitt/blog/fourier/article.pdf).
The ready assessment chain inspected these inputs; this turn does
not retrieve them again or audit their proofs. The finite contour
calculation is needed because those standard facts do not supply its
explicit error/norm balance. No general approximation theorem is
asserted or reproved.

All B_u(a) are nonzero: |a|>=d>t_j and U>t_j|a|. The possible
finite poles of f_u are 2x-t_j*conjugate(u), of modulus >3/2.
Since 2x-a=conjugate(a), f_u(a)=conjugate(W_a(u)). Also
|Im(a)|^2<=12029/40000<1, so |c1-c2|<2. For a center c in Z,
the exact ratio, with v=z-c, is

    f_u(c+v)/f_u(c)
      =product_(j<n) [1+t_j*u*v/(U-t_j*u*conjugate(c))]
                    /[1-v/(conjugate(c)-t_j*conjugate(u))]. (6)

The numerator coefficient has modulus <2 since U-|c|>1/2;
the denominator coefficient has modulus <4 since d-t_j>1/4.
For |v|<=r<=1/16, this gives

    |f_u(c+v)|<=|f_u(c)|[(1+2r)/(1-4r)]^n
                      <=|f_u(c)| exp(8nr).                (7)

Indeed log(1+2r)<=2r and -log(1-4r)<=4r/(1-4r)<=16r/3;
their sum is <8r. No logarithm branch of f_u is required. The
auxiliary degree hypothesis gives r=m/(8n)<=1/48<1/16.

For any polynomial s of degree <M, set v=P_+(b_u J s) and
e=P_-(b_u J s). L650's complete response and L651 give

    <F_u,v>=B_u(x)<L(R*zeta),e>
                         -R^(-1)sum_a r_a W_a(u)s(a/R),
    ||v||<=||s||,
    |B_u(x)<L(R*zeta),e>|<=tau_n||s||.                     (8)

L651 also gives a strictly positive lower Gram bound for nonzero s,
delta>1/16, and D_u>=64/21. The entire correction in (8) will be
paid. No grid prefix, separate-column normalization or assumed
cross-term positivity is used.

### 2. A confluent polynomial on a union of two disks

First take a radius r'>h, r'<=1/16, avoiding the possible tangency
of the two radius-r' disks about c1,c2. Let Omega be their union.
Its boundary is piecewise smooth, has total length <=4*pi*r',
and every boundary point w has |w-ci|>=r' for both centers.
Moreover |w|<=R-eta+r'<3/2, so f_u is holomorphic on a
neighborhood of its closure. For coincident centers Omega is a
single disk and the same length bound remains valid.

Define the polynomial kernel and polynomial

    K_Q(w,z)=(Q(w)-Q(z))/(w-z),
    H_u(z)=1/(2*pi*i) integral_(boundary Omega)
                               f_u(w) K_Q(w,z)/Q(w) dw.    (9)

Use the polynomial extension at w=z, so the integrand has no
singularity there and H_u has degree <q in z. For z inside Omega,
splitting the kernel and applying the Cauchy formula gives

    f_u(z)-H_u(z)=Q(z)/(2*pi*i) integral_(boundary Omega)
                               f_u(w)/[Q(w)(w-z)] dw.     (10)

The last integral is analytic in z on the interior of Omega. Thus
f_u-H_u has at least the multiplicities specified by Q at its zeros.
This proves existence, including coincident centers with multiplicity
2m. Uniqueness follows since a difference of two such degree-<q
polynomials is divisible by the degree-q polynomial Q. In particular
H_u is independent of the chosen regular radius.

Order the q factors of Q, with repetitions. Telescoping the difference
of products shows that K_Q is a sum of q products of q-1 factors,
each of the form w-ci or z-ci. On |z|=R, |z-ci|<2R.
On a boundary arc generated by one center, every |w-ci| is at most
r'+|c1-c2|<1/16+2<2R. Consequently

    |K_Q(w,z)|<=q(2R)^(q-1),  |Q(w)|>=(r')^q.            (11)

On each arc (7) bounds |f_u(w)| by B exp(8nr'). The full boundary
length in (9) therefore gives

    ||H_u(R*zeta)||_2<=2q B exp(8nr')(2R/r')^(q-1).        (12)

This estimates the finite polynomial on the whole spatial circle;
it does not extrapolate convergence of a local infinite series there.

For every actual pole a choose one center within h. As h<r'<1,

    |Q(a)|<=h^m(|c1-c2|+h)^m<=(3h)^m,
    |w-a|>=r'-h  on boundary Omega.                       (13)

The pole a lies inside Omega. Equations (10), (7), (11), (13)
and the complete boundary length now yield

    |f_u(a)-H_u(a)|
       <=[2r'/(r'-h)] B exp(8nr')(3h/(r')^2)^m.           (14)

Both cross-cloud errors are included even when the disks overlap.
When h=0 the right side is zero, consistently with the interpolation.

Regular radii tend to r=m/(8n) and are eventually >h. The polynomial
H_u is fixed across these radii. Taking the limit only in the scalar
bounds (12) and (14) proves (1), since 8nr=m and 2R/r=22n/m.
No contour convergence or interchange with the angular mean is needed.
The repeated-root construction treats c1=c2 directly; no inverse
separation or unproved coalescence limit enters.

### 3. Both cloud errors, the original diagonal, and full cost

The centers are actual poles and r_a>=1, so B^2<=S.
Weighted Cauchy--Schwarz gives sum_a r_a |W_a|<=sqrt(M S).
Use (1) inside the complete residue pairing:

    |R^(-1)sum_a r_a W_a H_u(a)-A|
       <=(B E/R)sum_a r_a |W_a|<=E sqrt(M) A.             (15)

This proves (2) without discarding any phase before bounding its
error. Since f_u(c1)!=0, H_u is nonzero, and its joint image is
nonzero by L651. Equations (8), (15) and ||s_u||<=B K give

    ||Proj_D F_u||>=max(0,(1-E sqrt(M))*A/(B K)-tau_n)

when E sqrt(M)<=1. The original diagonal satisfies

    D_u<=sigma^(-2)sum_a r_a^2 |W_a|^2<=M S/sigma^2.

Together with B<=sqrt(S), this gives
A/(B K)>=sigma sqrt(D_u)/(R sqrt(M) K), proving (3).
The calculation pays arbitrary original multiplicities.

### 4. Explicit degree, error, exponent and onset

Assume (4) and first M>=2m, where m=ceil(n/2048). Then

    m>=16,  n/2048<=m<=17n/32768,
    r>=2^(-14),  h/r<=2^(-20),  3h/r^2<=3/64.             (16)

The exponential series gives e<3: use 1/k!<=2^(-(k-1)) for k>=2,
strictly for k>=3. Since 2r/(r-h)<3, this implies

    E<3*(9/64)^m<=3*4^(-m).

As M<=n<=2048m and sqrt(M)<=M,

    E sqrt(M)<=6144m*4^(-m)<=6144*16/4^16
                         =3/131072<1/4.                  (17)

For integers m>=16 the middle bound follows since the ratio of
consecutive m*4^(-m) is (m+1)/(4m)<=1/2 for m>=1.

Next 22n/m<=45056 and log 45056<11. An exact witness is
e>8/3 (the series through the cubic term), and (8/3)^11>45056.
Also log(4m)<=2m for m>=1, since exp(2m)>=1+2m+2m^2>4m.
Therefore

    log K<2m+m+22m=25m<=425n/32768<n/64.                  (18)

Using M<=n/3 and 108sigma^2>R^2 gives

    (3/4)*sigma/[R sqrt(M) K]
       >=[1/(8 sqrt(n))]exp(-n/64)>=exp(-n/32).           (19)

The first constant comparison follows by squaring
3sigma sqrt(3)/(4R)>1/8; all factors are positive. For the last
comparison exp(n/64)>=n^2/8192>=8sqrt(n) whenever n^3>=2^32,
as holds for every n>=32768.

The entire correction, using L651's anchor and delta bounds, satisfies

    tau_n/[exp(-n/32)sqrt(D_u)]
       <=sqrt(21)/(24sigma)*n*exp(-(delta-1/32)n)
       <2n exp(-n/32)<=393216/n^2<=3/8192<1/2.            (20)

Here 21<2304sigma^2 proves the coefficient comparison, and the cubic
term of exp(n/32) proves the penultimate inequality. Combining (3),
(17)--(20) proves the pointwise assertion (5) when M>=2m.

If M<2m, then N<=M<2m<=17n/16384<n/384. L654 (5) supplies the
same pointwise bound, since n>=32768>8192. No polynomial exceeding
the permitted degree M-1 is used in this case.

For each fixed family, F_u and L651's invertible Gram matrix are
continuous in u, so the projection norm and D_u are integrable.
Integrating the pointwise result in normalized angular measure proves
the second part of (5). Centers can be selected from the family before
this mean; the estimates are uniform in their separation.

### 5. Verification and limits

Exact scalar witnesses are reproduced by
python3 scripts/one-sided-hankel/two-center-constants.py; the full
certificate is scripts/one-sided-hankel/two-center-constants.json.
These check the radius, degree, error, exponent, diagonal and
correction inequalities. The analytic argument and uniform family
conclusion are proved above, not by finite checks. The new lemma
and its inherited inputs still await separate critical audits.

This new subfamily allows arbitrary original distinct count and mass
near two arbitrarily separated admissible centers. One polynomial pays
the complete norm and both cloud errors. The proof does not assert a
constant comparison with the sum of cloud energies, which would ignore
L647's obstruction. The small radius cannot be extrapolated to general
dense spread families; their joint comparison remains open.

## Mathlib

Full matching coverage for this grid-specific two-center approximate
value bound has not been checked. Supporting residue, projection and
Fourier facts are the precise named imports above. Unknown coverage
is not evidence of absence. No formal theorem asserting the full
spread-family comparison or actual-Xi positivity is assumed.

