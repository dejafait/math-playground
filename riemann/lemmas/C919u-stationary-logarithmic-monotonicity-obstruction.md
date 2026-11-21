# Corollary919u: the stationary logarithmic source fails strict decrease

## Hypotheses

Use the conditional setting approved in literature assessment2264 and
source-gate review2265. Let K be positive, even and smooth on R, with
(log K)''<0 everywhere and, for every integer m>=0 and B>0,
exp(B|u|)|K^(m)(u)| tending to zero as |u| tends to infinity.
Suppose the cosine transform of K has a least positive real zero x;
its multiplicity is unrestricted. Conditionally suppose G is positive
and C2 on [0,infinity), with

    G''+x^2 G=x^2 K,  G'(0)=0,  G(u)->0 as u->infinity.       (1)

No generic existence, positivity, sine representation, even extension
or entire quotient identity is inferred from these assumptions.

The comparison being tested is specifically Theorem4.1 of M. Gallo,
R. Moraschi and M. Squassina, *Quantitative and exact concavity
principles for parabolic and elliptic equations*, Proc. Roy. Soc.
Edinburgh A, published online23September2026, DOI10.1017/prm.2026.10177,
equations(4.2)-(4.3), their restricted-interval qualification and
Remark4.3. Primary published source:
https://www.cambridge.org/core/journals/proceedings-of-the-royal-society-of-edinburgh-section-a-mathematics/article/quantitative-and-exact-concavity-principles-for-parabolic-and-elliptic-equations/A4D4DE35A8D20F122BBB36D4D2ECFA43 .
Use the stationary source independent of the time-derivative variable,
with leading coefficient +1 in -v''. No parabolic embedding is assumed.

## Conclusion

For v=log G the normalized equation is

    -v'' = B(u,v,v',0,t),
    B(u,s,q,r,t)=q^2+x^2-x^2 K(u) exp(-s).                  (2)

Here q is the spatial derivative variable and r the time-derivative
variable. For every finite u>0 and every real s,q,r,t,

    B_r=0,  B_s=x^2 K(u) exp(-s)>0.                        (3)

Consequently the hypothesis B_s+mu B_r<=-sigma<0 cannot hold for
any mu>=0, sigma>0 on any nonempty restricted solution-value
interval of the cited theorem. This includes singleton intervals;
the stationary time-derivative interval is itself the singleton [0,0].

This excludes only the specified direct stationary comparison. It
does not contradict the source theorem or rule out a differently
justified time-dependent problem. It proves neither a failure nor a
success of marginal log-concavity, actual-Xi applicability, repeated
zero removal, all-degree positivity or RH.

## Proof

### Literature input and reason for the specialization

The cited theorem uses a positive definite leading matrix in
-sum a_ij D_ij v=B. At a negative interior minimum of its weighted
concavity defect it requires B_r<=0 and B_s+mu B_r<=-sigma<0.
The latter need only hold at the middle spatial point, at the common
spatial gradient and on the two specified value intervals. We import
only these hypotheses, not any global conclusion or boundary result.
The theorem and its proof were inspected in source notes2264; its
equations(4.1)-(4.3) and restricted intervals were checked directly in
the published HTML on21November2026 for this calculation.

This is a chain-rule specialization of that source condition, not a
reproof of a maximum principle. It is necessary because the source
does not evaluate the logarithmic forcing in (1). Assessment2264's
coverage is reused. C919s's fixed quartic point calculation and
C919t's paired-density obstruction are comparisons only: neither is
a mathematical premise here, nor do their numerical contracts enter.

### Normalize both terms before taking the partial derivative

Positivity and C2 regularity of G give v in C2 and

    G'=exp(v)v',  G''=exp(v)[v''+(v')^2].

Divide (1) by exp(v)>0 and rearrange to obtain

    v''+(v')^2+x^2=x^2 K exp(-v),
    -v''=(v')^2+x^2-x^2 K exp(-v).

This proves (2) with a_11=1>0. The oscillatory term contributes
+x^2; the forcing contributes -x^2 K exp(-s). Partial
differentiation holds u,q,r,t fixed, rather than differentiating along
the solution u->v(u). It gives exactly (3). The strict sign follows
from x>0, K(u)>0 and exp(-s)>0. Increasing mu cannot affect it,
because B_r is identically zero.

### The theorem's actual restricted intervals

Write u2=(1-lambda)u1+lambda u3, with finite interior spatial
points and lambda in [0,1]. To express the stationary comparison in
the theorem's notation put v(u,t)=v(u). If a negative interior
minimum of the weighted concavity defect exists, its middle value
and interpolated endpoint value satisfy

    c=v(u2),  d=(1-lambda)v(u1)+lambda v(u3),  c<d.

The theorem's restricted intervals are precisely

    s in [c,d],
    r in [v_t(u2,t),(1-lambda)v_t(u1,t)+lambda v_t(u3,t)]
      =[0,0].                                             (4)

All solution values are finite. Whatever the common spatial gradient
q may be, for every s in [c,d] and every mu>=0,

    B_s(u2,s,q,0,t)+mu B_r(u2,s,q,0,t)
      =x^2 K(u2) exp(-s)
      >=x^2 K(u2) exp(-d)>0.                               (5)

The required upper bound is -sigma<0, so (5) rules it out even on
these restricted intervals. The same estimate applies if c=d:
evaluation at that single value still gives a positive derivative.
A negative defect supplies c<d, but no artificial empty-interval or
singleton exception can repair the sign. No existence of such a
minimum is asserted; (5) is conditional on any triple to which the
theorem would be applied.

Neither the boundary conditions nor log-concavity, evenness, decay
or the first-zero property beyond x>0 were used in this obstruction.
They cannot change the pointwise partial derivative in (3).
Remark4.3's repair uses a source containing a time-derivative term;
our B contains none. Inserting such a term changes the prescribed
representation and needs a separate argument. We make no claim
about that alternative, any source-concavity sign or half-line
boundary control. The decisive test in assessment2264 therefore
stops this direct stationary application.

## Mathlib

Full matching coverage for this conditional obstruction and for the
cited concavity principle is unchecked, not asserted absent. Only
the ordinary chain rule, positivity and the derivative of exp are
used in the specialization; no Lean verification is claimed.
