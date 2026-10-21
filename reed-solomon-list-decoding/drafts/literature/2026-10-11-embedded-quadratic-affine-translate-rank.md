# Auxiliary affine-translation rank test — completed coverage comparison

TARGET: Test whether L047's five-graph obstruction remains full rank under every common auxiliary affine translation p_i(Z) -> p_i(Z)+aZ+b for (a,b) in F_137^2, using L047's fixed actual-label embedding.
CHECKED: 2026-10-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 151 reused the embedded/common-center and uniform-extension assessments, searched the specific working notes, histories 139–150 and ATTEMPTS/021,031 for auxiliary affine/polynomial translations, and performed three narrow external searches; no inspected exact-match rank result or completed local test was found.
SOURCE_EVIDENCE: Reinspected Alrabiah–Guruswami–Li https://arxiv.org/html/2304.09445v3 (26 July 2023), Definition 2.5, Lemma 2.7 and its complete proof, Remark 2.8, Theorem 2.9 and Lemma 3.1 hypotheses, printed pp. 7–10; reuse Shangguan–Tamo https://arxiv.org/pdf/1911.01502v1 (4 November 2019), Lemma 4.3 common-root proof case, pp. 11–12, from the retained uniform-extension assessment.
COMPARISON: Signed stars cover the needed finite-field equations; symbolic/random guarantees and same-hyperedge variable permutations do not certify the translated fixed labels. L047 gives the unshifted finite input; C047a covers actual common multiplication only. The finite translation family requires its own certificate, without reproof of a generic theorem.
GAP: Coverage is ready; actual-label reconstruction, incidence verification, exact ranks and tuple/common-root applicability remain mathematical obligations for the later bounded test. No translated rank or new exclusion is proved here.
REASON: Changed auxiliary translations lie outside the common-shift-only stop, and the known framework supplies an adequate method for this independently testable finite diagnostic; no exact-match theorem or novelty is established.
SCOPE: Exactly L047's five polynomials, ordered seven evaluation points, original 61-core and exponential set labeling; add one common aZ+b over F_137, then recompute representatives and actual E-labels. No other embedding, independent graph translation, changed core, actual multiplicative shift or cap calculation is authorized by this assessment.

LITERATURE_REASON: The proposed auxiliary translation changes actual labels beyond the retained C047a scaling scope; inspect that changed scope once before calculation, retaining ready common-root and signed-star coverage.

## Gap, proposed input and decision test

The main gap is arbitrary-center safety at 67 or 68 agreements in the
fixed rate-1/16 instance; the bracket remains 955–957. The intermediate
target is the exact rank diagnostic in TARGET. Full-rank translated
configurations could supply additional labeled five-message exclusions
for a later strengthened support model. A useful quantitative cap,
all-core transport, cross-core consistency, compatible RS subfamilies and
the ABF definition comparison remain independent unresolved gaps.

Continue with verified full-rank configurations only. A certified singular
translate refutes the universal full-rank claim; preserve all singular
cases and do not infer a distinct-message realization. Even universal
full rank would not establish cap strength or safety. Failure of the
label/incidence/common-root checks requires isolating the failure rather
than suppressing the parameter or claiming a theorem.

## Retained and newly inspected source coverage

Omar Alrabiah, Venkatesan Guruswami and Ray Li, *Randomly punctured
Reed–Solomon codes achieve list-decoding capacity over linear-sized
fields*, arXiv:2304.09445v3, 26 July 2023, provides signed evaluation
stars in Definition 2.5. Lemma 2.7 assumes distinct scalar RS codewords;
its proof subtracts the last coefficient vector. Remark 2.8 permits
variable exchanges within identical hyperedges, not arbitrary changes
of evaluation values. Theorem 2.9 is symbolic over a rational-function
field. Lemma 3.1 samples uniformly random distinct evaluation points.
These conclusions do not settle this fixed exponential labeling.

The necessary specialization is already written for the original labels
in L047 and for common actual scaling in C047a. Their complete relevant
common-root and tuple passages were compared here. Reuse the inspected
Shangguan–Tamo Lemma 4.3 common-root proof case from
[the uniform-extension assessment](2026-10-10-embedded-quadratic-uniform-extension.md).
Its characteristic-two unsigned matrix method is not imported in
characteristic 65537. The BGM v4 generic/random-domain comparison in
[the common-center assessment](2026-10-10-embedded-quadratic-common-center.md)
is adequate and unchanged; no repeated retrieval or new generic-rank
proof is needed. Optional automorphism and MCA leads recorded there
remain unread and unnecessary to this exact finite test.

