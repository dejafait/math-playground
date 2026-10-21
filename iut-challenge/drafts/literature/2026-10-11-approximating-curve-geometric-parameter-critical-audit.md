# Approximating curve geometric parameter — approved audit coverage

TARGET: Critically audit L048's strengthened-precision split reduction and geometric Tate valuation, including same-curve retention of L045–L047.
CHECKED: 2026-10-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the completed construction assessment and primary-source comparisons for L044–L047; inspected L048, the input hypotheses, relevant audit records, histories 155–156 and ATTEMPTS/027. No completed duplicate L048 audit or new essential source gap was found; no renewed external discovery was needed.
SOURCE_EVIDENCE: Reused inspected Milne EC2 (2021) II.2 Theorem 2.4 pp.52–53, II.3 pp.58–61, III.3 (23)–(26) pp.102–103; Cremona second edition (1997) III.1 (3.1.2)–(3.1.3) pp.62–63 and III.2 multiplicative/p=3 branches pp.66–67 with 2003-09-26 errata; Kedlaya fall-2004 Theorem 2 p.4; the completed L044–L047 audit assessments cited below.
COMPARISON: Known integral invariant and transformation laws, general-characteristic nodal criteria, the p=3 multiplicative branch and Tate parameter theorem cover the written audit obligations. Their exact application to L048 and simultaneous same-curve retention still require independent mathematical verification; no stronger constancy theorem or new theorem is needed.
GAP: Coverage is ready for the exact audit TARGET; L048's polynomial identities, product and precision bounds, general-model minimality, residue geometry, parameter valuation and same-curve retention have no independent audit verdict from this turn.
REASON: The new audit scope has now been compared with reusable primary hypotheses and the actual local inputs; this supplies the separately requested coverage approval without deriving or validating mathematics.
LITERATURE_REASON: The startup REVIEW_REQUIRED gate requires separate approval for the newly proposed audit outside construction scope; all essential coverage is reused and no additional literature turn is proposed.

SCOPE: Exactly TARGET for L048's original integral monic cubic, M>=max(M_tors,31), absolute v_3(3)=1 and one curve reselected at fixed precision; includes auditing all four direct inputs and their retained embedded Omega,H,N, but no sufficient initial-data or original-IUT conclusion.

## Preserved proposal — source status superseded by completed review below

The main gap remains original finite B>=A. The intermediate target is
the exact TARGET above. A passing audit would validate the newly
closed local geometric prerequisite; a failure should identify and
repair or isolate the load-bearing model, invariant or retention step.
This is not an audit of a complete IUT-flaw candidate.

Essential local inputs are L048, L044, L046 and the downstream
same-curve L045/L047, retaining L042's Omega,H,N through them.
Check all of L048's hypotheses and the integer M>=max(M_tors,31).
Verify the integral discriminant polynomial, u=1 completion-of-square
identification, full product convergence, exact discriminant valuation,
unit c4 and minimality against general integral Weierstrass models.
Check the unique singular point, smooth infinity and distinct rational
tangents over F_3 using the general criterion; compare the inspected
Cremona p=3 branch. Apply Tate Theorem 2 to the actual changed curve,
and verify the complete integral expression proving v_3(q_0)=30.
Finally check fixed precision before L046's reselection and unchanged
hypotheses for L045/L047 applied to that same E_0.

The preceding construction assessment retains direct primary links,
theorem/page numbers, inspected cases and qualifications. Its search
and duplicate evidence should be reused; no broad renewed discovery
is proposed. Source approval and the mathematical audit are separate
invocations. This proposed assessment is not a new lemma or an audit
verdict and has no currently ready decision.

Unresolved assumptions for downstream use: sufficient initial data,
other-place conditions, native/input/action, marked pilot transport,
essentiality and original finite B>=A. Do not assume q_0=3^30 or
transfer a field-normalized valuation. ATTEMPTS/027 and the distinct
packet stops ATTEMPTS/022,025,026 remain intact. Full matching
Mathlib coverage remains unchecked; no absence claim is made.

## Completed coverage comparison — 2026-10-11

This is a source-scope review, not the mathematical audit. The proposal
above is preserved as the initial review request; its statements that
coverage has no ready decision are superseded by SPECIALIZE here.
The exact TARGET is unchanged. The main gap remains original finite
B>=A, and a successful later audit could validate one local geometric
prerequisite for an eventual sufficient-initial-data test.

### Reused primary statements and their audit roles

The full construction comparison in
`drafts/literature/2026-10-11-approximating-curve-geometric-tate-parameter.md`
records the inspected versions, queries, theorem hypotheses and cases.
No external source was newly retrieved in this turn. Reuse is justified
because the curve family, field, normalization and imported criteria
have not changed; only the task changes from construction to independent
verification of the written specialization.

