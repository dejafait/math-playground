# Shared degree-four moment extension — source comparison completed

TARGET: Determine whether L028's outer f,F admits a degree-four shared moment extension annihilating every pair conflict and determinant hyperedge.
CHECKED: 2026-10-06
DECISION: EXPLORE
SEARCH_EVIDENCE: Notebook-scoped duplicate/failure search and Boolean-moment, hypergraph-independent-set, prescribed-moment-extension, set-packing and constant-weight four-point searches on 2026-10-06; queries and inspected passages are recorded below.
SOURCE_EVIDENCE: foundations/08-boolean-moment-source.md records GPT arXiv:0809.3480v3 Remark 3.6, Theorem 2.14, Corollary 2.15 and Proposition 2.18; Laurent PNA-R0108 Lemma 13 with complete proof; Polak arXiv:1703.05171v1 equations (1)–(3) and Proposition 1.1 with proof.
COMPARISON: The finite-independence-system formalism covers mixed pair/triple exclusions, but no inspected result decides extension of L028's prescribed f,F; Polak's full A_4 has additional conditioned matrices and cannot be substituted for the saved diagnostic.
GAP: Construct a common third/fourth-moment assignment with an exact PSD certificate for every actual core, or rigorously exclude the fixed assignment on one actual core; separate link mixtures and graph-only theorems do not decide this.
REASON: Essential source coverage is now sufficient for one bounded fixed-witness attempt; the hierarchy is known mathematics, while this witness-specific feasibility question remains unresolved and is not claimed novel.
SCOPE: L027's actual mixed edge system, L028's unchanged first/second moments, real Boolean moments through size four, one unconditioned order-two PSD matrix, and exact all-core construction or actual-core exclusion; no added nonnegativity or conditioned-matrix constraints, relabeling symmetry, optimization optimum or list-realization claim.

## Exact proposed diagnostic

For every actual core C retain V_C, G_C, J_C and L028's fixed f,F.
Seek real variables y_S for all subsets S of V_C of size at most four,
with y_empty=1, y_{A}=f_A and y_{A,B}=F_AB for distinct A,B.
Let the matrix indexed by all subsets I of V_C of size at most two
have entry y_(I union J) at (I,J). Require this matrix to be PSD and
require y_S=0 whenever S contains an edge of G_C or J_C.
The target is extension for every core, or rigorous exclusion on one
actual core. This is the saved diagnostic, not a feasibility assertion
or a claim of useful global strength.

This mechanism shares the third/fourth moments across different
conditional matrices. L029's independent mixtures need not have this
compatibility. The completed conditional-link diagnostic must remain
stopped; merely reoptimizing its individual theta bodies is not the
proposed work.

## Sources, applicability and comparison

The precise citations, imported statements, proof ranges, versions and
Mathlib qualifications are canonical in
[the Boolean-moment source record](../../foundations/08-boolean-moment-source.md).
This turn imports source coverage only; no local moment lemma or
extension/exclusion is proved.

For applicability, take Delta_C to consist of subsets of V_C containing
neither a G_C edge nor a J_C edge. Deleting vertices cannot introduce
an edge, and all singletons are allowed, so this is a finite independence
system with exactly the source's hypotheses. Its nonfaces are precisely
the sets containing one of the specified edges. Set the source's order
to two. The source indexes faces; the saved diagnostic retains all
indices, with zero entries whenever their union is a nonface. Nonface
pair indices therefore have explicitly zero rows. This is the convention
to justify when applying the citation, not a change of target. Fixing
singleton and pair moments to L028's values is an additional affine
restriction that the source does not solve. No reproof of the general
hierarchy is justified or approved.

The graph-only comparison uses Laurent's own index convention: t=1
means moments through 2t+2=4 and matrix M_(t+1)=M_2. It does not justify
propagating cubic hyperedge zeros by a graph argument; retain every
required triple and quadruple zero explicitly.

Polak's distance-only universe is a relevant additional-constraint comparison:
the residual vertices have weight seven on 963 positions, and the pair
conflicts are distance below ten. Its source also imposes PSD for
nonempty conditioning sets and scalar nonnegativity. The saved target
has no separately imposed y_S>=0 for triples or quadruples. Do not
silently add those conditions or identify this target with full A_4.
Actual determinant labels introduce further zeros absent from that
distance-only program, so its symmetric reductions are not licensed
for the labeled slice. Source tables are not evaluated for this instance.

L028 already supplies a genuine permutation-averaged distribution for
the pair graph alone; this does not assert J_C independence. L029's
separate affine-family mixtures do not supply one common higher
moment assignment. Neither supplies the missing extension by citation.
No equivalence with the old recursive lift, the earlier Schrijver SDP,
a probability distribution, or an unsafe RS list is assumed.

