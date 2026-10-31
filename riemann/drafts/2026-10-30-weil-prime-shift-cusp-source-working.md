# Prime-shift cusp: source-review checkpoint

2026-10-30. Literature only; no cusp expansion or coefficient has been derived.

The supplied target is a one-image expansion for an assumed L516 nullvector,
with nonzero L513 endpoint trace, at an interior prime-power displacement.
L515 gives bounded data; continuity alone does not give the requested
little-o remainder. L518's raw-adjoint cusp concerns v, not the eigenvector u.
The raw-adjoint, Abel-energy and generic-pole stops remain in force locally.

Primary reading so far:

- Chang-Lara–Saldaña, arXiv:2208.12841v3, definitions of X^alpha/Y,
  Theorems 1.1–1.2 and 4.12; Section 4.3.2, Lemma 4.14 proof,
  Corollaries 4.15–4.17 and bootstrap proof; Section 5.1.2 and
  Section 6(1). Y requires interior 1-log-Hölder data. The cutoff
  commutator proof differentiates the regular kernel away from its
  diagonal; it does not discard translated rough copies of u.
  Its open question asks for a full one-log gain from alpha-log data.
- Biswas–Roy–Sen–Sharma, arXiv:2608.07315v1, Theorems 1.1–1.2,
  weak-solution definitions, Section 3 proof excerpts. These theorems
  assume n>=2 and positive-power Hölder data. They do not directly
  cover the one-dimensional logarithmic endpoint image.
- Feulefack, arXiv:2310.02481v2, Section 3, Theorem 3.1 and its
  proof, supplies a Green-kernel lead, not a usable signed localized
  remainder. Do not import its unshifted whole-line Green formula
  in dimension one without resolving its hypotheses. The cited
  original Sikić–Song–Vondraček Theorem 3.2 was subsequently read:
  Section 3 assumes d>alpha and its proof uses alpha/2<d/2.
- bramble_trace paper 67 v1, (3.1)–(3.6), confirms the complete
  common finite signed measure; Theorem 2.4 concerns an activating
  endpoint overlap, not an interior eigenfunction expansion.

Completed source check: Feulefack arXiv:2112.08783v2 Proposition 1.2
and Section 5 give an unshifted whole-line formula and parameterwise
Bessel expansions, not the signed local remainder. No such formula
has been imported. The canonical completed comparison is
`drafts/literature/2026-10-30-weil-prime-shift-cusp-coverage.md`.
It records a source-scope NEGATIVE and nominates a finite localized
inverse test solely as unproved mathematics, with all forcing retained.
