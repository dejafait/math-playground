# Lemma 636: full-Gram margin for the independent two-height block

## Hypotheses

Use L622's actual zero-safe normalizations Z=-Xi/A and
W=(Xi'^2-Xi Xi'')/A^2, its fixed nonnegative w in C_c^infinity((0,1))
of integral 1, L=log T, T<=X<=2T, w_XT(t)=w((t-X)/T), and
N=floor(T^(1/100)). For arbitrary complex vectors b,d of length N set

    M_b(t)=sum_(n<=N)b_n n^(-it),
    F(t)=M_b(t)Z(t+1/L)+M_d(t)Z(t-1/L),
    I(b,d)=integral w_XT(t)W(t)|F(t)|^2 dt/(T L^6).

Vectors may depend on X,T but remain fixed during shift operations.
Use the full G_N and gamma_N of L623, the exact arithmetic convolution
of L624, the used-scope analytic bounds L628 (1)-(2), the complete-sum
removability argument of L629, and the local entries and finite-degree
row proof in L634 Sections 1-4. No output coordinate r>N is dropped.
The extension of that row proof beyond degree eight is justified below;
it is not assumed to have been audited already.

Named external imports retain their existing qualifications:

- C. P. Hughes and M. P. Young, *The twisted fourth moment of the
  Riemann zeta function*, J. reine angew. Math. 641 (2010), 203-236,
  [arXiv:0709.2345v2, Theorem 1.1/(11)-(17), printed pp. 3-5,
  including complete-sum holomorphy](https://arxiv.org/pdf/0709.2345v2#page=3),
  used through L622/L624, with both prime-power orientations.
- H. Hedenmalm, P. Lindqvist and K. Seip, *A Hilbert space of Dirichlet
  series and systems of dilated functions in L2(0,1)*, Duke Math. J.
  86 (1997), 1-37, [arXiv:math/9512211v1, Section 2.2/(2-7),
  Lemma 2.3, pp. 7-9](https://arxiv.org/pdf/math/9512211v1#page=7),
  used via the full finite-prime isometry in L628/L634.
- bramble_trace, *Signs and uniform filtered positivity in fourth
  moments of Hardy's function*, [paper 36, displayed v4, 21 October
  2026, Theorem 6/(21)-(24)](https://rstation.ai/problems/riemann_hypothesis/papers/36),
  for the untwisted kernel and compact Fourier representation only.
  Its translated-square result is not an import of the block claim.

The moment theorem and manuscript proofs are named imports, not newly
audited here. No RH, zero-free premise, simplicity, spacing, polynomial
approximation to actual Hardy values, or pointwise sign is assumed.

## Conclusion

Put a=13/6-4 cos(1), c=-4+3 cos(1)+(17/6)sin(1), and

    H0 = [a c; c a],
    R(b,d)=(6/pi^2)[a(b^*G_N b+d^*G_N d)+2c Re(b^*G_N d)].       (1)

This is precisely the p=1 translated-kernel/full-G_N reference.
Its two eigenvalues, in units 6/pi^2, obey

    lambda_e=a+c>1/100,  lambda_o=a-c>1/3000,
    R(b,d)>=gamma_N (||b||^2+||d||^2)/(500pi^2).                (2)

The complete leading arithmetic block has sufficient relative
limsup defect less than 7/16; the exact rational certificate gives
an upper bound approximately 0.436296420178. After charging the
regular zeta factors, exact phase and actual-Xi transfer, one
existential onset, independent of X,b,d, gives

    |I(b,d)-R(b,d)| <= R(b,d)/2,
    I(b,d)>=R(b,d)/2>0  if (b,d) != (0,0).                    (3)

This local result passes the independent conceptual audit in Section 6,
under the named imports and the used-scope local inputs. It extends the checked moment toolkit
to this precise detector, not a new arithmetic moment theorem or a
certified originality claim. It stops negative averaged witnesses in
this family beyond an ineffective onset. Pointwise initial signs,
effective overlap, other lengths/windows/displacements and all-degree
mixed positivity remain unresolved. This is not an RH candidate.

## Proof

### 1. Four exact allocations and actual-Xi transfer

Let s,t range independently over {+1,-1}. Use the complete H_hk and
Q=partial_1 partial_2-(partial_1^2+partial_2^2)/2 of L622, with its
exact Phi and all six terms. Define

    J_hk(s,t)=(Q H_hk)(0,0,s,t).

Write a_+=b,a_-=d and g=gcd(m,n). The exact Hermitian 2N by 2N
source matrix has entries

    K_((s,m),(t,n))=
      [J_(n/g,m/g)(t,s)+conjugate(J_(m/g,n/g)(s,t))]/2.        (4)

Thus v^*Kv is Re sum_(s,t,m,n) a_s,m conjugate(a_t,n)
J_(m/g,n/g)(s,t). Transposition in (4) is necessary with the
ordinary v^*Kv convention. Both mixed orientations occur.

The source hypotheses checked in L622 still hold: every reduced
hk<=N^2, the shifts are bounded complex multiples of 1/L, and
T0=T with support in [T,3T]. Its four nonnegative phase-weight
decomposition and holomorphic error argument are unchanged.
Applying Q on unit circles in its first two variables, with
the observer variables fixed at s,t, costs at most 3. If
V2=||b||^2+||d||^2, then

    sum_(s,t,m,n)|a_s,m a_t,n|(mn/g^2)^(7/8)
      <= N^(7/4)(||b||_1+||d||_1)^2 <=2N^(11/4)V2.

Consequently the summed, normalized differentiated source error is
at most C_w T^(-17/80)L^(-4)V2. All coefficients and gcd
multiplicities remain; no phase error has been summed entrywise.

For completion, L622's identity gives
W=Z'^2-ZZ''-(log A)''Z^2, with |(log A)''|<=C T^(-2).
Finite Cauchy-Schwarz gives

    |F|^2<=N V2 [Z(t+1/L)^2+Z(t-1/L)^2].

The untwisted h=k=1 case of the same complex shifted formula
gives integral w_XT Z(t)^2 Z(t+s/L)^2=O_w(TL^4), uniformly
for s=+1,-1. One can bound its complete main function on fixed
separated contours and extend to these collisions by holomorphy;
there is no derivative or amplifier in this bound. Therefore

    |I-v^*Kv|<=epsilon_T V2,
    epsilon_T=C_w[T^(-17/80)/L^4+T^(-199/100)/L^2].           (5)

This establishes the changed coefficient and curvature budgets,
rather than copying a common-observer or first-jet bound.

### 2. Bilinear leading reduction and the exact reference

Let V be the real divisor-triangular basis used in L634, with
V^*G_N V=I. Write b=Vy_+, d=Vy_-. Define T_nm(q) by

    B_N(q;Vx,Vy)=sum_(n,m) x_n conjugate(y_m) T_nm(q),
    B_N(q;f,g)=C_N(q) sum_(r in S_N)
                    A_(alpha,beta)(f;r) A_(gamma,delta)(conjugate(g);r).

L624 justifies the full convergent identity. Applying L628 (1)
separately to f and conjugate(g), and its bound on C_N(q)/C_N(0),
gives the bilinear version of (2): the operator norm of T(q) is
at most exp((120M+168)S), where M=log N, S=sum|q_j| and SM<=1/16.
This follows from Cauchy-Schwarz on the full output, not a presumed
Hermitian property at complex shifts. At zero T(0)=I.

For I={i<j} in {1,2,3,4}, J={k<l} its complement, set

    D_I(z)=product_(u in I,v in J)(z_u-z_v),
    ell_I(z)=(sum_I z-sum_J z)/2,
    q_I(z)=(z_i,z_j,-z_k,-z_l)/L,
    mathcal F_nm(z)=sum_(|I|=2) exp(ell_I(z))T_nm(q_I(z))/D_I(z).  (6)

Only the complete sum is evaluated at collisions. The pair-swap
symmetries give cancellation of each generic hyperplane residue;
the Vandermonde division argument of L629 gives holomorphy at
intersections as well. This applies also to each homogeneous
arithmetic degree and every bilinear matrix entry.

Use the separated radii

    (|z1|,|z2|,|z3|,|z4|)=(1/4,1/2,5/4,3/2).                 (7)

Here S=7/(2L), SM<=7/200<1/16. L628 bounds the arithmetic
operator uniformly. The Laurent expansion of each zeta pole,
the reciprocal factor at 2, and L622's analytic phase give, on
this torus, the exact source matrix minus (6/pi^2)mathcal F
of norm O_w(1/L). Indeed all differences stay at distance at
least 1/4 from zero, log(t/(2pi))/L=1+O(1/L), and the exact
phase error is O(1/(TL)). These estimates multiply a uniformly
bounded full arithmetic operator, not N independent entry errors.

Cauchy extraction of Q in coordinates one and two costs
1/(r1 r2)+1/r1^2+1/r2^2=28. Evaluation at each s,t=+/-1
in coordinates three and four costs at most
(r3/(r3-1))(r4/(r4-1))=15. Thus each observer block has cost
at most 420; the two by two block norm adds at most a factor 2.
This proves that the exact source form differs from the leading
form P obtained from (6) by O_w((||y_+||^2+||y_-||^2)/L).

For T(q)=I, the imported compact Fourier representation gives
the p=1 reference kernel

    K(x,y)=(1-|x-y|)^4-(x+y)^4,   |x|,|y|<=1/2,
    H0(s,t)=1/48 integral integral K(x,y)exp(i s x-i t y) dx dy. (8)

Here multiplication by 6/pi^2 restores the source normalization.
Uniform convergence of exponential series on this compact square
justifies (8) directly from the Fourier identity, or its polynomial
coefficients. This passage concerns the limiting main function only;
no infinite derivative filter is substituted for actual Hardy values.

Set u=x-y,v=x+y. The Jacobian is 1/2 and |u|+|v|<=1.
For s=t=1, integrating v first gives

    H0(1,1)=(1/30) integral_0^1 (1-u)^5 cos(u) du
            =13/6-4cos(1)=a.

For s=1,t=-1, integrating u first gives

    H0(1,-1)=(1/24) integral_0^1
                  [1/5-v^4+(4/5)v^5]cos(v) dv=c.

Repeated integration by parts evaluates these elementary integrals.
The negative diagonal also equals a. The even/odd basis therefore
diagonalizes H0 with lambda_e=a+c, lambda_o=a-c. The rational
alternating-series enclosures described in Section 5 prove (2).

### 3. Fixed-degree row extension and a justified infinite tail

Write t_nm,nu=[q^nu]T_nm(q), and v_n=n^(-1/2). For every fixed
integer k>=0, the argument of L634 Sections 1-4 proves

    sup_(n<=N) M^(-k) sum_(m<=N)(v_m/v_n)
                     sum_(|nu|=k)|t_nm,nu| <= A_k+o_k(1),
    A_k=[u^k]A(u),  A(u)=exp(2u+4(exp(u)-1)).                (9)

The original application needed k<=8. Here is the justification
for each larger fixed degree, with no uniform-in-k remainder claim.
In L634 notation, u_d(h)=(d+1)e^(dh)-2d e^((d-1)h)
+(d-1)e^((d-2)h) has nonnegative coefficients and its degree-k
coefficient is O_k((d+1)^(k-1)). This is the second difference
of (d+1)d^k divided by k!, valid for every fixed k. The local
normalization kappa has degree-k nonconstant norm O_k(x), x=1/p.
Its geometric denominator has coefficients bounded by sums of
j^k x^(2j). For bulk off-diagonal entries, the remainder after
U_d has at least two positive-degree factors: it is zero at k=1
and O_k(x(d+1)^(k-2)) for k>=2. In the boundary formulas, the
additional O(x) factors and polynomial-geometric sums give
O_k(x(d+1)^(k-1)). Non-vacuum diagonal coefficients are O_k(x);
the vacuum diagonal is exactly 1. These are all cases in L634
(8)-(13); their proofs use arbitrary fixed k and not k<=8.

Incoming sums, at most two incoming boundary entries, and outgoing
x^d weights consequently give the full row majorant (14)-(16)
of L634 through any prescribed finite degree K, with constants C_k.
Tensoring retains every m in S_N before restriction to m<=N.
The incoming majorant is exp(2z log n). The outgoing logarithm
has coefficient at most 4M^k/k!+O_k(1), by
sum_(p<=N)log p/p<=2M and the convergent p^(-2) sums.
The remaining coefficient is bounded by

    C_k M^(-k)[sum_(p|n)(log p)^k(e_p+1)^(k-1)/p
                              +sum_(p<=N)(log p)^k/p^2]=o_k(1).

Uniformity follows from (e_p+1)log p<=2M and
sum_(p|n)log p/p<=sum_(p<=R)log p/p+M/R: first let M grow,
then R grow. This works for every fixed k. Finite-degree
exponentiation proves (9), with the same A_k, through any finite K.

The matrix with entries sum_(|nu|=k)|t_nm,nu| is real symmetric:
pair exchange transposes T and permutes these multi-indices.
The weighted Schur inequality therefore converts (9) to an
operator bound for each homogeneous part T_k on (7):

    limsup ||T_k(q_I(z))|| <= A_k (3/200)^k.                 (10)

It is uniform in z,I. This step also bounds non-Hermitian complex
evaluations, by entrywise domination by that symmetric matrix.

To justify summing infinitely many k, dilate z by a complex zeta
with |zeta|=3/2. Then SM<=21/400<1/16 and the bilinear L628
bound gives ||T(q_I(zeta z))||<=exp(7) for large L, uniformly.
Cauchy's formula in zeta bounds its homogeneous tail beyond K
by 3 exp(7)(2/3)^(K+1). Hence, for fixed K, use (10) on
degrees 9,...,K; then let K tend to infinity. This proves

    limsup sup_(z on (7),I) ||T(q_I(z))-sum_(k=0)^8 T_k(q_I(z))||
       <= delta:=sum_(k>=9) A_k (3/200)^k.                 (11)

Thus no uniformity in k of o_k(1), or unjustified interchange of
the growing arithmetic matrix with an infinite expansion, is used.

On (7), |D_I|^(-1)<=256 and |exp ell_I|<=exp(7/4)<6.
The six terms in (6), the cost 420, and the two observer blocks
give tail operator cost at most 2*420*6*256*6*delta.
Dividing by lambda_o>1/3000 bounds its relative contribution by

    C_tail=2*420*6*256*6*3000*delta.                         (12)

Every higher arithmetic degree is charged in this estimate.

### 4. Complete low-degree contraction at the finite displacements

For a>=b>=0 define m_ab(u,v)=u^a v^b+u^b v^a if a>b,
and m_aa(u,v)=u^a v^a. For nu=(a,b,c,d), a>=b,c>=d,
put o_nu=(1 if a=b else 2)(1 if c=d else 2). Define

    E_nu(z)=sum_(I={i<j},J={k<l})
       exp(ell_I(z))(-1)^(c+d)m_ab(z_i,z_j)m_cd(z_k,z_l)/D_I(z),
    w_nu(s,t)=Q_b E_nu(i b)|_(b=(0,0,s,t)).                (13)

This is exact evaluation, including all six permutations and all
orders of the exponential. It is not a Taylor approximation in s,t.
The homogeneous arithmetic coefficient is t_nm,nu/L^|nu|.
Pair symmetry means that distributing w_nu equally across its
o_nu indices leaves the functional unchanged.

Permutation symmetry of E_nu and conjugation of its real coefficients
show that its observer matrix is

    W_nu=[a_nu+i b_nu, c_nu; c_nu, a_nu-i b_nu],

with a_nu,b_nu,c_nu real. In the even/odd observer basis this is
[a_nu+c_nu, i b_nu; i b_nu, a_nu-c_nu]. Therefore

    ||H0^(-1/2) W_nu H0^(-1/2)||/o_nu
      <= ( max(|a_nu+c_nu|/lambda_e, |a_nu-c_nu|/lambda_o)
                                     +|b_nu|/sqrt(lambda_e lambda_o) )/o_nu. (14)

The displayed basis change is unitary; the imaginary off-diagonal
matrix has norm |b_nu|. Pair exchange of nu conjugates W_nu and
transposes the arithmetic coefficient, so the complete block is
Hermitian. Alternatively symmetrizing its total cannot increase
the norm bound. The positive absolute majorant obtained after
(14) has symmetric (n,m) entries; the weighted Schur argument
works also with the two-dimensional observer blocks.

For k=1,...,8 the rational upper bounds for (14), simultaneously
for all orbits of degree k, are

    k:    1       2        3         4          5
    B_k: 6053/1000 33241/1000 11723/100 118897/250 949507/1000
    k:    6           7            8
    B_k: 1422689/500 3711713/1000 5256449/1000.             (15)

Degree zero is exactly the reference, not estimated using these
rounded conditioning bounds. Combining (9), (14)-(15), and
M/L<=1/100 gives relative low-degree limsup defect at most

    C_low=sum_(k=1)^8 B_k A_k/100^k.                       (16)

This contraction includes both even/odd channels and their
imaginary coupling for arbitrary independent complex vectors.
No endpoint-observer inference or factor-two lift of L635 is used.

### 5. Exact certificate, total reserve and limitations

Run from this notebook:

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/full_gram/two_height_block.py

The full evidence is `scripts/full_gram/two_height_block_certificate.json`.
It records every weight in (13) as rational coefficients of
1, cos(1), sin(1), all 175 orbits/495 multi-indices, conditioning
intervals, degree bounds, A_k through 24, costs and failures.

For clarity, the exact coefficient algorithm is as follows. For
the diagonal set b=(u,-u,1+v,1-v); for the cross set
b=(u,-u,1,-1). Multiply (13) by Delta(b). Each subset numerator
is its pair monomials times epsilon_I(b_i-b_j)(b_k-b_l), times
i^|nu| exp(i ell_I(b)). Its constant exponential is exp(i e),
e in {-1,0,1}. Only u-degree<=3 and v-degree<=1 are needed.
The diagonal numerator and denominator both have factor uv;
the cross pair has factor u. Cancellation is checked in every
retained coefficient. After division, Q_b=-partial_u^2/2
extracts minus the u^2 coefficient at v=0. The regular denominator
has nonzero constant; multiplication back checks all coefficients
through u^2. Thus the truncated polynomial arithmetic computes
the required derivative exactly, without truncating exp(i e).

Twenty terms of the alternating sin(1), cos(1) series and their
next terms give rational enclosures. They prove lambda_e>1/100,
lambda_o>1/3000 and sqrt(lambda_e lambda_o)>1/550. Substitution
in (14) and rounding upward to multiples of 1/1000 prove (15).
The script also checks the two reference expressions by equality
with Section 2's direct kernel evaluations and all pair-exchange
symmetries. These checks are finite algebra, not an independent
conceptual audit of the analytic argument.

For a rational upper bound on (11), put u=3/200 and use

    delta <= sum_(k=9)^24 A_k u^k+19683 u^25.                (17)

Indeed A has nonnegative coefficients, A(1)=exp(2+4(e-1))
<exp(9)<3^9=19683. The elementary bound e<11/4 also gives
exp(7/4)<6, since (11/4)^7<6^4. The recurrence
k A_k=sum_(j=1)^k j e_j A_(k-j), with e_1=6 and
e_j=4/j! for j>=2, computes all coefficients exactly.

The certificate proves by rational comparisons

    C_low = 0.435840755630...,
    C_tail <= 0.000455664548481...,
    C_low+C_tail < 7/16 < 9/20.                            (18)

Decimals here only preview the stored rational values. The strict
comparison with 7/16 and every finite check pass with no failures.
Equations (11)-(18) imply an eventual leading defect <=(9/20)R,
uniformly in all coefficients and X. This chooses one onset after
taking the uniform limsup, not an onset for each vector.

The O_w((||y_+||^2+||y_-||^2)/L) error in Section 2 is o(R)
by lambda_o>1/3000. From L623,

    gamma_N>=T^(-1/20)/[4(1+L/100)^2],
    epsilon_T/gamma_N <=4 C_w(1+L/100)^2
                  [T^(-13/80)/L^4+T^(-97/50)/L^2] ->0.

By (2), the relative actual-Xi cost in (5) is at most
500pi^2 epsilon_T/gamma_N. Choose a further common onset so
this cost and the Section 2 relative error together are <=1/20.
The total is then 9/20+1/20=1/2, proving (3). This reserve is
spent once; the source error, regular-factor/phase error and
curvature are distinct and all included. Zero vectors give equality
trivially; otherwise the reference is strictly positive.

The former first-jet stops are retained as narrower statements.
The present finite-displacement comparison has its own coefficients,
conditioning and controlled infinite remainder. It supplies no
effective height, localizer at individual heights, or all-degree
mixed sign. The independent review below retains these limitations.

### 6. Independent conceptual audit, 1 November 2026

**Scope and decision.** Equations (1)-(3) pass this audit under the
specified moment/isometry/kernel imports. The audit checks Sections
1-5, including the all-fixed-degree extension and its infinite tail;
it does not audit the external manuscripts or certify an effective
onset. No stronger inequality or new moment theorem is claimed. The
new evidence independently confirms that this precise negative-average
detector is stopped. The original derivation and certificate are retained.

**Allocations, normalizations and analytic reduction.** Expand the
actual square, with integration variable x, as sum
a_(s,m) conjugate(a_(t,n)) times (m/n)^(-ix) Z(x+s/L)Z(x+t/L),
where s,t are the two observer displacements. After gcd
reduction, L624's common-multiple sum has r/m=(n/g)d and
r/n=(m/g)d. Thus h=m/g increments the second divisor function,
exactly as in L622's source convention. The ordinary conjugate-first
quadratic-form convention gives the transpose in (4); taking its
Hermitian part includes both mixed orientations and preserves the
real actual integral. No relation between b and d is imposed.

The phase-weight decomposition in L622 applies on the same fixed
complex neighborhood. The observer coordinates are fixed in {+1,-1}
while Q acts in the first two coordinates, so its unit-circle cost
is exactly 3. The coefficient sum is at most 2N^(11/4)V2. Its
normalized exponent is 3/4+1/100+11/400-1=-17/80. For curvature,
Cauchy-Schwarz applied to the full 2N-term vector gives the stated
N V2(Z_+^2+Z_-^2). The two unamplified integrals of Z^2 Z_+^2
and Z^2 Z_-^2 are O_w(TL^4) by the complete untwisted shifted
formula and its holomorphy, including collisions. Multiplying by
T^(-2)/(TL^6) leaves N/(T^2 L^2), as in (5). Neither estimate
divides by a Hardy value or loses a zero or multiplicity.

L623's full convolution identity and L634's real triangular
orthonormal basis give V^*G_N V=I. L624 retains every output
coordinate. Apply L628 (1) to each of two independent convolution
vectors, and its analytic C_N ratio bound to their bilinear pairing.
This proves the operator bound exp((120M+168)S) also for complex
q; it does not assert Hermitian symmetry at complex shifts. Exchanging
the two shift pairs transposes T, and the zero-shift matrix is I.

The two-variable pair symmetries cancel generic collision residues
of (6) for each matrix entry and each homogeneous arithmetic degree.
Multiplication by Delta and successive division by its distinct
linear factors extends this cancellation across all intersections,
as in L629. On (7), each difference has modulus at least 1/4,
S=7/(2L), and SM<=7/200. The source is compared with
(6/pi^2) mathcal F(i b), retaining the change z=i b before Q
is applied. The regular zeta factors and the exact phase therefore
cost O_w(1/L) in the full arithmetic operator norm. The Cauchy
cost is 28 times 15 per observer block; four blocks cost at most
twice their maximum operator norm. This verifies the complete
O_w((||y_+||^2+||y_-||^2)/L) reduction without an extra factor N.

**All fixed degrees and the order of limits.** L634's full local
formulas (8)-(10) are valid for arbitrary fixed Taylor degree. In
the bulk off-diagonal remainder, (kappa-1)U_d and every j>=1
product U_j U_(d+j) have two positive-degree factors. Their
degree-k bound is C_k x(d+1)^(k-2), zero for k=1. Boundary
remainders have bound C_k x(d+1)^(k-1); only two incoming
entries can be boundary entries. The vacuum diagonal is exactly
one; every other diagonal remainder is O_k(x). The reverse
orientation exchanges the shift pairs and preserves coefficient
norms. Geometric summation of all outgoing x^d weights, including
the infinite output, is uniform for x<=1/2 at each fixed k.
These observations verify the extension of every local row case.

For each k>=1, uniformly over n<=N, the remaining incoming
error after division by M^k is at most

    C_k 2^(k-1)(A_R/M+1/R)+O_k(M^(-k)),
    A_R=sum_(p<=R) log p/p,                R>=2 fixed.

The outgoing logarithm has degree-k coefficient at most
4M^k/k!+O_k(1), and the incoming main factor is exp(2z log n).
First M tends to infinity, then R does. Exponentiation in any
fixed finite coefficient cone gives (9) with precisely A_k.
No constants uniform over all k are required. Pair exchange
makes the matrix of absolute coefficient sums symmetric, so its
weighted row bound controls the operator norm. On (7), each
|q_j|<=3/(2L) and M/L<=1/100, proving (10), uniformly in
the torus point and subset I. This domination applies to the
non-Hermitian complex evaluations too.

For clarity, the exact two-limit inequality is, for any fixed K>=8,

    limsup_(L->infinity) sup_(z,I)
      ||T(q_I(z))-sum_(k=0)^8 T_k(q_I(z))||
      <= sum_(k=9)^K A_k(3/200)^k
                               +3 exp(7)(2/3)^(K+1).

Indeed on |zeta|=3/2 the radial arithmetic family has
SM<=21/400<1/16 and norm at most exp(6.3+882/L)<=exp(7)
for L>=1260. Operator-valued Cauchy integration in each finite
dimension gives the same tail bound independently of that dimension.
The finitely many degrees 9 through K use (10); only then is K
sent to infinity. The displayed bound proves (11), rather than
inferring a uniform infinite expansion from fixed-degree convergence.
Its six denominators, exponential bound, Cauchy costs, two observer
channels and division by lambda_o are precisely (12). Since A has
nonnegative coefficients, its remainder after degree 24 at u<1 is
bounded by u^25 A(1)<19683u^25. This verifies the analytic use of
the rational tail certificate.

**Independent confluent calculation.** The audit program
`scripts/full_gram/two_height_block_audit.py` imports no notebook
calculation module and does not use the original two-variable
quotient implementation. It reconstructs every weight by a
four-column alternant with confluent Hermite rows. Here are the
identities specifying the independent calculation in full.

Write wedge_(r,s)(x,y)=x^r y^s-x^s y^r. Then
(x-y)m_ab equals wedge_(a+1,b)-wedge_(a,b+1) when a>b,
and wedge_(a+1,a) when a=b. For a selected wedge from each
pair, with powers (r,s,u,v), define the row

    R(x)=(exp(i x)x^r, exp(i x)x^s, x^u, x^v),
    R_j=R^(j)(0)/j!,   P=R(1), P'=R'(1), M_-=R(-1).

Laplace expansion by the first two columns expresses its contribution
to E_nu(i b) as

    (-1)^(c+d) i^|nu| exp(-i sum b/2)
                   det(R(b1),R(b2),R(b3),R(b4))/Delta(b),

times the two wedge signs. This follows term by term from
Delta/D_I; there is no omitted multi-index factorial since
t_nm,nu is already a Taylor coefficient, not a derivative.

At b=(h,-h,1,-1), Delta(b)/h=4(1-2h^2+h^4).
The numerator coefficients of h and h^3 are respectively
-2 det(R_0,R_1,P,M_-) and
-2 det(R_0,R_3,P,M_-)+2 det(R_1,R_2,P,M_-).
Since Q=-partial_h^2/2, this wedge's cross weight, before its
displayed phase and signs, is

    [det(R_0,R_3,P,M_-)-det(R_1,R_2,P,M_-)
                              +2 det(R_0,R_1,P,M_-)]/2.

For the diagonal, take b=(h,-h,1+j,1-j) and then j->0.
The denominator after division by hj has the same constant
and h^2 coefficients, 4 and -8. The last two rows contribute
the factor -2j and become P,P'. The diagonal weight is therefore

    -[det(R_0,R_3,P,P')-det(R_1,R_2,P,P')
                                      +2 det(R_0,R_1,P,P')],

with the additional phase exp(-i) already specified above. Only
R_0 through R_3 are needed; these are exact derivatives, and
the exponentials at +/-1 are never truncated. This independently
checks the confluence, signs and retained derivative orders.

The complete replay covers all 175 pair orbits and 495 indices
through degree eight. It agrees with every stored rational
coefficient of 1, cos(1), sin(1), every orbit size, every interval
bound and every degree maximum. It also checks both pair-exchange
orientations and the full reference eigenvalue enclosures. The
alternating trigonometric series give rigorous intervals; powers
of the truncated exponential independently reproduce A_0 through
A_24, without using the original recurrence. Every stored budget
entry agrees. The full evidence, including all reconstructed rows,
is `scripts/full_gram/two_height_block_audit_certificate.json`.
Reproduce it by

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/full_gram/two_height_block_audit.py

The exact total is

    40237217407267503448018848506847600391559478591695144416410665251
    /92224495884750028800000000000000000000000000000000000000000000000
    < 7/16.

No failures were recorded. The independent reconstruction is finite
algebra evidence; the preceding analytic argument is essential.

**Block norm and one common onset.** In the even/odd observer basis,
each W_nu has diagonal entries a_nu+c_nu, a_nu-c_nu and
imaginary off-diagonal entries i b_nu. Conditioning by H0 gives
exactly the right side of (14), divided by its orbit size. Within
each orbit the Taylor coefficients agree. Thus their o_nu copies
in the absolute coefficient row compensate this division exactly.
Pair exchange makes that scalar row majorant symmetric; weighted
Schur bounds then apply to the 2-by-2 operator blocks. There is
no extra factor two in the low-degree bound: it already uses each
whole observer-block norm. The high-degree estimate separately
uses twice the maximum block norm, as explicitly charged in (12).
Taking the Hermitian part or transposing the complete matrix to
the conjugate-first convention cannot enlarge these norm bounds.

The direct compact-kernel integrals in (8) reproduce a and c, with
the stated Jacobian 1/2 and source factor 6/pi^2. Their eigenvalues
exceed 1/100 and 1/3000. Hence R>=gamma_N V2/(500pi^2).
The arithmetic limsup bound is uniform in all coefficients and X;
its strict gap below 9/20 yields a single eventual leading bound.
The regular-factor/phase term divided by R is O_w(1/L).
The source and curvature ratios have exponents respectively
-17/80+1/20=-13/80 and -199/100+1/20=-97/50, after the
explicit gamma_N lower bound. They tend to zero with the stated
logarithmic factors. Enlarge that one onset so their sum with the
regular-factor/phase ratio is at most 1/20. The final reserve is
9/20+1/20=1/2, spent once. Nonzero vectors have R>0 and zero
vectors give equality. This completes the audit of (3).

## Mathlib

Matching Mathlib coverage for the full arithmetic two-height block,
the row-extension/tail limit and the actual-Xi comparison has not
been checked and remains unknown. The cited sources support the
specified moment and isometry inputs; none is asserted to contain
the new complete block margin. The exact rational certificate is
not a Lean proof, an audit of those imports or a numerical RH test.
