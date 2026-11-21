# Source comparison: the paid inner spatial rational-response norm

TARGET: Test whether V_(1/32) >= c*n*exp(-n/48)*sqrt(D) holds uniformly for L666's independently displaced unit-residue family, where V_r=max_(|u|=|zeta|=1)|R^(-1) sum_a W_a(u)/(1-r*a*zeta/R)|, with an absolute c>0 and onset.
CHECKED: 2026-11-03
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 80 reused the full-spatial-root, signed-angular-sampling and highest-moment assessments; compared the exact L649/L650/L666/L669/L670/L671/L682 stops; and ran seven bounded searches on Cauchy/resolvent norms, residues, rational Turan inequalities and Cauchy-matrix conditioning. No inspected result matches TARGET; queries and reading limits are below, without a novelty inference.
SOURCE_EVIDENCE: Reuse Danchenko--Semin arXiv:1503.06476v1 Theorem 2 pp.1--2/proof pp.6--7, Baranov--Zarouf arXiv:1310.1182v1 Theorem 2.4 p.5/Section 4.4 Step 1 pp.12--13, Moitra v4 Theorems 2.2--2.3 pp.5--7, Biro's p.344 theorem and Brunault--Zudilin Propositions 1.4--1.5 pp.6--7 from the named ready assessments. New reading: Beckermann--Townsend arXiv:1609.09494v1 Theorem 2.1/complete proof pp.4--5 and Section 4.2/Corollary 4.2 pp.11--13; screened Scheidereiter--Faure arXiv:1907.05949v1 Section 1 p.1 only for class mismatch. L683's conditional transfer remains unaudited.
COMPARISON: Quadrature and rational norm comparisons concern the combined response, without a lower bound against original D. Power-sum and separated-exponential results do not remove W_a or pay the small-radius observation loss. The new Cauchy-matrix theorem gives upper singular-value bounds, not the required coercivity. L649's ambient inverse stop, L650's individual-dual failure and L682's highest-moment countersequence do not decide this joint small-circle norm. The parked c_0 flow is not reopened.
GAP: Establish the exact uniform joint norm estimate or an admissible normalized countersequence, retaining the original residues/D and one displacement vector at every angle. The sources supply neither the rate 1/48 with absolute c/onset nor a countersequence. H/support and actual-Xi realization/signs remain independent; failure of this sufficient norm condition need not stop H.
REASON: Changed-scope comparison now supplies essential source coverage for one bounded exact-target attempt, subject to separate supervisor approval next turn. No theorem import settles TARGET and no lower bound, countersequence, new lemma or mathematical script was produced in this literature-only step.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED isolated a new observation geometry and paid exponent after L683; this review compares that exact target using ready coverage and a narrow Cauchy-matrix lead, rather than repeating browsing of an approved target.
SCOPE: Exactly TARGET for L666's n=12q+3, q>=1, M=n/3, x=-5/4, R=11/8, independent real |e_m|<=1/8 and original unit residues; full B_u including j=0 and angle 1/u, original D and r=1/32, with the same displacement vector for both suprema. One bounded proof or countersequence test may use the cited observation/root tools with all remaining costs explicit. No generic coefficient coercivity, root separation, positive cross terms, fixed-angle replacement, scalar-energy closure or H/support/Xi bridge is assumed.

## Invocation-start nomination and possible use (historical)

The main gap remains actual-Xi all-degree mixed positivity. L683's
conditional transfer gives the original full-H threshold if this exact
norm estimate holds: on r=1/32 the complete-root cost is at most n/96
and the absolute geometric tail is at most
n*exp(-7n/12)*sqrt(D). The required main norm has exponent 1/48,
and 1/48+1/96=1/32. Its asserted lower bound is entirely unresolved.
The same displacement vector must serve all u and spatial angles.
The original residues and D are unchanged. No scalar c_0 energy bound,
positive surrogate or infinite-dimensional ambient minimizer is assumed.

Essential continuation inputs are L666's exact G,D and admissibility,
L683's qualified conditional transfer, and L658 with L657's nonzero-
slice/integrability qualifications. L683 imports the existing rational
quadrature specialization; its audit status is not upgraded here.
The L649/L650 and L669/L670/L671/L682 stops are comparisons, not
coercivity premises. The scalar signed-flow route remains parked.

The next review should reuse the ready primary readings in
`2026-11-03-full-spatial-root-contribution.md` and
`2026-11-02-displaced-signed-angular-sampling.md` before retrieving
anything new. Compare the exact lower-bound hypotheses and scale,
including the difference between a norm of the combined response and
the original separate-term diagonal. Resolve whether an existing
result covers the new observation geometry or whether the remaining
family-specific gap warrants a bounded attempt. Do not reprove the
root formula, repeat an endpoint certificate, or infer novelty from
an unsuccessful search.

