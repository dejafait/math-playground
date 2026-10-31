# Finite vertical-side measure certificate: source comparison

TARGET: Review whether finite nonnegative measures on the vertical sides of L504's rectangle can make Q_a plus the side integral have full-space M norm O_R(a), uniformly for large T.
CHECKED: 2026-10-30
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed the bounded weighted-Paley--Wiener, positive-boundary-measure and positive-Laplace/cosh searches recorded below; searched the scoped L504--L507 continuations/failure records for arbitrary-measure and common-witness coverage. No matching theorem or recorded every-vertical-measure obstruction identified; no novelty inference.
SOURCE_EVIDENCE: Reused the parent evaluations/positive-Poisson comparisons; retrieved Brevig et al. arXiv:2210.13922v2 Corollary 3.9, Theorem 3.10 and the complete p=1 paragraph/proof, pp. 14--15; Goberna--Volle arXiv:2106.14573v1 Proposition 3.2 and proof, pp. 7--8; inspected Instanes, DOI 10.1007/s00365-026-09777-0, Section 1 definitions and Theorems 1.1--1.3 (published 1 September 2026).
COMPARISON: The inspected theorems give unweighted point-evaluation estimates or qualified general convex duality, not this moving signed-functional norm. L504/L505 have different positive supports and their displayed witness-error bounds reach only b/2b, not B; no universal side-trace sign is recorded. L507's global-majorant obstruction supplies no finite-measure norm comparison.
GAP: The exact infimum remains undecided: an O_R(a) certificate at every large T or a lower bound divergent relative to a uniformly over every finite nonnegative measure. No optimizer, mass bound, strong duality, side-witness extension or H_a counterexample is established.
REASON: Essential comparison is adequate for one elementary finite-frequency/positive-measure norm test with genuine smooth Fourier witnesses, without importing an optimization theorem. This literature-only step provides coverage and an actionable test, not a mathematical advance, obstruction or originality claim. A separately saved ready continuation requires the supervisor's separate approval next turn.
SCOPE: The stated vertical-side family only; no horizontal/general-rectangle measure optimization, H_a realization, L503 audit, global-majorant retest, actual-Xi estimate or RH claim. Matching Mathlib coverage is unchecked.
LITERATURE_REASON: The next target changes from global harmonic-majorant nonexistence to a finite boundary-measure norm optimization with unrestricted vertical distribution; its essential theorem-level comparison is not covered by the reused SPECIALIZE assessment.

## Exact proposed scope and bounded decision

Fix R>0 and retain L504's V_R, H_a, a,b,B, lambda, Q_a and M.
For sufficiently large T, let nu be any finite nonnegative Borel
measure on [b,B], chosen independently of f but allowed to depend on
R,T. The proposed functional to assess is

    J_{a,nu}(f)=Q_a(f)
       +integral_[b,B] [Re f(a+iy)+Re f(-a+iy)] dnu(y),
    ||J_{a,nu}||_M=sup_{0!=f in V_R}|J_{a,nu}(f)|/M(f).

The target threshold is

    inf_{finite nu>=0 on [b,B]} ||J_{a,nu}||_M <= C_R a

for all sufficiently large real T, with C_R independent of T. Atomic
and singular measures are included. No uniform mass bound, optimizer,
strong duality, H_a nonemptiness or finite-norm assertion is presumed.
The paired side notation retains Q_a's normalization. These are
proposed definitions and a question, not a derived certificate.

The possible downstream use is a one-sided bound for Q_a on H_a using
only positivity on the compact rectangle, with the sign and endpoint
applicability to be checked in the separate research step. Even success
would leave T-uniform arithmetic errors, actual-Xi realization and
all-degree signs unresolved. This is an intermediate certificate test,
not a candidate proof of RH or a new zero-free estimate.

First check whether existing witnesses already control every nu in
this family, rather than just L505's two specified densities. Reuse
the previous positive-class assessment for classical functional tools;
inspect its precise qualifications before claiming they apply here.
Search the exact band-limited weighted-L1 and positive-measure
approximation problem and stronger known results, reading primary
theorem hypotheses and essential cases. Do not derive the optimization
or build mathematical scripts during this required literature step.

