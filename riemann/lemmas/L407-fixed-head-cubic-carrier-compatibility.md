# Lemma 407: fixed-head cubic zero/single-carrier compatibility

## Hypotheses

Use the actual functions, phase and ordinary height jets of L369, L390,
L391 and L405 on t>=40. In particular,

    c=1/(4pi), L=log(2+t), (x,y,z)=(f,f'/L,f''/L^2),
    R=exp(i phi), E=R^2, b=z-x/4,
    M=(z^2+3xz/2+x^2/16-y^2)/2, K=(b-iy)^2/2.

Fix a positive integer N independently of H, and define

    Z_N=sum_(n<=N) n^(-5/2-it), a_N=Re(RZ_N), h_N=Im(RZ_N),
    d_N=c^2[M|Z_N|^2+Re(K E Z_N^2)],
    B0_N=-c(b a_N+y h_N).

H tends to infinity through real values. No RH, phase independence,
zero, signed cubic asymptotic, growing-head, full-tail or clipping
assumption is made. Constants with subscript N may depend on N.

## Conclusion

The sharp integral I_N(H)=integral_[H,2H] d_N B0_N dt admits the exact
finite carrier decomposition (3) below. Its complete contour reduction
is the explicit finite arithmetic expression (9), with total error

    O_N(H^(71/120))=o(H(log H)^2).                         (1)

Each term has either zero or one exact gamma carrier and three zeta
factors, each differentiated at most twice. All rational resonances
and both sharp connectors are retained. In particular,

    I_N(H)=O_N(H(log H)^2).                               (2)

This is local REPRODUCTION using the assessed reflection, modified-Gonek
and subconvex tools. Neither (2) nor the unevaluated signed expression
determines a main scale, coefficient or sign. The separate step-111
critical audit below validates this fixed-N reduction. No infinite-head
passage, physical signed mean,
clipped statistic, total pencil margin, common-zero upper bound,
actual-theta positivity or RH consequence follows.

## Proof

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-13-fixed-head-cubic-carrier-coverage.md`,
whose COVERED_TARGET is this compatibility test. It reuses step 103's
cubic source exclusions and L391's audited tools; the narrowly checked
L369/L390/L405 and step-103/106/107 records contain no completed cubic
reduction. No novelty is inferred. L394/L399/L400 are historical contrasts,
not premises. L406 supplies downstream physical transfer only and is not
an input to the finite-head proof.

### Complete algebra and ordinary jets

On the original real line, x,y,z,M are real. Write V=RZ_N, so that
b a_N+y h_N=Re((b-iy)V). Expand d_N B0_N and pair each positive
harmonic with its negative conjugate. The exact result is

    d_N B0_N=-c^3 Re{
        [M(b+iy)+(b+iy)^2(b-iy)/4] R^(-1) conjugate(Z_N)^2 Z_N
                      +(b+iy)^3 R^(-3) conjugate(Z_N)^3/4 }.

This pairing retains all four harmonics R^(+/-1), R^(+/-3); it does
not average an independent phase. For example it follows immediately
by multiplying

    d_N/c^2=M Z_N conjugate(Z_N)
             +[(b-iy)^2 R^2 Z_N^2
                          +(b+iy)^2 R^(-2) conjugate(Z_N)^2]/4,
    B0_N/c=-[(b-iy)RZ_N+(b+iy)R^(-1)conjugate(Z_N)]/2.

At complex height tau set s=1/2+i tau, h_j(s)=zeta^(j)(s), and
L(tau)=Log(2+tau). L391 (3), obtained by differentiating f=-R h_0
before dividing, gives exactly

    D0=h_0,
    D1=i(h_1+Omega h_0)/L,
    D2=(-h_2-2Omega h_1-Omega^2 h_0+iOmega' h_0)/L^2,
    (x,y,z)=-R(D0,D1,D2), R'/R=iOmega,
    Omega=[Psi(1/4+i tau/2)+Psi(1/4-i tau/2)-2log pi]/4.

Primes on Omega are tau derivatives; h_j are complex s derivatives.
The i factors, Omega' term and order of normalization are exact. Put

    J_plus=D2-D0/4+iD1, J_minus=D2-D0/4-iD1,
    M_D=(D2^2+3D0D2/2+D0^2/16-D1^2)/2,
    P1=M_D J_plus+J_plus^2 J_minus/4,
    P0=J_plus^3/4.

The preceding identity becomes, on the real line,

    d_N B0_N=c^3 Re{ E P1(D) conjugate(Z_N)^2 Z_N
                                +P0(D) conjugate(Z_N)^3 }. (3)

Indeed each cubic critical polynomial contributes -R^3, canceling
the outside minus sign and reducing R^(-1), R^(-3) to E,1. One may
also use the exact factorization

    P1=J_plus(3D2^2/4+5D0D2/8+3D0^2/64-D1^2/4).

No reflection of an asymptotic formula or division by a zeta value is
involved; (3) holds at zeros. For its holomorphic extension replace
conjugate(Z_N) by Z_N^-(tau)=sum_(n<=N)n^(-5/2+i tau), rather than
conjugating an off-line value. The other head is Z_N^+(tau).

### Analytic coefficients and cited inputs

Let nu=(nu0,nu1,nu2) range over nonnegative triples with sum nu_j=3,
and set d(nu)=nu1+2nu2. Define the unique coefficients w_(e,nu)(tau)
by expanding the displayed ordinary D formulas in the formal variables
h_0,h_1,h_2:

    P_e(D)=sum_nu w_(e,nu)(tau) F_nu(s),
    F_nu(s)=h_0(s)^nu0 h_1(s)^nu1 h_2(s)^nu2, e=0,1. (4)

This specifies every coefficient; no terms are omitted. Each w is a
finite sum of constant multiples of Omega^b (Omega')^k/L^m with
m=d(nu)+b+2k. On the closed rectangle H<=Re tau<=2H,
-11/20<=Im tau<=0, the separately controlled polygamma estimates
in L391 give Omega=O(ell), Omega'=O(1/H), Omega''=O(1/H^2),
where ell=log H. Differentiating these exact monomials, using
L'=1/(2+tau), proves

    |w_(e,nu)|<=C ell^(-d(nu)),
    |w_(e,nu)'|<=C ell^(-d(nu))/H.                    (5)

Possible terms with k>0 are smaller; the proof never differentiates an
unspecified O term. L391 also supplies holomorphy of R, Omega, L and
the ordinary jets on a neighborhood of this rectangle. Gamma and zeta
poles have height zero and no singularity is crossed.

Import A. Sourmelidis, J. Steuding and A. I. Suriajaya,
*Dirichlet Series with Periodic Coefficients and their Value-Distribution
Near the Critical Line*, [arXiv:2007.14008v2, Section 3 immediately after
(35), both branches before (36)](https://arxiv.org/html/2007.14008v2#S3).
For fixed integer q>=1, a=1+epsilon, epsilon>0, and an absolutely
convergent series F(s)=sum A(n)n^(-s) on Re s>1 with
A(n)<<_eta n^eta for every eta>0, the primitive divided by 2pi i of
(q/(2pi))^s Gamma(s) exp(-pi i s/2) F(s), from a+i to a+iV,
is sum_(n<=Vq/(2pi)) A(n) exp(-2pi i n/q)+O(V^(1/2+epsilon)).
The plus-exponential branch is O(1). Periodicity is not a hypothesis
of this primitive statement; it is used in its subsequent application.
This is the unchanged fixed-parameter theorem assessed for L391 and
the present target. We do not reprove it or differentiate its error.

The exact functional-equation kernel is

    E=chi(1-s)=(2pi)^(-s) Gamma(s)
                              [exp(-pi i s/2)+exp(pi i s/2)]. (6)

This follows from gamma reflection/duplication as in L391 (4).
[DLMF 25.4.1](https://dlmf.nist.gov/25.4.E1) and
[25.4.5–6](https://dlmf.nist.gov/25.4.E5) supply exact reflection
and its derivatives (s!=0,1); our rectangle avoids both exceptions.
Here the already audited ordinary identities suffice, so no derivative
reflection theorem is reproved or real-shift asymptotic differentiated.

For connectors import J. Bourgain, *Decoupling, exponential sums and
the Riemann zeta function*, JAMS 30 (2017), 205–224,
[arXiv:1408.5794v2, Theorem 5/(0.5), p. 2](https://arxiv.org/pdf/1408.5794v2#page=2).
Its unconditional 13/84+epsilon exponent gives the convenient 1/6
bound with epsilon=1/168. The fixed-strip Phragmen–Lindelof and Cauchy
specialization already proved in L391 (10)–(11) gives, for j<=2,

    |h_j(sigma+it)|<=C_j ell^j
                   H^((5/18)(11/10-sigma)),
    1/2<=sigma<=21/20, H<=t<=2H.                    (7)

Its disks of radius 1/ell, functional equation just left of 1/2 and
pole-free height qualification are unchanged. These are supporting
known tools, not a cubic moment theorem.

### Both sharp connectors

Let delta=11/20 and a=21/20. Expand each of the finite response heads
in (3). A tuple (m,n,k) contributes alpha=(mnk)^(-5/2) times the
fixed rational twist r^(i tau), with

    r_1=mn/k for (Z_N^-)^2 Z_N^+,
    r_0=mnk  for (Z_N^-)^3.

For each coefficient in (4) move the height contour from [H,2H] to
[H-i delta,2H-i delta]. The exact oriented connector correction is
the integral down from H to H-i delta minus the integral down from
2H to 2H-i delta. Cauchy's theorem applies to the holomorphic
integrand, including w and the finite rational twist. On these two
connectors, (5) and (7) cancel every ell^d derivative factor. Since
|r^(s-1/2)| is bounded for each fixed r, and sector-qualified Stirling
gives |E|<=C H^(sigma-1/2), the single-carrier exponent is

    sigma-1/2+(5/6)(11/10-sigma).

It increases with sigma and equals 71/120 at sigma=21/20.
The zero-carrier exponent (5/6)(11/10-sigma) is at most 1/2.
Each connector has fixed length delta; thus both are respectively
O_(r,nu)(H^(71/120)) and O_(r,nu)(H^(1/2)). The complete E in (6),
not an isolated exponentially growing factor, is used for this bound.
The finite sum over response tuples and critical monomials is O_N
(H^(71/120)). Closed sharp endpoints require no smoothing limit.

### Right-line primitives, resonances and arithmetic expression

On Re s>1, the standard locally uniformly convergent derivative series
([DLMF 25.2.1](https://dlmf.nist.gov/25.2.E1)) gives
F_nu(s)=sum C_nu(j)j^(-s). If (p1,p2,p3) has nu_l entries equal
to l, then exactly

    C_nu(j)=(-1)^d sum_(j1 j2 j3=j)
                               product_(l=1)^3(log jl)^pl. (8)

A zero exponent means 1, including at jl=1. The choice of ordering
does not affect the coefficient. Thus |C_nu(j)|<=d_3(j)(log j)^d
for j>=2, with the evident j=1 value. Fixed divisor bounds imply the
subpolynomial coefficient hypothesis of the cited primitive theorem;
absolute local convergence holds on every compact subset of Re s>1.

For a fixed reduced rational r=u/v, encode the twist by integer support:
r^s F_nu(s)=u^s sum_j C_nu(j)(v j)^(-s). Its series has coefficient
C_nu(j) at vj and zero elsewhere, so the theorem applies with q=u,
epsilon=1/20. Converting ds/(2pi i) to dt/(2pi), and retaining
r^(-1/2), yields a primitive on [H,V] with main term
2pi r^(-1/2) sum_(H<t_j<=V) C_nu(j) exp(-2pi i vj/u),
where t_j=2pi vj/u, and error O_(r,nu)(H^(11/20)), uniformly for
H<=V<=2H. Both gamma branches in (6) are included; the plus branch
has O(1) primitive and is contained in this error.

Partial summation against w(t-i delta), with (5), gives the same main
sum with w evaluated at t_j-i delta, and weighted error
O_(r,nu)(H^(11/20)ell^(-d)). This follows from the uniform primitive
error times |w(2H-i delta)|+integral |w'|. It retains both endpoint
terms and does not differentiate the theorem's O term. The convention
H<t_j<=2H is exactly the difference of the two cutoff primitives.

For zero carrier, absolute right-line expansion instead gives the
frequency log(r/j). Isolate j=r if r is a positive integer. Its value
is r^(-1/2) C_nu(r), independent of the chosen right line. The
remaining unweighted primitive is bounded uniformly in H,V by

    2r^(a-1/2) sum_(j!=r) |C_nu(j)|j^(-a)/|log(r/j)|<infinity.

There are finitely many j near the fixed r, with nonzero denominators;
the rest converge absolutely by (8). Partial summation gives error
O_(r,nu)(ell^(-d)) and retains the exact resonant weight integral.
This proves the zero-carrier source case directly under the present
rational-twist hypotheses, rather than keeping only j=1.

Define, using r=u/v in lowest terms,

    S_(r,nu,w)=2pi r^(-1/2)
       sum_(H<2pi vj/u<=2H) C_nu(j) exp(-2pi i vj/u)
                                      w(2pi vj/u-i delta),
    T_(r,nu,w)=r^(-1/2) C_nu(r) integral_[H,2H] w(t-i delta)dt
                    if r is a positive integer, and 0 otherwise.

The complete arithmetic reduction is

    I_N(H)=c^3 Re sum_(m,n,k<=N) (mnk)^(-5/2)
        sum_nu [S_(mn/k,nu,w_(1,nu))
                           +T_(mnk,nu,w_(0,nu))]
                              +O_N(H^(71/120)).             (9)

The sums here are finite, signed and unevaluated. Every zero-carrier
twist arising in (3) is in fact an integer; the general resonance rule
also explains why none can be discarded. The gamma main sum's actual
additive phases, analytic weights and sharp cutoffs are retained.
Combining its H^(11/20) remainder, the zero-carrier remainder and
both connectors proves (1): the error divided by H ell^2 is
O_N(H^(-49/120)ell^(-2)), tending to zero.

Finally, sum_(j<=X)d_3(j)<=X(1+log X)^2 by counting the third divisor
variable and summing the first two reciprocals. Thus the gamma sum
before weighting is O_(r,nu)(H ell^(d+2)); (5) makes each S
O_(r,nu)(H ell^2). Each T is O_(r,nu)(H ell^(-d)). Summing over the
fixed finite heads proves (2). This is an absolute bound for the
retained signed expression, not a computed signed leading coefficient.

### Verification and limits

`python3 scripts/discriminant/check_fixed_head_cubic.py` checks, in exact
Q[i] Laurent-polynomial arithmetic, the full conjugate pairing, jet
carrier substitution, P1 factorization, the surviving R powers 0,2,
and critical degree three. The full certificate is
`scripts/discriminant/fixed-head-cubic-certificate.json`; the complete
three residual arrays, both coefficient polynomials and all checks were
inspected. All residuals vanish. The analytic bounds are proved above;
the certificate records them only as references, not numerical proof.

The achieved local reduction makes a separately assessed signed
arithmetic evaluation possible to formulate. It does not supply that
evaluation, an infinite-response limit at log^2 H scale or clipping.
L406's physical error is separately o(H ell^2), but using it for the
complete family still requires the missing signed full-tail work.
Regulator choice, the total L367 margin/remainder, actual common-zero
upper counts and global mixed positivity remain independent gaps.

### Separate critical audit — 2026-10-14, step 111

This REPRODUCTION audit uses the prior SPECIALIZE assessment
`drafts/literature/2026-10-14-fixed-head-cubic-critical-audit.md`.
Its inspected primary statements and proof-case coverage are reused:
Sourmelidis–Steuding–Suriajaya v2 Section 3 after (35), both gamma
branches; DLMF 25.2.1 and 25.4.1/25.4.5–6; and Bourgain v2
Theorem 5/(0.5), with the fixed-strip application audited in L391.
Their precise links and hypotheses occur above. No unproved shifted
cubic moment theorem, growing twist or higher gamma power is imported.
The audit establishes the correctness of the local application, not a
new source theorem or signed leading coefficient.

**Actual inputs and complete pairing.** L369 (5) gives f=-R h_0
with f real, without division by h_0; this is also L390 (6).
L390's d and L405 (4)'s B0 have exactly the signs used here.
Their finite-head replacements are definitions, not applications of
an infinite-head limit. Write A_-=b-iy and A_+=b+iy and V=RZ_N.
Then d_N/c^2=M V conjugate(V)+(A_-^2 V^2+
A_+^2 conjugate(V)^2)/4, and B0_N/c=-(A_- V+
A_+ conjugate(V))/2. The coefficient of
V conjugate(V)^2 in their product is
-(M A_+/2+A_+^2 A_-/8), and the coefficient of
conjugate(V)^3 is -A_+^3/8. The other two terms are exactly
their conjugates. Taking the real part therefore gives the two
coefficients printed before (3), including the factor 1/4.
This checks all four original harmonics, rather than selected terms.

Differentiate f=-R h_0, using d h_j/d tau=i h_(j+1)
and R'/R=i Omega. It gives f'=-R i(h_1+Omega h_0)
and f''=-R[-h_2-2Omega h_1-Omega^2 h_0+iOmega' h_0].
Only then divide by L and L^2. Thus every ordinary jet, including
the sign of iOmega', is retained. Substituting into each homogeneous
cubic contributes -R^3, canceling the preceding minus sign and
leaving exactly R^2 and 1. This proves (3) even at zeta zeros.
The continuation of conjugate(Z_N) is the separately defined Z_N^-,
so no antiholomorphic function is used in the contour argument.

The exact verifier was independently read and rerun. Its multiplication
reduces i^2=-1 in Q[i]; its conjugation fixes the real jets, negates
the R exponent and interchanges Z and Zbar. Carrier substitution
retains the total cubic degree. The full /tests, /paired_residual,
/substitution_residual, /factorization_residual, /P1, /P0 and
/carrier_R_powers values of the saved certificate were inspected,
using `python3 ../scripts/loop/inspect_json.py` with each selected
pointer and `--full`. All five checks pass; all three residual
arrays are empty; both ten-term coefficient polynomials agree with
the displayed definitions; the only R powers are [0,2]. This
verifies the finite algebra only. The script's analytic-bound fields
are references and are not used as evidence for analytic estimates.

**Every analytic coefficient.** In a term of D_j, record the tuple
(p,b,k,m) for h_p Omega^b (Omega')^k L^(-m). The possibilities are

    D0: (0,0,0,0);
    D1: (1,0,0,1), (0,1,0,1);
    D2: (2,0,0,2), (1,1,0,2), (0,2,0,2), (0,0,1,2).

All satisfy m=p+b+2k. Every term in P0 or P1 is a product
of three such entries. Hence (4) includes every term, d<=6, and
the identity m=d+b+2k is valid term by term. L391's separate
polygamma bounds on a neighborhood of the rectangle give
|Omega|<=C ell, |Omega'|<=C/H, |Omega''|<=C/H^2.
Also |L| is comparable to ell and |L'|<=C/H.
Differentiate the finite monomials directly: the three possible
derivatives hit Omega, Omega' or L^(-m). Each is bounded by
C ell^(-d)/H, and the original monomial by C ell^(-d).
No division by Omega or Omega' is needed, so their zeros cause no
exception. This proves (5) and total variation O(ell^(-d)) on
the shifted edge. The finite rational twist r^(i tau) is entire.
Gamma/polygamma poles and zeta's pole have Re tau=0; L has no
cut or zero here, and the nonvanishing E admits its actual branch
of square root R on this simply connected rectangle. No singularity
is crossed.

**Source hypotheses and normalization.** Absolute local convergence
of the three derivative series permits their Cauchy product.
For (8), all ordered triples are retained even when two orders agree;
no multinomial factor is added for repeated factors. Their logarithms
give the sign (-1)^d and the bound d_3(j)(log j)^d. The j=1
coefficient is one if d=0 and zero otherwise. Fixed divisor bounds,
with a smaller exponent absorbing logarithms, give O_eta(j^eta)
for every eta>0. Thus the cited primitive's coefficient hypothesis
is met, including for the series supported at vj. Both u and v
are fixed before H grows.

On the lower height edge s=a+it with a=21/20. The identity
r^(i tau)=r^(s-1/2) retains the constant r^(-1/2).
Inserting the exact E from (6), the support encoding is

    r^(s-1/2) E F_nu(s)
      =r^(-1/2) (u/(2pi))^s Gamma(s)
        [exp(-pi i s/2)+exp(pi i s/2)]
                            sum_j C_nu(j)(vj)^(-s).

Consequently the negative branch has cutoff t_j=2pi vj/u and
phase exp(-2pi i vj/u); ds=i dt gives the factor 2pi, not
1/(2pi), in S. The positive branch is included with its O(1)
primitive. Subtract the primitive at H from that at V: the error
is uniformly O_(r,nu)(H^(11/20)) for H<=V<=2H.
The right-continuous cutoff convention gives H<t_j<=V. At an
endpoint equal to a cutoff any alternative half-weight convention
differs by at most O_eta(H^eta), already inside this error.

More explicitly, let B(V) be this exact unweighted integral and
A(V) its finite step-function main sum, both based at H. Then
sup|B-A|<=C H^(11/20). Stieltjes integration by parts against
w(t-i delta) gives an error bounded by

    C H^(11/20) (|w(2H-i delta)|
                          + integral_H^(2H) |w'(t-i delta)| dt)
       <= C H^(11/20) ell^(-d).

The step-function integral is precisely the sum of w(t_j-i delta)
times its jumps. This accounts for both endpoints and explains why
the actual analytic weights are evaluated on the shifted edge.
No frozen weight, differentiated source error or omitted gamma
branch enters (9).

For zero carrier the expanded term is
r^(a-1/2) C_nu(j) j^(-a) exp(it log(r/j)). The frequency
vanishes exactly when j=r is a positive integer, with amplitude
r^(-1/2) C_nu(r). Every r0=mnk has this possibility, including
r0=1 and the possible zero coefficient when d>0. For all other
indices the primitive is bounded by 2/|log(r/j)|. Near a fixed
r only finitely many nonzero denominators occur; for sufficiently
large j the denominator is at least one and the remaining absolute
series converges on a>1. This proves the stated uniform O_(r,nu)(1)
primitive bound. The same partial summation then leaves precisely T
with O_(r,nu)(ell^(-d)) error. Resonances are retained before
taking the real part; none is dismissed through phase averaging.

**Sharp connectors and total error.** The orientation can be checked
by traversing H to 2H, down at 2H, back along the lower edge,
then up at H. Its zero contour integral says that the upper
integral equals the lower integral plus the downward integral at H
minus the downward integral at 2H, as claimed. Both are bounded.

Bourgain's exponent 13/84+1/168=9/56<1/6 permits the weaker
critical-line bound used in L391. Its pole-removed strip interpolation
gives B(sigma)=(5/18)(11/10-sigma); its Cauchy disks, including
slightly extended endpoint heights and the functional-equation strip
just left of 1/2, give |h_j|<=C ell^j H^B for j<=2.
Thus three factors cost H^(3B), after (5) cancels ell^d.
The exact carrier contributes at most H^(sigma-1/2), while each
fixed rational twist is bounded on this strip. The exponent is

    sigma-1/2+3B(sigma)=sigma/6+5/12,

whose maximum on [1/2,21/20] is 71/120. For zero carrier
3B(sigma) has maximum 1/2. Each connector has length 11/20.
The complete finite sum therefore costs O_N(H^(71/120)), with
neither a logarithmic loss nor an omitted sharp endpoint.
The source error H^(11/20) and zero-carrier bounded primitive
are smaller. Dividing the total error by H ell^2 gives
O_N(H^(-49/120)ell^(-2)) tending to zero.

Finally the elementary count sum_(j<=X)d_3(j)<=X(1+log X)^2
and (8) bound each gamma main sum by O_(r,nu)(H ell^(d+2));
(5) yields O_(r,nu)(H ell^2). The finitely many resonant terms
are O_(r,nu)(H ell^(-d)). This checks (2), without asserting any
nonzero coefficient or sign at that scale. The audit validates
(1)–(9) unchanged, with no new direct mathematical dependency.
It supplies an audited finite-head input only: no bound uniform in N,
signed full-tail limit, clipping control or RH consequence is proved.

## Mathlib

Full matching coverage of this fixed-head carrier reduction, the modified
Gonek theorem and cubic jet contour application has not been checked.
Polynomial algebra, Cauchy estimates and absolute series integration are
supporting tools only; no library absence, Lean verification, originality
beyond the sources checked or RH resolution is claimed.
