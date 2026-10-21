# Simultaneous fourth-support recovery — completed counting review

TARGET: Determine whether L043's recovery equations and triple gates allow at most eleven distinct nonuniversal candidate parameters for every tau=1 local pencil.
CHECKED: 2026-10-08
DECISION: EXPLORE
SEARCH_EVIDENCE: Bounded simultaneous-support, affine-line incidence and subspace-design searches; compared L010, L041–L043, L016's analytic and fixed-label counting scope, saved recurrence/ray assessments and ATTEMPTS/008–009, /017, /019–021; actual queries and limits below.
SOURCE_EVIDENCE: Inspected Guruswami–Kopparty, Explicit Subspace Designs, March 2013 author manuscript, section 4.2 Theorem 14 and Claims 15–16 with full proof, printed pp. 9–10; inspected Goyal–Guruswami–Sun–Wootters, arXiv:2607.08516v1, Definitions 2.3, 2.12, 3.1–3.3, 3.7, Theorem 3.27(1) with proof and Theorem 5.6; reused the saved inspected Chojecki DR2/DR6–DRC and ray statements and primary MDS/shortening coverage.
COMPARISON: The inspected design theorem controls a specially constructed family with disjoint structured root blocks, not all overlapping four-support spans; the newer deterministic threshold needs an established design parameter and local profile, and its RS MCA theorem is probabilistic over evaluation points. Neither supplies the eleven bound for fixed H or for L043's relaxation. L016's count five remains label-specific.
GAP: Bound or refute simultaneous satisfaction of L043 (4)–(7) for distinct nonuniversal finite parameters, uniformly in labels and extension-field weights, without assuming fourth-weight gates, rational chart, equality or completion.
REASON: Ingredient coverage is adequate and bounded discovery established no matching import; approve one bounded mathematical attempt on the unchanged TARGET, without claiming novelty or the bound.
SCOPE: F=F_(97^20), H order sixteen in F_97, k=8, pinned cell, L041 local converse tau=1 pattern (2,2,3), audited L042–L043; arbitrary distinct original finite gamma_i, nonzero lambda and p*q*(1-p-q)*r*(1-r) nonzero. Count every four-set K other than A_0,A_1,A_2 and K_*, all quotient cases and shared-label containments, satisfying (4)–(7), before (9); parameters must differ from all gamma_i.
LITERATURE_REASON: Checkpoint 094 proposed a new uniform simultaneous count with REVIEW_REQUIRED coverage; fixed-support construction/audit and saved fixed-label enumeration do not assess this scope.

## Exact gap and comparison target

The main gap is L010's arbitrary sixteen-error equality. The intermediate
threshold is eleven distinct nonuniversal candidates for one gated tau=1
pencil, across all eligible supports simultaneously. L043 gives at most
one additional universal parameter. The proposed threshold would therefore
supply a prospective twelve-additional bound in this branch, leaving
universal extraction, other triple patterns, lower-weight accounting and
ABF26 identification independent. No challenge resolution is claimed.

Use L010, L041, audited L042 and audited L043 as essential local inputs.
L016 is an analytic antecedent and fixed-instance obstruction to naive
support summation, not a uniform numerical input. Read L043's hypotheses,
complete reduced criterion, normalization and quotient cases; read L041's
local criterion/converse scope, L042's hypotheses and audited conclusion,
and L010's count and equality hypotheses. Compare L016 through its full
triple gate and simultaneous-row obstruction. No canonical proof is
modified in this literature-only step.

The target deliberately drops the recovered fourth-weight exclusions (9).
A candidate satisfying (4)–(7) must not be called a full-weight error merely
because its projected system passes. Count distinct original finite T,
not supports, equations or rows. Retain the nonrational rho case, E=0,
mu=-1 and all zero/independent projected systems exactly as in L043.
The proposed count has not been established even over the prime field.

## Reused primary coverage and local duplicates

