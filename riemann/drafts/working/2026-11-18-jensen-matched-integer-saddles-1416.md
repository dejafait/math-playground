# Fixed real source-prime witness — attempt1416

18 November 2026. Reuse unchanged prior EXPLORE assessment1409 for
exactly (N1). Main gap: L030–L032/C032a actual-Xi all-degree positivity.
The intermediate test pairs C020a’s type-(0) coherent integer saddles
with the corresponding type-(h) terms of C conjugate(A), retaining the
actual four tapers, source entries and own heat times. Its downstream
use is to decide whether the first natural matched cancellation can
remove the Bq^2 terms before estimating the full quotient. A nonzero
paired leading term is useful only locally: all other signed channels,
the denominator, actual-P transfer and density/root gaps remain open.

The supplied overview/DAG and ready assessment were read; targeted
reads covered C019’s complete reduction, C020a’s complete proof,
C019y’s definitions and exact full identity, C019z’s coefficient
correlations, source-notes1410 and stops1407/1408/1415. No matching
completed pairing appeared in the targeted local search. Existing
unfinished files and source coverage are preserved; no new source
premise or witness optimization is introduced.

Saved before extended reasoning: in CA, select n=p, r=a*s for ordered
witness primes p!=b. In C conjugate(A), the matching assignment is
m=p, s=a*r. The centers are 2*pi*a*m*b and 2*pi*a*m*b-h, respectively.
The negative phase contributes exp(-i*h*log(a*m*b)) at its saddle;
this factor must be combined with the shifted source coefficient,
not dropped. Test first a=4, then if the same uniform argument permits,
the already-covered fixed a in {1,2,3,4}, using only C019z’s existing
K_a values. No claim that these exhaust all integer/rational saddles.
Continue only after paying every selected endpoint/source transition;
if no full threshold is reached, retain the exact signed complement.
No conclusion has been established at this checkpoint.

## Preserved derivation before scalar certification

For each fixed a, write T_a^+ for the CA selection n=p,r=a*s,
and T_a^- for the C conjugate(A) selection m=p,s=a*r (rename the
other source m and the smaller mollifier index s). Their exact
outer factors are c_(as) conjugate(c_s) p^(ih)/(sqrt(a)*s*p*sqrt(m*b))
and c_s conjugate(c_(as)) m^(ih)/(sqrt(a)*s*p*sqrt(m*b)). The
respective source intervals are [max(X,rho_m),sqrt(2)X-h] and
[max(X,rho_m-h),sqrt(2)X-h]. At x=2*pi*a*m*b the type-(0) leading
phase is one. At x-h the negative type-(h) phase is
exp(-i*h*log(a*m*b)); combining it with m^(ih) gives (a*b)^(-ih).
Thus both full leading source amplitudes are 2+O(1/q).

The same transition partition Delta=X^(3/4) as C020a leaves
O_a(K1*X^(3/4)/q^2) total endpoint/source-entry error, and replacing
the own-time amplitudes costs O_a(K1*X/q^3). Let
H_a(t)=[min(sqrt(2)/(2*pi*a*t),a*t)-1/(2*pi*a*t)]_+,
J_a=integral_(1/10)^(1/5) H_a(t)dt,
F_a=sum_(p!=b) M_a(b)/p, with M_a the corresponding integer count.
Then T_a^+=4*pi*a*conjugate(K_a)*F_a plus these errors;
T_a^-=4*pi*a*K_a*F_a plus these errors. Pairing therefore
reinforces the real leading coefficient, rather than reversing it.
F_a~4*X*log(2)*J_a/q^2, interpreted additively when J_a=0.

For a=1,2,3,4 put C_a=2*pi*a*rho(a)*log(2)*J_a using C019z (12).
C1=0. With z=8*pi/25 and A=log(2),
C2=-(3*A/13)*(z-1-log(z)),
C3=-(2*A/11)*(sqrt(2)-1-A/2+(sqrt(2)-1)*log(18*pi/(25*sqrt(2)))),
and C4 is C020a (15). The anticipated total C2+C3+C4 is negative;
its numerical threshold remains to be certified. This finite set
is not all integer-saddle terms. No total numerator sign follows.

## Completion

[C020b](../../lemmas/C020b-real-prime-witness-matched-integer-saddles.md)
contains the exact families, full selected boundary payment and
matched-channel relation. The a=4 counterpart reinforces C020a.
The complete selected a=1,2,3,4 families have sum C_a<-19/1000;
with C019z’s negative resonance their partial constant is <-39/1000.
No statement about the sign of the full numerator follows: C020b
(12) preserves every complement and the actual-P residual. The full
denominator also remains unpaid. All thirteen rational scalar checks
passed, and the five conclusion intervals and failures were inspected
in full using the scoped JSON inspector. This is a local mathematical
advance, not a certified novelty claim or an independent audit.

The unchanged ready target is retained. Its next discriminator is a
uniform, summable comparison of the complete mixed channels with
all rational twists retained, not another isolated fixed-ratio sign.
The full cBq^2 or O(B) quotient alternatives remain the deciding tests.
