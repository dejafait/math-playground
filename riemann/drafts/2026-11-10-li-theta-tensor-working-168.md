# Complete Li/theta tensor transfer — step168 working record

The supplied step167 EXPLORE assessment covers this attempt, with its
exact target unchanged. Main gap: actual-Xi all-degree mixed positivity.
Intermediate test: one common boundary-payment rule for L966(15) at
n=2,3, keeping every even block and distant h term. A successful rule
would sign only the prescribed regularized observable; all-n closure
and L964's margin-dependent eta scope would still be unpaid.

Read L019-L020 and L966 in full, L964's hypotheses/normalization, and
L242/L044/L046 and the named step391 stop as contrasts. Reuse the
supplied source assessment; no new literature or cross-notebook input.
Existing uncommitted notebook work is preserved.

## Partial reasoning saved before further work

Write Delta=h-1/4. Since d_u^2 H_r=x H_r+r H_(r-1), integration by
parts should give

    I_r(x)=delta_(r,0)/2
             + integral A(u)[2(x-1/4)H_r(x,u)+2rH_(r-1)(x,u)]du.

The r=0 second summand is interpreted without H_(-1). The origin
derivative of H_r is zero; the nonzero boundary is -2A'(0)H_r(x,0).
All infinity limits, products and intersections still need a complete
write-up. In particular I_0(b)=1/2: zero-order b factors become origin
faces, rather than disappearing.

Tentative n=2 coefficients: d_1=4h^2/Delta^2, d_2=h/Delta.
Tentative n=3: d_1=h(3Delta+1)^2/Delta^3,
d_2=h(6Delta+1)/Delta^2, d_3=h/Delta.
These will be checked exactly against L966(2).

Proposed single common grouping: spread each origin mass 1/2 using
the actual positive profile A(u)cosh(u/2), normalized to that mass.
If a_0=integral A(u)cosh(u/2)du and c=1/(2a_0), its density relative
to A du is c H_0(b,u). Thus replace a zero-order b factor by cH_0(b,u),
a positive-order b factor by 2rH_(r-1)(b,u), and the h factors by
cH_0(b,u)+2Delta H_0(h,u) or 2H_0(h,u)+2Delta H_1(h,u).
This converts all origin strata into one common absolutely continuous
integral without dropping their mass. Test the fully symmetrized
kernel on the long ray (t,0,...,0). The h-derivative carries a factor
t exp(sqrt(h)t), while the h zeroth factor has no t and the other
placements have only polynomial times exp(t/2). This suggests a
strict negative tail, not yet a completed proof or sign certificate.

Continue only with a proved common payment rule and an all-n mechanism,
or stop this grouping with a rigorous obstruction. A negative kernel
region would refute only pointwise payment by this profile, not the
integrated inequality, Li positivity or RH. No numerical preview will
be treated as verification.

## Completion

The tentative coefficients and full transfer were checked exactly.
The canonical proof is
[L967](../lemmas/L967-li-theta-tensor-boundary-spreading-obstruction.md);
it includes every origin/intersection contribution and all convergence
conditions. The proposed reference-profile compensation is now stopped:
its fully symmetrized kernel has a strictly negative ray limit at both
test orders. This supplies no negative integral and leaves L966(16)
open. The full exact certificate is
`scripts/li-theta/tensor-boundary-check-168.json`. A separate independent
audit is nominated with REVIEW_REQUIRED; no further mechanism was
attempted or approved in this turn.
