# Lemma 580: the uncorrected bounded bulk fails quartic stationarity

## Hypotheses

Let C2(R;R) have the topology of local uniform convergence of a function
and its first two derivatives. Let F be a Borel random element of this
space whose law is invariant under every translation
T_s f(t)=f(t+s), s in R. Assume

    E(|F(0)|^4+|F'(0)|^4+|F''(0)|^4)<infinity.                 (1)

For the finite-law application, use exactly the uncorrected B of L473
Section 4 (11)--(13). Its first three coordinates are

    B_0=(epsilon,v,k epsilon),

where epsilon, v and k are independent, epsilon is uniform on {+1,-1},
k=1/12 with probability 1/6 and k=-7/60 with probability 5/6, and
v=0 with probability 1/2 and v=+/-1/sqrt(6) with probability 1/4 each.
The remaining three coordinates of B have the conditional construction
specified in L473; their values are not used in this first-marginal test.

No actual-Hardy stationarity, height limit, full-fourth realization,
RH, simplicity or zero-free premise is assumed. In particular B is not
L473's corrected total law nu_H.

## Conclusion

Every path law under (1) satisfies the necessary identity

    E[F(0)^3 F''(0)+3F(0)^2 F'(0)^2]=0.                       (2)

In contrast the stated finite marginal has the exact defect

    E[B_(0,0)^3 B_(0,2)+3B_(0,0)^2 B_(0,1)^2]=1/6.           (3)

Thus no translation-invariant Borel C2 path law can have B_0 as the
distribution of (F(0),F'(0),F''(0)). Consequently none can have B as the
joint distribution of its ordinary jets at 0 and 1. The first-marginal
equality itself would imply (1), so no additional moment escape is left
for this exact law. This conclusion does not reject a corrected or
rare-component law, general stationary feasibility, actual-Hardy
realization, or any RH statement.

## Proof

### Imported deterministic identity and the specialization needed

The deterministic input is the chain rule and fundamental theorem of
calculus, in the finite-interval transport form of J. B. Lasserre,
D. Henrion, C. Prieur and E. Trelat, *Nonlinear optimal control via
occupation measures and LMI-relaxations*, SIAM J. Control Optim. 47
(2008), 1643--1666, Sections 2.1--2.3, (2.7),(2.10)--(2.12), printed
pp. 3--5 of the inspected [arXiv v1](https://arxiv.org/pdf/math/0703377v1),
[DOI](https://doi.org/10.1137/070685051). Only the necessary transport
identity (2.12), retaining both endpoints, is used. Its compact state
setting applies separately to each continuous trajectory on [0,1];
no fixed compact box uniform over random trajectories is assumed.

For the unbounded-law integrability comparison, D. Henrion, M. Korda,
M. Kruzik and R. Rios-Zertuche, *Occupation measure relaxations in
variational problems: the role of convexity*,
[4 March 2023 manuscript](https://optimization-online.org/wp-content/uploads/2023/03/convexcov-1.pdf),
Definitions 2.4/2.7, (6)--(8), printed pp. 3--4, and Lemma B.1 with
proof, pp. 17--18, give the finite-p state/derivative integrability
framework. Here p=4, the state is (F,F'), control F'', and the test is
phi(x,y)=x^3 y. Neither source supplies a realization theorem for this
finite law. The expectation specialization is written out below because
the source identity alone does not justify stochastic interchanges.
The identity is known mathematics; the local work is its stated
specialization and the finite-law evaluation, with no novelty claim.

### Pathwise identity, measurability and all integrability steps

Derivative evaluation f -> f^(j)(s), j<=2, is continuous on C2(R;R).
Translation invariance of the Borel path law therefore implies that
(F(s),F'(s),F''(s)) has the same distribution as the jet at zero for
every real s. Joint evaluation (s,f) -> f^(j)(s) is continuous in this
topology. All random integrands below are consequently jointly measurable.

For any individual path f in C2(R;R), f and f' are C1 and bounded on
[0,1], and f'' is continuous and bounded there. The ordinary chain rule
and fundamental theorem give

    f(1)^3 f'(1)-f(0)^3 f'(0)
      =integral_0^1 [f(s)^3 f''(s)+3f(s)^2 f'(s)^2] ds.        (4)

No derivative of f'' is taken. The pathwise compactness needed for the
source's deterministic formulation follows from these bounded ranges;
(4) itself is the elementary transport identity for this trajectory.

Write X_s=F(s), Y_s=F'(s), Z_s=F''(s). Young's inequalities imply,
for every real x,y,z,

    |x^3 y| <= (3/4)|x|^4+(1/4)|y|^4,
    |x^3 z+3x^2 y^2|
      <= (9/4)|x|^4+(3/2)|y|^4+(1/4)|z|^4.                 (5)

Indeed |x^3 z|<=(3/4)|x|^4+(1/4)|z|^4 and
3x^2 y^2<=(3/2)(|x|^4+|y|^4), which gives the second bound.
Stationarity of the complete jet and (1) make the expectations of the
right sides finite and independent of s. The first bound proves that
both boundary random variables in (4) are integrable. Tonelli applied
to the absolute integrand, followed by the second bound, gives

    integral_0^1 E|X_s^3 Z_s+3X_s^2 Y_s^2| ds < infinity.      (6)

Thus Fubini legitimately interchanges expectation and the integral
in (4). The two boundary expectations agree by stationarity of
(X_s,Y_s), so their difference is zero. The expectation of the
integrand is independent of s by stationarity of all three jets and
its established absolute integrability. The interval length is one;
therefore the expectation of (4) is exactly (2). No differentiation
under an expectation or unproved local uniform domination is used.

### Exact defect and the scope of the obstruction

For the specified first marginal, epsilon^2=epsilon^4=1 gives

    (epsilon)^3(k epsilon)+3(epsilon)^2 v^2=k+3v^2.

Its complete expectations are

    E k=(1/6)(1/12)+(5/6)(-7/60)=1/72-7/72=-1/12,
    E v^2=(1/4)(1/6)+(1/4)(1/6)=1/12.

Consequently the defect is -1/12+3/12=1/6, proving (3).
Every coordinate of B_0 has absolute value at most one; hence a
hypothetical path law with this first jet marginal automatically
satisfies (1). Equations (2) and (3) contradict each other. If its two
jets had law B, its first jet would have law B_0, so that extension is
also impossible. The construction of B's other coordinates cannot
repair a constraint on this first marginal.

Only the uncorrected bulk has been evaluated. A rare component may
carry fourth moments of substantial size despite small probability,
and a covariance correction can change this quartic observable.
Neither is omitted from any claimed total-law conclusion: there is
no such conclusion here. Likewise finite-interval sampling of actual
Hardy jets retains endpoints in (4); it is not the invariant path-law
hypothesis used for the cancellation. No endpoint estimate or
actual-Hardy/Xi transfer is proved.

## Mathlib

Coverage of the full stationary-path statement and this exact finite-law
application is not checked. Chain rule, fundamental theorem, Young's
inequality and Fubini are the named mathematical inputs above; no
matching Mathlib theorem is claimed. Unknown coverage is not evidence
of absence.
