# Polymath uniform-tail audit working record

2026-10-30. Approved target and scope: the unchanged SPECIALIZE assessment
`drafts/literature/2026-10-30-polymath-uniform-tail-audit.md`.
One mathematical audit; no new saddle estimates or finite-collision claim.
Existing notebook changes are preserved.

Main gap: actual-Xi all-degree mixed positivity. Intermediate target:
one real/simple zero tail for F on 0<a<=lambda<=b<=1/8. Its possible use
is removal of escape to infinity before a bounded-height collision test.
Continue only if a strict circle count and complete high-zero exhaustion
have a common time threshold; otherwise record the failed comparison.

Primary passages inspected: Polymath arXiv:1904.12438v2 Theorem 1.5(i)–(ii),
absolute-constant convention, Proposition 9.1(i), Lemma 9.2 and (102)–(104),
and Theorem 3.2's cited strip bound. Reused prior source/failure comparison.
L018/L019/L058 normalizations and L126/L128 limitations checked narrowly.

Partial reasoning saved before completing the audit: set w=z-x_n,
A=(1/4)log(x_n/(4pi)), beta=pi/8 and M=M_t((1+i x_n)/2).
The two exponents in (102) share the EXACT factor exp(-beta w).
Together with (103), division by 2i M exp(-beta w) leaves sin(Aw)
with error bounded by a constant times
(x_n^(-kappa t)+log(x_n)/x_n)(|exp(iAw)|+|exp(-iAw)|).
Thus the displayed O(|y|log x_n) in (104) need not be used on circles.
Still to finish: strict boundary constants, nearest-center phase exclusion,
n/x threshold compatibility, compact-time/reflection specialization.
No conclusion is claimed by this partial checkpoint.

## Completed audit

The bounded test passed. The full replay and restricted specialization
are canonical in [L488](../../lemmas/L488-polymath-compact-positive-time-simple-tail.md).
It retains the exact exp(-pi w/8) factor, proves a strict Rouche margin,
counts multiplicity, bounds the nearest-center phase by 3pi/4, and
exhausts the high strip before making both thresholds uniform in time.
The printed coarse (104) is insufficient alone, not refuted. The source
asymptotics and strip theorem remain imports; no manuscript-wide audit
or progress beyond the published tail theorem is claimed.

No mathematical script was needed. The new transition nomination is
REVIEW_REQUIRED; it was neither derived nor approved during this audit.