C012a's field and generator passage was inspected: E=F_65537 is the
prime subfield of F=F_(65537^28), H has order 1024 and g=19139 has
that exact order. L030 supplies the fixed T and independence under set
bijections; it supplies no actual-label rank symmetry. C047a's coefficient
scaling identity cannot be assumed for an auxiliary translation followed
by taking representatives. Any wrap modulo 137 must be evaluated before
forming the actual exponent; do not replace this operation with a common
actual multiplier or an actual affine change of variable.

Full matching Mathlib coverage for the translation-family claim is **not
checked**. Reuse only supporting factor-theorem/composition declarations
and their hypotheses retained in C047a's Mathlib section and its assessment.
The scaling declarations support C047a's existing proof; they do not
certify these new ranks. No Mathlib absence claim is made.

## Discovery, duplicates and retained failures

External queries on 2026-10-11 were:

- `"Reed-Solomon" "intersection matrix" "translation"`
- `"Reed-Solomon" "quadratic graphs" "137"`
- `"Reed-Solomon" "agreement hypergraph" "fixed" rank`

The searches returned general reduced-intersection/random-code sources
and unrelated results; secondary snippets were not used as theorem
evidence. The pinned AGL primary statement and complete relevant proof
were read directly before completing the comparison. No exact-match
result was established; this bounded search is not evidence of novelty.

The targeted local search covered embedded-quadratic assessments and
working notes, L047, C047a, L030, histories 139–150, and ATTEMPTS/021,031.
The prior fixed search and audit do not test this parameter family.
L030's polynomial-difference translation used to count pair moments is
not a duplicate actual-label rank certificate. L048 and ATTEMPTS/031
stop exactly the old common-shift pattern cap; ATTEMPTS/021 stops the
old local edge system. Both stops remain intact. This proposed stronger
pattern diagnostic is independently testable, without reopening those
unchanged prescriptions or claiming it defeats their deletion argument.

## Bounded later calculation and certificate obligations

Use exactly L047's q0=(33,27,3), q1=(106,120,2), q2=(0,0,0),
q3=(64,44,1), q4=(34,47,2), in constant/linear/quadratic order;
T=(16,64,70,102,112,118,121). Use C={g^j:0<=j<=60} and
(t_j,y) -> g^(61+137*j+rep(y)), with rep in {0,...,136}.
Enumerate all ordered (a,b) in {0,...,136}^2, lexicographically,
and evaluate q_i(t_j)+a*t_j+b modulo 137 before applying that label map.
This is a prescription only; no graph value or rank was calculated here.

Reconstruct every full support, all subset intersections and every signed
star from the complete incident index set at each actual outside label.
Use the least incident index as anchor, omit index 4's coefficient block,
and order rows by actual label then other index. Verify the incidence
pattern and row count rather than copying old numeric labels or silently
assuming unchanged rows. Check seven distinct outside labels per graph,
core disjointness, selected-support size 68, distinct graphs and the
full injection. Check L030 applicability at the set level; never transport
auxiliary field operations to E.

Save a full exact certificate under scripts/finite-support/ in the later
research turn: every parameter, auxiliary values, actual exponents/labels,
intersections, matrix, rank, full elimination operations and transformation
identity. Verify the RREF, including zero rows; a full-rank square matrix
needs its complete inverse identities or an equivalent exact certificate.
For every singular case save a nonzero kernel witness and check every
row equation. Preserve and summarize all singular cases, the complete
rank distribution and any failed checks. The unshifted (0,0) case must
agree with L047's audited input, including determinant 26669 when using
its canonical row/column order. Do not rerun the old search.

The later mathematical write-up must justify common-root degree reduction
including zero differences, nonvanishing outside C, selected rather than
exact agreements, and coefficient identities over F in every tuple row.
No single scalar row distinguishing every tuple is assumed. Exact rank
identities over E can be used over F only with the stated field embedding.
A singular matrix does not establish simultaneous pairwise distinctions
or a compatible center. Store complete evidence, inspect load-bearing
values fully, and print compact bounds, failures and certificate paths.

Decision SPECIALIZE authorizes a later REPRODUCTION of the assessed
method on this finite family, subject to separate supervisor approval of
the updated assessment. This literature step writes no lemmas or
mathematical scripts and establishes no translated mathematical result.
