# General relative construction — critical-audit coverage

TARGET: Critically audit L038's complete relative lattice and operator construction at arbitrary exact conductor N.
CHECKED: 2026-10-08
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the completed general-construction searches and assessment; compared L038 with its source notes, L029's evidence contract, audited L037 and ATTEMPTS/022--024; no duplicate completed L038 audit was found in the construction attempt and history/107.
SOURCE_EVIDENCE: Stein 2007 equation (3.2.1), Propositions 3.10--3.11, Theorem 3.13 and Section 3.4.1 https://wstein.org/books/modform/stein-modform.pdf with online weight-two statement https://wstein.org/books/modform/modform/weight_two.html; reflection equations (11)--(12), Remark 1.43 https://wstein.org/books/modform/modform/modular_symbols.html; Cremona corrected second edition Propositions 2.2.1--2.2.2, pp. 15--16 https://johncremona.github.io/book/fulltext/chapter2.pdf; Sergeraert arXiv:2411.02422v1 Sections 4 and 7, Theorem 1 https://arxiv.org/html/2411.02422v1; reused evidence in drafts/2026-10-08-general-relative-construction-source-notes.md and audit comparison below.
COMPARISON: Primary domains cover arbitrary positive levels, complete integral relative symbols modulo all torsion, oriented reduction, geometric reflection and the complete good-prime correspondence, plus arbitrary-rank rectangular diagonalization; L038's specific witness and coordinate assembly requires an independent mathematical audit.
GAP: Check the CRT lift algorithm, N=1 branch, every repeated-index relation, transposed saturation/section coordinates, rank-zero and zero-dimensional cases, every signed/infinite endpoint and full operator descent/reconstruction; coverage approval supplies no audit verdict or instance evidence.
REASON: Newly written L038 has not been critically audited; known source domains suffice for its separate bounded audit, with coordinate and witness details examined as specialization rather than imported wholesale.
SCOPE: One proof_audit of unchanged L038 with essential inputs L029 and audited L037; supplied exact conductor, minimal model/newform and independent good-prime a_ell remain assumptions. L030 is comparison only. No implementation, cutoff, runtime bound, twist supply or BSD conclusion.

The completed literature action was: Assess source coverage for a separate
critical audit of L038's complete relative lattice and operator construction
at arbitrary exact conductor N. This approves the TARGET for a separate
research turn; it does not execute the audit. The prior REVIEW_REQUIRED
entry is preserved in the startup snapshot and history/107.

## Primary comparison and bounded audit cases

The construction assessment and source notes were read before reopening
only the relevant primary passages. No new broad search was necessary:
target and arithmetic hypotheses remain within their assessed domains.
Additional literature reason: the essential unread comparison was the
new L038 assembly's audit scope, specifically its coordinate conventions
and edge cases. This reason does not reopen the parked twist sources.

Stein's online weight-two chapter, matching the cited 2007 printed
passages, was inspected at Propositions 3.10--3.11 (both reduction proofs),
Theorem 3.13 and the good-prime formula. Positive N includes level one;
the presentation removes torsion after imposing every relation and does
not exclude elliptic points. Path reduction includes formal infinity
convergents and unrestricted rational numerators. Import the stated
presentation theorem: its injectivity proof is omitted there and referred
to Manin Section 1.7, which remains unread. The audit must check L038's
chosen chains and repeated-index relation multiplicities against this
contract, including its level-one branch. The source supplies the complete
good-prime sum, not descent of individual summands. Its scope is the full
relative module, not only absolute cycles. These imports do not themselves
check L038's matrix transpositions or any constructed witness.

Cremona's corrected second edition Chapter 2, Propositions 2.2.1--2.2.2,
printed pp. 15--16, was reopened through its equivalence proof and coprime
lift discussion. Its coset criterion uses primitive pairs modulo N up to
unit scaling, with coprime integer representatives and Bezout top rows;
there is no prime-level restriction. This covers the required object.
L038's particular prime-factor avoidance/CRT recipe is a local algorithm
whose completeness, exceptional c_0=0 branch, determinant and lookup
witnesses still need audit; no source citation is substituted for that
check. Cremona's rational absolute theorem is not used for the lattice.

Sergeraert v1, 4 November 2024, Section 4's zero-pivot and zero-tail
branches and Section 7's entire Theorem 1 proof were reopened. The latter
is stated after reduction of the general rectangular arbitrary-rank
matrix; it supplies finite diagonalization, followed by divisibility
normalization. Section 6's growth warning is retained from the completed
notes. Elementary-operation transforms are the imported normal-form
input. L038's U A W=D transposition, integral kernel and section, all
original coordinates and removal of all torsion are specialization audit
questions. Include r=0, r=s and d=0 rather than relying on the later
elliptic-newform d>=1 assumption. No polynomial or practical runtime claim
is approved. Original Kannan--Bachem remains unread and unnecessary.

Stein's online General Modular Symbols equations (11)--(12) and Remark
1.43 were reopened with their normalization hypothesis. Weight two gives
the recorded negative relation between star and geometric reflection;
L029's convention is reused. The audit must retain projective infinity,
path orientation and complete segment/coset witnesses for reflection and
all ell+1 endpoint paths. Check the full saturated-kernel image and
reconstruction on every original generator, rather than just a proposed
eigenvector. General correspondence well-definedness is imported;
L038's algebraic realization is the audit target.

## Decision and limits

The adequate known-source coverage supports SPECIALIZE / REPRODUCTION
for this one critical audit. A citation-only IMPORT would not verify the
new coordinate/descent assembly. No new result, counterexample or script
was derived in this literature turn, and no theorem novelty is claimed.
No full matching Mathlib theorem was checked; unknown availability is
not absence. No lemma or DAG edit is warranted by coverage approval.

Main gap: rank E(Q)=m(E) for arbitrary m(E)>=2. Intermediate threshold:
a correct finite complete relative-lattice/operator construction supplying
L037's finishing premise. Plausible use: L037's eventual dimension-one
kernel and L029's full-relative real line, independently of twist scale.
Continue only if every coset/lift, all-torsion quotient, oriented path and
full operator descent/reconstruction survives the later audit. A failed
identity or missing case requires a precise repair before downstream use;
essential changed source hypotheses require another coverage assessment.
Independent q, normalized coefficient production, rational membership,
divisible Sha and general complex-order comparison remain unresolved.
Preserve ATTEMPTS/022--024 and unfinished work. No BSD candidate exists.
