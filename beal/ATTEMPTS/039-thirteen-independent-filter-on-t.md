# Thirteen-adic filter as an additional restriction on T — stopped

2026-10-17. [L088](../lemmas/L088-global-cubic-norm-thirteen-redundancy.md)
proves that every L084 T-class has square D/F norm and belongs locally
to L087's exact J13. The proof handles supported nonunit class lifts,
and its complete determinant certificate has nine checks passing.
Independent critical audit completed on 2026-10-17 confirms the stop
without correction: all 201 determinant records match and all 22 audit
checks pass. The canonical audit is in L088, with evidence in
`scripts/thirteen-global-norm/audit-certificate.json`. No full Beal
candidate exists.

WHY IT FAILS: The primitive dyadic condition makes the D/F norm
locally square at two. The complete four-class supported norm-square
family in F injects at that place, forcing its global class to be
trivial. The unramified norm at thirteen then forces the rational-root
component square; support and the other norm condition force the
remaining two classes equal. Thus J13 is already satisfied by all of
T and cannot improve its dimension bound. Reopening requires a defect
in that proof or genuinely changed conditions; testing more classes
in the unchanged T cannot establish independence. This is specific
to J13 on T, not a ban on different primes, global mechanisms or
integer constraints. The independent eleven-adic question remains open.
