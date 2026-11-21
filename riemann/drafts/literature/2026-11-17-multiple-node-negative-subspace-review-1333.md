# Simultaneous reciprocal-node detection: nomination1333, review1334

TARGET: Assess whether known indefinite moment results give a finite-degree negative-subspace certificate for k prescribed distinct nonreal conjugate pairs of summable reciprocal nodes, with explicit tail and degree bounds beyond L032's one-pair witness.
CHECKED: 2026-11-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Completed bounded exact-statement, indefinite-moment, Hermite/Grommer, finite-rank Hankel and quantitative Vandermonde searches; full local L024/L025/L030/L032/C032a and named prior comparisons checked. Primary statements and load-bearing scope/proof cases below inspected; no exhaustive absence or novelty claim.
SOURCE_EVIDENCE: Deng--Yang--Lu arXiv:2608.11520v1 Proposition2.5, Section3.2 Theorem3.4/full proof and Corollary3.5; Neiman MFAT19(2013),168--186, pp168--170 definitions and Theorem1.1 hypotheses; Yafaev arXiv:1304.2677v1 Theorems1.1,3.13--3.14, Lemma3.15/full proof and concluding uniform-subspace argument, and (5.6)/Theorem5.5, pp1--2,14--16,23--24. Direct primary links below.
COMPARISON: Finite-support simultaneous inertia is known; none of the inspected conclusions supplies the nominated explicit polynomial-degree and infinite-tail margin. Neiman assumes eventual inertia; Yafaev's bounded positive sign-function tail hypothesis is unverified here. L032 already supplies the one-pair explicit template, so only a uniform multi-pair quantitative extension merits work.
GAP: One common finite head, computable interpolation bounds, a simultaneous negative restriction and explicit sufficient degree remain to be justified. The beta-squared weight must be retained. No multi-pair theorem or new estimate is established in this literature turn.
REASON: Reject direct-import and qualitative-inertia-only routes; prepare one bounded specialization using assessed finite interpolation and L032 tail suppression. Its entire-space negative margin, rather than k individual negative tests, is the decisive test. New continuation requires separate approval before research.
SCOPE: k>=1 fixed; conjugation-invariant nonzero node multiset with sum |beta_j|<infinity as in L032; k distinct prescribed nonreal conjugate pairs, arbitrary finite positive multiplicities. Real polynomial algebraic-square form Q of L030; no Hermitian replacement, actual-Xi sign, uniform zero separation or RH assumption. Full matching Mathlib coverage unchecked.

The main gap remains unconditional Q(q)>=0 for every real polynomial
on the actual Xi nodes (L030-L032/C032a). The proposed intermediate
target concerns **quantitative detection**, not proof of that sign.
Its plausible use is a justified degree and error threshold for finite
mixed-form diagnostics with several candidate off-line pairs, including
control of the rest of the divisor. It cannot by itself exclude a pair
of unknown height or give a finite stopping rule for RH. If it supplies
no information beyond a qualitative reformulation, do not create an
extra lemma merely to record the reformulation.

Essential mathematical inputs to inspect are L024/L025 (actual node
summability and moments), L030 (the algebraic-square form) and L032
(the fixed one-pair tail-isolation construction). C032a states the
main equivalence and is a relevance constraint, not a positivity input.
Their hypotheses must be restated when specializing an external result.
The presently read L032 proof counts multiplicity in its head and tail
but interpolates distinct nodes. The new target must preserve that
distinction rather than treat repeated zeros as distinct evaluations.
No cross-notebook theorem is used.

## Recovery comparison and admission test

Three mechanisms were compared, without new mathematical work on them:

1. **Fixed polynomial exponents:** C019b and audit1333 exclude exactly
   the prescribed real-uniform family. The negative cubic survives the
   real-limit escape, so a new degree sweep or retrieval is unmotivated.
2. **Fixed boundary-cloud interpolation:** review1278/approval1279
   records only fixed sampling-data asymptotics and explicitly leaves
   growing/degenerating clouds and global membership unresolved.
   Reusing that fixed-data result as a global sign mechanism would not
   be a materially new test; no such continuation is selected.
3. **Simultaneous reciprocal-node detection:** L032 currently supplies
   one negative test. A source comparison can decide whether an explicit
   multi-direction tail threshold is already known or needs a bounded
   specialization. This diagnostic is independent of polynomial exponent
   construction and of the parked source-access routes.

Continue only if a primary theorem or clearly identified specialization
can produce an explicitly computable sufficient degree and a strictly
negative bound for **every nonzero vector in one k-dimensional polynomial
space**, using finite interpolation data and a stated summable-tail
majorant. Individual negative diagonal tests do not suffice. The source
review must compare exact hypotheses and relevant proof cases before
preparing any mathematical attempt. Import a matching theorem if found.
Otherwise isolate the missing quantitative statement and assess its value
before research. Abandon this diagnostic as a next research target if
only a qualitative inertia count or the existing k=1 statement emerges.

At nomination this was an uncovered target requiring a literature-only
turn. Review1334 below completes that source comparison; no proof attempt,
multi-pair derivation, script or lemma extension was performed. No concrete
independent theta sign construction has yet been specified to justify
creative routing; this quantitative source comparison is not labeled
creative. Later creative work needs a separate central sign mechanism
and a discriminating bounded test, rather than relabeling this diagnostic.

