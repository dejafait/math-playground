# Actual-b_m obstruction — independent-audit coverage approved

TARGET: Audit L976's exact-radius and positive-axis continuation argument for the failure of L975's actual-b_m envelope, including multiplicities and finite prefixes.
CHECKED: 2026-11-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed steps208-209 exact actual-xi coefficient/Pringsheim comparison, duplicate searches and recorded failures in 2026-11-10-bn-envelope-singularity-compatibility-review-207.md and 2026-11-10-bn-envelope-pringsheim-test-review-208.md; same germ, envelope, theorem and analytic hypotheses. No new search or novelty claim.
SOURCE_EVIDENCE: Flajolet-Sedgewick, Complex Asymptotics, zeroth edition 8May2004, TheoremIV.3(ii) with complete proof pp15-16/PDF23-24, https://algo.inria.fr/flajolet/Publications/ch4567.pdf#page=23 ; DLMF https://dlmf.nist.gov/1.10.i , https://dlmf.nist.gov/1.10.ii , https://dlmf.nist.gov/1.9.vi (1.9.53-57), https://dlmf.nist.gov/25.10.i ; previously inspected in steps208-209. Local L013/L018/L975/L976 read for source-scope comparison in step211; direct theorem/proof and DLMF passages rechecked in step211. This is not a mathematical audit.
COMPARISON: The same known boundary theorem covers the contradiction once its hypotheses are checked; the proposed audit concerns only L976's actual-xi radius, nonremovability, branch agreement, geometric correction and quantifiers. No new coefficient mechanism or stronger imported theorem is needed.
GAP: Independently verify or identify a precise defect in the specialization, especially that the minimum is attained below 2, the corrected Taylor radius equals R, and continuation at positive R agrees with the original germ.
REASON: The recorded negative result changes the admissibility of L975's payment route and warrants a conceptual audit before relying on the stop; separate source approval completed in step211, with mathematical correctness still unreviewed.
SCOPE: Only audit L976 and the L013/L018/L975 inputs it actually uses, with arbitrary zero multiplicities and delta-dependent finite prefixes. Do not derive a replacement envelope, inspect Coffey's conditional asymptotic, or assume RH, simple zeros, an effective first zero, or radius2. L026 is used through L975; L968 is downstream only.

LITERATURE_REASON: Required separate approval of the newly written L976 audit scope; compare its actual input requirements with the already inspected sources, without expanding the ready feasibility-test literature or deriving mathematics.

## Reused coverage and separate approval boundary

The unchanged step209 assessment covered the mathematical test
completed in step210. That test produced L976 and the recorded
envelope stop. Step211 completes the required separate literature approval of
this exact audit target. This source comparison does not constitute
a mathematical attempt or an independent proof audit.
No new literature is needed unless an actual missing input is found;
any further source work must name it in LITERATURE_REASON.

Check the direct algebra for the image of a reflected zero, the
compactness argument giving a minimum, and the distinction between
a zero-free open disk and a regular positive boundary point. Check
local multiplicity preservation under the inner map and prove that
an additive correction analytic beyond R cannot remove the zero
singularity. Check the normalized logarithm on connected overlaps,
not just existence of an unrelated local branch.

Finally check the single choice a=(R+2)/2 against every-delta H,
all constant and prefix coefficients, and Pringsheim's exact finite
radius hypothesis. Acceptance means these checks hold for the
actual coefficients without RH. A genuine failed implication must
be reported and repaired or the obstruction withdrawn; an audit
cannot replace H by a weaker condition and claim the same result.

The main gap remains L030-L032/C032a and L966 signed forcing.
This audit can confirm or correct a route stop; it cannot pay that
independent gap. No justified creative payment mechanism has been
identified within the approved source scope. Full Mathlib coverage
is unknown and no Mathlib theorem is imported. Expected research
classification remains REPRODUCTION, with conceptual-audit routing.

## Step211 separate source approval, 10 November 2026

Reused the exact-target searches, duplicate comparison and recorded
failures in the step208 assessment and step209 source-link recovery.
Read L976 only to identify the inputs and audit obligations, alongside
L013, L018 and L975. The existing step210 attempt record already
identifies the envelope route stop; it is not independent validation.
No expanded search or new coefficient claim was needed.

Reopened the 8 May 2004 Flajolet-Sedgewick PDF, Theorem IV.3(ii)
and the complete two-case proof on printed pp.15-16/PDF pp.23-24.
Its hypotheses are analyticity at the origin, finite positive Taylor
radius and nonnegative Taylor coefficients. Its conclusion concerns
regularity of the same germ at its positive radius, not arbitrary
branches. Part (i) uses Cauchy estimates; part (ii) recenters inside
the disk and rearranges nonnegative terms. This named theorem is
imported by citation, with no reproof required. It supplies none of
L976's actual-xi radius, branch or coefficient checks.

Reopened DLMF 25.10(i) for unconditional strip-zero existence and
reflection symmetry; 1.10(i), especially 1.10.1 and the zero-order
paragraph, for Taylor radius and multiplicity; 1.10(ii) for equality
of analytic elements on overlaps; and 1.9.53-57 for the local
normalized logarithm, with nonzero constant term and sufficiently
small neighborhood. These sources require neither RH nor simple
zeros. DLMF's overlap statement must be applied on a connected
intersection; its local logarithm is not a global branch theorem.
L975 already records the standard disk logarithm theorem and its
normalization via integration. No new logarithm theorem is missing.

The exact audit is therefore ready under SPECIALIZE. Its remaining
work is mathematical: verify minimum attainment, nonremovability,
branch agreement, unchanged corrected radius, every coefficient and
all delta/prefix quantifiers, using only the named inputs. Reject or
repair a precise failed implication rather than silently weakening H.
This approval adds no evidence that L976 is correct and certifies no
new result beyond the sources. Full matching Mathlib coverage remains
unknown. No lemma, mathematical script, DAG or PROOF change was made.
The unchanged Next action should now receive the conceptual audit.
