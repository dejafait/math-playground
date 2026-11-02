# Lemma 585: a positive periodic carrier for the full leading fourth tensor

## Hypotheses

Use the six ordinary coordinates `(r,j)`, with `r=0,1`, `j=0,1,2`,
in the order of L473. Let `q=(q_m)_(|m|=4)` be precisely the 126 real
coefficients in L473 (9), including all lag allocations and odd entries.
The proof below uses that explicit integral formula. Its identification
with actual Hardy leading moments retains L473's arithmetic-source
qualifications, especially the imported, unaudited proof of Bui--Hall
Proposition 3. No additional arithmetic statement is assumed.

For a real periodic C2 function h with period P>0, define

    J_h(s)=(h(s),h'(s),h''(s),h(s+1),h'(s+1),h''(s+1)),
    T_m(h)=P^(-1) integral_0^P J_h(s)^m ds,
    C_2(h)=P^(-1) integral_0^P |J_h(s)|^2 ds.

The norm is Euclidean. Weights must be nonnegative; there is no
prescribed numerical upper bound on their sum, no common period or
frequency cutoff, and no requirement to realize L473's particular law.

## Conclusion

There are a finite number of fixed real C-infinity periodic functions
h_i, periods P_i>0, and fixed nonnegative weights a_i such that

    sup_s |J_(h_i)(s)|<=1,
    sum_i a_i T_m(h_i)=q_m                    for every |m|=4,
    W:=sum_i a_i<infinity,
    sum_i a_i C_2(h_i)<=W.                                  (1)

Thus the invocation's O(1/ell) approximation target holds for every
real ell>=1 with zero error, the same finite mixture, and fixed weight
and second-cost bounds. Existence is non-effective: no numerical
paths, weights, W or periods are supplied. The proof includes an exact
finite algebra certificate. The separate conceptual audit in Section 7
verifies the analytic assembly and the complete selected certificate;
the arithmetic source proof remains imported and unaudited.

This is local progress toward a derivative-consistent rare carrier,
not a stationary completion of all 147 second/fourth requirements.
Positive second completion, positive clipped mass, selected-law
realization, actual-Xi transfer and all-degree signs remain open.
Potential originality means only that the recorded source comparison
did not cover this construction; no broader novelty claim is made.

## Proof

### 1. A positive sinc-pulse formula for every entry

Fix any list `(r_l,j_l)`, l=1,...,4, representing m. Write
`g_l(k)=(ik)^(j_l) exp(i r_l k)`. In L473 (9), put

    a=1/2-u_1, b=1/2-u_2, S=a+b, d=|b-a|.

For each orientation of a,b, the Jacobian to (S,d) is 1/2;
`-1<=S<=1` and `0<=d<=1-|S|`. The variables A,C independently
run over the interval with endpoints a,b, while
`B=S-A`, `D=S-C`. Away from the measure-zero set d=0, changing
u_3,u_4 to A,C has absolute Jacobian d^(-2). It cancels
`(u_1-u_2)^2=d^2`. The two orientations together cancel 1/2.
Consequently the original integral becomes

    (3/pi^2) integral dS integral_0^(1-|S|) dd
       integral_((S-d)/2)^((S+d)/2) dA
       integral_((S-d)/2)^((S+d)/2) dC
       g_1(A) g_2(S-A) g_3(-C) g_4(C-S).

Set `k_1=A`, `k_2=S-A`, `k_3=-C`, `k_4=C-S`.
The absolute Jacobian between (S,A,C) and (k_1,k_2,k_3) is 1,
and `sum_l k_l=0`. The allowed d run from

    max(|k_1-k_2|,|k_3-k_4|) to 1-|S|.

