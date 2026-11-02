# Collective signed form: unscaled row-dominance test stopped

The exact collective transfer and the complete proof of the restricted
obstruction are in
[L622](../lemmas/L622-collective-signed-xi-transfer-and-row-sum-stop.md).
Its underlying arithmetic theorem remains a named import, and L622
has not yet received a separate critical audit.

WHY IT FAILS: The first row already has two fixed small-ratio correlations
whose limiting absolute sum exceeds its diagonal, uniformly over the
common real observer. Therefore the unscaled row-sum sufficient test
cannot certify positive definiteness of the growing matrix. The same
fixed leading block has a positive Gram factorization, so this failed
bound is not a negative eigenvalue or an actual-Xi sign witness. No
larger row sum or floating spectrum repairs that distinction. The exact
phase transfer now controls all absolute errors, but the full signed
spectral margin is still unproved. Preserve this specific stop; a
coefficient-uniform Gram comparison is a materially different spectral
test within the same covered collective target, not a repetition of
unscaled diagonal dominance or a global ban on arithmetic correlations.
