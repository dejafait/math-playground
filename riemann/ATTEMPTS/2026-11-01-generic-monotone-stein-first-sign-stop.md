# Generic monotone-Stein first-sign transfer: counterexample

Date: 2026-11-01. Mathematical witness established, independent audit pending.

[L607](../lemmas/L607-sextic-monotone-stein-negative-first-sign.md)
gives an even, positive, smooth, superexponentially decaying density
proportional to exp(-u^6-4u^2), with globally nonincreasing Stein ratio
on [0,infinity), yet strictly negative first Fourier sign at x=10.

**WHY IT FAILS.** The listed generic spatial assumptions, even including
log-concavity of the auxiliary density exp(-s^3-4s), do not control the
first Fourier determinant. The bounded search succeeded in finding a
counterexample to that implication; it did not fail inconclusively and
needs no larger sweep. The precise sign certificate and all error bounds
are canonical in L607. This stops only the generic transfer route with
these hypotheses, without resolving actual-Xi signs or ruling out a
stronger Xi-specific mechanism. Audit the witness before relying on it.

Independent audit completed on 2026-11-01: both the global specialization
and strict sign survive. The proof-level review is canonical in L607;
the original certificate is unchanged and the separate error/replay
artifact is scripts/sextic/first-sign-audit.json. The pending language
above records the original state. The generic implication is now stopped
with an audited witness; stronger Xi-specific hypotheses remain open.
