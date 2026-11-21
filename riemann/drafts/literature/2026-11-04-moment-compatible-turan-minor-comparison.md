# Moment compatibility and the generic Turan-to-minor bridge — completed comparison

TARGET: Compare known results for factorial-normalized Stieltjes moment sequences with strictly positive Turan iterates at every order, seeking either a theorem forcing D_(5,4)>=0 or an explicit positive-measure entire countermodel.
CHECKED: 2026-11-04
DECISION: EXPLORE
SEARCH_EVIDENCE: Step411 searched exact Stieltjes/factorial-normalized/Turan/Toeplitz and two-atom/cosh/infinite-log-concavity combinations; reused step407 and the L772 audit. Inspected primary statements and relevant proof cases of Wang–Zhu 1612.04114v1, Belton–Guillot–Khare–Putinar 2101.02129v2, Xie–Zhang–Zhang 2610.12237v1 and the cited Karlin–Proschan–Barlow (1961) Theorem3. No matching theorem or countermodel for the combined class was located in this bounded search.
SOURCE_EVIDENCE: Wang–Zhu PDF Theorem2.3 pp.5–6 concerns the opposite operator on raw moments; Belton et al. Theorem1.6 p.5 and its moment proof/Remark2.18 pp.16–18 concern Hirschman–Widder densities and p!-normalized full moments; Karlin et al. Theorem3 p.1027 equates full normalized-moment PF structure with density PF structure; Xie et al. Lemma2.1 p.5 and Corollary2.6 p.8 give conditional local stopping/holomorphic certificates. Relevant proofs, scopes and rendering discrepancies are below.
COMPARISON: Raw moment preservation, a density already having Polya-frequency structure, and a real-zero preserver do not furnish the requested implication under the saved hypotheses. The newly inspected position-dependent criterion offers an independently testable all-order obligation without assuming real zeros. It has not been applied to any moment-compatible negative minor here.
GAP: Neither a sign theorem nor a positive-measure entire all-iterate countermodel is established. A proposed two-atom construction must separately pass an exact negative-minor test and certify all positions and depths, including the zero boundary.
REASON: The comparison supports one bounded construction attempt using explicit atomic moments and a local stopping certificate; it does not support importing a solution to the combined problem or repeating the global-ratio L772 construction.
LITERATURE_REASON: The combined positive-measure hypothesis was outside step407/410 coverage; the new local stopping and holomorphic criterion is a specific relevant lead found during this essential comparison.
SCOPE: Completed literature-only review of the saved target. The separate two-atom continuation assessment is newly prepared and requires its own next-turn approval. No mathematical construction, calculation, lemma or script was performed in step411.

## Completed source comparison — step411

The main gap is actual-Xi all-degree mixed positivity, including exceptional
coefficient signs. The intermediate question adds the positive moment structure
missing from L772 to its all-iterate hypothesis. A sign theorem could supply a
generic bridge; a countermodel would show that even these joint hypotheses leave
actual-theta structure unpaid. Neither outcome would itself prove RH.

### Primary evidence and exact scope

