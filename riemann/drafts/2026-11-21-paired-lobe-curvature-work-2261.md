# Paired-lobe curvature attempt2261: saved working state

Approved target: the exact family and fixed point in assessment2260.
Main gap: L030-L032/C032a actual-Xi all-degree mixed positivity.
This attempt tests only the proposed joint-density sufficient premise.
No parameter retuning, marginal-curvature calculation or new source
search is included. C919s is imported with its software contracts.

## Unfinished mechanism, not yet a theorem

Put P(t)=t^4+t^2, c=3a/2, W=V-P. For t>=0 one expects
0<=W<=sqrt(rho)(2t+3a), |W'|<=2sqrt(rho), and
W''=rho^(-1/2)[sech^2((t-c)/rho)+sech^2((t+c)/rho)].
At s=u+v=a/2 the alternating lattice is t_n=(n+1/2)a.
Only n=1 meets the positive curvature peak c; its coefficient in
the difference-series is negative. Thus the proposed limit is

    sqrt(rho) S''(a/2) -> exp(-P(3a/2))

uniformly for 2/3<=a<=7/10, with S the full alternating series.
If S converges uniformly to its positive base value and S' stays
bounded, the scaled determinant should tend to

    (1/2) S_0(a/2) exp(-P(3a/2)) > 0.

Still to justify: all derivative/exponential tails; differentiable
series with local uniform majorants; every uniform limit and positive
lower bound; and a choice a(rho) for which pi/a is the LEAST positive
cosine zero. For the latter use C919s's fixed frequency cell
[147/32,37/8], positive preceding compact interval, and strict
negative derivative; use a in[8pi/37,32pi/147] and the intermediate
value theorem after uniform F,F' perturbation bounds. No branch
differentiability or new-family root simplicity is assumed.

Stop if any required hypothesis or sign cannot be established for this
fixed family. A positive determinant would stop only generic joint
log-concavity of this density, not marginal preservation or RH.

## Completion2261

The saved mechanism is resolved in canonical C919t. It supplies exact
root alignment and a uniform positive scaled determinant, conditional
on C919s's explicit software contracts. The proposed generic joint
log-concavity premise fails; a separate conceptual audit is pending.
The sketch above is retained as working history, not a second proof.
