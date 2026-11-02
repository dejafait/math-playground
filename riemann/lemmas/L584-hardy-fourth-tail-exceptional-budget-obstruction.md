# Lemma 584: the specified Hardy closure fails the exceptional fourth-energy budget

## Hypotheses

Use the real Hardy function Z, with |Z(t)|=|zeta(1/2+it)| for
real t>=0. For each sufficiently large real H, let ell=log H,
P=H ell+1, and use exactly L582's real C2 periodic function g:

    g(s)=Z(H+s/ell), 0<=s<=H ell,

with its prescribed unit quintic bridge. Use exactly L583's definitions
of V_g, a, M_P a, E and E_pair, its Euclidean six-coordinate norm,
lambda=ell^2/256, and normalized integral <f>=P^(-1) integral_0^P f.
No bound from L583 hypothesis (1) is assumed.

Import Louis-Pierre Arguin and Nathan Creighton, *Lower bounds for
the large deviations and moments of the Riemann zeta function on the
critical line*, arXiv:2603.01711v1, 2 March 2026,
[Theorem 1.1, p.2](https://arxiv.org/pdf/2603.01711v1#page=2),
[primary HTML](https://arxiv.org/html/2603.01711v1): for fixed alpha>0,
V~alpha log log T and all sufficiently large T,

    T^(-1) meas{t in [0,T]: log|zeta(1/2+it)|>V}
      >= K_alpha integral_V^infinity
           exp(-y^2/(log log T))/sqrt(log log T) dy,       (1)

where K_alpha>0. Only alpha=2 and V=2 log log T are used.
There is no RH premise. Section 1.4 specifies uniform sampling on
[0,T]; this is not a dyadic theorem.

The manuscript theorem is imported as stated, without an independent
proof audit. Its displayed (2.19) has the squared-denominator discrepancy
recorded in the source assessment, relative to (1.7) and the following
unnumbered formula. This proof neither uses (2.19) nor repairs or
certifies the manuscript's arithmetic argument. The conclusions below
retain this source qualification. L473/L582's other arithmetic-source
qualifications are unchanged; their moment estimates are not needed
for this obstruction. The Hardy identity above is also recorded in
L473's cited Bui--Hall Hardy conversion.

## Conclusion

Define the nonnegative scalar tail and exact periodic energy by

    R_4(H)=H^(-1) integral_H^(2H)
            |Z(t)|^4 1_{|Z(t)|>(log H)^2/256} dt,
    Q_4(H)=<1_E_pair (|V_g|^4+lambda^4)>.

Then

    limsup_(H->infinity) R_4(H)/(log H)^3=+infinity,       (2)
    Q_4(H)>=H ell/(H ell+1) R_4(H),                      (3)
    limsup_(H->infinity) Q_4(H)/(log H)^3=+infinity.       (4)

In particular, no finite B_4 can satisfy L583's fourth inequality (1)
on an eventual ray for this specified g and exceptional set. This
invalidates that sufficient uniform-budget route for this g, leaving
L583's conditional theorem intact. It does not rule out other
truncations, moment-preserving laws or support mechanisms. No
all-height scalar lower bound, second-budget obstruction, positive
clipping, Xi sign or RH conclusion is asserted. This is a reproduction
of an elementary application of the cited theorem, with no claim of
originality beyond the checked sources.

The separate critical application audit below passes without a change
to the argument. It verifies only the local implications of the stated
manuscript theorem; the arithmetic source proof remains unaudited.

## Proof

### Cumulative fourth energy from the cited unweighted tail

Put q=log log T and assume q>=1 and T beyond the source onset for
alpha=2, V=2q. Restricting the nonnegative integral in (1) to
[2q,2q+1] gives

    integral_(2q)^infinity exp(-y^2/q)/sqrt(q) dy
      >= exp(-(2q+1)^2/q)/sqrt(q)
      = exp(-4q-4-1/q)/sqrt(q)
      >= exp(-5)(log T)^(-4)/sqrt(q).                    (5)

The integrand is decreasing on this positive interval, whose length
is one. Let c=K_2 exp(-5)>0. Since exp(2q)=(log T)^2, the event
in (1) at this V is precisely |Z(t)|>(log T)^2. On that event
|Z(t)|^4>(log T)^8. Hence the finite integral

    C(T)=integral_0^T |Z(t)|^4 1_{|Z(t)|>(log T)^2} dt

satisfies

    C(T)>=c T (log T)^4/sqrt(log log T).                 (6)

Hardy Z is continuous on every compact real interval, so no
integrability issue arises at bounded t or at its zeros. The strict
source threshold is preserved. There is no weighted-tail theorem,
limit interchange or source-proof rederivation here.

### An eventual uniform dyadic budget contradicts (6)

Suppose for contradiction that there are finite B>=0 and H_0>=e
such that

    R_4(H)<=B(log H)^3 for every real H>=H_0.             (7)

For an integer n>=1 put T=2^n H_0 and H_j=2^j H_0 for
0<=j<n. These intervals [H_j,2H_j] partition [H_0,T], up to
endpoints of measure zero. For every such j,

    (log T)^2 >= (log H_j)^2 > (log H_j)^2/256.

Thus the global event used in C(T), restricted to that interval,
is contained in the local event used in R_4(H_j). The comparison
has the direction required for an upper bound on C(T). With the
fixed finite constant D=integral_0^(H_0) |Z(t)|^4 dt, it follows that

    C(T)<=D+sum_(j=0)^(n-1) H_j R_4(H_j)
         <=D+B sum_(j=0)^(n-1) H_j(log H_j)^3
         <=D+B (T-H_0)(log T)^3
         <=D+B T(log T)^3.                              (8)

No assertion of (6) on a dyadic interval was made. Combining (6)
and (8), for all sufficiently large integers n, gives

    c log T/sqrt(log log T) <= B+D/[T(log T)^3].          (9)

The left side tends to infinity along T=2^n H_0, whereas the right
side tends to B. This is impossible. Thus (7) fails for every B and
every eventual onset. Since R_4(H)/(log H)^3 is nonnegative, failure
of every eventual finite upper bound is exactly (2). This yields
arbitrarily large violating heights, not a lower bound at every height.

### The exact exceptional-set and period comparison

Fix H and s. The periodic function a=|g|+|g'|+|g''| is continuous.
Consequently

    lim_(rho->0+) (2rho)^(-1) integral_(s-rho)^(s+rho) a(u) du=a(s).

Taking the supremum over all positive radii in L583's definition
therefore gives M_P a(s)>=a(s)>=|g(s)|. In particular,

    {|g(s)|>lambda} subset E subset E_pair.             (10)

The norm |V_g(s)| contains the lag-zero value coordinate g(s), so
|V_g(s)|^4>=|g(s)|^4. Pointwise nonnegativity gives

    1_E_pair(s)(|V_g(s)|^4+lambda^4)
      >=1_{|g(s)|>lambda}|g(s)|^4.                      (11)

Restrict its integral to the unchanged segment [0,H ell]; discarded
bridge and derivative/lag terms are nonnegative in this exact
integrand. Substituting t=H+s/ell, so ds=ell dt, proves

    Q_4(H)>=ell/P integral_H^(2H)
                  |Z(t)|^4 1_{|Z(t)|>ell^2/256} dt
           =H ell/(H ell+1) R_4(H).                     (12)

This proves (3) with the exact normalization. For H>=e the factor
is at least 1/2, and it tends to one. Equations (2) and (12) imply
(4). Equivalently, an eventual bound Q_4(H)<=B_4 ell^3 would imply
R_4(H)<=2B_4 ell^3, contradicting (2). This completes the bounded
application without assuming the disputed budget.

### Separate critical application audit — 2026-10-31

The approved scope is
`drafts/literature/2026-10-31-l584-tail-application-audit-scope.md`.
Read the entire application and checked its exact definitions against
L582 and L583. Reopened the versioned primary HTML, Theorem 1.1 (1.1)
and Section 1.4. The theorem concerns the strict event on [0,T], for
fixed alpha>0 and V asymptotic to alpha log log T. Thus alpha=2 and
V=2 log log T are admissible, with one positive constant K_2 and one
eventual onset. No assertion for an H-dependent alpha, a dyadic interval
or an effective onset is used. The retained (2.19) discrepancy is not
an input to any local step.

For (5), on the positive unit interval the integrand is decreasing;
its endpoint exponent is -4q-4-1/q, at least -4q-5 for q>=1.
The fourth weight on the strict source event exceeds (log T)^8,
giving (6) with c=K_2 exp(-5)>0 independent of T. Bounded-interval
continuity of Z makes C(T), R_4(H) and the fixed initial integral D
finite. Values at zeros do not contribute to any strict positive
cutoff event; no logarithm at a zero is needed in these integrals.

For (7)--(9), the putative eventual bound is for every real H, hence
for each H_j=2^j H_0. The global cutoff is larger than each local
cutoff, so its indicator is bounded above by the local indicator.
The finite partition has sum_j H_j=T-H_0 exactly; its shared endpoints
have measure zero. D is fixed after choosing H_0 and does not depend
on T. Therefore division by T(log T)^3 yields exactly (9), whose two
sides have the stated incompatible limits along T=2^n H_0. No infinite
sum, dyadic lower-tail import or interchange is used. The negation of
an infinite limsup for this nonnegative ratio would give some finite
eventual upper bound, which (9) excludes. This proves the unbounded
limsup and does not prove divergence, or a lower bound at every H.

For (10)--(12), L582 supplies the actual continuous periodic jets,
including both bridge joins. Centered averages of continuous a tend
to a(s); the supremum over all positive radii is consequently at least
a(s). Its strict superlevel set contains {|g|>lambda}. Measurability
also holds: each fixed-radius average is continuous, so their supremum
has open strict superlevel sets. L583 defines E_pair to contain E,
and its Euclidean norm contains precisely the lag-zero value coordinate
g(s). Thus every inequality in (11) is pointwise, with no lag
independence, cancellation or removal of a signed term. Restricting to
the unchanged segment discards only nonnegative terms. The substitution
ds=ell dt gives ell/P times the unnormalized Hardy integral, namely
(H ell/P)R_4(H), not R_4(H) without a period factor. For H>=e this
factor is at least 1/2. An eventual B_4 bound would therefore imply
the excluded eventual 2B_4 bound for R_4.

All local implications pass with no repair. The result remains
conditional on the stated manuscript input. Neither L583's budgets
nor L473/L582's arithmetic moment estimates were used to prove the
obstruction. The audit verifies the recorded route stop, not the
source proof, the second budget, other support constructions, positive
clipping, actual-Xi transfer or RH. No new mathematical result beyond
the checked source application is claimed.

## Mathlib

Full matching coverage is not checked. No Mathlib theorem is claimed
for the cited large-deviation input or its Hardy-periodic specialization;
unknown availability is not evidence of absence. The remaining local
steps use elementary Gaussian-integral comparison, finite dyadic
partitions, continuity of centered averages and change of variables.
