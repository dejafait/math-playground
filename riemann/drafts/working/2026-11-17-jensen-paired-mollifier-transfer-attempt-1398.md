# Paired mollifier attempt1398 — saved reasoning

The exact target is the unchanged M1 action in ready assessment1394,
separately approved1395. This turn makes one mathematical attempt; it
does not change the shift, taper, length, heat times or source floors.
The main gap is actual-Xi all-degree positivity L030-L032/C032a and
the exceptional Jensen-root deficit. A paid fixed negative pair mean
could support pair density after an independent squared-mass estimate;
quantitative root selection would still be required.

Inspected inputs: full C019q and C019p, C019l's scales and elementary
amplitudes/phases/entries, C019m's actual normalization and product
transfer, source-notes1394 and nomination1393's completed comparisons,
working/history1397 and stop1391. The existing source assessment is
reused. C019p/q remain provisional; no new source import, reciprocal
evaluation on the critical line, RH or random-law assumption is made.

The bounded question is whether cancellation in the exact prescribed
coefficients pays the mixed transfer. C019p's sufficient estimate needs
Q_0+Q_h=o(Xq), where Q_j=integral_D V(Y+j)^2 W(Y)dY. Its absolute
bound is O(KXq), K=L^2; this inadequate upper bound is not an obstruction.
The whole signed G_d of C019q remains present and unsigned.

Possible route under examination: group each analytic half of V times
M(Y)M(Y+h) by its integer product. Keep its moving cutoff and heat
multiplier in the grouped coefficient. The unrestricted identity
alpha*alpha=mu does not identify the two tapered, truncated factors
with a mu mollifier. Any useful cancellation must pay this difference.
No coefficient norm bound or mixed transfer is proved at this save.

Continue if the exact coefficient norm gives a genuine logarithmic
saving sufficient for o(B) transfer, or the full signed form yields a
paid fixed negative margin. An incompatible actual-P signed asymptotic
would stop M1; failure of an absolute estimate decides neither sign.
Do not replace the finite harmonic sum by an integral with an unpaid
B-scale endpoint error. Preserve partial reasoning and reassess if
neither norm nor sign receives a discriminating bound.

## Second save: a possible common-norm comparison

For real beta define A(beta)=sum_{k,l<=K} beta_k beta_l gcd(k,l)/(kl).
The divisor identity gives A=sum_r phi(r)|z_r|^2, where
z_r=sum_{r|k} beta_k/k. Multiplication of beta_k by log k transforms
z_r into (log r)z_r+sum_a Lambda(a)z_{ra}. A weighted Schur estimate
appears to bound this operator by 3 log K: use phi(ra)>=phi(r)phi(a),
the Schur weights r^(-1/2), and
sum_{a<=K}Lambda(a)/a<=2 log K from log(floor(K)!) and
floor(K/a)>=K/(2a). This needs full checking, including the weights.

If the full signed G_d is bounded above by -c Xq A(beta), and the
weighted energies are O(Xq A(beta))+o(X), C019p's transfer error is
O(X sqrt(A(beta)))+o(X). The elementary inversion lower bound
A(beta)>=1/sum_{r<=K}mu(r)^2/phi(r), since beta_1=1, would then make
that error small relative to Xq A. This could meet the permitted
error-smaller-than-margin criterion without separately proving
Q=o(Xq). None of these sign/energy conclusions is established here.

The sign still requires control, in this same norm, of C019q's full
finite harmonic sum, its stationary integral and H_Y(log(k/l)).
Entrywise estimates do not suffice for signed beta. A possible route
uses the harmonic sum/integral remainder and complex powers of gcd,
but all endpoint terms and constants must be paid. If these operator
comparisons cannot be justified within this attempt, retain only the
verified part and leave the main sign test unresolved.

## Third save: explicit operator and sign bounds under checking

The Schur estimate above checks out with row bound 2 sqrt(2) log K
and column bound sqrt(2) log K, hence norm at most 2 log K for T
and 3 log K for D. For c=log(sqrt(kl)/gcd(k,l)) and a=log(k/l),
exp(sc+za) factors through the Jordan divisor coefficients J_(1-s).
The Taylor coefficients of J_(1-s)(r)/phi(r) are dominated coefficient
by coefficient by exp(2(log r)|s|). Together with D this gives

    |sum u_k v_l gcd(k,l)c^m a^n/(kl)|
      <=(5 log K)^m (6 log K)^n ||u||_A ||v||_A.

Thus entire kernel errors can be bounded by their absolute Taylor
series at R_c=5 log K<=q/100 and R_a=6 log K<=3q/250.
This is a norm comparison, not entrywise domination of a signed form.

Euler summation of the harmonic sum, retaining its endpoint, and the
stationary integral cancel the lower limit |a|/2. Up to an entrywise
O(K/sqrt(X)) error the brace becomes

    integral_0^(u-c) f(v)dv + gamma f(u-c)
      + integral_1^(N/K) E(r) f'(u-c-log r) dr/r,

where u=ell/2, f(v)=exp(t v^2/2)cos(hv),
E(r)=sum_(n<=r)1/n-log r-gamma, |E(r)|<=1/r.
The scalar integral at c=0 is <=-q/10 eventually. Its c variation
has norm at most 3q/100. The a-prefactor differs from its constant
by a Taylor majorant <=1/1000 eventually. The retained harmonic
remainder has norm O(1). These constants leave a negative q*A margin.
The aggregate entrywise error is O(K^2/sqrt(X)) before integration.

The prospective energy bound uses the full zero-shift square formula,
with coefficients beta_k k^(i(j-h/2)) and interval D+j. Its stationary
channel must be recomputed with the phase e^(i c_0 t a); the same
Euler cancellation would then give O(Xq A)+O(X^(451/500)).
No final actual-P conclusion is claimed until that variant and the
common-onset/error comparison are written and checked canonically.

## Completed disposition

The full argument is now canonical in
[C019r](../../lemmas/C019r-paired-mollifier-negative-mean-by-gcd-norm.md).
Its proof uses the safe elementary bound |E(r)|<=2/r; the stronger
1/r bound mentioned in the exploratory save is unnecessary. It
retains the harmonic endpoint and the stationary contribution in
both the signed pair and the complex-coefficient square variant.

The resulting reference margin is -BqA/50, and the actual-P error
is o(BqA), with qA bounded below by an absolute positive constant.
This provisionally establishes M1 (c=1/2), using the assessment's
error-smaller-than-margin alternative. It does not prove o(B) error,
the abandoned sufficient subgoal Q=o(Xq), or squared pair mass.
The argument needs an independent conceptual audit, including its
essential provisional C019p/q inputs. The nomination1398 is explicitly
REVIEW_REQUIRED; it neither approves nor carries out that audit.

The original coefficient-specific exploration is preserved above.
The successful development uses a common gcd norm instead of
identifying the tapered fractional product with a Mobius mollifier.
No mathematical script, numerical certificate, additional external
source, cross-notebook input or supervisor-state change was used.
