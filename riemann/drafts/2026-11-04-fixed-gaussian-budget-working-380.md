# Fixed Gaussian coefficient budget — working record 380

Completed: L763, the budget stop, step380 history and PROGRESS.md record
the symbolic obstruction. The provisional notes below preserve the saved
calculation checkpoint; they no longer describe pending mathematical work.

Authorized target: determine whether one fixed Gaussian exp(-a z^2),
a>0 independent of degree, satisfies O'Sullivan's sufficient Turan budget
in every unshifted degree for the actual gamma_j.

Prior assessment: drafts/literature/2026-11-04-fixed-gaussian-unshifted-jensen-budget.md
(SPECIALIZE, supplied at invocation). Main gap remains all-degree actual-Xi
positivity. A successful budget would provide a sufficient hyperbolicity
mechanism; failure stops only this budget. No input root signs are assumed.

Local inputs read: L018, L021, L028; the October31 Hermite comparison and
the prescribed-primitive stop. No duplicate exact fixed-parameter test was
found in the narrowly searched relevant attempts. Existing work is preserved.

Primary source rechecked: O'Sullivan, arXiv:2007.13582v2, Lemma3.4,
Theorem3.5 and (3.6), Theorem8.1/(8.1)-(8.2). HTML lines260-261 display
x^(d-j) in an intermediate Gaussian identity; use the defining reciprocal
Jensen sum, whose power is x^(d-2j), and verify scaling directly.

Provisional calculation, awaiting canonical write-up and checking:
Q_d^(a)(2 sqrt(a) x) = sum_j binom(d,j) gamma_j a^((d-j)/2) H_(d-j)(x).
The budget ratio is sum_(j=2)^d d binom(d,j)/(2^j j! a^j)
times (gamma_j/gamma_0)^2. Its j=2 term is
d^2(d-1)(gamma_2/gamma_0)^2/(16a^2), forcing failure for every fixed a
eventually. Only gamma_0,gamma_2>0 is needed, supplied by L021.

No numerical certificate or new mathematical script is needed: all sums
are finite and the obstruction is symbolic. No RH candidate is claimed.
