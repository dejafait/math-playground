# Adjoint-difference attempt1847 — working checkpoint

Approved target: assessment1846, exactly C034c(20), widths [1,2].
Main gap: L030-L032/C032a actual-Xi all-degree positivity. The local
curvature bound could pay C034b's final ECT prefix using C034c's cubic
margin; conditioning, weights, full observations and Xi transfer remain.
Reuse source-notes1846/1842 and stops1839/1843; no source refresh.

20 November2026, unfinished reasoning saved before the bounded test:
write D=Q_2-Q_1 and a(x)=p(x)-p(0),
v(x)=p(x)-p(0)-p''(0)x^2/2. Formal candidates to justify are

    D=-4 d/dx [x/((x^2+1)(x^2+2))], integral D=0,
    h=integral p D=integral a D,
    h'=integral p D''=integral v D'',
    e_1=integral v Q_1'',
    C=integral integral a(x)v(y)
                    [Q_1(x)D''(y)-D(x)Q_1''(y)] dx dy.

The singular Q_1 companion requires v, not a, after two integrations
by parts. At zero v=O(x^4); Q_1''=O(x^-4). At infinity v contains
its quadratic subtraction. Every boundary, absolute memberwise sum,
independent divisor pair and width-uniform limit still needs checking.
No global Sobolev assumption or arbitrary finite part is allowed.

Next part of this same attempt: inspect the signed rational joint
kernel and compare its possible bound with S4^3/5. An identity alone,
unsigned independent hull or unpaid sign parks the mechanism. Nothing
in this checkpoint proves the threshold or authorizes a new target.

Completion: the canonical proof and signed kernel test are now in
C034d; the full threshold remains unpaid. See stop1847 and history1847.
This working checkpoint preserves the original unfinished reasoning;
it is not an independent audit or a second canonical proof.
