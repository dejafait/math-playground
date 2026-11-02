# Lemma 619: first-sign smooth-window comparison with full Xi completion

## Hypotheses

Use the actual Xi function of L018, ordinary real derivatives, and the
exact amplitude and Hardy function in L471:

    A(t)=(t^2+1/4) pi^(-1/4)|Gamma(1/4+it/2)|/2,
    Z(t)=-Xi(t)/A(t),
    W(t)=D_1(Xi;t)/A(t)^2.

Fix 0<delta<1/13 and a nonnegative w in C_c^infinity((0,1)) with
integral 1. Let T tend to infinity, L=log T,

    T<=X<=2T,  T^(12/13+delta)<=H<=T,
    w_XH(t)=w((t-X)/H),
    P(z)=c0+c1 z,  U_P(t)=c0 Z(t)+c1 Z'(t)/L,

where c0,c1 are real and not both zero; they may depend on T,X,H.
The entire support is in [T,3T]. No RH, simplicity, spacing,
nonvanishing at the center, or zero-free half-plane is assumed.

The arithmetic input is C. P. Hughes and M. P. Young, *The twisted
fourth moment of the Riemann zeta function*, arXiv:0709.2345v2,
[Theorem 1.1, (12)–(17), printed pp. 4–5](https://arxiv.org/pdf/0709.2345v2#page=4),
including the subsequent holomorphy remark. Its arithmetic proof is
a named import, not independently audited here.

## Conclusion

The positive form in bramble_trace, *Signs and uniform filtered
positivity in fourth moments of Hardy's function*,
[paper 36 v4, 21 October 2026, Theorem 6/(21)](https://rstation.ai/problems/riemann_hypothesis/papers/36),
specializes exactly to

    B_1(P)=(28 c0^2+c1^2)/(840 pi^2).                       (1)

For any fixed 0<sigma<min(1/4,13delta/4), put

    e(T,H)=1/L+T^(3+sigma)/(H^(13/4)L^4).

Uniformly over the stated X,H and all nonzero real coefficient vectors,

    integral w_XH W U_P^2 dt / [H L^6 B_1(P)]
       =1+O_(w,sigma)( e(T,H)+(1+e(T,H))/(T^2 L^2) ).       (2)

For example sigma=13delta/8 makes the relative error
O_(w,delta)(1/L+T^(-13delta/8)/L^4+T^(-2)/L^2)=o(1).
Thus the signed integral is strictly positive beyond one onset
depending on w,delta, uniformly in X,H,c0,c1.

This verifies the fixed p=1,d<=1 application of source Theorem 8,
Section 7/(35)–(37), and retains the Xi curvature in transferring it.
It is reproduction/specialization, not a new arithmetic theorem.
The conclusion is averaged: it supplies no pointwise sign, negative-part
saving, individual-zero localization, higher-order sign or effective
height. The H=T, delta=1/26, sigma=1/88 application used by L621
received a separate later audit on 1 November 2026, as recorded below.
This does not certify every other H in the stated range.

## Proof

### 1. Exact import and admissible parameters

For small complex alpha,beta,gamma,eta, set

    J(alpha,beta,gamma,eta)
     = zeta(1+alpha+gamma) zeta(1+alpha+eta)
       zeta(1+beta+gamma) zeta(1+beta+eta)
       /zeta(2+alpha+beta+gamma+eta).

In the untwisted case h=k=1, Hughes–Young gives the integral of

    w_XH(t) zeta(1/2+it+alpha) zeta(1/2+it+beta)
             zeta(1/2-it+gamma) zeta(1/2-it+eta)

as the integral against w_XH of the following complete sum, plus
O_(w,sigma)(E), where ell=log(t/(2pi)) and
E=T^(3/4+sigma)(T/H)^(9/4)=T^(3+sigma)H^(-9/4):

    J(alpha,beta,gamma,eta)
    + exp(-ell(alpha+beta+gamma+eta)) J(-gamma,-eta,-alpha,-beta)
    + exp(-ell(alpha+gamma)) J(-gamma,beta,-alpha,eta)
    + exp(-ell(alpha+eta)) J(-eta,beta,gamma,-alpha)
    + exp(-ell(beta+gamma)) J(alpha,-gamma,-beta,eta)
    + exp(-ell(beta+eta)) J(alpha,-eta,gamma,-beta).         (3)

The source weight assumptions are support in [T/2,4T],
w^(j)=O_j(T0^(-j)), T^(1/2+sigma)<<T0<<T; the shifts are
O(1/log T) and coprime h,k obey hk<=T^(2/11-sigma).
Our support is in [T,3T], T0=H, and the derivative constants depend
only on w,j. Our sigma<1/4 and H>=T^(12/13+delta) satisfy the
smoothing condition. If necessary replace sigma by a smaller
positive exponent in the source: its error is then bounded by E,
and hk=1 satisfies its length condition. No twist is discarded.

### 2. Collision-safe leading germ, with all six terms retained

For complex a_j in a fixed bounded polydisc put r_j=i a_j and take

    (alpha,beta,gamma,eta)=(r1,r2,-r3,-r4)/L.

For each two-element subset S of {1,2,3,4}, define

    U_S=sum_(j in S) r_j-sum_(j not in S) r_j,
    D_S=product_(j in S,k not in S)(r_j-r_k),
    Hcal(r)=sum_(|S|=2) exp(U_S/2)/D_S,
    G(a)=6 Hcal(i a)/pi^2.                                (4)

Apparent singularities in Hcal are removable. Away from simultaneous
collisions, the residues at r_i=r_j cancel between S containing i
but not j and S with i,j exchanged. The same cancellation holds
for the complete sum (3): at the collision the remaining factors,
the exponential and the zeta denominator agree. Multiplication
by Delta=product_(i<j)(r_i-r_j) makes each sum analytic. Its numerator
vanishes on every collision hyperplane, first on the dense subset
with no other collisions and then everywhere by continuity.
Successively dividing by these distinct linear factors proves
analytic divisibility by Delta, including at all intersections.
The denominators near zeta(2) are nonzero for sufficiently large T.
This also checks the source's required pole-cancellation use.

Choose distinct fixed radii, for example 3,4,5,6, for the four a_j.
On this product of circles every pair difference is bounded away
from zero. Apply the Laurent expansion zeta(1+v/L)=L/v+O(1)
to each numerator factor, and 1/zeta(2+O(1/L))=6/pi^2+O(1/L).
Since ell/L=1+O(1/L) uniformly for t in [T,3T], multiplying (3)
by exp((r1+r2-r3-r4)/2) gives

    L^4 G(a)+O(L^3).                                      (5)

The six subsets in (4) are, respectively, the original pair, its
complement, and the four single exchanges in (3). Both sides of
(5) are holomorphic on the enclosed polydisc. Applying the maximum
principle successively in its four variables extends the error bound
to |a_j|<=2, including all shift collisions. No individual singular
term is evaluated or differentiated at a collision.

### 3. Hardy phase and a genuinely local absolute bound

L465 Sections 1–2 provide compatible analytic gamma branches around
every sufficiently large t. The resulting analytic Hardy phase obeys
theta'(z)=log(t/(2pi))/2+O(1/t) for |z-t|=O(1/L).
This follows by summing its upper/lower digamma expressions (4);
it does not use the order parameter or saddle restrictions of L465.
More explicitly, if g(s)=log(pi^(-s/2)Gamma(s/2)), its compatible
branches give

    theta(z)=[g(1/2+iz)-g(1/2-iz)]/(2i),
    theta'(z)=[g'(1/2+iz)+g'(1/2-iz)]/2.

The opposite leading arguments of the two logarithms cancel.
Integrating along the complex segment from t to t+a_j/L gives
theta(t+a_j/L)-theta(t)=a_j ell/(2L)+O(1/(TL)) uniformly
for bounded complex a_j. Since ell/L=1+O(1/L) on [T,3T],
this proves the stated phase approximation on a complex neighborhood,
not only on real shifts. The functional equation supplies the
negative-height representation with phase exp(-i theta).
Therefore

    product_(j=1)^4 Z(t+a_j/L)=Phi(t,a) F(t,a),
    Phi(t,a)=exp((r1+r2-r3-r4)/2)(1+O(1/L)),               (6)

where F is the four-zeta product with the shifts above. Here the
first two Z factors use the positive-height zeta representation and
the last two the negative-height representation. The two unshifted
phases cancel. The analytic identity and uniform bound apply to
complex a on a neighborhood of |a_j|<=2 and the full real support.

To estimate the error in (6), apply the same imported theorem to
|zeta(1/2+it+b)|^4. Its shifts are (b,b,conj(b),conj(b)); for a
negative-height factor conjugate first. These are still admissible
complex shifts. The removable-sum estimate above bounds their main
term by O(HL^4), also at repeated shifts. Consequently every such
weighted absolute fourth moment is O(HL^4+E). Holder with respect
to the nonnegative measure w_XH(t)dt then gives

    integral w_XH |F(t,a)| dt = O(HL^4+E).

Thus the integrated phase error is O(HL^3+E/L), on this window
itself. Integrating (5), using integral w_XH=H and the source
remainder E, establishes the holomorphic comparison

    Fcal(a):=integral w_XH product_j Z(t+a_j/L)dt/(HL^4)
            =G(a)+R(a),
    sup_(|a_j|<=2)|R(a)| <= C_(w,sigma) e(T,H).             (7)

Holomorphy of Fcal follows by differentiation of the finite-support
integral, uniformly on compact shift sets. This is not differentiation
of an unspecified error on the real shifts.

### 4. Fixed-degree Cauchy extraction and exact normalization

Let

    Q=partial_1 partial_2-(partial_1^2+partial_2^2)/2,
    V_P=(c0+c1 partial_3)(c0+c1 partial_4).

Then, exactly,

    Q V_P Fcal(0)
     =integral w_XH (Z'^2-ZZ'') U_P^2 dt/(HL^6).           (8)

Cauchy on the four unit circles bounds a derivative of R by the
product of its derivative factorials times C e. The three terms
in Q cost 1,1,1 after their factors 1/2. Since the last two orders
are at most one,

    |Q V_P R(0)| <= 3 C e (|c0|+|c1|)^2.                 (9)

For completeness, the small-degree leading coefficients are checked
directly from the six-term germ, avoiding any further arithmetic
moment import. Write Hcal_k for its homogeneous term of degree k.
Complementing S proves that odd terms vanish. Define m_4=sum_i r_i^4,
m_31=sum_(i!=j) r_i^3 r_j, m_22=sum_(i<j) r_i^2 r_j^2,
m_211=sum_i sum_(j<k; j,k!=i) r_i^2 r_j r_k, and m_1111=r1r2r3r4.
Exact expansion gives

    Hcal_0=1/12,
    Hcal_2=sum_i r_i^2/480-sum_(i<j)r_i r_j/720,
    Hcal_4=m_4/53760-m_31/40320+m_22/16128
             -m_211/40320+m_1111/6720.                   (10)

These finite identities can be checked without evaluating at a
singular point: multiply (10) by Delta and expand the six polynomials

    Delta Hcal_k
     =sum_(|S|=2) (Delta/D_S) U_S^(k+4)
                       /[2^(k+4)(k+4)!],  k=0,2,4.       (11)

Here Delta/D_S is a signed product of two within-pair differences.
The analogous numerator terms of exponential degrees 0,1,2,3
vanish. Formula (11), or direct monomial expansion, gives all
coefficients in (10). The exact rational replay below checks each
whole polynomial identity, not numerical samples.

In degree two Q Hcal_2=-1/180. In degree four
Q partial_3 partial_4 Hcal_4=1/5040, because the all-distinct
derivative is 1/6720 and each repeated-index derivative is
-1/20160. Including the factors 6/pi^2 and i^2 or i^4 in G gives

    Q V_P G(0)=c0^2/(30pi^2)+c1^2/(840pi^2).             (12)

There is no mixed c0c1 term, since Hcal_3=0.

This agrees with the source's exact B_1, rather than just proving
positivity for a different normalization. Its kernel formula is

    B_1(P)=1/(8pi^2) integral_[-1/2,1/2]^2
       [(1-|x-y|)^4-(x+y)^4] P(ix) conjugate(P(iy)) dxdy.

The mixed term integrates to zero by exchanging x,y. Set u=x-y,
v=x+y; the Jacobian is 1/2 and |u|+|v|<=1. Evenness in u gives

    I00=integral_0^1 (8/5)(1-u)^5 du=4/15,
    I11=integral_0^1 [(2/21)(1-u)^7
                         -(2/5)u^2(1-u)^5]du=1/105.

Here I11 includes xy=(v^2-u^2)/4. The real coefficient product is
c0^2+c1^2 xy after cancellation of the imaginary mixed term.
These two integrals prove (1) and in particular

    B_1(P)>=(c0^2+c1^2)/(840pi^2),
    (|c0|+|c1|)^2<=1680pi^2 B_1(P).                     (13)

Equations (7)–(13) prove the required relative Hardy error uniformly
even when the coefficient vector varies or tends to zero.

### 5. Entire completion, zeros included

L471 (7) supplies the exact zero-safe identity

    W=Z'^2-ZZ''-a'' Z^2,  a=log A.                       (14)

L465 Section 5 gives a''(t)=O(t^-2), including both the polynomial
prefactor and the cancellation between the paired gamma derivatives.
Its bound holds for every sufficiently large t, so is O(T^-2) on
[T,3T]; no dyadic-support restriction is imposed here.

The values Fcal(0) and partial_3 partial_4 Fcal(0) from (7) are
O(1+e) by Cauchy. Consequently

    integral w_XH Z^4 dt <= C HL^4(1+e),
    integral w_XH Z^2 (Z'/L)^2 dt <= C HL^4(1+e).

Both integrands are nonnegative. The elementary pointwise inequality
U_P^2<=2c0^2 Z^2+2c1^2(Z'/L)^2 now implies

    |integral w_XH a'' Z^2 U_P^2 dt|
       <= C T^-2 HL^4 (1+e)(c0^2+c1^2).                  (15)

Divide (15) by HL^6 B_1(P) using (13), and combine it with (8)–(9).
This proves (2) with the full completion cost. For sigma=13delta/8,
the second part of e is at most T^(-13delta/8)/L^4. All constants
are independent of X,H and the real coefficients. The error tends
to zero, yielding the stated eventual strict positivity.

No logarithm of Z or Xi has been differentiated; real zeros of any
multiplicity are included. Smooth signed integrals were never
sandwiched by sharp cutoffs. The form's positivity does not isolate
negative values of W or make the weights concentrate at one height.

### Verification and limits

Run `python3 scripts/first-sign-window/audit.py`. The complete exact
rational evidence is `scripts/first-sign-window/certificate.json`.
All six numerator identities through exponential degree eight have
zero polynomial-division remainder; both kernel integrals match (12).
The full degree-two and degree-four coefficients were inspected.
The certificate verifies the finite algebra only; the analytic bounds
are the arguments above, and Hughes–Young remains a cited import.

The source already asserts the Hardy comparison. The reason for this
fixed-degree rederivation is to audit collisions, phase and Cauchy
uniformity and to compare the completion error to an exact coefficient
margin. No novelty claim or RH candidate is made.

### Separate audit of the H=T input used by L621 — 1 November 2026

The audit checked Sections 1–5 at delta=1/26, sigma=1/88 and H=T,
including the full complex domain of the Hardy comparison and the
zero-safe completion. Its imported remainder is E=T^(67/88), hence
e=1/L+T^(-21/88)/L^4. All weight and smoothing hypotheses hold
uniformly for X in [T,2T]. The six-term germ, removable collisions,
absolute fourth-moment bound, Holder estimate and fixed-order Cauchy
operation use this same support and complex-shift range.

The existing rational replay was read and run again. Its full quotient
polynomials at exponential degrees 4, 6 and 8 match (10); the odd
quotients at degrees 5 and 7 vanish. The replay checks every numerator
identity at degrees 0 through 8 by exact multiplication/division. The
selected complete coefficient and kernel evidence gives
pi^2 B_1=(1/30)c0^2+(1/840)c1^2, with no mixed term or failure.
No numerical zeta samples or certificate previews are used as proof.
The paired-gamma curvature calculation in the used L465 ranges and
L471's direct product differentiation justify (14)–(15), including
multiple real zeros. Thus the used margin and absolute analytic bounds
pass this application audit under the named arithmetic imports.
The audit does not independently verify those arithmetic manuscripts,
all other window lengths, or the general source filter theorem.

## Mathlib

Full matching coverage for the shifted fourth moment and this
coefficient-uniform completed-Xi application was not checked and is
unknown. The rational identity replay is not a Lean formalization.
