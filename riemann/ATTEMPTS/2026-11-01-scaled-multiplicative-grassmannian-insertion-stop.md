# Scaled multiplicative Grassmannian insertion: exact N=2 stop

The full-tail arithmetic formula, scalar HCIZ normalization, exact
signed polynomial and class obstruction are canonical in
[L631](../lemmas/L631-full-tail-two-coordinate-grassmannian-insertion-obstruction.md),
which awaits an independent critical audit. Its exact rational replay is
`scripts/full_gram/grassmannian_n2_certificate.json`.

WHY IT FAILS: Inserting the arithmetic amplitude by evaluating it on
the two compressed spectra passes the constant-amplitude check but
misses the orbit-volume factor when the exponent changes. The actual
N=2 first shift coefficient disagrees. More generally a fixed-measure
integral with amplitude H(P,tau Z) can contribute only shift degrees
up to four to the order-four observer, whereas the full normalized
arithmetic form has nonzero degree eight. The infinite tail and all
C_2 derivatives are included in this calculation. This is a failure
of universal exact identities in that specified class; it is not a
negative direction, a disproof of the half-margin, or an asymptotic
growing-N obstruction. Spectral derivatives retaining the Vandermonde
factor fall outside the stopped class and remain unproved. The next
nomination requires a separate source comparison before construction.
