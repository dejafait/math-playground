# Lemma 597: the second Cauchy derivative of the associated theta kernel

## Hypotheses

Let k(u)=K(|u|) be the actual theta kernel of L019, with the even
continuation justified in L239. On the real axis put

    A(t)=integral_R s^2 k(s+t)k(s-t) ds,
    C_A(z)=(1/(2pi i)) integral_R A(t)/(t-z) dt,   Im z>0,
    c(y)=C_A(iy),                               y>0.

This A agrees with the real restriction of L596's associated kernel;
no assertion about its complex boundary is used. In particular C_A(iy)
is not A(iy). No Fourier positivity, RH, or simplicity is assumed.

Import George Csordas, *Fourier transforms of positive definite kernels
and the Riemann xi-Function*, arXiv:1309.0055v2 (21 February 2014),
Definition 1.2, (4.2), Theorem 4.5 and (4.6), printed pp.2, 9, 11:
[versioned primary text](https://arxiv.org/html/1309.0055v2),
[PDF](https://arxiv.org/pdf/1309.0055v2).
Theorem 4.5 supplies admissibility of K_1(t;Phi). Its strict-decrease
input is Theorem 3.5, whose two integration ranges were checked in the
saved source assessment. We import this shape theorem, rather than
reprove theta logarithmic concavity. The exact scaling is checked below.

## Conclusion

The function c is real and twice continuously differentiable on
(0,infinity), and for every y>0,

    c''(y)=-(2y/pi) integral_0^infinity t A'(t)/(t^2+y^2)^2 dt > 0.

All differentiation and integration-by-parts endpoints in this identity
are justified below. The same identity and strict sign hold for any
real even Schwartz function H with H'(t)<0 for t>0, on replacing A by H.
Thus this sign uses known shape information and elementary calculus;
it is not a theta-specific all-order positivity mechanism.

At second order, Norvidas arXiv:2009.04449v1 (2.15) has the opposite
sign to the defining Poisson integral. The necessary condition (1.7)
at n=0 consequently also has the opposite sign; a Gaussian satisfies
all hypotheses of Corollary 3 and violates that displayed condition.
This conclusion concerns those displayed statements at these indices,
not Norvidas's real-even full-hierarchy criterion (Theorem 2).

## Proof

### Exact kernel and imported shape

Comparing L019's series on u>=0 with Csordas's (4.2) gives

    k(u)=4 Phi(u/2).

Both functions are even: use L239 for k and Csordas's Theorem 4.5
for Phi. The equality therefore holds on the entire real line.
Set s=2v in the defining integral of A. The two kernel factors
contribute 16, s^2 contributes 4, and ds contributes 2. Hence

    A(t)=128 integral_R v^2 Phi(v+t/2)Phi(v-t/2) dv
        =128 K_1(t/2;Phi).

Theorem 4.5 and Definition 1.2 imply that A is smooth, positive and
even, and A'(t)=64 K_1'(t/2;Phi)<0 for t>0. Every derivative decays
at infinity under this positive rescaling. More precisely the source
bound becomes O(exp(-c |t|^(2+epsilon))) for some c,epsilon>0;
evenness gives the other end. In particular A and A' are integrable
and bounded, A tends to zero, and A(0)>0. L233 independently supplies
absolute integrability of A and all its polynomially weighted moments.
No spectral conclusion is imported from admissibility.

### Differentiation and the boundary terms

The Cauchy integral is absolutely convergent since |t-iy|>=y and
A is integrable. Writing 1/(t-iy)=(t+iy)/(t^2+y^2), the odd part
integrates to zero. Thus

    c(y)=(1/(2pi)) integral_R y A(t)/(t^2+y^2) dt
        =(1/pi) integral_0^infinity y A(t)/(t^2+y^2) dt.

This proves reality and fixes the normalization. For a compact interval
0<a<=y<=b, the j-th y derivative of (t-iy)^(-1) is bounded in modulus
by j! a^(-j-1), j=0,1,2. Multiplication by |A(t)| gives an integrable
majorant independent of y. Dominated differentiation, followed by
dominated convergence for continuity, is therefore valid twice.
Direct differentiation of the last real integral gives

    c''(y)=(2y/pi) integral_0^infinity
                       A(t)(y^2-3t^2)/(t^2+y^2)^3 dt.

For fixed y>0,

    d/dt [t/(t^2+y^2)^2]=(y^2-3t^2)/(t^2+y^2)^3.

Integrate by parts first on [0,R]. The boundary product at zero is
zero since A is bounded and t/(t^2+y^2)^2 vanishes there. The product
at R tends to zero, since A is bounded and that rational factor is
O(R^(-3)). The differentiated rational factor is bounded for fixed y,
as is the undifferentiated factor; integrability of A and A' therefore
justifies the two improper integral limits separately. This yields

    c''(y)=-(2y/pi) integral_0^infinity t A'(t)/(t^2+y^2)^2 dt.

The integrand is strictly negative at every t>0, is continuous and
absolutely integrable. Its integral is strictly negative (for example
already on any fixed compact subinterval of (0,infinity)). This proves
c''(y)>0 for every y>0. The compact-y argument covers (0,infinity);
it makes no uniform assertion as y tends to zero. All of this calculus
applies verbatim to the generic H in the conclusion.

### Independent replay of the source's second-order sign

Use S. Norvidas, *A note on harmonic continuation of characteristic
function*, arXiv:2009.04449v1 (9 September 2020), (1.3), Corollary 3
(1.7), and the integration-by-parts line preceding (2.15), printed
pp.2-3, 6: [primary text](https://arxiv.org/html/2009.04449v1),
[PDF](https://arxiv.org/pdf/2009.04449v1).
Both versioned HTML and extracted PDF display the signs discussed here.
This replay is necessary because quoting (2.15) would reverse the sign
just proved from the defining integral.

For a real even Schwartz function f, denote its Poisson continuation by

    u_f(0,y)=(1/pi) integral_R y f(t)/(t^2+y^2) dt,
    J_f(y)=integral_R Im[(t-iy)^(-2)] f'(t) dt.

The preceding calculus gives, with all the same endpoint justifications,

    u_f''(0,y)=-J_f(y)/pi,
    J_f(y)=integral_R 2ty f'(t)/(t^2+y^2)^2 dt.

In contrast (2.15) at n=1 displays u_f''(0,y)=+J_f(y)/pi.
One can locate the discrepancy directly. For this Schwartz f, the
analytic function E_f used in the source is 2C_f: the correcting
integral of t f(t)/(1+t^2) vanishes by oddness. Differentiating twice
and integrating by parts gives

    E_f''(z)=(2i/pi) integral_R f(t)/(z-t)^3 dt
            =-(i/pi) integral_R f'(t)/(z-t)^2 dt.

The boundary f(t)/(z-t)^2 vanishes at both infinities, and all integrals
are absolutely convergent for Im z>0. The source's intervening formula
at k=2 instead has a plus sign in front of this last integral. Using
u_f''(0,y)=-Re E_f''(iy) recovers -J_f(y)/pi. Thus the discrepancy is
not the factor two between C_f and the source's analytic continuation.
The companion Norvidas arXiv:2009.04492v1, (1.6)-(1.7), uses
k_f(z)=(i/pi) integral_R f(t)/(z-t)dt=2C_f(z), consistently with this
normalization; see [primary text](https://arxiv.org/html/2009.04492v1).

For an explicit check on Corollary 3's necessity claim, take f(t)=exp(-t^2).
It is the characteristic function of N(0,2), by the standard Gaussian
Fourier integral

    exp(-t^2)=(1/(2 sqrt(pi))) integral_R exp(-x^2/4)exp(itx) dx.

It is normalized at zero, real and even, and every derivative is a
polynomial times exp(-t^2), hence bounded and continuous. Nevertheless

    J_f(y)=-4y integral_R t^2 exp(-t^2)/(t^2+y^2)^2 dt < 0

for every y>0, contradicting the displayed requirement J_f(y)>=0 in
(1.7) at n=0. This Gaussian need not meet Csordas's super-Gaussian
admissibility definition; it meets all hypotheses of the corollary
being checked. No other index of that corollary is audited here.

For the actual A, u_A(0,y)=2c(y); for f=A/A(0) the factor is
u_f(0,y)=2c(y)/A(0). The established strict second derivative therefore
has the required orientation for one member of the Poisson hierarchy.
The full hierarchy remains an unproved hypothesis of Norvidas's
Theorem 2; we do not apply its sufficiency direction. In particular
neither positive definiteness of A nor L233's all-frequency first
Laguerre sign, higher mixed positivity, or RH follows from this result.
The finite test ends here without a third-derivative claim.

## Mathlib

Not checked for a full matching theorem or the supporting Cauchy,
Poisson, Gaussian Fourier, differentiation-under-integral and
integration-by-parts results. Availability is unknown, not absent.
[Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/).