Continue only if that comparison identifies adequate coverage for one
bounded norm test with the exact quantifiers above. A uniform divergent
lower bound would stop this family; failure of one selected nu would
not. If the family is already covered by a recorded obstruction, record
that overlap rather than rename or repeat the test. An unavailable
essential source does not license a new lemma. This proposal changes
the support geometry and signed functional, but whether that is a
material mathematical distinction is itself still to be assessed.

Essential local inputs: L504 definitions; L505 and L507 as scope
contrasts only unless a later applicability check establishes otherwise.
No cross-notebook result is proposed. Mathlib coverage is unchecked.
No justified creative actual-Xi mechanism follows from this nomination:
an independently verified theta/arithmetic signed-cancellation input
is still missing. Route the next step to literature comparison.

## Completed bounded review, 30 October 2026

The preceding nomination is preserved as the question reviewed, not as
an instruction to repeat its searches. This review used the supplied
overview and DAG and inspected only the relevant local material. No
cross-notebook theorem was read. No lemma or mathematical script was
written, and no proposed estimate below has been derived.

### Duplicate and failure comparison

Read L504's definitions, norm conclusion and the full resonant/smoothed
witness calculation (its proof of (11)--(18)); L505's hypotheses,
conclusion and complete common-sign construction (7)--(15); L507's
hypotheses, conclusion and restriction paragraph. Reused the completed
positive-class residual and signed-gap reviews. Scoped searches in the
30 October detector drafts, assessments and failure records found the
two-height stop, the slow-dilation stop and the explicit warnings that
arbitrary measures had not been excluded. The prior L507 audit history
contains the nomination of this exact finite problem, not its answer.

L504 estimates its envelope error on |x|<=a, 0<=y<=b. L505 estimates
it on |x|<=a, 0<=y<=2b and proves signs of two horizontal integrals.
Their canonical conclusions do not assert a sign for every point on
the paired sides through B. Neither recorded norm lower bound is
therefore an already stated theorem for J_{a,nu}. This is a scope
comparison, not a proof that their functions cannot be adapted.

Any adaptation must control the whole side integral for an arbitrary
finite measure, including endpoint atoms and arbitrarily large mass.
A compact approximation error multiplied by unrestricted mass cannot
be ignored. A future uniform lower bound may use different witnesses
for different measures; a single common witness is sufficient but
not required. The quantified infimum may not be replaced by the norm
for one trial measure. L504's slow-dilation result concerns a different
family and remains stopped. L507's nonexistence result concerns a
harmonic majorant on an unbounded exterior domain, not this infimum;
no extraction of such a majorant is assumed.

### Queries actually made

The bounded searches included:

- `"Paley-Wiener" "positive measures" "extremal" duality`;
- `bandlimited entire function vertical line positive measure norm approximation cosh moment`;
- `"entire functions" "positive" "rectangle" "L1"`;
- `weighted Paley Wiener dual norm complex point evaluation positive measure`;
- `"positive measures" "Laplace transforms" "approximation" "interval"`;
- `"bandlimited" "complex" "measure" "dual norm"`;
- `"Laplace transform" "ratio" "monotonicity" "positive measure"`;
- `"cosh" "log-convex" "integral" measure`;
- `"positive measure" "Laplace" "support" "monotone ratio" theorem`;
- `"positive measures" "approximation" "cosh" norm`;
- `"Paley-Wiener" "boundary measures" "extremal"`;
- `"Laplace transforms" "positive measures" "best approximation"`;
- `"positive measure" "entire functions" "norm" "vertical"`;
- `"cosh" "totally positive" kernel`;
- `"positive exponential sums" approximation lower bound`.

Search results included positive-definite real-axis extremals,
weighted Hilbert-space results, special-function inequalities and
finite exponential fitting. No matching moving-rectangle weighted-L1
functional theorem was identified. Snippets and abstracts were used
only to locate or discard leads, not as theorem evidence.

