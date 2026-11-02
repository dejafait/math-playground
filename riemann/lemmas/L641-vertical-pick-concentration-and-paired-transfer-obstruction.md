# Lemma 641: vertical Pick concentration and an exterior paired-transfer obstruction

## Hypotheses

Use the actual completion and zero correspondence of L018 and exactly
the definitions of C, K, ell_X, T, N and s_j in L640. Thus
T>=e^5, N=floor(log T), X in [T,2T], s_j=2+i(X+j/N), 0<=j<N.
Only L640's definitions and its elementary Gram identification are
needed here; the latter is checked below. Its arithmetic reduction and
its separate outstanding audit are not premises for this result.

Put a=3/2, c=X+1/2, u_j=j/N-1/2 and

    Q_N(z)=product_(j<N)(z-u_j+ia),
    B_N(z)=product_(j<N)(z-u_j-ia)/(z-u_j+ia),
    H_N={P/Q_N: P is a complex polynomial, deg P<N},
    ||h||^2=(1/(2pi)) integral_R |h(x)|^2 dx,
    I=[-1,1].

All zeros below are zeros of the actual Xi, counted with multiplicity.
The source inputs are:

* Masatoshi Suzuki, *Aspects of the screw function corresponding to the
  Riemann zeta-function*, JLMS 108 (2023), 1448--1487,
  [arXiv:2206.03682v4](https://arxiv.org/pdf/2206.03682v4), Section 2.2,
  printed p.7, equation (2.6) and its proof: the locally absolutely
  convergent compensated logarithmic-derivative expansion, with b=0.
* Bellotti--Wong, [arXiv:2412.15470v2](https://arxiv.org/pdf/2412.15470v2),
  7 July 2025, Theorem 1.1, with the all-zero, multiplicity and endpoint
  conventions audited in L467. Write its counting main term as
  V(H)=H log(H/(2pi e))/(2pi) and error as
  E(H)=0.10076 log H+0.24460 log log H+8.08344, H>=e.
* The finite rational model-space identification and kernel in
  Baranov--Zarouf, [arXiv:1310.1182v1](https://arxiv.org/pdf/1310.1182v1),
  Section 1.1, and the half-plane normalization in
  Baranov--Jaming--Kellay--Speckbacher,
  [arXiv:2304.02385v2](https://arxiv.org/pdf/2304.02385v2), Section 3.1,
  (3.1)--(3.3), (3.7).

The elementary finite formulas below verify the norm and moving distinct
poles in this specialization. They are not claimed as new model-space
theorems. No nested-array spectral limit, RH, simplicity, critical-line
nonvanishing, positive zero measure or zero-free-region input is used.

## Conclusion

For a coefficient column v define

    g_v(z)=sum_(j<N) conjugate(v_j)/(a+i(X+j/N-z)),
    h_v(z)=g_v(c+z).

Then h_v ranges over H_N, and

    v* C v=||h_v||^2,
    v* K v=sum_zeta g_v(zeta) conjugate(g_v(conjugate(zeta))).   (1)

The sum is over all Xi zeros, including both signs of the real part,
and is absolutely convergent for each fixed finite family and v.
An off-real conjugate pair contributes twice a real part, not a modulus
square. If ||h_v||=1 and x=C^(1/2)v, then ||x||=1 and the normalized
K-Rayleigh quotient is exactly the sum in (1) divided by ell_X.

There is, for every sufficiently large T, a choice X_T in [T,2T]
and a subspace U_T of H_N of complex dimension at least

    kappa N-O(sqrt(N) log N),
    kappa=(arctan(1/3)+pi/4-1)/pi>0,                           (2)

such that every h in U_T satisfies

    (1/(2pi)) integral_(R\I) |h|^2 <= N^(-1/2)||h||^2,
    h(zeta-c)=0 whenever |Re(zeta)-c|<=1.                     (3)

Thus all local zero contributions vanish identically on U_T. This is
a genuine dimension surplus using **all** local zeros, not only real
ones. It does not bound the remaining sum in (1).

There is also the following obstruction to a proposed boundary-only
estimate for that remaining sum. For each sufficiently large N there
are unit h_N^+, h_N^- in the same H_N for which, with m=floor(sqrt(N)),

    (1/(2pi)) integral_(R\I) |h_N^+|^2,
    (1/(2pi)) integral_(R\I) |h_N^-|^2
                 <= C sqrt(m) (9/10)^m,                      (4)

but at the fixed exterior conjugate pair w=2-i/4, conjugate(w)=2+i/4,

    2 Re[h_N^+(w) conjugate(h_N^+(conjugate(w)))] >= A_N,
    2 Re[h_N^-(w) conjugate(h_N^-(conjugate(w)))] <= -A_N,
    A_N=(2/3)(36/149)^m(149/125)^((N-m)/2),
    log(A_N)/N -> (1/2)log(149/125)>0.                        (5)

C is absolute. In original coordinates this pair is c+2 +/- i/4,
strictly inside the permitted Xi zero strip and outside the local
window. It is a test pair, **not an asserted pair of actual Xi zeros**.
The vectors in (4)--(5) are not asserted to satisfy (3)'s actual-zero
interpolation conditions. Their boundary leakage tends to zero faster
than any inverse power of N, yet their paired energy divided by ell_X
has unbounded magnitude when N=floor(log T).

Consequently no universal estimate of exterior paired evaluations by a
polynomial in N times exterior boundary leakage, even with an added
o(N)||h||^2 allowance, follows from boundary concentration and this pole
geometry alone. This rules out that generic transfer step, not the
constraint-sensitive remainder on U_T. No actual-Xi Rayleigh witness,
fixed norm reserve, negative eigenvalue or RH conclusion is established.
This result is locally proved but separately unaudited.

## Proof

### The exact zero-pair identity and norm

Let F=xi'/xi. Suzuki's compensated expansion, after changing from its
xi(1/2-iz) variable to s, gives for any nonzero evaluation points s,r

    F(s)-F(r)=sum_rho [1/(s-rho)-1/(r-rho)],

where rho runs over xi zeros with multiplicity. Here and below
"nonzero evaluation points" means points where xi does not vanish.
This subtracts each compensated summand before summing; it never
separates the compensators into a possibly divergent series. Its local
absolute convergence justifies the subtraction. L018 gives
F(1-s)=-F(s), F(conjugate(s))=conjugate(F(s)) and nonvanishing at the
points of real parts 2 and -1 that will be used. Set s=s_j and
r=1-conjugate(s_k), and divide by s-r. The result is

    K_jk=sum_rho 1/[(s_j-rho)(conjugate(s_k)-(1-rho))].         (6)

If zeta=(rho-1/2)/i, then the reflected zero 1-conjugate(rho)
corresponds to conjugate(zeta). Thus the second factor in (6) is
the conjugate of s_k-(1-conjugate(rho)). Multiplication by
conjugate(v_j)v_k and finite summation gives (1) with the stated sign
and conjugations. In particular both terms of a nonreal pair are
retained, and their sum is twice the real part in (5).

For completeness the source's absolute convergence also agrees with
the explicit count input: outside any fixed ordinate interval the
summands of (6) are O(|Im rho|^(-2)). L467's unit-shell estimate, its
conjugate negative-height counterpart from L018, and compact finiteness
give a summable majorant. The same argument applies to g_v's paired
products. Constants may depend on N,X,v here; no dimension-uniform
tail estimate is being inferred from convergence.

Direct integration, or the residue at X+k/N+ia, gives

    (1/(2pi)) integral_R
       1/[(a+i(X+j/N-u))(a-i(X+k/N-u))] du
       =1/(2a+i(j-k)/N)=C_jk.

This proves the norm identity. Partial fractions at the distinct lower
poles show that h_v ranges over all P/Q_N with deg P<N, since
1/(a+i(u_j-z))=i/(z-u_j+ia). These functions are linearly independent;
a zero norm forces the rational function, and then every residue, to
vanish. Hence C is strictly positive definite. This also checks the
full Gram, its square-root normalization and the Rayleigh assertion
without using L640's subsequent arithmetic estimates.

### Finite concentration in the exact moving grid

Use the quoted finite model-space identity with the norm divided by
2pi. To verify its constants explicitly, an orthonormal basis of H_N is

    e_j(z)=sqrt(2a)/(z-u_j+ia)
                   product_(k<j)(z-u_k-ia)/(z-u_k+ia).

On the real line the product has modulus one, so each squared norm is
one. For j>k the integrand e_j(x) conjugate(e_k(x)) has only lower
half-plane poles after cancellation, decays as x^(-2), and its upper
contour integral is zero. Each e_j is in H_N; N orthonormal elements
therefore form a basis. Telescoping the one-factor identity gives

    k_N(z,w)=sum_j e_j(z)conjugate(e_j(w))
            =i[1-B_N(z)conjugate(B_N(w))]/(z-conjugate(w)).

On the boundary its diagonal is

    k_N(x,x)=sum_j 2a/((x-u_j)^2+a^2),
    |k_N(x,y)|<=min(2N/a, 2/|x-y|).                          (7)

Indeed the phase derivative of B_N is the displayed positive diagonal,
at most 2N/a, and |1-exp(i theta)|<=min(2,|theta|).
This proves (7), including its diagonal limit. These calculations are
the required normalization and distinct-pole specialization of the
standard source identities, not an appeal to a nested-sequence theorem.

Let P_N be the orthogonal projection onto H_N in L2(dx/(2pi)), and
let A=P_N 1_I P_N restricted to H_N. It is a positive contraction. Its
trace is the integral of (7)'s diagonal over I. The function

    u -> arctan((1-u)/a)+arctan((1+u)/a)

is even and decreasing for 0<=u<=1/2: differentiating shows the
negative term has the smaller positive denominator. Its minimum on
the grid's containing interval [-1/2,1/2] occurs at an endpoint.
Consequently

    tr A >= q_0 N,
    q_0=(arctan(1/3)+pi/4)/pi.                               (8)

The projection identity and finite basis expansion also give exactly

    tr(A-A^2)= integral_I integral_(R\I)
                         |k_N(x,y)|^2 dx dy/(2pi)^2.          (9)

Here all integrands are nonnegative. Set b=2N/a and eta=2/b=a/N.
For either endpoint of I, write v in [0,2] for the inside distance
and w>=0 for the outside distance. By (7), the corresponding double
integral before its (2pi)^(-2) factor is at most

    integral_0^2 integral_0^infinity min(b^2,4/(v+w)^2) dw dv
       =6+4 log(2/eta).

For 0<=v<eta the inner integral is 4b-b^2 v; for v>=eta it is
4/v. Integrating these two cases proves the equality. Both endpoints
are charged, and eta<=2, so

    tr(A-A^2)<=V_N,
    V_N=[3+2 log(2N/a)]/pi^2=O(log N).                       (10)

Let E_N be the span of A-eigenvectors with eigenvalue at least
1-N^(-1/2), and let d_N=dim E_N. If an eigenvalue lambda is below
that threshold, lambda<=sqrt(N) lambda(1-lambda). The contribution
of the other eigenvalues to tr A is at most d_N. Thus

    d_N>=q_0 N-sqrt(N)V_N.                                  (11)

Every h in E_N has boundary leakage at most N^(-1/2)||h||^2.
All statements so far hold for every N and this exact grid; no rate
has been extracted from an inapplicable spectral-limit theorem.

### Average over X, retaining every local zero

Let M_T(X) count Xi zeros with |Re(zeta)-(X+1/2)|<=1,
with multiplicity. The window is [X-1/2,X+3/2]. For sufficiently
large T it is wholly at positive ordinate in the xi variable. Every
zero participates for a set of X of length at most 2; hence

    integral_T^(2T) M_T(X) dX
       <=2 #{rho: T-1/2<=Im rho<=2T+3/2}.                    (12)

To cover a possible lower-endpoint zero, the source's continuous count
envelopes are passed to the left limit as in L467. The count on the
right of (12) is therefore at most

    V(2T+3/2)-V(T-1/2)+E(2T+3/2)+E(T-1/2)
       = (T/(2pi))log T+O(T).

This uses V'(H)=log(H/(2pi))/(2pi); the errors E are O(log T).
Consequently some X_T in [T,2T] satisfies

    M_T(X_T)<= (1/pi)log T+O(1)=N/pi+O(1).                  (13)

One may choose a non-endpoint of the finitely many counting intervals;
alternatively their endpoints have measure zero. Existence follows
directly from the integral average, without a zero-spacing assumption.

Impose on E_N every linear evaluation h(zeta-c)=0 in this window.
There are at most M_T(X_T) constraints when counted with multiplicity.
Repeated copies of a zero require only the same evaluation, so this
upper bound on codimension is conservative and requires no simplicity.
Equations (11)--(13) give (2). Positivity of kappa can be checked
without decimals: arctan(1/3)>1/3-1/81=26/81 and pi/4>3/4,
whose sum exceeds one. Both conjugates of a local nonreal zero are
in the same window. Thus (1)'s entire local contribution vanishes
on the resulting U_T, and (3) follows.

This establishes only the rank and boundary parts of the test. The
unbounded complement in (1) is still present.

### Boundary concentration does not bound an exterior paired evaluation

This final test uses the same distinct poles and gives a fully explicit
obstruction to discarding the strip-evaluation issue. Set m=floor(sqrt(N))
and assume N is large enough that 2m<=N. Let J_1={0,...,m-1} and
J_2={N-m,...,N-1}. Define

    Q_r(z)=product_(j in J_r)(z-u_j+ia),
    h_r(z)=d_r/Q_r(z),   d_r>0 chosen so ||h_r||=1,
    B(z)=product_(j<N-m)(z-u_j-ia)/(z-u_j+ia).

The poles in each J_r lie within delta=m/N of one of its endpoint
centers b_r in [-1/2,1/2]. Here delta<=m^(-1/2). On
|x-b_r|<=m^(-1/2), every denominator has squared modulus at most
a^2+4/m. Consequently, with C_0=pi exp(4/a^2),

    d_r^(-2)>=exp(-4/a^2)/(pi sqrt(m) a^(2m)),
    d_r^2<=C_0 sqrt(m) a^(2m).                              (14)

In the other direction, keep one denominator and bound the remaining
m-1 squared denominators below by a^2. Integration gives

    d_r^(-2)<=a^(-2m+2)/(2a),
    d_r>=sqrt(2/a) a^m.                                     (15)

For x outside I every |x-u_j| is at least 1/2. Keep one denominator
for integration and bound the others below by a^2+1/4. From (14),

    integral_(R\I) |h_r|^2 dx/(2pi)
       <=[C_0(a^2+1/4)/(2a)] sqrt(m)
                              [a^2/(a^2+1/4)]^m
       =(5C_0/6) sqrt(m)(9/10)^m.                           (16)

The rational-space decomposition verified by the basis above is
H_N=K_B orthogonal-sum B K_(B_N/B), with the same boundary norm.
Here h_1 belongs to K_B (its poles form a subset of those of B),
and h_2 belongs to K_(B_N/B). Thus for every real theta,

    f_theta=(h_1+exp(i theta) B h_2)/sqrt(2)

belongs to H_N and has norm exactly one. On the real line |B|=1;
|p+q|^2/2<=|p|^2+|q|^2 and (16) prove (4) with C=5C_0/3,
uniformly in theta.

Now put w=2-i/4 and w'=conjugate(w). For u_j in [-1/2,1/2],
1.5<=2-u_j<=2.5, so

    |B(w)|^2
       =product_(j<N-m) [((2-u_j)^2+(7/4)^2)
                           /((2-u_j)^2+(5/4)^2)]
       >=(149/125)^(N-m),
    B(w)conjugate(B(w'))=1.                                 (17)

At either w or w' all denominator moduli in Q_r are at most
D=sqrt(149)/4 and at least 5/4>1. Equations (14)--(15) give

    |h_r(w)|, |h_r(w')| >=sqrt(2/a)(a/D)^m,
    |h_r(w)|, |h_r(w')| <=sqrt(C_0) m^(1/4) a^m.             (18)

Write

    A=h_1(w)conjugate(h_1(w'))+h_2(w)conjugate(h_2(w')),
    C_1=B(w)h_2(w)conjugate(h_1(w')),
    D_1=conjugate(B(w'))h_1(w)conjugate(h_2(w')).

Direct expansion, including the normalization 1/sqrt(2), yields

    2 Re[f_theta(w)conjugate(f_theta(w'))]
       =Re[A+exp(i theta) C_1+exp(-i theta) D_1].             (19)

The two phase extrema on the right are Re A +/- |C_1+conjugate(D_1)|.
By (17)--(18),

    |C_1| >= (4/3)(36/149)^m(149/125)^((N-m)/2),
    |A|+|D_1| <=3 C_0 sqrt(m) a^(2m).                       (20)

The first lower bound has logarithm
(N/2)log(149/125)-O(sqrt(N)); the second upper bound has logarithm
O(sqrt(N)). For all sufficiently large N the latter is less than
half the former. Choosing the two phase extrema in (19) proves (5).
This also proves the claimed growth rate, and (16) proves decay of
the boundary leakage faster than every inverse power of N. No
floating spectrum, sampled asymptotic or numerical certificate is used.

The cancellation B(w)conjugate(B(w'))=1 was retained: the obstruction
comes from the cross terms in (19), not from incorrectly multiplying
independent lower-half-plane evaluation bounds. Both signs are obtained
for a full conjugate-pair functional. Nonetheless these vectors need
not lie in U_T, and (17) specifies no actual zero. The surviving
question is whether actual local interpolation constraints and signed
cancellation in the entire exterior sum suppress this obstruction.
Boundary concentration alone supplies no such implication.

## Mathlib

Full matching coverage is not checked; unknown coverage is not absence.
The standard finite Hardy/model-space identities are cited above and
their normalization is verified here. Finite Hermitian spectral theory,
residue integration, elementary arctangent estimates and dimension/rank
arguments are supporting mathematics, not a claimed formalization of
the assembled statement. [Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/).
