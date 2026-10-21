# Proposed separate critical audit of the balanced limit

TARGET: Critically audit L398's fixed-N balanced mollified limit, including finite-prime cancellation, uniform combined shift errors, ordinary jet signs and both sharp endpoints.
CHECKED: 2026-10-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 73 reused the ready step-71 calculation assessment and step-69 reciprocal-bound coverage, read complete L398 and relevant L390/L395 passages, checked the L390/L394/repeated-carrier failures, and queried the exact Titchmarsh 3.11.8 and Theorem 3.8 citations; no new discovery search or novelty inference.
SOURCE_EVIDENCE: Reinspected Young, published Arch. Math. 95 (2010), Lemmas 3–7, both Lemma 5 orderings, (6.1)–(6.4), and Section 7, pp. 540–547; Bui–Hall arXiv:2304.05178v1 Proposition 1/(6)–(8). Reused previously inspected Baluyot–Gonek, Pacific J. Math. 303 (2019), Section 2, p. 53, before (2-3), for the precise reciprocal-zeta region. Original Titchmarsh book pages were not inspected.
COMPARISON: Known moment, zero-free-region and holomorphic differentiation tools cover the unchanged audit hypotheses; neither source states L398's response-twist arithmetic extension or verifies its error estimates. A separate proof audit is now approved, not the claimed limit.
GAP: Audit finite-prime cases, weighted double Dirichlet-series representation and O(ell^2) remainder, complex-shift reciprocal contours, reflected diagonal and combined holomorphy, ordinary jet coefficient and absolute small-bump endpoints.
REASON: Essential analytic source coverage is ready; the differences are explicit existing proof obligations in L398, so a mathematical audit rather than further unchanged literature is next. No new result is derived and the completed calculation is preserved.
LITERATURE_REASON: The separate audit compares newly written L398's modified Mellin and small-bump argument against source scope, especially the left-of-one reciprocal contour; this is distinct from repeated approval of the carrier reduction.
SCOPE: Only the exact TARGET, with fixed N, direct local inputs L390/L395, Y=H^(1/100), P(u)=u^2, all ordered response twists, both functional-equation diagonals, ordinary order two per side and sharp [H,2H]; no growing-N or complete signed-mean assembly.

The exact proposed action is the TARGET above. Essential local inputs are
L398 and its directly used L390/L395 definitions, Hardy identity and audited
weighted bounds. L396/L397 are downstream context only, not mathematical
inputs to the balanced proof. Fix N before H tends to infinity, retain the
actual length H^(1/100), polynomial u^2, all ordered r,s pairs, both
functional-equation diagonals and ordinary order two on each side.

The current proof's weakest new specialization is the uniform O(ell^2)
modified Mellin remainder and its use inside both diagonal residues. Check
the double Dirichlet-series weighted absolute convergence, reciprocal-zeta
contours (including complex shifts), finite-prime poles and power-saving
approximate-functional-equation contour. Check the absolute small-bump
bound separately from the whole-interval L395 bound. The rational script
checks only algebra; no finite preview can validate these analytic steps.

Reuse drafts/literature/2026-10-11-mollified-balanced-fixed-head-limit.md
and the exact primary passages it records. A targeted new primary read is
appropriate only if an essential quantitative hypothesis is not covered.
No source obstruction or novelty is inferred here. Full matching Mathlib
coverage remains not checked. The complete physical signed mean, growing
N, eventual discriminant sign, actual common-zero upper bounds and global
mixed positivity remain unresolved; assume none of them in the audit.

The future audit should accept L398 only if its complete normalized error
vanishes with both endpoints and every response twist. Otherwise isolate
the specific unsupported bound or wrong coefficient without inferring a
sign of the actual mean from the failed proof.

## Separate source-scope comparison — step 73

This is literature-only EXPLORATION, classified KNOWN_IMPORTED for known
analytical tools. It establishes a ready scope for a subsequent audit,
without verifying L398 or deriving a new lemma. The main gap remains
global actual-theta mixed positivity. The intermediate target is the exact
audit above; its plausible use is a later complete mollified signed-mean
assembly, subject to the independent gaps below.

