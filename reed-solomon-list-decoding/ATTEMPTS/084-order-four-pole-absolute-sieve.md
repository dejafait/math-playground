# Fourth-order-pole absolute character-sieve upper test

Tested 2026-10-20 under the saved SPECIALIZE assessment.

## WHY IT FAILS

[L101](../lemmas/L101-order-four-pole-dictionary-and-upper-test.md)
gives the entire list dictionary and exact extra-agreement correction.
The test keeps the complete residual character sum, uses the full
unit group modulo X^4, cancels every nonprincipal constant-only
character and retains all 67 sieve cycle lengths. Its resulting
absolute upper allowance divided by T=65537^28/2^128 is strictly
between 3676307 and 3676308, against the required ratio at most one.
The nonconstant character estimate and absolute cycle sum are too
coarse for this sufficient certificate; the nonnegative 68-root
correction is not quantitatively exploited. Park this one estimate
without retuning. This is not a lower bound on any actual list or a
failure of the dictionary, and does not stop other mechanisms or
prove arbitrary-center safety or unsafety. The separate critical audit
in step 377 retains the dictionary and this failed-certificate diagnosis;
its full proof review and exact evidence are recorded in L101.
