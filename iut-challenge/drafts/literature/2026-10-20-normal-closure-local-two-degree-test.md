# Normal-closure local degree at two — specialization coverage

TARGET: Prove or refute v_2([(G_o^nor)_w:T_v])<=10 uniformly for L089's survivors, all six L090 orderings and every actual v above 2 and w above v, using the joint odd-torsion inertia and full four-division tower.
CHECKED: 2026-10-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step368's completed local-two-degree-scope review screened exact local-degree/normal-closure queries, L089,L090,L092 and the scoped failures; no exact changed-field estimate was found. Reuse that comparison; no novelty claim.
SOURCE_EVIDENCE: Reuse step368's precise theorem/proof readings: Silverman AEC (2009) VII.5.5, A.1.4(b), VII.7.1/7.3 and III.8.1(c,d)/8.1.1, https://studylib.net/doc/28155304/the-arithmetic-of-elliptic-curves ; Milne ANT v3.08 7.50–7.54, 7.58(a), 8.10/8.13, https://www.jmilne.org/math/CourseNotes/ANT.pdf ; FT v5.10 3.17/3.18, https://www.jmilne.org/math/CourseNotes/FT.pdf . Qualified numerical context only: IV reproduction 1.3(ii), 1.10(ii), https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%204.pdf .
COMPARISON: Known potential-good and finite-inertia criteria plus finite Galois completion theory cover the method. What remains is a finite-level congruence and matrix-order verification, followed by the actual local tower comparison; none of these criteria alone states the target.
GAP: The uniform bound is unproved. No exact local decomposition group, equality of completions or sharp local degree is supplied, and no complete repair follows from a passing test.
REASON: This bounded specialization can decide whether the dyadic degree allowance survives the global relative-degree excess, leaving independent gaps explicitly open.
SCOPE: Exactly TARGET. Retain the fixed family, domains, closure, full-coordinate fields and all actual places; permit theorem application, explicit finite congruence/matrix-order checks and local degree towers only. No other primes, different computation, new occurrence family, field reinterpretation or essentiality verdict.

Step369 repairs the missing direct URLs in this assessment and retains its
exact target and SPECIALIZE scope. The Silverman reproduction was opened,
and Milne ANT v3.08 and FT v5.10 were verified at the direct URLs on
2026-10-20. Reuse the complete relevant readings and page numbers in
`2026-10-20-normal-closure-local-two-degree-scope.md`; no fresh theorem
comparison, new coverage or mathematical specialization is claimed. The
IV reproduction was not reopened; its earlier readings and authentication
qualification remain unchanged. Step368 performed no specialization.
LITERATURE_REASON: Supervisor-required repair of missing direct source URLs; reuse existing coverage without another source-discovery turn.

Main gap: original finite B>=A. Intermediate target: the displayed bound.
Downstream use: recover or rule out this one sufficient local degree
input after the global C_0 argument was lost; a passing result would
weaken a proposed obstruction to repair, not demonstrate an IUT flaw.

Use audited L089,L090,L092. Fix one original survivor once, with the
same c,h,d_*,e_*, both domains and algebraic closure. Let T=F_tpd
and M=Q(E[60]) be L090's actual fields. Keep d=6, epsilon_d=1.
For each v above two choose extending places through the actual
closure and M, using completion/decomposition theory. Do not replace
E by a named old member, the height-selected prime by seven, or
full division fields by x-coordinate fields.

Import the cited reduction and local-field theorems, with their perfect
field and residue-characteristic hypotheses checked. The residue-two
potential-good case was explicitly read in the primary book. The
original Serre–Tate scan remains unread; do not depend on uninspected
corollaries or rerun that access route. The small congruence-kernel
verification allowed here connects the read finite-inertia criterion to
the finite level used in this specific estimate. Its purpose is a
checkable reproduction, not another theorem discovery or a reproof of
Neron–Ogg–Shafarevich. Clark–Xarles section 2.4, p.9, already records
the finite-level consequence; retain its wording qualification from
the source comparison.

The mathematical checks must separate inertia from its cyclic residue
quotient on the joint level fifteen, retain the cyclotomic determinant,
and bound the full level-four contribution after adjoining actual T_v.
Check matrix orders in both CRT factors, rather than multiplying
independent unramified degrees or replacing a local degree by its
ramification index. A fully written finite-dimensional argument is
sufficient; no mathematical script is required. If one is necessary,
its certificate must be complete and its printed output bounded.

Continue only with a proved uniform valuation at most ten and all
field-tower divisibilities justified. If the certified upper bound
exceeds ten, report only insufficiency; refutation requires an actual
survivor and place giving a lower bound above ten. A failed hypothesis
requires narrowing and a separately reviewed target. Do not subtract
the global core's order from a local group without proving its local
membership. A passing degree test supplies no sharpness, full different
estimate, original field-generation equality or complete repair.

Unresolved: IV reproduction authentication/current-version and def=
boundary, other primes, the complete different argument and field
prescription, alternative repairs, height-selected prime, independent
initial data, native input/action/factorization/pilot and essentiality.
Original finite B>=A stays open. Full matching/supporting Mathlib
coverage is unchecked. Expected classification: REPRODUCTION.
