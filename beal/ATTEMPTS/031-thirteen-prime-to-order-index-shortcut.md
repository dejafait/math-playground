# Bruin prime-to-reduction-order shortcut at thirteen — stopped

2026-10-14. [L068](../lemmas/L068-thirteen-reduction-order.md) computes
the exact entire residue-field order for E1 as 23,298,078,211,200,
with remainder zero modulo thirteen. Its canonical certificate records
all affine residues and the exact Milne extension-count specialization.
Independent critical review completed on 2026-10-14 confirms the stop:
all 19 independent checks pass in
`scripts/thirteen-reduction-order/audit-certificate.json`. Only the
canonical Bruin citation locator is corrected, to printed p.44.

WHY IT FAILS: Bruin Lemma 4.2's sufficient subgroup-index test requires
reduction-group orders prime to the residue characteristic. The single
full completion at thirteen fails that premise. Good reduction of the
curve and covering cannot replace it. This stops only the stated
shortcut at thirteen, without asserting anything about an actual
subgroup index, alternative saturation techniques, other primes,
rank or branch emptiness. Reopening this exact premise requires a
concrete correction to the count or its model/field applicability.
