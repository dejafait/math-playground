# Height-normalized suffix selection — 2026-09-11

The tested extension was to remove Lemma 84's height-tail restriction by
selecting suffix minima of x_n/(n sqrt(H−b_n)), or of x_n/q_n with q_n
at least a positive constant multiple of n sqrt(H−b_n) eventually.
The canonical obstruction is [Lemma 85](../lemmas/L085-obstruction-to-height-normalized-suffix-minima.md).

**WHY IT FAILS.** Admissible coordinates and heights can make the positive
normalized coordinate sequence tend to zero, leaving no attained suffix
minimum at all. In the same example the sufficient factor in Lemma 84
diverges along every unbounded index set, so selection alone cannot repair
that bound. This failure is limited to the specified normalization class
and bound; it neither disproves the unrestricted liminf assertion nor
excludes arguments using actual height increments.
