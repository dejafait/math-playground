# Negative-strip lower-bound checkpoint

The completed L197 is preserved. A scoped sharpness step is to reduce
Y_mid^- >= c Nh to a positive-density count of exact eligible ordered
tuples. L197 bounds the number of eligible tuples by O_K(N^3): both
product intervals have O_K(N^(3/2)) ordered factor pairs and each u,v
allows O(1) m. Every tuple weighs O(N^(-1/2)).

Unproved draft: a matching lower bound is equivalent to having >= c N^3
tuples with ell >= eta N^(3/2), phi(u)/u >= eta, and both signed-profile
ratios bounded away from zero on opposite sides. Retain gcd(m,u)=1
and all L191 endpoints. Prove by deleting small-factor contributions
from a bounded-cardinality set. No density of these tuples is proved.

Resume with the threshold argument, uniform lower profile/coefficient
bounds and the equivalence between ratio thresholds and distance from
sqrt(2). This is a reduction, not an established lower bound.

Completed in L198: the equivalence is proved with exact thresholds and
uniform constants. The positive-density count itself remains unproved.
No calculation is in progress.
