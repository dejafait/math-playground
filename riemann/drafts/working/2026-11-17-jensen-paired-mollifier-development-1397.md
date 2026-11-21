# Paired mollifier development1397 — interim reasoning

The exact approved target remains assessment1394's M1, unchanged in
shift, taper, length, degree range, both times and both floors. This is
one research attempt using its prior EXPLORE coverage; no additional
source import or approval is being asserted.

Main gap: actual-Xi all-degree positivity L030-L032/C032a and the
exceptional Jensen root deficit. A fixed negative actual-P weighted
mean could support opposite-sign pair density only after the independent
squared-mass and root-selection gaps are resolved. Continue on a paid
negative margin or a materially sharper necessary arithmetic estimate;
stop the fixed test on an incompatible rigorous signed asymptotic.

Inputs inspected: canonical C019p in full, C019l's exact scales and
amplitude/phase/entry estimates, C019m's actual normalization, square and
product transfer, source notes1394 and the paired comparisons in
nomination1393/review1394. C019o/stop1391 is comparison evidence only.
No reciprocal is evaluated on the critical line; no RH, random law,
simple-zero or nonvanishing assumption is made. C019p is provisional.

The working question is whether the coefficient cancellation in
b_k=sum_{uv=k} alpha(u)alpha(v) omega(u)omega(v) v^(-ih) controls
the mixed transfer. The positive quantities Q_j=integral_D V(Y+j)^2 W
need o(Xq) under C019p's sufficient bound. The existing estimate
O(KXq) is inadequate and is not a lower bound. Both arithmetic product
channels of the signed mean must remain present. No cancellation,
fixed sign or small-Q conclusion has been established in this save.

A possible finite-sum route is to group the resonant difference terms
by their common integer product and to express the weighted energy
using the resulting divisor sums. Any use of coefficient cancellation
must retain the moving source cutoff and heat amplitude. The stationary
channel cannot be declared negligible by an absolute second-derivative
bound after summing all mollifier twists. Further work below will record
either a rigorous payment or the precise unpaid expression.

## Second save: proposed stationary arithmetic reduction

The mixed transfer has not been paid. A concrete refinement of the
other channel is now available for checking. Write K=L^2 and
a=log(k/l). After replacing the truncated Fresnel factor by its
whole-line value only at centers inside the true entry interval,
the stationary summand is

    4*pi Re[(b_k conjugate(b_l)/l) exp(-2*pi*i*mn*k/l)
             E_d(2*pi*mn*k/l;a,log(m/n))],

where E_d(Y;a,u)=exp(t(Y)(a^2+u^2)/8-pi^2*t(Y)/32
+i((pi/8)t(Y)a+h(a+u)/2)). The entry inequalities are eventually
exactly ml<=nk and nl<=mk. Thus k<l has no centers, k=l has only
m=n, and k>l has the region X<=2*pi*mn*k/l<=sqrt(2)X-h,
|log(m/n)|<=a.

For k>l reduce k/l to denominator c=l/gcd(k,l). Summation over n
has zero average unless c divides m. The proposed full average is
therefore 1/c=gcd(k,l)/l, with row geometric-sum error bounded by
O(c*q*sqrt(X)). The change of variables (m,n) to
(Y,u) has Jacobian l/(4*pi*k). This would leave

    Re sum_{k>l} b_k conjugate(b_l) gcd(k,l)/(kl)
       integral_D integral_{-log(k/l)}^{log(k/l)} E_d(Y;a,u) du dY.

The necessary boundary count is at most
O(H*(l/k)*q+sqrt(X)) per (k,l), for H=X^(3/5).
At these centers the weighted stationary amplitude is O(1/l), so
the aggregate boundary cost is O(H*K*q^2+sqrt(X)*K*q)=o(X).
The distant Fresnel-tail cost is O(X^(451/500)); arithmetic averaging
costs O(sqrt(X)*K^2*q). These bounds and the exact floor equivalence
are being checked before a canonical statement. No sign of the
remaining resonant plus gcd expression follows from this save, and
Q_0+Q_h=o(Xq) remains unproved. This is not a completed M1 test.

## Third save: combining the two channels

Symmetry in u,v in b_k gives b_k=k^(-ih/2)*beta_k with beta_k real,
|beta_k|<=1. This cancels the h*log(k/l)/2 phase in the stationary
integral. It leaves its real kernel with cos((pi/8)t*log(k/l)) and
cos(h*u/2), rather than a complex unevaluated arithmetic average.

For the resonant expression only, replacing the n-entry at Y+h by
its entry at Y costs O(h*N_*K)=o(X): each lost interval has length
at most h and all absolute coefficients sum to O(N_*K). This is a
paid integration-domain change, not a change of the actual observable.
Write g=gcd(k,l), m=(l/g)r, n=(k/g)r and
v=ell(Y)/2-log(r*sqrt(kl)/g). Pairing k,l gives the same real
cos((pi/8)t*log(k/l)) prefactor as the stationary kernel.

With f_Y(v)=exp(t(Y)*v^2/2)*cos(h*v), the candidate combined formula is

    2 integral_D sum_{k,l<=K} beta_k beta_l gcd(k,l)/(kl)
      exp[t(Y)(log(k/l)^2/8-pi^2/32)]
      cos[(pi/8)t(Y)log(k/l)]
      { sum_{1<=r<=N_d(Y)*gcd(k,l)/max(k,l)} f_Y(v)/r
        + integral_0^{|log(k/l)|/2} f_Y(v) dv } dY
      + O(X^(451/500)).

This retains all resonances and both channels. The continuous term
is the evaluated stationary channel, not an assumed negligible term.
No sign of this full quadratic form is established. In particular,
real or pointwise-positive kernel factors do not make its off-diagonal
quadratic contribution positive or give the required negative margin.
The final proof and exact error payments will be canonical in C019q.

## Completed disposition

The full proof is now canonical in
[C019q](../../lemmas/C019q-paired-mollifier-real-gcd-kernel.md).
It establishes the proposed real gcd quadratic form with absolute
O(X^(451/500))=o(B) error. It pays all exceptional stationary endpoints,
the full Fresnel tail, the arithmetic row averages and the resonant
common-entry replacement. The apparent real-floor comparison was
corrected during writing to the required integer-floor inequality.

This is a local analytic/arithmetic reduction, not a completed negative
mean or a new literature theorem. The initial coefficient-cancellation
attempt supplied no bound Q_0+Q_h=o(Xq); that obligation remains
explicit. Both G_d's sign and the actual-P transfer remain unresolved.
C019p and C019q are provisional pending separate conceptual audit.

Reassessment: this attempt gives a materially sharper input for the
unchanged approved M1 discriminator: a real quadratic form instead of
incomplete stationary sums. Reuse ready1394 for one development of its
sign/transfer test. Do not infer the sign from entrywise factors or
discard the finite harmonic-sum endpoints. Independent squared mass,
root selection, earlier stops and parked(A) are unchanged. No new
assessment, source approval, mathematical script or numerical evidence
was produced. The interim reasoning is preserved above.
