# Gevrey paired tails: the absolute variation fallback remains unpaid

WHY IT FAILS: [C703a](../lemmas/C703a-growing-head-and-paired-tail-logarithmic-payments.md)
pays the prescribed growing head and the exact tail denominator, then
retains the signed numerator variation and endpoint logarithmic errors.
Its tested fallback uses an absolute bound for that variation and the
full degree-rectangle term cap in BGMP Proposition 4.10. After paying
the actual coefficient normalization, any scale at which this source
error bound is at most n forces the returned variation majorant to grow
as exp(Theta(n^3 log n)-O(n^(1/3))). This lower-bounds a computed upper
bound, not the actual variation or loss. Thus this certificate cannot
establish the required o(n) loss; no fixed L703 counterprofile, universal
impossibility or RH result follows. Better signed variation or zero
geometry could change the decision, but is not established. Preserve
L695's absolute-tail and L702's interior stops separately. Stop this
fallback; the proposed inner-disk complete-charge test has a different
observable and requires its own source comparison before mathematics.
