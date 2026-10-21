# Sixty-core extremal transfer — completed source comparison

TARGET: Review source coverage for a 60-core extremal bound on 8-subset families satisfying the pair-packing constraint and L031's four-support restrictions.
CHECKED: 2026-10-07
DECISION: EXPLORE
SEARCH_EVIDENCE: Searched high-girth partial designs, four-block forbidden configurations, polynomial graph packings and exact 8/121 parameters; checked L001, C001a, L031, relevant L027/L030 proofs, prior triple-extremal/packing assessments and ATTEMPTS/019–022. No inspected source supplies the finite labeled cap; no novelty claim follows.
SOURCE_EVIDENCE: Read Glock–Joos–Kim–Kühn–Lichev arXiv:2205.05564v1 (https://arxiv.org/pdf/2205.05564v1), Theorems 1.1/1.6, printed pp. 2/6, and Section 9's matching/conflict construction and complete degree checks, pp. 53–55; Delcourt–Postle arXiv:2402.17856v1 (https://arxiv.org/pdf/2402.17856v1), Section 1.2, Conjecture 1.5/Theorem 1.6, p. 2; Ge–Shangguan arXiv:1706.03306v2 (https://arxiv.org/pdf/1706.03306v2), definitions and Theorems 1.3/1.5/1.6/1.10, pp. 1–6; Shangguan–Tamo arXiv:1902.05903v1 (https://arxiv.org/pdf/1902.05903v1), Theorem 3, p. 3. Reused named packing and signed-matrix coverage below.
COMPARISON: Near-optimal high-girth (n,8,4)-packings avoid even the entire four-block incidence pattern; a constant-factor asymptotic improvement does not follow just from L031's labeled subset. No inspected theorem supplies a cutoff or certificate at n=964; actual RS families need satisfy only the labeled exclusions.
GAP: The finite labeled local cap and exact 60-core safety transfer remain unproved; the literature supplies an avoidance mechanism but no usable finite obstruction or upper bound at these parameters.
REASON: Park direct import of an extremal cap and select one separately approved finite cubic-graph avoidance diagnostic; preserve the exhausted seven-point quadratic model and do not claim a new extremal theorem.
LITERATURE_REASON: Essential quantitative coverage was missing for the supplied REVIEW_REQUIRED target; the changed 60-core/four-support hypotheses were outside the ready L031 audit.
SCOPE: C001a's fixed H, a 60-point core C, residual 8-subsets of H minus C with pair intersections at most three and exactly L031's labeled six-noncontainment restrictions; source comparison only.

## Gap, intermediate target and decision test

The main gap is arbitrary-center safety at 68 agreements, with
955<=t_star(m)<=957. A sufficiently small uniform or summed residual-family
cap could feed a core-incidence certificate. The correct 60-core transfer
and sufficient cap remain mathematical work; neither is derived here.

Residual A corresponds to C union A of size 68. Distinct residuals have
intersection at most three. Four residuals in L031's pattern have six
mutually disjoint 2-point pair-only overlaps and four 2-point private parts.
Their labels must satisfy L031's actual rank/noncontainment test; its
antipodal example permits this abstract pattern. Extra agreements and
arbitrary tuple width remain allowed. Never exclude all abstract patterns
when asserting a property of actual lists.

The supplied continuation asked for known packing bounds and avoidance
constructions. Continue only with a concrete finite quantitative test or
obstruction; abandon a repackaging of the stopped 61-core system. The
comparison below identifies a different finite avoidance diagnostic, not
a finite cap. L001, C001a and audited L031 are essential local inputs;
L027's incidence proof and L030's construction are comparisons. Cross-core
consistency, 67-agreement safety, full SDP feasibility and ABF equivalence
remain independent gaps.

## Inspected primary statements

Glock, Joos, Kim, M. Kühn and Lichev, *Conflict-free hypergraph matchings*,
[v1](https://arxiv.org/pdf/2205.05564v1), dated 12 May 2022:
Theorem 1.1 gives, for fixed s>t>=2 and ell, constants eta>0,n0 and,
for every n>=n0, a partial (n,s,t)-Steiner system of size at least
(1-n^(-eta)) binomial(n,t)/binomial(s,t), whose j blocks span more than
(s-t)j+t points for 2<=j<=ell. Theorem 1.6 permits a finite forbidden
collection of t-linear s-uniform hypergraphs with e>=2 edges and at most
(s-t)e+t vertices; t-linear means intersections <t.
The template has four 8-blocks on 20 vertices, with pair intersections two,
so s=8,t=4,ell=4 fits. Section 9 converts blocks to edges on t-subsets,
removes nonminimal conflicts and checks maximum degrees/codegrees.
No numerical eta or cutoff usable at 964 is supplied. This comparison
imports neither a finite packing nor an RS realization. The guessed v2
URL returned 404; readable v1 removes that access issue.

Delcourt and Postle, *Proof of the High Girth Existence Conjecture via
Refined Absorption*, [v1](https://arxiv.org/pdf/2402.17856v1), 27 February
2024 arXiv stamp (manuscript dated 29 February), Section 1.2, p. 2:
girth is the first g with g blocks on at most (q-r)g+r points.
Theorem 1.6 proves Conjecture 1.5: for q>r>=2 and prescribed girth,
all sufficiently large n satisfying binomial(q-i,r-i) dividing
binomial(n-i,r-i), 0<=i<r, admit a Steiner system of that girth.
Parameters q=8,r=4 and girth at least five cover the abstract template.
Divisibility and an unspecified cutoff prevent an assertion at 964.
Only the hypotheses were needed; the absorption proof was not audited.
This is an asymptotic lower-construction lead, not an upper cap.

Ge and Shangguan, *Sparse hypergraphs: new bounds and constructions*,
[v2](https://arxiv.org/pdf/1706.03306v2), definitions pp. 1–2 and
Theorem 1.3 p. 4: f_r(n,er-(e-1)k+1,e)=o(n^k) for fixed
r>=k+1>=e>=3. At r=8,k=4,e=4 this excludes every four-edge union on
at most 21 points, a stronger hypothesis than our labeled restriction.
Its upper bound cannot be applied. Theorems 1.5/1.6, pp. 4–5, concern
linear r-partite families without rainbow 3/4-cycles and asymptotic
n^(2-o(1)) constructions, not this finite cap. Theorem 1.10, p. 6,
also assumes exclusion of every small union. Their proofs were not
needed for these hypothesis rejections and were not audited.

Shangguan and Tamo, *Universally sparse hypergraphs with applications to
coding theory*, [v1](https://arxiv.org/pdf/1902.05903v1), Theorem 3,
p. 3, assumes r>=2,e>=3,v>=r+1 and gcd(e-1,er-v)=1, giving
asymptotic sparse lower bounds. For the whole-template comparison
(r,e,v)=(8,4,20), coprimality fails. The theorem is not applied or
repaired; its probabilistic proof and coding applications were not audited.

Reuse Bailey–Burgess, *Generalized packing designs*, author manuscript
14 November 2011, Definitions 1.1.1/1.1.3 and Proposition 1.1.4, p. 2,
from [the inspected assessment](2026-10-05-nested-floor-support-endpoint.md).
It covers ordinary (964,8,4,1)-packing without L031's labels. Reuse the
ordinary asymptotic Liu–Shangguan Theorem 1.4 comparison, arXiv:2401.00733v2,
from [the core-theta assessment](2026-10-06-core-theta-uniform-cap.md);
its opening packing definitions were also retrieved here. Neither provides
a finite labeled improvement. No numerical bound was computed here.

## Duplicate checks and bounded continuation

The earlier triple-extremal review rejected whole-pattern triangle
imports and unjustified weight-to-cardinality conversion. L027 supplies
a transfer method to specialize later, not a proved 60-core transfer.
L030 concerns seven-position quadratic graphs and intersections at most
two. Eight positions, cubic graphs and four-message incidence require a
new avoidance check. ATTEMPTS/019–021 remain stopped; ATTEMPTS/022 is
only an administrative park. The scoped search found no completed test
of the prescribed shortened F_121 cubic family.

The finite diagnostic is specified in
[its assessment](2026-10-07-shortened-cubic-four-pattern-test.md).
It asks whether that fixed family avoids the entire incidence pattern,
and, only if so, whether its size obstructs a sufficient uniform cap.
An incidence witness rejects this label-independent construction, not
the labeled counting route. This is one test, not an unbounded search for
evaluation sets. Its new ready assessment requires separate supervisor
approval next turn. No lemma, mathematical script, DAG edge or PROOF
argument was changed. Full matching Mathlib coverage: not checked.

Queries included `high girth partial designs r t e(r-t)+t sparse
hypergraphs theorem packing`; `Delcourt Postle high girth designs general
q r theorem`; `polynomial cubic graph packing forbidden four blocks
configurations Reed Solomon extremal`; `even free packings four
configurations Pasch generalized polynomial evaluation codes`;
`"cubic" "packing" "Reed-Solomon" polynomial configurations`; and
`"8" "121" "packing" design`. Exact-number hits were largely irrelevant,
not evidence of novelty. The earlier hypergraph Hoffman input is already
assessed and is not reopened without new spectra. Unread leads include
explicit even-free design constructions and newer matching variants;
none is used as an essential input to the finite diagnostic.
