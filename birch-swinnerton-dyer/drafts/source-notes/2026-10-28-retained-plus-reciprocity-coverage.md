# Retained-plus reciprocity: primary-source coverage

Literature-only step 540, 2026-10-28. No conditional criterion is proved
here and no application to the actual coefficient is accepted.

## Scope and discriminating test

The main gap is rational rank versus analytic order for arbitrary
curves. The intermediate target is the saved assessment's finite-at-p
question for L123's **actual** descended outer-plus coefficient.
Its downstream use would be to place that coefficient in a Selmer
group before addressing the independent rational-Kummer, nonvanishing
and strictness gaps. Continue with a conditional specialization only
if the exact duality hypotheses can be matched. Abandon an unconditional
application at the first missing input; analytic order two cannot
stand in for a rational point.

## Sources actually inspected

1. Karl Rubin, *Euler systems*, 1999 AWS manuscript,
   [primary PDF](https://swc-math.github.io/aws/1999/99RubinES.pdf).
   This is the accessible manuscript, not an assertion about pagination
   of the subsequently published book. Read I.2.2 and its proof;
   I.3.2--3.5, I.3.10; I.4.1--4.3; I.5.1--5.7;
   I.6.4 including Remark 6.6 and Proposition 6.7;
   I.7.1--7.3 including the complete proof (printed pp. 17--19).
   Theorem I.7.3 assumes a number field, a finite free p-adic
   representation unramified outside finitely many primes, mutually
   orthogonal chosen local subspaces at p, nonzero coefficient M,
   and finite sets Sigma_0 contained in Sigma. It identifies the
   relaxed singular localization and dual finite localization images
   as exact orthogonal complements, for enlarged and arbitrary Sigma.
   I.5.6/I.3.10 give limit comparisons; I.2.2 invokes B.2.4 for
   rationalization. It does not apply itself to L123.

2. Karl Rubin, *Euler systems and modular elliptic curves*,
   [primary PDF](https://swc-math.github.io/aws/1999/99RubinDur.pdf),
   Section 1, printed pp. 1--2, and Section 5's local definitions,
   Proposition 5.1 with proof and displayed exponential/duality
   identifications, printed pp. 5--6, inspected.
   For an elliptic curve over Q, Section 5 identifies the local
   finite subspace with the Kummer image, states its self-orthogonality,
   and identifies the singular quotient with the dual of local points.
   The exponential identifies the rational local point space with
   the tangent space. These statements do not impose good reduction;
   the later integral evaluation in Proposition 5.2 is not used.

3. Darmon--Fornea, *Mock plectic points*, published online 2025,
   [publisher text](https://www.cambridge.org/core/journals/journal-of-the-institute-of-mathematics-of-jussieu/article/mock-plectic-points/1FB89BA4F920603AEE9D624B3897E876),
   Section 3.7, Definition 3.7 and following paragraph, and Theorem 3.9's
   complete sketch inspected. The paragraph explicitly identifies
   away-p local Kummer with full integral Tate-module H^1. The sketch
   uses local Tate duality and a global sum of local pairings. Its
   particular mock class and minus/twist conclusions are not imported.
   Theorem 3.8 was already assessed in step 511; no repetition of its
   class comparison or proof is needed for this target.

4. Fornea, *Plectic Heegner classes*,
   [arXiv:2603.28327v2, 13 April 2026](https://arxiv.org/html/2603.28327v2),
   Section 1.2 (Conjectures 1.9--1.10), Definition 4.23 and
   Corollary 4.24's statement and displayed descent formula rechecked.
   Reuse step-512's complete proof coverage and its coverage of
   Definition 4.17, Proposition 4.18 and Corollary 4.19. The global factor is
   H^1, while Selmer membership is conjectural. Theorem C concerns a
   p-adic auxiliary place w; it supplies no automatic assertion at the
   retained prime in S when w is infinity. Existing step-512 coverage
   is reused for the defining integral and comparison proof.

Local copies: `2026-10-28-rubin-euler-systems-source.pdf` and
`2026-10-28-rubin-modular-elliptic-source.pdf` in this directory.
Selected complete extracts: `2026-10-28-rubin-cohomology-extract.txt`
(PDF pp. 10--13), `2026-10-28-rubin-local-extract.txt` (14--17),
`2026-10-28-rubin-duality-extract.txt` (18--30), and
`2026-10-28-rubin-elliptic-extract.txt` (1--6).
They preserve source text, including the apparent residue-prime typo
in I.6.7's proof; no conclusion relies on reading that typo literally.
The stated supporting B.2.4 is cited through the inspected I.2.2 proof;
its appendix proof was not independently inspected.

## Comparison to the actual object; work deliberately left for mathematics

L123 (5) and its descent paragraphs, not a raw measure coefficient,
specify the class to use. Its projected, descended symmetrization is
c-invariant. A later specialization must explicitly use rational
inflation--restriction to Q, preserve localization compatibility, and
justify a global integral lift after a **single** p-power rescaling.
This is different from claiming an integral bound on the composite
raw-measure projection, which L123 does not supply. No repair of
L128 or use of the stopped covariant tower is proposed.

The literature now covers the away-p condition for global integral
Tate-module classes, rather than requiring a new CM-by-CM ramification
calculation. Applying it to this rational descended class still requires
the lift/rationalization check. At the real place retain p odd and
the vanishing of positive finite-group cohomology after rationalization.
Do not replace a bad-prime integral Kummer condition by an arbitrary
unramified condition at finite torsion level. A finite-level nonzero
local residue is not itself a spanning statement over Q_p.

The unresolved arithmetic input is a specified rational Kummer class
whose p-localization is nonzero, and verification that this localization
spans the finite local line for the split-multiplicative curve over Q_p.
The source-supported proposed conclusion is only finite membership of
the descended coefficient, **conditional** on that input. No such point
is constructed or inferred from analytic rank here. There is no claim
that this conditional membership identifies the coefficient with a
rational point, makes it nonzero, or makes it strict. L005's
good-reduction rank certificate cannot be applied unchanged.

## Search and duplicate/failure checks

Local checks: L123's hypotheses, definition (5) and descent proof;
L005's hypotheses/conclusions; foundations/10-selmer-bockstein-duality.md;
step-511/512 plectic source notes and assessments; ATTEMPTS/058; and
targeted reciprocity/orthogonality searches in local literature notes.
The older good-ordinary duality setup is outside the current
split-multiplicative/inert hypotheses. The plectic rational-exterior
import failure remains intact. ATTEMPTS/061--063 stay parked; their
tower-action obstruction is unrelated to the present standard duality
application. No duplicate actual-class application was found in these
specific paths; this is not a novelty claim.

Queries included: “Milne arithmetic duality theorems local Tate duality
abelian varieties Kummer orthogonal global reciprocity pdf”; “elliptic
curve relaxed Selmer global reciprocity nonzero localization finite
local condition p”; “Rubin Euler systems local cohomology H1 K v V
elliptic v not p zero”; “Plectic Heegner classes local conditions”;
and “elliptic H^1 relaxed non-torsion point duality”. Search hits alone
were not used as mathematical evidence. Milne ADT's author-hosted PDF
failed in the web reader; a Stanford mirror opened. Its theorem was
not inspected completely and is not an additional claimed input.
Other unrelated or unverified search results were not used.

Decision: SPECIALIZE for the conditional application only. The needed
specialization is Q-descent, rational-to-integral transfer, local
condition matching, and the passage from the cited finite-coefficient
duality to the exact rational class. None is reproved in this
literature turn. The named nonzero rational localization remains an
explicit assumption, not an established input. Mathlib coverage:
not checked. No source match claiming the actual coefficient is
unconditionally finite, rational Kummer or nonzero is asserted.
