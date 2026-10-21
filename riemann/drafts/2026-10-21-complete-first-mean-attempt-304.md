# Complete first-mean attempt — step 304

Completed: the full proof and qualifications are now in
`lemmas/L451-complete-first-mean-temporal-defect.md`. The response probe
has a strictly positive complete residual for every sufficiently large
real H. The saved preliminary reasoning below is retained as such;
L451 is canonical and a separate critical audit remains pending.

The approved target is the unchanged L449 law's temporal x identity.
The main gap is global mixed positivity; this attempt tests only a
necessary realization condition. Reuse the supplied SPECIALIZE
assessment, without changing the law or the original L429 stages.

Saved reasoning before full write-up: use a fixed C1 cutoff eta supported
strictly inside (1,2), of integral one, and phi_H(t)=eta(t/H)h(t)/L(t),
where a+ih=R zeta(5/2+it). L440 (13) gives
h'/L=a/2+O(1/log H). L438's complete mean differs in normalized L1
from d_H b/|b|^2 by O(1/log H): the high first absolute moment is
O((log H)^(-5)) by its mass/second-moment bounds, both intermediate
first moments are O(1/log H), and the bulk mass loss is smaller.
Moreover d_H=-b0+O(1/log H). L449 preserves this mean exactly.

L419 gives b=c(a/4,-h,-a)+O(1/log H). The proposed full residual
therefore has principal term (d_H/c) E_H eta(t/H) g(alpha(t)), with
g(theta)=[cos(theta)^2/8-sin(theta)^2]/
[(17/16)cos(theta)^2+sin(theta)^2]. L440 (14) applies to this fixed
smooth angular function after subtracting its circle mean. That mean
is strictly negative: it is at most 1/16-8/17=-111/272.

Continuation/abandonment test: verify the complete absolute remainder,
strict interior support, exact test derivative including L', and the
real-H uniform phase bound. A nonzero limiting full residual decides
failure; a jump in an individual atom is not evidence. This approach
does not need any actual critical-jet crossing or derivative of the
selected atoms. Full proof and final status will be canonicalized only
after these checks. No mathematical script or numerical claim is used.