Yi Wang and Bao-Xuan Zhu, [*Log-convex and Stieltjes moment
sequences*](https://arxiv.org/pdf/1612.04114v1), v1, 13 December2016,
PDF Section1 pp.1–3, Lemma2.1/Corollary2.2 p.4, Theorem2.3 and its
complete compound-matrix proof pp.5–6, were read. Their operator is
S(a)_k=a_k a_(k+2)-a_(k+1)^2. The theorem preserves the raw Stieltjes
moment property and yields infinite log-convexity. It does not concern
the negative of this expression on factorial-normalized entries. The proof
uses the adjacent-pair principal submatrix of a second compound Hankel
matrix, and then applies the same argument to the shifted sequence.
The text uses strict positive definiteness and strict inequalities; it
does not justify applying its strict corollary to every finite atomic
measure. No such specialization is imported. The general nonnegative
moment representation, rather than strict Hankel positivity, is the
class in this notebook's question. The regenerated HTML renumbers this
theorem2.4; citations here bind to the versioned PDF's Theorem2.3.

Alexander Belton, Dominique Guillot, Apoorva Khare and Mihai Putinar,
[*Hirschman–Widder densities*](https://arxiv.org/pdf/2101.02129v2),
v2, 9 April2022, Theorem1.6 p.5, Corollary2.13 p.15,
Proposition2.14 pp.15–16, the moment part of the theorem's proof
pp.16–18, and Remark2.18 p.18, were inspected. For m>=2 and
alpha_j>0, their density has moments nu_p=p! h_p(alpha) and full
normalized-moment generating function product_j(1-alpha_j z)^(-1).
The moment proof treats distinct parameters by a Vandermonde expression,
then repeated parameters by continuity; the exponential-sum proof in
Remark2.18 was read too. This is a special density class with a rational
generating function, not an arbitrary positive measure with the question's
entire B. Applying a full-moment result here would require the even
moments of the square-root pushforward and its density hypotheses;
identifying m_n with nu_n while retaining (2n)! is invalid.

The cited original was then retrieved: Samuel Karlin, Frank Proschan and
Richard E. Barlow, [*Moment inequalities of Polya frequency
functions*](https://msp.org/pjm/1961/11-3/pjm-v11-n3-p20-p.pdf),
Pacific J. Math.11(3) (1961),1023–1033, definitions pp.1024–1025,
Theorem3 and both directions of its proof p.1027. For a probability
density on the nonnegative axis with finite integer moments nu_s,
the theorem equates the density being PF_infinity with its zero-extended
full normalized-moment sequence r_s=nu_s/s! being PF_infinity.
The proof identifies the local generating function with the moment
transform, uses the PF product representation, excludes numerator zeros
by positivity of the transform on the negative real axis, and invokes
Schoenberg's characterization; the reverse direction uses that same
representation. No independent audit of those representation theorems
is claimed. Crucially, a positive measure is not the theorem's PF-density
hypothesis, and repeated Turan positivity is not its full Toeplitz
positivity hypothesis. Assuming either missing premise would not justify
the proposed bridge. This original-source check resolves the secondary
lead's scope; it imports no actual-Xi result or arbitrary-atomic analogue.

Matthew H. Y. Xie, Candice X. T. Zhang and Philip B. Zhang,
[*A unified approach to infinite log-concavity of combinatorial
sequences*](https://arxiv.org/pdf/2610.12237v1), v1,8 October2026,
Section2.1 pp.4–5, Lemma2.1 p.5, Lemma2.2 pp.6–7,
Theorem2.3/Corollary2.5 pp.7–8 and Corollary2.6 p.8, including
their complete proofs, were read. On positive fixed half-line support
with zero extension, put c_j(n)=a^[j]_(n-1)a^[j]_(n+1)/(a^[j]_n)^2
and q_*=(3-sqrt(5))/2. Lemma2.1 suffices if each position has a finite
T(n), positivity through T(n), and c_T(n)<=q<=q_*; endpoints have
c=0. Infinite T is permitted only with already known positivity there.
For h_0 holomorphic near a closed radius-R disk, real on its real
diameter, Re h_0>=eta>0 and eta R^2>=128, Corollary2.6 reaches
rho_*=-log q_* at the center by K=0 if eta>=rho_*, otherwise
K=ceil(log_2(2rho_*/eta)), retaining positive real curvature on
nested radii R(3/4)^j. Integer/analytic agreement and required shifts
must still be checked. These are conditional tools, not an application
to the proposed class. No application-specific computer certificate or
Liu–Mao estimate was imported.

### Reuse, duplicates and limits

The step407 assessment supplies the exact Branden real-zero/LP-input
restriction and McNamara–Sagan factor criterion; neither source was
rediscovered or re-proved. L772 and its step410 audit remain the
canonical generic countermodel and finite/universal verification.
L021 supplies M_(2n) and (2n)!; the step407 comparison records the
actual convention a_n=M_(2n)/(8*4^n*(2n)!). No sign transfer between
normalizations is proved in this literature turn; any use must check
constant/geometric rescaling explicitly. L766 is not a premise.
L738 remains only a shape obstruction; it supplies no all-iterate
certificate. The old generic stop is preserved.

Narrow local searches in the indicated same-day coefficient assessments,
countermodel assessments, step407/408 history and the generic-stop
ATTEMPTS file found no earlier two-atom/stopping-time construction or
the new source identifier. No exhaustive duplicate claim is made.
Web searches used "Stieltjes moment" with "infinite log-concavity",
"factorial"/"moment"/"Turan", "Stieltjes moment"/"Polya frequency"/
"factorial", "factorial-normalized", "two atoms", "cosh mixture",
"1/(2n)!" and "Toeplitz". Search snippets and keyword indexes were
used to locate sources only. The de Bruijn–Newman claim, companion-matrix
preprint summaries, and unrelated moment-of-averages papers are unread
leads, not accepted evidence. No access blocker prevents the next test.
One Hirschman–Widder screenshot timed out; the versioned PDF extraction
and complete HTML moment proof supplied the relevant cases instead.

No inspected source forces D_(5,4)>=0 under exactly the proposed joint
hypotheses; this bounded failure to find coverage is not a novelty claim
or evidence that such a theorem cannot exist. Mathlib coverage of the
combined statement and local stopping tools was not checked.

### Decision and bounded discriminator

Prepare one two-atom family test in the separately named assessment.
The new input is position-dependent certification, not more finite
iterate samples. A finite exact screen may select or reject a bounded
parameter grid; only a complete all-index stopping/tail and boundary
argument could turn a survivor into a joint countermodel. Stop this
attempt if the grid has no eligible negative minor, or if its selected
candidate has no certifiable all-order closure within the attempt.
Do not silently expand the grid, infer all orders numerically, or assume
real zeros. A justified creative actual-Xi mechanism is still absent:
even success here only tests a generic bridge. This is an established
certificate-method application, not a creative RH proof attempt.

## Original nomination — retained as pre-step411 history

The proposed class consists of b_n=m_n/(2n)!, where
m_n=integral_[0,infinity) x^n dmu(x) for a finite nonzero positive
measure mu, all b_n>0, and B(z)=sum b_n z^n is entire.
Require L^j(b)_n>0 for every j,n>=0, with zero extension at negative
indices, and use exactly D_(5,4)=det[b_(4+j-i)]_(i,j=0)^4.
Constant and geometric normalizations must be accounted for when
comparing the L021 convention; no normalization transfer is proved
in this nomination. Neither an actual-theta representation nor
strong uniform adjacent ratios are part of the proposed hypothesis.

The independent missing input is positive-measure moment compatibility
combined with an all-order certificate. This is a different class test,
not another audit of L772, a repeat finite Turan scan, or a claim that
moment positivity alone signs a Toeplitz determinant. Retain the
step408 generic stop and L738's shape stop. Reuse step407's inspected
nonlinear-preserver and multiplier statements; do not assume a
preserver's converse or real-rootedness of an unverified input.

One future literature-only turn should inspect exact primary theorem
hypotheses for this combined class and known counterexamples, including
any essential finite/infinite distinction. Its actionable success is
either an applicable cited sign theorem, a source-supported explicit
countermodel, or one bounded construction target with independently
testable moment and all-order obligations. If neither theorem nor
certifiable mechanism is found within that comparison, park this
bridge and record the precise missing obligation. A finite sample of
iterates cannot authorize an all-order claim. A theorem assuming the
desired real-zero property does not close the gap.

This review has not been performed. No creative proof attempt is
ready: it would first need a source-assessed way to certify both
properties without assuming the exceptional sign. If a genuinely
new central mechanism emerges, nominate it with a bounded
discriminator and the required creative escalation in a later turn.
Mathlib coverage of the combined class is not checked.
