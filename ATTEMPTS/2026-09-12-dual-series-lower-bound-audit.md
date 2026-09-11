# Dual-series lower-bound audit — 2026-09-12

The proposed inference was that summing the positive stationary-phase terms in explicit Dirichlet form might supply the missing center lower bound. [Lemma 144](../lemmas/L144-gaussian-weighted-dual-dirichlet-series.md) proves the transformation and its precise limitations.

WHY IT FAILS: the transformed series still has rotating logarithmic phases. Its positive absolute weights do not bound its modulus below; every subset of o(sqrt(t)) terms has negligible absolute mass and cannot pass the subset-versus-complement absolute dominance test. The normalized center error becomes O(sqrt(t)) in the new series coordinates. No bound exceeding that error has been established. This rejects the automatic lower-bound inference only, not every possible analysis of this series and not RH. A contour representation may reveal further structure, but it is not an established lower bound.
