# Lemma 579: the finite-covariance resonant mixture also misses the clipped threshold

## Hypotheses

Let A,C,D be deterministic numbers in [0,4], p in [0,1], and phi real.
Let U be uniform on [-1/4,1/4] and B uniform modulo 2pi, independently.
Let V have an even positive probability law on [-1/2,1/2], and E be
uniform modulo 2pi independently of V. A selector, independent of the
whole tuple (U,B,V,E) and constant along each path, chooses

    P(x)=A cos(Ux+B)+C cos(2Ux+2B+phi)

with probability p, and R(x)=D cos(Vx+E) otherwise. Call the selected
process S. No independence between the unselected packet and remainder
tuples is required. Define the ordinary derivative jet and clipped form

    J=(S(0),S'(0),S''(0),S(1),S'(1),S''(1)),
    Q(J)=(S(0)S''(0)-S'(0)^2)_+.

Require all 21 unordered entries E JJ^T=K, where K is the matrix of
L473 (6), namely

    K_((r,j),(s,k))=integral_(-1/2)^(1/2)
                    (iw)^j(-iw)^k exp(i(r-s)w) dw,
    r,s in {0,1}, j,k in {0,1,2}.

There is no equality-of-full-spectral-measures hypothesis. There are no
fourth-moment, actual-Hardy, Xi, RH or simplicity assumptions.

## Conclusion

Every such finite-K mixture satisfies

    0<=E Q(J)<=1/(72 pi sqrt(2))<5/1512<1/288.                  (1)

The rational threshold gap is 1/288-5/1512=1/6048. In fact the same
bound holds under only the necessary entry E S(0)^2=1; no supported
moment representation, spectral density domination or residual matrix
sufficiency is assumed. Thus the entire stated finite-K family fails
the clipped-mean test. It is nonempty: p=0, D=sqrt(2) and uniform V
satisfy all entries, as checked in L578.

This is a local route obstruction under the prior EXPLORE assessment,
not a resolution of any actual-Hardy or RH gap, nor a certified novelty
claim. The separate critical application audit below passes without
changing the hypotheses or bound.

## Proof

### A necessary finite covariance constraint

The mass entry of L473 (6) is K_((0,0),(0,0))=1. Orthogonality of the
first and second B harmonics gives E P(0)^2=(A^2+C^2)/2. Uniform E
gives E R(0)^2=D^2/2, also if V is zero or has atoms. Independence of
the selector from the whole tuple therefore implies the exact identity

    1=p(A^2+C^2)/2+(1-p)D^2/2.

Nonnegativity of the second term and (A-C)^2>=0 yield

    pAC<=p(A^2+C^2)/2<=1.                                    (2)

Only this necessary entry of K is used below. In particular (2) does
not assert the stronger density inequality L578 (5), which required
full spectral completion. No existence conclusion follows from (2).

### A sharper integrated phase envelope

The algebraic identities L578 (6)--(7) hold before imposing spectral
completion. At x=0 they give

    PP''-(P')^2=U^2 W(B),
    W(theta)=-A^2-4C^2
                -(AC/2)(9 cos(theta+phi)+cos(3theta+phi)),
    W(theta)<=AC[-7/2-(9/2)cos(theta+phi)].                    (3)

Indeed A^2+4C^2>=4AC and cos(3theta+phi)>=-1 prove the last line.
All signs and normalizations in (3) are part of the audited local
L578 calculation, not a new spectral import. For the remainder,

    RR''-(R')^2=-D^2 V^2<=0,                                  (4)

including zero frequencies. We now integrate (3) more sharply than
L578's arc-length-times-height bound.

Represent theta+phi modulo 2pi as pi+v with -pi<=v<=pi; endpoint
choices are irrelevant to the phase integral. Put

    h(v)=-7/2+(9/2)cos v.

For 0<=v<=1, Taylor's theorem through degree three with Lagrange
remainder gives

    cos v<=1-v^2/2+v^4/24
          <=1-(11/24)v^2<=1-(4/9)v^2,                         (5)

because the fourth derivative of cosine is at most one, v^4<=v^2,
and 11/24-4/9=1/72>0. The same inequality holds for negative v by
evenness. At v=1 it also gives cos 1<=13/24<7/9. Cosine decreases
on [0,pi], so h(v)<0 for 1<=|v|<=pi. For |v|<=1, (5) gives
h(v)<=1-2v^2. Consequently the following bound holds on the entire
closed interval, not just on a sampled arc:

    h(v)_+<=(1-2v^2)_+,  -pi<=v<=pi.                         (6)

Outside [-1,1] both positive parts in (6) vanish. Within it, the
positive-part function is monotone, which proves (6) even where its
quadratic right side vanishes. Since AC>=0, (3) implies
W(theta)_+<=AC h(v)_+. Uniform B remains uniform after translation
and reduction modulo 2pi. Therefore

    E_B W(B)_+
      <=AC/(2pi) integral_(-1/sqrt(2))^(1/sqrt(2)) (1-2v^2) dv
       =2AC/(3pi sqrt(2)).                                   (7)

For the integral, evaluating v-(2/3)v^3 at the two endpoints gives
4/(3sqrt(2)); the factor 1/(2pi) is retained. The integration domain
lies inside [-pi,pi], since pi>3.

Independence of U and B, E U^2=1/48, independence of the selector,
and (4) now give

    E Q(J)=p E U^2 E_B W(B)_+
           <=pAC/(72pi sqrt(2))<=1/(72pi sqrt(2)),             (8)

using (2). Every variable is bounded, so all phase and frequency
integrals and the conditioning are legitimate finite expectations.

### Strict comparison and all degenerate cases

The elementary inequalities pi>3 and sqrt(2)>7/5 imply

    1/(72pi sqrt(2))<5/1512,
    1/288-5/1512=1/6048>0.

This proves (1). If A=0 or C=0, (3) gives W<=0 and the clipped
mean is exactly zero; if p=0 only (4) contributes, again giving zero.
The argument for p=1 uses (2) unchanged and does not divide by 1-p.
If D=0, or the remainder covariance mass is zero for any other reason,
the mass identity and (2) still hold without normalization or division
by that mass. U=0 and any atom V=0 cause no exception in (3)--(4).
These cases exhaust all possibly vanishing factors used in the proof;
no division by p, A, C, D or a remainder mass has occurred.

The remaining 20 K entries can only restrict the family further.
Their representing-measure feasibility is unnecessary for a necessary
uniform upper bound. This does not replace them by a matrix positivity
test or assert a construction. The existing fully completed example
quoted after (1) verifies nonemptiness. Positivity and the phase model
are retained throughout; signed repairs are never admitted.

### Scope and source qualification

The prior assessment is
`drafts/literature/2026-10-31-resonant-finite-k-relaxation.md`, whose
exact COVERED_TARGET permits a necessary finite-moment inequality and
reuse of L578's phase calculation. Its inspected representation inputs
are Bayer--Teichmann, *The proof of Tchakaloff's Theorem*, Proc. AMS 134
(2006), 3035--3040, Corollary 2, and di Dio--Schmuedgen,
arXiv:1703.01497v2 Lemma 8 and arXiv:1809.00584v1 Proposition 75.
None is needed in this proof: a necessary mass constraint and pointwise
phase envelope decide the bound before any representation problem.
L473 is used only for its definition of K, not its arithmetic or
nonstationary bulk construction. L578 supplies algebraic phase and
single-wave identities without its full-spectrum hypothesis, and the
nonempty example with full completion.

The known single-wave spectral construction is already qualified in
L578: Rahimi--Recht (2007), *Random Features for Large-Scale Kernel
Machines*, Section 3, Theorem 1, equation (2) and its following real-phase
formula, printed p. 3,
[author PDF](https://people.eecs.berkeley.edu/~brecht/papers/07.rah.rec.nips.pdf).
No new source theorem or reproof is claimed; the elementary calculation
above addresses the precise nonlinear difference left by the assessed
sources. The assessment's bounded search did not supply this conclusion,
which does not establish originality.

The amplitude caps and supported even remainder restrictions are kept
exactly as approved, even though the bound uses only nonnegative
amplitudes, a legitimate uniform-phase remainder and its variance.
There is no conclusion for extra harmonics, changed packet frequency
law, nonuniform phase, a sum in place of the selector, or other stationary
processes. Full fourth-law realization, derivative-preserving correction,
actual-Hardy law comparison and Xi transfer remain separate open gaps.
The present obstruction stops this family without a parameter retry.

### Independent application audit, 2026-10-31

The unchanged EXPLORE assessment
`drafts/literature/2026-10-31-l579-independent-audit.md` was approved
before this audit. This is an independent replay of the mathematical
application, not a new source theorem or an audit of the background
manuscripts. Only L473 (6) and L578's algebraic phase and single-wave
identities enter; L578's full-spectrum condition (5) does not enter.

**Mass and mixture.** Direct phase integration gives
E cos(B)^2=E cos(2B+phi)^2=1/2 and
E cos(B)cos(2B+phi)=0. Likewise E cos(E)^2=1/2 regardless
of V. Independence of the path-constant selector gives exactly the
mass identity above, with weights p and 1-p rather than their squares.
The K mass is the length of [-1/2,1/2], namely 1. Thus
pAC<=p(A^2+C^2)/2<=1, without division by any parameter or
an assertion of residual-measure feasibility. Cross-dependence between
the two unselected tuples is immaterial to these conditional laws.

**Derivative signs and the whole circle.** With theta=B and
psi=2B+phi, the derivatives are

    P'(0)=-U(A sin(theta)+2C sin(psi)),
    P''(0)=-U^2(A cos(theta)+4C cos(psi)).

Expansion gives diagonal terms -A^2-4C^2 and cross terms
-AC(5 cos(theta)cos(psi)+4 sin(theta)sin(psi)), times U^2.
The product-to-sum identities give precisely the 9:1 coefficients
in (3). Since (A-2C)^2>=0, its envelope follows for every phi;
the third harmonic is bounded pointwise, never assumed independent
of the first. For the remainder the same expansion gives exactly
-D^2 V^2. Both identities include zero frequencies.

For 0<v<=1, the degree-three Taylor polynomial of cosine at zero
is 1-v^2/2, with remainder cos(xi)v^4/24 for some xi in (0,v).
Hence (5) holds, also at v=0 and by evenness at negative v.
The coefficient check is 11/24-4/9=1/72>0. At 1 the sharper
bound is cos(1)<=13/24<7/9. Monotonicity of cosine on [0,pi]
therefore makes h strictly negative for 1<=|v|<=pi. On the
remaining interval h<=1-2v^2, and monotonicity of the positive
part proves (6), including the region 1/sqrt(2)<=|v|<=1.
Outside [-1,1] both positive parts vanish. This proves the entire
closed-circle bound; no quadrature, grid or local-only estimate enters.

**Integration and strict threshold.** At a=1/sqrt(2),
a-(2/3)a^3=2/(3sqrt(2)); subtracting its value at -a gives
4/(3sqrt(2)). The uniform phase density is 1/(2pi), so the
phase mean is at most 2AC/(3pi sqrt(2)). The uniform frequency
density is 2 on [-1/4,1/4], giving E U^2=1/48. Independence of
U and B and the zero remainder contribution therefore yield exactly
the upper bound (8). Since pi>3 and sqrt(2)>7/5 (the latter from
2>49/25), it is strictly smaller than 5/1512. In denominator
6048 the last threshold difference is 21-20=1, as claimed.
All variables and derivatives involved are bounded; finite conditioning,
phase integration and factorization require no limit interchange.

**Degeneracies and the nonempty example.** If AC=0 or p=0 the
clipped mean vanishes. If p=1 the mass inequality still applies;
if D=0 or a remainder mass vanishes no normalization is used.
Atoms of V, including zero, cause no exception. These cover every
possibly vanishing factor; no probability, amplitude or frequency
was divided out. Arbitrary fixed phi is covered by uniform phase
translation and the pointwise third-harmonic bound.

For nonemptiness take p=0, D=sqrt(2) in [0,4], and V uniform
on [-1/2,1/2], independently of E. For every r,s in {0,1} and
j,k in {0,1,2}, expand the two real parts in

    R^(j)(r)=sqrt(2) Re((iV)^j exp(i(rV+E))).

The terms with phase exponent +/-2iE integrate to zero, leaving

    E R^(j)(r)R^(k)(s)
      =Re integral_(-1/2)^(1/2)
          (iw)^j(-iw)^k exp(i(r-s)w) dw.

The integral is real: its integrand at -w is the conjugate of its
integrand at w. It is exactly K by L473 (6). This verifies all
21 unordered entries simultaneously, with the covariance signs of
ordinary derivatives and no independence between the two heights.
The example has Q=0 and serves only to verify nonemptiness.

**Verdict and limits.** Every proof case passes, with no hypothesis
or numerical correction required. The finite-K family stop is now
independently audited; the sharper phase integral, rather than any
full-spectrum domination, is decisive. The direct mathematical uses
match the unchanged canonical DAG. No bound
has been improved and no new mathematical discovery or RH advance
is claimed. General stationary laws, extra harmonics, different packet
frequency laws, all 126 fourth constraints, derivative-preserving
correction and actual-Hardy/Xi transfer remain outside the result.

## Mathlib

Full matching coverage for this finite-covariance coherent packet and
clipped phase integral has not been checked. No absence or matching
formal theorem is asserted. Supporting facts used here are elementary
phase orthogonality, Taylor's theorem with its stated remainder,
monotonicity of cosine on [0,pi], and finite expectation arithmetic;
the complete specialization and inequalities are given above.
