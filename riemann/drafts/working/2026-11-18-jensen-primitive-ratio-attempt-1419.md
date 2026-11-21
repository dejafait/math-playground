# Primitive source ratio attempt1419 — working checkpoint

Approved target: Test whether primitive-source-ratio grouping evaluates
C020c's complete signed rational mixed-channel expression with error
o(Bq^2), retaining every endpoint term and original coefficient.
Coverage: unchanged EXPLORE assessment1417, completed by source-notes1418.

Main gap: L030-L032/C032a actual-Xi all-degree positivity. This one
component could inform the fixed quotient cBq^2 versus O(B) test; the
other numerator channels, denominator and actual-P transfer stay open.
Continue only with a quantified source-compatible full reduction;
otherwise save the first unpaid term and stop this implementation.

Inputs read: C020c in full, C019 including the exact channels and error
payment, C019y's fixed-witness definitions and full quotient decomposition;
source-notes1418 and stops1415-1417. The supplied assessment is reused.
The local inputs still await conceptual audit. No actual-P contract is used.

Unfinished reasoning, not yet a proved result: write m=k*a, n=k*b with
(a,b)=1, then reduce a*r/(b*s)=A/D. The center phase depends on A*v/D
but not k. Its denominator is D/gcd(D,v). Since witness primes exceed R
and their product exceeds N*, the common-factor cases should be only
1 or either individual witness prime. The k-dependent heat factors and
both source-entry domains must remain inside the grouped weight. The
remote endpoint phases must also remain, even though they are not merely
additive center phases. At this initial checkpoint the remaining work
was to check these cases and the actual modulus range against the
previously inspected sources, then state the exact unpaid expression.
No cancellation or error saving was claimed.

Completed later in this step: C020d contains the full proof, complete
kernel and explicit high-modulus stratum. The direct additive-source
implementation stops; its signed residual remains unevaluated. This
working note preserves the initial reasoning, not a second proof or
current next-action record.
