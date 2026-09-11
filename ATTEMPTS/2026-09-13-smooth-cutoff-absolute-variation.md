# Smooth cutoff with absolute variation — 2026-09-13

The moving-core tail estimate is still unproved. The precise integration
identity and bounds are in [Lemma 156](../lemmas/L156-smooth-amplitude-cutoff-variation-cost.md).

WHY IT FAILS: a smooth amplitude cutoff creates a derivative term in each
off-diagonal integration by parts. Even after removing the common carrier,
the available L2 derivative estimate bounds cutoff variation only by CT/M.
The resulting absolute pair sum contributes C sqrt(T)log(2T)/M, which
cannot establish a small tail for fixed M. This is failure of this upper
bound, not proof that the tail is large or that a signed estimate fails.
