# Endpoint logarithmic clock — source assessment

TARGET: Determine whether, for every real B>=0, there are unbounded odd integers n=47+243k, k>=0, having no positive c<n with c=20 modulo 27 and T^s(c)=T^t(n) for integers 0<=s,t<=log(n)/log(12)+B, retaining actual parities on both paths.
CHECKED: 2026-10-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Focused endpoint, exact-cylinder, logarithmic-coalescence and rational-slope queries established no matching theorem; the executed queries and access qualifications are recorded below. No novelty or literature-wide absence is inferred.
SOURCE_EVIDENCE: Reuse the inspected Rozier Definition 1/Lemma 1, Sodelin ancestor/L4/L5 and LaDue both-case records in the three ready residue47 assessments; newly read Laurent (2008), section 1 including Theorem 2 and Corollaries 1–2, pp. 326–328, and section 4 real-case proof, pp. 345–347. Novgorodtsev v4.1 landing description was read, but its manuscript retrieval failed and no theorem was imported.
COMPARISON: Audited L026 covers every horizon under n>12^L; audited L027 covers strict subcritical coefficients. Finite parity coding, CRT and known two-logarithm separation cover supporting arithmetic, but none of the inspected sources states this endpoint two-path obstruction with a positive residue-20 companion and strict original-root order.
GAP: Sharpen L026's slope-above-one size requirement using its displayed powers of 2 and 3 and shifted offset, then select unbounded CRT roots whose endpoint clock fits the proved integer horizon for every fixed B; retain the audited lambda<=1 argument and every path guard. No improved size estimate or endpoint conclusion is proved here.
REASON: Essential source coverage suffices for one separate quantitative specialization attempt; the missing difference is a local all-horizon size estimate and root selection, not an unread essential coalescence theorem. Standard parity coding, CRT and the existing anchor proof should be reused, not reproved.
SCOPE: The exact TARGET using L026's valuation-4 congruences, its existing inverse-offset estimate, and a proposed sharper size guard in the lambda>1 case. Preserve integer L>=6, both zero clocks, actual paths and all residue/positivity/order guards. Other cylinders, larger coefficients and new anchor or parity mechanisms are outside this assessment.
LITERATURE_REASON: Equality of the coefficient with 1/log(12) removes L027's positive coefficient slack and lies outside its assessment; this separate review compares that changed hypothesis before any derivation.

## Relevance and approved test

The main gap is universal eventual descent. The intermediate target is
exactly TARGET. A two-path cover with a smaller residue-20 companion could
transfer convergence to a hypothetical least bad residue-20 root; the
endpoint obstruction would constrain the permitted time in such a route.
Neither a least root nor a cover, convergence of finite bases, or
convergence of the selected roots is assumed. Other surviving cylinders
and a universal terminating mechanism remain independent gaps.

Approve one separate mathematical attempt. Seek an all-horizon size guard
that can replace n>12^L in L026 and permits roots satisfying both its
congruences and log(n)/log(12)+B<=L, or a rigorously justified integer-clock
version of that comparison, for every fixed real B>=0. The roots must be
unbounded. This is a desired threshold, not an established estimate.

First test the reduced powers in L026's lambda>1 expression together with
0<=d<=2^s-1, treating every permitted exponent sign and zero case. This is
distinct from repeating L027's positive-slack comparison. If this yields a
usable height margin, continue with CRT representative selection and
explicit integer rounding within the same attempt. Preserve or separately
justify every use of the old size guard. If it supplies no usable margin,
stop this endpoint selection mechanism and record the exact obstruction.
Finite samples, a fixed-B example or increasing an old constant horizon do
not establish the target. Failure of the proposed lower obstruction does
not establish an endpoint cover.

The target is now ready for a subsequent research invocation. This turn
establishes source coverage only: outcome EXPLORATION, classification
NOVELTY_UNCHECKED, no mathematical exploration budget spent. No lemma,
mathematical script or candidate solution was produced.