For real x,y, `|x+y|+|x-y|=2 max(|x|,|y|)`.
The two pairs have sums S and -S. The length of the d interval
is therefore `1-2 max_l |k_l|`, when all |k_l|<=1/2, and zero
otherwise. Integrating d gives

    q_m=(3/pi^2) integral_(sum k_l=0, |k_l|<=1/2)
             (1-2 max_l |k_l|) product_l g_l(k_l)
                                  dk_1 dk_2 dk_3.         (2)

Here hyperplane integration means the displayed three coordinates,
not Euclidean hypersurface measure. The symmetric density checks
the occurrence-order invariance and the two reflected signs directly.
All these integrals are absolutely integrable on bounded sets.

For 0<=b<=1/2 define the real entire pulse

    f_b(s)=integral_(-b)^b exp(iks) dk
          =2 sin(bs)/s, with f_b(0)=2b.

The layer identity

    1-2 max_l |k_l|
      =2 integral_0^(1/2) product_l 1_(|k_l|<=b) db

holds on the support in (2). With the Fourier convention
`f(s)=integral g(k) exp(iks) dk`, the Plancherel theorem applied
to the products of the first two and last two factors gives

    integral_R product_l f_b^(j_l)(s+r_l) ds
      =2pi integral_(sum k_l=0, |k_l|<=b)
                       product_l g_l(k_l) dk_1 dk_2 dk_3.

