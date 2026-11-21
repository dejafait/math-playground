# Unrounded GMP execution: bounded segment incomplete

The unchanged C033y/C033z evaluator was integrated with an exact GMP rational
backend, restoring the replayed1816 prefix. Execution1823b saved15/780 profiles
and0/8 scalars in its300-second segment; independent replay completed six
profiles before its own300-second limit. Full evidence, source qualifications,
debugging failures and replay boundaries are canonical in
[C033z](../lemmas/C033z-direct-positive-real-stable-inner-arithmetic.md),
execution1823. Preserve every1823/1823a/1823b artifact and certificate.

WHY IT FAILS: This bounded segment did not finish the eight scalar outputs,
complete replay or accounted required-path cap. Exact GMP fixes the arithmetic
integration seam and permits additional profiles, but does not itself bound
denominator growth, memory or runtime. An operational timeout is no proof
that the arithmetic or RH is impossible. Further repetition of the unrounded
execution is parked; a different, independently testable width-constructor
cost target is proposed for a separate source review. Its success, any
resulting rounding scheme, all scalar assertions and the RH gaps remain open.
