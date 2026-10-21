# Finite ordinary packing lower bound — primary source comparison

TARGET: Assess finite ordinary (965,9,5,1) packing lower bounds against L041's uniform cap plus L042's 1024-block loss.
CHECKED: 2026-10-10
DECISION: EXPLORE
SEARCH_EVIDENCE: Searched exact 965/9/5 packing and A(965,10,9) parameters, finite packing-design lower bounds, constant-weight RS constructions, Graham–Sloane/B_h constructions, and graph augmentation; checked L041/L042, relevant existing assessments and ATTEMPTS/019,021,024,026.
SOURCE_EVIDENCE: Inspected Xu–Chen arXiv:1505.06524v4 Section 2 pp. 3–4, Propositions 2.1–2.2 and Theorems 2.1–2.2 with proofs; Derksen arXiv:math/0311385v1 Proposition 2, Corollary 4, Theorem 5, Lemma 6 and Theorem 7 pp. 2–5; Keevash arXiv:1401.3665v4 Definitions 1.2–1.3/Theorem 1.4 p. 2 and cutoff qualification p. 14; reused Bailey–Burgess definitions and ordinary bounds and the prior Liu–Shangguan asymptotic comparison.
COMPARISON: The direct q=107,w=9,r=5 graph-source bound is 14025517325, below the strict required 19800269675; the inspected design theorem has no applicable finite cutoff. Neither supplies the sought obstruction. This is a source comparison, not a new packing theorem or a global nonexistence conclusion.
GAP: A finite ordinary packing above 19800269675 remains absent; assess a materially larger augmentation rather than repeat the nested upper bound or assume sufficiently-large-v existence at 965.
REASON: The review identifies an explicit finite baseline and a different bounded augmentation diagnostic; no adequate threshold-crossing theorem was found in the sources checked and no novelty is inferred.

The main gap is still arbitrary-center safety at 68 or 67 agreements.
This intermediate target tests whether the specific L041 local cap
route can be obstructed using a finite ordinary packing and audited
L042. No threshold-crossing packing or obstruction is asserted here.
The required strict comparison is with L041's sufficient uniform cap
19800268651 plus the worst-case 1024 deletions. A bound below that
comparison may still be useful evidence, but does not stop the cap route.

Essential local inputs are L041's exact admissibility and benchmark,
and L042's audited comparison of finite maxima. Ordinary packings may
be relabeled onto a 965-point ground set, but actual-label admissibility
must follow from L042, not assumed permutation invariance. Finite
ordinary lower-bound sources are now assessed below. The review used
the exact finite parameters, standard packing-design and constant-weight
code terminology, stronger construction leads, and effective hypotheses.
The inspected finite cases and unread leads are distinguished below.

Continue to mathematics only after an applicable source or a concrete
assessed construction has been identified. Park any source-dependent
route that remains persistently blocked; do not substitute a nested
upper bound or an unspecified sufficiently-large-v theorem for a lower
bound at v=965. ATTEMPTS/019,021,024,026 remain intact: their stopped
local relaxations, anchored graph and repeated upper-bound reviews do
not decide this new finite lower-bound question. Cross-core consistency,
common-center RS realization, safety and the ABF comparison remain
unresolved even if a large admissible local family is obtained.
Matching Mathlib coverage for a finite construction is not checked.

## Primary statements actually inspected

