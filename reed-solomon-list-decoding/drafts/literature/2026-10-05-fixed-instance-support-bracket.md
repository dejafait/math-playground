# Fixed-instance universal support bracket: completed assessment

TARGET: Determine the largest error index certified safe by L001's common-support bound for n=1024, k=64, F=F_(65537^28), epsilon*=2^(-128) and every m>=1, and combine it with L019's t_star<=957 to bracket the pinned boundary.
CHECKED: 2026-10-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched local support/packing/binomial/Johnson assessments and failures; searched primary-source leads for Reed Solomon list size binomial agreement packing bound, Guruswami Sudan Extensions Johnson bound, and packing t-subsets blocks Schonheim. Exact queries and inspected sources are recorded below.
SOURCE_EVIDENCE: Read L001 in full, C012a's hypotheses/admissibility/threshold passages, L019's hypotheses/conclusion and construction passage, and the pinned model; read Bailey-Burgess, Generalized packing designs, 2011-11-14 author manuscript, Definitions 1.1.1/1.1.3 and Proposition 1.1.4, p. 2; read Guruswami-Sudan, Extensions to the Johnson bound, February 2001 manuscript, Theorem 1/Corollary 2, p. 2, and reused the prior Section 2.4/Theorem 5 proof comparison.
COMPARISON: L001 already proves the universal simultaneous-agreement bound needed for this target. Known Johnson-Schonheim packing bounds retain nested floors and can improve that bound; Johnson list bounds have a restricted radius condition and their alphabet is q^m here. Neither supplies an exact arbitrary-center boundary on the fixed subgroup.
GAP: Only an exact finite-grid application of established L001 and assembly with established L019 remain for this target; no safe endpoint is computed here. The sharp boundary, safety at 67 agreements and pinned-model/ABF comparison remain unresolved.
REASON: Approve the unchanged saved target as a reproduction using existing universal and unsafe certificates, without reproof of a general packing or Johnson theorem and without a novelty claim.
SCOPE: n=1024, k=64, H<=F_65537^* of order 1024 inside F_(65537^28), every m>=1, closed simultaneous column-Hamming balls, ambient threshold 2^(-128)*65537^28; largest index certified by L001 only, not largest actual safe index or a packing-refinement calculation.
LITERATURE_REASON: Universal interior-grid safety was outside the saved rational-center assessment; this separate comparison now completes that missing essential coverage.

## Gap, downstream use and decision test

The main gap is the unknown arbitrary-center list maximum and sharp grid
boundary. The intermediate target is a universal safe endpoint on the same
fixed instance as L019's unsafe witness. Its downstream use is a rigorously
qualified interval for the pinned boundary, rather than another witness
family. Continue if exact adjacent-grid comparisons yield a nontrivial safe
endpoint. If they do not, report this certificate's limitation; failure of an
upper certificate is not unsafety. Independent source/model and sharper-bound
gaps need not be closed to make the bracket useful.

The later calculation should retain the floor in L001 and compare its integer
value multiplied by 2^128 with 65537^28. It should check the proposed endpoint
and the next index, with monotonicity or a complete bounded grid search
justifying maximality *for this certificate*. L019 supplies the separate
unsafe index, not sharpness of L001. No mathematical computation, new lemma
or theorem application result is produced in this literature turn.

## Local coverage, duplicates and recorded failures

L001's complete proof counts common k-subsets for whole tuples, not separately
for each row. Its hypotheses require only distinct domain points, 1<=k<=n,
m>=1 and errors at most n-k. C012a already establishes the finite field,
proper smooth subgroup and ambient threshold; L019 is audited and already
establishes t_star<=957. These existing results supply every essential
mathematical input for the proposed bracket. No field enlargement, uniform
fiber assumption or additional extension-field reduction is required.

