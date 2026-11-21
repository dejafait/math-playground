# Fixed beta/Bessel specialization — working record, step782

Approved scope: assessment780, unchanged fixed function and H_1 only.
Main gap: actual-Xi all-degree mixed positivity, L030-L032/C032a.
Test: jointly verify the qualitative premises and det(H_1)<0; stop this
fixed discriminator after either result, without adjacent tests or sweeps.

Normalization to check: gamma_n=4^(-n)(3/2)_n/((1)_n(100)_n).
Thus b_n=gamma_n^(-1)=4^n(100)_n(1)_n/(3/2)_n. Berg's gamma100
and beta(1,3/2) power-moment laws factor b_n^c for every real c>0.
For f(x)=log b_x the candidate second derivative is the integral of
t exp(-xt)[exp(-100t)+exp(-t)-exp(-3t/2)]/(1-exp(-t)).
This kernel is strictly positive; all-order differences need endpoint
domination and the repeated fundamental theorem of calculus.

Cosine construction: beta variable s has parameters3/2,197/2;
conditional density of u in(0,sqrt(s)) is2/(pi sqrt(s-u^2)).
The proposed marginal density integrates this against the beta density.
Tonelli gives its mass; compact support gives all moments and absolute
interchanges. Check actual density finiteness, not just measure existence.
Exact order follows from Sokal's order1/2 for G and M_F(r)=M_G(r^2).

Remaining before completion: exact rational four-coefficient certificate,
all analytic justifications and canonical proof. No actual-Xi conclusion
or quantitative coefficient premise is an input. Existing work preserved.

Completion: the obligations above are now proved in C040c; the exact
certificate is `scripts/beta-bessel/fixed-h1-782.json`. The determinant
and a real quadratic-form witness are strictly negative. This closes
the fixed discriminator and refutes only the listed generic implication.
Critical audit remains pending under assessment782; no sweep followed.
