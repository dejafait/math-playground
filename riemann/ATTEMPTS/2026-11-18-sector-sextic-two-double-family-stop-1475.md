# Two-double-input witness family is excluded

The canonical result is
[C020s](../lemmas/C020s-sector-sextic-outer-threshold-order-and-family-exclusion.md),
with full algebra evidence in
`scripts/quartic-differential/sector-sextic-outer-thresholds-1475.json`.
Independent critical audit1476 accepts the result as stated; its full
review is in the canonical C020r/s proofs, with independent certificate
`scripts/quartic-differential/sector-sextic-independent-audit-1476.json`.
The original1475 evidence is preserved.

WHY IT FAILS: For T=1+D+tD^2 with 1/4<=t<=5/18, an input
(y^2-h^2)^2 Q(y), h>0 and Q monic real quadratic, always has at
least four distinct real output roots. If Q has a nonreal pair, the
output therefore cannot have four nonreal roots. At every real double
collision its residual quartic has four simple real roots. This defeats
the proposed witness search in the whole two-double-input family,
including the normalized C020q domain, rather than merely at the finite
tested parameters. It does not exclude general four-real-root inputs,
other allowed symbols, or products; no reduction to this family has
been established. The sextic target and RH remain open. A reopening
needs a materially different input family or operator mechanism, not
another grid in the family just excluded.