The 2026-09-25 finite-support audit and 2026-10-03 endpoint assessment were
read narrowly and reused. They concern the universal count and endpoint
attainment, respectively; this step does not reproduce their proofs. The
2026-10-05 pole audit is complete. ATTEMPTS/004, /006, /007 and /008 record
failed family-specific certificates; their search hits and PROOF overview
are sufficient to distinguish the new universal application. No such stopped
route is reopened. The support bound itself is old local mathematics; only
its finite-instance safe side is awaiting calculation.

## Primary theorem comparison

Robert F. Bailey and Andrea C. Burgess,
[Generalized packing designs](https://www.math.mun.ca/rbailey00/papers/packings.pdf),
author-hosted manuscript dated November 14, 2011, p. 2, Definitions 1.1.1
and 1.1.3, Proposition 1.1.4: for positive integers v>=b>=r and lambda,
the maximum number of b-subsets with each r-subset in at most lambda blocks
is bounded by

U_lambda(v,b,r)=floor((v/b) floor(((v-1)/(b-1)) ...
floor(lambda*(v-r+1)/(b-r+1)) ... )).

The relevant dictionary is v=n, b=agreement size A, r=message dimension k,
lambda=1. L001 supplies the needed uniqueness on common k-subsets.
Choosing A columns from larger agreement sets is the applicability issue;
the target uses L001's already-proved count and requires no new packing
lemma. Nested floors give a known potentially stronger alternative, not a
new mechanism. Its numerical benefit and exact packing number are untested.
The manuscript cites Johnson and Schonheim originals, which were not read;
no claim about their exact formulations is based on those unread references.
Only the ordinary-packing statement was inspected, not the paper's later
constructions.

Venkatesan Guruswami and Madhu Sudan,
[Extensions to the Johnson bound](https://web.stanford.edu/class/cs250/restricted/guruswami_sudan.pdf),
February 2001 manuscript, Section 2.2, Theorem 1 and Corollary 2, p. 2:
for an s-ary length-n code with minimum distance
D=(1-1/s)(1-delta)n, 0<delta<1, and error radius
 e=(1-1/s)(1-gamma)n, 0<gamma<1, the strict condition
gamma>sqrt(delta) gives list size at most
min(n(s-1),(1-delta)/(gamma^2-delta)). Equality gives
2n(s-1)-1. The closed-ball definition and arbitrary-center quantifier were
read. Prior assessment 2026-09-26-current-target.md, Section 2.4/Theorem 5,
pp. 5-6, covers its weighted version and proof comparison and is reused.
For simultaneous interleaving its alphabet is s=q^m; the polynomial-root
input in L001 supplies minimum column distance n-k+1. Thus neither the
alphabet-dependent n(s-1) allowance nor an unchecked scalar substitution
certifies the ambient epsilon*q target. The radius hypothesis must be
checked before using the smaller Johnson allowance. This comparison imports
no new Johnson specialization and does not compute a Johnson endpoint.

These are known universal bounds, not random-domain, folded-code or
higher-order-MDS substitutes. Previously assessed fixed-slack differential
bounds are not recalculated: their explicit constants have not been shown
useful on this finite instance. No source inspected here determines its
exact arbitrary-center maximum.

## Search record and qualifications

External queries executed:
- `Reed Solomon list size binomial n k binomial agreement k packing bound`
- `Guruswami Sudan Extensions Johnson bound 2001 pdf theorem list size`
- `packing bound t subsets blocks binomial v t binomial k t Schonheim primary theorem`

Author-hosted theorem text above was retrieved before larger passages.
Johnson PDF screenshot retrieval failed; its text extraction was readable,
and the earlier weighted-theorem assessment was available. No essential
statement depends on the failed screenshot. Search snippets and other leads
(random-domain results, multiplicity bounds, covering-design texts) were
not treated as inspected theorems or novelty evidence.

Full matching Mathlib coverage: not checked. Pinned ArkLib definitions and
boundary conventions are already recorded in foundations/02-pinned-list-model.md;
they do not supply the support count. The calculation must cite canonical
L001, C012a and L019 and retain their qualifications. SPECIALIZE licenses
REPRODUCTION for this exact saved action; no new theorem reproof is needed.
