# Fixed-rectangle reality propagation: separate source-review nomination

TARGET: Review source coverage for propagating reality of every zero in Omega={|Re z|<100,|Im z|<1/2} through 0<=lambda<=1/20 from the finite-height initial theorem and C919c's boundary, allowing initial multiplicities and checking the backward-heat multiple-zero case.
CHECKED: 2026-11-21
DECISION: IMPORT
SEARCH_EVIDENCE: Step2159 reused the 9November compact-propagation assessment and step2150 boundary comparison, inspected the primary statements and essential proofs below, and searched exact compact propagation/backward-heat rectangle multiplicity terminology. The source covers the proposed finite-region statement; no novelty inference or new derivation.
SOURCE_EVIDENCE: Planat-Raymond arXiv:2611.06245v1 (4November2026), Section7 Lemma7.1, (22)-(23), Theorem7.2 and their complete proofs, plus Section7.1's initial-coordinate/zero-ordinate argument, https://arxiv.org/html/2611.06245v1#S7 ; Polymath1904.12438v2 Section3 Proposition3.1(i)-(ii), (28)-(33) and complete proof, https://arxiv.org/html/1904.12438v2#S3 ; Platt-Trudgian2004.09765v1 Theorem1 and Section2, printed p2, https://arxiv.org/pdf/2004.09765v1 . Exact applicability comparison follows.
COMPARISON: Theorem7.2 directly covers a closed time band and fixed rectangle, permits initial multiplicities, and concludes reality with simplicity only at positive times. L058 and audited C919c cover its analytic and boundary hypotheses; the finite-height theorem has ample range for the initial map. No general propagation reproof is needed.
GAP: Coverage is ready for a separate canonical theorem application and its hypothesis audit; no propagation lemma is established in this literature turn. Uniform head margin above1/2000000000, quantitative zero brackets/separation, higher degrees and global signs remain unpaid.
REASON: Newly available full boundary changes the earlier conditional comparison to an actionable known-theorem import. Citation and explicit applicability suffice; no novel compactness, motion or collision lemma is justified.
LITERATURE_REASON: Changed available hypothesis: C919c's full closed-band rectangle boundary is now audited. The exact initial finite-height-to-rectangle comparison and compact multiple-zero propagation were outside the completed five-functional audit and require separate coverage.
SCOPE: Completed one literature-only review of TARGET in step2159. No lemma or mathematical script changed. The separate application is specified in 2026-11-21-h2-rectangle-reality-import-2159.md and requires next-turn approval before invocation.

## Original nomination (preserved)

The main gap remains L030-L032/C032a actual-Xi all-degree algebraic
mixed positivity. The proposed intermediate target is confined to
reality inside the displayed fixed rectangle over the closed band.
Its plausible use is a later real-zero Gram lower-bound argument for
the rectangular head in C919c, compared with epsilon=1/2000000000.
Reality alone is not a quantitative lower eigenvalue bound; adequate
separation, weights or an alternative quantitative head input would
remain to be paid. Higher-degree and global signs remain unresolved.

The actual family, real type and heat PDE are those of L019/L058;
L018 fixes initial Xi coordinates. L919 fixes source coordinates
F(lambda,z)=8H_(4lambda)(2z). C919a and C919b enter through the
audited C919c boundary, with the unchanged Decimal contracts.
L466 is relevant only for its explicitly cited Platt-Trudgian initial
zero-location input; its separate all-order Laguerre import is not
needed for this nomination. The review must check both real signs
of the initial spatial coordinate, any zero-real-part case, all
multiplicities, and the precise finite-height range. Do not assume
a simple-zero census or extrapolate a positive-time asymptotic to zero.

Reuse the old compact-propagation assessment while checking its exact
source and applicability. Planat-Raymond's global numerical claim is
not an input: the earlier notes explicitly did not audit that claim
or its artifacts. Compare only the local theorem and its proof cases
with the older Polymath repeated-root result and the paid hypotheses.
The compactness step, treatment of initially multiple roots, a possible
first nonreal event and the final endpoint must all be covered. If a
needed theorem is conditional on all zeros being real globally, or
merely supplies local simple-root continuation, it does not pay this
target. No source conclusion is inferred from its abstract or title.

