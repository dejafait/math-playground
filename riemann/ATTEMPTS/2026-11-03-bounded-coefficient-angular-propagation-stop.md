# Bounded-coefficient angular propagation

The whole-circle countermodel in
[C672a](../lemmas/C672a-bounded-coefficient-angular-normalization-stop.md)
specializes L672's audited construction: all auxiliary coefficients
have modulus less than 2/3, their total modulus is O(log n), and the
response equals one at every exterior point x/t_j. Its circle maximum
is nevertheless o(exp(-n/1000)). The new coefficient and normalization
checks are unaudited; the inherited approximation estimate was audited.

WHY IT FAILS: Propagating from the exterior anchor values while using
only node-value bounds discards the correlation imposed by L688's one
low-degree polynomial. An existing explicit angular approximation
already satisfies those relaxed inputs with bounded coefficients.
It cancels on the whole circle at a rate faster than the proposed arc
threshold. This stops the relaxation, not the particular Taylor filter
or the full original-D norm. The auxiliary coefficients are not original
residues, allowed displacements, or a demonstrated low-cost polynomial
multiplier. A continuation must retain an additional exact relation,
such as the joint low spatial moments; magnitude bounds or nonvanishing
alone cannot reopen this propagation argument.
