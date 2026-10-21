# Finite-depth localization witness — source comparison

TARGET: Assess the finite-depth test p^e loc_p(c) != 0 for L061's k=1 branch, with p^e(D/D_div)=0 and c in Sel_{p^n} for n>e under L026.
CHECKED: 2026-10-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched finite-depth Selmer localization, maximal-divisible-subgroup localization, finite-quotient exponent and Kurihara bound terminology; compared L021/L026/L061, their ready assessments and ATTEMPTS/031. No inspected exact finite-depth theorem was found; no novelty inference is made.
SOURCE_EVIDENCE: Kim, https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf, dated 2025-05-12, directly read Section 1.5.1 and Theorem 1.8(1)--(3), printed pp. 5--6, and Theorem 1.10, p. 7; reused the approved Definition 2.12, Theorem 2.13(5), Proposition 3.13, (5.1) and complete positive-corank cases. Stacks Project, Lemma 15.55.1, tag 01D7, https://stacks.math.columbia.edu/tag/01D7, statement and full proof read 2026-10-14.
COMPARISON: Known sources cover the paired finite quotient, its valuation-minimum length formula, divisible-subgroup splitting and L061's exact coefficient/localization identifications. They support a conditional finite-depth specialization; they do not supply the proposed class or a numerical exponent bound from L026 alone.
GAP: The finite-depth implication remains unproved locally. Independently certifying p^e(D/D_div)=0 and a classical class with p^e loc_p(c)!=0 remains separate from its applicability proof; failure of one finite test is inconclusive.
REASON: Approve one bounded known-source specialization of the supplied exponent test, retaining finite images and distinguishing a certificate implication from production of its inputs.
SCOPE: All L026 hypotheses and audited L061 conventions; e>=0, n>e, supplied annihilation of the full finite quotient, and an independently certified classical finite Selmer class. No rational point, finite Sha, zero finite quotient or successful whole-system index is assumed.
COVERED_TARGET: Prove the conditional finite-depth implication p^e loc_p(c) != 0 implies k=1 in L061, assuming p^e(D/D_div)=0 and c in Sel_{p^n} with n>e under every L026 premise.
LITERATURE_REASON: The changed target introduces a finite-depth threshold and an exponent certificate beyond the ready first-index audit; its essential finite-quotient and divisible-group source comparison was missing at invocation start.

The main gap remains arbitrary higher-order rational/complex rank equality.
The proposed intermediate target is precisely TARGET. Here D is L061's
classical discrete Selmer group, D_div its maximal divisible subgroup,
e>=0 and n>e are integers, and loc_p(c) is the finite Kummer localization
in E(Q_p)/p^n E(Q_p). The bound p^e(D/D_div)=0 is supplied with independent
evidence, not inferred from residual primitivity or augmentation
semisimplicity. The class c and its localization must also be independently
certified. The assessment must distinguish this finite point quotient
from the rationalized compact target via L061's coefficient maps.

Essential inputs: L005, L026 and audited L061; no L018 basis and no
cross-notebook result. Start with the existing first-index coverage and
the finite-quotient cautions in L021/ATTEMPTS/031, reading only relevant
ranges if needed. Inspect exact known structure/exponent statements before
approving any applicability argument. This is a new target rather than
a request to repeat L061's audit or direct semisimplicity import.

Plausible downstream use: a successful finite-coefficient witness could
supply L061's localization prerequisite without a rational-point basis.
Rational Kummer membership of a strict class, auxiliary availability,
uniform coefficient production and comparison with complex order would
remain separate gaps even if the test succeeds.

Continuation test: approve a mathematical specialization only if the
known results support the stated threshold with both finite-image and
positive-corank branches retained, and separate an existential criterion
from production of its inputs. Park the test as a production route if it
requires already nonzero rationalized localization or circular knowledge
of the successful index. Exponent availability and class production must
be recorded as unresolved if the checked sources do not supply them.
No proof of this proposed test is given here. Mathlib coverage is not checked.

## Sources, scope and duplicate comparison

The existing [first-index assessment](2026-10-14-first-kato-index-localization-criterion.md)
and [separate audit coverage](2026-10-14-first-index-localization-critical-audit.md)
are reused for unchanged arithmetic statements and essential proof cases.
The new task is finite-coefficient detection, not another audit of Kim's
first-index theorem. The necessary local reads were L061's hypotheses,
conclusion and coefficient/finite-image proof, L026's hypotheses and
source matching, L005's definitions and Kummer qualifications, and L021's
paired finite-quotient statement and named imports. The local search found
only this proposed test and its preceding history entry, not a completed
duplicate. ATTEMPTS/031's semisimplicity obstruction is retained; L021's
positive finite factors remain relevant rather than being set to zero.

