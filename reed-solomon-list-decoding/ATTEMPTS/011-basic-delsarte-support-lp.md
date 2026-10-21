# Basic Delsarte support LP — stopped as a threshold certificate

WHY IT FAILS: The exactly feasible primal and dual witnesses in
[L021](../lemmas/L021-basic-delsarte-support-lp-optimum.md) have equal
objectives. The optimal basic A(1024,10,68) LP upper certificate equals
L001's support ratio and is more than 2.766 times the ambient threshold.
Thus further optimization or tighter solver tolerances within this same
LP cannot certify index 956. This is a limitation of the relaxation,
not a lower bound on an actual code or an unsafe RS list. The complete
exact certificates and independent audit are in `scripts/finite-support/`.
Additional joint-distance constraints or RS-specific determinant restrictions
are different mechanisms and require their own assessed coverage; the
stopped basic LP is not a global ban on support methods.
