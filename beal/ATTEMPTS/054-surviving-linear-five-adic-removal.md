# Fixed mask-17 five-adic removal test stops

2026-10-24. The approved fixed-product test is complete; see
[C124a](../lemmas/C124a-surviving-linear-product-passes-five.md)
for the exact proof and finite certificate.

WHY IT FAILS: L124's mask-17 product theta²−9 is square in every
factor of the actual five-adic algebra. It has identity class in
L119's exact point image, so this condition removes neither mask of
the existing joint-zero fiber. The calculation has strictly positive
relative bounds in all factors. This stops removal of this product
by this unchanged filter; it proves neither global scalar-squareness
nor rational-point existence. Full supported arithmetic and point
control remain open. Repeating precision or the same membership test
offers no new discrimination. A critical audit may check this result;
further pruning requires a materially different test or target.
