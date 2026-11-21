# Direct frequency-resolvent ansatz: local absolute-norm stop

Step364 tested the approved commutator mechanism in L759's exact cell,
lambda=sqrt(13), N=120, z=i/4. The canonical algebra and full certificate
are in [L760](../lemmas/L760-finite-commutator-fourier-row-saving.md).

WHY IT FAILS: For the direct row H_F=(k/a)x^T F, the commutator leaves
r_F=(kf/a)(beta^T F-a eta^T). The complete certified residual norm exceeds
||q|| by a relative amount between 2.2592e-29 and 2.2593e-29. Completing
this ansatz with the absolute bound ||r_F R||<=||r_F||/g therefore pays
at least the original full-row gap cost before adding the explicit row.
Rounding the ratio to one or omitting its odd component hides this failure.
This stop applies to that ansatz and completion only. L760's second
commutator gives a different, smaller residual and remains a finite
partial result; no general commutator ban or RH obstruction is inferred.
