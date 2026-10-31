# Analytic fixed-cutoff alternative for the parked square test

TARGET: Review whether L317's analytic fixed-cutoff approximate functional equation supplies the missing low-order and moving-endpoint coverage for the parked G_T square-surrogate defect test.
CHECKED: 2026-10-29
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Read L317 completely, its recorded AFE/Stirling foundations, L316 normalization, L471 hypotheses and gauge identity, L465 Section 5, the blocked square assessment and the differentiated-AFE failure. New exact-square, absolute-mean, analytic-Cauchy and stronger-result queries are recorded below; no inspected matching defect theorem was located and no novelty is inferred.
SOURCE_EVIDENCE: Reuse the inspected Hardy--Littlewood AFE recorded in foundations/notation-and-inputs.md: Titchmarsh--Heath-Brown (1986), Theorem 4.15/(4.12.4), printed pp. 79, 81--84; its new PDF body retrieval timed out, so no fresh primary reinspection is claimed. L317 supplies the complete local analytic specialization through order four. DLMF 5.11.1/Section 5.11(ii), Bui--Hall arXiv:2304.05178v1 (1) and Montgomery--Vaughan (1974), Theorem 2/Corollaries 2--3, were consulted with the extraction qualifications below.
COMPARISON: The existing analytic specialization covers ordinary orders zero through two, the identical Hardy phase and all local cutoff transitions. It does not freeze the balanced length across [T,2T]. The dyadic replacement is a separate finite-sum endpoint calculation using retained entering terms, elementary integration by parts and the recorded finite Hilbert inequality; neither its cost nor the absolute residual is asserted.
GAP: No missing differentiated-Riemann--Siegel source is essential for a bounded attempt using L317 as its established local input. The dyadic endpoint cost, theta'-to-lambda replacement, square normalization and phase-sensitive absolute defect remain mathematical obligations for a separately approved research scope; full matching Mathlib coverage is unchecked.
REASON: Complete this one alternative source review and nominate the unchanged square-defect test with explicit endpoint obligations. This is source-readiness progress only, not a saving, lower bound, new lemma or independent reproof/audit of L317.
LITERATURE_REASON: Changed source mechanism: analytic fixed-cutoff AFE plus Cauchy, instead of the inaccessible low-order Riemann--Siegel derivative theorems. Its applicability and dyadic endpoint coverage are essential and unreviewed.
SCOPE: Source review only; L317's analytic remainder, L316 definitions only where needed, L471's exact A and W, L465's gamma gauge, and the unchanged G_T from the parked square assessment. No RH, simplicity, spacing, external half-plane estimate or new positivity premise.

## Exact prospective mathematical question

The main gap is actual-Xi initial signs at unbounded heights and global
mixed positivity. Preserve the square candidate already specified in
`2026-10-29-riemann-siegel-square-surrogate-coverage.md`:

    W(t)=D_1(Xi;t)/A(t)^2,
    M_T=floor(sqrt(T/(2pi))), lambda(t)=(1/2)log(t/(2pi)),
    P_(1,T)(t)=sum_(1<=n<=M_T) (lambda(t)-log n)n^(-1/2-it),
    G_T(t)=4|P_(1,T)(t)|^2,
    E(T)=integral_T^(2T) |W(t)-G_T(t)| dt.

These definitions are unchanged; no approximation assertion follows.
The intermediate source target asks whether an accessible, already
recorded analytic remainder can justify a bounded arithmetic test of
E(T)=o(T(log T)^3). Success of that eventual test could imply a mean
first-sign saving; individual signs, higher signs and RH would remain
unresolved. A rigorous positive full-scale lower bound on E along an
unbounded sequence would instead stop this particular surrogate.

## Narrow source comparison and decision test

Read L317's hypotheses and its analytic-remainder proof first, then only
the L316 normalization and source-foundation passages it actually uses.
The old level-ordering form, its fourth derivative, and its exponential
sum/diagonal-dominance conclusions are not proposed inputs. Retain their
failed dominance evidence; importing a derivative estimate would not
revive the stopped sign argument.

