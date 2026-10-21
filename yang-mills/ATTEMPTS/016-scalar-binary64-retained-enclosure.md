# Scalar majorant with binary64-scale retained input errors

WHY IT FAILS: [L034](../lemmas/L034-retained-fourier-error-budget.md)
propagates Fourier-coefficient and inverse-weight errors using L033's
full absolute heat-moment majorant. Even the illustrative assumptions
eta=epsilon_s=epsilon_r=2^-52 and zero arithmetic residual produce
allowances above 2.23e15 and 8.94e15, compared with same-cutoff diagnostic
sizes 453 and 3353. Thus that sufficient test cannot certify the signs.
The actual input errors are still unvalidated, and this is not a lower
bound on actual error. Stop this scalar-majorant/binary64-scale method;
neither tensor-level propagation with actual mode weights nor a rigorous
higher-precision computation is excluded. Ideal time-window tails are
already small. The next discriminating test retains the individual
coefficient and mode factors in an absolute tensor sensitivity sum.
No upper-face sign, compensated power coefficient or logarithm follows.
