# Common-scale two-component replacement — working checkpoint

7 November 2026. Invocation-start coverage is the unchanged EXPLORE
assessment `literature/2026-11-07-paired-fiber-finite-replacement-test.md`.
The exact approved target is its finite coupled two-fiber replacement.
No new source or cross-notebook input is used. Existing notebook changes
are preserved.

The main gap is L030-L032/C032a actual-Xi all-degree mixed positivity.
The intermediate test changes both components on one common shrinking
scale at the two clean fibers. A strict full-mass decrease could exclude
that conditional configuration from a minimizer, if a minimizer exists.
The test requires the whole mass, all collars, an actual-G remainder and
nonzero endpoint J; a negative trace coefficient alone is insufficient.

Read L847's actual form, L879's phase line and radial variation argument,
the needed L889 endpoint identity and the full L890 finite-shear proof.
Reused the parent source comparison and read attempt65/69/78. L887's
fixed-field logarithm and L890's fixed positive shear cost are not
uniform over shrinking supports. Neither supplies this test's sign.

At a fiber point (gamma,y0), write A0=[[p,0],[n,k]],
J0=(1-ip)(1-ik), and h=partial_x s != 0. For a fixed smooth compact
V=(V1,V2) in rescaled coordinates (X,Y), the proposed endpoint is
u_epsilon=u+epsilon*V((x-gamma)/epsilon,(y-y0)/epsilon).
Its candidate leading full density is

    epsilon*lambda*h * ((p+i)*X+V1)/(p+i)
        * det(I-i(A0+DV))/J0.

This is unfinished reasoning, not a proved mass sign or accepted input.
The nominated profile is V1=a*chi(X,Y), V2=b*Y*chi(X,Y), with both
components and their complete cutoff derivatives retained. Need a
strict sign or an informative scoped obstruction for its full integral,
then a uniform actual-data remainder and endpoint determinant check.
Disjoint small neighborhoods do not test interaction across the fixed
positive separation between the fibers.

Independent gaps remain: configuration realization, a mass minimizer
and compactness, other contacts, L868's sharp bound, higher signs and
Xi transfer. No mathematical script or new lemma has yet been written.

## Analytic result in progress

The bounded profile is now fixed: eta(t)=exp(-t^2/(1-t^2)) on (-1,1),
zero outside; chi=eta(X)eta(Y); V=(chi,-Y*chi). At p=k=1,n=0,
J0=-2i. Write phi=chi+Y*chi_Y. The full model Jacobian has
real part r=phi-(1-chi)chi_X and imaginary part t=-2+phi-chi_X.
Thus r-t=2+chi*chi_X. In fact sup|chi*chi_X|<1, so |J|>1/sqrt(2)
on the entire square, including all collars.

For q={chi+i(2X+chi)}*(r+it)/4,
Re q = X+chi/2+chi^2*chi_X/4+X*chi_X/2-X*phi/2.
Let K_j=integral_{-1}^1 eta(Y)^j dY and
E=integral(|q|-sign(X)*Re q). Exact integration gives the signed
interface term I=-K_3/6 and full coefficient m=E+I.
On [-a,0]x[-1,1], E>=2 integral Re q. Hence

    m >= -2a^2+a*eta(a)*K_1-eta(a)^3*K_3/6.

At a=1/4, eta(a)>14/15, eta(a)^3<5/6, K_3<=32/35,
and K_1>13/12 suffice to give m>1/1260. A finite elementary
exponential-series estimate proves K_1>13/12. This is a full
integral lower bound, with no excluded neighborhood or unpaid collar.

The one floating diagnostic agrees (m about 0.590534, E about 0.733012,
I about -0.142478), but is explicitly not a sign or endpoint certificate:
`scripts/actual-g-radial-graph/common-scale-profile-diagnostic-79.json`.
Next within this same attempt: write the analytic inequalities completely,
bound the actual-G density error uniformly by O(epsilon^2) before area
scaling, and transfer endpoint J!=0. No actual slope data or graph is
asserted to exist. This would stop this balanced shrinking profile at
the stated conditional slopes, not all shrinking constructions.

## Completed bounded attempt

The complete proof, hypotheses and finite constants are now canonical
in `lemmas/L891-balanced-shrinking-profile-increases-full-mass.md`.
It is unaudited. All 14 exact rational checks passed in
`scripts/actual-g-radial-graph/common-scale-exact-checks-79.json`;
that certificate does not audit the analytic proof. The result is a
strict mass increase for the specified conditional slope subclass and
profile, with all collars and an actual-G remainder. No actual datum
or general shrinking-support obstruction was established. The earlier
working paragraphs are retained as unfinished reasoning history;
the sole current continuation is in PROGRESS.md.