## Search and duplicate/failure evidence

Local search was limited to foundations/, drafts/literature/, ATTEMPTS/
and history/ for degree-four, Boolean moment, Lasserre and shared-moment
terms, after targeted reads of L027's hypotheses/model, L028's outer
construction and exact entries, L029's conclusion, the existing theta
source record and ATTEMPTS/019–020. Only the proposed review and the last
history entry named this target. The supplied overview records the older
distance-SDP failures; those are different fixed assignments and do not
decide this extension. Preserve both stopped link diagnostics.

External queries included:

- `Lasserre stable set hypergraph moment matrix union subsets forbidden edges level 2 Laurent`
- `Lasserre 2002 semidefinite programming relaxations 0 1 programs moment matrix stable set theorem`
- `"A Recursive Theta Body for Hypergraphs" Lasserre moment`
- `site.cwi.nl Laurent Lasserre stable set moment matrix hypergraph`
- `"hypergraph" "Lasserre" "moment matrix" independent set`
- `"Lasserre" "moment" "extension" stable set pair distribution packing`
- `Gouveia Parrilo Thomas theta bodies polynomial ideals hypergraph stable set moment matrix 2009 theorem`
- `"hypergraph" "independent" "Lasserre hierarchy" moments`
- `"137" "packing" "Lasserre" 7`
- `"set packing" "Lasserre" "pairwise" moments extension`
- `"constant weight codes" "quadruples" semidefinite moment matrix`
- `"moment extension" "stable set" prescribed`
- `"Lasserre" "set packing" "degree" integrality gap`

Primary readings were the statements and proof cases cited in the source
record, not search snippets. GPT's earlier Optimization Online June 2009
draft was inspected as a lead, then replaced by v3 for all imported
numbering and hypotheses: the later version explicitly qualifies general
closure claims. Laurent's [2014 ICM author manuscript](https://homepages.cwi.nl/~monique/files/16-5_Laurent.pdf), Section 6,
equation (6.1), pp. 17–18, was inspected as a terminology/reference lead;
the cited original graph lemma supplies the operative statement.
Laurent's 2007 [*Semidefinite representations for finite varieties*](https://ir.cwi.nl/pub/11663/11663D.pdf),
Theorem 23, p. 18, and the low-order discussion, p. 19, were inspected
as a convergence lead; no low-order extension theorem for this witness
was found there or is applied.

The Princeton report at https://www.cs.princeton.edu/techreports/2008/843.pdf
was an unread hypergraph-hierarchy lead: the initial PDF metadata loaded,
but targeted passage retrieval returned HTTP 403. Its hypotheses and
claims are not used. General integrality-gap search hits, including
Ghazi–Lee and set-packing material, remain unread leads, not coverage
of these deterministic labeled moments. They are nonessential because
GPT's finite-independence-system statement covers the needed formalism.
The bounded search found no theorem deciding the prescribed extension;
that is not evidence of novelty or a universal nonextension theorem.

## Continuation and stopping test

Essential inputs remain L027, L028, L029 and foundations/07; add the
known-source record foundations/08. Source coverage is ready for the
unchanged exact TARGET, subject to the supervisor's separate approval
of this newly completed assessment. No mathematical attempt occurred
in this literature-only turn.

One bounded attempt may seek a symbolic all-core assignment, or a finite
principal subsystem on one named actual core with an exact PSD
incompatibility certificate. Shared union entries and the unchanged
pair values must be retained. A numerical infeasibility report, a
failure of one ansatz or a symmetry assumption is insufficient. Certify
all entries/zeros and PSD for an all-core construction; certify every
used actual edge, fixed value and rational separation identity for an
exclusion. Singular determinant triples remain nonedges. Failure on
one principal subsystem means only that this subsystem did not exclude
the witness, not that an extension exists.

All-core extension stops this degree-four diagnostic for this witness.
One rigorous actual-core exclusion demonstrates an incompatibility
worth investigating, but supplies no bound below 1532496. With neither
result, record a bounded EXPLORATION and save the attempted mechanism;
do not reopen separate-link optimization. Follow the shared two-turn
reassessment and three-turn exploration limits.

All shared-moment feasibility and exclusion claims are unresolved.
An exclusion would detect only this witness; all-core extension would
stop this further diagnostic. Neither would itself give a sufficient
global cap or settle actual realization, 67/68-agreement safety, the
older full SDP or ABF equivalence. Mathlib coverage is not checked.
The known framework is imported, not newly discovered. The next
mathematical invocation must keep the exact saved target and scope;
any strengthened or materially changed diagnostic needs its own review.
