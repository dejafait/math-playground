# Conditional prime-twist certificate — critical audit

STEP_ID: BSD-2026-10-07-067-prime-twist-certificate-audit

The approved target is the mathematical audit of L028 under
`drafts/literature/2026-10-07-prime-twist-certificate-critical-audit.md`.
Main gap: rank E(Q)=m(E) for m(E)>=2. Intermediate target: verify the
conditional exact normalization and uniform denominator certificate.
Downstream use: L027's exact symbol and all-level C premises, followed
only when its strict error threshold excludes zero. Continue only if
scale, sign, period, full-relative extension and lattice generation all
follow from the stated premises; stop an implication requiring extra data.

Pre-audit checkpoint: read all of L028, L027's hypotheses and relevant
normalization requirements, ATTEMPTS/022 and history/065--066. The provided
source assessment is reused. No actual relative presentation, certified
integration line, independent q, C or coefficient has appeared. The audit
must not promote these premises to constructed data. Existing changes are
preserved. Primary formula verification and final disposition are pending.

## Completed disposition

RESEARCH / REPRODUCTION / EXPLORATION. The bounded critical test passes
under exactly L028's granted data. No error needing repair, new arithmetic
input, numerical certificate or advance beyond the sources checked was
found. This is one mathematical exploration turn, not a budget reset.
The complete proof and citations remain canonical in
[L028](../lemmas/L028-prime-twist-normalization-and-uniform-denominators.md).

The primary passages were opened to check the proof, not to reopen source
coverage: Stein Definition 1.23, Proposition 1.24 (including integral
continued fractions), Theorem 1.25 and Remark 1.26; Cremona corrected
second edition Sections 2.1 and 2.11, pp. 9--10, 38--39; Pal
arXiv:1012.0094v2 Corollary 2.6 with proof and Theorem 3.2's entire
positive-d case; Stein--Wuthrich Section 3, p. 1762. The URLs and precise
specializations are in L028. No essential source was inaccessible today.

Audit findings, by the proof's load-bearing stages:

- Presentation: all relations and torsion removal are required, and the
  cited integral generation applies at weight two. Rational relation
  checks annihilate the saturation; they do not certify completeness.
- Calibration: coprimality to Delta ensures the prime-to-N condition.
  The character sum removes the change of base cusp without reversing
  paths. Cremona's positive real Gauss sum gives the sign used in (4).
- Period: Pal's positive-twist proof uses the full real locus. Its
  corollary removes the minimalization factor in precisely this case;
  connectedness introduces no extra factor in (3).
- Relative scope: evaluating at G_ell fixes the scalar only because the
  integration line was already certified on the whole relative module.
  A nonzero value cannot itself certify that line. The proof never uses
  nonvanishing of the untwisted central value.
- Plus convention: the path-conjugation calculation in (5) matches
  Stein--Wuthrich's two integrals and its total-period denominator.
- Denominators: every integral generator is evaluated after calibration.
  The valuation bound uses integral coefficients, including after
  relation saturation; zero coordinates are harmless. No bound is
  inferred from an arbitrary rational basis or sampled cusp paths.

No direct local mathematical input was added to L028; its downstream
references are uses, not premises. DAG and PROOF are unchanged because
the argument has not changed. No mathematical script or numerical check
is relevant without actual data. Mathlib coverage remains not checked.
L027's required strict bound remains min(n-1-C,M-C)>v_p(b); no actual
side of that comparison is available. Rational membership, F, divisible
Sha and the comparison with complex order remain unresolved.

## Recovery and next-direction comparison

Repeated conditional calibration audits are now parked in ATTEMPTS/023,
with ATTEMPTS/022 unchanged. Three directions were compared:

1. Certify the full relative integration line by exact Hecke and real-
   involution operators and a certified one-dimensional simultaneous
   kernel. This addresses L028 hypothesis 2 independently of twist
   values; it is selected for source review, not proved here.
2. Produce independent q through a certified modular parametrization,
   periods and isogeny data. This addresses a separate scale gap but
   needs additional unassessed normalization inputs; defer it.
3. Sharpen the already conditional p-adic tail bound. This still lacks
   actual symbols and is stopped by ATTEMPTS/022; no new mechanism.

The selected target requires full-relative operator compatibility and
integration equivariance, not merely a vector with matching eigenvalues.
The existing normalization assessment explicitly grants this identification
and therefore does not cover its production. A new REVIEW_REQUIRED
assessment records the exact target and its independent test. No theorem
about that target is derived or approved in this turn.
