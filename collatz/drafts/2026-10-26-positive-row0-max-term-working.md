# Step513 working record — coupled maximum-term relaxation

Invocation-start assessment:
`literature/2026-10-26-positive-row0-max-term-feasibility-test.md`
(EXPLORE; unchanged). Main gap: universal descent. Intermediate target:
the approved log25-loss necessary relaxation of all25 own-input J guards
on the literal d35 positive-row0 simplex. A complete exclusion would
cover those remaining supports only; actual-word transfer, other orders,
entry, unrestricted cycles and divergence remain separate.

Read the supplied overview/DAG and assessment, the omitted step511
source comparison, Attempt032/033/034, L055's table and affine formulas,
L104's enclosure proof/audit, and L106 through equation(9). Scoped search
found no already recorded cumulative-product-minimum exclusion in the
relevant L10*/C10* proofs and failure files. Existing edits are preserved.

## Saved partial reasoning before certificate work

Let C_i=product_(j<i)c_j, P=C25 and D=P^-1-1. For every allocation,
the same totals match L104; the affine formula must be specialized
again to show one common cyclic tuple and all25 cut identities. If
T_(i,k)=eta_(i+k)/P_(i,k) and g_i=(4/11)2^(4J_i), the known
25-term maximum inequality gives the necessary condition
max_k T_(i,k)>=D(g_i-kappa)/25, retaining the exact shift.

Potential complete exclusion to check: choose a minimum of C0,...,C24.
Since b0>=1 gives c0<=3^29/2^57<1, its index r cannot be0.
For a nonwrapping cut term, reciprocal prefix is C_r/C_j<=1;
for a wrapping term, it is C_r/(P C_j)<=P^-1. Thus every term
at r is <kappa/P. The audited denominator gives D>10^-10 and
P^-1<2, while every J_r with r>=1 is at least15. This compares
max term <46/11 against a necessary value
>(2^62-23)/(275*10^10). Check the exact signs, all wrap identities,
the general-allocation formula and the complete table before claiming
exclusion. This minimum is a derived finite-prefix choice, not an
assumed minimum junction or a reordering of the word.

The bounded test was complete exclusion versus one certified feasible
relaxed allocation. The finite-minimum mechanism yielded complete
exclusion. Final proof and citations are in L107; exact operands and all
prefix coverage are in
`scripts/postspell-word-count/d35-positive-row0-max-term-certificate.json`.
There were2699 passing checks, no failures and no allocation samples.
This record preserves the initial partial reasoning; it is not a second
proof or current next-action record. Separate critical audit remains.
