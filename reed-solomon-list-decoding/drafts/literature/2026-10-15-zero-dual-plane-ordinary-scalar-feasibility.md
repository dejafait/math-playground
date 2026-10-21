# Zero-dual plane with ordinary scalar rows — source scope approved

TARGET: Test whether L068's zero-dual plane w=w_star contains a column satisfying every ordinary scalar row on all 85 five/seven and six/seven types at all six presentations.
CHECKED: 2026-10-15
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the inspected scalar comparison in 2026-10-14-simultaneous-shell-ordinary-scalars.md and L062; checked L021/L053's full pair definitions, L065/L068's column scope, ATTEMPTS/044,050 and history/234. Fresh queries were `"constant weight" "Schrijver" "scalar" triple inequalities fixed pairs feasibility` and `"Schrijver" "1024" "68" "seven"`; they located the primary Schrijver paper but no inspected family-specific verdict.
SOURCE_EVIDENCE: Freshly read Schrijver DOI 10.1109/TIT.2005.851748 author manuscript III.B (62)–(65) and complete explanation after (65), printed p. 7; Kim–Toan arXiv:1212.3467v1 III.A Remark 11 and III.B (31)–(35), conditions (i)–(iv), printed pp. 8–9. Reuse Polak's indicator and union-index coverage in foundations/12. Inspected the complete original a13 value at /exact/primal/8 in delsarte-lp-results.json.
COMPARISON: These necessary scalar conditions cover all actual triple orbits, including the added 85 types and their other-anchor presentations. L062 covers only the 121 old types; L068 establishes its square and nonnegative zero but omits the added scalar upper/lower rows. No inspected source decides feasibility on this prescribed plane; general PSD completion does not impose these scalar rows.
GAP: Apply the imported rows exactly to the full two-variable plane with unchanged moments and original pairs through p13, producing a rational feasible point or a complete exact infeasibility certificate. No such calculation or verdict is supplied by this review.
REASON: Essential source hypotheses, normalization and the formerly omitted p13 input are now covered. Approve one bounded finite reproduction; do not repeat source review without a changed hypothesis or essential new lead.
LITERATURE_REASON: The added ordinary scalar constraints and through-thirteen pair input were outside the approved nonnegative-only affine-family audit; this separate comparison closes that source-scope gap.
SCOPE: Exactly TARGET, one common real (u,v,w_star), original positive rho and p7, unchanged L061/L062 dictionary and L021/L053 pairs, L065 affine coordinates and all inherited Boolean/forbidden/equal-union and range conditions. No seven/seven free-moment completion, alternate dual, pair/base retuning, labeled averaging or global feasibility test.

## Primary import and hypotheses

Import Alexander Schrijver, *New code upper bounds from the Terwilliger
algebra and semidefinite programming*, IEEE Trans. Inform. Theory 51
(2005), 2859–2866, DOI 10.1109/TIT.2005.851748,
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
III.B (62)–(65), printed p. 7. It assumes a nonempty binary
constant-weight code; linearity and RS structure are unnecessary.
The triple normalization is (62)–(63). Condition (65)(ii) gives
nonnegativity, an incident-pair upper bound and the scalar lower bound.
Its proof after (65) uses row domination in the two indicator averages;
(iii)–(iv) use pair distances and the three-word symmetric difference.
That argument explicitly retains repeated words. The suspect complement
prefactor in (61) is unused. Canonical theorem and qualifications remain
in foundations/04; no reproof or new canonical theorem is needed.

