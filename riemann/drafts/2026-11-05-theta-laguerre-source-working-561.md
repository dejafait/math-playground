# Step561 source comparison — preserved early checkpoint

Finalized in
[the completed source assessment](literature/2026-11-05-theta-laguerre-uniform-oscillatory-localization.md).
The notes below preserve the state before final source comparison;
their pending items are historical, not current task instructions.

Literature-only target is the supplied uniform oscillatory localization
assessment. L019/L021/L795 were read in full. Existing notebook changes
are preserved. No lemma, mathematical script, or new estimate is written.

Inspected: NIST DLMF 18.15(iv), formulas 18.15.14–23 and their domains.
The elementary expansion is compact-argument only; Bessel 18.15.19
covers scaled argument t in [0,1-delta], Airy 18.15.22 covers
[delta,infinity), for fixed alpha and fixed truncation order. Both
errors are additive envelope bounds, not relative signed errors.
For L795 the dictionary to check is n=d, alpha=-1/2,
nu=4d+1, z=u^2*x/4, t=z/nu. This is notation matching only.

Frenzen–Wong (1988), DOI 10.1137/0519087: publisher PDF request
redirects to abstract/access page; full proof not inspected. Do not
attribute a read of its explicit remainder integrals. Temme (1990),
*Asymptotic estimates for Laguerre polynomials*, ZAMP 41, 114–126,
https://ir.cwi.nl/pub/2379/2379D.pdf, section 2, pp.115–117, was read
as an author-written summary of Frenzen–Wong, not the original proof.
It confirms fixed alpha>-1 and overlapping Bessel/Airy domains.
Do not use its section 3 nonnegative-alpha formulas at alpha=-1/2.

Pending final record: distinguish fixed-degree integrability from
degree-uniform relative sign control. No signed margin or independent
barrier is supplied by these sources. A possible narrower continuation
is to test absolute theta-support localization in a specified logarithmic
window, relative to a positive exponential envelope; that would pay only
a complement at the envelope scale and would not establish a sign.
No bound or readiness claim for that continuation has yet been made.
