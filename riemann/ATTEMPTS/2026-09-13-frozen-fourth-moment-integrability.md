# Frozen fourth moment does not yet supply integrability — 2026-09-13

The variance-normalized block calculation is stored in
[L171](../lemmas/L171-frozen-block-fourth-moment-and-integrability-gap.md).

WHY IT FAILS: the multiplicative diagonal has order log T and the
available signed endpoint error is O(T^(1/4)log T) after block
normalization. The resulting fourth-moment bound grows with T and
does not control first-moment tails uniformly. L171 gives an explicit
abstract family satisfying these moment bounds without uniform
integrability. This rules out the inference from these bounds alone,
not uniform integrability of the actual sums; diagonal growth is not
a lower bound for their full fourth moment.
