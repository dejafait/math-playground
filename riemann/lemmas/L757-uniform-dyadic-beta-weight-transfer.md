# Lemma 757: uniform dyadic beta-weight transfer

## Hypotheses

Let rho=beta+i gamma run over all nontrivial zeros of zeta with
analytic orders; distinct zeros sharing an ordinate are separate
terms. Let T tend to infinity through arbitrary real values and
T<=tau<=2T. Define z_rho=gamma+i(1/2-beta) and
z^(-i tau)=exp(-i tau Log z), with the principal logarithm.
L018 identifies z_rho as the Xi zero, preserves orders, gives
0<beta<1, and supplies reflection rho -> 1-conj(rho).

Import Aleksander Simonic, *Explicit zero density estimate for the
Riemann zeta-function near the critical line*,
[arXiv:1910.08274v2](https://arxiv.org/pdf/1910.08274v2#page=33),
29 November 2019, Section 4.5, p.33, equation (74), with constants
defined after (73). Section 4.2's Littlewood count retains orders.
The conventions are

    N(u,H)=sum_{beta>u, 0<gamma<=H} ord(rho),
    D_T(u)=N(u,2T)-N(u,T).

For T>=T_0>=e^24 and 1/2<=sigma<=1/2+8/log T_0, (74) states

    integral_sigma^1 D_T(u) du
      <= (2e^2/pi+alpha) T^(1-(sigma-1/2)/4)
         + b log T+c log log T+d+0.88
         +2.4 log log T_0/log T_0+20/log T_0.             (1)

Here b,c,d rename the source's beta,gamma,delta constants. Fix the
source's final T_0=3.0610046*10^10 and sigma_1=2.40764, satisfying
T_0>=e^24 and sigma_1>=2.4. It records alpha<15291.986, b<4.416,
c<0.6881 and d<0; only finite constants independent of T are needed.
At sigma=1/2, (1) gives nonnegative constants A,B,C,D such that

    I(T):=integral_(1/2)^1 D_T(u) du
         <= A T+B log T+C log log T+D =: Q(T).           (2)

The inspected source coverage includes sigma=1/2, microscopic
displacements and arbitrary ordinate endpoints with all orders.
Full source moment proofs and numerical constants remain independently
unaudited; they are imported, not reproved. The invocation-start
SPECIALIZE assessment is
`drafts/literature/2026-11-04-zero-ordinate-beta-transfer.md`.
This proof supplies exactly its outstanding finite-sum, reflection
and principal-log applicability arguments, not a new density theorem.

## Conclusion

Uniformly for every real T<=tau<=2T, at arbitrary real endpoints,

    E(T,tau):=sum_{T<gamma<=2T}
                [z_rho^(-i tau)-gamma^(-i tau)]

obeys the absolute-difference bound

    |E(T,tau)|
      <=sum_{T<gamma<=2T}|z_rho^(-i tau)-gamma^(-i tau)|
      <=4e I(T)<=4e Q(T)=O(T)=o(T log T).               (3)

All sums retain orders. This is routine specialization of a cited
input, with no originality claim. It proves no shorter-window bound,
paid Xi witness margin, initial Laguerre sign or RH. The application
was critically audited in step 352; the imported source proofs retain
the qualifications above.

## Proof

Fix T>=T_0. Only finitely many zeros occur in the closed slab
T<=gamma<=2T: L018's nonzero entire completion has isolated zeros
in the compact rectangle 0<=Re(s)<=1, T<=Im(s)<=2T. Write each zero
repeated according to its analytic order. Subtracting the inclusive
height counts gives, for every u in [1/2,1], the exact identity

    D_T(u)=sum_{T<gamma<=2T} 1_{u<beta}.                (4)

Zeros at gamma=T cancel, and zeros at gamma=2T are included with
their full orders. Integrating this finite sum and using 0<beta<1,

    I(T)=sum_{T<gamma<=2T} integral_(1/2)^1 1_{u<beta} du
        =sum_{T<gamma<=2T} (beta-1/2)_+.               (5)

The strict cut u<beta changes no integral at u=beta; central zeros
contribute zero. No infinite interchange or limiting choice of
endpoints is used.

The endpoint-inclusive form of (1) is part of the cited input:
Section 4.5, p.33, opening paragraph explicitly extends its estimates
past the exclusion of zeros of the auxiliary mollified function
Phi_X(s)=zeta(s)S_X(s) at T or 2T. We import that extension with (74).
Avoiding zeta ordinates alone would not establish the auxiliary
nonvanishing condition; no such implication is used here.

To check the zeta-count endpoint convention, choose T_j>T decreasing
to T with neither T_j nor 2T_j a zeta ordinate. Finiteness in a
slightly larger compact slab
implies that, eventually, (T_j,2T_j] contains exactly the zeros in
(T,2T], with the same orders: no new zero lies just above either
endpoint. Thus D_(T_j)(u)=D_T(u) for every u, eventually, including
when either original endpoint is an ordinate. The right side of
(1) is continuous in T with T_0 and sigma fixed. Taking this limit
therefore respects precisely the desired endpoint convention,
without assuming continuity of N at an ordinate. This finite-count
check is not a separate proof of the source's auxiliary-mollifier
endpoint extension.

The reflection rho -> 1-conj(rho) sends beta+i gamma to
(1-beta)+i gamma. L018's functional equation and conjugation preserve
orders, making this an involution of the precise multiset in (4).
Reindexing a finite sum therefore gives

    sum (1/2-beta)_+ = sum (beta-1/2)_+ = I(T),
    sum |1/2-beta|=2 I(T),                             (6)

with all sums over T<gamma<=2T. Coincident ordinates and central
zeros cause no exception. The source controls displacement mass,
even at arbitrarily small displacements, rather than an off-line
presence count or an o(T) union of bad heights.

For one zero put v=1/2-beta, so |v|<1/2. For real y on the segment
joining 0 to v, define

    F(y)=exp(-i tau Log(gamma+i y)).

This entire segment lies in the right half-plane since gamma>T>0.
The principal logarithm is holomorphic on a neighborhood of it and
has derivative 1/z. Differentiation yields

    F'(y)=tau exp(-i tau Log(gamma+i y))/(gamma+i y).

Writing theta=arg(gamma+i y)=arctan(y/gamma), one has

    |F(y)|=exp(tau theta),
    |theta|<=|y|/gamma<=1/(2gamma),
    tau/gamma<=2T/gamma<=2,
    |gamma+i y|>=gamma.

Hence tau theta<=tau |theta|<=1, and uniformly over both signs of
v, the entire segment and the whole tau band,

    |F'(y)|<=e tau/gamma<=2e.                         (7)

The fundamental theorem of calculus, reversing orientation if v<0,
gives the pointwise comparison

    |z_rho^(-i tau)-gamma^(-i tau)|
       =|F(v)-F(0)|<=2e |v|.                         (8)

Sum (8), apply the triangle inequality and use (6). This gives
|E|<=4e I(T). Applying (2) proves the asserted O(T), with constants
independent of tau. More explicitly,

    sup_{T<=tau<=2T} |E(T,tau)|/(T log T)
      <=4e [A/log T+B/T
             +C log log T/(T log T)+D/(T log T)] ->0.  (9)

This is the required uniform little-o with one common onset. In
(4)--(6) no count is replaced by a continuous function at an
ordinate. Input (1) applies to arbitrary real T with its recorded
endpoint conventions; the specialization introduces no good-height
restriction or unestimated endpoint loss. No simplicity, spacing,
RH, Lindelof hypothesis, new zero-free region or cancellation inside
E is assumed.

The continuation threshold succeeds with O(T). L756 is a possible
subsequent scalar input, not an input to this transfer proof. General
beta-dependent witness weights, shorter windows, witness realization,
analytic costs and positive margins remain independently unresolved
steps toward actual-Xi signs.

### Critical application audit (4 November 2026, step 352)

The audit passes for (3) and (9), relative to the precise imported
source (74). The following checks account for every application
hypothesis; they do not independently verify the source's moment
proofs or numerical constants.

- The source's microscopic case and its subsequent comparison of
  (73) with (74) explicitly include sigma=1/2. The upper endpoint
  of the integral is 1, not the headline theorem's 0.831 cutoff.
  Fixing T_0=H_0 and sigma_1=2.40764 leaves sigma=1/2 admissible
  for every T>=T_0; all four constants then remain fixed. Taking
  nonnegative upper bounds for the coefficients gives (2), since
  T, log T and log log T are positive throughout this range.
- Littlewood's lemma in Section 4.2 counts analytic orders: an
  order-m zero contributes m times its horizontal distance in its
  zero sum. In the slab there is no pole, and multiplication by
  the holomorphic mollifier cannot remove a zeta zero. Thus the
  source's count majorization and its imported endpoint extension
  apply with orders. The endpoint argument above now explicitly
  distinguishes auxiliary zeros from zeta zeros.
- Compact finiteness and (4) give (5) exactly, including gamma=T
  excluded, gamma=2T included, coincident ordinates, beta=1/2 and
  arbitrarily small positive displacements. Reflection fixes each
  ordinate and preserves the order, so (6) holds on this same
  multiset; it does not require simplicity or pairing different
  ordinates. No lower bound for displacement is used.
- The chain rule gives (-i tau)i/(gamma+i y)=tau/(gamma+i y),
  with the positive exponent tau arg(gamma+i y) in the modulus.
  For the negative displacement segment the exponent is nonpositive;
  for the positive segment it is at most 1. Both have derivative
  bound 2e, also at tau=T and tau=2T. Reversing the integral for
  v<0 gives the same length |v|; v=0 contributes exactly zero.
- Consequently the factor is (2e)(2I(T))=4e I(T) for the full
  sum of absolute differences, before cancellation in E. Dividing
  the single tau-independent majorant by T log T yields exactly
  the four vanishing terms in (9). Thus the onset is common to
  every allowed real endpoint and tau, not a good-height onset.

Only the endpoint justification needed clarification: the source's
auxiliary extension is an imported part of (74), rather than a
consequence of avoiding zeta ordinates. The bound, constants and
conclusion survive unchanged. L018 is the only local mathematical
input; no new DAG edge or independent source reproof is needed.

## Mathlib

Full matching coverage of the integrated-density input and (3), with
these order and endpoint conventions, has not been checked; availability
is unknown. Holomorphic differentiation of the principal logarithm,
finite integration and the triangle inequality are supporting facts,
not a formalization of the analytic number-theory input. No absence
or Mathlib completion claim is made.