## Local inputs, duplicate checks and stopped routes

The complete L026 proof was read, including all slope cases, the precisely
transferable anchor prefix, the exceptional anchor 47, the formal suffix
bound and audit qualifications. L027's representative selection and
real-horizon comparison were inspected. L025's shifted inverse-offset
passage and Attempts 014–016 were checked narrowly.

For L>=6, L026 assumes n>0,
n=47 modulo 3^(L+4), 81n+97=0 modulo 2^(L+1), and n>12^L.
It excludes every smaller positive residue-20 companion with both clocks
at most L and fixes v_2(n+1)=4. Its proof writes
c+1=lambda(n+q_t)-d, with q_t in {1,97/81}, 0<=d<=2^s-1,
and lambda=K_t*2^s/3^a, where 0<=a<=s<=L and 0<=t<=L.
The displayed K_t equals 3^t/2^t for t<=4 and 3^(t-1)/2^t
for t>=5. The existing coarse estimate lambda-1>=6^(-L) in the
lambda>1 case is the stated source of the 12^L guard. These are recalled
existing identities and proof limits, not a new bound.

L027's roots obey 12^L<n<=12^L+162*6^L<4*12^L. Its strict coefficient
hypothesis supplies positive slack. Its conclusion and audit expressly
leave coefficient equality open. The proposed improvement is not a
previously established endpoint result and does not repair an error in
L026 or L027. The endpoint is neither a duplicate of their statements nor
excluded by Attempts 014–016. Preserve those stops on constant,
initial-valuation-only and strictly subcritical clocks. No historical
counter, stop evidence or supervisor state is changed.

## Reused primary coverage

Reuse `2026-10-05-residue47-log-height-coalescence.md` and the ready
`2026-10-05-residue47-bounded-coalescence.md` and
`2026-10-05-residue47-odd-run-clock-coalescence.md` assessments. They supply
precise inspected statements and relevant proof cases; unchanged external
passages were not fetched again. The target/map statement rechecked on
2026-10-05 in the bounded assessment agrees with local foundations.

