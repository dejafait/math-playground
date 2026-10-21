# Coupled two-family certificates with free pairs — source review

TARGET: Review source coverage for a coupled two-family Schrijver dual certificate with free pair variables at (1024,10,68), and specify one finite block/row support to test against floor(65537^28/2^128).
CHECKED: 2026-10-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the 2026-10-05 triple-distance assessment and foundations/04; searched the exact A(1024,10,68) string and sparse/rational Schrijver dual certificates; compared ATTEMPTS/012–018,067,068,071,079 and relevant L021–L024 statements. No inspected source supplies the finite-instance certificate; no novelty inference is made.
SOURCE_EVIDENCE: Reinspected Schrijver (2005) author manuscript III.A (53)–(58) and III.B (60)–(67), pp. 6–7; Kim–Toan arXiv:1212.3467v1 III.B (31)–(35), III.C.2 (40), printed pp. 8–10; newly read Boyd–Vandenberghe (2004), corrected 2009 printing, §5.9.1 pp. 264–266, weak-duality proof and Example 5.11; compared Coregliano et al., ITCS 2026 article 44, Theorem 3 and Corollary 27. Reused Polak v1 Proposition 1.1 coverage. Direct primary URLs: https://homepages.cwi.nl/~lex/files/codes.pdf ; https://arxiv.org/pdf/1212.3467v1 ; https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf .
COMPARISON: The sources supply standard constraints and weak duality, not the needed finite bound. The old common feasible extension passes L022's batch and L023/L024's specified diagnostics, but has not been checked on the complete coupled shells-5–8 support below. Fixed-pair/base/column stops do not cover this variable-pair objective model.
GAP: Construct the exact shared-variable model and check the old above-threshold extension on every retained row/block. A failed old assignment leaves a global dual or a different feasible lift to be found; it gives no upper bound. The new relaxation value is unknown.
REASON: The changed free-pair/global-objective scope requires a specified finite support and exact certificate normalization; inspected standard inputs now cover these, without a new lemma, mathematical script or solve.
SCOPE: Only the finite support below at n=1024,w=68,v=956,d=10, all original pair variables free; first perform its old-witness precheck within 20000 orbit variables and 200000 scalar/pair rows. No optimization, full-scale SDP, retuning, RS determinant zeros or stopped conic restart is authorized by this first test.
LITERATURE_REASON: The changed free-pair objective and previously unassessed coupled support require coverage beyond the reusable selected-batch assessment; weak-duality normalization is an essential additional source input.

The main gap is arbitrary-center safety at 68 agreements. The intermediate
target is one bounded global objective certificate with pairs free. Its
possible downstream use is L001/L021's existing support transfer, uniform
in tuple width m. The bracket stays 955–957. Independent unresolved steps
include 67 agreements, RS realization, stronger labeled restrictions and
the qualified ABF/ArkLib comparison. This is source/specification progress
only, with no progress beyond the known methods checked.

## Inspected inputs and applicability

A. Schrijver, *New code upper bounds from the Terwilliger algebra and
semidefinite programming*, IEEE TIT 51 (2005), 2859–2866,
DOI 10.1109/TIT.2005.851748,
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
III.A (53)–(58), manuscript p. 6, and III.B (60)–(67), p. 7.
Read the tensor restriction and positive diagonal rescaling, two anchor
averages, normalization, scalar proof, repeated words and objective.
The full formulas are canonical in
[foundations/04](../../foundations/04-constant-weight-triple-sdp-source.md).