Check the precise Hardy--Littlewood AFE hypotheses, complex neighborhood,
pointwise auxiliary cutoff, analytic fixed-cutoff function, endpoint
correction and Cauchy radius. Resolve whether constants are uniform in
height and through cutoff transitions. Compare L317's phase/gauge with
L471's Hardy Z and exact completion curvature. Separately determine
what is already covered for replacing the local length by M_T over a
dyadic interval; do not assume that replacement is harmless. A remaining
finite-sum endpoint calculation may be nominated only with its source
inputs and bounded threshold made explicit, for a later research turn.

Reuse adequate inspected primary coverage, and retrieve only genuinely
missing theorem hypotheses/proof cases. This is not authorization to
repeat the inaccessible Blanc/Karatsuba/Korolev downloads. Search the
exact alternate application and stronger known defect estimates before
approving it; no novelty follows from the local omission identified here.
No derivation, new lemma or mathematical script belongs to this review.

Continue only if the analytic AFE route supplies adequate essential
coverage for a concrete residual test, with the dyadic endpoint issue
resolved or explicitly source-covered as a later calculation. Otherwise
park this alternate implementation with the precise remaining obstacle;
do not repeat generic source readiness or an already completed audit.
No existing ready assessment is claimed for this changed mechanism.

If coverage becomes adequate, the exact arithmetic absolute-defect test
is a potential proof_attempt/creative continuation: the obstruction is
the unproved absolute residual between W and a positive arithmetic
square at scale T(log T)^3, and the decisive alternatives are little-o
or a rigorous positive full-scale lower bound. That continuation must
be approved separately; no creative proof attempt is executed now.
Full matching Mathlib coverage remains unchecked. No cross-notebook
mathematical input is proposed.

## Completed source comparison

The preceding paragraphs preserve the nomination and its tests. This
section records the completed review. No mathematical defect estimate
has been attempted. Outcome EXPLORATION concerns a new source comparison;
it neither repeats the old access-block decision nor proves an obstruction.

### Existing input and applicability

The precise unconditional AFE already checked in the foundations has
s=sigma+it, t>0, 2pi xy=t, x,y bounded below and sigma in a fixed closed
subinterval of (0,1). Its two errors are O(x^(-sigma)) and
O(t^(1/2-sigma)y^(sigma-1)). That recorded source coverage is reused,
not replaced by a search snippet. The Rutgers PDF initially returned
its bibliographic header; subsequent body and screenshot requests
failed. No fresh inspection of its endpoint proof is claimed. This
does not erase the earlier inspected coverage or canonical L317.

L317's proof, read completely, bounds an already holomorphic difference
with the balanced first cutoff fixed on a disk of radius 1/log a.
The auxiliary second cutoff is used pointwise only. The proof retains
its possible single entering/leaving term even at integer cutoffs,
then applies Cauchy. Its conclusion (1) includes ordinary j=0,1,2
and all sufficiently large real centers. No high-order-only derivative
theorem or differentiation of a real error is needed. This review
uses that existing conclusion; it is not a new independent proof audit.

L316's H and theta have the same displayed definitions as L471's A
and Hardy phase. L471 (7) is therefore the applicable zero-safe
identity for W, including -(log A)'' Z^2. L465 Section 5 supplies
the retained curvature bound. L316 (7) and L317 (7) record the phase
expansion needed to compare theta' with the candidate lambda. The
comparison error in the quadratic dyadic application must still be
estimated; equality of these two frequencies is not an input.

The derivative statement is local in its frozen length. Applying it
at each t does NOT give a formula with length M_T throughout [T,2T].
The future calculation must keep all indices between M_T and the
balanced length floor(sqrt(t/(2pi))), for each of the three jets.
There are finitely many transition heights 2pi k^2 on each dyadic
interval. Splitting finite integrals there, retaining boundary terms,
and using the fundamental theorem of calculus/integration by parts
requires no further differentiated-zeta source. This is the concrete
endpoint calculation being nominated, not a bound proved by this review.
No global holomorphic remainder with cutoff M_T is claimed.

### Additional primary checks and limits