Olivier Rozier, *Parity Sequences of the 3x+1 Map on the 2-adic Integers
and Euclidean Embedding*, INTEGERS 19 (2019), A8,
[Definition 1, Lemma 1 and proof, pp. 2–3](https://math.colgate.edu/~integers/t8/t8.pdf#page=2),
provides a unique class modulo 2^j for each j-symbol parity word and the
finite affine identity. The signed-integer extension supports L026's
anchor-prefix transfer. It supplies neither a height guard nor endpoint
coalescence. The standard named Chinese Remainder Theorem applies to the
coprime moduli already used in L026; quantitative representative selection
is still mathematical work, not a separate reproof of CRT.

Sodelin's informal live-main
[B-S20-ANCESTOR-DEPTH-OBSTRUCTION-001](https://raw.githubusercontent.com/Sodelin/Collatz-Conjecture-Work/main/proof-search/lemmas/Bounded_Ancestor_Depth_Obstruction.md),
read 2026-10-05 in the ready assessment, treats bounded ancestors and a
simultaneous direct-descent obstruction. Lines 67 and 71 leave general
coalescence open. L4's guarded inverse semantics and L5's unrefined-family
scope do not supply the endpoint assertion or license pruning refined,
parameter-dependent companions. No new external ancestor theorem is
imported and no immutable revision or formalization is assumed.

Mark D. LaDue, *Clusters of Integers with Equal Total Stopping Times in
the 3x+1 Problem*,
[arXiv:1709.02979v3, 2017-11-15](https://arxiv.org/pdf/1709.02979v3#page=3),
Lemma 3.1 and Theorems 3.2/4.1, pp. 3–5, already has both actual parity
cases assessed. For odd m=2^p(2q+1)-1>1, p=v_2(m+1)>=1, q>=0,
the specified adjacent companion m-1 coalesces at p+2 exactly under the
source's same-parity criterion. This is neither a residue-20 companion
assertion nor a uniform endpoint bound on the present cylinder. It is
comparison, not a matching import.

## Stronger separation comparison

Michel Laurent, *Linear forms in two logarithms and interpolation
determinants II*, Acta Arithmetica 133.4 (2008), 325–348,
[Corollary 2, p. 328; real-case proof, pp. 345–347](https://www.impan.pl/shop/en/publication/transaction/download/product/82485#page=4),
DOI 10.4064/aa133-4-3, revised 2008-07-24, gives the following bound.
For multiplicatively independent algebraic alpha_i with alpha_i and their
chosen logarithms positive real, b_i positive integers,
Lambda=b_2 log(alpha_2)-b_1 log(alpha_1),
D=[Q(alpha_1,alpha_2):Q]/[R(alpha_1,alpha_2):R],
A_i>1 with log(A_i)>=max{h(alpha_i),abs(log(alpha_i))/D,1/D},
and b'=b_1/(D log(A_2))+b_2/(D log(A_1)),

\[
\log|\Lambda|\ge-C_2D^4
 \max\{\log b'+0.38,m/D,1\}^2\log A_1\log A_2.
\]

For example Table 1 permits (m,C_2)=(10,25.2). The proof's real case uses
positive logarithms to sharpen the height estimate and derives Table 1's
constants from Theorem 2. This is known logarithmic separation, not the
endpoint theorem. Bases 2 and 3 fit its base hypotheses; positive exponent
coefficients, conversion to lambda-1, offsets and CRT height still require
a separate application. Zero/sign cases are not covered by silently
allowing nonpositive b_i. The approved elementary reduced-denominator test
need not invoke or reprove this deeper result.

## Search and access record

Queries executed in this review:

- `Collatz coalescence "log(12)"`
- `Collatz "coalescence" "logarithmic" lower bound`
- `Collatz rational slope 2 powers 3 powers coalescence bound`
- `Collatz "coalescence" "endpoint" logarithmic`
- `Collatz "47" "243" coalescence logarithmic bound`
- `"Collatz" "coalescence" "log(12)"`
- `Collatz coalescence affine slopes Diophantine approximation lower bound`
- `"2" "3" "linear forms" "Matveev" theorem pdf`
- `Collatz powers two three lower bound linear form logarithms primary theorem`
- `Laurent linear forms two logarithms 2008 Theorem 2 pdf`
- `Matveev explicit lower bound homogeneous rational linear form logarithms algebraic numbers II 2000 theorem 2.1`

The last searches followed the separation lead to Laurent's publisher PDF;
its theorem/corollary hypotheses and real-case proof were read. A page-22
screenshot timed out, but complete relevant extracted text was retrieved,
so no essential Laurent passage remains inaccessible. Matveev snippets
and bibliographic hits were discovery only; its theorem was not inspected
or imported. This bounded search does not certify absence or originality.

The CCChallenge index was used only to locate Aleksei Novgorodtsev's
[version 4.1 record, published 2026-08-08](https://zenodo.org/records/21848913).
Its landing description concerns prescribed consecutive pairs and initial
run coordinates. The linked manuscript returned an internal retrieval
error. This remains an optional unread theorem lead; the description is
not theorem evidence and no statement is imported. Its access failure
blocks no input to the proposed independent size-guard calculation.
Burson's withdrawn numerical study and stochastic-coalescence search hits
supply no theorem for this target; reuse the prior access assessment.

No cross-notebook theorem was read. The overview and DAG remain unchanged
because this review changes no mathematical argument.

## Mathlib

Full matching endpoint residue-20 coalescence obstruction: **not checked**.
Supporting parity coding, CRT, rational slope separation and Laurent's
bound: **not checked**. Unknown availability is not absence; no Lean
check was run. Precise published parity coverage, named CRT and audited
local inputs suffice for the bounded informal attempt now approved.
