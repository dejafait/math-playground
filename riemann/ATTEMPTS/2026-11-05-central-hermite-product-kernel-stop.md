# Prescribed central degree-six Hermite product kernel: pointwise stop

Step496 constructs the exact denominator-cleared symmetric product-theta
kernel in [L794](../lemmas/L794-central-hermite-product-kernel-pointwise-stop.md).
The least clearing power is m_6^10. A fixed integer vector gives the
exact negative value -1281831933403422720 at (1,...,1,4); negativity
persists on an open positive distinct-variable set. The full exact
certificate is `scripts/central-hermite/product-kernel-496.json`.

WHY IT FAILS: although K is positive and the kernel integrates to the
positive scalar m_6^10 times the Hermite matrix, the prescribed polarized
matrix polynomial is not pointwise PSD. Therefore its integral cannot
be signed just by claiming that polynomial is PSD everywhere. The
negative region may be offset elsewhere. This stops only that fixed
representation's pointwise-sign route, not its integrated positivity,
known central degree-six hyperbolicity, other Gram representations or RH.
No degree sweep or alternative polarization was attempted. Independent
audit of the exact obstruction is nominated before further use; no new
theta compensation mechanism is justified by this negative test alone.
