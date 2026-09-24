# Pointwise Hilbert control of the cutoff remainder — 2026-09-13

The signed formulation and its precise estimate are proved in
[Lemma 157](../lemmas/L157-signed-cutoff-hilbert-remainder.md).

WHY IT FAILS: the frequency spacing is of order T^(−1/2), so the
pointwise Hilbert bound costs sqrt(T). Combining it with the available
cutoff variation gives sqrt(T)/M in the normalized remainder. This
removes the earlier logarithm but supplies no small bound for fixed M.
Keeping the exact correlation and integrating it back instead reproduces
the original weighted moment identically. An additional correlation
estimate is needed; neither this calculation nor its growing upper bound
shows that the actual tail target is false.