Consulted [DLMF 5.11.1 and Section 5.11(ii)](https://dlmf.nist.gov/5.11):
logarithmic Stirling has sector qualifications and complex remainder
bounds. Reuse the canonical analytic/Cauchy implementation rather than
differentiate a real asymptotic. No gamma estimate supplies positivity.

Read [Bui--Hall v1, (1), Introduction](https://arxiv.org/html/2304.05178v1),
11 April 2023: the mixed second moments concern fixed ordinary derivative
orders. They can check signed normalization and jet norms. They do not
estimate the L1 distance to G_T. The theorem/proof comparisons in the
blocked square assessment remain adequate for Blanc, Ivic and paper 41
v4; their scope has not changed. No inaccessible derivative source was
retried and no newer paper-41 search excerpt is imported.

Consulted [Montgomery--Vaughan, *Hilbert's inequality*, JLMS (2) 8
(1974), 73--82, Theorem 2 and Corollaries 2--3, pp. 74--75](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf).
Its distinct-frequency hypotheses and finite/infinite qualifications
were readable, but PDF extraction lost the displayed inequalities and
screenshots supplied no usable image. Thus no new exact constant or
formula is certified from that extraction. Use the already recorded
finite generalized Hilbert inequality in the foundations if needed;
the endpoint calculation can also expand finite sums and integrate
each nonzero frequency directly. A mean-value theorem for a polynomial
with fixed coefficients cannot silently cover pair-dependent endpoints.

### Search and overlap record

Queries on 29 October 2026 included:

- "Hardy" "Z" "approximate functional equation" "Cauchy" derivatives;
- "Laguerre" "4" "Dirichlet polynomial" "zeta";
- "Z'(t)" "Z(t)Z" "Dirichlet" Laguerre;
- "Hardy" "Laguerre" "absolute" "mean";
- "Hardy" "Laguerre" "square" zeta absolute mean defect;
- "Z" "square" "absolute" "Riemann-Siegel" defect;
- Montgomery Vaughan Hilbert inequality 1974 pdf Corollary 2.

No inspected exact absolute-defect theorem was located. Das--Pujahari,
*Mean of the product of derivatives of Hardy's Z-function with Dirichlet
polynomial*, JNT 258 (2024), 334--367, DOI
[10.1016/j.jnt.2023.11.001](https://doi.org/10.1016/j.jnt.2023.11.001),
is an unread full-theorem lead: the publisher introduction describes
signed twisted moments, not this L1 residual. It is not an essential
input to the nominated finite-sum test. Search snippets, secondary
theses and an unrelated claimed RH disproof are not theorem evidence.
Failure to locate a match is not evidence of originality.

L317's failed level-ordering absolute/third-derivative dominance budget
is preserved in ATTEMPTS/2026-09-24-differentiated-afe-ordering-test.md.
It concerns a fourth-order polynomial and a pointwise diagonal surplus;
the contemplated test retains arithmetic phases at first order and
asks for a dyadic absolute norm. That distinction permits a test, not
a prediction of success. The blocked square assessment's moment-law,
pair-quotient, band-cost and Selberg source failures also remain in force.

### Decision and bounded continuation

The local derivative-source obstacle is bypassed by an existing input,
not by recovering the inaccessible low-order papers. Essential source
coverage is adequate to nominate one bounded mathematical attempt on
the original G_T and E(T), with the finite endpoint calculation inside
its scope. The separately saved continuation assessment is
`2026-10-29-fixed-cutoff-square-defect-test.md`; its new scope requires
the supervisor's separate approval next turn before mathematics.

The discriminant stays E(T)=o(T(log T)^3), or a rigorous positive
full-scale lower bound along an unbounded sequence. Signed mean agreement,
a large upper envelope, a finite numerical sample or a failed inequality
would establish neither alternative. If the endpoint transfer itself
cannot be bounded adequately, preserve that exact obstruction and park
this implementation. Individual-height/higher signs, global mixed
positivity and RH remain unresolved even if the mean saving succeeds.
No lemma, mathematical script, DAG or PROOF.md has changed.