A subsequent approved mathematical test must either establish the
displayed bound with absolute constants/onset, isolate a useful input
with every remaining loss charged, or give the normalized countersequence
above. Failing this sufficient condition would not disprove the original
full-H inequality. H/support, Xi realization and actual signs remain
independent. Full matching Mathlib coverage is unchecked; the supporting
root-formula names in L683 do not supply the required norm comparison.

At nomination this file was REVIEW_REQUIRED throughout step 79. The
completed comparison below changes the source decision in step 80;
it does not change or retroactively reject the completed L683 work.

## Completed comparison — step 80, 3 November 2026

### Exact gap, use and local overlap

The main gap is actual-Xi all-degree mixed positivity and signs at
unbounded height. The intermediate target is exactly TARGET, not
generic rational sampling. L683 states its conditional downstream use:
the complete spatial-root cost at r=1/32 is at most n/96 and the
geometric tail is at most n*exp(-7n/12)*sqrt(D). Its asserted
implication gives L658's sufficient H threshold, including +log n.
This review imports neither a coercivity premise nor a fresh proof of
that unaudited implication. L657's nonzero-slice and integrability
qualifications, and L658's localization, remain essential.

Read the exact L666 and L683 definitions and conclusions, L649's
complete-response identity and ambient coisometry argument, L650's
individual-dual and joint-dual qualifications, and the relevant stop
statements in L669/L670/L671/L682. Also read L666's recorded second
inconclusive scalar-flow closure. The following scope comparisons
do not extend these results beyond their established hypotheses:

- L649 concerns the same full moment response on the spatial boundary,
  but its stopping result is about information recovered by an ambient
  inverse. It expressly does not realize the ambient minimizer in this
  family. It therefore supplies neither a lower bound nor a family
  counterexample for the present small spatial circle.
- L650 excludes selecting and normalizing individual pole-isolating
  duals in a broader family with an exponentially close pair. Its own
  joint combination has a much better response. That example is not
  the L666 displaced lattice. No arbitrary close-pole obstruction is
  imported into this separated family or its joint supremum.
- L669's fixed-angle loss grows faster than any fixed multiple of
  log n, with K-dependent constants/onsets. It gives no uniform
  linear-rate failure of this joint maximum. L670/L671 exclude their
  specified clearing certificates, not the response itself.
- L682's audited zero-shift countersequence concerns only the highest
  prescribed moment. It does not upper-bound the complete resolvent.
  The recorded scalar-flow failure is an insufficient relative
  derivative bound; repeating its absolute subtraction is not a new
  test here. The new test must use the joint spatial response and
  account for its small-radius cost against the original D.

These are duplicate and failure checks, not a mathematical audit of
the unaudited statements or a new proof of their conclusions. No
certificates or mathematical scripts were run.

### Reused primary theorem scope

Reuse the full primary reading records in
`2026-11-03-full-spatial-root-contribution.md`,
`2026-11-02-displaced-signed-angular-sampling.md` and
`2026-11-02-displaced-highest-spatial-moment.md`.

