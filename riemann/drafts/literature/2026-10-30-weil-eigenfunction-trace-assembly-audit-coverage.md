# Fixed-interval eigenfunction trace assembly — proposed audit coverage

TARGET: Critically audit L514–L515's discharge of L513's domain-split and bounded-data premises for fixed-interval signed-measure eigenvectors.
CHECKED: 2026-10-30
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the unchanged primary-source searches and scope comparisons in the half-line-domain-split and eigenfunction-boundedness assessments below; the target is critical review of their completed specializations, not a new mathematical mechanism or hypothesis.
SOURCE_EVIDENCE: Direct primary sources: Yafaev v2 https://arxiv.org/html/1210.5709v2 (1.2)–(1.4); Chen–Weth v6 https://arxiv.org/html/1710.03416v6 Theorem 3.1; Kato https://webhomes.maths.ed.ac.uk/~v1ranick/papers/kato1.pdf VI.1.33/VI.2.1; Engel–Nagel https://www.math.uni-tuebingen.de/de/forschung/agfa/members/engel-nagel_one-parameter-semigroups.pdf III.1.3/1.9–1.10; GR v1 https://arxiv.org/html/1107.0745v1 Section 2; paper 67 v1 https://rstation.ai/problems/riemann_hypothesis/papers/67 (3.4)–(3.8). Access and the selected statements/proof cases below were checked in the separate recovery literature turn; earlier full proof reading is reused.
COMPARISON: These standard inputs cover the fixed-reference domain split and the arbitrary finite signed convolution specialization of the manuscript's smoothing bound. A critical application audit must still check the actual local closure arguments, atomic domination and convergence topology; source coverage is not a correctness certificate.
GAP: Independently check both form-domain inclusions, the product operator domain, L515's finite-measure Dyson induction and identification of the time-one stronger-norm sum, then match every L513 premise. Do not broaden to full-Weil identification, collars, varying operators or near-null flux bounds.
REASON: The separate recovery literature turn repairs missing direct source URLs and confirms unchanged theorem scope. SPECIALIZE remains appropriate for the saved critical audit; no critical audit of the assembled proofs or new mathematics is claimed.
LITERATURE_REASON: Supervisor required direct primary-source URLs in this ready assessment before the saved audit; reuse unchanged coverage and repair traceability only.
SCOPE: Fixed ell>0, c real, arbitrary finite real even signed Borel mu including atoms; G_I is the smooth-core part operator with Psi(xi)=(1/2)log(1+xi^2); all complex eigenvectors of A_I=G_I-cI-K_mu. No arithmetic uniformity or actual-Weil realization is included.
COVERED_TARGET: Critically audit L514–L515's discharge of L513's domain-split and bounded-data premises for fixed-interval signed-measure eigenvectors.

## Reused coverage and bounded test

The source statements, inspected proof cases and original searches are
in [the domain-split assessment](2026-10-30-weil-half-line-domain-split-coverage.md)
and [the smoothing assessment](2026-10-30-weil-eigenfunction-boundedness-coverage.md).
The [trace-input assessment](2026-10-30-weil-renewal-trace-input-coverage.md)
covers L513's retained conditional theorem. No new search or novelty
claim is made, and no new literature turn is claimed by this reuse note.

Essential local inputs are L513's conditional trace theorem and the
new L514/L515 proofs. The review should focus on the genuine logical
risks: whether finite-energy restrictions lie in the stipulated smooth
core closures; whether both form-domain inclusions precede representation;
whether the cross term is an actual bounded L2 operator; whether
domination is valid for signed atomic convolution and complex vectors;
and whether the time-one L-infinity limit is proved independently of
L2 convergence. Inspect the complete relevant arguments rather than
only their concluding bounds. The cited source proofs are imports.

Continue if the core closures, operator domain, time-one bound and
all L513 hypotheses pass. If a specific implication fails, retain
the original conditional theorem and record the exact failed premise;
do not turn an analytic failure into an RH counterexample. Full-Weil
realization and the arithmetic relation between traces and eigenvalues
remain unresolved even if every fixed-model check passes. Mathlib
matching coverage remains unchecked. No cross-notebook input.


## Separate source-traceability review, 2026-10-30

The six direct URLs in SOURCE_EVIDENCE were opened successfully. The
following is a source-scope check, not a review of the completed local
proofs. Earlier full-source inspections remain in the two reused
assessments; this turn did not repeat their searches or derive lemmas.

- [Yafaev v2](https://arxiv.org/html/1210.5709v2), (1.2)–(1.4),
  identifies the Carleman kernel and its Mellin multiplier. Reflection,
  restriction and the reference kernel's factor one-half remain local
  application checks, as previously assessed.
- [Chen–Weth v6](https://arxiv.org/html/1710.03416v6), (3.1)–(3.7),
  Theorem 3.1 and proof (i), was checked through the boundary-cutoff
  estimate and start of mollification (ii). Density concerns the full
  zero-exterior energy on a bounded Lipschitz domain. The proof uses
  the killing weight to control the boundary layer. Its remaining
  mollification proof is reused from the earlier assessment. It does
  not assert a general half-line density theorem.
- [Kato, reprint of the 1980 edition](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/kato1.pdf),
  VI.1.33, printed pp. 320–321 (PDF pages 342–343), and VI.2.1,
  printed p. 322 (PDF page 344), were checked, together with the
  core-testing proof on pp. 324–325. The first requires relative form
  bound less than one; the second requires a densely defined closed
  sectorial form. Core testing presupposes membership in the form
  domain. They do not bypass either domain inclusion in L514.
- [Engel–Nagel (2000)](https://www.math.uni-tuebingen.de/de/forschung/agfa/members/engel-nagel_one-parameter-semigroups.pdf),
  III.1.3, printed p. 158 (PDF page 173), and III.1.9–1.10,
  printed pp. 162–163 (PDF pages 177–178), were checked, including
  the perturbation proof and convergence statement. The perturbation
  is a bounded operator on the same Banach space. Dyson integrals
  are strong-operator integrals; the sum converges in operator norm
  on that space uniformly on compact time intervals. An L2 use does
  not itself establish the L2-to-L-infinity limit needed by L515.
- [Grzywny–Ryznar v1](https://arxiv.org/html/1107.0745v1), Section 2,
  was checked from the characteristic exponent through (2.4) and
  the following killed-density formula. The source includes alpha=2,
  exponent log(1+xi^2), and domination by the whole-line density.
  The notebook uses half speed. Matching the killed form realization
  is an application obligation; killing after subordination must not
  be replaced by subordinating killed Brownian motion.
- [bramble_trace paper 67 v1, 27 October 2026](https://rstation.ai/problems/riemann_hypothesis/papers/67),
  Section 3.1 after (3.6) and Section 3.2 (3.7)–(3.8), were
  checked. The source already claims the domain split and signed
  measure time-one bound, including atoms. These are the claims
  under audit, not independent correctness evidence for L514–L515.

The narrow duplicate/failure screen reused the prior assessments,
previous boundedness-audit history, and the recorded support-propagation
and rank-trace stops. Neither stopped implication is reopened: fixed
model boundedness supplies no near-null eigenvalue-relative flux control.
No source blocker was found. No novel result or Mathlib match is
claimed; Mathlib remains unchecked. No cross-notebook input is used.
The exact target, continuation test and exclusions above remain unchanged.
