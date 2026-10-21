# Normal-closure local degree at two — proposed source comparison

TARGET: Assess whether L089's fixed 2-adic domain and L090's full conjugate fields support the uniform bound v_2([(G_o^nor)_w:T_v])<=10 for every v above 2, w above v and all six orderings.
CHECKED: 2026-10-20
DECISION: IMPORT
SEARCH_EVIDENCE: Step368 read L089's domain/invariant hypotheses, L090's complete ambient/conjugate-field proof and L092's global-only comparison; searched the scoped normal-closure records and ATTEMPTS/033–035. Exact searches and primary readings are recorded below; no matching changed-field theorem was identified, with no novelty inference.
SOURCE_EVIDENCE: April 2020 IV reproduction Proposition 1.3(i),(ii) and proof pp.11–12, Proposition 1.8(v)–(vii) with proof pp.19–21, Theorem 1.10 proof (i),(ii) pp.23–24; Silverman AEC second edition (2009), VII.5.5 pp.197–199, A.1.3/1.4(b) pp.412–413, VII.7.1/7.3 pp.201–202 with proofs, read in the linked book reproduction; Milne ANT v3.08, 7.50–7.54 pp.127–129, 7.58 p.131, 8.10/8.13 pp.139–141.
COMPARISON: Ten is the relevant 2-primary degree allowance in the inspected source use, conditional on the other different-estimate hypotheses. Standard potential-good, finite-inertia and completion results cover a later local specialization through L090's actual ambient field; neither global degree twelve nor the source's odd-residue Legendre case decides it.
GAP: No local degree bound is proved here. The remaining specialization must control the joint odd-torsion image, its cyclic residue quotient and full four-division extension at actual places; a passing bound would not establish a complete field repair.
REASON: The newly inspected residue-characteristic-two coverage makes this an independently testable calculation using known methods, without reopening authentication or the exhausted cyclic Frobenius separator.
SCOPE: Import only the source comparison and standard inputs below. The proposed mathematical continuation is assessed separately in 2026-10-20-normal-closure-local-two-degree-test.md and receives separate next-turn approval.
LITERATURE_REASON: Changed-field local degree control and the characteristic-two proof case were outside the ready global-degree assessment.

## Completed source comparison — step368

The earlier proposal is retained below as historical scope. This review
imports known source inputs only; it does not calculate the bound.

### Exact source use

Read the same [April 2020 IV reproduction](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%204.pdf).
Proposition 1.3(ii) uses n_i=v_p([k_i:k_0]) and requires k_i/k_1
Galois with k_1/k_0 tame; its bound is d_i<=d_0+n_i+1/e_0,
with absolute valuation ord(p)=1. Its proof includes the n_i=0
case, reduction to a p-group, and the degree-p Kummer step.
Theorem 1.10(ii) uses the torsion-group allowance at 2,3,5 in the
printed different/conductor increment. Thus ten is a relevant
sufficient degree input at two; it is not a necessary sharp threshold
or a complete different calculation. Proposition 1.8(vi)'s extra
local Legendre assertion assumes 2 invertible in the valuation ring
and cannot cover this dyadic test. No source mismatch forces a
changed threshold. Authentication/current-version qualifications
from step364 remain; no authentication retry was undertaken.

### Read standard inputs and precise scope