Liqing Xu and Hao Chen, *New Explicit Binary Constant Weight Codes
from Reed-Solomon Codes*, [v4, 7 August 2015](https://arxiv.org/pdf/1505.06524v4),
printed pp. 3–4, Section 2. Read the complete graph and augmentation
proofs; the [HTML transcription](https://arxiv.org/html/1505.06524v4)
confirms the fraction in Theorem 2.2. For a prime power q and integers
q>=w>r-1, Proposition 2.2 gives A(wq,2w+2-2r,w)>=q^r.
Theorem 2.1 adds w; with r>=3, Theorem 2.2 gives
q^r+w+w/(floor((w-r+1)/(q-w+r-1))+1).
The graph proof evaluates polynomials of degree at most r-1 on w
distinct field points. The augmentation proof uses at most two
evaluation columns. The q=107,w=9,r=5 substitution has length 963,
weight nine and distance ten, and its stated bound is 14025517325.
Embedding its coordinates into 965 adds two unused coordinates.
This source-level comparison is below 19800269675; it does not
authorize replacing the source augmentation by an arbitrarily large
family. No reproof or augmented packing is supplied in this turn.

Harm Derksen, *Error correcting codes and B_h-sequences*,
[v1, 21 November 2003](https://arxiv.org/pdf/math/0311385v1),
printed pp. 2–5. Proposition 2 and Corollary 4 give a constant-weight
distance 2h+2 fiber and A(n,2h+2,w)>=binomial(n,w)/c(n,h).
Theorem 5(a) uses distinct a_i in F_q and a degree-h polynomial P
with P(a_i) nonzero, yielding a B_h sequence in (F_q[X]/P)^*;
5(b) uses degree h+1 and the quotient by F_q^*. Theorem 7 chooses
the latter when n-1 is a prime power, otherwise the least prime
power q>=n and the former. Lemma 6 assumes 0<h<q and gives the
minimum group-size cases. Read the full Proposition 2/Corollary 4
proofs and every Lemma 6 case, including repeated linear factors.
Theorem 5 refers its proof to Bose–Chowla; that referenced original
proof was not audited. These are finite formulas for h=4,w=9,
not an inspected numerical certificate above our threshold. No
source optimization or new fiber estimate is attempted here.

Peter Keevash, *The existence of designs*,
[v4, 27 November 2024](https://arxiv.org/pdf/1401.3665v4),
printed p. 2, Theorem 1.4: fixed q>r>=1 admit c_0,alpha>0 and
h,n_0 such that a K_q^r-divisible, (c,h)-typical r-graph on n>n_0
with density d>n^(-alpha) and c<c_0*d^(h^2) has a decomposition.
Definitions 1.2–1.3 specify every local divisibility condition and
common-neighborhood typicality. Section 3, printed p. 14, explicitly
leaves n_0 and omega_0 uncomputed. For block size nine and strength
five, the theorem does not verify its cutoff at 965, nor does it
remove divisibility. Its absorption proof was not needed for this
rejection and was not audited. Reuse the previously inspected
Liu–Shangguan Theorem 1.4 comparison in
`drafts/literature/2026-10-06-core-theta-uniform-cap.md`; its
sufficiently-large-n/o(1) conclusion has the same finite limitation.

## Search scope, unread leads, and decision

Queries included `packing design lower bound D(n 9 5) Reed Solomon
code construction`, `"packing designs" "lower bounds" "construction"
t`, `"A(31,10,9)" OR "A(32,10,9)" OR "A(965,10,9)"`,
`"constant weight codes" "four" "supports" "Reed-Solomon"`, and
`"constant weight" "augmentation" "Reed Solomon"`. Exact-parameter
searches did not retrieve a matching threshold-crossing theorem;
that is not a novelty or nonexistence finding. The original
Graham–Sloane scanned PDF was located at
https://web.vu.lt/mif/s.jukna/boolean/Graham-Sloane-codes.pdf but its
load-bearing scanned text was not obtained. The theorem-level
Derksen source provides independent finite coverage; the older scan
is an unread lead, not an essential blocker for the proposed test.
Small-code tables and other search hits were not imported as theorems.

The direct quoted graph bound misses the benchmark; no global
packing route is stopped. The proposed future diagnostic is an
exact five-subset resource upper test for substantially larger
augmentations on at most four columns. Its precise scope is saved
in `drafts/literature/2026-10-10-four-column-packing-resource-test.md`
for separate next-turn approval. No resource inequality,
compatibility proof, LP, construction or L042 specialization is
derived here. Essential inputs remain L041/L042. A certificate
below the required augmentation size would stop this restricted
mechanism; a larger relaxation allowance would leave actual
construction open, not prove a lower bound. Cross-core consistency,
RS realization, safety and the ABF comparison remain unresolved.
