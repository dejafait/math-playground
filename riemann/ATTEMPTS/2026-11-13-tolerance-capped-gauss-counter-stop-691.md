# Tolerance-capped Gauss setup counter stop691

Canonical result: C998m in `lemmas/C998m-tolerance-capped-gauss-setup-counter-stop.md`.
Assessment687 was ready before the calculation. All prior prescriptions,
witness data and unfinished work are preserved.

WHY IT FAILS: The output-tolerance cap passes690's grid obstruction and
completes248 node/weight pairs, but the retained fixed16-bisection prefix
uses a substantial part of the scheduled budget. The upfront recurrence
charge for the next root's third bisection raises the conservative counter
from4998958 to5000490 and triggers its cap guard. This is not an actual-work
lower bound or an impossibility theorem for Newton, and the13 uncomputed
outputs and complete setup work remain unpaid. Both recorded-prefix
inclusions and the exact counter stop are separately verified in691's
replay certificates. Abandon this fixed schedule; a separate adaptive
initial-refinement safeguard can test whether unnecessary sign bisections
can be avoided while preserving every derivative/inclusion guard.
