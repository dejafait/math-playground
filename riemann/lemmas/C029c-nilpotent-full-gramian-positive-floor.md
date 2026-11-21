# Corollary C029c: a positive full-cost floor for the nilpotent Gramian

## Hypotheses

Let d>=3 be an integer, n=d-1, T=d^2, and let S be the real d by d
unit subdiagonal shift: S e_j=e_(j+1) for 1<=j<d, S e_d=0.
Use the realification and normalization of C029b, with C replaced by S:

    M=[0 -S; S 0],
    W=integral_0^T exp(t*M^T)*exp(t*M) dt,
    G=T^(-1) times the upper-left d by d block of W,
    J=(G^(1/2)*S*G^(-1/2)-G^(-1/2)*S^T*G^(1/2))/(2i),
    k_d(S)=||J||_1.

Positive matrix square roots are the positive Hermitian ones, and
||.||_1 is the Schatten trace norm on complex matrices. The integral
uses the identity observation on all 2d realified coordinates before
the specified principal block is taken. No observation coordinate,
coefficient or singular value is removed. This is the nilpotent model,
not C029b's actual centered companion.

## Conclusion

G is positive definite, and, with q_d=(d+1)/(2*sqrt(2)*d),

    k_d(S) >= (1-q_d^2)*sqrt(1-d^(-2))/2
           >= 7*sqrt(2)/27 > 1/3                  (d>=3),
    liminf_(d->infinity) k_d(S) >= 7/16.                       (1)

Thus the approved o(1) alternative fails for this exact model and
horizon. The spectrum of S consists only of zero, with algebraic
multiplicity d. Real spectrum alone therefore does not guarantee
vanishing of this prescribed full trace-norm cost. S is not
diagonalizable for d>=2; no conclusion about uniformly controlled
diagonalizations is asserted.

This is a local model estimate, not an actual-companion floor or a
lower bound for the imaginary root height. That height is zero for
the model. C028b's actual H_d=o(d), actual full k_d=o(1), and RH remain
open. Independent conceptual audit1953 verified the proof below under
exactly these hypotheses; no substantive mathematical correction was
needed. This verifies the local model estimate, not an RH argument.
The bounded literature assessment did not supply (1); this does not
certify originality beyond the sources checked.

## Proof

### Imported inputs and the precise specialization

The finite realification formula in C029b applies to every real finite
matrix: its proof uses matrix power series, without companion
coefficients or a spectral hypothesis. It gives, for X=cos(tS),
Y=sin(tS),

    G=T^(-1) integral_0^T (X^T*X+Y^T*Y) dt.                 (2)

