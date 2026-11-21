# Uniform exterior-tail working checkpoint1511

Approved target: assessment1509, SPECIALIZE before this invocation.
Main gap: actual-Xi all-degree positivity, with C028b's H_d=o(d)
equivalent to RH. Attempt only the stated exterior bound at A*d.

Inputs read: C028a actual entire F and polynomial normalization;
C028d centered coefficients and definitions; source-notes1510's
primary theorem comparison. C028a/C028c reference-budget stops are
contrasts. No full-line identity or root-reality assertion is needed.

Proof outline to finish: write G(u)=exp(-b_1*u)F(u)=sum h_k*u^k.
Finite coefficient convolution gives c_(d,k)=(d)_k*h_k,
h_0=1,h_1=0. Put M=max_(|u|=1)|G(u)|>=1. Cauchy's coefficient
inequality gives |h_k|<=M. For r=d/|y|<=1/2, bound
|Q_d(y)/y^d-1|<=M*r^2/(1-r)<=2M*r^2. The candidate choices
A_0=2*sqrt(M), C=8M make this at most 1/2 and yield
|f_d(y)|<=4M*d^2/y^2. Integrating both rays should prove the
stronger absolute-tail bound C*d/A. Check every coefficient factor,
endpoint and logarithm condition in the canonical proof before claiming it.

Success test: finite fixed-family constants independent of all d>=3
and A>=A_0. Failure test: any hidden degree dependence or unproved
root-reality/domination requirement. No numerical calculation is needed.
The central cancellation and C028d's unaudited full-line identity remain
independent; this is a classical-method specialization, not novelty.

Completed: the proof is canonical in
[C028e](../lemmas/C028e-reciprocal-jensen-degree-uniform-exterior-log-tail.md).
It uses the explicit upper bound M=exp(b_1)*F(1) in place of the circle
maximum proposed above, with the same A_0 and C formulas. The positive
actual coefficients justify that replacement. All degrees and both
unbounded rays are treated without the full-line identity or a d-limit.
The outline above is retained as the unfinished-work checkpoint.