**Rational observation.** V. I. Danchenko and L. A. Semin,
[*Sharp quadrature formulas and Nikol'skii type inequalities for
rational functions*, arXiv:1503.06476v1](https://arxiv.org/pdf/1503.06476v1),
22 March 2015, Theorem 2 pp.1--2, complete proof pp.6--7. The finite
interior pole set includes zero, with its reflected completion;
ordinary pole orders are at most s and the combined order at zero
and infinity at most 2s-1. L666's s=1 angular census and normalized
weights are already recorded. At each fixed spatial argument the
coefficients multiplying W_a are angular constants, so the same
pole-order scope is relevant; no new quadrature identity is derived
here. Observing a signed rational function exactly does not bound it
below by its separate-term diagonal. Theorem 1's underlying source
proof retains the saved unaudited qualification.

**Norm conversion.** A. Baranov and R. Zarouf,
[*A model space approach to some classical inequalities for rational
functions*, arXiv:1310.1182v1](https://arxiv.org/pdf/1310.1182v1),
4 October 2013, Theorem 2.4 p.5, Section 4.4 Step 1 pp.12--13.
For rational f of bounded degree with no poles in rho<=|z|<=1/rho,
0<rho<1, and 1<=p<s<=infinity, its inequality compares ||f||_s
from above to ||f||_p with explicit degree and clearance factors.
The saved p=2,s=infinity proof covers both pole sides, with earlier
representation lemmas cited rather than independently audited.
This compares norms of the combined function, not D. Neither the
norm direction nor clearance alone supplies TARGET. No application
to a rescaled spatial variable is asserted without its pole census.

**Power sums and finite samples.** A. Biro,
*An improved estimate in a power sum problem of Turan*, Indag. Math.
11(3) (2000), 343--358,
[unnumbered Theorem p.344](https://users.renyi.hu/~biroand/pdfs/Turan1.pdf),
gives max_(1<=j<=N)|sum_k z_k^j|>q_*>1/2 for N complex nodes
with z_1=1, allowing repetitions. Its unit amplitudes are not W_a(u).
The ready Friedland--Yomdin v3 Theorems 1.1--1.2 comparison concerns
exponential norm propagation, not this rational-to-D comparison.
A. Moitra,
[arXiv:1408.1681v4](https://arxiv.org/pdf/1408.1681v4),
29 April 2015, Theorems 2.2--2.3 and proof pp.5--7, requires separated
unit-circle exponential nodes and more than 1+Delta^(-1) samples
for a positive lower frame constant. Vertical spacing of a is not
that frequency hypothesis; no exact exponential transfer with a paid
error is known here. None of these readings proves the r=1/32 norm
bound for the original complex amplitudes. The saved Negreanu--Zuazua
indexing issue remains unused and is not an essential source blocker.

**Downstream roots.** F. Brunault and W. Zudilin,
*Many Variations of Mahler Measures*, ISBN 9781108794459,
[Propositions 1.4--1.5 pp.6--7](https://assets.cambridge.org/97811087/94459/excerpt/9781108794459_excerpt.pdf),
cover actual degree, leading factor, multiplicities and all root
moduli, including boundary roots. The saved complete reading is reused.
L683 already specializes this formula; there is no reason to reprove
it. It does not provide a lower bound for V_r against D.

### Newly inspected leads and reading limits

B. Beckermann and A. Townsend,
[*On the singular values of matrices with displacement structure*,
arXiv:1609.09494v1](https://arxiv.org/pdf/1609.09494v1),
29 September 2016, Theorem 2.1 and complete proof pp.4--5:
for normal A,B, an m-by-N matrix X, m>=N, satisfying
AX-XB=MN* with displacement rank at most nu, and disjoint closed
spectral enclosure sets E,F, the theorem bounds
sigma_(j+nu*k)(X)<=Z_k(E,F)*sigma_j(X), 1<=j+nu*k<=N.
Read the rank construction and spectral-norm conclusion. Section 4.2,
Corollary 4.2/proof pp.11--13 treats weighted Cauchy matrices on
disjoint real intervals. These are upper singular-value estimates.
They supply no lower frame bound or structured coefficient estimate
for W_a(u), and are not applied to this family. No matrix minimizer
is asserted admissible. Section 3's auxiliary Zolotarev estimates
were not audited; no numerical constant from them is used.

G. D. Scheidereiter and O. R. Faure,
[*On the residues vectors of a rational class of complex functions*,
arXiv:1907.05949v1](https://arxiv.org/pdf/1907.05949v1),
10 July 2019, Section 1 p.1, was screened only for source scope.
Its class is 1/(1-sum_(j=1)^N alpha_j*z^j), with real alpha_j,
sum |alpha_j|<1 and simple exterior poles. This is not an assessed
representation of our combined resolvent. Its advertised residue
norm conclusion is not a lower bound on the function relative to
the original D. Later proofs are unread and no theorem is imported.

### Bounded search and access record

Queries on 3 November 2026:

- `"Cauchy" "rational functions" "lower bound" norm residues`
- `"rational functions" "Turán" "sum" residues norm`
- `"Cauchy matrix" "smallest singular value" separated nodes circle`
- `"Cauchy transform" "positive residues" "Blaschke" norm`
- `Cauchy matrix singular values separated sets Beckermann Townsend theorem Zolotarev arxiv`
- `"rational functions" "residues" "lower" "norm" Blaschke`
- `"sum" "Cauchy kernels" "lower" "norm" Riesz`

The rational-approximation hit Baratchart--Chevillard--Qian was already
used for projection conventions in L649/L650; its approximation-error
abstract is not a new coercivity input. Other snippets, aggregator
results and abstracts were discovery aids only. No novelty follows
from the lack of a matching result. The Beckermann--Townsend author
URL and nonexistent v2 returned 404; the NSF mirror returned 502.
The primary arXiv PDF succeeded and identifies itself as v1, so these
optional access failures do not block the comparison. No repeated
source-recovery turn or API access is needed.

### Bounded continuation decision

EXPLORE is justified for exactly TARGET, after separate approval of
this changed assessment next turn. Continue only with the uniform
displayed rate and absolute c/onset, a useful intermediate estimate
that charges every remaining loss, or an admissible sequence with
V_(1/32)/[n*exp(-n/48)*sqrt(D)] tending to zero. A small finite-n
ratio, generic ill-conditioning, c_0 nonvanishing, or a worse-rate
certificate settles none of these. Failure stops this sufficient
L683 transfer, not full H or RH. Any claimed use of L683 in an RH
assembly still needs its later critical audit and the independent
H/support and realization bridges.

No new family-specific result is derived or approved in this source
review. Full matching Mathlib coverage of TARGET, Cauchy coercivity
or rational quadrature is unchecked. Reuse the saved supporting
Mahler/Fourier names without treating them as TARGET coverage.
This changed assessment does not reset mathematical exploration or
recovery counts and does not reopen the parked scalar mechanism.
