# L462 critical audit — source-scope assessment

TARGET: Critically audit L462's conditional interior-anchor signed-tail obstruction, including the two L461 instantiations, four epsilon losses and uniformity in every allowed K.
CHECKED: 2026-10-25
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the exact-statement, Taylor-section and stronger-result searches recorded in the interior-anchor construction assessment; compared full L462 and L461 (including its dated audit), L018, L322's statement and smaller-circle proof, the local failure record and relevant October 25 histories. No fresh external search or originality claim.
SOURCE_EVIDENCE: Reused the construction assessment's inspected statement and full proof of Grava, Complex Function Theory (December 29, 2024), section 4.4 Lemma 4.16, printed p. 42 (PDF p. 46), and DLMF 5.11.9 with bounded-real-part uniformity. Reused L461's saved audit coverage for Titchmarsh second edition (1986), Theorem 14.2 proof pp. 336–337, especially (14.2.5)–(14.2.6), and its retained pinned external premise.
COMPARISON: The audit requires the same source mechanisms and fixed-parameter domain already assessed for construction. Neither Grava nor L322 directly states the conditional interior-anchor conclusion. L461 supplies the combined estimates to be instantiated twice; correctness of that application, model multiplication and uniform finite-sum bound remains for mathematical review.
GAP: Essential source coverage is adequate; the independent mathematical audit of L462 remains undone. Verify each parameter order, the explicit model rather than an anchor upper bound, shifted complex heights, all losses, positive denominator, strict decay margin and uniformity for every allowed integer K.
REASON: This separate scope comparison changes REVIEW_REQUIRED to SPECIALIZE for the unchanged audit target; approve one later REPRODUCTION audit without deriving or certifying L462 in this literature-only step.
SCOPE: Actual Xi; fixed 3/8<eta<1/2, 0<=c<eta/2 and B>=0; all real centers and integers 0<=K<=c log(2+|a|)+B; precisely L461's retained external premise. No external-manuscript audit, moving anchors, endpoint conclusion or signs.
LITERATURE_REASON: The invocation-start assessment was REVIEW_REQUIRED for this newly nominated audit. This turn fills that specific scope comparison using adequate saved coverage, without repeating external browsing or extending the target.

## Main gap and bounded test

Initial low-index signs at unbounded heights and global mixed positivity
remain unproved. The intermediate target is independent scrutiny of
L462, so that its conditional fixed-anchor small-tail stop can be used
when choosing further sign or witness work. It supplies no signs.
Continue to the audit because every source mechanism lies in existing
coverage. Pass only if the complete stated quantifiers follow with fixed
parameters and constants independent of a and K; otherwise identify the
first unsupported bound and restrict the route stop accordingly. This
coverage review makes no correctness verdict.

## Reuse and applicability boundaries

The [construction comparison](2026-10-25-interior-anchor-signed-tail-barrier.md)
records the queries, inspected primary passages and nearby finite-height
Laguerre theorem. Those searches concern exactly the fixed interior-anchor
domain and cutoff now under audit. They are reused, not represented as
new searches or evidence of novelty. Nearby positivity sources and unread
leads do not become inputs to the audit. The separate
[L461 audit coverage](2026-10-24-l461-witness-cutoff-critical-audit-coverage.md)
and L461's dated canonical audit cover its changed-domain logarithm,
strip and anchor argument; their external-premise qualification persists.

Grava, [Complex Function Theory](https://people.sissa.it/~grava/cft.pdf#page=46),
December 29, 2024, section 4.4 Lemma 4.16, assumes analyticity on a domain
containing the closed disk and a boundary modulus bound. Its differentiated
Cauchy formula and contour-length proof give the derivative estimate at
the center, for every nonnegative order. The saved assessment inspected
the full statement and proof. L018 supplies the proposed entire-function
input. Evaluation of a finite polynomial outside the disk does not change
the cited estimate's hypotheses; the resulting finite sum and height
majorant still require independent local verification. No direct import
of a signed-tail limit is available from this citation.

[NIST DLMF 5.11.9](https://dlmf.nist.gov/5.11.E9) covers vertical gamma
moduli at both infinite-height signs uniformly for bounded real parts;
the construction and L461 audit assessments inspected this uniformity.
Reuse their 5.11.1/5.11.3 sector/remainder coverage as well. This is
support for L461, not an all-height lower bound by itself. Compact-height
positivity and nonvanishing must remain justified locally.

Titchmarsh, second edition revised by Heath-Brown (1986), Theorem 14.2,
proof pp. 336–337, particularly (14.2.5)–(14.2.6), is reused through the
saved source comparison and audited L461. The printed theorem assumes RH;
it cannot be directly imported under a substituted 7/8 boundary. No new
logarithm derivation or reopening of the external theorem is authorized.
The retained September 30 Theorem 1.1 is at commit
`1581d4cbdd69a0faf34b2089614fe2a814316a6a`: strict Re(s)>7/8, pole
allowed, boundary not excluded, manuscript/import closure locally
unaudited. No stronger zero-free premise enters this audit.

## Obligations reserved for the mathematical audit

L462's direct local inputs are L018 and L461. The full canonical texts
were read to compare scope, not to certify their application. L322's
statement and equations (4)–(6) establish the earlier exterior-anchor
mechanism; its eta>1/2 hypothesis does not cover this interior domain.
The [current failure record](../../ATTEMPTS/2026-10-25-interior-anchor-small-tail-comparison.md)
and relevant histories stop only the specified small-tail comparison.
They preserve exterior/ellipse evidence and leave moving anchors and
other comparisons open. No second obstruction proof or ellipse analysis
is needed for this audit, and L322 is a comparison rather than a direct
mathematical input to L462.

The audit must inspect, without assuming its answer:

- Both independent L461 instances, (alpha,r) and (eta,R_*), their strict
  anchor-before-radius inequalities, and separate constants. Check that
  multiplication uses the explicit positive model A_1 rather than an
  upper bound on the actual anchor H_a(alpha).
- The full complex-circle estimate with both shifted heights, including
  crossing zero, and the separate positive all-height denominator. Keep
  central zeros and arbitrary multiplicity admissible.
- All four epsilon losses, the existence of fixed
  max(3/8,2c)<r<eta, and epsilon<delta0/4. Verify the strict decay margin
  and fix every parameter before constants or varying heights.
- Cauchy's estimate for each even coefficient, the finite geometric sum,
  and independence of the bound from every integer K in the stated range,
  including c=0 and K=0. Keep B fixed, and check that the difference is the
  actual Taylor remainder without an infinite-limit interchange.
- The final small-tail impossibility claim only for positive lower bounds
  at the same fixed anchor; exclude endpoint c=eta/2, moving-anchor bounds,
  sign claims and RH conclusions.

No source outside the already assessed scope is essential to these checks.
Full matching Mathlib coverage and supporting analytic APIs remain
unchecked; absence is not claimed. The classification for the later audit
is REPRODUCTION under SPECIALIZE. This assessment changes coverage only:
L462's independent audit remains pending, all original evidence is
preserved, and lemmas, scripts, DAG and PROOF.md are unchanged this turn.