The general finite-horizon positivity input is Tony Stillfjord and
Filip Tronarp, *Computing the matrix exponential and the Cholesky
factor of a related finite horizon Gramian*, arXiv:2310.13462v2,
30 April 2024, [Section 1, (1b)-(2), p.1](https://arxiv.org/pdf/2310.13462v2).
Take generator T*M^T and input sqrt(T)*I in its unit-interval
controllability integral. The input has full range, so W is positive
definite; its principal block and positive multiple G are positive
definite. No stability or unique algebraic Lyapunov solve is assumed.

The derivative estimate used below is A. Shadrin, G. Nikolov and
D. Aleksov, *On the Markov inequality in the L2-norm with Gegenbauer
weight*, arXiv:1510.03265v1, 12 October 2015,
[Theorem 1.1, p.2; (2.1)-(2.3), p.3; both concluding parity cases,
p.7](https://arxiv.org/pdf/1510.03265v1). For degree at most n and
weight (1-x^2)^(lambda-1/2), lambda>-1/2, its derivative constant is
less than (n+1)(n+2lambda+1)/(2*sqrt(2lambda+1)). At lambda=1/2
this is the unweighted L2 norm on [-1,1]. The affine rescaling to
[-T,T] divides this constant by T. Since n=d-1 and T=d^2, it gives

    ||p'||_0 <= q_d*||p||_0,
    ||p||_0^2=(2T)^(-1) integral_(-T)^T |p(t)|^2 dt.       (3)

The constant factor in the measure does not affect the inequality.
The source covers both parities; no restriction to even polynomials
is imposed. The same bound applies to every lower-degree derivative
because it still lies in the degree-at-most-n space. It extends to
complex coefficients by applying its squared real inequality to real
and imaginary parts and adding them.

For the final compression use John Watrous, *The Theory of Quantum
Information*, 2018 author version,
[Section 1.1, (1.165)-(1.175), (1.179)-(1.181), pp.32-34](https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf):
the Schatten ideal inequality implies ||V^* H V||_1<=||H||_1 when
V^*V=I. These general inputs were assessed in source-notes1947/1950
and are imported without reproof. Neither the single-input Legendre
Gramian example nor a first-order-only Sobolev norm replaces (2).
The work here is the exact phase conversion, all-channel norm
comparison and full-cost lower bound missing from those sources.

For the standard Legendre data used below, precise references are
NIST DLMF [Table 18.3.1, Legendre row](https://dlmf.nist.gov/18.3#T1)
(orthogonality, weight, squared norm and leading coefficient),
[18.5.5 and Table 18.5.1](https://dlmf.nist.gov/18.5#E5)
(Rodrigues normalization), and [18.5.7](https://dlmf.nist.gov/18.5#E7)
at Jacobi parameters alpha=beta=0 (finite expansion). These references
were inspected in source review1952. The finite calculation below is
retained to check the endpoint signs and normalization in this metric;
it does not claim a new Legendre identity.

### Unitary phase conversion and all observation channels

Let U=diag(i^(d-j))_(j=1)^d. Then U is unitary and U^* S U=i*S.
Put E_+(t)=exp(i*t*S), E_-(t)=exp(-i*t*S). Equation (2) says

    G=(2T)^(-1) integral_0^T (E_+^* E_+ + E_-^* E_-) dt,

because the cross terms in X+iY and X-iY cancel. Unitary conjugation
gives U^* E_+(t) U=exp(-tS) and U^* E_-(t) U=exp(tS). Therefore

    K=U^* G U
     =(2T)^(-1) integral_(-T)^T exp(t*S^T)*exp(t*S) dt.     (4)

This is a real positive definite matrix. By the spectral theorem,
positive square roots commute with unitary conjugation. With
B=K^(1/2)*S*K^(-1/2), this proves

    U^* J U=(B+B^T)/2=:H,          k_d(S)=||H||_1.         (5)

The plus sign in (5) is essential: the conjugated first similarity is
iB, whose adjoint is -iB^T. This is not the imaginary part of B.

For v in C^d set

    p_v(t)=sum_(j=1)^d v_j*t^(d-j)/(d-j)!.

This is a bijection onto the polynomials of degree at most n.
The j-th coordinate of exp(tS)v is p_v^(d-j)(t), and
p_(Sv)=p_v'. Thus (4) gives the exact norm and inner product

    v^* K v=||p_v||_S^2,
    <p,q>_S=sum_(r=0)^n (2T)^(-1)
                          integral_(-T)^T conjugate(p^(r))*q^(r) dt.

Every observation row appears once, as a derivative order r=0,...,n.
The map p_v -> K^(1/2)v is an isometry to C^d, and differentiation
is carried to B. Hence H is the symmetric part of differentiation
in this full inner product, not in the scalar zeroth-order norm.

For d>=3, q_d^2<=2/9<1. Iterating (3) and summing a finite geometric
series establishes the uniform, inverse-safe comparison

    ||p||_0^2 <= ||p||_S^2
               <= sum_(r=0)^n q_d^(2r)*||p||_0^2
               <= (1-q_d^2)^(-1)*||p||_0^2.              (6)

No matrix condition number in the original coefficient coordinates is
bounded or assumed. Equation (6) retains all derivative energies.

### Explicit parity witnesses with nonnegative endpoint derivatives

Use the Legendre polynomials with Rodrigues normalization

    P_m(x)=(2^m*m!)^(-1) (d/dx)^m (x^2-1)^m.

The following standard finite identities are checked here only to
fix the normalization, parity and endpoint signs needed by the
specialization; their rederivation is not a novelty claim. Integration
by parts m times shows orthogonality to every polynomial of degree
less than m: the needed boundary derivatives of (x^2-1)^m vanish.
The leading coefficient of P_m is
a_m=(2m)!/(2^m*(m!)^2). Consequently the same integration by parts
against P_m gives

    integral_(-1)^1 P_m(x)^2 dx
        =a_m/2^m * integral_(-1)^1 (1-x^2)^m dx
        =2/(2m+1).

For the last equality, if I_m is the remaining integral, integration
of the derivative of x*(1-x^2)^m gives
(2m+1)*I_m=2m*I_(m-1) for m>=1, while I_0=2. Thus
I_m=2^(2m+1)*(m!)^2/(2m+1)!, proving the displayed normalization.
Rodrigues' formula also gives P_m(-x)=(-1)^m P_m(x).
Expanding (x^2-1)^m=(x-1)^m*(2+(x-1))^m before differentiating
gives the finite Taylor identity

    P_m(x)=sum_(r=0)^m (m+r)!/[2^r*(r!)^2*(m-r)!]*(x-1)^r.

In particular P_m(1)=1 and
P_m^(r)(1)=(m+r)!/[2^r*r!*(m-r)!]>0 for 0<=r<=m;
higher derivatives are zero. These statements fix all endpoint signs.

Define two real polynomials

    p_e(t)=sum_(0<=m<=n, m even) (2m+1)*P_m(t/T),
    p_o(t)=sum_(0<=m<=n, m odd)  (2m+1)*P_m(t/T),
    E=sum_(0<=m<=n, m even) (2m+1),
    O=sum_(0<=m<=n, m odd)  (2m+1).

E and O are positive for d>=3. Orthogonality, rescaling and the
endpoint values just proved show

    ||p_e||_0^2=E,  ||p_o||_0^2=O,
    p_e(T)=E,      p_o(T)=O,
    p_e^(r)(T)>=0, p_o^(r)(T)>=0                 (all r>=0). (7)

The derivative signs survive rescaling since T>0. The finite sums
satisfy E+O=d^2 and E-O=(-1)^(d-1)*d (the latter follows immediately
by induction on n). Therefore

    sqrt(E*O)=d*sqrt(d^2-1)/2.                              (8)

Even and odd polynomials are orthogonal for the full inner product
<.,.>_S: after the same number of derivatives their parities remain
opposite, so each integrand is odd. In particular the normalized
witnesses e=p_e/||p_e||_S and o=p_o/||p_o||_S are orthonormal.

### Boundary pairing and the full Schatten lower bound

For real p,q, the bilinear form of H, transported by the isometry
above, is

    h(p,q)=(<p',q>_S+<p,q'>_S)/2
          =(4T)^(-1) sum_(r=0)^n
                           [p^(r)(t)*q^(r)(t)]_(t=-T)^(t=T). (9)

This is finite integration by parts; at r=n both differentiated
factors in the integral are zero, and their constant product has
zero endpoint difference. There is no omitted top-order term or
interchange of infinite sums. For an even p and odd q,
p^(r)(-T)*q^(r)(-T)=-p^(r)(T)*q^(r)(T) for every r. Thus (7)-(9)
give, retaining all channels and then dropping only nonnegative terms,

    h(p_e,p_o)=(2T)^(-1) sum_(r=0)^n p_e^(r)(T)*p_o^(r)(T)
              >= E*O/(2T).

By (6), ||p_e||_S*||p_o||_S <= sqrt(E*O)/(1-q_d^2). It follows that

    h(e,o) >= (1-q_d^2)*sqrt(E*O)/(2T).                   (10)

The diagonal forms h(e,e), h(o,o) are zero, either by parity in the
inner products or by equal squared endpoint values in (9).
Compression of H to the two orthonormal witnesses therefore has
matrix [0 h(e,o); h(e,o) 0], with trace norm 2*h(e,o). The imported
compression inequality and (5), (8), (10) yield

    k_d(S) >= (1-q_d^2)*sqrt(E*O)/T
           = (1-q_d^2)*sqrt(1-d^(-2))/2.

This lower-bounds the full norm; it never identifies that norm with
the compression. Since 1-q_d^2>=7/9 and sqrt(1-d^(-2))>=2*sqrt(2)/3
for d>=3, the uniform floor in (1) follows. Finally q_d^2 tends to
1/8 and sqrt(1-d^(-2)) tends to 1, proving the liminf bound 7/16.
No convergence of k_d(S) itself, sharp limiting constant, actual-Xi
transfer, or RH consequence has been proved.

### Independent conceptual audit1953

The approved audit checked the existing specialization, using the
source coverage recorded in assessment1951 and source-notes1952/1950.
The following explicit checks establish the scope of the verification;
no numerical experiment or floating-point inverse is an input.

For the local input C029b, only its general real-matrix power-series
realification is used. For this S it gives (2) exactly. The Gramian
substitution in the cited source is N=T*M^T with input sqrt(T)*I:
the factors in its integral are exp(s*T*M^T)*T*I*exp(s*T*M).
Changing variables t=T*s gives W in the stated order, so no transpose
or time-normalization reversal is present. Full-range identity input
establishes positivity without stability or diagonalizability.

The nonzero (j+1,j) entry of U^* S U equals
conjugate(i^(d-j-1))*i^(d-j)=i. Taking the adjoint gives
U^* S^T U=-i*S^T. Unitary covariance of the positive square root
and its inverse therefore transforms the two numerator terms of J
to i*B and -i*B^T, respectively. This verifies the plus sign and
factor 1/2 in (5); trace-norm invariance is unitary, not invariance
under an arbitrary similarity.

Directly, (exp(tS)v)_j=sum_(l=1)^j v_l*t^(j-l)/(j-l)!
equals p_v^(d-j)(t). Thus the orders 0 through n each occur exactly
once in the full norm, and p_(Sv)=p_v'. If y=K^(1/2)v and
z=K^(1/2)w for real coefficient vectors, direct multiplication gives

    y^T H z=(v^T*K*S*w+v^T*S^T*K*w)/2
           =(<p_v,p_w'>_S+<p_v',p_w>_S)/2.

This also checks the direction of the transported bilinear form.
At lambda=1/2 the source constant is (n+1)(n+2)/(2*sqrt(2));
rescaling the argument by T divides it by T. Substituting n=d-1
and T=d^2 gives exactly q_d, with q_d^2=(d+1)^2/(8*d^2)<=2/9.
Every differentiated polynomial remains in that degree-at-most-n
space. Constants have zero derivative, and derivatives beyond the
degree vanish, so iterating the weak version of the source bound
requires no positive-degree assumption at later stages. The real and
imaginary part argument checks the complex norm extension. These
facts verify (6) for all channels, without conditioning assumptions.

The Rodrigues integration by parts has no boundary terms because
(x^2-1)^m vanishes to order m at both endpoints. Its leading
coefficient, integral recurrence and Taylor coefficients give exactly
the normalization and endpoint derivatives displayed above; m=0
uses I_0=2 directly. The positive weights 2m+1 and T>0 preserve
all derivative signs. Opposite parity survives the same derivative
order on both factors. In (9) each endpoint difference is therefore
twice the value at T for the cross pairing, whereas a diagonal
endpoint difference vanishes. At order n at least one derivative in
the cross product is zero, since the two polynomial degrees have
opposite parity and are at most n. There is no hidden top-order term.

Let V have columns K^(1/2)v_e and K^(1/2)v_o, where p_(v_e)=e
and p_(v_o)=o. The full-norm parity orthogonality gives V^*V=I_2.
The preceding bilinear identity gives V^* H V=[0 h; h 0], with
h=h(e,o)>0, hence its singular values are h,h. Applying the cited
rectangular Schatten ideal inequality at p=1 bounds 2h by ||H||_1.
Inserting (6)-(8) gives the first inequality in (1), including its
factor 1/2. For all d>=3 the two lower factors are 7/9 and
2*sqrt(2)/3, giving 7*sqrt(2)/27; its square 98/729 exceeds
(1/3)^2=81/729. Taking the limit of the lower bound gives 7/16
as a liminf, without assuming convergence of the full norm.

Finally S is nilpotent with S^(d-1) nonzero and S^d=0, so its
only eigenvalue is zero and it is defective for d>=2. The verified
positive cost thus obstructs only real-spectrum-alone sufficiency
for this fixed metric and horizon. It does not turn the upper height
majorant into a lower height estimate or transfer to the actual C_d.
The audit adds no direct local mathematical input beyond C029b.

## Mathlib

Full matching coverage for this nilpotent realified-Gramian trace-norm
floor has not been checked. No Lean verification or absence claim is
made. The external Gramian, scalar Markov and Schatten inputs are the
precisely cited analytic references above; the elementary finite
Rodrigues calculation fixes the normalization used in this proof.
