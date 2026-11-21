# BPY direct finite-closure test — working record, step2141

Completed: the canonical proof is now C874e, in
`lemmas/C874e-bpy-tilted-operator-nonclosure.md`. The provisional notes
below preserve the reasoning checkpoint; they are not a second proof.

Approved scope: the exact COVERED_TARGET in
`drafts/literature/2026-11-21-theta-size-bias-contact-nomination-2139.md`.
Main gap L030-L032/C032a; possible use is an additional physical-law
relation constraining L874's degree-two contact flux. No contact is assumed.

Import BPY2001 Proposition2.1/(2.9)-(2.10), Proposition3.1(i), rather
than reprove its fixed-point characterization. Put a=2/pi, m=2/3,
x(u)=a exp(2u), u(x)=log(sqrt(x/a)), lambda=1/16. Its Y-law has log
density H(exp(u)), so K(u)=exp(u/2)H(exp(u)) is the even extension
of L019. The full weight is w(x)=exp(lambda u(x)^2+u(x)/2), with
Z=E w(X)=2F(lambda,0), not the negative half-tilt.

For independent original X, X*, h with density h^(-1/2)-1 on (0,1),
the direct convention f=w(P composed with u) gives

    A P(u)=x(u)P(u)-m E[w(x(u)+h X*)P(u(x(u)+h X*))]/w(x(u)).

The expectation of A P under the full tilted law should be zero.
For even P, use its explicit reflection average A_e P before the
half-line identification. Joint weighting is retained; no independent
tilted summands are substituted.

Candidate stop: A_e 1=a cosh(2u) minus a bounded positive term.
For u>=0, t=v/a, delta=(1/2)log(1+t exp(-2u)),
log(w(x+v)/w(x))=lambda u log(1+t exp(-2u))
+(lambda/4)log^2(1+t exp(-2u))+(1/4)log(1+t exp(-2u))
<=19t/64. For u<=0, monotonicity about x0=a exp(-8) gives
w(x+v)<=w(x)+w(a+v); also w>=exp(-1).
E exp(19 X*/(64a)) is finite from the actual theta upper tail,
whose x-rate is pi^2/2. Need finish the full polynomial domain and
absolute expectation checks, then record the canonical proof.

Discriminator: a proved nonpolynomial constant image retires this
direct finite-closure mechanism; it does not stop all nonlocal
operators, supply a signed contact result or resolve RH. Existing
node-mass/score/finite-moment stops remain intact.
