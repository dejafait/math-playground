# Exact five-adic whole-fiber class list — source coverage ready

TARGET: Compute a certified exact list of L060's whole-fiber connecting classes at five, retaining both scalar disks and all class collisions.
CHECKED: 2026-10-12
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched X0(11)/5-adic/descent/image, X0(11)/whole fiber/descent, X0(11)/local image/5, X0(11)/5-descent, 54a1/local/descent, Schaefer–Stoll/local images/precision, p-descent/deterministic/local and unramified p-adic units/pth powers; checked L037, L060 and ATTEMPTS/010,012. No inspected source supplies this exact list; failed searches establish no novelty.
SOURCE_EVIDENCE: Reused L033–L035 and L038–L040 coverage; inspected Milne ANT v3.08 Proposition 2.43 p.40 with proof, Theorem 7.33 and Remark 7.36 pp.121–122 with lifting proof, Proposition 7.50 pp.127–128 with embedding proof; Clark ANT II Theorem 2.36 p.79 and its higher-unit proof; Schaefer–Stoll June 13, 2001 Section 5 pp.8–10; FNS June 10, 2019 Section 7.2 equation (7.4) p.27 and both Lemma 7.6 proof cases pp.28–29.
COMPARISON: Known lifting, integral-basis and fifth-power methods cover a finite exact-certificate specialization; unrestricted subgroup spanning and FNS's two-adic square classes do not enumerate the present whole-fiber subset. L060 supplies sufficient precision and necessity, not reverse realization or collision completeness.
GAP: Prove and certify the exact whole-fiber presentations on both disks, fix a faithful integral model of U, enumerate every lifted embedding, prove the finite unit quotient test in both directions, retain all collisions and reconstruct the exceptional rational class; no enumeration or global intersection is yet obtained.
REASON: Approve one bounded REPRODUCTION attempt using imported general methods; explicit fiber realization and arithmetic are required because no matching exact list was found, and no new general lifting or descent theorem needs reproof.
SCOPE: Exactly TARGET over L038's entire A=Q5 x U_11 with L033's dual connecting map; both L060 disks, every full-fiber isomorphism, L034's removable 2T chart and L035's norm identity including T; no global class/unit calculation or branch exclusion.
LITERATURE_REASON: Separate coverage was required for the newly proposed exact-list target beyond L060's approved bound/audit, specifically reverse whole-fiber realization and faithful collision testing; reuse all unchanged general descent and Hensel coverage.

## Gap, comparison and literature reuse

The main gap is global positive primitive integer emptiness in the 54a1
branch and the other surviving signatures. The intermediate target is the
saved exact class list. Its plausible downstream use is a local membership
test in a future certified global class intersection. Global classes/units,
other-place compatibility, rational points and integer lifting remain
independent unresolved steps. No complete Beal candidate exists.

L060 is audited and read in full. Its scalar exclusions and uniform unit
precision already give a finite upper bound. L037 supplies a faithful
whole-fiber/class formulation, including exceptional charts, but not an
executed exact list. L039's factor and reconstruction argument applies
only to its fixed scalar. None duplicates the proposed complete list.
ATTEMPTS/010 parks inherited norm-only properness; ATTEMPTS/012 parks
additional primitive-scalar strictness by L040. This proposal preserves
both stops: it enumerates the already common I_pow=I_fiber, without
reviving either failed test. Global ATTEMPTS/013,025–028 remain parked.

The queries above returned general descent, modular-curve and unrelated
results; no inspected matching theorem was located. Mazur's 1978 X0(11)
five-descent discussion and Conrad's moduli notes concern different
global fields/rational-point questions and are unread leads, not inputs.
The Stoll deterministic two-descent and Creutz second-descent leads are
also not imported. No exhaustive literature or originality claim follows.
The ready local-five/norm-slice assessments are reused for their actual
scope; no repeated Cohen elimination review is needed.

## Primary inputs and their exact scope

