# Supported ambient dimension does not meet the rank threshold

2026-10-26. The complete specialization and precise citations are
canonical in [L139](../lemmas/L139-pair-supported-norm-dimension-bound.md).
The supported norm kernel has dimension 11+c<=13, where 0<=c<=2 is
the ordinary localized class contribution. Rational Jacobian two-torsion
has dimension one, giving rank at most 10+c<=12.

WHY IT FAILS: The required numerical rank upper bound is one. The
obtained bound twelve exceeds it by eleven; even eliminating the entire
class contribution leaves the same ambient method with bound ten.
Thus this dimension-only shortcut ends, without asserting a rank lower
bound or Selmer equality. Further local filtering or a different
mechanism would require its own justified target and coverage. This
does not ban general descent. Earlier route stops and unfinished L108
are preserved. The separate critical audit of L139 on 2026-10-26
accepts this bound and shortfall without a mathematical correction.
