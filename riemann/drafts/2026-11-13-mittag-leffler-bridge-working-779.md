# Fixed model attempt779 — saved reasoning

Approved target: assessment778, unchanged SPECIALIZE scope; one model and
one H_3 only. Main gap L030-L032/C032a remains actual-Xi mixed positivity.
No off-line zeta zero or actual-Xi sign is asserted.

Let b_n=Gamma(3n/2+1)/Gamma(n+1)=1/gamma_n, x=n/2 and
K=3^(3/2)/2. Gamma multiplication gives
b_n=K^n [Gamma(x+2/3)/Gamma(2/3)]
 [Gamma(x+1/3)Gamma(1/2)/(Gamma(1/3)Gamma(x+1/2))].
Thus b_n is the moment sequence of K sqrt(G B), with independent
G~Gamma(2/3,1), B~Beta(1/3,1/6). Berg5.1-5.2 supply powers of
the Mellin factors, not an unjustified arbitrary quotient closure.

For f(x)=log b_x, f''(x)=1/4 integral_0^infinity
t exp(-xt/2) A(t)/(1-exp(-t)) dt,
A(t)=exp(-2t/3)+exp(-t/3)-exp(-t/2)>0.
Iterated finite differences of f'' give strict alternating signs
from order2, including n=0; endpoint bounds must be retained in proof.

M_(3/4) is the imported nonnegative density on [0,infinity), with
moment q equal to Gamma(q+1)/Gamma(3q/4+1), q>-1.
The absolute cosine-series integral is sum |t|^(2n)/Gamma(3n/2+1),
finite by the gamma ratio/Stirling estimate; hence Tonelli plus absolute
integration justifies F(t)=integral M_(3/4)(u) cos(tu) du.

Completed: canonical C040b gives full sources and proof. The single H_3
is positive definite by rational interval LDL pivots above
1/10,1/10000,1/10^7,1/10^10; the negative-direction objective failed.
The full e_0,...,e_8, logarithmic sums, matrix, trial vector, form and
elimination intervals are in scripts/mittag-leffler/fixed-h3-779.json.
No parameter/dimension sweep. The fixed discriminator is stopped.
