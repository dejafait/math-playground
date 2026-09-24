# Local mean squares do not close block cutoff covariance

The block decomposition and local estimate are proved in
[L168](../lemmas/L168-blockwise-cutoff-covariance-and-local-moment-gap.md).

WHY IT FAILS: choosing sqrt(T)log T≪H≪T/(log T)^4 makes the
within-block amplitude error vanish and gives accurate local first
moments of Q. But the remaining block sum contains χ''(Q/M), a
nonlinear signed observable. First moments control transition mass only;
the explicit same-mean laws in L168 have different cutoff expectations.
Thus the inference from the existing local mean-square estimate alone
to cancellation fails. This does not rule out a proof using the actual
arithmetic distribution or establish a nonzero actual covariance.