### Primary theorem comparisons

Brevig, Chirre, Ortega-Cerda and Seip, *Point evaluation in
Paley--Wiener spaces*, [arXiv:2210.13922v2, 1 November 2022](https://arxiv.org/pdf/2210.13922v2#page=15),
Corollary 3.9 and Theorem 3.10, printed pp. 14--15. Reused the parent
review of (3.3)/Theorem 3.6 and retrieved the angular Fourier convention,
distributional matching, full endpoint paragraph and Theorem 3.10
proof. The theorem takes 1<=p<infinity and a normalized PW^p function.
For p=1 its residual norm is a possibly unbounded functional on
Schwartz L1 tests; its proof uses Fourier matching, Holder and density.
This controls origin evaluation, not J_{a,nu}, and has neither the
weight K nor the moving support geometry. No norm estimate or measure
optimization for our target is imported from it.

Goberna and Volle, *Duality for convex infinite optimization on linear
spaces*, [arXiv:2106.14573v1, 28 June 2021](https://arxiv.org/pdf/2106.14573v1#page=8),
Proposition 3.2 and proof, printed pp. 7--8. Reused the parent review
of the real linear-space convex setting, Example 1.2 and the different
duals; reread the strong Slater condition, scalar-supremum proof and
finite-constraint remark. Proposition 3.2 requires one point with all
constraints <=-alpha for one alpha>0. It gives attained sup-duality
and a relaxation limit under that qualification. It does not provide
a positive Borel side measure, its support, its mass or an O_R(a)
bound here. No strong-duality/finite-atomic reduction is asserted.

Sarah May Instanes, *An Optimization Problem and Point-Evaluation in
Paley--Wiener Spaces*, *Constructive Approximation*, published
1 September 2026, [DOI 10.1007/s00365-026-09777-0](https://doi.org/10.1007/s00365-026-09777-0),
Section 1 definitions (1.1)--(1.2), Theorems 1.1--1.3 and their stated
equality cases were inspected in the publisher full text. Its new
optimizations address unweighted origin evaluation for 2<=p<=5 via
separated real sequences. They exclude our p=1 endpoint and do not
optimize vertical measures. Their hypotheses already prevent an
application here, so their later proof cases were not needed or
claimed inspected. This recent lead does not supersede the endpoint
warning or settle the target.

The parent ABR positive-Poisson and L507 growth-source assessments are
reused solely with their recorded domain qualifications. No new
positive harmonic representation is claimed across the signed gap.

### Unread leads and readiness

The total-positivity searches surfaced Pinkus, *Totally Positive
Matrices*, Section 4.2. Publisher/author contents and previews were
located, but a primary passage proving the cosh-kernel claim was not
retrieved. A publisher contents link redirected to a different chapter;
search snippets from third-party copies are not source evidence.
No theorem from this lead is imported, required, or certified read.
Likewise the new Instanes article's references to subsequent p=1
origin extremals and the positive-exponential-fitting leads remain
unread; they are not essential premises of the elementary proposed
test. There is no persistent essential source blocker: calculus,
Fourier inversion, finite-measure integration and the existing L504
class definitions suffice to attempt the stated norm question without
a total-positivity or duality theorem. If a future argument needs an
unread theorem instead, that changed dependency requires review.

The ready continuation is recorded in
`2026-10-30-vertical-side-finite-measure-norm-test.md`. It retains the
same mathematical question and all its quantifiers. It proposes a
bounded finite-frequency/positive-measure separation attempt, with
smooth compact spectra and side-error control as explicit obligations.
This is development of the existing certificate route, not a central
creative actual-Xi mechanism. The latter still lacks independently
justified arithmetic or theta signed-cancellation input. Outcome of
this review is EXPLORATION, not a new negative result or source import;
mathematical exploration usage remains zero. Separate approval of the
new ready continuation belongs to the next invocation.