Reuse the inspected source extraction in
`2026-10-08-nine-union-fourth-support-incidence.md`, Primary recurrence
input and applicability, rather than reprove annihilator or decoder results.
The precise input is Przemek Chojecki, *Shortening Bounds for Reed–Solomon
MCA*, live author TeX v9.2 dated July 17, 2026, source lines 2785–2935,
`drc:lem-locator-recurrence` (DR2) and `drc:thm-exact-compiler` (DR6–DRC),
including their complete proofs and zero-direction cases,
[author source](https://raw.githubusercontent.com/przchojecki/rs-mca/main/RS_MCA_Paving_v9.2.tex).
It was opened today for source identification, without a new full extraction.
The source is mutable and is not certified identical to ePrint 2026/1463.
R=8, support size four, shifted moments eta_j=s_(j+1), distinct labels
and nonzero multipliers x meet its hypotheses over F. Its fixed-support
intersection compiler does not provide this simultaneous numerical bound.

Reuse the inspected bounded-residual-kernel and single-MDS-circuit ray
comparison in `2026-10-07-nine-coordinate-triple-compatibility.md`.
The latter's 36 bound requires every counted support inside a fixed
nine-set, whereas only the selected triple is so restricted here.
Reuse the general MCA and Tamo incidence scope/size comparisons in
`2026-10-07-six-coordinate-twelve-incidence-bound.md`; a planar incidence
or fixed received-word list is not automatically this syndrome-pencil count.
The saved Hall Theorem 5.1.1, printed pp. 63–64, and Marquez-Corbella–Pellikaan
section 5, printed pp. 7–8, cover the MDS and shortening ingredients already
used in L041. No changed hypothesis requires refreshing those extracts.

L016's thirteen isolated rows share the same pencil weights; its proof
uses that simultaneity and a triple-weight gate to reduce the saved class
to one isolated row plus one universal parameter. Summing eligible rows
would miss that argument. Its supports and parameters 0,1,2 are fixed,
and its finite certificate does not cover arbitrary labelings. L043's
separate audit verifies each support's equivalence, not a total count.
This proposed uniform count is outside both established conclusions.

## New primary simultaneous-incidence comparison

Guruswami–Kopparty, *Explicit Subspace Designs*, March 2013
[author manuscript](https://www.math.utoronto.ca/swastik/subspace-designs.pdf),
section 4.2, Theorem 14 and Claims 15–16, printed pp. 9–10; construction
hypotheses and complete proof inspected on 2026-10-08. Numbering here is
this manuscript's, not a claimed match to the 2016 journal version.

For s<=t<=m<q, gamma generating F_q^*, and alpha of full degree r in
F_(q^r), require S_alpha={alpha^(q^j)*gamma^i:0<=j<r,0<=i<t} to have
size rt and be pairwise disjoint. In V=F_q[X]_(<m), the subspaces
H_alpha={P:P(alpha*gamma^i)=0 for 0<=i<t} satisfy
sum_alpha dim(W intersect H_alpha)<=(m-1)s/[r(t-s+1)] for every
s-dimensional W. The proof uses a nonzero folded Wronskian, its rank
loss and root multiplicities on disjoint shortened blocks.

These are vanishing-polynomial subspaces with controlled blocks.
L043 uses all four-support moment spans and quotients by missing shared
columns; no identification preserving those incidences and the required
block conditions has been supplied. Arbitrary four-sets can overlap.
The theorem is a relevant counting mechanism, not a certificate for this
family. We do not specialize it, dualize it without proof, or assert that
the relaxed family is a strong subspace design. No reproof is authorized.

Goyal–Guruswami–Sun–Wootters, *Locality of Curve-Decoding and Improved
Proximity Gaps*, [arXiv:2607.08516v1](https://arxiv.org/html/2607.08516v1),
submitted July 9, 2026; inspected Definitions 2.3, 2.12, 3.1–3.3, 3.7,
Theorem 3.27(1) and its complete proof, and Theorem 5.6 on 2026-10-08.

Definition 2.12 requires average coordinate-kernel dimension at most
 tau(r)*dim(A) for every code subspace A of dimension at most r.
Theorem 3.27(1) excludes an r-local profile/row-span pair (V,U) when
 tau(r)<R_V(U), where Definition 3.7 maximizes the threshold over proper
subspaces of U. Its proof projects to negative potential, applies
rank-nullity to encoded columns and uses that design inequality.
Theorem 5.6 assumes independently uniform RS evaluation points,
R<=1-delta-2*eta, q>=n*exp(Omega(ell^4/eta^7)) and
n>=Omega(ell^4/eta^7); its MCA conclusion holds with high probability.

No suitable tau inequality or profile threshold is established for our
fixed H and relaxed recovery systems. Nor are our evaluation points
random. Thus neither result can be imported as an eleven-parameter bound.
In particular an MCA theorem about actual errors does not itself certify
a relaxation omitting fourth-weight gates. Theorem 2.15, attributed there
to GG25 Theorem 4.7, was read as a source lead only, not imported coverage.

The underlying Goyal–Guruswami ECCC TR25-166 revision 1 (March 2026)
[download](https://eccc.weizmann.ac.il/report/2025/166/revision/1/download/)
returned Internal Error. Its abstract/metadata and author publication links
were inspected, but its theorem proofs remain unread. This is a
nonessential lead for this target: the independently accessible primary
comparisons above establish no usable matching hypotheses. Do not infer
that all relevant work has been excluded or that this source is globally
unusable. ABF26, Jo26 and the recorded campaign/ePrint blockers remain
parked; they supply no premise or novelty claim here.

## Bounded discovery and failure record

Actual queries issued on 2026-10-08:

- `"Reed Solomon" "affine line" "subspace" intersection list decoding`
- `"strong subspace designs" "Reed Solomon" Guruswami Kopparty theorem`
- `"Reed-Solomon" "syndrome" "simultaneous" support incidence`
- `"RS MCA" "ray" Chojecki`
- `Guruswami Kopparty Explicit subspace designs pdf theorem 14`
- `"Reed-Solomon" "simultaneous" "support" "affine" count`
- `"mutual correlated agreement" "count" "support"`
- `"Optimal Proximity Gaps for Subspace-Design Codes" Reed Solomon`
- `"Reed-Solomon" "simultaneous recovery" support`
- `"Reed-Solomon" "eleven" "MCA"`
- `Goyal Guruswami "Optimal Proximity" arxiv 2025 pdf`

Search hits on random-code decoding, storage recovery, later design-code
papers and secondary summaries are discovery leads, not inspected theorem
coverage. The bounded search established no exact match for the uniform
relaxation. Failed search does not establish novelty. Exact Mathlib
coverage remains not checked, with no absence claim.

ATTEMPTS/008–009, /017 and /019–021 were read in full. Preserve the
zero-syndrome-kernel blindness, fixed-triple generator stop, refuted
six-edge/eight-vertex extraction, exhausted cyclic containment,
positive-only rank-sampling stop and surviving support-only packing.
The present target changes to arbitrary tau=1 labelings and simultaneous
actual recovery equations; it does not repeat those exhausted tests.
No cross-notebook theorem is used. No calculation, enumeration, new
mathematical derivation, lemma or mathematical script was performed.

## Ready bounded continuation and decision test

One POTENTIALLY_NEW mathematical attempt on the exact TARGET is ready:
this classification means only that the documented search did not establish
coverage, not certified originality. Reuse L010, L041 and audited L042–L043.
Attempt a uniform symbolic count or an exact gated counterexample for the
same relaxed systems, retaining all shared-label containments, quotient
ranks, finite-chart exclusions and arbitrary F weights. Account for
simultaneous affine recovery constraints and parameter collisions before
using a support tally. Prime-field tests can refute a universal bound with
a fully verified witness, but positive samples cannot prove it.

Continue if a proof gives at most eleven distinct relaxed candidates under
these unchanged hypotheses, or establishes a relevant uniform constraint
with the remaining count gap stated. Abandon this relaxed eleven threshold
if an explicit gated local pencil has at least twelve distinct eligible
nonuniversal finite parameters satisfying (4)–(7); verify the complete
recovery equations and triple gates, not only projected compatibility.
Keep the potential actual-error bound using (9) open in that event.
If the attempt only repeats L043 or requires unjustified descent, save
that obstruction and reassess. No count, global improvement or complete
candidate is asserted by this review. Mathematical exploration usage is
unchanged by this literature-only turn.
