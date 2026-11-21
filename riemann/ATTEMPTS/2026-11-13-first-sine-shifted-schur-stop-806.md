# Fixed shifted Schur test — retained-direction stop

The full argument is [C759d](../lemmas/C759d-first-sine-shifted-schur-stop.md),
with its complete outward certificate. This is a local NEGATIVE result
using assessed standard methods. The independent conceptual and full
scalar audit in C759d Section5 (step808) accepts this stop; its3674
checks include all series rows and tails, with no failures.

WHY IT FAILS: At tau=11/200, the unit retained sine s_1=sin(pi*x)
already has Q(s_1)<0.004<tau. Complete cross representers exist and
K is their positive semidefinite covariance, so S_d=A-K/d has a
negative value in this direction for d=2859/10000. C759c's complement
cannot repair a negative retained diagonal. This is not a failed upper
enclosure, an unpaid tail or a negative value of unshifted Q. The even
trial is only an upper bound, so actual parity and Xi realization remain
open. Stop this fixed shift; no cutoff or shift sweep is authorized.
The independent audit changes the verification status, not this scope.