Direct primary sources inspected:

- [Kim, Theorem 1.8(1)--(3), printed p. 6](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf#page=7):
  p>=5, surjective residual representation, prime-to-p Manin constant,
  and a nonzero integral Kurihara collection. It gives corank, higher
  Fitting ideals, finite-quotient length and paired cyclic factors.
  Clauses (4)--(6) add finite p-primary Sha and are excluded.
- [Kim, Section 1.5.1, printed p. 5](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf#page=6):
  the quantities partial^(i) are minima over all integral indices with
  i prime factors; valuations are in the actual coefficient quotient.
  They are not individual computed values or residual prime counts.
- [Kim, Theorem 1.10, printed p. 7](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf#page=8):
  also retains local p-torsion vanishing and prime-to-p Tamagawa factors.
  Its primitivity conclusion supplies the zero terminal valuation
  recorded in L021, not a zero finite quotient.
- [Stacks Project, Lemma 15.55.1 (01D7)](https://stacks.math.columbia.edu/tag/01D7):
  an abelian group is injective exactly when divisible. The full proof
  was read, including extension over a new cyclic generator. This is
  sufficient standard coverage for splitting off a divisible subgroup;
  any application to D must be justified in the mathematical turn.

L026's residual/period matching supplies Kim's collection hypothesis;
its additional ordinary, non-anomalous, torsion and Tamagawa assumptions
are retained, not replacements for source assumptions. L061 already
identifies Sel_(p^n) with D[p^n] and the finite point quotient with
the local discrete p^n-torsion, with commuting localization maps.
The future argument must apply these identifications at the same n.
Multiplication by p^e in E(Q_p)/p^n E(Q_p) is the stated test; it
must not be silently changed to reduction to a different point quotient.

L021 already records the known-source formula length(D/D_div)=
partial^(2)(tilde-delta) under the present corank and residual premises.
This identifies relevant arithmetic information but supplies no number
here. Exact minima over an unbounded index set are not finite certificates
merely because a theorem expresses them. Kim explicitly discusses
approximate structural upper bounds after Theorem 1.8. Extracting a
certified exponent bound from concrete scalar evidence would require
its own coefficient-precision and bound comparison; it is not carried
out or added to the covered proof target. No such scalar evidence or
class is available in this step.

## Search record and decision

Queries on 2026-10-14 were: `"Selmer" "localization" "divisible" "exponent"`,
`"Selmer" "finite" "localization" "p^e"`,
`"Selmer" "finite quotient" "exponent" Kim`,
`"finite depth" "Selmer" "localization"`,
`"Selmer" "localization" "maximal divisible subgroup"`,
`"Selmer" "finite quotient" "Kurihara" "bound"`,
`"Selmer" "localization" "p^e" "p^n"`, and
`site.stacks.math.columbia.edu divisible abelian groups injective`.
Results led to the inspected Stacks statement and the already relevant
Kim source. Other returned fine-Selmer, supersingular, anticyclotomic
and broader BSD leads were not inspected as theorem coverage and are
not used. A failed exact search establishes neither novelty nor absence.

DECISION is SPECIALIZE, not IMPORT of an exact finite-depth theorem.
The general structure and injectivity results are named source inputs;
the only planned local work is the finite-depth applicability argument.
Reproving Kim's system/structure theorems or the Stacks theorem is
unnecessary. The covered target is ready for a separate mathematical
attempt classified REPRODUCTION; this review proves no new implication.

The attempt must explicitly check how the supplied exponent controls
the finite-image alternative, how nonzero localization of the divisible
part relates to L061's rationalized map, and how the finite coefficient
identifications preserve the test. It must keep the potentially nonzero
finite image, retain the positive-corank branch's possible integral
finite cokernel, and avoid assuming inverse-limit right exactness.
An isolated zero result or an unsuccessful depth cannot select k=2;
no fixed-depth converse or search termination is approved.

Continue if a full conditional proof can be written from these imports
and L061 without presupposing nonzero rationalized localization or k=1.
Abandon this conditional specialization if that matching fails under
the retained hypotheses. Park any unconditional production claim unless
independent exponent and class certificates are available. Even a
successful implication supplies neither its inputs nor rational Kummer
membership, auxiliary availability, uniform coefficient production or
arbitrary complex-order comparison. The full matching Mathlib theorem
and supporting coverage are not checked; no absence is asserted.