J. S. Milne, [Algebraic Number Theory v3.08, July 19, 2020](https://www.jmilne.org/math/CourseNotes/ANT.pdf),
Proposition 2.43, p.40: over a PID, an integral field basis with
discriminant d bounds the full integral closure between its span and
its d-inverse span. Its Cramer-rule proof was read. This covers
certifying the chosen unramified power basis by a unit discriminant.
Theorem 7.33/Remark 7.36, pp.121–122, lift all coprime monic residue
factors over a complete DVR, preserving degrees and uniqueness; read
the Bezout, uniqueness and successive-correction proof. Proposition
7.50, pp.127–128, identifies unramified extensions and their embeddings
with separable residue extensions when base and residue fields are
perfect; its proof was inspected. These hypotheses hold for Q5 and
finite fields. Exact factorization and discriminant witnesses still
belong to the research attempt, not this review.

Pete L. Clark, [Algebraic Number Theory II](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf),
161-page version retrieved 2026-10-12, revision date unidentified,
Theorem 2.36, p.79, concerns a Henselian normalized discrete valuation,
finite residue field, and N not divisible by the field characteristic.
It computes unit and field Nth-power indices, retaining the Nth roots
of unity. Read the higher-unit equality and Hensel–Newton surjectivity
proof. Reuse Theorem 1.79, p.58, as documented in foundation 17 and
L060's audit assessment. For N=5 the derivative has valuation one in
both Q5 and U, so simple-root lifting alone is insufficient. The
research can keep L060's sufficient modulus 125, justify the reduction
kernel by the existing strong-Hensel bound, and compare fifth powers
in the finite unit group. An index formula alone gives no class labels.

Romyar Sharifi, [Algebraic Number Theory](https://www.math.ucla.edu/~sharifi/algnum.pdf),
259-page version retrieved 2026-10-12, revision date unidentified,
Section 6.3, Lemma 6.3.8, p.131, was inspected as an alternative
higher-unit lead. Its printed successive correction has a sign issue
(the positive correction accompanies a positive residual excess).
Do not use that displayed proof or require its sharper filtration
cutoff here; Clark's independently inspected coverage and L060's
already audited sufficient precision are adequate. No source correction
or new unit theorem is proved in this literature turn.

Edward F. Schaefer and Michael Stoll, *How to do a p-descent on an
elliptic curve*, Trans. AMS 356 (2004), 1209–1231,
[DOI](https://doi.org/10.1090/S0002-9947-03-03366-X),
[June 13, 2001 long manuscript](https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf),
Section 5, pp.8–10: the good-divisor evaluation equals the connecting
map under the cohomological hypotheses, which L033 already checks.
The local spanning/size test computes an unrestricted subgroup.
It cannot certify this restricted subset, which is not assumed a
subgroup. Its deterministic reference [30] is not imported.

Nuno Freitas, Bartosz Naskręcki and Michael Stoll, *The generalized
Fermat equation with exponents 2, 3, n*, Compositio Math. 156 (2020),
77–113, [June 10, 2019 final manuscript](https://www.mathe2.uni-bayreuth.de/stoll/papers/genfermat-final.pdf),
Section 7.2, equation (7.4), p.27; Lemma 7.6, pp.28–29: re-read both
ordinary-disk and branch-disk proof cases. This result is for finite
extensions of Q2 with no rational two-torsion, the specified disks,
and square classes of x-theta. It does not cover Q5 fifth powers.
The equation alone also needs reconstruction/chart justification.
L034 and L037 supply the available exact map and chart inputs. No
GRH-dependent Selmer computation is imported.

## Approved certificate interface and discriminating test

The following are obligations of the next mathematical attempt, not
results established by this review. Import the general theorems above;
prove only their explicit specialization and the completeness of the
implementation. Keep full mathematical reasoning with any successful
canonical result, not just in a script or a certificate preview.

1. For each scalar disk, certify the complete monic residue
factorization, its degrees, irreducibility and coprimality, and
invertibility of b. Prove its lift identifies the entire twelve-point
fiber with A for every admitted scalar, or precisely identify a failure.
Retain the rational factor and every degree-eleven embedding. A root
in U alone is insufficient. Use the curve and complete modular map
for reverse reconstruction; a necessary elimination relation alone
is insufficient at d=0. Treat s=-121 using L034/L037's 2T chart and
s=-24729001 using L033/L035's exceptional descent convention.

2. Fix one monic unramified model and certify its full integer ring,
so coefficient arithmetic modulo 125 represents R/125R faithfully.
For every scalar residue modulo 125 in both disks and every relevant
residue-field embedding, retain the unique simple coordinate lifts,
the reconstructed y and the unit f-value. Prove every actual class
is covered and every listed representative has an exact whole-fiber
realization. L060's uniform precision supplies constancy only after
these realization hypotheses have been checked.

3. Reduce unit class comparison to the finite unit quotient by fifth
powers at the justified modulus. Supply a complete finite root-testing
method, fifth-root witnesses for collisions and complete rejection
certificates for noncollisions. Verify invertibility and all embeddings
in the same fixed ring. Distinct residue representatives, or unequal
f-values, need not give distinct classes. Avoid brute-force enumeration
of the whole very large ring unless a concrete feasible bound is given;
a binomial/finite-field lift solver needs a proof of completeness.
A smaller modulus or a new normalization requires its own applicability
proof within this same assessed local-power scope.

4. Reconstruct the rational component by L035's class norm identity,
with exact norm arithmetic or its faithful finite class counterpart.
Prove both directions for the resulting pair list, including exceptional
rational evaluations. Keep all collision memberships and a full on-disk
certificate; print only actual list size, required completeness checks,
failures and artifact paths. Compare with L060's upper bound 600 and
nonemptiness, without treating either check as proof of exactness.

Continue only if whole-fiber realization, class comparison and complete
coverage pass together. If a factor/chart or finite quotient test cannot
be justified, report that specific failure and preserve partial reasoning;
do not label a necessary candidate list exact. A source obstruction
requires separate source scope/access review; an arithmetic failure is a
research outcome. This approval changes coverage, not the mathematics:
no scalar-disk sufficiency, exact image size or class list is asserted.
No cross-notebook input, global class basis, Sha vanishing or integer
lifting is assumed. Full and supporting Mathlib coverage are not checked.
