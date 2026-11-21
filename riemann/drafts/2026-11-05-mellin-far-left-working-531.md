# Far-left Mellin attempt — working checkpoint, step531

Approved target: the exact T_F bound in the unchanged SPECIALIZE
assessment `drafts/literature/2026-11-05-mellin-far-left-horizontal-segment-test.md`.
Main gap: actual-Xi all-degree mixed positivity. One far-left contour
component could support later assembly; no sufficient sign implication
or global contour identity is assumed.

Read the supplied overview/DAG/assessment and the relevant L797–L799,
L802 proofs and step530 source comparison; preserved existing changes.
The old global-import source stop remains in force.

Work in progress, not yet a result: for h>0 write s=sigma+i t and
y=y_L>=h>0. The logarithmic derivative of
W(v)=|exp(2s Log(v+i y))| is
2(sigma v+t y)/(v^2+y^2). If sigma>=0 its numerator is positive.
If sigma<0 and v<=u, it is at least sigma u+t h
=|x|^2 Re(q-c)>0, using L802's Re(q-c)>0 and t>0.
Check every sign and the h=0/conjugate cases before using this.
This suggests W(v)<=W(u/2) on the whole far-left interval without
claiming phase concavity there.

Remaining obligations: a complete-series bound for P on 0<=v<=u/2
with constants polynomial in u; h=0 improper convergence from
s=u(Q-c)>0; exact phase comparison at u/2 using L802's tangent
bound, including the removed theta exponential; normalization and
uniform payment of 600u^(5/2)sqrt(47Q/(20pi))(1+10u/Q)e^(-Q/(20u)).
No mathematical script or numerical evidence is needed at this stage.
Continue only with a full proof or a rigorous method obstruction.

Analytic completion candidate, to be written out and checked: with
K=cos(2y_L)>1/(5u), tau=pi K exp(2v), splitting each Gaussian
exponent in half and comparing the remaining decreasing sum to its
integral gives sum n^4 exp(-tau n^2)<4tau^(-5/2) and
sum n^2 exp(-tau n^2)<2tau^(-3/2), for every tau>0.
Consequently |P(v+i y_L)|/(4pi^2)<28u^(5/2)exp(-v/2).
The monotone W then reduces the entire integral to 56u^(5/2)W(u/2).
L802's endpoint tangent inequality gives
phi(u/2)<=-(85/48)Qd^2-(105/256)(Q/u)(v_L-u/2).
Adding tau(u/2)<=Q exp(-u) and dropping -9u/4 gives a loss
at least [805/4096-1/14]Q=(1/8+3/28672)Q>Q/8.
This would prove the stronger allowance
56u^(5/2)sqrt(47Q/(20pi))exp(-Q/8).
The h=0 endpoint has s=u(Q-c)>0, so v^(2s) tends to zero;
for h!=0 the endpoint lies inside the principal-Log domain.
This remains a local component, not an RH candidate or an audited result.

Completion: the full argument, with all parameter cases and exact
normalization, is now canonical in L803. This working record preserves
the reasoning before completion; it is not the proof or an audit.