Preserve the step2156 outer-only representation stop, step2157
inner-evaluator budget stop, and L917/L920/L922 coefficient-enclosure
failures. This proposal supplies no new coefficient evaluator and is
not a radius, mesh, cutoff or precision refinement of those attempts.
The discriminating question is whether the existing finite initial
zero-location theorem and now-paid boundary satisfy a precise local
propagation result without an unproved collision or global-reality
assumption. Approve an import/specialization only after that comparison;
otherwise record the missing premise or source blocker and park the
dependent application. No proof of propagation has been attempted.

This is not labeled creative: it is a proposed application of known
local heat-zero methods to an independently testable finite region.
No justified new mechanism for the all-degree/global sign gap emerged
from the five-functional audit; that is the blocker to nominating a
central creative proof now. Full matching Mathlib coverage is unchecked.

## Step2159 completed source comparison

The nomination above records the earlier state, not a continuing source
blocker. The discriminating test passes at the level of source coverage:
the exact fixed-domain result is already stated and proved in the
inspected source. It needs no global reality assumption. This is local
source progress only; application is deferred to a separate turn.

### Primary result and load-bearing proof cases

Michel Planat and Dale James Raymond, *Certified Collision Exclusion and
an Unconditional Upper Bound Lambda<0.156821 for the de Bruijn-Newman
Constant*, arXiv:2611.06245v1, 4November2026,
[Section7](https://arxiv.org/html/2611.06245v1#S7), Lemma7.1 and
Theorem7.2 with complete proofs, were reopened. This recent preprint's
global claim and numerical artifacts are not imported. Section7 is a
self-contained analytic input, with its sign convention explicit.

Theorem7.2 assumes T,X,Y>0, a fixed open rectangle
Omega={|Re z|<X,|Im z|<Y}, joint holomorphy on a complex neighbourhood
of [0,T] times its closure, F_t=-F_zz, real type for real t, full
boundary nonvanishing at every time including endpoints, and reality
of all initial interior zeros. Its conclusion is reality and simplicity
for 0<t<=T. Initial simplicity is expressly unnecessary.

Inspected the essential cases, rather than just the theorem statement.
Lemma7.1 uses the joint Taylor expansion at a finite-multiplicity real
zero and the heat PDE. Equations(22)-(23) give the forward Hermite model
and its imaginary-root backward companion, with locally uniform scaled
errors. The proof establishes the Hermite roots' reality and simplicity
by Gaussian orthogonality. Conjugation-invariant small disks and Rouche
give real simple forward zeros; a second, fixed disk counts the entire
cluster. For multiplicity at least two the backward companion has a
nonreal pair, including when the multiplicity is odd and also has a
zero root. A disk missing the real axis retains a nonreal zero at
every sufficiently close earlier time. Thus a first positive-time
multiple zero is excluded without assuming initial simplicity.

Theorem7.2's proof counts all zero copies by the argument principle.
It uses the compact zero-free complement of finitely many disks to
exclude untracked zeros at nearby times; it does not label trajectories
or assume a uniform separation of infinitely many zeros. After the
initial forward splitting, an alleged last time of persistence has
only real zeros by off-axis disk persistence. A multiple zero there
contradicts the backward case just inspected. Simple-zero continuation
extends persistence, or supplies the final endpoint if that time is T.
The proof covers an empty interior census as well. No source proof
case needed for this target remains unread.

D. H. J. Polymath, *Effective approximation of heat flow evolution of
the Riemann xi function, and a new upper bound for the de Bruijn-Newman
constant*, Research in the Mathematical Sciences6(2019), article31,
[arXiv:1904.12438v2, Section3](https://arxiv.org/html/1904.12438v2#S3),
Proposition3.1(i)-(ii) and full proof through(33), were inspected again.
It allows complex/repeated zeros, uses the backward heat sign, and
gives the Hermite square-root splitting with a local exhaustive Rouche
count. Its constants depend on the zero/time/multiplicity. It supplies
no quantitative closed-band brackets. Its local statement alone is not
the compact-domain theorem; the latter is imported from Theorem7.2.
There is no reason to reproduce either result here.

### Applicability comparison, not an executed theorem application

| Source hypothesis or qualification | Local comparison for the later import |
| --- | --- |
| Time and rectangle | Use the theorem directly for local F with T=1/20, X=100, Y=1/2. These are strictly positive constants. |
| Joint holomorphy, PDE and real type | L058 supplies all three on C^2, hence on the required neighbourhood; the local time direction has exactly the source sign. |
| Whole closed boundary | C919c's audited conclusion covers all four sides and corners at every time, including zero and 1/20. Retain C919b's original Decimal contracts. Its proof uses L018 separately at zero time, so no positive-time bound is extrapolated to that endpoint. |
| Initial positive ordinates | L018's multiplicity-preserving local map is z=gamma+i(1/2-beta), not the doubled Polymath coordinate. Thus 0<Re z<100 uses only 0<gamma<100. |
| Initial negative ordinates | L018's conjugation for xi maps these to the same positive-height input; no separate negative-height verification or global RH is needed. |
| Initial Re z=0 | Section7.1 explicitly excludes this case by H_0(iy)>0 from the positive theta kernel. L019/L058 provide the local normalization of that same integral. This includes z=0 and does not assume a simple census. |
| Multiplicities and endpoints | Affine changes preserve multiplicity. Permit arbitrary initial multiplicities; the cited conclusion asserts simplicity only for lambda>0 and includes lambda=1/20. |

Dave Platt and Tim Trudgian, *The Riemann hypothesis is true up to
3 times10^12*, [arXiv:2004.09765v1](https://arxiv.org/pdf/2004.09765v1),
Theorem1, printed p2, verifies height3,000,175,332,800. Read the statement
and Section2's explanation of sign-change counting and the Turing
comparison accounting for all zeros. This height is greater than100.
Only zero location is imported; neither simplicity nor tabulated
brackets are needed. L466 is used solely to locate this citation,
not for its all-order Laguerre conclusion or its additional Sra input.

L919's source normalization is F(lambda,z)=8H_(4lambda)(2z), so a
comparison in H coordinates would use [0,1/5] and spatial cutoff200.
Applying the abstract theorem to F avoids changing its PDE coefficient.
Do not use the source's numerical separator at a different X, its
Corollary7.3 global-scale constants, or its announced Lambda bound.

### Duplicates, limits, search record and decision

Reused the 9November assessment's exact local-motion comparison and
step2150's boundary comparison. Narrowly read the canonical definitions
L018/L019/L058, L919's statement, C919b's hypotheses/conclusion, and
C919c's statement/boundary proof. No existing local compact-propagation
result was used as an established lemma. The preserved L058 warning
concerns propagation toward smaller time, not this increasing-time
application. Steps206,2156,2157 remain stopped: neither real-zero
propagation nor the cited theorem supplies a new coefficient evaluator
or a numerical head margin. No radius/precision/mesh retry is proposed.

Queries performed: `"backward heat" "zeros" "rectangle" "multiplicities"`;
`"Compact interior propagation" "7.2"`; `"Riemann" "finite" "real zeros"
"propagation" "Polymath"`. Other search hits, including an unsigned-strip
preprint and a separate Lean repository, remain unread leads and are
not inputs. No claim of novelty or of exhaustive literature discovery.
Full matching Mathlib coverage remains unchecked; no formalization of
this fixed-domain heat-propagation application is asserted.

IMPORT is justified because Theorem7.2 covers the entire proposed
propagation statement after the listed routine applicability checks.
No new general lemma is justified. Continue only with that known-result
application, retaining every arithmetic qualification and the
zero-ordinate check; abandon this import if an input fails its exact
hypotheses. Quantitative head margin, higher-degree and global signs
are independent unresolved obligations. The proposed import receives
separate next-turn approval; no propagation conclusion is added to
lemmas/, DAG.md or PROOF.md in this source-only turn.