[Silverman, The Arithmetic of Elliptic Curves, second edition, 2009](https://studylib.net/doc/28155304/the-arithmetic-of-elliptic-curves),
VII.5.5, pp.197–199, characterizes potential good reduction by
integral j. The residue-characteristic-two proof is A.1.3 and
A.1.4(b), pp.412–413, using Deuring normal form. Both its integral
parameter case and converse were read. VII.7.1 and VII.7.3,
pp.201–202, give the good-reduction/unramified-Tate-module criterion
and the finite-inertia characterization; both proofs were read.
The chapter assumes complete discretely valued K with perfect K
and residue field. All actual finite extensions of Q_2 meet these
hypotheses. OCR drops negation signs in several displayed formulas;
use the theorem statements, not those corrupted formulas. The ENS
PDF failed; this is a readable reproduction of the primary book,
whose second-edition title/ISBN and page headings were inspected.

[Milne, Algebraic Number Theory, v3.08, 19 July 2020](https://www.jmilne.org/math/CourseNotes/ANT.pdf),
Theorem 7.50, Corollaries 7.51–7.52 and Example 7.54, pp.127–129,
cover unramified extensions and their finite-field cyclic groups.
Theorem 7.58(a), p.131, identifies the inertia quotient. Proposition
8.10, p.139, identifies actual completion groups with decomposition
groups; Proposition 8.13, p.141, gives restriction in towers.
These are finite Galois statements, not equality of different
completions. Reuse Milne FT v5.10, Theorem 3.17/Remark 3.18,
pp.39–40, already covered in step364, for the ambient subfields.

Reuse L090's inspected Weil-pairing/determinant input (Silverman
III.8.1(c,d)/Corollary 8.1.1, pp.94–96). No reproof of these
standard geometric or local-field theorems is needed.

### Auxiliary source status, without a source-access loop

[Serre–Tate, Good reduction of abelian varieties, Annals 88 (1968),
492–517](https://wstein.org/papers/bib/Serre-Tate-Good_Reduction_of_Abelian_Varieties.pdf),
section 2, Corollary 3, p.498, is an original lead for the common
finite-level inertia kernel. The scan opened but supplied no readable
continuous text or screenshot through the available tools. Indexed
page extracts are not treated as full inspection. JSTOR supplied no
readable article and shell retrieval failed DNS. Do not route another
turn to these access retries.

[Clark–Xarles, Local bounds for torsion points on abelian varieties](https://mat.uab.cat/~xarles/local.pdf),
the inspected author-hosted 23-page version, section 2.4, p.9,
explicitly records good reduction over K(A[N]) for potentially good
A over complete K and N>=3 prime to residue characteristic. Its
opening sentence has an apparent wording omission concerning potential
good reduction and is not used as an unconditional theorem. This
supports the known overlap, but the proposed proof need not rely on
unread original Serre–Tate pages: the fully read Silverman finite-inertia
and unramifiedness criteria permit an explicit congruence-kernel check.
That small verification is justified as a checkable finite-level
implementation for the changed-field degree estimate; it is a
reproduction of known mathematics, not a novelty claim. Do not
reprove the imported reduction criteria or claim the original scan
was read.

### Duplication, proposed specialization and limits

The targeted local record search found only L092's explicit warning
that global degree does not decide local degree. ATTEMPTS/033's
classification access, /034's order-four Frobenius powers and /035's
IV authentication are different mechanisms and remain stopped.
No source inspected states this exact normal-closure estimate.

L089's integral-j domain is within the hypotheses of the book's
criterion. L090 supplies M=Q(E[60]) containing the actual closure,
and T=Q(E[2]); full coordinates and every conjugate are retained.
The later proof must account for local inertia on the joint odd
levels, the cyclic unramified quotient, the mod-four kernel over T_v,
and all actual extending places. This comparison approves those
methods, not their numerical outcome. In particular the global
order-two core need not lie in a chosen decomposition subgroup;
no local division by its order is assumed.

The exact mathematical target and continuation/abandonment test are in
`drafts/literature/2026-10-20-normal-closure-local-two-degree-test.md`.
The same-bound attempt is useful even with the original finite B>=A,
other primes, different estimates, field prescription and essentiality
unresolved. No lemma, mathematical script, PROOF or DAG was modified.
Full matching and supporting Mathlib coverage is unchecked.

Queries included: `Mochizuki Legendre normal closure local`;
`potentially good reduction torsion local Serre Tate degree 24 elliptic 2`;
`Serre Tate Good reduction abelian varieties 1968 pdf theorem 2 corollary`;
`local field GL2 15 torsion degree elliptic`; and the exact paper title.
Modern classification papers and secondary search results were leads
only; no uninspected classification or claimed absence is imported.

## Invocation-start proposal — historical

This was REVIEW_REQUIRED before step368; no calculation was authorized
in this literature turn.

Retain audited L089,L090,L092: one survivor, fixed c,h,d_*,e_* and
both domains, fixed closure, all six literal full-coordinate G_o,
and T=F_tpd. Keep d=6 and epsilon_d=1. Completions are at actual
extending places v,w; no equality across orderings is assumed.
Do not substitute an old named member or prime seven.

Main gap: original finite B>=A. Plausible downstream use: determine
whether the 2-primary local degree input survives loss of the global
group-size argument. Ten is v_2(C_0); its precise sufficiency for
any different estimate must be checked, not assumed. Even a passing
test would leave Galois/tame-intermediate hypotheses, other primes,
full different estimates and the exact field prescription unresolved.

Continue only if primary local results and the fixed-domain hypotheses
support a bounded independently checkable test on these same fields.
If ten is not the relevant allowance, document the mismatch and review
a corrected target separately. Persistent missing coverage requires
parking dependent calculations and choosing an independent target;
do not repeat authentication. No favorable local outcome is predicted.

Reproduction/current-version and def= qualifications, alternative
models/repairs, height-selected prime, independent initial data,
native input/action/factorization/pilot and essentiality remain open.
Full matching/supporting Mathlib coverage is unchecked.
LITERATURE_REASON for the next turn: changed-field local degree
control is outside the ready global audit and lacks essential coverage.
