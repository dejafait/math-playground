# 478 — 2026-10-25: exact reflected coefficient extraction

Completed the prior SPECIALIZE target as a reproduction of known
finite-dimensional Laplace/cumulant mathematics. Canonical
[L279](../lemmas/L279-fixed-mesh-exact-reflected-coefficient.md) gives
the exact two-insertion coefficient and fixed-mesh remainder, using
L003's forest reduction and leading curvature law, L011's density and
connected-expansion method, and Kirwin v2 Theorem 2.1. Both moving means
and all required jets are explicit. This is local mathematical progress,
not a claim of mathematics beyond the checked sources.

The reusable nonzero-cubic generic Gaussian check matches independent
normalized moment division exactly: both second coefficients are 47/80,
with zero difference and no failed checks. Full inputs and evidence:
`scripts/exact-reflected-coefficient/cumulant-certificate.json` (not a
four-dimensional box evaluation). The scratch preflight is preserved in
[the work record](../drafts/2026-10-25-exact-reflected-coefficient-work.md).

This does not bound cutoff growth, the higher-order uniform remainder,
or the c_box/2 error on a physical trajectory. The continuum,
nontrivial-sector and finite-positive-mass gaps remain. Prior scalar-only,
direct-import and Ward-substitution limitations remain in force for
their respective approaches. The newly registered
[critical-audit scope](../drafts/literature/2026-10-25-exact-reflected-coefficient-critical-audit.md)
requires separate approval; no independent audit or changed repair is
claimed. Existing unfinished notebook work was preserved.