H. K. Kim and P. T. Toan,
[arXiv:1212.3467v1](https://arxiv.org/pdf/1212.3467v1),
14 December 2012, III.B (31)–(35), printed pp. 8–9, and III.C.2 (40),
p. 10: read the zero-multinomial convention, both independently restated
PSD families, scalar identities and distance-count normalization. No
strengthened four-block or conditional-shell row is imported here.

The code hypotheses are nonempty binary constant weight, even d and
d<2w<=n; here 10<136<=1024 and v=956. L021 already proves the support
selection for entire tuples with extra agreements allowed. Empty lists
satisfy an upper bound automatically; no reproof, scalar projection or
exponent m is needed. Use both affine source matrices with shared orbit
variables. Keep the suspect printed (61) complement-prefactor qualification:
use explicit (64), corroborated by Kim–Toan (32)–(33), not that prefactor.
Changing pairs invalidates inherited fixed-pair Schur inverses/kernel
ranks; construct the original affine blocks directly.

S. Boyd and L. Vandenberghe, *Convex Optimization*, Cambridge (2004),
author PDF seventh printing with corrections (2009),
[§5.9.1, pp. 264–266](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf),
weak-duality proof and Example 5.11: read the dual-cone sign argument,
PSD self-duality and coefficient cancellation. This supplies the trace
certificate rule recorded in foundations/04. Neither strict feasibility,
strong duality, attainment nor a rational optimum is assumed.

## One finite block and row support

This is a chosen test prescription, not a theorem that it improves a bound.
Keep all p_i, 0<=i<=68, and one y variable per touched actual source orbit.
Write W_k={k,...,68-k}, V_l={l,...,956-l}. Retain **both** source PSD
families on the following principal index sets:

1. For every ordered (k,l) in {0,...,8}², use
   I_(k,l)={5,6,7,8} intersect W_k intersect V_l.
2. At (0,0), use {0,5,6,7,8,68}, replacing its smaller item-1 matrix.
3. Retain L022's (33,33) block on {33,34,35} and (34,34) on {34}.

These are principal restrictions of the cited blocks. The two beta labels
are distinct; do not identify (k,l) with (l,k) or delete rows of a zero-label
matrix to construct a different label. This does not specify the full SDP.

Retain all 68 basic pair-LP rows from L021 with
 a_i=binom(68,i)binom(956,i)p_i, all p_i>=0, p_0=1 and p_1=...=p_4=0.
Seed the touched set with all pair orbits (i,0,0,0), 0<=i<=68, and all
admissible orbits in the selected entry sums, then take full source
permutation closure. On this entire actual-orbit set retain
y>=0, p_i-y>=0, 1+y-p_i-p_j>=0, all source equalities preserving t-s,
Boolean/repeated-word identifications and distance zeros if any of
 i,j,h=i+j-t-s is 1,...,4. Include every original p_h appearing in a
complement entry. Impossible orbits are absent; omitted triples are not
set zero. Shared entries use the full source orbit, not distances alone.
Every pair remains free except the stated normalization/distance zeros.

Construction caps, not computed counts: 20000 retained orbit variables
including pairs and 200000 scalar/pair rows after source equality reduction.
Save actual counts. Exceedance parks this prescription as a resource
limitation, without increasing the caps or dropping required rows.

## Exact certificate and first discriminating test

Use M(p)=sum_i binom(68,i)binom(956,i)p_i, including p_0=1, and
K=floor(65537^28/2^128). An exact upper certificate U is sufficient when
floor(U)<=K, equivalently U<K+1; U<=K is a stronger sufficient condition.
An above-K feasible relaxation objective blocks every sufficient
certificate only when it is at least K+1, so retain the integer test.

The cited weak-duality certificate contract, after substituting fixed
values and reducing source equalities, is an affine identity

    U - M(p) = sum_r lambda_r g_r(p,y)
               + sum_(b,family) trace(Z_(b,family) A_(b,family)(p,y)),

where g_r>=0 are exactly retained scalar/pair rows, rational lambda_r>=0,
and rational Z are PSD. Uneliminated equalities allow arbitrary signed
multipliers times their zero residuals. Match the constant and **every**
free pair/orbit coefficient. The symmetric trace counts off-diagonal
contributions twice. Record and transport any positive diagonal scaling.
PSD evidence requires full rational congruence/LDL identities, including
zero residual rows at singular pivots. Numerical signs, solver status and
near cancellation do not suffice. This imports a standard certificate
rule; it is not a derived finite-instance certificate.

The first calculation constructs this one shared-variable model and
evaluates L022/L023's unchanged full extension on it, without retuning or
optimization. Reconstruct every retained coefficient, row and matrix.
If the assignment passes, certify all PSD blocks exactly; L022's existing
floor(M)>65537^28/2^128 then stops this whole finite batch without a solve.
If it fails, save an exact failed scalar row or full matrix with a
rational negative vector. This rejects only that assignment and preserves
the model for a future separately approved free-pair certificate attempt.
It gives no upper bound or infeasibility claim. Unverified signs remain
inconclusive. This first coupled precheck is finite and independently
testable; no new calculation was performed in this literature turn.

## Recorded overlap and stops

L022's stopped batch is contained here, but its witness does not come with
a proof for the newly added shell modes/cross entries. L023/L024 and the
full scalar audit pass on the same extension; their union alone would
already be stopped. The added support must be checked as one batch, not
used to justify restarting a sequence of isolated block diagnostics.
No canonical result read establishes a common pass for this whole support.

ATTEMPTS/016–018 concern different weakened four-block/conditional rows.
ATTEMPTS/067,068,071 concern fixed ancestral pairs/base/columns and capped
solves; ATTEMPTS/079 excludes four frozen vectors. Preserve every stop.
The changed objective model has no such fixed prescription, rank or face
assumption. L053–L096 are historical comparison evidence, not mathematical
inputs of the new model. No stopped solve, hull enlargement, ancestor
contract or labeled symmetry is imported.

## Search, stronger results and qualifications

Reuse the 2026-10-05 assessment of Polak,
[arXiv:1703.05171v1](https://arxiv.org/pdf/1703.05171v1), Proposition 1.1
and proof, for stronger four-word A_4/B_4 bounds. No four-word block
formula or target-instance value is imported; later details remain unread
leads outside this triple-only test.

A new relevant lead was checked at theorem level: L. N. Coregliano,
F. G. Jeronimo, C. Jones, N. Linial and E. Loyfer,
[*Higher-Order Delsarte Dual LPs: Lifting, Constructions and Completeness*](https://drops.dagstuhl.de/storage/00lipics/lipics-vol362-itcs2026/html/LIPIcs.ITCS.2026.44/LIPIcs.ITCS.2026.44.html),
ITCS 2026 article 44, DOI 10.4230/LIPIcs.ITCS.2026.44.
Read the introductory Theorems 1 and 3 and full Corollary 27 statement.
The explicit rate construction concerns balanced linear binary codes,
sufficiently large n and asymptotic errors; the inspected lift retains the
starting objective. These do not supply the finite bound for generally
nonlinear selected support families. Its proof and formal lifting
Theorem 15 remain unread and are not imported. No failure of all higher
hierarchies is inferred.

Queries: `"A(1024,10,68)"`, `"A(1024,10,68)" Schrijver`,
`"1024" "68" "constant weight" semidefinite bound`,
`constant weight Schrijver semidefinite dual certificates selected blocks large parameters`,
`Schrijver constant weight codes sparse dual semidefinite certificates rational`.
Returned primary coding sources and stronger comparisons supplied no
matching finite certificate. Unrelated quantum/WSOS results were not used.
This is bounded coverage, not an exhaustive search or novelty claim.
Primary PDFs were readable in the web reader; no local snapshot or
checksum is claimed. Full matching Mathlib coverage: not checked.

Future finite specialization is REPRODUCTION. No new lemma, mathematical
script, witness evaluation or solve occurred. The companion assessment
binds the exact proposed first calculation; the supervisor handles its
separate approval. The argument, DAG, historical stops and 955–957 bracket
are unchanged.