## Completed source comparison, step1334

Read the full five canonical local input files named above. L032 is
already quantitative for one pair: its constants depend on the full
finite head and a square-summable tail, and its degree bound is explicit.
Thus the comparison is not against a merely existential one-pair result.
Relevant failure/scope records reused: discovery106 Section "New primary
comparison", the heat-contact assessment's indefinite-form discussion,
and the full-pole assessment's AAK operator comparison. A scoped search
of moment/node/Hankel assessments and attempts found no separately
recorded simultaneous reciprocal-node certificate. This is a duplicate
check, not evidence of originality.

### Primary theorem scope

Zhiliang Deng, Xiaomei Yang and Huazhong Lu, *Contour Hankel dynamics and
indicator fields for the Riemann Xi-function*,
[arXiv:2608.11520v1](https://arxiv.org/html/2608.11520v1), 12 August 2026,
Theorem 3.4 and full proof: a conjugation-compatible finite measure with
positive real weights and equal positive conjugate weights has inertia
(r0+c,c,m-r) for m>=r=r0+2c. Distinct support determines r; multiplicity
only changes weights. The proof uses real/conjugate blocks, Vandermonde
rank and Sylvester congruence. This supplies no eigenvalue margin or
infinite-tail control. L030's beta-squared factor is not a positive
weight; direct identification is unjustified. No contour-coordinate
realization for arbitrary reciprocal nodes is assumed.

Evgen Neiman, *Indefinite moment problem as an abstract interpolation
problem*, Methods Funct. Anal. Topology **19** (2013), 168--186,
[publisher PDF](https://mfat.imath.kiev.ua/article/2013/02/nei2013.pdf),
pp.168--170: H_kappa is defined by eventual exact Hankel negative index;
the paper adopts indeterminacy, and Theorem 1.1 assumes membership in
H_kappa and biorthogonal polynomial bases to parametrize solutions.
Its Pontryagin construction therefore cannot establish the missing
index or a degree threshold from our node hypotheses. Read these
definitions and theorem hypotheses; its later parametrization proof
was unnecessary and was not audited. Krein--Langer [22] is an unread
reference, not an imported theorem.

D. R. Yafaev, *On finite rank Hankel operators*, J. Funct. Anal. **268**
(2015), 1808--1839,
[inspected preprint arXiv:1304.2677v1](https://arxiv.org/pdf/1304.2677v1),
9 April 2013, pp.1--2,14--16,23--24. Theorem 5.5 treats discrete
finite-rank Hankel sequences (5.6): a finite-support term plus finitely
many polynomial-times-geometric terms with nodes strictly inside the
unit disk, subject to self-adjoint conjugation symmetry. Theorem 1.1
counts both signs; nonreal exponential pairs contribute equally.
Theorems 3.13--3.14 preserve negative index when the background has a
bounded nonnegative sign-function. Their proof, including Lemma 3.15,
uses localized entire interpolants and uniform small norm on a finite
negative space, not an explicit polynomial cutoff. No such background
sign-function hypothesis is supplied by L024 or L032. Read this proof
case completely; the full finite-rank theorem proof was not audited.
The journal DOI endpoint failed; v1 was accessible. No source blocker
remains for this comparison, and no unverified coordinate/operator
specialization is imported.

### Search record and decision

Queries included `Hankel moment matrix complex conjugate nodes negative
eigenvalues Hermite theorem quantitative infinite zeros`, `indefinite
moment problem negative squares summable complex nodes polynomial
interpolation tail degree`, `Grommer Krein Hankel matrices number nonreal
zeros entire function finite negative squares theorem`, `Hankel nonreal
tail negative`, and `Hermite matrix inertia perturbation explicit
Vandermonde lower bound complex nodes`. Also searched Yafaev's exact
title to obtain the primary preprint after the publisher access failure.

Search-only leads, not assessed theorem inputs: Grommer's original real
zero criterion; Kytmanov--Khodos finite-rank root counts; generalized
Nevanlinna rational-index formulas; and Vandermonde conditioning papers
for circle/separated/clustered nodes. None is asserted to be absent or
novel. Arbitrary summable nodes do not automatically satisfy circle
geometry or uniform separation. AAK coverage is reused without browsing
it again because that operator mismatch is unchanged.

The direct-import test fails, but a concrete quantitative specialization
is identifiable: use L032's existing polynomial isolators with one
common head and require control of the entire k-dimensional restriction.
This is a proposed task, not a deduction made here. The separate ready
assessment is
`drafts/literature/2026-11-17-multiple-node-uniform-tail-specialization-1334.md`.
It requests an explicit degree inequality from finite data and a tail
majorant. Stop if that cannot be obtained without an unproved separation,
positivity or interpolation-conditioning hypothesis. Do not pursue a
qualitative index identity alone or repeat the source-access route.

No lemma, mathematical script, PROOF.md or DAG.md changed. Mathlib
coverage of the full target and external theorems remains unchecked.
This review improves local source coverage only; it establishes no
result beyond the inspected sources and no actual-Xi sign. No concrete
independent sign construction yet justifies creative routing. The
working record is `drafts/2026-11-17-multiple-node-source-working-1334.md`.
