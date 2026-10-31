# Weighted cubic feasibility: constant-candidate attempt

Work in progress, 29 October 2026. The approved target is exactly the
E_3 infimum in `literature/2026-10-29-saturation-weighted-cubic-feasibility.md`.
This is a mathematical attempt using that pre-existing EXPLORE assessment,
not a fresh literature comparison. No conclusion about the infimum is
assumed from testing one candidate.

Inputs: L477 (1)--(5), L481's exact F and finite mean-square estimate (3).
The first test is p=1, retaining its complete error
integral |R_T|/(1+|F|^6). A short/long coefficient split is being checked
to see whether the denominator buys a logarithmic saving. Neither a
weighted small-value estimate nor a uniform cubic lower bound is known.
Keep the chirped term and both interval endpoints throughout. No RH,
Haar transfer, phase independence or discarded exceptional set is used.

## Completed diagnostic calculation

This is the calculation log of an unsuccessful estimate, not a new
accepted lemma or input to the argument. The E_3 infimum is undecided.
Use arbitrary sufficiently large real T, L=log T, M=floor(sqrt(T/(2pi))),
N=floor(T^(1/24)). Eventually 1<=N<=M. All integrals below are over
the entire [T,2T]; no endpoint or exceptional set is removed.

For p=1 write q=1/(1+|F|^6) and E_const=integral |R_T|q.
Only 0<=E_3<=E_const follows from admissibility. Define

    D_j=sum_(n<=M)(log n)^j n^(-1/2-it), j=0,1,2,

with (log 1)^0=1. The exact identities
P_0=D_0, P_1=lambda D_0-D_1 and
P_2=lambda^2 D_0-2lambda D_1+D_2 give from L477 (1)

    R_T=2 Re(D_0 conjugate(D_2)-|D_1|^2)
          +2 Re(exp(2i theta)(D_0 D_2-D_1^2)).

The lambda cross terms in the first expression cancel after taking
real parts, and those in the second cancel algebraically. No derivative
or freezing of theta is involved. Split D_0=F+Q_0 with
Q_0=sum_(N<n<=M)n^(-1/2-it), retaining all D_1,D_2 terms. Put

    B(t)=2 Re(Q_0 conjugate(D_2)-|D_1|^2)
          +2 Re(exp(2i theta)(Q_0 D_2-D_1^2)),
    J=integral |B|q.

Exactly R_T-B=2 Re(F conjugate(D_2))+2 Re(exp(2i theta)F D_2).
Since r/(1+r^6)<=1 for r>=0 (check r<=1 and r>=1 separately),
the reverse triangle inequality and Cauchy--Schwarz give

    |E_const-J|<=4 integral |D_2|
                 <=4 sqrt(T)||D_2||_2.                 (a)

The precise imported mean-square estimate is Heap--Soundararajan,
*Lower bounds for moments of zeta and L-functions revisited*,
arXiv:2007.13154v1, Section 5, p. 9, equation (14) and preceding
calculation, in the arbitrary-finite-coefficient form of L481 (3):
[primary version](https://arxiv.org/pdf/2007.13154v1#page=9).
It applies on this actual interval with length M and squared
coefficient sum at most (log M)^(2j) sum_(n<=M)1/n<=C L^(2j+1).
Its error factor M log(2M)=o(T) is retained. Applying it also to
the coefficients supported on N<n<=M gives

    ||D_j||_2<=C sqrt(T)L^(j+1/2),
    ||Q_0||_2<=C sqrt(T)L^(1/2).

Thus (a) is O(T L^(5/2)), with constants and onset independent of
the fractional parts defining M,N. The chirped part is retained;
only its modulus-one phase is used. But the remaining available bound
is just

    J<=integral |B|
      <=4(||Q_0||_2||D_2||_2+||D_1||_2^2)
      <=C T L^3.                                      (b)

The error in (a) divided by the required scale T L^3 is
O(L^(-1/2)); the remainder estimate (b) divided by that scale is
only O(1), not little-o or a positive lower bound. The loss is
precisely replacement of q by one in (b). Suppression of explicit
F factors has not controlled the remaining weighted quadratic jets.

## Check of the proposed downstream use

For the exact signed saturation correlation let
C_sat=integral R_T |F|^6/(1+|F|^6). Since the saturation is 1-q,
L477 (5) gives

    |C_sat|<=|integral R_T|+|integral R_T q|
            <=C sqrt(T)+E_const.                       (c)

Therefore little-o success for this constant candidate along a sequence
would also force C_sat=o(T L^3) on that sequence. It could establish
approximation feasibility, but could not simultaneously yield the
proposed positive full-scale signed certificate. This does not exclude
a nonconstant cubic. Nor is (c) a lower bound for E_const without an
independently proved signed lower bound, which is unavailable.

## Outcome and stop

EXPLORATION: neither alternative for E_3 is proved; testing p=1 does
not control the infimum from below over T-dependent cubics. This makes
the unsuccessful estimate explicit but does not overcome the recorded
ordinary-moment/joint-weight mismatch. Do not promote these diagnostic
inequalities to an accepted lemma or claim progress beyond the assessed
established tools. Park this implementation. Reopening needs a new
actual-height weighted estimate or a coefficient-uniform cubic
separation argument, with coverage and a discriminating test. Neither
has been obtained. L481/L482's narrower stops remain intact.

The fixed-square L1 thresholds, negative mass, individual signs and RH
are unresolved. Mathlib matching is not checked; no absence claim.
The finite mean-square theorem is imported by the precise citation
above; other tools are finite algebra, reverse triangle and
Cauchy--Schwarz. No mathematical script or numerical evidence is used.