Cross-check Hyun Kwang Kim and Phan Thanh Toan, *Improved Semidefinite
Programming Bound on Sizes of Codes*,
[arXiv:1212.3467v1](https://arxiv.org/pdf/1212.3467v1), 14 December 2012,
III.A Remark 11, III.B (31)–(35), printed pp. 8–9.
Their even d>=4 and d<2w<=n assumptions hold at d=10,w=68,n=1024.
Equation (31) sets impossible multinomial indices to zero. Conditions
(i)–(iv) reproduce the scalar bounds, permutation equalities preserving
t-s, and zeros at forbidden nonzero distances. Section III.C adds stronger
inequalities; these are outside the present target and their omission
must not become a full-feasibility claim.

Both primary PDFs were directly accessible in this turn. No local
snapshot or checksum is asserted. Search snippets and secondary results
were discovery leads only, not theorem evidence. Reuse the stronger
hierarchy/completion comparisons and Polak's indicator proof already
recorded in the ready scalar assessment and foundations/12; nothing
there supplies a verdict for the new affine slice. Full matching Mathlib
coverage remains not checked. No novelty is inferred from the search.

## Exact application contract for the later calculation

Essential local inputs: L021,L053,L061,L062,L065,L067,L068 and
foundations/04,12, retaining L068's inherited normalization/range inputs.
Read the complete needed affine coordinates/certificate values when
implementing; a preview cannot certify the resulting inequalities.

L053 fixes N=binomial(1024,68), M=(U+1)/2, rho=M/N>0 and
p0=1, p1=...=p4=0,

    p_h=a_h/[2*binomial(68,h)*binomial(956,h)]  (5<=h<=68).

L021 specifies every a_h by its exact 64-equation system Ax=1; it is
not permissible to introduce a new p13 variable. Its saved vector is
ordered h=5,...,68, so a13 is entry 8 (zero-based). Full selected-value
extraction, not a preview, returned

    a13 = 808753696404081487284494974858496/11.

Thus the required p13 is exactly this a13 divided by
2*binomial(68,13)*binomial(956,13), with no change to L053's factor two.
This is extraction of a canonical input, not a new computed bound.
Reproduction command:

    python3 ../scripts/loop/inspect_json.py scripts/finite-support/delsarte-lp-results.json --pointer /exact/primal/8 --full

The later mathematical attempt must check its pair import against L021's
specification and independently reconstruct the relevant rows; this
review does not re-audit the whole LP certificate.

Reuse L062's established source normalization y=x(triple)/rho, obtained
from the ordered orbit count N*O and source denominator M*O.
L065's free entries are f_j=c_j+u*a27_j+v*a33_j+w*a42_j;
the actual conditional moment is y=p7*f_j, not f_j or rho*f_j.
Fixed entries retain the full L062 lookup, not a distance-only rule.
L068 specifies w_star=beta/alpha exactly and proves the complete family
identities and attained zero. Do not approximate w_star in a certificate.

L065 already specifies all 85 types (l,i,j), l=5,6 and
0<=i,j<=l. Its full atoms, in masks 0,...,7 for D,E,G bits 4,2,1, are

    (949-l+j,7-j,l-j,j,i,l-i,7-i,61-l+i).

Its stated half-distances are l,7,l+7-i-j. The five/seven types need
pairs through twelve; six/seven needs through thirteen. These are
application ranges of the existing dictionary, not a new lemma.
The attempt must reconstruct them from complete atoms at every support
order and check nonnegative regions and source orbit denominators.
Reuse L065's partition into 20 represented, 16 forbidden and 49 free
keys, verifying it rather than treating the counts as a certificate.

For each of all six presentations regenerate (a,b,t,s),
h=a+b-t-s and original t-s, and impose the source slacks

    y >= 0;  p_a-y >= 0;  1+y-p_a-p_b >= 0.

This includes other-anchor bounds involving p_h even when that anchor
is outside the retained PSD layers. Preserve equal complete unordered
keys and all source equalities; distance multisets alone are insufficient.
Forbidden nonzero half-distances 1,...,4 force zero. Repeated-word
lookups in the inherited dictionary use the appropriate pair moment,
although these 85 cross-column triples have distinct supports by L065.
Retain the already audited old scalar rows, not a new old assignment.
Do not add new/new seven/seven rows or unrepresented variables in this
bounded target. Such rows and simultaneous PSD remain separate gaps.

## Relevance and discriminating test

Main gap: arbitrary-center safety at 67/68 agreements, bracket 955–957.
Intermediate target: exact scalar feasibility on the entire zero plane,
with both u and v allowed to vary and all original nonnegativity retained.
A failure of u=v=0 alone cannot exclude the plane. ATTEMPTS/044's old
scalar pass and ATTEMPTS/050's original nonnegative-domain zero remain
valid; neither duplicates this changed necessary-constraint test.

Downstream use: an exact exclusion of the plane would make L068's
unchanged square pointwise strictly negative on this strengthened slice,
without asserting a uniform negative margin. A surviving rational column
would stop these scalar rows as a repair of the fixed-dual strict-sign
argument; it would not supply simultaneous PSD. L067's immutable negative
obstruction is retained in either case.

Continuation/abandonment test: give one exact rational (u,v) satisfying
every row and shared lookup, or a complete exact rational nonnegative
combination of the affine inequalities giving a strict contradiction.
Check every coefficient, sign and residual in original normalization;
a numerical solver status or sampled rows are insufficient. If neither
certificate is found in the bounded attempt, save the reasoning and
report exploration honestly. No further source turn is needed at this
unchanged scope. Independent PSD, global moments, label constraints,
measures, packings and RS realization remain unresolved. This approval
contains no new mathematical derivation or feasibility claim.
