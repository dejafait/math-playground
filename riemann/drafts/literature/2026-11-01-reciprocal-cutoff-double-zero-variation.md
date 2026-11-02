# Reciprocal-cutoff double-zero variation: bounded calculation scope

TARGET: Compute the reciprocal-cutoff first variation and leading first-sign term at an assumed double real zero of Xi, with a uniform remainder and any shifted-Xi sign input left explicit.
CHECKED: 2026-11-01
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed small-cutoff multiple-zero source comparison, including exact reciprocal-cutoff/first-variation queries and scoped theta/cutoff/heat duplicate searches. No inspected source gives this specific local expansion; no novelty claim follows.
SOURCE_EVIDENCE: Direct sources rechecked 2026-11-01: https://www.math.stonybrook.edu/~cschnell/mat545/class2.pdf (Definitions 2.5-2.6, Theorem 2.8, pp.2-3); https://www.mat.univie.ac.at/~armin/publ/handbook_paper.pdf (2024-10-07, Theorem 2.2 and Puiseux discussion, p.7). L019 supplies the exact kernel and dominating superexponential bound; L020 supplies its entire cosine transform. The completed review reads Schnell Class 2 Theorem 2.8/proof, Parusinski--Rainer Theorem 2.2/Puiseux discussion, de Bruijn Theorems 10-12 and Newman Theorem 1, distinguishing preparation and Gaussian preservation from the actual weight. Original collision scans remain unimported and are unnecessary to this calculation.
COMPARISON: Generic differentiation/Taylor expansion covers the method; the remaining specialization is the exact reciprocal parameter derivative, its justified shifted-Xi expression and its contribution to the first form at a double zero. No preservation or shifted-value sign theorem was found in the bounded comparison.
GAP: Establish the exact coefficient and remainder without presupposing its sign. A useful strict-sign implication would remain conditional on Xi data; equality, higher multiplicity, moving frequency and all-frequency positivity are outside this calculation.
REASON: One source-covered diagnostic can expose the precise missing small-cutoff sign input without a frequency sweep or another all-cutoff witness. It is routine specialization, not a new creative mechanism or a reproof of heat preservation.
SCOPE: A fixed hypothetical a in R with Xi(a)=Xi'(a)=0 and Xi''(a) nonzero; epsilon decreases to zero through positive values; use exactly K,W_epsilon,F_epsilon,D_1 of L610. Establish compact-frequency uniformity of the needed remainder only; constants may depend on the chosen compact set. The separate literature-only direct-source recovery on 2026-11-01 confirms this bounded scope; no calculation was performed.

## Inputs, hypotheses and planned test

Use L019 and L020 in the L018 Xi convention. L016 underlies the theta
normalization; no cross-notebook result is used. L610 specifies the family
but its conditional numerical enclosure is a contrast, not an input.
Read its definition and the relevant existing proofs before calculation.
Do not assume RH, simplicity of other zeros, any off-line zero, or any
first-sign inequality. A double zero is a stated hypothetical hypothesis;
no such actual zero is supplied by this notebook or the sources.

Differentiate the exact weight in its parameter with all domination
checks, and seek its expression through appropriately shifted entire
Xi values using L020. Establish the Taylor remainder with the frequency
derivatives needed for D_1. Then calculate the leading first-sign term at
the fixed double zero. This paragraph poses the computation; it asserts
neither an identity nor a coefficient or its sign.

The discriminator is whether a strict, explicitly stated sign condition
on independently defined shifted-Xi data decides the local first form
for every sufficiently small positive epsilon. Report both strict-sign
possibilities and isolate a vanishing leading coefficient as undecided.
Do not infer nearby zero splitting, preservation of real-rootedness,
uniformity in hypothetical zero height, or a sign on a moving interval.
Preparation/Rellich and heat-collision theorems are comparisons only.

If domination fails, record the failure and stop this implementation.
If the expansion succeeds but leaves an uncontrolled shifted-value sign,
record that as the precise remaining obstruction and park further sign
development unless a materially new independent input is nominated and
assessed. Do not consume successive turns on higher-order coefficients
or numerical sweeps in an equality case. A conditional local result can
be useful while actual-Xi all-height signs and independent higher signs
remain open; it is not a candidate proof of RH.

## Source reuse and justification of local work

The full comparison and precise links/theorem hypotheses are in
`2026-11-01-small-cutoff-multiple-zero-stability-review.md`.
No essential source is missing for differentiation and Taylor expansion.
No general collision theorem is imported or reproved. The inaccessible
original collision scans do not block this different first-sign test.
The local work is needed because Gaussian preservation does not compute
the derivative of the specified reciprocal weight. Classify completed
work as REPRODUCTION if successful, without claiming source-level novelty.
Full matching and supporting Mathlib coverage has not been checked.


## Direct-source recovery, 2026-11-01

The previous ready assessment omitted direct source URLs from its own
source evidence. This repair retains the exact target and SPECIALIZE
decision; it establishes no new identity or sign result.

Reopened [Schnell, Class 2](https://www.math.stonybrook.edu/~cschnell/mat545/class2.pdf),
Fall 2024, Definitions 2.5-2.6 and Theorem 2.8, printed pp.2-3,
including the beginning of the contour proof. A holomorphic germ regular
of order d in the distinguished variable factors as a unit times a unique
monic Weierstrass polynomial of degree d. This supplies no real-root sign.
It is comparison evidence only, not an input to the proposed calculation.

Reopened [Parusinski--Rainer, author manuscript](https://www.mat.univie.ac.at/~armin/publ/handbook_paper.pdf),
7 October 2024, Theorem 2.2 and Puiseux discussion, printed p.7.
A monic hyperbolic polynomial with real analytic coefficients on an open
real interval has local real analytic root labels. Hyperbolicity is
assumed throughout that interval. The proof discussion uses precisely
this reality assumption to eliminate fractional powers. This is not a
preservation theorem from one real-rooted parameter value. No original
Rellich paper was newly inspected or imported.

The earlier complete comparison remains the search/heat-source record;
no duplicate search or inaccessible collision-source retrieval was needed.
Read L019 and L020 completely and only the definition/convention portion
of L610 needed here. The existing superexponential envelope and entire
cosine representation provide the local analytic starting inputs. The
parameter differentiation and uniform remainder remain tasks, not results.
L610's numerical execution and its source are not required inputs. No new
lemma, mathematical script, root-splitting assertion or Mathlib claim was
made. Full matching Mathlib coverage remains not checked.

Recovery disposition: ready for the exact saved calculation under the
stated hypothetical double-zero assumptions. Its strict-sign discriminator
and abandonment test above are unchanged. This is a source-reference
repair, honestly STALLED as mathematical progress, rather than a new
literature discovery or an exploration-budget reset.
