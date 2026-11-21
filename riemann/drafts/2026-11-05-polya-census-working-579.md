# Bounded census working checkpoint, step579

Approved target: the exact implementation TARGET in the supplied assessment
2026-11-05-polya-census-implementation.md. Reuse its SPECIALIZE coverage.
Inputs read: L016/L019/L020/L021/L814, step578 source comparison and
step575 failed-sign working record. No reference-zero theorem is assumed.

Attempt: implement outward Decimal interval boxes on u in [0,3], n<=4,
x in [0,40], with fixed finite caps, and preserve every undecided cell.
Use direct same-sign F,G exclusion or W exclusion; no center scan is evidence.
Normalization and all orders 0,1,2 get complete series/integral tails.
This slower method deliberately accepts unresolved cells rather than
assuming installed Arb or its integration contract. New explicit bounds
will be canonical if used; implementation and results will need an audit.
