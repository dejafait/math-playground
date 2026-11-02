# Angular inner-input cancellation — quantitative method stop

One attempt on the ready common-pole angular Hankel target used the
unit inner input f_theta(zeta)=B_theta(R*zeta). The exact response,
uniform weaker lower bound and rate comparison are proved in
[C645n](../lemmas/C645n-angular-inner-input-rate-gap.md). The result has
not received an independent audit.

WHY IT FAILS: This input cancels every inverse-grid factor exactly,
leaving B_theta(x)/R times the unweighted positive-residue symbol.
Its angular response has rate lambda=0.04792001946...>1/32; C645n
bounds the complete response above by a constant times
n*exp(-lambda*n) and bounds it below with the same exponential rate
up to polynomial factors. Thus even the full output from this input
cannot supply the required exp(-n/32) lower bound. This is an upper
bound on one response, not on the operator norm; no angular
countersequence or RH disproof follows. The obtained weaker uniform
lower bound is retained, and the positive scalar coefficient is not
misrepresented as the missing quantitative noncancellation theorem.

The next proposed mechanism uses the constant Hardy input and exact
angular Gram/residue analysis under the unchanged ready target.
Neither this response stop nor C645m's separate ellipse-envelope stop
prohibits that test. Interior angular poles and all complex phases
must remain. The full angular target and all Xi bridges remain open.