Reuse [the calculation assessment](2026-10-11-mollified-balanced-fixed-head-limit.md)
for complete primary hypotheses and discovery comparison. Reinspection of
[Young's published paper](https://www.math.ntnu.no/emner/MA3001/2020v/2022v_MA3004/Young.pdf),
DOI 10.1007/s00013-010-0199-9, confirms: Lemma 5 permits positive integer
twists with hk<=T^(2 theta), fixed theta<1/2, small complex shifts and
weights satisfying (2.1)–(2.3). Both unequal-order proof cases and both
diagonals were read. Lemmas 6–7/(6.2)–(6.4), pp. 544–547, treat the scalar
arithmetic factor, a power-saving contour reduction and uniform residue
error. Combined holomorphic extension is on pp. 544–545; normalized Cauchy
differentiation is on p. 541. These are technique inputs, not a theorem
evaluating modified response collisions. L398's existing fixed-N range
check is within the assessed family; its accuracy, coefficient summation
and exact-Y implementation remain audit obligations. Section 6 uses
t>=T/2, covering the bulk and endpoint neighborhoods at T=2H; do not
silently extend that step to every weight allowed by (2.2) without checking
its height lower bound.

The [Bui–Hall statement](https://arxiv.org/html/2304.05178v1#S3),
11 April 2023, Proposition 1/(6)–(8), printed pp. 6–8, was reinspected.
It supplies a sharp scalar differentiated mollifier moment for fixed
polynomials with P(0)=0 and 0<vartheta<4/7, and ordinary Hardy-jet
conversion with Schwarz error control. It has no response head or
small-bump assertion. Reuse audited L395 for the exact Hardy identity and
whole-interval weighted bounds; those bounds alone do not remove endpoints.

For the reciprocal contour reuse [step-69 coverage](2026-10-11-mollified-diagonal-limit-audit.md).
Its inspected primary reference is S. Baluyot and S. M. Gonek,
*Explicit formulae and discrepancy estimates for a-points of the Riemann
zeta-function*, Pacific J. Math. 303 (2019), 47–72, DOI
10.2140/pjm.2019.303.47,
[Section 2, p. 53, before (2-3)](https://msp.org/pjm/2019/303-1/pjm-v303-n1-p02-p.pdf#page=9).
The statement gives |zeta(sigma+it)|>=c/log t for sufficiently large
positive t and sigma>=1-A/log t with fixed positive constants, citing
Titchmarsh (3.11.8). Conjugation covers negative heights. This supplies
the required kind of left-of-one region, but does not certify containment
of L398's shifted rectangles. Young p. 546 invokes Titchmarsh, second
edition (1986), Theorem 3.8 and (3.11.8). Original book pages are not an
inspected premise; new search hits and unrelated results are not used.
No essential access blocker remains because the exact bound is already
available in the inspected primary-paper coverage.

### What citation alone does not establish

The mathematical audit must test these existing claims without assuming
their truth from this approval:

- Check all four squarefree exponent pairs for each sign of the response
  valuation difference, nonsquarefree r,s, common factors and r=s. Check
  L398 (1)–(2) without dividing by a local numerator that can vanish.
  Evaluation at the origin alone is insufficient.
- Verify (4) on a common shift disk with nonnegative double Dirichlet
  indices and weighted absolute coefficient moments. Euler-product
  convergence alone does not supply that representation. Check finite
  modified factors and the unmodified infinite product separately.
- Check the approximate-functional-equation contour with actual Y at
  T=2H: gamma poles, denominator zero-free domains, finite-prime poles,
  annular G losses and power-saving bounds. Preserve both reflected shifts.
- For (6), check all horizontal, vertical and original-tail bounds, the
  initial positive line, uniform shift containment, bounded-q regime and
  X=1 or X<1. The residue and O(1) remainder must hold on a disk large
  enough for later Cauchy contours. Compact shifted heights require their
  own zero-free neighborhood, not a large-height bound.
- Check the complete (3)–(7) interchange, both Perron cutoffs, coefficient
  tails and sum–integral error. Require O_N(ell^2) before multiplying the
  diagonal pole. Check X replacement on each diagonal, the removable
  combined pole, unequal-radius enclosing bidisk and scaled order-two
  derivatives on each side, with one uniform error.
- Independently verify ordinary i^j(-i)^k signs, theta'' contribution, both
  logarithm normalizations and the full signed M combination. The saved
  rational certificate checks algebra only; inspect complete relevant
  evidence if using it, without treating a preview as analytic verification.
- Check nonnegative smooth majorants for both sharp boundary neighborhoods
  with the actual mollifier. Require an absolute O(H/ell) weighted jet
  envelope for each bump from a uniform smooth estimate and exact jet
  conversion. L395's O(H) whole-interval envelope, a signed bracket or
  changed cutoff is insufficient. Qualify overly broad generic-weight
  claims without discarding the target proof.

This is scrutiny of an existing specialization, not approval to reprove
the scalar theorem or invent a replacement on uncovered hypotheses.
If an essential claim fails, isolate the estimate and its effect on the
conclusion; preserve the original proof and do not infer a sign of the
actual mean from that failure.

### Duplicates, failures and decision test

The narrow local comparison read step-71/72 records, relevant L390/L395
passages and complete L398. The L390 absolute-contour failure, L394
fixed-quadratic-weight obstruction and repeated-carrier stop concern other
certificates and remain intact. L396/L397 provide downstream context only,
not inputs validating the balanced arithmetic. Reuse the assessment's
stronger/different-mollifier exclusions; no unmatched source or
cross-notebook input is imported. No novelty conclusion follows.
Full matching Mathlib coverage remains not checked.

Continue with one critical audit of the unchanged target. Accept its
conclusion only if every retained twist and both diagonals give the claimed
normalized O_N(1/log H) bound, uniformly enough for the ordinary jets, and
both absolute endpoint errors vanish. An order-one error, wrong coefficient,
unsupported contour or invalid specialization requires qualifying the result
or recording a proof failure; it does not decide RH or the actual complete
mean. No mathematical audit was performed here.

The complete physical mollified signed mean, infinite-response passage,
total L367 margin, eventual physical sign, actual common-zero upper bounds
and global mixed positivity remain unresolved. Fix N before H tends to
infinity; assume no RH, simplicity, disjointness or phase independence.