- [Milne, Elliptic Curves, second edition (2021)](https://www.jmilne.org/math/Books/EC2.pdf),
  II.2 Theorem 2.4 and pp.52–53, provides general Weierstrass invariants
  and pointed coordinate changes. II.3 pp.58–61 uses a minimal equation
  and distinguishes a node with rational tangents from the nonsplit
  case; its general criterion permits characteristic 3. III.3
  (23)–(26), pp.102–103, supplies integral Tate coefficients and the
  complete discriminant product and j-expression. These are the
  inputs for checking the cubic, the completion of square, convergence
  and valuation, rather than a ready proof of L048's precision bound.
- [Cremona, Algorithms for Modular Elliptic Curves, second edition (1997),
  Chapter III](https://johncremona.github.io/book/fulltext/chapter3.pdf),
  III.1 (3.1.2)–(3.1.3), pp.62–63, supplies invariant scaling under
  general coordinate changes. III.2 pp.66–67 includes the p=3
  coordinate adjustment and the unit-c4 multiplicative exit with its
  residue quadratic. The algorithm accepts integral equations without
  a minimality assumption. Reuse the previously inspected
  [2003-09-26 errata](https://johncremona.github.io/book/errata.pdf);
  no relevant correction changes these branches. General-model
  minimality and the actual residue quadratic must still be audited.
- [Kedlaya, Introduction: the Tate curve, fall 2004](https://kskedlaya.org/18.727/tate-curve.pdf),
  Theorem 2 p.4 assumes a finite extension K/Q_p and |j(E)|>1.
  It gives a unique q in K with 0<|q|<1 and a geometric Tate
  isomorphism, defined over K precisely in the split multiplicative
  case. Import the named theorem without reproof; its proof discussion
  cites Silverman V.5.3, not newly inspected here. Audit the valuation
  using Milne's normalization, retaining the prior warning about
  Kedlaya's displayed a4 formula. No coefficient formula from that
  warned display is authorized as a replacement.

The broader Schrettner regular-model result was compared in the
construction assessment and does not supply minimal-model constancy.
It is unnecessary here. Its full proof and original Tate/Silverman
proofs remain unread leads, not claimed inspected coverage.

### Same-curve inputs and duplicate/failure comparison

Reuse the completed assessments
`drafts/literature/2026-10-11-finite-torsion-global-curve-critical-audit.md`,
`drafts/literature/2026-10-11-global-torsion-adjunction-critical-audit.md`,
`drafts/literature/2026-10-11-mod7-approximation-critical-audit.md`, and
`drafts/literature/2026-10-11-restricted-mod7-image-critical-audit.md`.
Their precise primary citations cover finite m=210 module constancy,
embedded completion identities and degree divisibility, fixed-level
counting and pointed rational transport, and restricted SL_2 image.
L044–L047 record completed independent audits. This turn read their
hypotheses and the relevant L044/L046 audit records to compare scope;
it did not repeat their full mathematical proofs.

L046's hypothesis permits any fixed sufficient M. L045 requires the
chosen L044 curve's full local torsion conclusions, and L047 requires
that same curve with L046's global image and L045's field. These
requirements match the retention obligations written in L048; checking
that they all hold simultaneously is left to the proof audit. No
uniform-in-M estimate, global rational torsion over the smaller field,
full GL_2 image over F, or exact q equality is an imported conclusion.

Histories 155–156 record source comparison and construction only;
L048 still explicitly awaits audit. ATTEMPTS/027 excludes the exact
old curve, not changed curves retaining finite modules and parameter
valuation. The distinct packet exclusions 022,025,026 are contrasts,
not new hypotheses or bans. No new result or novelty claim follows
from this duplicate/failure comparison.

### Approved discriminating test and qualifications

The later research turn must independently check every listed audit
obligation in the preserved proposal, including all integral invariant
identities, strict error valuation at the stated precision, general
integral-model minimality, smooth infinity and rational distinct
characteristic-3 tangents, the complete convergent Tate expression,
and fixed precision followed by a single same-curve application of
L045–L047. Pass only if all hold under L048's exact hypotheses.
Otherwise isolate the failing identity, source hypothesis or retention
step and record its consequence; finite-module agreement cannot replace
the geometric tests. No such computation or verdict is performed here.

Essential continuation inputs are L048, direct inputs L044–L047,
and their retained L042 Omega,H,N. Keep q_0 distinct from 3^30 and
absolute valuation distinct from valuations normalized in H or N.
Other-place conditions, sufficient initial data, native/input/action,
marked pilot transport, essentiality and original finite B>=A remain
unresolved. Full matching Mathlib coverage is unchecked, without an
absence claim. No reproof of named theorems or mathematical script is
needed for this audit. Its expected classification is REPRODUCTION.