This is the bilinear form of Plancherel: the last convolution is
evaluated at the negative of the first frequency. Each spectral
factor is bounded with compact support; its convolution with another
is L2. The physical products are L2 as well, since each factor is
both bounded and L2. Thus no distributional delta substitution or
uncertified infinite interchange is required. The named theorem is
used with its standard L2 hypotheses, not reproved here. Precisely, use
Terence Tao, *245C Notes 2: The Fourier transform* (6 April 2009),
[Theorem 43, Exercise 44 and (5)](https://terrytao.wordpress.com/2009/04/06/the-fourier-transform/).
The source convention is exp(-2pi i x xi); k=2pi xi gives the
normalization here. The inverse-transform product follows from Fubini
for the compactly supported L1 spectral factors, before applying L2
Plancherel to the two products.

It follows that, for every one of the 126 entries,

    q_m=(3/pi^3) integral_0^(1/2) U_m(f_b) db,
    U_m(f)=integral_R J_f(s)^m ds.                         (3)

For j<=2, differentiating the spectral integral bounds f_b^(j)
uniformly on compact s sets, uniformly in b. Differentiating
`2 sin(bs)/s` bounds it by `C/(1+|s|)` for |s|>=1, again uniformly
for 0<=b<=1/2. After enlarging C the same bound applies to the six
lagged coordinates. Hence every integrand in (3) is dominated by
`C(1+|s|)^(-4)`. This proves absolute convergence, continuity in b
including b=0, and the required Fubini and dominated-convergence uses.
As a normalization check, (2) gives `q_(4,0,0,0,0,0)=1/(2pi^2)`,
also obtained directly from L473 (9) by integrating `(u_1-u_2)^2`.

### 2. The actual periodic occupation cone and its universal identities

Let K be the set of all finite nonnegative sums of T(h), where h
is real C-infinity periodic and `sup |J_h|<=1`. Include the zero
sum. This is a convex cone in R^126; it is not assumed closed and
no compactness of the set of paths is asserted.

Identify a coefficient vector c with the homogeneous quartic
`F_c(v)=sum_(|m|=4) c_m v^m`. Two types of coefficient vectors
give exact zero integrals for every such periodic path:

* The total derivatives `D R`, for all degree-four polynomials R
  in `(x,y,X,Y)=(h,h',h(.+1),h'(.+1))`, where

      D R=y R_x+z R_y+Y R_X+Z R_Y.

* The 15 differences `p(x,y,z)-p(X,Y,Z)` for degree-four
  three-variable monomials p.

There are 35 displayed total-derivative generators and 15 difference
generators. Let R be their linear span in coefficient space and put
`V=R^perp` in R^126. Integration of a full-period derivative and
translation of the integration variable prove `K subset V`.
These statements also hold for U(f) when f and its first two
derivatives decay like `O(1/|s|)`, and for compact perturbations of
such f: the quartic boundary expressions tend to zero and the
integrands are integrable.

The 35 derivative generators are independent. Indeed `D R=0`
forces `R_y=R_Y=0` by the independent z,Z coefficients, and then
`R_x=R_X=0` by y,Y, so the homogeneous R is zero. The difference
map on the 15 monomials is also injective. Their two images share
the five independent vectors obtained by differentiating
`x^(4-k)y^k-X^(4-k)Y^k`, k=0,...,4. Thus `dim R<=45`.
The 45 by 45 minor certified in Section 4 has nonzero determinant
modulo 1000003, so `dim R>=45`. Consequently

    dim R=45,             dim V=81.                       (4)

### 3. Cutoffs give closure, without claiming bounded mass yet

If f is a real smooth compactly supported function, choose a period
so large that distinct copies of its support, enlarged by one unit
for the lag, are disjoint. Periodically repeat f to get g. On one
period all nonzero contributions to `J_g(s)^m` coincide with those
of J_f on R. Thus `U(f)=P T(g)` entrywise. If
`M=max(1,sup_s |J_g(s)|)`, then h=g/M is admissible and

    U(f)=P M^4 T(h) belongs to K.                          (5)

This equality treats every mixed lag monomial: the separation by
more than one unit prevents samples at s and s+1 from meeting
different copies. It also treats the two unmixed height blocks.

Choose a smooth compactly supported cutoff chi equal to 1 on [-1,1],
with support in [-2,2], and put `f_(b,A)(s)=chi(s/A) f_b(s)` for
A>=2. The product rule through order two, with factors A^(-1)
and A^(-2), gives the same `C/(1+|s|)` jet bound as above, uniformly
in A and b. The jets converge pointwise to J_(f_b), so

    U(f_(b,A)) -> U(f_b) in R^126.

The same argument applies to `f_b+epsilon psi`, for any fixed real
`psi in C_c^infinity(R)` and real epsilon. By (5), these vectors
lie in the closure of K. Continuity in b and ordinary finite
Riemann sums in (3) now show

    q belongs to closure(K) subset V.                    (6)

No uniform bound on the coefficients in (5) as A grows is asserted.
In fact this approximation alone does not prove the target. The
following interior argument is what permits a single finite mixture.

### 4. Exact first-variation rank

For smooth f and compactly supported psi, the first variation of
`U_c(f)=sum_m c_m U_m(f)` is

    d/depsilon U_c(f+epsilon psi)|_(epsilon=0)
       =integral_R E_c(f)(s) psi(s) ds,
    E_c(f)(s)=sum_(r=0)^1 sum_(j=0)^2
        (-D)^j [partial_(r,j) F_c(J_f(s-r))].             (7)

Each partial derivative is evaluated first, then differentiated
with respect to s. The second lag's entire pair is shifted by -1.
Formula (7) follows by a change of variable and j integrations by
parts; compact support of psi removes all boundary terms. All
expressions are smooth and locally integrable. The differentiated
polynomial is cubic in derivatives of f at offsets -1,0,1, with
derivative orders at most four.

For f=f_b its exact Taylor series is

    f_b^(j)(t)/(2b)
      =sum_(n>=ceil(j/2))
          (-1)^n t^(2n-j)/[(2n+1)(2n-j)!] (b^2)^n.       (8)

It is an entire power series, including its removable value at b=0.
For each monomial F and fixed s, take the coefficients of
`E_F(f_b)(s)/(8b^3)` in powers of b^2. These are rational linear
functionals on coefficient space when s is an integer. The exact
certificate uses s=0,1,2 and orders n<=48. It finds 81 independent
such coefficient rows. Their common annihilator is exactly R.

The complete deterministic certificate is
`scripts/periodic-tensor/pulse-rank-certificate.json`. Its generator
is `scripts/periodic-tensor/pulse_rank.py`. Monomials are all weak
compositions of 4 into 6 parts, in ascending recursive lexicographic
order; thus all 126 are present. For each coordinate occurrence the
generator removes that occurrence, shifts all three remaining lags
by minus its lag, differentiates the product j times, and multiplies
by `(-1)^j`. This is exactly (7), including multiplicities.

The finite arithmetic is performed modulo the prime p=1000003.
Trial division through floor(sqrt(p)) verifies primality. All
denominators in (8) through n=48 are products of positive integers
less than p and are invertible modulo p. Reduction therefore
preserves these rational coefficients, and a nonzero modular minor
proves the corresponding rational minor is nonzero. The two minors are

    relation minor: size 45, determinant mod p = 897600;
    pulse minor:    size 81, determinant mod p = 700255.   (9)

Selected pulse rows are n=0,...,30 at s=0; n=2,...,48 at s=1;
and n=3,4,5 at s=2. The selected columns, full matrices, elimination
pivots and all 50 integer relation rows are retained in the certificate.
Every universal relation's symbolic Euler expression is checked to
be identically zero over the integers, not merely zero modulo p.

An independently implemented replay is
`scripts/periodic-tensor/verify_pulse_rank.py`. It reconstructs (7)
by the multinomial product rule, and (8)'s triple products by direct
finite sums over n_1+n_2+n_3=n, using differentiated powers and
factorials rather than the generator's repeated differentiation and
convolution. It regenerates all 81*126=10206 selected entries, all
126 Euler columns and all 50 relation rows. It constructs inverses
of both square minors modulo p and checks every entry of both
matrix-inverse products against the identity. The complete inverses
and results are in `scripts/periodic-tensor/pulse-rank-verification.json`.
Both checks pass, with no failing entry. Reproduction commands are

    python3 scripts/periodic-tensor/pulse_rank.py
    python3 scripts/periodic-tensor/verify_pulse_rank.py

For the analytic implication, suppose `E_c(f_b)(s)=0` for all
0<b<1/2 and real s. At each of s=0,1,2 the expression is analytic
in b. The identity theorem makes every coefficient in (8)'s cubic
substitution zero, including the 81 certified independent rows.
They annihilate R, and by (4) their annihilator has dimension 45.
Therefore

    E_c(f_b) identically zero for all 0<b<1/2
          implies c belongs to R.                       (10)

This is a finite exact algebra check and an analytic identity
argument. No numerical rank threshold, fitting tolerance, sampled
inequality or finite dictionary feasibility assumption is used.

### 5. A supporting functional cannot vanish at q except as an identity

Let c be nonnegative on K, so `c dot k>=0` for every k in K,
and suppose `c dot q=0`. Continuity makes it nonnegative on
closure(K). In particular, by Section 3,

    U_c(f_b+epsilon psi)>=0

for every interior bandwidth b, every compact smooth real psi, and
every real epsilon. Formula (3) writes c dot q as the integral of
the continuous nonnegative function `U_c(f_b)`, times 3/pi^3.
Hence `U_c(f_b)=0` for every 0<b<1/2. For each such b, epsilon=0
is a minimum of the displayed differentiable polynomial in epsilon.
Its derivative vanishes. By (7),

    integral E_c(f_b)(s) psi(s) ds=0 for every psi in C_c^infinity(R).

The continuous function `E_c(f_b)` must be identically zero: a
strict sign at any point would persist on a neighborhood and give
a nonzero integral against a nonnegative bump supported there.
Equation (10) now proves

    c>=0 on K and c dot q=0 imply c in R.                 (11)

This conclusion holds over the entire path cone, not just a tested
finite family. Neither the arithmetic sampling law nor an assumed
stationary extension of its atoms has been used.

### 6. From relative interior to one finite mixture

Work in the 81-dimensional Euclidean space V and set C=closure(K).
Equation (11) first shows span(C)=V. Otherwise a nonzero vector
c in V annihilating span(C) would be nonnegative on K and vanish
at q, so belong to R as well as R^perp, a contradiction.
The closed convex cone C therefore has nonempty interior in V.

The finite-dimensional supporting-hyperplane theorem (Stephen Boyd and
Lieven Vandenberghe, *Convex Optimization*, 2004,
[Section 2.5.2, pp.50--51](https://www.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf#page=64))
now implies that q is an interior point of C. Indeed, if q were a boundary
point, there would be a nonzero c in V with
`c dot (v-q)>=0` for every v in C. Taking v=0 and v=2q gives
`c dot q=0`, hence c is nonnegative on C and contradicts (11).

Only the standard finite-dimensional theorem is used. To specify
its boundary case here, take exterior points x_n tending to q,
let y_n be their nearest points in the closed convex set C, and
normalize y_n-x_n. Existence of y_n follows by minimizing on a
sufficiently large compact ball; convexity gives
`(y_n-x_n) dot (v-y_n)>=0` for v in C by differentiating the squared
distance along the segment to v. Also y_n tends to q. A convergent
subsequence of unit normals supplies the stated nonzero supporting
vector. This short specialization makes the closed-set hypothesis
explicit; it asserts no separation theorem in an infinite path space.

It remains important that K itself need not be closed. R. Tyrrell
Rockafellar and Roger J-B Wets, *Variational Analysis*, third printing
2009, [Proposition 2.40, p.64](https://sites.math.washington.edu/~rtr/papers/rtr169-VarAnalysis-RockWets.pdf#page=72),
states rint(cl K)=rint K for a nonempty finite-dimensional convex
set. Here aff K=V, so it applies directly and gives q in K. The
following finite-simplex specialization records why this application
produces a finite mixture despite nonclosedness; it is not a new
convex attainment theorem. Choose an
orthonormal basis e_1,...,e_81 of V. For sufficiently small delta>0,
the 82 points

    v_0=q-delta sum_j e_j,       v_j=q+delta e_j (1<=j<=81)

belong to the interior of C, and q is their strict barycenter.
Approximate each v_j by a point k_j in K. If the approximations
are sufficiently close, the k_j remain affinely independent and
the unique barycentric coordinates of q remain strictly positive.
This follows directly from continuity of the inverse of the
invertible affine-coordinate matrix; the original coordinates are
all 1/82. Consequently q is a convex combination of these k_j.
Each k_j is, by the definition of K, a finite nonnegative sum of
actual unit-jet periodic occupation tensors. Expanding the finite
convex combination gives (1)'s exact representation.

This finite-simplex argument supplies the needed attainment from an
interior point. It does not infer attainment merely from (6), nor
assert a compact set of C2 paths or a uniform period for approximants.
Choose the resulting finite representation once. Its weight sum W
is finite and independent of ell. Since `|J_(h_i)|<=1` everywhere,
`C_2(h_i)<=1`, so the second cost is at most W. This proves every
assertion of (1), including phasewise support and uniformity.

The sine-integral transformation and rank-based strictness are the
new local calculation. Plancherel, elementary integration by parts,
finite-dimensional supporting hyperplanes and simplex continuity are
standard inputs/applications, not new theorems being claimed. The
existing cubature and first-velocity closure sources do not supply
the prescribed tensor's feasibility. The standard relative-interior
theorem above supplies attainment after the local strictness argument.

### 7. Separate conceptual audit, 31 October 2026

The invocation-start SPECIALIZE assessment was
`drafts/literature/2026-10-31-l585-periodic-carrier-audit-scope.md`.
This audit verifies the existing theorem from L473 (9); it neither
reproves the arithmetic input nor establishes a new moment theorem.
The full proof and both exact scripts were read. Both scripts were
then run in the order stated in Section 4, with complete regeneration
and comparison of the selected certificate, not a numerical preview.

**Density and Fourier normalization.** In L473 (9), a=1/2-u_1 and
b=1/2-u_2 give A=a+(b-a)u_3 and C=a+(b-a)u_4. Each orientation
has Jacobian 1/2 from (a,b) to (S,d), while the two linear interval
maps have Jacobian d^2. Their inverse cancels the original d^2;
the two orientations then cancel 1/2. The singular set d=0 is null
and has zero original weight. The three-coordinate change has
absolute determinant one. In particular k_3=-C and k_4=-D=C-S:
both reflected derivatives and both phases are retained.

For either pair, its absolute sum plus its absolute difference is
twice its largest absolute entry. Both pairs have absolute sum |S|.
Hence the allowed d length is exactly 1-2 max |k_l| on the stated
support, with no additional angular or hypersurface factor. This
argument works for an arbitrary occurrence list and therefore for
all 126 monomials, including repetitions and odd total derivative
orders; it introduces no multinomial coefficient or parity deletion.

Writing a_l(k)=1_{|k|<=b}(ik)^j_l exp(i r_l k), each a_l is in
L1 intersect L2 and each inverse transform is bounded and in L2.
Both convolutions a_1*a_2 and a_3*a_4 are bounded with compact
support, hence L2. Their inverse transforms are the physical pair
products by absolutely convergent spectral Fubini. Applying the
cited Plancherel theorem to these products gives the bilinear pairing
2pi integral (a_1*a_2)(k)(a_3*a_4)(-k) dk. Thus the layer factor 2
and inverse pairing factor 1/(2pi) change 3/pi^2 to 3/pi^3 in (3).
No L1 assumption on an individual sinc pulse is made or needed.
The zeroth entry is 3/pi^2 times integral_[0,1]^2 (u_1-u_2)^2
=1/(2pi^2), consistent with the density.

**Limits and support.** For j<=2 the explicit derivatives of
2 sin(bs)/s are uniformly O(1/|s|) away from zero, for b in
[0,1/2]; the spectral formula controls the bounded region. Translation
by one only changes the domination constant. The cutoff product
rule preserves this bound, and each quartic is dominated by an
integrable C(1+|s|)^(-4), uniformly in cutoff size and bandwidth.
This proves vector convergence, continuity at b=0 and both required
integral interchanges. For a fixed compact perturbation the same
argument holds with a constant depending on that perturbation.

If a compact pulse has support in [a,b], take P>b-a+1. The enlarged
intervals [a+nP-1,b+nP] are disjoint, so both coordinates of every
paired sample refer to the same copy, or to zero. Period integration
then equals the whole-line integral, including unmixed entries.
Dividing by M=max(1,sup |J_g|) gives phasewise Euclidean unit support
and the exact coefficient P M^4 in (5). This proves closure only;
no bound uniform in P or cutoff size is used later.

**Euler operator and exact rank.** A removed occurrence (r,j)
contributes psi^(j)(t+r). Setting s=t+r shifts *all three* remaining
lags by -r. Integration by parts gives (-1)^j D^j of their product.
This verifies both lag terms of (7), with multiplicities counted once
per occurrence. Every variation term has a compactly supported psi
factor before integration by parts, so differentiation of the integral
and the boundary removal are justified. Orders of f up to four occur;
the sinc pulses are smooth at all these orders.

The generator uses repeated product differentiation; the replay
instead allocates j derivatives among three factors with multinomial
coefficient j!/(d_1!d_2!d_3!). Both were checked against (7). The
replay reconstructs all 126 Euler columns and all 50 integer relation
rows. The 35 derivative relations are independent by the polynomial
argument in Section 2, the 15 shift differences are independent, and
their five stated overlaps are independent by the same derivative
injectivity. Thus the exact dimension is at most 45 before computing.

The replay verifies all 50 Euler identities over the integers. It
regenerates each of the 81*126=10206 selected Taylor entries, using
falling factorials divided by (2n+1)! instead of the generator's
convolutions and simplified factorials. The selected rows are exactly
s=0, n=0,...,30; s=1, n=2,...,48; s=2, n=3,4,5. Their counts are
31+47+3=81. The prime check tests every possible divisor through 1000;
1000^2<1000003<1001^2. All denominator prime factors are at most 97,
so rational reduction modulo this prime is valid.

Both scripts passed. Relation rank is 45 (required 45), pulse rank
is 81 (required 81); determinants are respectively 897600 and 700255
modulo 1000003. The replay forms each square minor from regenerated
entries, computes its inverse and checks every entry of its product
with that inverse. Full matrices and inverse certificates remain at
the Section 4 paths; failures are empty. Thus the evidence covers
the complete selected minors, not merely the displayed determinants.

The integer Euler identities imply exact annihilation of R by every
Taylor row. The two nonsingular minors imply dim R=45 and rank 81
over Q and hence over R. After division by 8b^3 the Euler expression
is an even entire function of b by (8); vanishing on 0<b<1/2 forces
all its Taylor coefficients to vanish. The selected rows therefore
force c in R, even for real, nonrational coefficient vectors. The
remaining sample rows need not supply additional independent rank.

**Strictness and attainment.** Nonnegativity of c on K passes to its
closure. Each U_c(f_b) is then nonnegative and continuous in b, and
(3) with c dot q=0 forces it to vanish for every interior bandwidth.
Every compact perturbation also belongs to closure(K), so epsilon=0
minimizes its quartic integral for each sign of epsilon. The first
variation is zero for every real test function, and continuity makes
E_c(f_b) identically zero. This uses nonnegativity of the integrated
functional; it does not assert pointwise nonnegativity of F_c.
The rank conclusion gives precisely (11).

Working in V is essential: a nonzero supporting normal there cannot
belong to R. Equation (11) first excludes a proper span for closure(K),
and then excludes a boundary point q by the supporting-plane theorem.
The cone tests v=0 and v=2q force the supporting value to be zero.
All these are finite-dimensional claims. Since aff K=V, the cited
Proposition 2.40 applies without any closedness premise on K and puts
q in K itself. The existing simplex paragraph also checks this exact
specialization: choose delta with all 82 vertices inside the interior
ball, approximate each from K, and preserve strictly positive
barycentric coordinates by continuity of an invertible finite matrix.

Membership in K means a finite sum of actual admissible periodic
tensors by its definition. Choosing this sum once gives a finite W
independent of ell, with second cost at most W because each paired
jet has norm at most one. Neither a limit of periods nor a bound on
the masses of the earlier cutoff approximants is used to infer W.

**Verdict and remaining scope.** The fixed-carrier theorem passes this
independent conceptual audit without mathematical repair. Precise
standard-source citations were added; no new input node or DAG edge
is needed. L473 (9) is the sole local mathematical input. No numerical
W, period, path or covariance-completion bound has been certified.
The identification of q with actual arithmetic moments still imports
Bui--Hall Proposition 3's unaudited proof. Second completion, positive
clipped mass, a selected stationary law and actual-Xi transfer remain
open. This verifies a local intermediate result, not a candidate RH
argument or a claim of progress beyond the literature checked.

## Mathlib

Coverage of this full paired-jet tensor and positive periodic-carrier
statement has not been checked. Relevant Fourier/Plancherel,
finite-dimensional convexity and modular linear algebra support has
not been inspected for a matching formalization. The two Python
certificates use exact integer/modular arithmetic and are reproducible;
they are not Lean proof terms. Section 7 audits the analytic assembly
and its linkage to the exact finite certificate; it makes no new
formalization claim. Unknown Mathlib coverage is not evidence of absence.
